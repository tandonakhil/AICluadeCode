"""Core session/password authentication -- argon2id passwords, opaque
SHA-256-hashed session tokens, sliding+absolute expiry, TOTP-pending-session
gating, dual-transport (cookie + mobile Bearer) reads, in-process rate
limiting.

Harvested from `little-milestones/dev/backend/app/auth.py` (F10 Increment 3,
hardened by F12 Increment 6 and the F18 mobile increment). See
`accelerators/auth-core/ACCELERATOR.md` for the full contract, H2 config
table, and the security-architect co-sign conditions this file implements.

--- Tenancy genericization (accelerator-specific, not in the source) -------

The source project is single-tenant-model "family" scoped: every session
row resolves to a `family_id`. A generic accelerator cannot hardcode a
tenant column name or a principal table name, so this module resolves
principals through a small `PrincipalResolver` Protocol the adopting
project implements once (see `PrincipalResolver` below and H2's config
table in ACCELERATOR.md). If your project has no tenant concept at all,
implement a resolver with `tenant_field = None` -- `Principal.tenant_id`
will simply be `None` on every request.
"""

from __future__ import annotations

import hashlib
import os
import secrets
import sqlite3
import time
import uuid
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional, Protocol

from fastapi import Depends, HTTPException, Request, Response
from passlib.context import CryptContext
from pydantic import BaseModel

# argon2id specifically (not bcrypt): current OWASP-recommended default.
# Exported so an adopting project's totp.py (or any other password-class
# secret) reuses this exact CryptContext rather than constructing a second
# one with different tuning -- see ACCELERATOR.md item 8(a).
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# A fixed, never-valid hash used to run verify_password() against an
# unknown email so login's timing profile for "no such user" and "wrong
# password" stays close to identical (constant-cost enumeration
# resistance -- see ACCELERATOR.md item 8(d) for the test-pack gap this
# behaviour has today).
DUMMY_PASSWORD_HASH = pwd_context.hash("not-a-real-password-marker")

SESSION_COOKIE_NAME = "session"

# --- Native-client / mobile Bearer transport --------------------------------
#
# The web app authenticates with the httpOnly session cookie. A native
# client has no browser cookie jar, and Secure/SameSite semantics don't map
# onto it, so the SAME session token is also accepted from an
# `Authorization: Bearer` header. One token, one `sessions` table, one
# validation path -- only the read point differs.
#
# Cookie is read FIRST and wins on conflict, so no browser request's
# resolution can change. Bearer is non-ambient, so the new path is
# inherently CSRF-immune.
CLIENT_HEADER = "X-LM-Client"
MOBILE_CLIENT = "mobile"
SESSION_TOKEN_HEADER = "X-LM-Session-Token"


def is_mobile_client(request: Request) -> bool:
    """True when the caller identified itself as the native app."""
    return request.headers.get(CLIENT_HEADER, "").strip().lower() == MOBILE_CLIENT


def _extract_raw_token(request: Request) -> Optional[str]:
    """Session token from the cookie (web) or the Bearer header (native).

    Cookie first -- a browser request resolves exactly as it did before this
    existed. The Authorization value is a credential: never log it.
    """
    cookie_token = request.cookies.get(SESSION_COOKIE_NAME)
    if cookie_token:
        return cookie_token
    header = request.headers.get("Authorization", "")
    scheme, _, value = header.partition(" ")
    if scheme.lower() == "bearer" and value.strip():
        return value.strip()
    return None


SESSION_SLIDING_DAYS = 30
SESSION_ABSOLUTE_DAYS = 90


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


def hash_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()


def generate_opaque_token() -> str:
    """`secrets.token_urlsafe(32)` -- 256 bits raw entropy, the same
    primitive to reuse for every other high-entropy token (invite codes,
    reset tokens, unsubscribe tokens) in an adopting project."""
    return secrets.token_urlsafe(32)


def get_db() -> sqlite3.Connection:
    """FastAPI dependency yielding a request-scoped connection. Replace
    `get_connection` with your project's own connection factory -- this
    accelerator is SQLite-only (see ACCELERATOR.md H2: `sqlite3.Connection`
    is a FORK POINT, not configurable)."""
    from app.db import get_connection  # adopting project supplies this

    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()


# --- Tenancy / principal resolution seam ------------------------------------


@dataclass(frozen=True)
class Principal:
    """The generic authenticated caller. Deliberately minimal -- an
    adopting project's own app-specific claims (e.g. little-milestones'
    `digest_opt_in`) do NOT belong here; look them up from `id` in your own
    store if a route needs them. Keeping this generic is what lets one
    session-resolution code path serve any host schema."""

    id: int
    email: str
    role: str
    tenant_id: Optional[int]
    session_id: str


