# Unit/integration + live end-to-end smoke — 2026-07-31 (test-agent)

Run by test-agent, 2026-07-31, in response to a human report that "the app is
still not working, it is throwing an error" (exact error text not supplied —
reproduction was the priority). Suite policy: **blocking** (no advisory
marking on record for unit/integration or live smoke). Servers were already
running when invoked (backend PID 16751 on 127.0.0.1:8000, Next.js on :3000);
no long-lived process was started inside this turn.

Commits at HEAD: `f292506` (red-team false-alarm fix) on `main`.

## Per-suite status
- Backend pytest — **EXECUTED**, exit 0.
- Frontend vitest — **EXECUTED**, exit 0.
- Mobile jest (RNTL) — **EXECUTED**, exit 0 (with a cold-start flake, below).
- Live end-to-end smoke (curl, real running app) — **EXECUTED**.
- Rendered-UI / web (Playwright) — **STATIC ONLY — NOT EXECUTED**: Playwright
  is not installed in `dev/frontend` (`node_modules/.bin/playwright` absent).
  To run, Playwright + a browser download would have to be installed.

## Test-count delta
- Backend: 275 (2026-07-13, increment7) / 284 (2026-07-26, mobile evidence
  prose) → **294** now. Net **+10 vs the 2026-07-26 baseline** (+19 vs 07-13).
  Movement is growth; no drop. A per-test manifest for the prior run is not on
  record, so individual renames can't be diffed, but no coverage-count loss.
- Frontend: 80/80 across 15 files (2026-07-13) → **80/80 across 15 files** now.
  Count held exactly. Cannot rule out silent 1:1 replacement without a prior
  per-test name list, but no count drop.
- Mobile jest: no prior numeric jest count on record (prior mobile evidence
  2026-07-26 was iOS-simulator-based, not jest). Reported here as **baseline:
  7 tests across 2 files** (`journey.test.tsx` 4, `ask.test.tsx` 3).

---

### Scenario: backend pytest full suite
- Input: `cd dev/backend && source .venv/bin/activate && python -m pytest -v`
- Expected: full suite passes
- Actual: `294 passed, 3 warnings in 73.17s`. Warnings are pre-existing
  deprecation notices (passlib argon2 `__version__`, FastAPI `on_event`
  startup) — unrelated to any failure.
- Result: PASS
- Evidence: pytest summary line `294 passed, 3 warnings in 73.17s`

### Scenario: frontend vitest full suite
- Input: `cd dev/frontend && npx vitest run`
- Expected: full suite passes
- Actual: `Test Files 15 passed (15)`, `Tests 80 passed (80)`, 7.12s
- Result: PASS
- Evidence: vitest summary block, exit 0

