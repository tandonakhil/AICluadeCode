# Regression suite: live LAN/mobile testing defects — 2026-07-11

Suite: unit/integration (frontend regression additions + backend re-run).
Context: three code defects were found and fixed during live LAN/mobile
testing after the Increment-3 gates closed (dev commits 037254d, 561e452,
c3a2bde). The frontend had zero test infrastructure, so a minimal vitest +
jsdom + @testing-library/react setup was added (dev commit b658a2a) and the
regression tests committed as 4b4ef0b. The fourth live finding (`next build`
during `next dev` corrupts `.next/`) is process-level with no code change —
recorded in admin/LESSONS.md, no test possible or attempted.

Runner: `npm test` (vitest run) in `dev/frontend`; `.venv/bin/python -m
pytest` in `dev/backend`. `tsc --noEmit` clean. `next build` deliberately
NOT run (dev server active).

## Defect 1 — hardcoded API_BASE broke SameSite=Lax session cookies (037254d)

### Scenario: API base derived from page hostname (LAN IP)
- Input: `resolveApiBase()` with `window.location.hostname = "10.0.0.47"`, no env override
- Expected: `http://10.0.0.47:8000` (same-site with the page, cookie survives)
- Actual: `http://10.0.0.47:8000`
- Result: PASS
- Evidence: `frontend/lib/api.test.ts` — "derives the backend host from the page's own hostname (LAN IP)"

### Scenario: API base derived from page hostname (localhost)
- Input: `resolveApiBase()` with hostname `localhost`
- Expected: `http://localhost:8000`
- Actual: `http://localhost:8000`
- Result: PASS
- Evidence: `frontend/lib/api.test.ts`

### Scenario: NEXT_PUBLIC_API_BASE_URL overrides derivation
- Input: env `NEXT_PUBLIC_API_BASE_URL=https://api.example.com`, hostname `10.0.0.47`
- Expected: `https://api.example.com` (deploy-agent's explicit seam wins)
- Actual: `https://api.example.com`
- Result: PASS
- Evidence: `frontend/lib/api.test.ts`

### Scenario: SSR fallback with no window
- Input: `resolveApiBase()` in node environment (`typeof window === "undefined"`)
- Expected: `http://localhost:8000`
- Actual: `http://localhost:8000`
- Result: PASS
- Evidence: `frontend/lib/api.test.ts`

## Defect 2 — crypto.randomUUID() throws in insecure contexts (561e452)

### Scenario: secure context uses crypto.randomUUID
- Input: `localMessageId()` with real `crypto.randomUUID` available
- Expected: RFC-4122-shaped UUID string
- Actual: UUID matched `/^[0-9a-f]{8}-.../`
- Result: PASS
- Evidence: `frontend/components/localMessageId.test.ts`

### Scenario: insecure context (crypto present, randomUUID absent)
- Input: `localMessageId()` with `crypto` stubbed to `{}` (plain-HTTP LAN IP behavior)
- Expected: no throw; fallback id `msg-<ts>-<rand>`
- Actual: no throw; id matched `/^msg-\d+-[a-z0-9]+$/`
- Result: PASS
- Evidence: `frontend/components/localMessageId.test.ts`

### Scenario: crypto entirely absent
- Input: `localMessageId()` with `crypto` stubbed to `undefined`
- Expected: no throw; `msg-` fallback id
- Actual: no throw; `msg-` id returned
- Result: PASS
- Evidence: `frontend/components/localMessageId.test.ts`

### Scenario: fallback ids distinct across calls
- Input: two consecutive `localMessageId()` calls in fallback mode
- Expected: distinct values (React list keys)
- Actual: distinct
- Result: PASS
- Evidence: `frontend/components/localMessageId.test.ts`

## Defect 3 — rejected getMe() stranded the shell on "Loading…" (c3a2bde)

### Scenario: pending session check shows Loading
- Input: `<Home />` rendered with `getMe()` never resolving
- Expected: "Loading…" visible (baseline behavior)
- Actual: "Loading…" rendered
- Result: PASS
- Evidence: `frontend/app/page.test.tsx`

### Scenario: rejected getMe() surfaces a visible error
- Input: `<Home />` with `getMe()` rejecting `Error("Failed to fetch")`
- Expected: `role="alert"` with "Failed to fetch"; "Loading…" gone (this was the infinite-Loading regression, including the render-order half of the fix)
- Actual: alert rendered with exact message; no "Loading…" in the document
- Result: PASS
- Evidence: `frontend/app/page.test.tsx`

### Scenario: non-Error rejection gets calm fallback copy
- Input: `getMe()` rejecting a non-Error value (`"wat"`)
- Expected: alert reading "Could not reach the server."
- Actual: exact match
- Result: PASS
- Evidence: `frontend/app/page.test.tsx`

### Scenario: logged-out (null) session still reaches the auth screen
- Input: `getMe()` resolving `null`
- Expected: no alert, no Loading, auth screen shell renders (render-order change must not break the normal path)
- Actual: as expected
- Result: PASS
- Evidence: `frontend/app/page.test.tsx`

## Backend suite re-run (unchanged by this work)

### Scenario: full backend pytest suite
- Input: `.venv/bin/python -m pytest -q` in `dev/backend`
- Expected: 168 passed (no backend changes in this pass)
- Actual: `168 passed, 3 warnings in 3.90s`
- Result: PASS
- Evidence: pytest terminal output, 2026-07-11

## Summary

- Frontend regression suite (new): 12/12 PASS — `Test Files 3 passed (3), Tests 12 passed (12)`
- Backend unit/integration: 168/168 PASS
- `tsc --noEmit`: clean
- Suite is now runnable by name: `npm test` in `dev/frontend`
- Not covered by any test (documented, not silent): the `.next/` corruption
  from running `next build` alongside `next dev` — process discipline only.
