# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `functional-design-agent` (executed by `test-agent`)
**Blocking:** yes (project Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**358 scenarios, 358 pass, 0 fail, 0 skip, exit 0.**
Entry point: `bash tests/suites/functional/run.sh` (delegates to `tests/suites/_runner.sh`,
which returns 3 for an empty suite and 4 for cannot-execute — neither occurred).
Interpreter `dev/.venv/bin/python`. Re-run again inside six whole-tree runs.

**Test-count delta vs `1b1b56e`: 355 → 358, +3 added, 0 removed. The three are the whole-surface disclosure guard and the two `unregistered_actors` scenarios.**

---

### Scenario: the suite entry point executes
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0
- Actual: **exit 0, 358 ran, 0 failed**
- Result: PASS
- Evidence: `scratchpad/p19/suite-functional.txt`; collected node ids under
  `tests/suites/functional/` = 358, matching the executed count exactly

### Scenario: the suite is not empty and not silently shrinking
- Status: EXECUTED
- Expected: a non-zero scenario count, and any drop explained
- Actual: **358 scenarios. 355 → 358, +3 added, 0 removed. The three are the whole-surface disclosure guard and the two `unregistered_actors` scenarios**
- Result: PASS

### Scenario: the suite passes under five independent collection orderings
- Status: EXECUTED
- Input: test-agent's own out-of-tree salted plugin, five orderings
- Expected: identical node-id set, all pass
- Actual: **identical set (`sort | md5` = `15e22b1a…` on all five), all pass**
- Result: PASS
- Evidence: `order-independence-2026-08-03.md`

---

## The three findings gate 8 blocked on last pass — all three closed

### Scenario: F1 — the `AC-F5-02` claim is gone from the four agent pages
- Status: EXECUTED
- Input: the served agent pages, read in Chromium; and the source of
  `backend/app/ui/pages.py`
- Expected: the sentence on none of the four
- Actual: **gone from all four.** `grep` across `dev/` finds the string in
  exactly three places: the test constant `UNQUALIFIED_F5_02_CLAIM`, and two
  code comments (`pages.py:3612`, `:4128`) recording that it used to be there.
  Playwright read `unqualified: false` and `discloses: true` on all four pages
- Result: PASS
- Evidence: `rendered-ui-2026-08-03.md`; screenshot
  `ui-agent-page-absent-agent-1280-2026-08-03.png`

### Scenario: F1 — the guard is re-scoped to "no reachable screen"
- Status: EXECUTED
- Expected: whole reachable surface + post-control documents, and the four pages
  asserted IN the traversed set by the broker's own absent ids
- Actual: **confirmed and mutation-held both ways** — restoring the sentence
  fails naming five pages; crippling the traversal to reach nothing also fails
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` M1, M2a. Independently corroborated
  over real HTTP by smoke S27 — 46 URLs crawled from `/`, zero offenders, five
  agent pages actually reached

### Scenario: F2 — `AC-F5-07` asserts every agent row, labels and values
- Status: EXECUTED
- Expected: mutation F7-M now fails; the sibling's counting assertion is gone
- Actual: **F7-M FAILS. The `len(lineage) == len(rows)` count became
  containment and attributing every view to agent 0 FAILS**
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` F7-M, M5, M6

### Scenario: F3 — `unregistered_actors` returns register 33's UNKNOWN shape
- Status: EXECUTED
- Expected: one scenario asserts the shape, one joins `computable: False` to the
  `LINEAGE_UNTRAVERSED` entry justifying it, and it is rendered on `/inventory`
- Actual: **all three confirmed.** Four mutations caught
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` F3-M1…M4; smoke S26; the rendered
  answer measured at `data-computable="false"`, `display:block`,
  compounded opacity `1.0`, 1036 × 148.5 px

---

## Findings from THIS pass — two defects and one wording issue

### Finding A: `AC-F40-16`'s "every produced file" is asserted of one file
- Status: EXECUTED · Result: **FAIL**
- The rewrite from `entries[-1]` to a loop cannot fail differently: the register
  holds exactly one entry in that scenario. Full detail and the probe output in
  `sampling-sweep-2026-08-03.md`, Finding A

### Finding B: `obligation_gap` lost four literal-value assertions
- Status: EXECUTED · Result: **FAIL**
- Rewording all three `scheduled_reversal` labels to generic words leaves
  **2,987 green**. The rewritten scenario compares the evaluator's output to the
  constant the evaluator reads. Detail in `sampling-sweep-2026-08-03.md`,
  Finding B

### Observation 3: a docstring that its own scenario contradicts
- Status: EXECUTED · Result: **PASS with a note — not a suite failure**
- `test_the_broker_answers_the_population_question_UNKNOWN_and_not_none` says it
  asserts the shape *"so it holds on the day findings become ledger-recorded and
  the answer becomes computable"*. It asserts `answer["computable"] is False`,
  and mutation F3-M2 confirms it **fails** the moment that becomes true. The
  assertion is right — the day it changes should force a revisit — but the
  sentence describing it is not. In a project that has twice been blocked for a
  claim outrunning its evidence, a test's own docstring is worth the same
  standard. For `code-agent`, non-blocking
