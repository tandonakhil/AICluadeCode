# Test evidence — register cross-check (the standing question)

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** node-ID collection over the whole tree + a grep of every
`COVERS` join in both test trees
**Exit code:** 0
**Scenarios: 8 — PASS 8, FAIL 0**

> **The standing question — "does any suite report a pass the 33-entry register
> says cannot be true?" — returns NO for the SEVENTH consecutive pass.**

---

### Scenario: the register still has 33 entries, numbered 1–33 with no gaps
- Status: EXECUTED
- Input: every numbered row of the deferred-substitution register in
  `PROJECT_CONTEXT.md`
- Expected: 33 entries, contiguous
- Actual: `1 2 3 4 5 … 33` — 33 distinct numbers, no gaps, no duplicates
- Result: PASS
- Evidence: the sorted unique row numbers, printed in full

### Scenario: `AC-F1-08` is claimed by no scenario name
- Status: EXECUTED
- Input: all 2,774 collected node IDs, matching both `AC-F1-08` and `AC_F1_08`
- Expected: zero claims
- Actual: **1 node ID contains the string, and it is not a claim** —
  `backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`,
  a parametrisation label of a scenario asserting the export is **REFUSED**
- Result: PASS
- Evidence: the other five mentions in the trees are
  `assert stamp["unmet_criterion"] == "AC-F1-08"` and `assert "AC-F1-08" in
  body` — assertions that the *unmet-ness* is disclosed, which is what the
  claim prohibition requires, not that the criterion is met

### Scenario: `AC-F1-11` is claimed by no scenario name
- Status: EXECUTED
- Input: as above
- Expected: zero claims
- Actual: **1 node ID**, the sibling parametrisation label
  `…test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]`
- Result: PASS
- Evidence: the tree's other mentions are `assert status["unmet_criterion"] ==
  "AC-F1-11"` and `assert "AC-F1-11 unmet" in statement`

### Scenario: `AC-REFUSAL-11` is claimed by no scenario name
- Status: EXECUTED
- Input: as above
- Expected: zero
- Actual: **0 node IDs**
- Result: PASS
- Evidence: the only mentions anywhere are three self-denying comments in
  `tests/suites/red-team/test_adversarial.py` — `AC-REFUSAL-11 is NOT
  VERIFIED.` and `**AC-REFUSAL-11 IS NOT SATISFIED BY THIS SCENARIO AND IS NOT
  SATISFIED …**`

### Scenario: `AC-F40-17` is claimed by no scenario name
- Status: EXECUTED
- Input: as above
- Expected: zero
- Actual: **0 node IDs**
- Result: PASS
- Evidence: `backend/tests/test_cuec_export_probe.py` opens with `WHAT IS NOT
  CLAIMED HERE — AC-F40-17 … No scenario in this file claims AC-F40-17, and one
  asserts that nothing in` — the file polices itself

### Scenario: `AC-F36-48` is claimed by no scenario name
- Status: EXECUTED
- Input: as above
- Expected: zero
- Actual: **0 node IDs**
- Result: PASS
- Evidence: `# AC-F36-48 IS DENIED AND NO SCENARIO IN THIS FILE CLAIMS IT.`

### Scenario: no `COVERS` join asserts any of the five
- Status: EXECUTED
- Input: every `COVERS …` string in `backend/tests` and `tests/suites`
- Expected: zero, other than register-27-compliant self-denying joins
- Actual: exactly **two** joins name a declared criterion, both
  register-27-compliant with the denial travelling *inside* the join string:
  `COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH IS ITSELF DENIED:`
  and `COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48 (its above-band tail),`
- Result: PASS
- Evidence: identical to the previous six passes; nothing new was added

### Scenario: the 38 NEW node IDs were scanned with the same query
- Status: EXECUTED
- Input: the 38 node IDs added since `75f5e27`, differenced as a set
- Expected: zero occurrences of any of the five
- Actual: **zero.** The 38 are 25 in `test_harness_rendered_numbers.py`, 12 in
  `test_harness_live_ledger_guard.py`, 1 in the architecture suite — all
  harness scenarios, none naming a product criterion at all
- Result: PASS
- Evidence: neither new file mentions any `AC-` identifier except `AC-F12-15`
  in `rendered_numbers`'s docstring, which is an in-scope MVP1 criterion and
  not one of the five
