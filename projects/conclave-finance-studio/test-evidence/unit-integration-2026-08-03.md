# Test evidence — unit / integration suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — **re-run** after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent` (this suite is mine; the other six belong to their SMEs)
**Blocking:** yes — `PROJECT_CONTEXT.md` Active Team: *"Test Policy: all suites
blocking. No advisory exceptions."*
**Status:** `EXECUTED`
**Command:** `.venv/bin/python -m pytest backend/tests -o addopts="" -q -p no:cacheprovider`
**Exit code:** 0
**Scenarios: 2,302 — PASS 2,302, FAIL 0**

The whole tree (this suite plus the six SME suites) is **2,977** and was run to
completion **six times** in six different orders, exit 0 each time — see
`order-independence-2026-08-03.md`.

## Test-count delta since the previous run (`dev` @ `6bf8ed9`, 2,955)

Computed by collecting node IDs at both commits and diffing the sorted sets.

| | count |
|---|---|
| previous total | 2,955 |
| **added** | **+25** |
| **removed** | **−3** |
| **changed (same node ID, changed body)** | **3** |
| **current total** | **2,977** |

The 25 added and 3 removed are enumerated per scenario in
`changed-scenario-audit-2026-08-03.md`. **The three removals are a coverage
decision and are put in front of the human there, not buried in a diff** — all
three were the scenarios that made the false `AC-F5-02`/`-03`/`-05` claims gate
8 blocked on.

---

### Scenario: the whole unit/integration tree runs clean
- Status: EXECUTED
- Input: `pytest backend/tests` at `1b1b56e`
- Expected: exit 0, no failures, no errors, no skips reported as passes
- Actual: **2,302 passed in 131.06s**, exit 0
- Result: PASS
- Evidence: `2302 passed in 131.06s`

### Scenario: the collected total is exactly the count the brief states
- Status: EXECUTED
- Input: `--collect-only` over `backend/tests` and `tests/suites`
- Expected: 2,977 = 2,955 + 25 − 3
- Actual: **2,977 collected**, summing to 2,977 across the seven suites
  (2,302 + 355 + 194 + 61 + 28 + 23 + 14)
- Result: PASS
- Evidence: per-file collection sum `SUM: 2977`; sorted node-ID file 2,977 lines

### Scenario: no suite is empty
- Status: EXECUTED
- Input: each `tests/suites/<suite>/run.sh` plus `backend/tests`
- Expected: every suite has at least one `test_*.py` and collects >0
- Actual: **all seven collect >0.** The shared runner exits 3 on an empty suite
  and did not; smallest suite is `security` at 14
- Result: PASS
- Evidence: `_runner.sh` exit codes all 0; no `NO SCENARIOS DEFINED` line emitted

### Scenario: `test_ui_no_orphaned_style_rule.py` — the new orphaned-rule checker
- Status: EXECUTED
- Input: the file added at `0470aba`/`1b1b56e`
- Expected: the checker runs and passes
- Actual: **19 passed.** Note the count: `code-agent`'s hand-off says
  **22 scenarios**; the file contains **19** (5 parser + 8 matcher + 6 build).
  The remaining 3 of the 22 are in other files (2 in `test_ui_boundaries.py`,
  1 in `test_ui_governance_screens.py`). A naming discrepancy, not a shortfall
  — all 22 exist and all 22 run
- Result: PASS (with the count restated)
- Evidence: `backend/tests/test_ui_no_orphaned_style_rule.py 19 passed in 1.63s`

### Scenario: the orphan sweep passes over the REAL surface, no exemptions
- Status: EXECUTED
- Input: `cssmatch.orphans(chrome.STYLESHEET, surface, NO_EXEMPTIONS)` over
  15 link-reachable URLs + 4 declared coverage states + the driven-control
  documents + a dark-theme copy of each
- Expected: `[]`
- Actual: **`[]`**, with `NO_EXEMPTIONS == {}` asserted in the same file
- Result: PASS
- Evidence: mutation-proven in `mutation-tests-2026-08-03.md` M1, M1b, M4, M5,
  M6a — every one of which turns this green into a failure

### Scenario: the traversal now reaches post-POST states
- Status: EXECUTED
- Input: `uihelpers.documents_from_driving_the_controls` step 7b — the three
  fetches added at `1b1b56e` that go BACK to `/approvals/<id>`,
  `/proposal/<id>` and `/approvals` after the approval POST
- Expected: `.seal` and `.card.approved` are matched by the surface
- Actual: **both matched.** Removing the three fetches makes them orphans:
  `['.seal', '.card.approved']`
- Result: PASS
- Evidence: mutation M4. The two rules that "looked dead" are live, and were
  only ever invisible because no traversal revisited an approved artefact

### Scenario: no vacuous pass in the tree
- Status: EXECUTED
- Input: AST sweep of all 110 test files for functions with no `assert`, no
  `pytest.raises`, no `pytest.fail`
- Expected: every such function asserts through a helper that can raise
- Actual: **13 candidates, all 13 assert-by-helper, and every helper has a
  paired `pytest.raises` scenario proving it can fail.** Zero vacuous passes
- Result: PASS
- Evidence: `vacuous-and-empty-parametrize-sweep-2026-08-03.md`

### Scenario: no empty `parametrize`
- Status: EXECUTED
- Input: AST sweep for `@pytest.mark.parametrize` with an empty argvalues list
- Expected: none — an empty list collects zero cases and reports as a pass
- Actual: **NONE**
- Result: PASS
- Evidence: `sweeps18.json` `"empty_parametrize": []`

### Scenario: the tree does not write to the developer's live decision ledger
- Status: EXECUTED
- Input: `live_ledger_guard`, session-autouse in both conftests
- Expected: `dev/var/broker_db.sqlite3` byte-identical across every whole-tree
  run
- Actual: **unchanged across all six whole-tree runs.** It grew only under the
  smoke, which drives the real application — disclosed in
  `smoke-test-2026-08-03.md`
- Result: PASS
- Evidence: `assert_nothing_was_refused(guard)` raised in none of the six runs
