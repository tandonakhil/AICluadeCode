# Unit/Integration Test Evidence — Increment 6 (F12: hardened auth — password
reset, opt-in TOTP MFA, session hardening)

Suite: Test-agent, unit/integration (blocking per default policy — no
advisory marking on record for this suite in PROJECT_CONTEXT.md).
Run date: 2026-07-12.
Backend commit under test: `e3f48e5`. Frontend commit under test: `e179012`.

## Suite totals (re-verified)

- Backend, `.venv/bin/python -m pytest -q` from `dev/backend`: **199 passed**,
  0 failed, 3 warnings (pre-existing deprecation warnings only —
  `argon2.__version__`, two `on_event` deprecations — non-blocking, unrelated
  to F12). Matches code-agent's reported 199.
- Frontend, `npx tsc --noEmit` from `dev/frontend`: clean, zero errors.
- Frontend, `npm test -- --run` from `dev/frontend`: **54 passed** (9 test
  files), 0 failed, 880ms. Matches code-agent's reported 54.
- Zero-test-suite caveat: not applicable to the totals above — both suites
  are nonzero. **However, see the coverage-gap finding below: within these
  passing totals, zero net-new test cases exist for F12 itself.**

## COVERAGE GAP — no committed tests for F12 (real gap, not a suite failure)

- `dev/backend/tests/` contains no new test file for F12 (no `test_totp.py`,
  `test_password_reset.py`, `test_sessions.py`, etc.), and `test_auth.py`'s
  29 test functions are all pre-existing (Increment 3) session/login/logout
  tests — grepping `test_auth.py` for `totp|reset|recovery|session|mfa`
  matches only pre-existing cookie/login/logout tests, none of the new F12
  behavior.
- `git show --stat e3f48e5` (backend) confirms this directly: 11 files
  changed, all under `app/` (new modules `crypto.py`, `security_tokens.py`,
  `sessions.py`, `totp.py`, plus edits to `auth.py`/`db.py`/
  `email_delivery.py`/`photos.py`/`routes/auth.py`/`users.py`/
  `pyproject.toml`) — **zero files under `tests/` touched.**
- `git show --stat e179012` (frontend) confirms the same pattern: new
  `SecurityCard.tsx` (564 lines), `app/forgot-password/page.tsx` (97 lines),
  `app/reset-password/page.tsx` (160 lines), and `AuthScreen.tsx` changes
  (+132 lines for the TOTP challenge step) — but `app/page.test.tsx` and
  `SettingsScreen.test.tsx` each changed by only **1 line** (consistent with
  a trivial mock/import adjustment, not new test coverage), and no
  `SecurityCard.test.tsx`, `AuthScreen.test.tsx`,
  `forgot-password/page.test.tsx`, or `reset-password/page.test.tsx` exists
  anywhere in the repo (`find . -name "*.test.tsx"` lists only
  `page.test.tsx`, `Avatar.test.tsx`, `ChatScreen.test.tsx`,
  `JourneyScreen.test.tsx`, `Lightbox.test.tsx`, `SettingsScreen.test.tsx` —
  none new this commit, none exercising TOTP/reset/SecurityCard).
- Both commit messages are explicit about this themselves: e3f48e5 says "new
  flows smoke-tested end-to-end" (a manual/TestClient script, not committed
  pytest); e179012's message doesn't claim new frontend tests either.
- **This is a real gap, not a feature-working-but-untested nitpick**: F12 is
  security-sensitive (auth, MFA, password reset, session revocation) and
  currently has zero regression coverage — a future refactor could silently
  break TOTP verification, recovery-code single-use enforcement, or the
  cross-user session-id 404 with no test catching it. Flagging for
  code-agent to close before this suite can be called complete for F12,
  per SECURITY_KB/ARCHITECTURE_KB's usual "new security-relevant surface
  gets its own regression tests" pattern established in prior increments
  (e.g. Increment 3's 30 new auth tests, Increment 5's family-scoping ×3
  tests).

---

## Live backend smoke test (curl, real HTTP against a running :8000 server)

Both dev servers (backend :8000, frontend :3000) were found **not running**
at the start of this run, despite the task brief's assumption that they were
already up (likely stopped between sessions) — started fresh via
`uvicorn app.main:app --port 8000` and `npm run dev -- --port 3000`
respectively before smoke testing; confirmed `/health` 200 and `/` 200
first. Flagging this discrepancy for the record, not as a defect.

### Scenario: Signup + login (baseline, no MFA)
- Input: `POST /auth/signup` with a fresh email/password, then
  `POST /auth/login` with the same credentials.