class PrincipalResolver(Protocol):
    """Implemented once by the adopting project, supplied as a FastAPI
    dependency override. This is the entire seam that replaces
    little-milestones' hardcoded `users`/`family_id` JOIN.

    `tenant_field`: the column on your principal table that scopes a user to
    a tenant (e.g. `"family_id"`, `"org_id"`, `"account_id"`). Set to `None`
    for a single-tenant project -- `Principal.tenant_id` is then always
    `None` and no tenant column is queried.

    `roles`: the full set of valid role strings your project uses (e.g.
    `frozenset({"owner", "caregiver"})` or `frozenset({"admin", "member"})`).
    Used only for validation in `require_role`; this module never
    special-cases a role name.

    `principal_table`: the table holding your user rows, joined against
    `sessions.user_id = <principal_table>.id`. Must have at least `id`,
    `email`, `role` columns, plus `tenant_field` if set.
    """

    tenant_field: Optional[str]
    roles: frozenset[str]
    principal_table: str


def _session_select_sql(resolver: PrincipalResolver) -> str:
    tenant_col = (
        f", {resolver.principal_table}.{resolver.tenant_field} AS tenant_id"
        if resolver.tenant_field
        else ", NULL AS tenant_id"
    )
    return f"""
        SELECT sessions.token_hash AS token_hash, sessions.created_at AS session_created_at,
               sessions.expires_at AS expires_at, sessions.id AS session_id,
               sessions.mfa_pending AS mfa_pending,
               {resolver.principal_table}.id AS user_id, {resolver.principal_table}.email AS email,
               {resolver.principal_table}.role AS role
               {tenant_col}
        FROM sessions
        JOIN {resolver.principal_table} ON {resolver.principal_table}.id = sessions.user_id
        WHERE sessions.token_hash = ?
    """


# --- Sessions ------------------------------------------------------------


def create_session(
    conn: sqlite3.Connection,
    user_id: int,
    mfa_pending: bool = False,
    client: str = "web",
) -> str:
    """Returns the raw token (embedded in the Set-Cookie response) -- only
    its SHA-256 hash is ever persisted.

    `mfa_pending=True`: used for an enrolled user's login -- the resulting
    session row is real (has an id, is cookie-carried) but
    `get_current_session_user` rejects it on every route except the
    adopting project's own TOTP-code-entry route, until that route clears
    the flag via `clear_mfa_pending`. Pending sessions carry a 5-minute
    expiry regardless of the normal 30-day sliding window (enforced by
    `_resolve_session_row`).
    """
    raw_token = generate_opaque_token()
    token_hash = hash_token(raw_token)
    session_id = uuid.uuid4().hex
    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(days=SESSION_SLIDING_DAYS)
    conn.execute(
        "INSERT INTO sessions (token_hash, user_id, created_at, expires_at, id, mfa_pending, last_seen_at, client) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            token_hash,
            user_id,
            now.isoformat(),
            expires_at.isoformat(),
            session_id,
            int(mfa_pending),
            now.isoformat(),
            client,
        ),
    )
    conn.commit()
    return raw_token


def delete_session_by_raw_token(conn: sqlite3.Connection, raw_token: str) -> None:
    """Logout: a real server-side row delete, not just a client-side cookie
    clear -- a stolen cookie must not remain valid after logout."""
    conn.execute("DELETE FROM sessions WHERE token_hash = ?", (hash_token(raw_token),))
    conn.commit()


def _parse_iso(value: str) -> datetime:
    dt = datetime.fromisoformat(value)
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


# "Pending sessions expire after 5 minutes regardless" of the normal 30-day
# sliding window -- the primary bound on how long a mfa_pending row can be
# probed against.
TOTP_PENDING_SESSION_MINUTES = 5


