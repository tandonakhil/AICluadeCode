# Unit/integration test evidence — Increment 7 (F17: Google Photos import)

Run by test-agent, 2026-07-13. Suite policy: blocking (no advisory marking
on record for unit/integration). Commits under test: backend `8a76d55`,
frontend `0056069`.

## Scenario: backend pytest full suite
- Input: `cd dev/backend && .venv/bin/python -m pytest -q`
- Expected: full suite passes, matching code-agent's reported 275/275
- Actual: `275 passed, 3 warnings in 10.94s` (warnings are pre-existing
  deprecation notices — passlib argon2 version access, FastAPI `on_event` —
  unrelated to F17)
- Result: PASS
- Evidence: pytest summary line `275 passed, 3 warnings in 10.94s`

## Scenario: backend F17 test files are genuine, not name-only
- Input: read `tests/test_google_photos.py` (317 lines) and
  `tests/test_google_photos_routes.py` (656 lines) in full
- Expected: real assertions against DB rows/ciphertext/mocked HTTP
  responses, not trivially-true placeholders
- Actual: confirmed genuine —
  - `test_google_photos.py`: real SQLite fixture (`test_db`), asserts
    `OAuthStateStore` single-use/expiry/wrong-user rejection by directly
    manipulating `google_oauth_states` rows; asserts Fernet ciphertext at
    rest via `gp.decrypt_token`/raw-byte non-containment checks on
    `google_photos_connections` columns; asserts lazy-refresh behavior
    (unexpired token skips refresh, expired token refreshes, rotated
    refresh token persisted, `invalid_grant` deletes the connection row and
    raises `ConnectionLapsed`); a static-source guard asserts no log call
    in the module ever interpolates `access_token`/`refresh_token`/
    `code_verifier`.
  - `test_google_photos_routes.py`: every Google network call is mocked via
    a `FakeGooglePhotosClient` injected through a real FastAPI
    `dependency_overrides` seam (`routes_gp._google_client`) — no
    monkeypatched `requests` calls, the same discipline as the existing
    `test_email_delivery.py`/`test_scheduler.py` convention. Drives a real
    `/connect` → captures the server-generated `state` → real `/callback`
    round trip (not a hand-constructed state value), exercises CSRF
    (wrong-user state, expired state, replayed state — each a real DB
    row manipulation or genuine second signup/logout/signup sequence, not
    a mocked assertion), disconnect revoke-then-delete ordering including
    a failed-revoke-keeps-row case, cross-family 404 via two genuine
    signups sharing one `TestClient` cookie jar, a lazy-refresh-failure →
    409 "not connected" path with the connection row confirmed deleted,
    a content-minimization guardrail test that feeds a fake Google response
    containing `peopleGrouping`/`labels`/`description` fields and asserts
    none of them appear in the API response, a real-Pillow-encoded JPEG
    fixture used to exercise the actual EXIF-strip/encryption/content-hash
    pipeline (on-disk bytes asserted to differ from the original and
    contain no `JFIF` marker — i.e., genuinely Fernet-encrypted, not just
    copied), duplicate-detection scoped correctly to per-child (not
    per-family), batch-size cap, and a static AST-based import-graph check
    asserting neither new module imports `app.llm`/`app.prompts`/
    `app.guardrails`.
  - Conclusion: both files are real regression tests exercising actual
    code paths (DB, crypto, mocked HTTP, static analysis), not
    name-only/trivially-passing tests. This closes the gap class the
    Increment 6 Test gate found (F12 shipped with zero committed tests) —
    F17 does not repeat it.
- Result: PASS
- Evidence: full file reads of both test files, quoted above by scenario
  class; see `dev/backend/tests/test_google_photos.py` and
  `dev/backend/tests/test_google_photos_routes.py`.

## Scenario: frontend typecheck
- Input: `cd dev/frontend && npx tsc --noEmit`
- Expected: clean, no errors
- Actual: clean exit, no output
- Result: PASS

## Scenario: frontend vitest full suite
- Input: `cd dev/frontend && npm test -- --run`
- Expected: full suite passes, matching code-agent's reported 80/80
- Actual: `Test Files 15 passed (15)`, `Tests 80 passed (80)`
- Result: PASS

## Scenario: frontend F17 test files are genuine, not name-only
- Input: read `components/GooglePhotosCard.test.tsx` (147 lines) and
  `components/GooglePhotosImportDialog.test.tsx` (184 lines) in full
- Expected: real RTL assertions against rendered DOM/state transitions,
  mocked API layer only (not mocked component internals)
- Actual: confirmed genuine — `GooglePhotosCard.test.tsx` mocks only
  `@/lib/api` (`getGooglePhotosStatus`/`disconnectGooglePhotos`), renders
  the real component, and asserts real DOM text/role queries for
  not-connected/connected/cancelled/error states, a real click-driven
  disconnect confirm dialog (asserting the button's className is the
  non-destructive `lm-btn-secondary` variant, not `lm-btn-destructive` —
  a real design-system contract check), and a real optimistic-then-
  reverted-on-failure state transition on a rejected disconnect call.
  `GooglePhotosImportDialog.test.tsx` mocks only the API layer, drives a
  real `fireEvent.click` through the intro → picker hand-off (asserts
  `window.open` called with the real picker URL) → preview (duplicate
  badge defaults a checkbox to checked/skipped, live confirm-count text
  updates on toggle, confirm button disables at zero) → import (asserts
  `importFromGooglePhotos` called with the exact skip-selection payload)
  → partial-failure rendering with a scoped retry that re-calls the API
  with only the failed item.
