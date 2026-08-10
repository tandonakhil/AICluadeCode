# `auth-core` — Auth, session and mobile token-store core

**Version:** 1.0.0 · **Status:** built · **Origin:** `little-milestones`
(F10 Increment 3, F12 Increment 6, F18 mobile increment) · **Admission:**
H1–H10, all satisfied · **H9 co-sign:** security-architect, **2026-08-09,
conditional** — all eight items below incorporated in this harvest.

Harvested and written by `mas-registrar` under
`admin/proposals/2026-08-08-accelerator-layer.md` and
`accelerators/ADMISSION.md`, per the human's per-item approval 2026-08-08.

---

## H1 · Declared contract

The public surface an adopting project may depend on. Anything not listed
here is private and may change in a MINOR release without notice.

**`src/auth.py`**
- `pwd_context: CryptContext` — the shared argon2id context; reuse it, don't
  construct a second one (see security-architect item 8(a)).
- `hash_password(plain) -> str`, `verify_password(plain, hash) -> bool`
- `hash_token(raw) -> str`, `generate_opaque_token() -> str`
- `DUMMY_PASSWORD_HASH: str` — for constant-cost login on an unknown email
- `Principal` (frozen dataclass: `id`, `email`, `role`, `tenant_id`,
  `session_id`) and `PrincipalResolver` (Protocol: `tenant_field`,
  `roles`, `principal_table`) — the tenancy seam, see the note below
- `get_current_session_user(resolver) -> FastAPI dependency`
- `get_pending_session(resolver) -> FastAPI dependency`, `PendingSession`
- `create_session`, `delete_session_by_raw_token`, `clear_mfa_pending`,
  `destroy_session_by_token_hash`
- `require_role(get_principal, *allowed) -> FastAPI dependency factory`
  (takes the principal-dependency callable itself, so it can declare it as
  its own `Depends` sub-dependency)