### Scenario: mobile jest (RNTL) full suite
- Input: `cd dev/mobile && npm test` (jest, jest-expo preset)
- Expected: full suite passes deterministically
- Actual: `Tests: 7 passed, 7 total` across `journey.test.tsx` and
  `ask.test.tsx` — BUT the **first** invocation of the run returned
  `Tests: 2 failed, 5 passed`. The two failures were in `ask.test.tsx`
  ("offers a way into past conversations", "lists past conversations and can
  open one"), both `render function has not been called` — the render helper
  aborted so `screen` had no tree, preceded by `act(...)` warnings from
  `AskScreen` effects (`setPrompts`/`setStageSentence` at
  `src/screens/AskScreen.tsx:93-94`) firing after teardown.
- Result: PASS (deterministic content) with a FLAKINESS FINDING
- Evidence: `ask.test.tsx` run in isolation = 3/3 pass; full suite re-run 5
  consecutive times = `7 passed` every time. The failure reproduced only on a
  cold first run (async prompt-fetch effect racing the `waitFor` timeout
  before jest-expo transform cache is warm). Non-deterministic, not a
  hard failure, but a real test-isolation/timing weakness in `ask.test.tsx`.

### Scenario: live GET /health
- Input: `curl -s -i http://localhost:8000/health -H "Origin: http://localhost:3000"`
- Expected: 200 + `{"status":"ok"}` + CORS allow headers for localhost:3000
- Actual: `HTTP/1.1 200 OK`, body `{"status":"ok"}`,
  `access-control-allow-origin: http://localhost:3000`,
  `access-control-allow-credentials: true`
- Result: PASS
- Evidence: raw response captured above

### Scenario: live auth flow — signup + session cookie
- Input: `POST /auth/signup` with `Origin: http://localhost:3000`, cookie jar,
  `{"email":"tester_<ts>@example.com","password":"testpass123"}`
- Expected: 201, `Set-Cookie: lm_session=...`, user body
- Actual: `HTTP/1.1 201 Created`, `set-cookie: lm_session=...; HttpOnly;
  Max-Age=2592000; Path=/; SameSite=lax`, body user id 19 family_id 15 owner
- Result: PASS
- Evidence: cookie jar populated with `lm_session`

### Scenario: live on-load endpoints (authenticated)
- Input: `GET /auth/me`, `GET /profiles`, `GET /auth/sessions` with session
  cookie + `Origin: http://localhost:3000`
- Expected: 200s; empty profiles for a new user
- Actual: `/auth/me` 200 (user echoed); `/profiles` 200 `[]`; `/auth/sessions`
  200 (one current web session). (`/products` unprefixed = 404, expected — it
  is `/profiles/{id}/products`.)
- Result: PASS
- Evidence: raw responses captured above

### Scenario: live feature endpoints on a real profile
- Input: created profile id 9 (`Testchild`, DOB 2025-01-15), then
  `GET /profiles/9/{suggested_prompts,timeline,activities,products,memories,chat_sessions}`
- Expected: all 200 with age-scoped content
- Actual: all `[HTTP 200]` — suggested_prompts (age-18mo chips), timeline
  (7 chapter markers), activities (2 + coming_next), products (2 items),
  memories `[]`, chat_sessions `[]`. Every payload carries the exact medical
  disclaimer constant.
- Result: PASS
- Evidence: raw responses captured above

### Scenario: live POST /chat — real Anthropic LLM call
- Input: `POST /chat` `{"profile_id":9,"message":"What activities help an 18
  month old?"}` with session cookie + `Origin: http://localhost:3000`
- Expected: 200 with guarded, disclaimer-bearing text (this is the dependency
  most likely to 500 — ANTHROPIC_API_KEY / model name)
- Actual: `HTTP 200` in 7.54s. Real generated reply referencing Testchild,
  age-appropriate activities, closing with the exact disclaimer constant and
  `session_id: 9`. `.env` has a valid `sk-ant-api03-` key (len 108) and
  `ANTHROPIC_MODEL=claude-sonnet-5` — the model resolves and answers.
- Result: PASS — no 500, no missing-key failure, no unhandled exception
- Evidence: full JSON response captured; `time_total=7.540865s`

### Scenario: CORS trap — 127.0.0.1:3000 vs localhost:3000 (ROOT-CAUSE PROBE)
- Input: `OPTIONS /profiles` preflight with `Origin: http://127.0.0.1:3000`
  vs `Origin: http://localhost:3000`; also actual `GET /auth/me` at 127.0.0.1
- Expected: localhost allowed; 127.0.0.1 rejected (per the origin convention)
- Actual:
  - `localhost:3000` preflight → `200`, `access-control-allow-origin:
    http://localhost:3000` present.
  - `127.0.0.1:3000` preflight → **`400 Bad Request`, NO
    `access-control-allow-origin` header** → a browser blocks the request.
  - `GET /auth/me` at 127.0.0.1 origin → 401 with no allow-origin header.
- Result: PASS (backend behaves exactly as designed) / this is the most
  likely explanation for the human's "throwing an error"
- Evidence: raw header captures above. In the browser this surfaces via
  `app/page.tsx` — a rejected `getMe()` sets `loadError` and renders
  `role="alert"`: "Could not reach the server — check that the backend is
  running, then reload." The backend is healthy; only the wrong origin breaks.

### Scenario: allowed-origin whitelist matches this machine
- Input: verified each `EXTRA_CORS_ORIGINS` entry against the live server;
  checked current LAN IP + hostname
- Expected: LAN/mDNS origins the human might use are whitelisted
- Actual: allowed = `localhost:3000`, `10.0.0.47:3000`,
  `akhils-macbook-pro.local:3000`, `localhost:8081` (all preflight 200 with
  matching allow-origin). Current LAN IP is still `10.0.0.47`; hostname
  `Akhils-MacBook-Pro.local` (browser lowercases the Origin header → matches
  the whitelisted lowercase entry). No stale/missing LAN origin found.
- Result: PASS — the only unreachable common origin is `127.0.0.1:3000`

### Scenario: rendered-UI web verification (Playwright)
- Input: intended to drive a real browser at localhost:3000 for computed
  styles / a11y tree / screenshots
- Expected: EXECUTED
- Actual: **NOT EXECUTED** — Playwright is not installed in `dev/frontend`.
- Result: STATIC ONLY — NOT EXECUTED
- Evidence: `ls node_modules/.bin/playwright` → absent; `npx playwright
  --version` → not found. Would require installing `@playwright/test` + a
  browser to run.
