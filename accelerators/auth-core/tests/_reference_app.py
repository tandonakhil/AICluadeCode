"""A minimal reference FastAPI app wiring `src/`'s primitives together.

This file is test-only scaffolding, NOT part of the accelerator's declared
contract (H1) -- it exists so this suite can exercise `auth.py`/
`sessions.py`/`security_tokens.py`/`totp.py` end-to-end without importing
any host project's domain modules (H3: host decoupling, proven). An
adopting project writes its own routes file; this is a reference shape
only, using a generic two-tenant, two-role schema (`tenant_id` /
`owner`|`member`) instead of little-milestones' `family_id` /
`owner`|`caregiver`, to prove the `PrincipalResolver` seam genuinely
generalizes.

A synthetic `/items` resource (tenant-scoped, owner-only delete) stands in
for whatever protected resource an adopting project actually has -- it
exists purely so authz-boundary tests (cross-tenant 404, role 403) have
something to assert against.
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from pydantic import BaseModel, field_validator

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.auth import (  # noqa: E402
    DUMMY_PASSWORD_HASH,
    MAX_TOTP_ATTEMPTS,
    Principal,
    check_rate_limit,
    clear_mfa_pending,
    clear_session_cookie,
    client_ip,
    create_session,
    delete_session_by_raw_token,
    destroy_session_by_token_hash,
    generate_opaque_token,
    get_current_session_user,
    get_db,
    get_pending_session,
    hash_password,
    hash_token,
    is_mobile_client,
    issue_session_token,
    record_totp_failure,
    require_role,
    reset_totp_failures,
    verify_password,
    _extract_raw_token,  # noqa: F401  (imported for test access)
)
from src.security_tokens import (  # noqa: E402
    RECOVERY_CODE_COUNT,
    PasswordResetTokenStore,
    RecoveryCodeStore,
)
from src.sessions import SessionInfo, SessionStore  # noqa: E402
from src.totp import (  # noqa: E402
    decrypt_secret,
    encrypt_secret,
    generate_recovery_codes,
    generate_totp_secret,
    hash_recovery_code,
    provisioning_uri,
    verify_recovery_code,
    verify_totp_code,
)

LOGIN_MAX_ATTEMPTS = 10
LOGIN_WINDOW_SECONDS = 15 * 60
MIN_PASSWORD_LENGTH = 8


# Request/response models live at MODULE scope, not nested inside
# build_app(). This file uses `from __future__ import annotations`
# (postponed evaluation), which turns every annotation into a string;
# FastAPI/Pydantic resolve a route handler's parameter annotations via
# typing.get_type_hints() against the function's *module* globals, not its
# enclosing closure. A model class nested inside build_app() is invisible to
# that lookup, so FastAPI silently falls back to treating `data: SignupRequest`
# as a query parameter named "data" -- passing a real JSON body then 422s
# with "field required: query.data". Caught by actually running this suite,
# not by the STATIC ONLY review that first shipped it.
class SignupRequest(BaseModel):
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def _len(cls, v: str) -> str:
        if len(v) < MIN_PASSWORD_LENGTH:
            raise ValueError("too short")
        return v


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResult(BaseModel):
    mfa_required: bool = False
    user: Optional[dict] = None
    recovery_codes_remaining: Optional[int] = None


class TotpLoginRequest(BaseModel):
    code: str


class TotpSetupRequest(BaseModel):
    password: str


class TotpVerifyRequest(BaseModel):
    code: str


class TotpDisableRequest(BaseModel):
    password: str
    code: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str


class ResetRequestRequest(BaseModel):
    email: str


class ResetConfirmRequest(BaseModel):
    token: str
    new_password: str


class _Resolver:
    tenant_field = "tenant_id"
    roles = frozenset({"owner", "member"})
    principal_table = "users"


resolver = _Resolver()
get_principal = get_current_session_user(resolver)
get_pending = get_pending_session(resolver)
require_owner_dep = require_role(get_principal, "owner")


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE tenants (id INTEGER PRIMARY KEY AUTOINCREMENT);
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            tenant_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            totp_secret_enc TEXT,
            totp_verified_at TEXT
        );
        CREATE TABLE sessions (
            token_hash TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            id TEXT,
            mfa_pending INTEGER NOT NULL DEFAULT 0,
            last_seen_at TEXT,
            client TEXT NOT NULL DEFAULT 'web'
        );
        CREATE TABLE password_reset_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token_hash TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            used_at TEXT
        );
        CREATE TABLE recovery_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            code_hash TEXT NOT NULL,
            used_at TEXT
        );
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL
        );
        """
    )
    conn.commit()


