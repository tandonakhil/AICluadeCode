# Test evidence — unit / integration

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes (project Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**2,988 scenarios, 2,988 pass, 0 fail, 0 skip, exit 0.**
Interpreter `dev/.venv/bin/python` (3.9). Entry point
`.venv/bin/python -m pytest -o addopts= -q`, and the same scenarios again in
five further whole-tree runs under alternative collection orders, plus once
more under AST instrumentation (see the vacuous-pass sweep).

Note on output: `dev/pytest.ini` carries `addopts = -q`; the runs above pass
`-o addopts=` so pytest's own summary line is printed rather than suppressed.
The count is taken from that line and cross-checked against collected node ids
(`--collect-only -q -o addopts=`), which agree exactly.

## Test-count delta — measured by comparing collected node ids, not counted

Baseline: `dev` @ `e00a214` (the commit gate 8 pass 19 reported on), collected
in a detached worktree with the same interpreter.

| | Baseline `e00a214` | Head `c428fe5` | Delta |
|---|---|---|---|
| whole tree | 2,987 | **2,988** | **+1 net** |
| node ids added | — | — | **+1** |
| node ids removed | — | — | **0** |
| changed in place (same id, different body) | — | — | **2** |
| changed in place (docstring only) | — | — | **1** |

### Added (1)

| Node id | Why |
|---|---|
| `backend/tests/test_obligation_gap.py::test_every_kind_the_build_holds_has_its_words_written_out_in_this_file` | the companion scenario that makes the kind parametrisation able to fail on a fourth kind — asserts `KIND_VOCABULARY`'s key set equals `EXPECTED_KIND_WORDS`'s |

### Removed (0)

**None.** No coverage was dropped this pass.

### Changed in place (3)

| Node id | Change |
|---|---|
| `backend/tests/test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words` | compares against the literal `EXPECTED_KIND_WORDS` table in the test file rather than `obligation_gap.KIND_VOCABULARY`; widened from 4 worded fields to 5 (adds `summary`) |
| `tests/suites/functional/test_f40_criteria.py::test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts` | drives the real export control three times; asserts `count >= 3` and group-id distinctness *before* the per-entry loop |
| `tests/suites/functional/test_unclaimed_criteria.py::test_the_broker_answers_the_population_question_UNKNOWN_and_not_none` | **docstring only.** Assertions unchanged |

### Per-suite collected counts (reconcile to the whole tree)

| Suite | Count |
|---|---|
| `backend/tests` (unit / integration) | 2,310 |
| `tests/suites/functional` | 358 |
| `tests/suites/ux` | 194 |
| `tests/suites/red-team` | 61 |
| `tests/suites/architecture` | 28 |
| `tests/suites/industry` | 23 |
| `tests/suites/security` | 14 |
| **total** | **2,988** |

2,310 + 358 + 194 + 61 + 28 + 23 + 14 = **2,988** — exact. Unit/integration is
the only suite whose count moved (2,309 → 2,310).

---

### Scenario: the whole tree collects and runs
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest -o addopts= -q -p no:cacheprovider` at `c428fe5`
- Expected: every collected node id executes; no error, no skip
- Actual: **`2988 passed in 218.37s`, exit 0**
- Result: PASS
- Evidence: pytest summary line, whole tree, no `-k`, no deselection

### Scenario: the collected count reconciles across the seven suites
- Status: EXECUTED
- Input: `--collect-only` per suite directory, summed
- Expected: the parts equal the whole
- Actual: **2,988 — exact**
- Result: PASS
- Evidence: the table above

### Scenario: no test was silently removed since the last run
- Status: EXECUTED
- Input: sorted collected node ids at `e00a214` vs `c428fe5`, `comm -23`
- Expected: any removal named explicitly
- Actual: **0 removed**
- Result: PASS
- Evidence: `comm -23 basecollect.txt head.txt` — empty output

### Scenario: no suite is empty
- Status: EXECUTED
- Input: `tests/suites/_runner.sh` for each of the six SME suites
- Expected: exit 0 (ran and passed), never exit 3 (no scenarios defined)
- Actual: **all six exit 0**, none reported `NO SCENARIOS DEFINED`
- Result: PASS
- Evidence: `EXECUTED — suite passed` on all six