- Expected: 201 on signup; 200 on login with `mfa_required: false` and a
  populated `user` object (`totp_enabled: false`).
- Actual: exactly as expected.
- Result: PASS
- Evidence: `{"id":13,...,"totp_enabled":false}` HTTP 201;
  `{"mfa_required":false,"user":{...,"totp_enabled":false},...}` HTTP 200.

### Scenario: TOTP enrollment (setup + verify)
- Input: `POST /auth/totp/setup` with current password → returns
  `provisioning_uri`/`secret`; computed a real 6-digit code from the
  returned secret via `pyotp.TOTP(secret).now()` (pyotp confirmed available
  in the backend venv); `POST /auth/totp/verify` with that code.
- Expected: setup requires correct password and returns a usable secret;
  verify with a correct live-computed code succeeds and returns exactly 8
  recovery codes.
- Actual: setup returned `{"provisioning_uri":"otpauth://totp/little-
  milestones:...","secret":"GIYP5NDJJZYANK4ZFFUGDOZISTMNO2W6"}` HTTP 200;
  verify returned exactly 8 recovery codes (format `XXXX-XXXX-XXXX-XXXX`)
  HTTP 200.
- Result: PASS
- Evidence: full request/response pairs captured above; recovery codes:
  `NG9Q-P7Q2-82D2-2GGN, 4ESG-D5G6-8V2F-6WSW, WD5Q-8U4P-LZD8-4FX2,
  7HQU-3G43-KRGF-A2E8, HTD4-L542-X4E5-6TSL, J3XQ-YBB9-39M6-SQBE,
  W2LX-RHKJ-7RVC-SE8C, K82L-X9V5-YVWU-P39L` (test account only, discarded).

### Scenario: Login after TOTP enrollment triggers `mfa_pending` challenge
- Input: logout, then `POST /auth/login` with correct credentials for the
  now-TOTP-enrolled user; then `GET /auth/me` while still in the
  `mfa_pending` state.
- Expected: login returns `mfa_required: true`, `user: null` (no session
  data leaked pre-MFA); any non-MFA authenticated route (`/auth/me`) is
  blocked (401) while the session is `mfa_pending`.
- Actual: `{"mfa_required":true,"user":null,"recovery_codes_remaining":null}`
  HTTP 200 on login; `{"detail":"Not authenticated"}` HTTP 401 on `/auth/me`.
- Result: PASS
- Evidence: captured above.

### Scenario: TOTP challenge completion with a freshly-computed code
- Input: `POST /auth/totp/login` with a newly-computed `pyotp` code (not
  reused from enrollment) while the session was `mfa_pending`.
- Expected: clears `mfa_pending`, returns the full user object with
  `totp_enabled: true`; subsequent `/auth/me` succeeds.
- Actual: exactly as expected — `mfa_required:false`, `totp_enabled:true`
  on the login response, and `/auth/me` returned 200 immediately after.
- Result: PASS
- Evidence: captured above.

### Scenario: Recovery-code login + single-use enforcement
- Input: logout, login (re-triggers `mfa_pending`), `POST /auth/totp/login`
  with one of the 8 recovery codes from enrollment; then logout, login again,
  and re-submit the **same** recovery code a second time.
- Expected: first use succeeds and reports `recovery_codes_remaining: 7`
  (one consumed); second use of the same code fails (already marked used).
- Actual: first use →
  `{"mfa_required":false,"user":{...},"recovery_codes_remaining":7}` HTTP
  200; second use of the identical code →
  `{"detail":"That code didn't work -- 4 attempts left"}` HTTP 401 (correctly
  rejected as already-consumed, with the 5-attempt lockout counter visibly
  active).
- Result: PASS
- Evidence: captured above.

### Scenario: Password-reset request — generic response, token created server-side
- Input: `POST /auth/password-reset/request` for a real, freshly-signed-up
  email.
- Expected: 202 with a generic "if an account exists..." message (no
  enumeration); a reset token row is created server-side even though the
  actual email send fails in this dev environment (no `RESEND_API_KEY`
  configured — confirmed via `app/email_delivery.py`, ARCHITECTURE_KB §5.1's
  documented operational precondition).