- `issue_session_token`, `set_session_cookie`, `clear_session_cookie`
- `is_mobile_client`, `_extract_raw_token` (underscore-prefixed but
  intentionally re-exported — every route needing raw-token access, e.g.
  logout, calls this directly; see the source's own precedent)
- `check_rate_limit(key, max_requests, window_seconds) -> bool`,
  `reset_rate_limits()` (test-only)
- `record_totp_failure`, `reset_totp_failures`, `MAX_TOTP_ATTEMPTS`
- `client_ip(request) -> str`
- Constants: `SESSION_COOKIE_NAME`, `SESSION_SLIDING_DAYS`,
  `SESSION_ABSOLUTE_DAYS`, `SESSION_TOKEN_HEADER`, `CLIENT_HEADER`,
  `MOBILE_CLIENT`, `TOTP_PENDING_SESSION_MINUTES`

**`src/sessions.py`**
- `SessionInfo` (pydantic model), `SessionStore` (`list_for_user`,
  `delete`, `delete_all_for_user`)

**`src/security_tokens.py`**
- `PasswordResetToken`, `PasswordResetTokenStore` (`create`,
  `get_valid_by_token_hash`, `mark_used`), `RECOVERY_CODE_COUNT`
- `RecoveryCode`, `RecoveryCodeStore` (`create_batch`, `unused_count`,
  `unused_for_user`, `mark_used`, `delete_all_for_user`)

**`src/totp.py`**
- `generate_totp_secret`, `encrypt_secret`, `decrypt_secret`,
  `provisioning_uri`, `verify_totp_code`, `generate_recovery_codes`,
  `hash_recovery_code`, `verify_recovery_code`, `TOTP_ISSUER` (override
  this constant per project)

**`src/crypto.py`**
- `get_fernet() -> Fernet`, reading `APP_ENCRYPTION_KEY`

**`mobile/tokenStore.ts`**
- `saveToken`, `loadToken`, `clearToken`

**Not part of the contract** (private, may change without notice):
`_session_select_sql`, `_resolve_session_row`, `_parse_iso`, everything
underscore-prefixed except `_extract_raw_token` (named above as an
intentional exception). `tests/_reference_app.py` is test scaffolding only
— never import it from adopting-project code.

**What is deliberately NOT in this accelerator** (H6's "what defect it
prevents" implies naming what it doesn't cover too): route wiring
(`routes/auth.py` in the source) is not vendored as source — it is a shape
reference only, reproduced in `tests/_reference_app.py` for this suite's own
use. Every adopting project wires its own routes against the `src/`
primitives, because route shape (URL paths, request/response schemas,
which endpoints exist at all) is exactly the kind of decision H2 says stays
with the adopter, not the accelerator.

---

## H2 · Config-vs-code boundary

| Surface | Configuration (env var / call arg) | Requires a fork |
|---|---|---|
| Password hashing algorithm | — | **Fork.** `pwd_context` is `CryptContext(schemes=["argon2"])`, hardcoded. Changing algorithms is a security decision, not a config toggle. |
| Session cookie name | — | **Fork.** `SESSION_COOKIE_NAME = "session"` is a module constant; edit it directly (a real fork of one line, tracked like any other local edit per the vendoring convention). |
| Session sliding / absolute expiry | — | **Fork.** `SESSION_SLIDING_DAYS`/`SESSION_ABSOLUTE_DAYS` constants. |
| `Secure` cookie flag | **Config.** `ENV=production` env var toggles it. | — |
| Persistence backend | — | **FORK POINT, not configurable.** `sqlite3.Connection` is threaded through every function's signature and every query is literal SQL. Security-architect explicitly rejected building a repository-abstraction seam against a backend (Postgres, etc.) nobody currently consumes — that is exactly the premature abstraction this platform's admission bar exists to prevent. **A Postgres-backed adopter forks this module.** This is a documented limitation, decided at harvest time, not a gap discovered mid-build. |
| Tenancy field name / whether tenancy exists at all | **Config**, via the `PrincipalResolver` Protocol (`tenant_field`, `roles`, `principal_table`) supplied at wiring time — see the tenancy note below. | — |
| Role vocabulary | **Config.** `PrincipalResolver.roles`; `require_role(*allowed)` takes any role-string set at call time. | — |
| Symmetric encryption key | **Config.** `APP_ENCRYPTION_KEY` env var. | — |
| **Key reuse across purposes** (TOTP secrets + whatever else you point `get_fernet()` at) | **Not a config toggle — a decision.** See security-architect item 4: every adopting project's security-architect must explicitly re-decide whether to share this key across purposes, never silently inherit the source project's choice. | — |
| Rate-limit thresholds (max requests, window) | **Config**, per call site (`check_rate_limit(key, max_requests, window_seconds)`). | — |
| **Rate-limit / TOTP-lockout storage** (`_RATE_BUCKETS`, `_TOTP_FAILURE_COUNTS`) | — | **FORK POINT beyond single-process.** See the dedicated subsection below (security-architect item 3) — this is not a tunable, it is a documented precondition with a mandatory revisit trigger. |
| TOTP parameters (digits, step, window) | — | **Fork.** `pyotp.TOTP(secret).verify(code, valid_window=1)` — RFC 6238 defaults are hardcoded in `totp.py`. |
| Recovery code count / format | **Config**, at call time (`generate_recovery_codes(count)`); alphabet/length/grouping are module constants — **fork** to change those. | — |
| Mobile Bearer header names | — | **Fork.** `CLIENT_HEADER = "X-LM-Client"`, `SESSION_TOKEN_HEADER = "X-LM-Session-Token"` are module constants. Rename on fork if your project already uses those header names for something else. |
| **CORS `expose_headers`** | — | **SECURITY INVARIANT, not a configuration choice.** `X-LM-Session-Token` (or whatever you rename `SESSION_TOKEN_HEADER` to) must NEVER be added to your CORS middleware's `expose_headers`. This is not something an adopter tunes — doing so defeats the header transport's entire fail-safe property (unreadable to cross-origin browser JS). Security-architect co-sign item 8(b). |
| Mobile web fallback (`Platform.OS === 'web'` → `localStorage`) | — | **DEV-PREVIEW-ONLY, not a production configuration.** See the dedicated statement below (security-architect item 8(c)). |

### Tenancy genericization — the `PrincipalResolver` seam

The source project hardcodes `family_id` throughout its session-resolution
SQL. A catalogue accelerator cannot hardcode any one project's schema, so
`auth.py` resolves the session→user JOIN through a small Protocol an
adopting project implements once:

```python
class MyResolver:
    tenant_field = "org_id"          # or None for a single-tenant project
    roles = frozenset({"admin", "member"})
    principal_table = "users"        # must have id, email, role columns
                                       # (+ tenant_field, if set)

get_principal = get_current_session_user(MyResolver())
# Depends(get_principal) everywhere a route needs the caller.
require_admin = require_role(get_principal, "admin")
# Depends(require_admin) on routes needing that specific role.
```

This was the one genuinely hard design decision in this harvest — see the
"What proved harder than expected" note at the end of this document for an
honest account of where it is and isn't a clean generalization.

### Persistence — stated as its own line, not buried in the table above

**`sqlite3.Connection`: FORK POINT, not configurable.** A Postgres-backed
adopter forks this module; this is a documented limitation, not a gap
discovered mid-build. (Security-architect co-sign item 2.)

---

## Precondition: single-process deployment only

*(Own labeled subsection per security-architect co-sign item 3 — verbatim,
carried into `src/auth.py`'s own comment block above `_RATE_BUCKETS` and
`_TOTP_FAILURE_COUNTS`.)*

`_RATE_BUCKETS` (login/join/reset rate limiting) and `_TOTP_FAILURE_COUNTS`
(TOTP pending-session lockout) are Python module-level `dict`s — in-process,
non-shared state. Correct and sufficient for a single-process local deploy.
**Silently wrong — not degraded, silently bypassable — under any
multi-worker/multi-process deployment**: each process gets its own
counters, so an attacker distributed across workers gets N× the stated
limit, and a TOTP brute-force attempt landing on a fresh worker resets its
own 5-attempt counter to zero.

**Revisit trigger — mandatory, before, not after:** more than one worker
process; behind a load balancer fronting more than one instance; any move
off a single always-on process (serverless/autoscaled compute). At that
point this moves to a shared store (Redis or equivalent) before the
deploy, not after.

---

## H3 · Host decoupling, proven

No import of any host project's domain modules anywhere in `src/` or
`mobile/`. `src/auth.py`'s `get_db()` imports `app.db.get_connection` —
this is the one intentional exception, documented inline as "adopting
project supplies this," and is exactly the shape H2's persistence-as-a-
fork-point line describes: the connection factory is the adopter's, not
this accelerator's.

`tests/_reference_app.py` and its synthetic `/items` resource exist
precisely so this suite does not need to import a host project's routes
(e.g. little-milestones' `/profiles`) to exercise authz-boundary behaviour
— see H4/H5 below.

**Closure-check status:** A5 (`structural conformance kit`) is the
instrument H3 calls for ("the catalogue eats its own dog food"). At the
time of this harvest A5 is still `planned` in `accelerators/CATALOGUE.md`
(build order: A4 → A5 → A3 → A2 → A1, per the approved proposal) and A1 is
being harvested out of that stated order at the human's explicit approval.
**This is stated, not concealed:** H3 is satisfied by manual inspection for
this harvest (the import list above is exhaustive and was verified by
reading every file in full) but not yet by A5's automated closure checker,
because A5 does not exist on disk yet. Re-run A5 against this directory
once A5 ships, and record the result here.

---

## H4 · Own executable suite

`tests/run.sh` — pytest, in-memory sqlite3, ASGI `TestClient` (no bound
socket, no long-lived process, no network, no credentials). Exit codes: `0`
pass, `1` fail, `3` no scenarios collected, `4` cannot execute (missing
`python3` or a required package) → `STATIC ONLY`.

`mas-registrar` holds no `Bash` grant and did not execute this script at
harvest time. **It has since been executed for real** (orchestrator pass,
2026-08-09, `little-milestones`' own venv as interpreter — `python3.9`,
`fastapi`/`pytest`/`passlib[argon2]`/`pyotp`/`cryptography` all present):
`55 passed` — **EXECUTED, PASS**, exit code 0. See `CHANGELOG.md` for the
four real defects that first run found and fixed, none of which the STATIC
ONLY review could have caught since it never ran the interpreter.

---

## H5 · Negative controls

- **Cross-tenant access (guard: 404-not-403 tenant isolation).** Fires:
  `test_cross_tenant_item_access_is_404_not_403`,
  `test_cross_tenant_item_access_is_404_over_bearer`. Does-not-fire
  control: same-tenant access to the same resource succeeds (implicit in
  every other authenticated test that reads back what it just created).
- **Role enforcement (guard: `require_role`).** Fires:
  `test_member_cannot_delete_item_owner_can`'s 403 branch. Does-not-fire:
  the same test's owner-succeeds branch, same fixture tree.
- **Rate limiter (guard: `check_rate_limit`).** Fires:
  `test_login_rate_limited_after_repeated_attempts`,
  `test_rate_limit_helper_windowing`'s final assertion. Does-not-fire:
  the same tests' preceding N-1 successful calls.
- **TOTP pending-session lockout (guard: 5-failure destruction).** Fires:
  `test_totp_login_wrong_code_repeated_destroys_pending_session`,
  `test_five_failed_totp_codes_destroy_the_pending_session_over_bearer`.
  Does-not-fire: `test_login_with_totp_enrolled_returns_mfa_pending_and_
  gates_other_routes`'s correct-code branch, same fixture shape.
- **Cookie-wins-on-conflict ordering (guard: cookie read first).** Fires
  both directions: `test_cookie_wins_on_conflict` (valid cookie beats
  valid different bearer) and `test_invalid_cookie_beats_valid_bearer`
  (a *stale* cookie still wins) — the sharper case, since without it the
  guarantee is really "whichever happens to work."
- **mfa_pending route gating (guard: pending sessions rejected outside
  the TOTP-login route).** Fires:
  `test_mfa_pending_bearer_is_gated_everywhere_but_totp_login`'s loop over
  `/auth/me`, `/auth/sessions`. Does-not-fire: the same test's final
  `totp/login` success.

---

## H6 · Provenance and rationale

**Exact source paths (little-milestones, `dev/` at time of harvest):**
`backend/app/auth.py`, `backend/app/sessions.py`,
`backend/app/security_tokens.py`, `backend/app/totp.py`,
`backend/app/crypto.py`, `backend/app/users.py` (referenced for shape,
not vendored — user/invite/family storage is host-project domain),
`backend/app/routes/auth.py` (referenced for shape, not vendored),
`mobile/src/auth/tokenStore.ts`. Tests: `backend/tests/test_auth.py`,
`test_auth_hardening.py`, `test_mobile_auth.py`,
`tests/suites/security/test_mobile_bearer_auth.py`.
`knowledge/SECURITY_KB.md` §1, §7, §9 (kb-seed).

**Explicitly excluded from harvest** (both the approving proposal and
security-architect's review confirm): `chat_sessions.py` — a chat concern,
not auth; its *shape* (narrow single-purpose methods, no ad hoc SQL in
routes) is worth imitating, its code is not worth vendoring, and
`sessions.py`/`security_tokens.py` already copied the shape correctly.

**What defect this prevents:** re-deriving argon2id-vs-bcrypt,
hashed-vs-plaintext session tokens, sliding-vs-absolute expiry interaction,
constant-cost login, TOTP pending-session gating, and safe dual-transport
(cookie+bearer) reads — each a genuine security decision with a documented
wrong answer, not boilerplate. The `max_tokens=4096` incident named in the
approving proposal (a real fix that stayed trapped in one project for a
month because nothing tracked drift) is the general failure mode this
accelerator's `[SECURITY]`-tag CHANGELOG convention (item 1 below) exists
to prevent for this specific, higher-stakes code path.

**What was deliberately left behind:** see H2's persistence line (no
repository abstraction), the rate-limiter precondition (no shared store),
and item 7 below (no password-strength/breach-list check). Also left
behind: OAuth/social login, magic-link email (both rejected in the source
project on privacy grounds specific to that product — re-evaluate for
yours, don't inherit the rejection either).

---

## H7 · Semver + CHANGELOG

`VERSION` = `1.0.0`. `CHANGELOG.md` documents the `[SECURITY]`-tag
convention (security-architect co-sign item 1) in its own header. A MAJOR
release will name every consumer in `accelerators/CATALOGUE.md`'s
known-consumers list in a migration note, per H10/H7's linkage.

---

## H8 · Deprecation

Not deprecated. If superseded in the future, this entry stays runnable and
records what supersedes it and why — never deleted.

---

## H9 · Security co-sign — the eight items, verbatim disposition

**Security co-sign: security-architect, 2026-08-09, CONDITIONAL, all eight
items below incorporated in this harvest.**

1. **Drift + security propagation tracking.** Implemented in
   `CHANGELOG.md`'s header: any entry touching `auth.py`, `sessions.py`,
   `security_tokens.py`, `totp.py`, or `crypto.py` is tagged `[SECURITY]`.
   A `[SECURITY]`-tagged entry means `CATALOGUE.md`'s consumers list records
   each named consumer as **"fix available, not yet applied"** until that
   consumer confirms it applied the fix.
2. **Persistence: SQLite is a fork point, not configuration.** Stated in
   H2's config table and its own dedicated line: no repository abstraction
   shipped; a Postgres-backed adopter forks this module.
3. **Module-global rate-limit/lockout dicts.** Own labeled subsection
   above ("Precondition: single-process deployment only"), reproduced
   verbatim into `src/auth.py`'s comment block above both dicts.
4. **`PHOTO_ENCRYPTION_KEY` → `APP_ENCRYPTION_KEY`.** Done in `crypto.py`.
   Documented as designed for reuse across an adopting project's own
   symmetric-encryption-at-rest needs, not restricted to auth, with the
   key-reuse-across-purposes decision named explicitly in H2's config
   table as one every adopting project's security-architect must
   re-make, never silently inherit.
5. **"Floor, never a ceiling."** Stated in this document's own words (H4
   and this sentence): the vendored test pack proves this accelerator's
   own claims about itself, not that an adopting project wired it up
   correctly (env-gated `Secure` cookie flag, every route actually gated
   behind the auth dependency, `APP_ENCRYPTION_KEY` actually set). Every
   adopting security-architect runs the vendored pack **plus** authors
   integration-level scenarios specific to their own wiring.
6. **KB seed provenance-tagging requirement.** `kb-seed/SECURITY_KB_seed.md`
   opens with the required header; this document's own adoption
   instruction (see "Adoption steps" below) requires (a) the adopting
   project re-fills the multi-tenancy/PII/network-exposure/deployment-
   target criteria table against its own attributes, and (b) every seeded
   decision not re-derived from that re-fill carries a visible provenance
   tag in the adopting project's own `SECURITY_KB.md`.
7. **Documented limitation for missing password-strength/breach-list
   checks.** No password-strength meter, no breach-list check (e.g. HIBP
   k-anonymity) — left behind because no current consumer's threat model
   required it and it adds a network dependency this local-first
   accelerator otherwise avoids. A future adopter handling higher-value
   credentials should re-evaluate per their own criteria table, not
   inherit this as an acceptable gap.
8. **Four sub-findings:**
   - **(a) TOTP's shared `CryptContext`.** Documented in `totp.py`'s module
     docstring: `totp.py` depends on `auth.py`'s password-hashing primitive
     as a sub-module, not an independent unit. A partial vendor (auth
     without TOTP) is fine; a partial vendor of TOTP without preserving the
     `from .auth import hash_password, verify_password` line, reconstructing
     a second `CryptContext` instead, is the footgun this note exists to
     prevent.
   - **(b) CORS `expose_headers` must NEVER include the session-token
     header.** Named explicitly in H2's config table as a security
     invariant, not a configuration choice, and re-stated in
     `auth.py`'s `issue_session_token` docstring.
   - **(c) The mobile web `localStorage` fallback is dev-preview-only.**
     The exact label `DEV PREVIEW ONLY` is preserved verbatim in
     `mobile/tokenStore.ts`'s own comment, and asserted on by
     `test_dev_preview_only_label_present_on_web_fallback`.
   - **(d) Constant-cost enumeration resistance — test-pack gap found and
     closed.** Read `test_auth.py` and `test_auth_hardening.py` in the
     source project in full: **neither contains an explicit assertion that
     `verify_password` is called on the unknown-email login path** — only
     the outcome (401, generic message) is asserted
     (`test_login_unknown_email_same_generic_401`), never the mechanism
     that makes the response-time profile actually match the wrong-password
     case. This is a real gap in the existing 78-test pack, logged here
     rather than left unaddressed, and **closed in this accelerator's own
     vendored copy** by
     `test_login_unknown_email_calls_verify_password` in `tests/test_auth.py`
     (spies on `verify_password`, asserts it is called with
     `DUMMY_PASSWORD_HASH` for an unknown email). This closes the gap going
     forward for every consumer of this accelerator; it does not retroactively
     fix little-milestones' own suite, which `mas-release-manager`/that
     project's own security-architect should track separately if desired.

---

## H10 · Known consumers

See `accelerators/CATALOGUE.md`'s A1 row. `little-milestones` is the
origin (harvested *from*, not yet vendored *back into* — it runs its own
pre-harvest copy of this code, not this accelerator's copy). No other
project has vendored this accelerator as of this harvest.

---

## Adoption steps

1. Implement `PrincipalResolver` against your own schema (H2's tenancy
   note above).
2. Set `APP_ENCRYPTION_KEY` (only if you use `totp.py` or otherwise call
   `crypto.get_fernet()`) — and have your security-architect explicitly
   re-decide the key-reuse-across-purposes question (item 4 above), not
   inherit it silently.
3. Wire your own routes against `src/`'s primitives (H1's contract) — this
   accelerator does not ship a routes file; `tests/_reference_app.py` is a
   shape reference, not a contract.
4. Wire CORS with `X-LM-Session-Token` (or your renamed header) **absent**
   from `expose_headers` — this is not optional (item 8(b)).
5. Copy `kb-seed/SECURITY_KB_seed.md` into your project's own
   `knowledge/SECURITY_KB.md`, then **re-fill** the criteria table against
   your project's own multi-tenancy/PII/network-exposure/deployment-target
   attributes (item 6) — do not copy the source project's answers. Tag
   every decision you keep without re-deriving it as "inherited from
   accelerators/auth-core@1.0.0, re-confirmed applicable [date]."
6. Vendor `tests/` (all files, including `_reference_app.py` and
   `conftest.py`) and run `tests/run.sh` inside your own project — then
   author your own integration-level scenarios per item 5 above ("floor,
   never a ceiling"). Reuse never lowers the evidence bar: every
   acceptance criterion touching this accelerator's code is still verified
   in your own project at your own Verification gate.
7. Before any non-local/multi-process deployment: revisit the rate-
   limiter precondition (this document's own labeled subsection) *before*
   deploying, not after.

---

## What proved harder than expected — stated honestly, per this task's brief

The `PrincipalResolver` seam is a genuine generalization, not a cosmetic
rename, for the pieces it touches (the session→principal JOIN and the
`Principal` shape). It is **not** a complete abstraction over "what is a
user" in every possible schema:

- It assumes exactly one principal table with `id`/`email`/`role` columns.
  A project that splits identity across multiple tables (e.g. a separate
  `credentials` table from a `profile` table) still forks the JOIN in
  `_session_select_sql`.
- It assumes a single, simple tenant column (or none). A project with
  multi-level tenancy (e.g. org → team → user) forks it.
- `Principal` deliberately dropped little-milestones' `digest_opt_in`
  field rather than trying to generalize "arbitrary extra claims" — an
  adopting project needing extra cached claims on the principal is
  expected to look them up from `Principal.id` in its own store, not to
  extend this dataclass. This was a real design choice (a generic
  `extra: dict` field was considered and rejected as exactly the kind of
  premature, unconstrained flexibility this catalogue's admission bar
  exists to prevent) — worth surfacing rather than presenting as
  obviously correct.

None of this is a broken abstraction being forced through — it is a
seam sized to the one thing that actually varied (tenant field name,
role vocabulary, table name) and left everything else as an honest fork
point, consistent with H2's own discipline of naming forks rather than
hiding them behind false configurability.