def build_app(conn: sqlite3.Connection) -> FastAPI:
    app = FastAPI()

    # `get_current_session_user`/`get_pending_session` (src/auth.py) resolve
    # their own connection via `Depends(get_db)`, and `get_db()`'s real body
    # does `from app.db import get_connection` -- a deliberate placeholder an
    # adopting project overrides with its own connection factory (H2:
    # sqlite3.Connection is a FORK POINT). This reference app must override
    # the SAME dependency object FastAPI sees, or `Depends(get_db)` falls
    # through to that placeholder import at request time. Left unoverridden,
    # this doesn't fail loudly -- in an environment where some unrelated
    # `app` package happens to be importable (e.g. another Conclave project's
    # own `app.db` sitting on sys.path via an editable install in a borrowed
    # venv), it silently resolves and connects to THAT project's real
    # database instead, producing confusing schema-mismatch errors far from
    # the actual cause. Caught by actually executing this suite, not by the
    # STATIC ONLY review that first shipped it.
    def _get_db_override():
        yield conn

    app.dependency_overrides[get_db] = _get_db_override

    def _user_public(row: sqlite3.Row) -> dict:
        return {
            "id": row["id"],
            "email": row["email"],
            "tenant_id": row["tenant_id"],
            "role": row["role"],
            "totp_enabled": row["totp_verified_at"] is not None,
        }

    def _session_store():
        return SessionStore(conn)

    def _reset_store():
        return PasswordResetTokenStore(conn)

    def _recovery_store():
        return RecoveryCodeStore(conn)

    @app.post("/auth/signup", status_code=status.HTTP_201_CREATED)
    def signup(data: SignupRequest, request: Request, response: Response):
        existing = conn.execute("SELECT id FROM users WHERE email = ?", (data.email,)).fetchone()
        if existing is not None:
            raise HTTPException(status_code=409, detail="exists")
        cur = conn.execute("INSERT INTO tenants DEFAULT VALUES")
        conn.commit()
        tenant_id = cur.lastrowid
        cur = conn.execute(
            "INSERT INTO users (email, password_hash, tenant_id, role) VALUES (?, ?, ?, 'owner')",
            (data.email, hash_password(data.password), tenant_id),
        )
        conn.commit()
        row = conn.execute("SELECT * FROM users WHERE id = ?", (cur.lastrowid,)).fetchone()
        token = create_session(
            conn, row["id"], client=("mobile" if is_mobile_client(request) else "web")
        )
        issue_session_token(response, token, request)
        return _user_public(row)

    @app.post("/auth/join", status_code=status.HTTP_201_CREATED)
    def join(data: SignupRequest, tenant_id: int, request: Request, response: Response):
        """Test-only shortcut standing in for an invite flow: joins an
        existing tenant as `role=member`."""
        existing = conn.execute("SELECT id FROM users WHERE email = ?", (data.email,)).fetchone()
        if existing is not None:
            raise HTTPException(status_code=409, detail="exists")
        cur = conn.execute(
            "INSERT INTO users (email, password_hash, tenant_id, role) VALUES (?, ?, ?, 'member')",
            (data.email, hash_password(data.password), tenant_id),
        )
        conn.commit()
        row = conn.execute("SELECT * FROM users WHERE id = ?", (cur.lastrowid,)).fetchone()
        token = create_session(
            conn, row["id"], client=("mobile" if is_mobile_client(request) else "web")
        )
        issue_session_token(response, token, request)
        return _user_public(row)

    @app.post("/auth/login", response_model=LoginResult)
    def login(data: LoginRequest, request: Request, response: Response):
        rate_key = f"login:{client_ip(request)}:{data.email.strip().lower()}"
        if not check_rate_limit(rate_key, LOGIN_MAX_ATTEMPTS, LOGIN_WINDOW_SECONDS):
            raise HTTPException(status_code=429, detail="rate limited")
        row = conn.execute("SELECT * FROM users WHERE email = ?", (data.email,)).fetchone()
        password_hash = row["password_hash"] if row is not None else DUMMY_PASSWORD_HASH
        # Constant-cost enumeration resistance: verify_password runs even
        # when `row is None`, against DUMMY_PASSWORD_HASH.
        password_ok = verify_password(data.password, password_hash)
        if row is None or not password_ok:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        if row["totp_verified_at"] is not None:
            token = create_session(
                conn, row["id"], mfa_pending=True,
                client=("mobile" if is_mobile_client(request) else "web"),
            )
            issue_session_token(response, token, request)
            return LoginResult(mfa_required=True)
        token = create_session(
            conn, row["id"], client=("mobile" if is_mobile_client(request) else "web")
        )
        issue_session_token(response, token, request)
        return LoginResult(user=_user_public(row))

    @app.post("/auth/totp/login", response_model=LoginResult)
    def totp_login(
        data: TotpLoginRequest,
        pending=Depends(get_pending),
        recovery_store: RecoveryCodeStore = Depends(_recovery_store),
    ):
        auth_row = conn.execute(
            "SELECT * FROM users WHERE id = ?", (pending.user_id,)
        ).fetchone()
        if auth_row is None:
            raise HTTPException(status_code=401, detail="not authenticated")
        code = (data.code or "").strip()
        ok = False
        recovery_codes_remaining = None
        if auth_row["totp_secret_enc"] and code and "-" not in code and code.isdigit():
            ok = verify_totp_code(decrypt_secret(auth_row["totp_secret_enc"]), code)
        if not ok and code:
            for row in recovery_store.unused_for_user(pending.user_id):
                if verify_recovery_code(code, row["code_hash"]):
                    recovery_store.mark_used(row["id"])
                    ok = True
                    recovery_codes_remaining = recovery_store.unused_count(pending.user_id)
                    break
        if not ok:
            attempts = record_totp_failure(pending.token_hash)
            if attempts >= MAX_TOTP_ATTEMPTS:
                destroy_session_by_token_hash(conn, pending.token_hash)
                reset_totp_failures(pending.token_hash)
                raise HTTPException(status_code=401, detail="too many attempts")
            raise HTTPException(status_code=401, detail="wrong code")
        reset_totp_failures(pending.token_hash)
        clear_mfa_pending(conn, pending.token_hash)
        user = conn.execute("SELECT * FROM users WHERE id = ?", (pending.user_id,)).fetchone()
        return LoginResult(
            user=_user_public(user), recovery_codes_remaining=recovery_codes_remaining
        )

    @app.post("/auth/logout")
    def logout(request: Request, response: Response):
        raw_token = _extract_raw_token(request)
        if raw_token:
            delete_session_by_raw_token(conn, raw_token)
        clear_session_cookie(response)
        return {"logged_out": True}

    @app.get("/auth/me")
    def get_me(principal: Principal = Depends(get_principal)):
        row = conn.execute("SELECT * FROM users WHERE id = ?", (principal.id,)).fetchone()
        return _user_public(row)

    @app.post("/auth/totp/setup")
    def totp_setup(data: TotpSetupRequest, principal: Principal = Depends(get_principal)):
        row = conn.execute("SELECT * FROM users WHERE id = ?", (principal.id,)).fetchone()
        if not verify_password(data.password, row["password_hash"]):
            raise HTTPException(status_code=401, detail="wrong password")
        raw_secret = generate_totp_secret()
        conn.execute(
            "UPDATE users SET totp_secret_enc = ?, totp_verified_at = NULL WHERE id = ?",
            (encrypt_secret(raw_secret), principal.id),
        )
        conn.commit()
        return {
            "provisioning_uri": provisioning_uri(raw_secret, principal.email),
            "secret": raw_secret,
        }

    @app.post("/auth/totp/verify")
    def totp_verify(
        data: TotpVerifyRequest,
        principal: Principal = Depends(get_principal),
        recovery_store: RecoveryCodeStore = Depends(_recovery_store),
    ):
        row = conn.execute("SELECT * FROM users WHERE id = ?", (principal.id,)).fetchone()
        if not row["totp_secret_enc"]:
            raise HTTPException(status_code=400, detail="no setup in progress")
        if not verify_totp_code(decrypt_secret(row["totp_secret_enc"]), data.code):
            raise HTTPException(status_code=401, detail="bad code")
        conn.execute(
            "UPDATE users SET totp_verified_at = datetime('now') WHERE id = ?", (principal.id,)
        )
        conn.commit()
        codes = generate_recovery_codes(RECOVERY_CODE_COUNT)
        recovery_store.create_batch(principal.id, [hash_recovery_code(c) for c in codes])
        return {"recovery_codes": codes}

    @app.post("/auth/totp/disable")
    def totp_disable(
        data: TotpDisableRequest,
        principal: Principal = Depends(get_principal),
        recovery_store: RecoveryCodeStore = Depends(_recovery_store),
    ):
        row = conn.execute("SELECT * FROM users WHERE id = ?", (principal.id,)).fetchone()
        if not verify_password(data.password, row["password_hash"]):
            raise HTTPException(status_code=401, detail="wrong password")
        if not row["totp_secret_enc"] or not row["totp_verified_at"]:
            raise HTTPException(status_code=400, detail="not enabled")
        code = (data.code or "").strip()
        ok = verify_totp_code(decrypt_secret(row["totp_secret_enc"]), code) if code else False
        if not ok and code:
            for r in recovery_store.unused_for_user(principal.id):
                if verify_recovery_code(code, r["code_hash"]):
                    ok = True
                    break
        if not ok:
            raise HTTPException(status_code=401, detail="bad code")
        conn.execute(
            "UPDATE users SET totp_secret_enc = NULL, totp_verified_at = NULL WHERE id = ?",
            (principal.id,),
        )
        conn.commit()
        recovery_store.delete_all_for_user(principal.id)
        return {"disabled": True}

    @app.post("/auth/password")
    def change_password(
        data: ChangePasswordRequest,
        principal: Principal = Depends(get_principal),
        session_store: SessionStore = Depends(_session_store),
    ):
        row = conn.execute("SELECT * FROM users WHERE id = ?", (principal.id,)).fetchone()
        if not verify_password(data.current_password, row["password_hash"]):
            raise HTTPException(status_code=401, detail="wrong password")
        conn.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (hash_password(data.new_password), principal.id),
        )
        conn.commit()
        session_store.delete_all_for_user(principal.id, except_id=principal.session_id)
        return {"changed": True}

    @app.post("/auth/password-reset/request", status_code=status.HTTP_202_ACCEPTED)
    def reset_request(
        data: ResetRequestRequest,
        request: Request,
        token_store: PasswordResetTokenStore = Depends(_reset_store),
    ):
        rate_key = f"reset:{data.email}"
        allowed = check_rate_limit(rate_key, 3, 3600)
        if allowed:
            row = conn.execute("SELECT id FROM users WHERE email = ?", (data.email,)).fetchone()
            if row is not None:
                raw_token = generate_opaque_token()
                token_store.create(row["id"], hash_token(raw_token))
        return {"detail": "generic"}

    @app.post("/auth/password-reset/confirm")
    def reset_confirm(
        data: ResetConfirmRequest,
        token_store: PasswordResetTokenStore = Depends(_reset_store),
        session_store: SessionStore = Depends(_session_store),
    ):
        token = token_store.get_valid_by_token_hash(hash_token(data.token))
        if token is None:
            raise HTTPException(status_code=400, detail="invalid")
        conn.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (hash_password(data.new_password), token.user_id),
        )
        conn.commit()
        token_store.mark_used(token.id)
        session_store.delete_all_for_user(token.user_id)
        row = conn.execute("SELECT * FROM users WHERE id = ?", (token.user_id,)).fetchone()
        return _user_public(row)

    @app.get("/auth/sessions")
    def list_sessions(
        principal: Principal = Depends(get_principal),
        session_store: SessionStore = Depends(_session_store),
    ):
        return session_store.list_for_user(principal.id, current_session_id=principal.session_id)

    @app.delete("/auth/sessions/{session_id}")
    def revoke_session(
        session_id: str,
        principal: Principal = Depends(get_principal),
        session_store: SessionStore = Depends(_session_store),
    ):
        if not session_store.delete(session_id, principal.id):
            raise HTTPException(status_code=404, detail="not found")
        return {"deleted": True}

    @app.post("/auth/sessions/revoke-others")
    def revoke_others(
        principal: Principal = Depends(get_principal),
        session_store: SessionStore = Depends(_session_store),
    ):
        session_store.delete_all_for_user(principal.id, except_id=principal.session_id)
        return {"revoked": True}

    # --- synthetic protected resource, for authz-boundary tests only -------

    @app.post("/items", status_code=status.HTTP_201_CREATED)
    def create_item(principal: Principal = Depends(get_principal)):
        cur = conn.execute("INSERT INTO items (tenant_id) VALUES (?)", (principal.tenant_id,))
        conn.commit()
        return {"id": cur.lastrowid, "tenant_id": principal.tenant_id}

    @app.get("/items/{item_id}")
    def get_item(item_id: int, principal: Principal = Depends(get_principal)):
        row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        if row is None or row["tenant_id"] != principal.tenant_id:
            raise HTTPException(status_code=404, detail="not found")
        return {"id": row["id"], "tenant_id": row["tenant_id"]}

    @app.delete("/items/{item_id}")
    def delete_item(
        item_id: int,
        principal: Principal = Depends(require_owner_dep),
    ):
        row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
        if row is None or row["tenant_id"] != principal.tenant_id:
            raise HTTPException(status_code=404, detail="not found")
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        return {"deleted": True}

    return app
