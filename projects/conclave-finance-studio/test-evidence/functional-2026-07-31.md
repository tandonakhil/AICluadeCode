# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 13 verification)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `functional-agent` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/functional/run.sh`
**Exit code:** 0
**Scenarios: 354 — PASS 354, FAIL 0, SKIP 0** (19 scenario files)

`test-agent` does not author this suite. It ran it, read its scenario names and
docstrings against the deferred-substitution register, and reports the result.

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0, and not exit 3 (no scenarios) or 4 (cannot execute)
- Actual: `interpreter: dev/.venv/bin/python`, `scenarios: 19 file(s)`,
  `EXECUTED — suite passed`
- Result: PASS
- Evidence: `EXECUTED — suite passed` / exit 0

### Scenario: the suite is unchanged since the previous run
- Status: EXECUTED
- Input: set-wise diff of collected node IDs, `9d819c1` → `55878c9`
- Expected: a delta, if any, that is explained
- Actual: **354 → 354, 0 added, 0 removed, 0 changed**
- Result: PASS (baseline held)
- Evidence: `comm -13`/`comm -23` over the two sorted node-ID sets return nothing
  for this suite

### Scenario: `AC-F1-08` is claimed nowhere in this suite
- Status: EXECUTED
- Input: node-ID scan plus every textual occurrence in
  `tests/suites/functional/test_acceptance_criteria.py`
- Expected: register 20 says the ID is covered by no suite
- Actual: zero claims. Four occurrences, all denials, including a scenario
  docstring that names the join risk explicitly.
- Result: PASS
- Evidence: `test_acceptance_criteria.py:294: # AC-F1-08 IS NOT COVERED BY THIS
  SUITE.` and `:326: """AC-F1-08 IS NOT SATISFIED BY THIS SCENARIO — do not map
  it to that ID.` and `:347: to any ID-to-criterion mapping as a satisfied AC-F1-08.`

### Scenario: `AC-F40-17` is claimed nowhere, and the denial travels inside the join string
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py`
- Expected: register 28 keeps `-17` open while `-18` is built
- Actual: zero claims; the scenarios that touch the area state the negative in
  their own docstrings and assert the denial is rendered
- Result: PASS
- Evidence: `:571: # AC-F40-17 is NOT covered by anything below and the denial
  travels inside`; `:641: NOT AC-F40-17: nothing here detects drift after a
  recorded pass.`; `:676: NOT AC-F40-17: authorised_on == synthetic_attestation
  is the opposite of`; `:686: assert "AC-F40-17 is unmet" in response.text`

### Scenario: this suite carries one of the interleaved-shuffle failures
- Status: EXECUTED
- Input: whole-tree shuffle, seeds 1 and 7
- Expected: n/a — reported, not expected
- Actual: `test_unclaimed_criteria.py::test_AC_REFUSAL_07_the_refusals_are_registered_and_therefore_recordable`
  fails at both seeds, on `assert []` — no control event recorded, because a
  `backend/tests` scenario ran between the suite's autouse sink reset and this
  assertion
- Result: **FAIL under interleaved shuffle only.** Passes in collection order,
  reversed, and when the suite is run alone through its own `run.sh`.
- Evidence: `AssertionError: no control event was recorded for a refused
  selection / assert []`. Pre-existing — see `fix-verification-2026-07-31.md` OD-2.
