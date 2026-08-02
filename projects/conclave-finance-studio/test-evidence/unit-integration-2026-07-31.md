# Test evidence — unit/integration suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 13 verification)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `test-agent`
**Blocking:** yes (Test Policy: all suites blocking, no advisory exception recorded)
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest backend/tests -q`
**Exit code:** 0
**Scenarios: 2,000 — PASS 2,000, FAIL 0, SKIP 0**

The whole tree (`backend/tests` + `tests/suites`) collects **2,664** and
`.venv/bin/python -m pytest` returns `2664 passed in 53.91s`, exit 0. The
unit/integration figure below is `backend/tests` alone.

---

### Scenario: the suite executes and passes in collection order
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest backend/tests -q --override-ini="addopts="`
- Expected: exit 0, no skips
- Actual: `2000 passed in 23.10s`
- Result: PASS
- Evidence: `2000 passed in 23.10s`

### Scenario: the whole tree executes and passes
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest`
- Expected: exit 0
- Actual: `2664 passed in 53.91s`
- Result: PASS
- Evidence: `2664 passed in 53.91s`

### Scenario: the whole tree is order-clean under full reversal
- Status: EXECUTED
- Input: a `pytest_collection_modifyitems` plugin reversing the collected list,
  applied to the whole tree (`ORDER_MODE=reverse`)
- Expected: exit 0 — this is the permutation that found the persona leak at gate 8
- Actual: `2664 passed in 54.13s`
- Result: PASS
- Evidence: `ORDER MODE: reverse items: 2664` then `2664 passed`

### Scenario: the `ux` suite is order-clean reversed and under three shuffle seeds
- Status: EXECUTED
- Input: `ORDER_MODE` ∈ {`reverse`, `1`, `7`, `20260731`} over `tests/suites/ux`
- Expected: 186 pass in every permutation
- Actual: 186 passed, four times
- Result: PASS
- Evidence: `186 passed in 14.58s` / `14.76s` / `14.64s` / `14.67s`

### Scenario: an interleaved shuffle of `backend/tests` with `tests/suites` is NOT order-clean
- Status: EXECUTED
- Input: `ORDER_MODE` ∈ {`1`, `7`, `42`, `20260731`} over the whole tree
- Expected: `code-agent` disclosed this as a known, unfixed limitation
- Actual: seed 1 → **2 failed**, seed 7 → **1 failed**, seed 42 → **1 failed**,
  seed 20260731 → 2,664 passed
- Result: **FAIL (disclosed, and verified as pre-existing — see
  `fix-verification-2026-07-31.md` for the reproduction at `9d819c1`)**
- Evidence:
  ```
  seed 1  FAILED tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_07_the_refusals_are_registered_and_therefore_recordable
          FAILED backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[reject-submit]
  seed 7  FAILED tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_07_the_refusals_are_registered_and_therefore_recordable
  seed 42 FAILED backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected
  ```
  Failure text, seed 1: `AssertionError: no control event was recorded for a
  refused selection / assert []` and `AssertionError: reject-submit is mounted
  nowhere on /review/ITEM-21400-CP / assert False` — i.e. the control-event sink
  and the disposition/workflow store, not the viewer session.

### Scenario: the AST guard on `PilotState` fails when a third public attribute is planted
- Status: EXECUTED (mutation)
- Input: `self.last_persona_switch = key` added to `PilotState.view_as`
- Expected: `test_every_publicly_mutable_attribute_of_the_state_is_declared` fails, naming it
- Actual: 2 failed, 7 passed
- Result: PASS (mutation killed)
- Evidence: `AssertionError: these attributes of the process-wide PilotState are
  set outside __init__ and are not in VIEWER_SESSION_ATTRS, so nothing restores
  them between scenarios: {'last_persona_switch': 'view_as'}`. Mutation reverted;
  9 passed.

### Scenario: `export.build`'s no-default guarantee, mutated exactly as gate 8 mutated it
- Status: EXECUTED (mutation)
- Input: `integrity: Dict[str, Any] = {}` restored on **both** `Export.__init__`
  and `build()` — the gate-8 mutation that previously survived all 2,602 scenarios
- Expected: the suite now fails
- Actual: **3 failed**, 2,661 passed
- Result: PASS (mutation killed — it survived at `9d819c1`)
- Evidence:
  ```
  FAILED backend/tests/test_export_integrity_contract.py::test_integrity_has_no_default_on_the_construction_path[build]
  FAILED backend/tests/test_export_integrity_contract.py::test_integrity_has_no_default_on_the_construction_path[Export.__init__]
  FAILED backend/tests/test_export_integrity_contract.py::test_omitting_integrity_is_a_TypeError_rather_than_an_empty_statement
  ```
  And, separately, `Export(..., integrity={})` under the mutation now raises
  rather than constructing: `IntegrityStatementMissing: the export failed at
  evidence_integrity: this export states nothing about anchor.` — the content
  guarantee holds even with the default put back.

### Scenario: the two CONTENT legs of the integrity contract are each load-bearing
- Status: EXECUTED (two mutations)
- Input: (B) the "says something in words" check replaced with `pass`;
  (C) the "names its unmet criterion" check replaced with `if False:`
- Expected: each kills scenarios
- Actual: B → 2 failed; C → 2 failed
- Result: PASS (both mutations killed)
- Evidence: B → `test_declaring_the_residual_with_an_empty_sentence_is_refused[anchor]`
  and `[retention]`; C → `test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]`
  and `[retention-AC-F1-08]`. Both reverted; tree clean at `55878c9`.

---

## Test-count delta — `9d819c1` → `55878c9`

Previous counts were **re-derived**, not trusted from the prior table: `9d819c1`
was checked out into a git worktree and collected there. It collects **2,602**
and runs `2602 passed`, reconciling exactly with the previous run's headline.

Node IDs were diffed set-wise, not compared as totals.

| | Count |
|---|---|
| node IDs at `9d819c1` | 2,602 |
| node IDs at `55878c9` | 2,664 |
| **added** | **+62** |
| **removed** | **0** |
| **changed (same ID, different file/class)** | 0 |

**Nothing was removed and nothing was replaced.** All 62 additions are in five
files, and all five are pass-13 work:

| File | Added | What it covers |
|---|---|---|
| `backend/tests/test_export_integrity_contract.py` | 20 | F3 — the integrity statement's existence and content |
| `backend/tests/test_tier_selection.py` | 17 | A2 — the unknown run tier |
| `backend/tests/test_warehouse_migration.py` | 13 | F1 — a warehouse that already exists |
| `backend/tests/test_ui_state_session.py` | 9 | F2 — the declared viewer-session set and its AST guard |
| `tests/suites/architecture/test_architecture_conformance.py` | 3 | F1 at the pilot's own bootstrap (ARCH_05) |

Per-suite: unit/integration 1,941 → 2,000 (+59); architecture 23 → 26 (+3);
functional 354, security 14, red-team 61, industry 23, ux 186 all unchanged.
