# Test evidence — unit / integration

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run, after the `AC-F41-13` ruling was built
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes (project Test Policy: **all suites blocking**, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**3,037 scenarios, 3,037 pass, 0 fail, 0 skip, exit 0.**

Interpreter `dev/.venv/bin/python` (3.9). Entry point
`.venv/bin/python -m pytest -o addopts= -q -p no:cacheprovider`, run on a
verified-clean tree at `7757e0d`, and the same scenarios again in five further
whole-tree runs under alternative collection orders, once more under AST
instrumentation, and once more as a final confirmation after every mutation had
been reverted.

`dev/pytest.ini` carries `addopts = -q`; the runs pass `-o addopts=` so pytest's
own summary line is printed rather than suppressed. The count is taken from that
line and cross-checked against collected node ids (`--collect-only -q`), which
agree exactly at 3,037.

## Test-count delta — measured by comparing collected node ids, not counted

Baseline: `dev` @ **`c428fe5`** (the commit gate 8 pass 20 reported on),
collected in a detached worktree with the same interpreter.

| | Baseline `c428fe5` | Head `7757e0d` | Delta |
|---|---|---|---|
| whole tree | 2,988 | **3,037** | **+49 net** |
| node ids added | — | — | **+54** |
| node ids removed | — | — | **−5** |
| changed in place (same id, different assertions) | — | — | **0** |
| changed in place (parametrisation widened) | — | — | **1** |

### Removed (5) — every one an instructed consequence of the ruling

**A removed test is a coverage decision and is named here in full.**

| Node id | Why it went, and what replaced it |
|---|---|
| `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible` | bore the retired ID. `FUNCTIONAL_SPEC` §28.1 instruction 1: *"Remove the `AC-F41-13` ID from every check that bears it… re-point it at `AC-F41-22` and extend it"* |
| `…::TestNoApproveControlHere::test_no_button_on_this_screen_approves_anything` | folded into the single `AC-F41-22` scenario, per the same instruction — *"so that one ID's evidence is not spread across three independently-named scenarios"* |
| `…::TestNoApproveControlHere::test_no_form_on_this_screen_posts_to_an_approval_endpoint` | folded into the same scenario, same reason |
| `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements` | quantified over **registered** agents — the tautology `FUNCTIONAL_SPEC` §28.2 ruled against. Replaced by `test_AC_F5_07_IS_NOT_MET_…` plus a scope-narrowed `test_every_REGISTERED_agent_row_carries_its_own_version_and_entitlements` |
| `…::TestTheInventoryScreen::test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version` | same cause; replaced by `test_a_lineage_view_is_reachable_from_each_REGISTERED_listed_version` |

**Net coverage of the three folded scenarios did not narrow**: the replacement
`test_AC_F41_22_the_three_elements_are_co_visible_and_nothing_here_approves`
asserts all three clauses (co-visibility, no disclosure, no approving control at
**any permission level**), over 14 finding screens across two personas, with
both approval eligibilities required present. Measured under instrumentation:
its traversal loop iterates 47 URLs and its per-screen loop 14 times.
Mutation-verified — see `mutation-tests-2026-08-04.md` M8.

**Net coverage of the two `AC-F5-07` scenarios did not narrow either**: 2
scenarios became 3, and the criterion moved from *claimed* to *recorded unmet*
in the `_IS_NOT_MET_` shape that fails in either direction.

### Added (54)

| File | Added |
|---|---|
| `backend/tests/test_ui_retained_view.py` (new file) | 33 |
| `backend/tests/test_ui_approvals.py` | 8 |
| `tests/suites/functional/test_f41_retained_view.py` (new file) | 7 |
| `backend/tests/test_ui_governance_screens.py` | 4 |
| `backend/tests/test_ui_review.py` | 2 |

**Every one of the 54 carries at least one `assert` or `pytest.raises`** —
checked by AST over the added node ids, 0 exceptions. Full audit in
`changed-scenario-audit-2026-08-04.md`.

### Changed in place (1, and it is a widening)

| Node id | Change |
|---|---|
| `backend/tests/test_ui_approvals.py::TestReachability::test_the_approval_object_mounts_its_components` | `@parametrize` list gained `approval-detection-evidence` and `evidence-set` (the two new node ids appear in the Added set). **No existing scenario's assertions changed.** |

An AST comparison of every function surviving in both revisions, in all six
touched test files, found **no scenario whose body or decorators changed other
than this one**, and **no docstring-only change**.

### Per-suite collected counts (reconcile to the whole tree)

| Suite | `c428fe5` | `7757e0d` | Δ |
|---|---|---|---|
| `backend/tests` (unit / integration — **this suite**) | 2,310 | **2,352** | +42 |
| `tests/suites/functional` | 358 | **365** | +7 |
| `tests/suites/ux` | 194 | **194** | 0 |
| `tests/suites/red-team` | 61 | **61** | 0 |
| `tests/suites/architecture` | 28 | **28** | 0 |
| `tests/suites/industry` | 23 | **23** | 0 |
| `tests/suites/security` | 14 | **14** | 0 |
| **total** | 2,988 | **3,037** | **+49** |

2,352 + 365 + 194 + 61 + 28 + 23 + 14 = **3,037** — exact.

---

### Scenario: the whole tree collects and runs
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest -o addopts= -q -p no:cacheprovider` at `7757e0d`, tree verified clean
- Expected: every collected node id executes; no error, no skip
- Actual: **`3037 passed in 232.60s`, exit 0**
- Result: PASS
- Evidence: pytest summary line, whole tree, no `-k`, no deselection, no `-x`

### Scenario: the count is the collected node-id count, not a summary line taken on trust
- Status: EXECUTED
- Input: `--collect-only -q -o addopts=` at `7757e0d`
- Expected: exactly 3,037 node ids
- Actual: **3,037**, agreeing with the run
- Result: PASS
- Evidence: `head_ids.txt`, 3,037 lines

### Scenario: the delta against the last reported run is measured, not asserted
- Status: EXECUTED
- Input: node ids collected at `c428fe5` in a detached worktree, `comm`-diffed against head
- Expected: a named added set and a named removed set
- Actual: **+54 / −5 / 1 widened parametrisation = +49 net**, and every removal explained above
- Result: PASS
- Evidence: `base_ids.txt` (2,988 lines) vs `head_ids.txt` (3,037)

### Scenario: no scenario changed its assertions in place while keeping its name
- Status: EXECUTED
- Input: AST comparison of every same-named function in the six touched test files, at both revisions, comparing the dumped body and the decorator source
- Expected: any body change is reported, not inferred from a line count
- Actual: **one change, and it is a parametrisation widening.** Zero silent assertion edits, zero docstring-only edits
- Result: PASS
- Evidence: `changed_bodies.py` output — one `CHANGED BODY/DECORATOR`, two `NEW FILE`

### Scenario: the final run happens on a tree with every mutation reverted
- Status: EXECUTED
- Input: `git status --porcelain` (empty), `git rev-parse --short HEAD` (`7757e0d`), then the whole tree again
- Expected: clean tree, 3,037 pass
- Actual: **clean, `7757e0d`, `3037 passed in 265.67s`, exit 0**
- Result: PASS
- Evidence: the mutation harness reverts each file with `git checkout --` and refuses to continue on a dirty tree; both worktrees used this pass were removed

### Scenario: no suite in this tree has zero scenarios
- Status: EXECUTED
- Input: per-suite collection, and `tests/suites/_runner.sh`'s exit-code contract (3 = no scenarios, 4 = cannot execute)
- Expected: no suite reports 0, no runner returns 3 or 4
- Actual: **seven suites, smallest 14, all six SME runners returned exit 0 with `EXECUTED — suite passed`**
- Result: PASS
- Evidence: the per-suite table above; runner transcripts