def _resolve_session_row(
    conn: sqlite3.Connection,
    raw_token: str,
    resolver: PrincipalResolver,
    allow_pending: bool = False,
) -> Optional[sqlite3.Row]:
    """`allow_pending=False` (the default, used by every ordinary
    authenticated route): a `mfa_pending` session resolves to None (401).
    `allow_pending=True` is used only by the TOTP-code-entry route's own
    resolution path."""
    token_hash = hash_token(raw_token)
    row = conn.execute(_session_select_sql(resolver), (token_hash,)).fetchone()
    if row is None:
        return None

    is_pending = bool(row["mfa_pending"])
    if is_pending:
        created_at = _parse_iso(row["session_created_at"])
        if datetime.now(timezone.utc) > created_at + timedelta(
            minutes=TOTP_PENDING_SESSION_MINUTES
        ):
            conn.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash,))
            conn.commit()
            return None
        if not allow_pending:
            return None
        return row

    expires_at = _parse_iso(row["expires_at"])
    if expires_at < datetime.now(timezone.utc):
        conn.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash,))
        conn.commit()
        return None

    # Sliding expiry, capped at the absolute cap from the session's own
    # creation time -- a boundary burst of activity cannot extend a session
    # past 90 days from creation.
    created_at = _parse_iso(row["session_created_at"])
    absolute_cap = created_at + timedelta(days=SESSION_ABSOLUTE_DAYS)
    new_expiry = min(
        datetime.now(timezone.utc) + timedelta(days=SESSION_SLIDING_DAYS), absolute_cap
    )
    conn.execute(
        "UPDATE sessions SET expires_at = ?, last_seen_at = ? WHERE token_hash = ?",
        (new_expiry.isoformat(), datetime.now(timezone.utc).isoformat(), token_hash),
    )
    conn.commit()
    return row


def get_current_session_user(resolver: PrincipalResolver):
    """Returns a FastAPI dependency callable bound to your resolver. Wire it
    once per app: `get_principal = get_current_session_user(my_resolver)`,
    then `Depends(get_principal)` everywhere a route needs the caller."""

    def _dep(request: Request, conn: sqlite3.Connection = Depends(get_db)) -> Principal:
        raw_token = _extract_raw_token(request)
        if not raw_token:
            raise HTTPException(status_code=401, detail="Not authenticated")
        row = _resolve_session_row(conn, raw_token, resolver, allow_pending=False)
        if row is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        return Principal(
            id=row["user_id"],
            email=row["email"],
            role=row["role"],
            tenant_id=row["tenant_id"],
            session_id=row["session_id"],
        )

    return _dep


class PendingSession(BaseModel):
    """Resolved only by the TOTP-code-entry step -- the one route a
    `mfa_pending` session is allowed to reach."""

    user_id: int
    token_hash: str


def get_pending_session(resolver: PrincipalResolver):
    def _dep(request: Request, conn: sqlite3.Connection = Depends(get_db)) -> PendingSession:
        raw_token = _extract_raw_token(request)
        if not raw_token:
            raise HTTPException(status_code=401, detail="Not authenticated")
        row = _resolve_session_row(conn, raw_token, resolver, allow_pending=True)
        if row is None or not bool(row["mfa_pending"]):
            raise HTTPException(status_code=401, detail="Not authenticated")
        return PendingSession(user_id=row["user_id"], token_hash=row["token_hash"])

    return _dep


def clear_mfa_pending(conn: sqlite3.Connection, token_hash: str) -> None:
    """Completes a TOTP (or recovery-code) login: the pending session
    becomes a normal one, with a freshly-issued normal expiry."""
    now = datetime.now(timezone.utc)
    new_expiry = now + timedelta(days=SESSION_SLIDING_DAYS)
    conn.execute(
        "UPDATE sessions SET mfa_pending = 0, created_at = ?, expires_at = ?, last_seen_at = ? "
        "WHERE token_hash = ?",
        (now.isoformat(), new_expiry.isoformat(), now.isoformat(), token_hash),
    )
    conn.commit()


def destroy_session_by_token_hash(conn: sqlite3.Connection, token_hash: str) -> None:
    """Used by "5 failed TOTP attempts destroy the pending session" -- keyed
    by hash (already in hand from `PendingSession`), not the raw token."""
    conn.execute("DELETE FROM sessions WHERE token_hash = ?", (token_hash,))
    conn.commit()


def require_role(get_principal, *allowed: str):
    """Factory replacing little-milestones' hardcoded `require_owner`.
    Takes the SAME principal-dependency callable you got back from
    `get_current_session_user(resolver)`, so it can declare it as its own
    sub-dependency (`Depends` needs a concrete default to resolve
    `Principal` from -- it cannot be injected positionally). Use as
    `Depends(require_role(get_principal, "owner"))` -- a
    legitimate-session-but-wrong-role request gets 403 (not 404, which
    should be reserved for cross-tenant access, per H2)."""

    def _dep(principal: Principal = Depends(get_principal)) -> Principal:
        if principal.role not in allowed:
            raise HTTPException(status_code=403, detail="Insufficient role")
        return principal

    return _dep


