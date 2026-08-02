# Test evidence — register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> **Does any suite report a pass that the 33-entry register says cannot be true?**

**No — for the fifth consecutive pass.**

---

### Scenario: the register still has 33 entries, no gaps
- Status: EXECUTED
- Input: counted the distinct entry numbers in `PROJECT_CONTEXT.md`'s
  "Deferred-substitution register"
- Expected: 1–33, no gaps, no duplicates
- Actual: `1 2 3 … 33`, **count 33**
- Result: PASS
- Evidence: distinct-and-sorted entry numbers `1..33`, `wc -l` = 33

### Scenario: the five declared criteria are claimed by no scenario name
- Status: EXECUTED
- Input: searched every scenario name and node ID across all 2,692 collected
  tests for `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`
- Expected: **zero** scenario names claim any of the five
- Actual: zero
- Result: PASS
- Evidence: no `def test_*` name in `backend/tests` or `tests/suites` contains
  any of the five IDs.

### Scenario: the five are claimed by no `COVERS` line either
- Status: EXECUTED
- Input: `grep -rn "COVERS" backend/tests tests/` filtered to the five IDs — a
  name-only check would miss a docstring join, which is how gate 9 maps
  criterion to test
- Expected: either no hit, or a hit whose denial is **inside the join string**
  so an ID-keyed mapper cannot score it satisfied (register 27)
- Actual: **exactly two hits, both the known and closed `AC-F36-48` case**:
  - `backend/tests/test_abstention.py:331` — `"""COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH IS ITSELF DENIED:`
  - `backend/tests/test_abstention.py:360` — `"""COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48 (its above-band tail), AND AC-F36-48 IS ITSELF DENIED:`
  Zero `COVERS` lines name the other four.
- Result: PASS
- Evidence: register A1 is CLOSED on exactly this condition — the denial is
  inside the join string, so a by-ID mapper reading the join reads
  "WHICH IS ITSELF DENIED" with it. Unchanged from the previous pass.

### Scenario: every other mention of the five is a denial, not a claim
- Status: EXECUTED
- Input: read all 40 mentions of the five IDs across the test tree
- Expected: each is either the product **asserting the criterion is unmet**, or
  a comment stating the criterion is not covered
- Actual: all 40 are one of those two shapes. Representative:
  - `assert stamp["unmet_criterion"] == "AC-F1-08"` (the build says it is unmet)
  - `assert integrity["anchor"]["unmet_criterion"] == "AC-F1-11"`
  - `assert payload["unmet_criterion"] == "AC-F40-17"` and
    `assert declared["unmet_criteria"] == ["AC-F40-17"]`
  - `# AC-F40-17 is not claimed, and the vocabulary keeps the two apart`
  - `"""AC-F1-08 IS NOT SATISFIED BY THIS SCENARIO — do not map it to that ID.`
  - `#: AC-REFUSAL-11 is NOT VERIFIED.` / `"""WHY AC-REFUSAL-11 IS NOT VERIFIED. Do not "fix" this scenario.`
  - `# AC-F36-48 IS DENIED AND NO SCENARIO IN THIS FILE CLAIMS IT.`
- Result: PASS
- Evidence: a test that asserts the product **states a criterion is unmet** is
  the opposite of a test claiming it satisfied, and both the smoke test (S10,
  S11) and the served auditor export confirm those denials reach the reader.

### Scenario: two node IDs still contain two of the IDs as parameters
- Status: EXECUTED
- Input: `test_export_integrity_contract.py:128` —
  `[("anchor", "AC-F1-11"), ("retention", "AC-F1-08")]`
- Expected: carried from the previous pass, and still on a scenario asserting
  the export **declares these unmet**
- Actual: unchanged, and the file header states it directly: "neither
  `AC-F1-11` nor `AC-F1-08`. Required is not validated, because…"
- Result: PASS
- Evidence: the parametrisation drives `assert integrity["anchor"]["unmet_criterion"] == "AC-F1-11"`.
  A mapper keying on node IDs would see the ID; the scenario it lands on
  asserts the denial, so the reading is safe. Carried, unchanged, not blocking.

---

## Conclusion

**No suite reports a pass the register says cannot be true.** Four consecutive
contradiction-free passes has become five. The five declared criteria are
claimed by zero of the 2,692 scenario names and by zero `COVERS` joins other
than the two register-27-compliant `AC-F36-48` strings, whose denial travels
inside the join.
