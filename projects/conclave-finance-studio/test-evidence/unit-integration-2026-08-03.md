# Test evidence — unit / integration

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes (project Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**2,309 scenarios, 2,309 pass, 0 fail, 0 skip, exit 0.**
Interpreter `dev/.venv/bin/python` (3.9). Entry point
`.venv/bin/python -m pytest backend/tests`, and the same scenarios again inside
six whole-tree runs (canonical, `file`, `reverse`, three salted shuffles).

Note on output: `dev/pytest.ini` carries `addopts = -q`; adding a second `-q`
suppresses pytest's summary line entirely. Counts below are taken from the
progress characters of each run and cross-checked against collected node ids
(`--collect-only -q -o addopts=`), which agree exactly.

## Test-count delta — measured by comparing collected node ids, not counted

Baseline: `dev` @ `1b1b56e` (the commit gate 8 last reported on), collected in a
detached worktree with the same interpreter.

| | Baseline `1b1b56e` | Head `e00a214` | Delta |
|---|---|---|---|
| whole tree | 2,977 | **2,987** | **+10 net** |
| node ids added | — | — | **+12** |
| node ids removed | — | — | **−2** |
| changed in place (same id, different body) | — | — | **5** |

### Added (12), named individually

| Node id | Why |
|---|---|
| `test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force[1000]` | parametrisation of a scenario that ran one case |
| `…[1]` | below-direction case, previously unrun |
| `…[200.01]` | upper edge |
| `…[49.99]` | lower edge |
| `test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words[scheduled_reversal]` | parametrised over `KIND_VOCABULARY` |
| `…[interface_feed_entry]` | " |
| `…[intercompany_counterparty]` | the kind that was named by no scenario |
| `test_obligation_gap.py::test_no_two_kinds_share_a_label_so_the_words_are_ITS_OWN` | new |
| `test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_01_EVERY_dataset_row_carries_the_nine_attributes` | new |
| `test_unclaimed_criteria.py::test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen` | new (F1) |
| `test_unclaimed_criteria.py::test_the_broker_answers_the_population_question_UNKNOWN_and_not_none` | new (F3) |
| `test_unclaimed_criteria.py::test_the_unregistered_actor_answer_is_not_computable_WHILE_findings_stay_off_the_ledger` | new (F3) |

### Removed (2), named individually — verified NOT a coverage reduction

| Node id | Verdict |
|---|---|
| `test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force` | pre-parametrisation id. Survives as 4 parametrised ids above. **Not deleted.** |
| `test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words` | pre-parametrisation id. Survives as 3 parametrised ids above. **Not deleted.** |

### Changed in place (5)

`AC-F5-07`'s two scenarios, the `AC-F5-02` disclosure scenario, `AC-F40-16`, and
the export reconstruction-field scenario. Four of the five assert strictly more
and are mutation-held (`mutation-tests-2026-08-03.md`). **One does not** — see
`sampling-sweep-2026-08-03.md`, Finding B: `test_each_kind_labels_its_own_fields_in_its_own_words`
lost four literal-value assertions and asserts strictly LESS in the value
dimension, contrary to the recorded claim that "no scenario asserts less than it
did".

### Criteria-reference delta

Every `AC-…` identifier referenced anywhere in either test tree, base vs head:
**256 → 256, none lost, none gained.** No criterion silently stopped being
named.

---

### Scenario: the unit/integration entry point executes and passes
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest backend/tests`
- Expected: exit 0, zero failures, zero skips
- Actual: **2,309 ran, 2,309 passed, exit 0**
- Result: PASS
- Evidence: `backend/tests` node ids in the collected set = 2,309; 0 `F`, 0 `s`
  characters in the progress output

### Scenario: the whole tree executes and passes in canonical order
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest` at `dev/`
- Expected: 2,987 pass, exit 0
- Actual: **2,987 progress characters, 0 `F`, exit 0**
- Result: PASS
- Evidence: `run-canonical.txt`, 100% marker reached

### Scenario: the suite total equals the sum of its suites
- Status: EXECUTED
- Expected: 2,309 + 358 + 194 + 61 + 28 + 23 + 14 = 2,987
- Actual: **2,987 — exact**
- Result: PASS
- Evidence: node ids partitioned by path prefix

### Scenario: no scenario is skipped, xfailed or deselected in a whole-tree run
- Status: EXECUTED
- Expected: zero `s`/`x` characters in progress output
- Actual: **zero**
- Result: PASS
- Evidence: `tr -cd 'sx'` over the progress lines of all six whole-tree runs

### Scenario: the test tree does not write to the developer's live ledger
- Status: EXECUTED
- Input: md5 of `dev/var/broker_db.sqlite3` before and after five whole-tree runs
- Expected: byte-identical
- Actual: **`449791062f2f1adb8db41a9d5406fb24` before and after every one of the
  five runs**
- Result: PASS
- Evidence: `order-independence-2026-08-03.md`
