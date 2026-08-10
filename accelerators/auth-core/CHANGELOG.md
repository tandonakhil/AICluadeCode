# Changelog — `accelerators/auth-core`

Semver per `admin/MAS_REGISTRY.md` conventions (adapted for accelerators):
MAJOR = breaking change to the declared H1 contract or a security-relevant
behaviour change requiring adopter action; MINOR = additive surface; PATCH =
no behaviour change.

**`SECURITY`-tag convention (security-architect co-sign item 1, mandatory):**
any entry below touching `auth.py`, `sessions.py`, `security_tokens.py`,
`totp.py`, or `crypto.py` is tagged `[SECURITY]`. A `[SECURITY]`-tagged
entry means every consumer named in `accelerators/CATALOGUE.md`'s known-
consumers list is recorded there as **"fix available, not yet applied"**
until that consumer confirms (to `mas-release-manager`) that they applied
the fix — `CATALOGUE.md` is the record of who still needs to act, not just
who once vendored this accelerator.

## [1.0.0] — 2026-08-09

Initial harvest from `little-milestones/dev/backend/app/{auth,sessions,
security_tokens,totp,crypto}.py`, `dev/backend/app/routes/auth.py` (shape
reference only, not vendored as-is), and `dev/mobile/src/auth/tokenStore.ts`.
78 test functions in the source pack, surviving a dedicated hardening
increment (F12) and a mobile increment (F18); this accelerator's own vendored
pack is adapted, not byte-identical (see `ACCELERATOR.md` item 5).

`[SECURITY]` Every file in `src/` is security-relevant by construction — this
initial harvest is the baseline, not a fix to a prior version.

Changes made during harvest, all attributed to security-architect's
conditional H9 co-sign (`ACCELERATOR.md`'s "Security co-sign" section names
each item):

- `[SECURITY]` Tenancy genericized: `family_id` → a `PrincipalResolver`-
  resolved `tenant_id`, so no host project's schema is hardcoded.
- `[SECURITY]` `PHOTO_ENCRYPTION_KEY` renamed to `APP_ENCRYPTION_KEY` in
  `crypto.py`, with the key-reuse-across-purposes decision named explicitly
  as one every adopting project's security-architect must re-make.
- `[SECURITY]` Module-global rate-limit/TOTP-lockout dicts documented as a
  single-process-only precondition with a named, mandatory revisit trigger.
- `[SECURITY]` `sqlite3.Connection` documented as a fork point, not a
  configuration option — no repository abstraction shipped.
- `[SECURITY]` Added `test_login_unknown_email_calls_verify_password` to the
  vendored test pack — the source pack asserted the unknown-email path's
  *outcome* (401, generic message) but not the *mechanism* (verify_password
  actually runs against the dummy hash) that gives constant-cost
  enumeration resistance its guarantee. Logged as a gap in the source pack,
  closed in this vendored copy.
- Documented (not code): no password-strength meter, no breach-list check —
  left behind deliberately, named as a decision a future adopter with a
  higher-value-credential threat model should re-evaluate, not inherit.

H9 co-signed by security-architect 2026-08-09, conditional on all 8 items in
the review being incorporated — see `ACCELERATOR.md`'s "Security co-sign
(H9)" section for the item-by-item disposition.

## [1.0.1] — 2026-08-09

Not a behaviour change to `src/` — PATCH, test-scaffolding-only. The harvest's
own H4 suite (`tests/run.sh`) was marked STATIC ONLY — NOT EXECUTED at
1.0.0, since `mas-registrar` holds no `Bash` grant. Executed for real
immediately after (orchestrator pass, same day): **4 real defects found and
fixed**, all in `tests/`, none in `src/`:

1. `tests/_reference_app.py` — request/response Pydantic models (`SignupRequest`
   etc.) were nested inside `build_app()`. Combined with this file's
   `from __future__ import annotations`, FastAPI could not resolve them as
   body models via `typing.get_type_hints()` against closure scope, and
   silently treated `data: SignupRequest` as a query parameter — every route
   422'd on a well-formed JSON body. Moved all request/response models to
   module scope.
2. `tests/conftest.py` — the `test_db` fixture's `sqlite3.connect(":memory:")`
   used the default `check_same_thread=True`, but FastAPI's `TestClient` runs
   sync route handlers in an anyio worker thread — first request raised
   `sqlite3.ProgrammingError`. Added `check_same_thread=False` (safe here: one
   connection, one `TestClient`, never concurrent).
3. `tests/_reference_app.py` — `get_current_session_user`/`get_pending_session`
   (in `src/auth.py`) resolve their connection via `Depends(get_db)`, and
   `get_db()`'s real body does `from app.db import get_connection` — a
   deliberate placeholder for an adopting project to override. The reference
   app never registered a matching `app.dependency_overrides[get_db]`, so in
   an environment where an unrelated `app` package happens to be importable
   (here: another Conclave project's own `app.db`, reachable via its venv's
   editable install), the placeholder import silently succeeded and connected
   to *that* project's real database — producing a confusing
   `no such column: users.tenant_id` far from the actual cause. Added the
   override.
4. `tests/test_mobile_bearer_auth.py` — a local `PASSWORD =
   "correct-horse-battery-staple"` (hyphens) diverged from `conftest.py`'s
   `DEFAULT_PASSWORD = "correct horse battery staple"` (spaces), which is
   what `signup_mobile()` actually signs up with. Every TOTP-setup call in
   the file authenticated with the wrong password and 401'd. Now imports
   `DEFAULT_PASSWORD` instead of re-typing it.

After all four fixes: `55 passed` for real (`python3.9`,
`fastapi`/`pytest`/`passlib[argon2]`/`pyotp`/`cryptography`), exit code 0.
`src/` required no changes — every defect was in the harvest's own test
scaffolding, not in the vendored `auth.py`/`sessions.py`/`security_tokens.py`/
`totp.py`/`crypto.py`. Recorded here rather than silently amended, per this
platform's standing discipline that a suite once reported "could not execute"
must actually be re-run, and its real result — including what that run
found — belongs in the record.