- Actual: `{"detail":"If an account exists for that address, we've sent a
  link."}` HTTP 202; backend log shows
  `password_reset_email_send_failed user_id=14` (caught and logged per
  design, response path unaffected — exactly per `routes/auth.py`'s
  documented "no enumeration via failure" comment); a direct read-only query
  of `data/little_milestones.db`'s `password_reset_tokens` table confirmed a
  new row for `user_id=14` with a 30-minute `expires_at` and `used_at IS
  NULL`, proving the request-side of the flow genuinely runs end-to-end up
  to token creation.
- Result: PASS (request side). **Confirm side NOT fully live-smoke-testable
  in this environment** — see gap note below.
- Evidence: HTTP 202 response; backend.log line; DB query output
  `(3, 14, '2026-07-13T02:34:50...', None)`.

### Scenario: Password-reset confirm — invalid token rejected
- Input: `POST /auth/password-reset/confirm` with a fabricated garbage
  token.
- Expected: 400, generic "no longer valid" message (no distinguishing detail
  per SECURITY_KB §7.2).
- Actual: `{"detail":"This reset link is no longer valid"}` HTTP 400.
- Result: PASS
- Evidence: captured above.

**Gap note (environment limitation, not a code defect):** the real
reset-confirm happy path (using the actual raw token from a delivered
email) could not be live-smoke-tested end-to-end in this dev environment,
because (a) no `RESEND_API_KEY` is configured (by design — no verified
Resend sending domain yet, an existing documented precondition, not new to
F12), and (b) **`email_delivery.py` has no dev-mode outbox/console-log
fallback** that captures the reset URL/raw token when the real send fails —
the route's `except Exception: logger.warning(...)` only logs `user_id`,
never the token or URL (correct for the no-PII-in-logs rule, but it also
means there is currently no way to recover the raw token in local dev
without either a real Resend account or an application-code change).
Flagging this as a secondary, smaller gap for code-agent/solution-architect:
a dev-only outbox (e.g. writing the reset URL to a gitignored file or
console when `RESEND_API_KEY` is unset) would make this flow testable
locally without weakening the production no-enumeration/no-PII design.

### Scenario: Session list, self-scoped, marks current session
- Input: `GET /auth/sessions` for two different logged-in users (A, B), each
  with 2 active sessions.
- Expected: each user sees only their own sessions, with exactly one marked
  `is_current: true`.
- Actual: user A's list showed 2 sessions (one `is_current:true`); user B's
  list showed a disjoint set of 2 sessions (one `is_current:true`) — no
  cross-user leakage.
- Result: PASS
- Evidence: captured above.

