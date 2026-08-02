# Test evidence — register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 13 verification)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> **Does any suite report a pass that the register says cannot be true?**

**No — for the fourth consecutive pass.**

The deferred-substitution register has **33 entries** (verified by counting the
distinct entry numbers in `PROJECT_CONTEXT.md` §"Deferred-substitution
register": 1–33, no gaps, no duplicates). Nine are CLOSED (6, 8, 10, 11, 13, 14,
16, 18, 25). Entries 1–5, 7 and 9 stand as recorded at pass 1 and 2c.

---

### Scenario: the five declared criteria are claimed by no scenario name
- Status: EXECUTED
- Input: all **2,664** collected node IDs (`pytest --collect-only -q`), scanned in
  both spellings — the underscored form a Python test name would use, and the
  dashed form the criteria are written in
- Expected: zero
- Actual:

  | Criterion | Underscored (`AC_F1_08`…) | Dashed (`AC-F1-08`…) |
  |---|---|---|
  | `AC-F1-08` | 0 | 1 |
  | `AC-F1-11` | 0 | 1 |
  | `AC-REFUSAL-11` | 0 | 0 |
  | `AC-F40-17` | 0 | 0 |
  | `AC-F36-48` | 0 | 0 |

- Result: **PASS**
- Evidence: the two dashed hits are **parametrize labels**, and both are on a
  scenario that asserts the export is **refused** unless it names the criterion
  it does not meet:
  ```
  backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]
  backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]
  ```
  These are new at `55878c9` — they arrived with the F3 fix. They are the
  strongest possible statement of the denial, not a claim: the scenario fails if
  the product ever declares the residual **without** naming the unmet criterion.
  Recorded explicitly because a node-ID scan run mechanically would flag them.

### Scenario: every textual occurrence of the five is a denial
- Status: EXECUTED
- Input: `grep -rn` over `backend/tests` and `tests/suites` for each of the five
- Expected: every occurrence either denies the criterion, instructs a reader not
  to map it, or asserts that the **product's own disclosure** names it as unmet
- Actual: all of them are. Counts and representative lines:

  | Criterion | Occurrences | Representative |
  |---|---|---|
  | `AC-F1-08` | 13 | `test_acceptance_criteria.py:326: """AC-F1-08 IS NOT SATISFIED BY THIS SCENARIO — do not map it to that ID.` |
  | `AC-F1-11` | 7 | `test_retention_and_anchor_disclosure.py:130: assert "AC-F1-11 unmet" in statement` |
  | `AC-REFUSAL-11` | 9 | `test_adversarial.py:356: #: AC-REFUSAL-11 is NOT VERIFIED.` |
  | `AC-F40-17` | 10 | `test_f40_criteria.py:641: NOT AC-F40-17: nothing here detects drift after a recorded pass.` |
  | `AC-F36-48` | 8 | `test_abstention.py:311: # AC-F36-48 IS DENIED AND NO SCENARIO IN THIS FILE CLAIMS IT.` |

- Result: PASS
- Evidence: as above. `assert "AC-F40-17 is unmet" in response.text`
  (`test_f40_criteria.py:686`) is the shape to note — the suite asserts the
  product **tells the reader**, which is the opposite of claiming the criterion.

### Scenario: registers 3 and 4 are unchanged and still open
- Status: EXECUTED
- Input: the register text, plus the served `/audit/export` screen and the
  auditor export file
- Expected: register 3's anchor is still a labelled digest and register 4's
  retention is still unenforced; both denials reach the artefact
- Actual: unchanged. Both IDs appear in the served screen and inside the export
  payload, each attached to the claim it qualifies.
- Result: PASS
- Evidence: `"The hash-chain anchor is a labelled digest, not a KMS-signed one.
  An attacker who holds the application could recompute the chain and the
  recomputation would not be detected (AC-F1-11 is unmet)."`;
  `GET /audit/export/file` → 200 with `evidence_integrity`, `AC-F1-11` and
  `AC-F1-08` all present

### Scenario: the F3 fix does not quietly close register 3 or 4
- Status: EXECUTED (mutation)
- Input: the three mutations in `fix-verification-2026-07-31.md` F3-1..F3-3
- Expected: what F3 built is an enforcement that the residual be **declared** —
  it does not sign anything and does not enforce retention, and nothing may read
  it as doing so
- Actual: confirmed. `REQUIRED_INTEGRITY_SECTIONS` maps `anchor → AC-F1-11` and
  `retention → AC-F1-08` as the criteria a declared residual must **name**. The
  export is refused if it declares the residual and does not name them, and
  refused if it names them and says nothing in words.
- Result: PASS — the fix strengthens the disclosure of two open registers rather
  than closing either
- Evidence: `REQUIRED_INTEGRITY_SECTIONS` in `backend/app/evidence/export.py`;
  the four mutation kills

### Scenario: no new register entry is needed for pass 13
- Status: EXECUTED (reviewed)
- Input: the four pass-13 commits against `ARCHITECTURE_KB` and `SECURITY_KB`
- Expected: a substitution introduced without disclosure would need one
- Actual: none of the four substitutes anything. F1 is a dev/pilot-only fixture
  migration confined to `seed()`, which the runtime path deliberately does not
  have (`schema_gaps()`/`assert_schema_current()` are public so a deployment can
  say so up front against a customer warehouse we connect to read-only). F2
  removes a fixture. F3 adds validation. A2 adds a refusal.
- Result: PASS
- Evidence: `git show --stat 55878c9 38b160d 7f190c9 59351a3`

---

## One finding about the evidence corpus itself

The previous run's `PROJECT_CONTEXT.md` Test Results section states that the
corpus was rewritten at `9d819c1` and that "the entire `f56ab9f` corpus was
deleted, not left beside this one". **It was not.** Every one of the nine files
found in `test-evidence/` at the start of this run carried
`**Commit under test:** dev @ **f56ab9f** · parent repo @ **8939ebb**` — the
corpus on disk described the run *before* the one the narrative summary
described. The `9d819c1` per-scenario evidence was never written.

This is exactly the failure mode the source-of-record split exists to prevent: a
narrative summary claiming evidence that does not exist. It is recorded here,
and this run's corpus supersedes it — all nine files were **deleted** and
rewritten at `55878c9`, and every file names both commits.
