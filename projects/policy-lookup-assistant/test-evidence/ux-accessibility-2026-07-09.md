# Suite: UX/usability + accessibility (ui-ux-designer) — 2026-07-09

Status: **Advisory** (Test Policy set 2026-07-09 — see `PROJECT_CONTEXT.md` Active
Team section for rationale)

**NOT re-run in this session.** No repeatable automated UX/accessibility suite
exists in this codebase — the only real UX verification to date was a one-time
manual Playwright/screenshot session during the frontend's Code gate
(2026-07-06). This file reproduces that prior real result under the new
Advisory reporting format to demonstrate the mechanism; it is not a new test
run and no new evidence was collected today.

### Scenario: Empty state renders per spec
- Input: Load the app fresh (backend :8421, frontend :3421).
- Expected: Scope statement, labeled input, `aria-live` region present, matching UX_KB.md.
- Actual: Matched exactly.
- Result: PASS
- Evidence: Real Playwright/Chromium session, 2026-07-06 (see `PROJECT_CONTEXT.md` "Test Results — Frontend").

### Scenario: Answered state renders per spec
- Input: Ask a grid-maintenance question with a known answer in the corpus.
- Expected: Correct answer text, authority badges with correct colors, filename + as-of date always paired with color, disclosure note present, neutral container.
- Actual: Matched exactly (screenshot verified).
- Result: PASS
- Evidence: Real Playwright/Chromium session, 2026-07-06.

### Scenario: Refused state renders per spec
- Input: Ask an out-of-corpus question.
- Expected: Fixed refusal sentence, scope-statement reminder, slate-tinted container, neutral info-circle icon — not red/error styling.
- Actual: Matched exactly (screenshot verified).
- Result: PASS
- Evidence: Real Playwright/Chromium session, 2026-07-06.

### Scenario: Cross-origin request from real browser
- Input: Submit a question from the frontend origin to the backend API.
- Expected: Request succeeds.
- Actual: **Initially failed** — CORS error, browser-only failure mode curl testing never caught. Fixed with scoped `CORSMiddleware` (`FRONTEND_ORIGIN` env var, not wildcard). Re-verified passing after fix.
- Result: PASS (after fix, re-verified same session)
- Evidence: Real Playwright/Chromium session, 2026-07-06; fix committed `d4e0055`.

## Summary
4/4 scenarios passed (one required and received a fix mid-session before
sign-off), per the 2026-07-06 real browser-based verification. No failures
outstanding. This suite is Advisory as of 2026-07-09: a future failure here
will be reported in full but will not by itself block the Test gate.