### Scenario: Cross-user session revoke → 404, not 403, and no actual deletion
- Input: user A attempts `DELETE /auth/sessions/{id}` using user B's session
  id (obtained from B's own `/auth/sessions` listing).
- Expected: 404 (not 403 — consistent with the project's established
  cross-family/cross-user pattern of not leaking existence), and B's session
  must remain listed afterward (proving it wasn't actually deleted despite
  the request being made).
- Actual: `{"detail":"Session not found"}` HTTP 404; re-querying B's
  `/auth/sessions` immediately after confirmed the session was still present
  and unchanged.
- Result: PASS
- Evidence: captured above.

### Scenario: Own non-current session revoke succeeds
- Input: user A revokes their own older (non-current) session id.
- Expected: 200, and the session list subsequently shows only the current
  session.
- Actual: `{"deleted":true}` HTTP 200; follow-up list showed exactly 1
  remaining session (the current one).
- Result: PASS
- Evidence: captured above.

### Scenario: TOTP disable — requires correct password AND a valid code
- Input: `POST /auth/totp/disable` first with a wrong password (expect
  rejection before the code is even considered), then with the correct
  password and a freshly-computed TOTP code.
- Expected: wrong password → 401, TOTP still enabled; correct
  password+code → 200, TOTP cleared, and a subsequent login for that user
  shows no MFA challenge.
- Actual: wrong password → `{"detail":"Current password is incorrect"}` HTTP
  401; correct → `{"disabled":true}` HTTP 200; `/auth/me` confirmed
  `totp_enabled:false`; a fresh logout/login cycle for that user returned
  `mfa_required:false` directly (no challenge).
- Result: PASS
- Evidence: captured above.

## Live frontend smoke test (curl against :3000)

### Scenario: `/forgot-password` route
- Input: `GET http://localhost:3000/forgot-password`.
- Expected: 200, no Next.js error-boundary trigger, page contains relevant
  copy.
- Actual: HTTP 200; page `<title>` renders normally
  (`little-milestones`); body contains "Reset your password"/"forgot"
  copy; no "Application error" or `__next_error__` marker present (the
  literal strings `error-h1`/`errorScripts`/`errorStyles` found are Next.js's
  bundled error-boundary component *names* shipped in every page's JS/CSS
  chunk, not an actually-triggered error — confirmed no
  "Application error"/"Internal Server Error"/`__next_error__` digest text
  anywhere in the response).
- Result: PASS
- Evidence: HTTP 200; grep counts as described.

### Scenario: `/reset-password` route, with and without a token query param
- Input: `GET http://localhost:3000/reset-password?token=bogus` and
  `GET http://localhost:3000/reset-password` (no token).
- Expected: both 200, no server crash either with or without the expected
  query param.
- Actual: both HTTP 200; the token-present request's body contains "Reset"
  copy confirming real content rendering.
- Result: PASS
- Evidence: HTTP 200 x2.

### Scenario: Settings' Security card — client-error check (partial verification)
- Input: `GET http://localhost:3000/` with an authenticated session cookie
  (a real logged-in test user's cookie jar).
- Expected: page loads without a server-side error.
- Actual: HTTP 200, no `Application error`/`__next_error__` marker; frontend
  dev-server log (`npm run dev`) shows no compile or runtime errors for the
  full session, including the `SecurityCard.tsx` module.
- Result: **PASS with a caveat** — `app/page.tsx` gates the whole app shell
  behind a client-side session check (`getMe()` called in a `useEffect`,
  confirmed via `app/page.tsx`), and Settings/SecurityCard is not a separate
  Next.js route (`find app -name page.tsx` shows only `/`,
  `/forgot-password`, `/reset-password` as routes) — it's a client-rendered
  view switched in-app after JS runs. A plain curl request cannot execute
  that client-side session check or render, so this scenario cannot fully
  confirm "SecurityCard renders without a client error for a logged-in
  user" the way browser automation could. What *was* confirmed: `tsc
  --noEmit` is clean (would catch `SecurityCard.tsx` type errors), the dev
  server's own compile log shows zero errors for the module, and the root
  page itself serves and loads cleanly with an authenticated cookie present.
  Full behavioral confirmation of this specific scenario requires browser
  automation this environment doesn't have — flagged per the task's own
  acknowledged limitation, not treated as a silent pass.
- Evidence: HTTP 200; `tsc --noEmit` clean (see suite totals above); dev
  server log free of errors for the session.

---

## Gate verdict

**Backend unit/integration: PASS, 199/199** (matches code-agent's report,
re-verified independently). **Frontend unit: PASS, 54/54, tsc clean**
(matches code-agent's report). **Live backend smoke (F12 flows): PASS** on
every scenario exercised — signup, login, TOTP setup/verify, `mfa_pending`
challenge + completion, recovery-code login + single-use enforcement,
password-reset request (generic response + real server-side token
creation) and confirm-with-invalid-token rejection, session list/revoke
including cross-user 404 and own-session revoke, TOTP disable with
password+code requirement. **Live frontend smoke: PASS** on
`/forgot-password` and `/reset-password` (both 200, real content, no error
markers); Settings/SecurityCard client-render check is a **partial PASS**
— no evidence of failure, but full confirmation needs browser automation
this environment lacks.

**Two flagged gaps, both real, neither a "feature is broken" finding:**
1. **Blocking-suite coverage gap**: zero committed pytest/vitest tests exist
   for any F12 behavior (TOTP enroll/verify/disable, recovery-code login,
   password reset request/confirm, session list/revoke, cross-user
   session-id 404) — the 199/54 passing totals contain no F12 regression
   coverage at all, despite F12 being fully live-smoke-tested and working.
   This is a real gap in this blocking suite (no advisory marking recorded
   for unit/integration) and should be sent back to code-agent to close
   before this increment is considered test-complete, per the human's
   override-or-send-back gate contract.
2. **Minor environment gap**: no dev-mode email outbox in
   `email_delivery.py` means the password-reset confirm happy path can't be
   exercised via a real token in local dev without a Resend account —
   request-side behavior and invalid-token rejection were both verified
   directly; the token-creation step was independently confirmed via a
   read-only DB query.

Scratch files created during this run (`cookies_a.txt`, `cookies_b.txt`,
`totp_setup.out`, `totp_verify.out`, `sessions_a.json`, `sessions_b.json`,
temp HTML fetches) were all cleaned up before finishing; one accidental
0-byte `dev/backend/little_milestones.db` (created by a diagnostic query
run from the wrong working directory, distinct from and non-overlapping
with the real `dev/backend/data/little_milestones.db`) was also removed —
`git status` on `dev/` is clean.