def issue_session_token(response: Response, raw_token: str, request: Request) -> None:
    """Hand the session token to the client in the right transport.

    Native (`X-LM-Client: mobile`): returned in the `X-LM-Session-Token`
    response header and **no `Set-Cookie` is sent**. Suppressing the cookie
    is not cosmetic -- the platform cookie jar (NSURLSession/OkHttp) is
    unencrypted and inside the default backup set, so emitting it anyway
    would leave a second plaintext copy of a long-lived credential on disk.

    Header rather than response body, so adding mobile support never
    requires changing an existing `response_model` the web frontend parses.

    SECURITY INVARIANT: `X-LM-Session-Token` must NEVER be added to CORS
    `expose_headers` -- unreadable to cross-origin JS is a deliberate
    fail-safe. See ACCELERATOR.md H2's config table, item 8(b).
    """
    if is_mobile_client(request):
        response.headers[SESSION_TOKEN_HEADER] = raw_token
        return
    set_session_cookie(response, raw_token)


def set_session_cookie(response: Response, raw_token: str) -> None:
    secure = os.environ.get("ENV") == "production"
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=raw_token,
        httponly=True,
        samesite="lax",
        secure=secure,
        max_age=SESSION_SLIDING_DAYS * 24 * 3600,
        path="/",
    )


def clear_session_cookie(response: Response) -> None:
    response.delete_cookie(SESSION_COOKIE_NAME, path="/")


def client_ip(request: Request) -> str:
    return request.client.host if request.client else "unknown"


# --- TOTP pending-login failure tracking ------------------------------------
#
# "5 failed attempts destroy the pending session (fresh password login
# required)" -- this, not the rate limiter below, is the primary 6-digit
# brute-force control.
#
# ****************************************************************************
# PRECONDITION: SINGLE-PROCESS DEPLOYMENT ONLY.
# ****************************************************************************
# `_TOTP_FAILURE_COUNTS` is a Python module-level `dict` -- in-process,
# non-shared state. Correct and sufficient for a single-process local
# deploy. SILENTLY WRONG -- not degraded, silently bypassable -- under any
# multi-worker/multi-process deployment: a TOTP brute-force attempt landing
# on a fresh worker process resets its own 5-attempt counter to zero, so an
# attacker who can land requests across N workers gets N times the stated
# attempt budget with no error, no log line, and no visible symptom.
#
# REVISIT TRIGGER -- mandatory, before, not after: more than one worker
# process; behind a load balancer fronting more than one instance; any move
# off a single always-on process (serverless/autoscaled compute). At that
# point this moves to a shared store (Redis or equivalent) before the
# deploy, not after. See ACCELERATOR.md's own labeled subsection for the
# full statement (security-architect co-sign item 3).

MAX_TOTP_ATTEMPTS = 5
_TOTP_FAILURE_COUNTS: dict[str, int] = defaultdict(int)


def record_totp_failure(token_hash: str) -> int:
    _TOTP_FAILURE_COUNTS[token_hash] += 1
    return _TOTP_FAILURE_COUNTS[token_hash]


def reset_totp_failures(token_hash: str) -> None:
    _TOTP_FAILURE_COUNTS.pop(token_hash, None)


# --- Rate limiting -----------------------------------------------------------
#
# In-process sliding-window counter, no external dependency -- a sliding
# list of timestamps within the window, not a literal fixed clock-aligned
# window, so a burst right at a window boundary can't double the effective
# limit.
#
# ****************************************************************************
# PRECONDITION: SINGLE-PROCESS DEPLOYMENT ONLY -- same statement as above.
# ****************************************************************************
# `_RATE_BUCKETS` is also a module-level `dict`. Correct and sufficient for
# a single-process local deploy. SILENTLY WRONG under any multi-worker
# deployment: each process gets its own counters, so an attacker distributed
# across workers gets N times the stated limit, with no error and no
# visible symptom. Same revisit trigger as `_TOTP_FAILURE_COUNTS` above.

_RATE_BUCKETS: dict[str, list[float]] = defaultdict(list)


def check_rate_limit(key: str, max_requests: int, window_seconds: int) -> bool:
    """Returns True if the request is allowed (and records it), False if
    the caller should be rejected (429). Callers choose the key shape --
    e.g. IP+email for login, IP alone for join/reset-request."""
    now = time.monotonic()
    bucket = _RATE_BUCKETS[key]
    cutoff = now - window_seconds
    while bucket and bucket[0] < cutoff:
        bucket.pop(0)
    if len(bucket) >= max_requests:
        return False
    bucket.append(now)
    return True


def reset_rate_limits() -> None:
    """Test-only helper -- rate-limit state is process-global and would
    otherwise leak between test cases."""
    _RATE_BUCKETS.clear()
    _TOTP_FAILURE_COUNTS.clear()
