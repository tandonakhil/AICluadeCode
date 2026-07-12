# Unit/Integration Test Evidence — Increment 4 (F14 avatars+upload, F15 Lightbox, F16 Gallery)

Suite: Blocking (Test Policy not marked advisory for this project).
Run: 2026-07-12. Verified independently by test-agent (not re-using code-agent's report).
Repo: `projects/little-milestones/dev/` @ commits `f2ae184` (backend), `69a5cae` (frontend).

## Suite re-run results

| Invocation | Location | Result |
|---|---|---|
| `python -m pytest -v` | `dev/backend` (venv active) | 173 passed, 0 failed, 3 warnings (deprecation only) |
| `pytest -v` | `dev/backend` (venv active) | 173 passed, 0 failed, 3 warnings (deprecation only) |
| `npm test -- --run` (`vitest run`) | `dev/frontend` | 34 passed, 0 failed, 7 test files |

Both backend invocations agree exactly (same 173, same test IDs). Frontend 34/34. Matches code-agent's reported 173/34 — no discrepancy between claimed and actually-observed counts.

No suite here has zero tests; all four target areas (photos, profiles, Avatar, Lightbox/JourneyScreen) have populated, non-trivial test files.

---

### Scenario: security-architect condition 3 — repeated profile-level upload replaces, not accumulates
- Input: `test_photos.py::test_repeated_profile_level_upload_replaces_not_accumulates` — two sequential profile-level (avatar) uploads to the same profile.
- Expected: exactly one `memory_id IS NULL` row remains in `photo_meta` for that profile after the second upload, and it is the new photo's id; old file unlinked from disk, new file present.
- Actual: test asserts `SELECT id FROM photo_meta WHERE profile_id=? AND memory_id IS NULL` returns exactly `[second_id]`; asserts `first_path.exists() == False` and `second_path.exists() == True`. Ran green.
- Result: PASS
- Evidence: `dev/backend/tests/test_photos.py:251-280`; both DB row count and on-disk file count are checked, per the mandate (not just one).

### Scenario: security-architect condition 1 — cross-profile isolation of avatar replacement
- Input: `test_photos.py::test_avatar_replacement_is_cross_profile_isolated` — profile A gets one avatar upload; profile B then receives two sequential avatar uploads.
- Expected: profile A's `memory_id IS NULL` row/file is completely untouched by profile B's replace-cleanup logic.
- Actual: test asserts profile A's row still exists with `profile_id == profile_a`, file still exists, and `SELECT ... WHERE profile_id=profile_a AND memory_id IS NULL` still returns exactly `[photo_a_id]` after B's two uploads. Ran green.
- Result: PASS
- Evidence: `dev/backend/tests/test_photos.py:316-348`

### Scenario: memory-attached photos unaffected by avatar replacement (adjacent coverage, not separately mandated but load-bearing for condition 3's scoping)
- Input: one memory-attached photo upload, then two profile-level (avatar) uploads on the same profile.
- Expected: memory-attached photo row/file survive untouched (cleanup scoped to `memory_id IS NULL` only).
- Actual: row present with correct `memory_id`, file exists. PASS.
- Result: PASS
- Evidence: `dev/backend/tests/test_photos.py:283-313`

### Scenario: cleanup query's `profile_id` filter is explicit in the real SQL (security-architect condition 1, code-level check)
- Input: read `PhotoStore._replace_prior_profile_level_photos` in `dev/backend/app/photos.py`.
- Expected: both the SELECT identifying stale rows and the DELETE removing them filter `profile_id = ?` explicitly, not merely implied by which store/connection instance is in scope.
- Actual: confirmed in code — `SELECT id FROM photo_meta WHERE profile_id = ? AND memory_id IS NULL AND id != ?` (line 233) and `DELETE FROM photo_meta WHERE id = ? AND profile_id = ? AND memory_id IS NULL` (lines 242-243). Both parameterized with `profile_id`.
- Result: PASS
- Evidence: `dev/backend/app/photos.py:228-244`

### Scenario: authz-bypass comment exists (security-architect condition 2, code-level check)
- Input: read the same method's docstring in `dev/backend/app/photos.py`.
- Expected: an explicit one-line (or block) comment stating the cleanup path deliberately bypasses `delete()`'s owner-only authz check, and why it's safe (runs only inside `create()`'s already-authorized upload request).
- Actual: confirmed — docstring lines 223-226: "This also means it bypasses `delete()`'s owner-only authz check (security-architect's condition 2, ARCHITECTURE_KB §9.3) -- safe here because it runs only inside `create()`'s own already-authorized upload request, never as an independently reachable operation."
- Result: PASS
- Evidence: `dev/backend/app/photos.py:216-231`

### Scenario: Avatar.tsx — fallback-to-dot on load error
- Input: `Avatar.test.tsx::"degrades to the fallback dot on image load failure"` — render with `avatar_photo_id` set, fire a synthetic `onError` event on the `<img>`.
- Expected: image element removed, `.lm-identity-dot` fallback rendered with the correct `fallbackColor`.
- Actual: test fires `fireEvent.error(img)`, then asserts `img` is gone and `.lm-identity-dot` present with `background: var(--lm-moss)`. Ran green.
- Result: PASS
- Evidence: `dev/frontend/components/Avatar.test.tsx:58-70`

### Scenario: Avatar.tsx — correct size/ring per surface
- Input: `Avatar.test.tsx` — renders with different `size` props (32/44/56) and a `photoStyle` override (e.g. box-shadow ring).
- Expected: rendered `<img>` width matches the `size` prop in px; `photoStyle` overrides (used by callers for per-surface rings) apply only to the photo variant, not the fallback dot.
- Actual: `"renders a circular photo avatar..."` asserts `img.style.width === "44px"`; `"applies photoStyle overrides..."` asserts `img.style.boxShadow === "0 0 0 2px red"`. Both green. Confirms the size/ring mechanism is exercised at the component level (actual per-surface values — 32px ring / 44px ring / 56px border — are wired in `ProfileSwitcher`/`TodayScreen`/`JourneyScreen`, not re-tested per call site here, which is a reasonable scope boundary for a shared-component unit test).
- Result: PASS
- Evidence: `dev/frontend/components/Avatar.test.tsx:46-56, 72-84`

### Scenario: Lightbox.tsx — Escape dismiss
- Input: `Lightbox.test.tsx::"calls onClose on Escape"` — `fireEvent.keyDown(document, { key: "Escape" })`.
- Expected: `onClose` called exactly once.
- Actual: PASS, `onClose` called once.
- Result: PASS
- Evidence: `dev/frontend/components/Lightbox.test.tsx:38-45`

### Scenario: Lightbox.tsx — backdrop dismiss, image/caption click does not dismiss
- Input: click on `.lm-lightbox-img`, then click on `.lm-lightbox-backdrop`.
- Expected: image click does not close; backdrop click does.
- Actual: PASS as specified.
- Result: PASS
- Evidence: `dev/frontend/components/Lightbox.test.tsx:47-59`

### Scenario: Lightbox.tsx — multi-photo nav vs. single-photo no-nav
- Input: single-photo list (no nav buttons expected) vs. 3-photo list with ArrowLeft/ArrowRight and visible prev/next buttons.
- Expected: single-photo list renders no Next/Previous buttons; multi-photo list navigates via both keyboard and button click, with a dot per photo.
- Actual: PASS — `"renders no nav controls for a single-photo list"`, `"navigates with ArrowRight/ArrowLeft..."`, `"navigates via visible prev/next buttons and shows a dot per photo"` all green.
- Result: PASS
- Evidence: `dev/frontend/components/Lightbox.test.tsx:61-92`

### Scenario: Lightbox.tsx — focus-trap (Tab cycling) and focus-return-to-trigger — GAP
- Input: code inspection of `dev/frontend/components/Lightbox.tsx` (Tab-trap logic, lines ~59-74) and `dev/frontend/components/JourneyScreen.tsx` (`closeLightbox`'s `lastTriggerRef.current?.focus()`, lines ~75-78).
- Expected (per task item 4 and the commit message's own claim — "Tab-trapped controls, and focus returned to the trigger on close"): a test exercising Tab/Shift+Tab wrap-around among the dialog's own controls, and a test confirming focus returns to the originating `.lm-photo-trigger` button after `onClose` fires.
- Actual: **Neither behavior is tested.** `Lightbox.test.tsx` only tests focus-on-open (`"moves focus to the close button on open"`) — it does not fire any `Tab`/`Shift+Tab` keydown to verify the trap actually cycles among close/prev/next rather than escaping to the document body. `JourneyScreen.test.tsx` opens the Lightbox from a gallery tile and asserts the dialog appears, but never asserts on `document.activeElement` after `onClose` to confirm focus actually returns to the triggering `.lm-photo-trigger` button. Both behaviors are implemented in shipped code (confirmed by direct code read) but are not covered by any automated regression test — a real gap between the commit message's claim ("Tab-trapped controls, and focus returned to the trigger on close" presented as already covered by "34 frontend tests pass") and actual test coverage.
- Result: FAIL (gap — code exists, test coverage does not)
- Evidence: `dev/frontend/components/Lightbox.tsx:39-80` (implementation); `dev/frontend/components/Lightbox.test.tsx` (no Tab/Shift+Tab test, no post-close `document.activeElement` assertion); `dev/frontend/components/JourneyScreen.test.tsx` (no focus-return assertion in the one Lightbox-opening test at lines 103-120).

### Scenario: `next build` not run against the live dev server's `.next/` dir
- Input: `git diff HEAD -- frontend/tsconfig.json frontend/next-env.d.ts`; `git log --oneline -- frontend/tsconfig.json`; `git show 69a5cae -- frontend/tsconfig.json frontend/next-env.d.ts frontend/next.config.js`.
- Expected: no incidental tsconfig.json/next-env.d.ts diffs from an accidental `next build` against the live `.next/` dir during Increment 4.
- Actual: `tsconfig.json` has exactly one commit in its history (Increment 1, `928cc85`) and zero diffs since; the Increment-4 frontend commit (`69a5cae`) touches neither file (empty diff for both). The only historical `next-env.d.ts` diff (adding `/// <reference path="./.next/types/routes.d.ts" />`) is from an unrelated, earlier commit (`0548e1f`, an Increment-1 Review-gate finding about a stale-age backstop check, dated 2026-07-11, well before Increment 4's work). `next.config.js` sets `distDir: process.env.NEXT_DIST_DIR || ".next"` with a comment explicitly noting the isolation ("live dev server is never [touched]... with NEXT_DIST_DIR=.next-build"), and the Increment-4 commit message states `next build clean (via NEXT_DIST_DIR, incidental tsconfig.json/next-env.d.ts changes reverted)`, consistent with the observed empty diff. Working tree is clean (`git status --porcelain` empty).
- Result: PASS
- Evidence: `dev/frontend/next.config.js:12-14`; `git show 69a5cae --stat`; commit `69a5cae`'s message.

---

## Coverage gaps vs. claimed coverage

1. **Lightbox focus-trap and focus-return-to-trigger are implemented but untested.** code-agent's Increment-4 commit message explicitly claims "Tab-trapped controls, and focus returned to the trigger on close" as part of what F15 ships, and frames it alongside "34 frontend tests pass" — read together this reads as if the behavior is covered, but it is not. This is a real gap between claimed and actual test coverage on an accessibility-load-bearing interaction (keyboard-only users must be able to both stay trapped in the dialog and return correctly to their place in the page). Not a blocker on functional correctness (manual code read confirms the implementation itself looks correct), but it is a gap in verified regression protection — a future refactor could silently break either behavior with no test catching it.

All other mandated items (both security-architect regression tests, the explicit `profile_id` filter, the authz-bypass comment, Avatar fallback/size-ring coverage, Lightbox Escape/backdrop/multi-nav coverage, and the `next build` non-contamination check) are confirmed present and correct.

## Gate verdict

**Backend: 173/173 pass (both invocations agree). Frontend: 34/34 pass.** All Architecture §9.3 / security-architect-mandated tests exist, are meaningful (real DB-row + on-disk-file assertions, real cross-profile isolation assertions), and pass. Both security-architect code-level conditions (explicit `profile_id` filter, authz-bypass comment) are independently confirmed in the actual source, not assumed from a comment claim. `next build` contamination check is clean.

One coverage gap found: Lightbox's Tab-trap and focus-return-to-trigger behaviors are shipped but not test-covered, despite being called out in the commit message as delivered. This suite is **blocking** for this project (no advisory suites are recorded in PROJECT_CONTEXT.md's Active Team section for little-milestones). Recommend: do not treat this as grounds to fail the whole gate outright (it is a missing-test gap, not a failing/broken-behavior gap — the underlying code was read and appears correct), but it should be sent back to code-agent to add the two missing test cases before this gate closes, consistent with "a suite with zero tests [or a gap in mandated coverage] is not the same as a passing suite — say so explicitly."

**Verdict: hold — send back to code-agent for two additional Lightbox tests (Tab/Shift+Tab focus-trap cycling; focus returns to `.lm-photo-trigger` after close) before this gate is marked fully passing.** Everything else re-verified and passing.
