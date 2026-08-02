# Test evidence — unit/integration suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `test-agent` (authored and executed)
**Blocking:** yes (Test Policy: **all suites blocking**, no advisory exception recorded)
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest backend/tests`
**Exit code:** 0
**Scenarios: 2,028 — PASS 2,028, FAIL 0, SKIP 0**

The whole tree (`backend/tests` + `tests/suites`) collects **2,692** and passes
in file order in 194.8s, exit 0. The figure above is `backend/tests` alone.

---

### Scenario: the suite executes and passes in collection order
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest backend/tests -p no:cacheprovider`
- Expected: exit 0, every scenario passes, none skipped
- Actual: **2,028 passed, 0 failed, 0 skipped**, exit 0, 124s wall
- Result: PASS
- Evidence: progress-character tally `Counter({'.': 2028})` — no `F`, `E`, `s`
  or `x` anywhere in the run

### Scenario: the whole tree passes together
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest` (testpaths = `backend/tests tests/suites`)
- Expected: 2,692 collected, all pass
- Actual: **2,692 passed**, exit 0, `real 194.82`
- Result: PASS
- Evidence: `Counter({'.': 2692})`

### Scenario: the collected count is what it is claimed to be
- Status: EXECUTED
- Input: `pytest --collect-only -q`, summed per tree
- Expected: 2,692, matching the brief
- Actual: `backend/tests 2028`, `functional 354`, `red-team 61`,
  `architecture 26`, `security 14`, `industry 23`, `ux 186` — **total 2,692**
- Result: PASS
- Evidence: every per-suite figure below is the collected count for that suite,
  and the seven sum to the whole-tree collection exactly.

### Scenario: the result does not depend on collection order
- Status: EXECUTED
- Input: five further orderings under this agent's own plugin
- Expected: 2,692 pass in all
- Actual: 2,692 pass in all six orderings
- Result: PASS
- Evidence: `order-independence-2026-08-02.md`, which is the full record.

---

## Test-count delta — against the previous run (`dev` @ `55878c9`, 2026-07-31)

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 2,000 | **2,028** | **+28** |
| functional | 354 | 354 | — |
| red-team | 61 | 61 | — |
| architecture | 26 | 26 | — |
| security | 14 | 14 | — |
| industry | 23 | 23 | — |
| ux | 186 | 186 | — |
| **total collected** | **2,664** | **2,692** | **+28** |

**Tests added: 28. Tests removed: 0. Tests changed: 1.**

The +28 is accounted for exactly, with no residue — 27 new test functions
across two new files, one of which is parametrized over the two participating
modules (28 node IDs):

* `backend/tests/test_pilot_process_state.py` — **16 functions, 17 node IDs**
  (`test_every_module_level_mutable_binding_is_classified` is parametrized over
  `app.ui.state` and `app.pilot_close`). Covers what is declared, what
  restoring does, and the AST guard.
* `backend/tests/test_pilot_test_binding.py` — **11 functions, 11 node IDs**.
  Covers the one-binding-per-process fix, the pinned client token, and rebuild
  semantics.

**Removed: none.** Verified two ways — `git diff 55878c9..fc197a6` over the
test tree contains **zero** removed `def test_`/`class Test` lines, and no test
file was deleted (`git diff --stat` shows 10 files changed, 0 deleted).

**Changed: one**, and it asserts strictly more —
`test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_field_not_a_guess`
gained **three assertions and zero removals**. Full diff analysis in
`order-independence-2026-08-02.md` §5.

This is a delta against a real previous run, not a baseline: the previous
figures come from the 2026-07-31 corpus at `55878c9`.
