# Test evidence — mutation verification of pass 26's three claims

**Project:** conclave-finance-studio
**Gate:** 11 — post-deploy smoke re-run (verification of `code-agent` pass 26)
**Date:** 2026-08-06
**Commit under test:** `dev` @ **`b447a11`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**22 scenarios, 22 pass, 0 FAIL.**

Pass 26 *claims* four construction refusals, a substring guard in two files, and
two hand-kept lists replaced by derived ones. This file is those claims
**re-run** rather than accepted. Every mutation was applied to a **scratch clone
at `b447a11`** and reverted; `dev/` was never modified (`git status` clean
throughout).

The discipline this file exists for: on 2026-08-06 my own first draft of two
scenarios reported green against a build that disclosed nothing, because it
asserted on the substring `fixture` — which occurs in this build only inside
`gl_balances vFIXTURE-2026.06.03-a`. A check that cannot fail is not a check, so
each claim below is verified by making it fail on purpose.

---

## Claim 1 — four mutations refused at construction

Nine mutations run, not four: the four claimed, plus five further shapes I chose
because a contract that refuses the shapes somebody thought of and admits the
ones they did not is not a contract. **All nine refused.**

### Scenario: M0 - positive control, the real payload constructs
- Status: EXECUTED
- Input: `Export(..., integrity=<the four real producers>)`
- Expected: constructs; the negative controls below are worthless if it did not
- Actual: constructed; provenance section present
- Result: PASS
- Evidence: `real_ledger_sourced=False, unmet_criterion=None, register_entry=15, dataset_version='gl_balances vFIXTURE-2026.06.03-a'`

### Scenario: M1 - the provenance section removed entirely
- Status: EXECUTED
- Input: `integrity.pop("provenance")`, then construct
- Expected: `IntegrityStatementMissing`, naming the section
- Actual: REFUSED
- Result: PASS
- Evidence:

```
the export failed at evidence_integrity: this export states nothing about
provenance. Silence reads as the STRONGER claim - that this guarantee is held -
and the reader this file is for has no application login and no access to the
running system to find out otherwise (AC-F1-04). Every section of
REQUIRED_INTEGRITY_SECTIONS is a guarantee the pilot does not hold: anchor,
provenance, retention, transport
```

### Scenario: M2a - residual declared without naming register 15 (register_entry -> None)
- Status: EXECUTED
- Input: `integrity["provenance"]["register_entry"] = None`
- Expected: refused, naming `register_entry=15`
- Actual: REFUSED
- Result: PASS
- Evidence: `the provenance statement declares the residual (real_ledger_sourced=False) without naming register_entry=15, which is what it is unmet against`

### Scenario: M2b - register_entry set to 19, another register's number
- Status: EXECUTED
- Input: `integrity["provenance"]["register_entry"] = 19`
- Expected: refused — a plausible wrong reference must not satisfy the clause
- Actual: REFUSED, same message
- Result: PASS
- Evidence: not claimed by pass 26; added because a presence check would have passed here

### Scenario: M2c - register_entry set to the STRING "15"
- Status: EXECUTED
- Input: `integrity["provenance"]["register_entry"] = "15"`
- Expected: refused — the contract names the int
- Actual: REFUSED, same message
- Result: PASS
- Evidence: the comparison is `!=` against the contract value, so type is part of the reference

### Scenario: M3a/M3b/M3c - residual declared with an empty sentence
- Status: EXECUTED
- Input: `statement` set to `"   "`, then `""`, then `None`
- Expected: refused in all three
- Actual: REFUSED in all three
- Result: PASS
- Evidence: `the provenance statement declares the residual and says nothing about it in words`

### Scenario: M4 - presence-only `{"real_ledger_sourced": false}`
- Status: EXECUTED
- Input: `integrity["provenance"] = {"real_ledger_sourced": False}`
- Expected: refused, naming the missing keys
- Actual: REFUSED
- Result: PASS
- Evidence: `the provenance statement omits statement, register_entry, so a reader cannot tell what is claimed from what is stubbed`

### Scenario: M5 - the section present but emptied
- Status: EXECUTED
- Input: `integrity["provenance"] = {}`
- Expected: refused (`{}` is a value, and gate 8 proved that mattered)
- Actual: REFUSED
- Result: PASS
- Evidence: same "states nothing about provenance" message — an empty dict is treated as silence, not as presence

### Scenario: M6 - the shipped export carries the phrases, no invented AC id
- Status: EXECUTED
- Input: serialise the real `Export`; check the provenance section and the whole file
- Expected: four phrases present; `unmet_criterion` null; `register_entry` 15; no `AC-` in the statement
- Actual: all four phrases PRESENT in the section AND in the whole serialised file; `unmet_criterion=None`; `register_entry=15`; `"AC-" in statement` = False; `"register entry 15" in statement` = True
- Result: PASS
- Evidence: sections = `['anchor', 'provenance', 'retention', 'transport']`

---

## Claim 2 — the substring guard fails when a phrase is weakened

**This is the check that stops my own false pass recurring**, so it is the one
verified hardest. `REQUIRED_PHRASES` was weakened one phrase at a time in the
scratch clone and both guard files were run.

### Scenario: W1 - a phrase weakened to the bare word `fixture` fails the guard IN BOTH FILES
- Status: EXECUTED
- Input: `REQUIRED_PHRASES[0]` changed from `"synthetic fixture data"` to `"fixture"`; run `backend/tests/test_provenance_disclosure.py` and `tests/suites/security/test_provenance_disclosure.py`
- Expected: the parametrised vacuity guard fails in **both** files
- Actual: **4 failed, 35 passed** — and the failures are exactly the guards
- Result: PASS
- Evidence:

```
FAILED backend/tests/test_provenance_disclosure.py::test_the_dataset_version_alone_satisfies_no_required_phrase[fixture]
FAILED backend/tests/test_provenance_disclosure.py::test_every_required_phrase_is_prose_rather_than_a_token[fixture]
FAILED backend/tests/test_provenance_disclosure.py::test_the_bare_word_fixture_is_not_what_anything_asserts_on
FAILED tests/suites/security/test_provenance_disclosure.py::test_the_version_identifier_alone_would_not_satisfy_these_scenarios[fixture]
```

Note what does **not** appear in that list: the positive controls still passed,
because the shipped statement does contain `fixture`. That is the point — the
weakening is caught by the guard, not incidentally by an unrelated assertion.

### Scenario: W2 - three further substring weakenings, each caught
- Status: EXECUTED
- Input: the same phrase weakened in turn to `"FIXTURE"`, `"gl_balances"`, `"vFIXTURE-2026.06.03-a"`
- Expected: the guard fails in both files each time
- Actual: 5 failed / 4 failed / 4 failed respectively (the `FIXTURE` case fails one extra, case-insensitively)
- Result: PASS
- Evidence: the guard is case-insensitive against the version identifier, so an upper-case dodge does not slip through

### Scenario: W3 - CONTROL: a one-word weakening that is NOT in the version identifier
- Status: EXECUTED
- Input: the phrase weakened to `"synthetic"`
- Expected: the version-identifier guard correctly does NOT fire (that word is not in the identifier); the prose/token guard must catch it instead
- Actual: **1 failed** — `test_every_required_phrase_is_prose_rather_than_a_token[synthetic]`
- Result: PASS
- Evidence: the two guards divide the space correctly rather than overlapping and leaving a gap

### Scenario: W4 - ADVISORY OBSERVATION, not a failure
- Status: EXECUTED
- Input: comparing which guard lives in which file
- Expected: —
- Actual: the **version-identifier** guard is in both files, as pass 26 claims. The **prose/token** guard (`>= 3 words`) is in `backend/tests/` **only**; the security suite has no equivalent. A one-word weakening that is not a substring of the version is therefore caught by one file rather than two.
- Result: PASS (the claim made — "a parametrised scenario in two files asserting the version satisfies none of them" — is true as stated)
- Evidence: recorded as an observation for `code-agent`, not as an unmet claim

---

## Claim 3 — the two hand-kept lists are derived, not enumerated

### Scenario: D1 - the `(section, key)` list is derived from the contract
- Status: EXECUTED
- Input: baseline collection, then a **fifth** section added to `REQUIRED_INTEGRITY_SECTIONS` in the scratch clone
- Expected: the key-level parametrisation grows without anybody editing the test file
- Actual: **12 -> 15**, and the three new ids appear automatically
- Result: PASS
- Evidence:

```
baseline: 12 ids, covering anchor(3) provenance(3) retention(3) transport(3)
after adding "fifthweakening": 15 ids, the new three being
  test_a_section_missing_any_declared_key_is_refused[fifthweakening-fifth_held]
  test_a_section_missing_any_declared_key_is_refused[fifthweakening-statement]
  test_a_section_missing_any_declared_key_is_refused[fifthweakening-register_entry]
```

All three of `provenance`'s keys are witnessed at baseline. Under the old
nine-literal list they would not have been — which is the defect pass 26 says it
found, confirmed here by construction.

### Scenario: D2 - the refusal MESSAGE is derived from the contract
- Status: EXECUTED
- Input: trigger `check_integrity_statement({})` at baseline, and again with the fifth section added
- Expected: the message enumerates whatever the contract declares, never a fixed three
- Actual: baseline -> `anchor, provenance, retention, transport`; with the fifth -> `anchor, fifthweakening, provenance, retention, transport`
- Result: PASS
- Evidence: the message no longer describes the weakenings individually; it names the section that is missing and states the harm once, which is identical for every section

### Scenario: D3 - the join in the other direction still bites
- Status: EXECUTED
- Input: with a fifth section declared and **no producer** for it, run `test_export_integrity_contract.py`
- Expected: the file fails loudly rather than passing over an undeclared section
- Actual: **15 failed, 37 passed**
- Result: PASS
- Evidence: a section added to the contract with nothing producing it cannot reach an auditor's export silently

### Scenario: D4 - no section is named explicitly in the clause
- Status: EXECUTED
- Input: `inspect.getsource(check_integrity_statement)` scanned for each section name
- Expected: none present — one rule over the declared contract, not a branch per section
- Actual: none present, for all four sections
- Result: PASS
- Evidence: verified by the project's own `test_the_fourth_section_needed_no_new_contract_machinery`, re-run here and independently re-read in source

---

## What was NOT verified here, and is owed

**`ARCH-16` must not assert `AC-F41-03` against the export artefact.**
`solution-architect` re-ruled at gate 10 that `AC-F41-03` is a **screen**
criterion by its own text, that the risk band is correctly absent from the
artefact, and that register 35 stays open for **legibility** and not for
`AC-F41-03`. Per that instruction the scenario was **not written this pass**. It
is recorded as **owed** to the architecture suite, and the earlier `G12`/`G13`
observations in `smoke-test-2026-08-06.md` stand as measurements, deliberately
not re-litigated.