- Result: PASS
- Evidence: full file reads of both test files; see
  `dev/frontend/components/GooglePhotosCard.test.tsx` and
  `dev/frontend/components/GooglePhotosImportDialog.test.tsx`.

## Scenario: live backend smoke — blocked by stale running process (environment finding, not a code defect)
- Input: `GET /auth/google-photos/status`, `GET /auth/google-photos/connect`,
  `GET /auth/google-photos/callback?state=bogus`, missing-state callback,
  all against the already-running `:8000` uvicorn process (per task
  instruction: do not restart it), with a freshly-signed-up authenticated
  test user's session cookie
- Expected: `status` 200 not-connected; `connect` 302 to a Google OAuth URL
  with the `photospicker.mediaitems.readonly` scope and a `state` param;
  bogus/missing-state `callback` rejected generically (302 to a Settings
  error flag, no stack trace)
- Actual: **all four returned 404 `{"detail":"Not Found"}`**. Root cause
  confirmed, not a routing bug: `ps -o lstart` shows the running uvicorn
  process (`pid 4109`) started **2026-07-12 21:25:39**, and
  `git log` shows the F17 backend commit (`8a76d55`) landed at
  **2026-07-12 22:03:42** — the live process predates the code that adds
  `routes/google_photos.py` and its `main.py` mount by ~38 minutes, and
  was started without `--reload`, so it is serving a stale in-memory app
  build with no knowledge of the new router at all.
  `curl http://localhost:8000/openapi.json` confirms zero `google` paths
  in the running app's schema. This is an **environment/process-lifecycle
  gap, not a code defect**: `dev/backend/app/main.py` (as committed)
  correctly imports and mounts `google_photos.router`
  (`app.include_router(google_photos.router)`, confirmed by direct read),
  and the in-process pytest suite (which imports `app.main.app` fresh,
  not the long-lived uvicorn process) exercises every one of these routes
  successfully (see the route-file scenario above) — so the routes are
  known-working in the current codebase, just not reachable on the
  currently-running port-8000 process without a restart.
- Result: **BLOCKED (environment), not a FAIL of the code under test** —
  live curl verification of F17's backend routes could not be completed
  against the running dev server per the explicit "do NOT restart them"
  instruction. Recommend deploy-agent (or an explicit human-approved
  restart) bring `:8000` current before any further live smoke pass on
  F17; the in-process TestClient suite above is the authoritative
  confirmation these routes work correctly today.
- Evidence: `ps -o pid,lstart,command -p 4109`; `git log -3` on
  `dev/backend`; `curl -s http://localhost:8000/openapi.json` (no
  `google` paths present); `grep -n google_photos app/main.py` (confirms
  the router is mounted in the committed code).

## Scenario: cross-family / unauthenticated 401/404 on picker-session and import routes
- Input: `POST /profiles/{id}/google-photos/picker-sessions`,
  `POST /profiles/{id}/photos/import-from-google` for an unauthenticated
  caller and a cross-family profile id
- Expected: 401 unauthenticated, 404 cross-family
- Actual: not independently live-curl-verified for the same stale-process
  reason as above; **verified instead via the committed integration suite**
  (`test_create_picker_session_cross_family_profile_404`,
  `test_import_cross_family_profile_404`,
  `test_connect_requires_authentication`,
  `test_callback_requires_authentication`,
  `test_status_requires_authentication`,
  `test_disconnect_requires_authentication`,
  `test_create_picker_session_not_connected_returns_409`,
  `test_import_requires_connection`), all passing in the 275/275 run above
- Result: PASS (via integration suite; live-curl portion blocked per the
  scenario above)

## Scenario: frontend Settings page renders without a client error
- Input: authenticated `curl` of `http://localhost:3000/` (the SPA root —
  `Settings`/`GooglePhotosCard` are client-rendered, not a separate
  file-route, confirmed by `find app -maxdepth 3` showing no `/settings`
  route file), plus inspection of the frontend dev server's live compile
  log (`/private/tmp/lm-frontend.log`)
- Expected: 200, no Next.js error-boundary markers, no compile errors
  referencing the new F17 components
- Actual: root request returns 200; dev-server log shows only benign
  `Cross origin request detected` dev-mode warnings and normal
  `✓ Compiled` lines, zero errors, and no compile failure at any point
  since the F17 frontend commit landed (the dev server has been running
  continuously and Next's dev server recompiles per-request on file
  change, unlike the backend's non-reloading uvicorn process — confirmed
  the frontend process is not subject to the same staleness as the
  backend). `tsc --noEmit` is clean (see above). Full behavioral
  confirmation (does the rendered DOM actually show the Google Photos
  card after client-side auth) requires browser automation this
  environment doesn't have — **same partial-pass framing used at the
  Increment 6 (F12) Test gate**, not claimed as a full pass.
- Result: PARTIAL PASS (consistent with the F12 precedent's framing) — no
  evidence of a client error; full DOM-level confirmation unverifiable
  without browser automation.
- Evidence: `curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/`
  → `200`; `/private/tmp/lm-frontend.log` tail (no error lines).

## Scenario: live OAuth round-trip with real Google credentials
- Input: N/A — no live Google OAuth credentials exist in this environment
- Expected/Actual: not attempted; **this is a pre-existing, already-
  recorded known limitation** (Google OAuth app verification / real
  credential exchange), consistent with ARCHITECTURE_KB §12.3's own
  "Testing" mode / go-live-checklist framing and not re-litigated here as
  a new finding
- Result: N/A (environment limitation, not a test failure)
