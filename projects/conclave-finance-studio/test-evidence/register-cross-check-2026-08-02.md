# Test evidence — register cross-check (the standing question)

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `pytest --collect-only -q -o addopts=` over the whole tree,
plus an AST walk of every `test_*.py` docstring in both trees
**Scenarios: 5 — PASS 5, FAIL 0**

> **The standing question:** does any suite report a pass the 33-entry
> deferred-substitution register says cannot be true?
>
> **Answer, for the sixth consecutive pass: no.**

The five declared criteria — `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
`AC-F40-17`, `AC-F36-48` — are claimed by **zero** of the **2,736** collected
scenario names, other than two parametrisation labels that are part of a
**refusal**, and by **zero** `COVERS` joins that are not self-denying.

---

### Scenario: `AC-F1-08` (object-lock retention) is claimed nowhere
- Status: EXECUTED
- Input: all 2,736 node IDs, scanned for `AC-F1-08` and `AC_F1_08`
- Expected: zero claims
- Actual: **1 node-ID occurrence**, and it is a denial:
  `test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`
- Result: PASS
- Evidence: the scenario asserts the export is **REFUSED** when the criterion is
  not named. The ID is the parametrisation label of the thing being refused,
  not a claim that it is satisfied. Elsewhere the ID appears only in
  disclosure assertions (`unmet_criterion == "AC-F1-08"`) and in a comment in
  `test_evidence_store.py` explicitly disclaiming a coverage join it once
  carried.

### Scenario: `AC-F1-11` (KMS-signed anchors) is claimed nowhere
- Status: EXECUTED
- Input: same scan
- Expected: zero claims
- Actual: **1 node-ID occurrence**, the sibling parametrisation
  `[anchor-AC-F1-11]` on the same refusal scenario
- Result: PASS
- Evidence: `assert integrity["anchor"]["unmet_criterion"] == "AC-F1-11"` and
  `assert "AC-F1-11 unmet" in statement` — the build states the criterion is
  unmet, on the screen (smoke S10) and in the auditor's file (smoke S11)

### Scenario: `AC-REFUSAL-11` is claimed nowhere
- Status: EXECUTED
- Input: same scan, plus every `COVERS` docstring in the red-team suite
- Expected: zero claims — register 13 holds it NOT VERIFIED and records that
  extending the paraphrase battery does not unlock it
- Actual: **0** node-name claims, **0** `COVERS` joins
- Result: PASS
- Evidence: the ID appears only in prose that denies it —
  "`AC-REFUSAL-11` IS NOT SATISFIED BY THIS SCENARIO AND IS NOT SATISFIED…",
  "WHY `AC-REFUSAL-11` IS NOT VERIFIED. Do not 'fix' this scenario.", and two
  messages instructing a future reader to "re-assess AC-REFUSAL-11 on the new
  boundary"

### Scenario: `AC-F40-17` (CUEC drift detection) is claimed nowhere
- Status: EXECUTED
- Input: same scan
- Expected: zero claims
- Actual: **0** node-name claims. Two `COVERS` docstrings mention the ID and
  both **cover `AC-F40-18` instead**, saying so explicitly:
  "NOT AC-F40-17: `authorised_on == synthetic_attestation` is the…"
- Result: PASS
- Evidence: `test_cuec_export_probe.py` carries a header section titled
  "WHAT IS NOT CLAIMED HERE — `AC-F40-17`", and one scenario asserts that
  nothing in the file claims it

### Scenario: `AC-F36-48` is claimed nowhere, and its two joins deny themselves
- Status: EXECUTED
- Input: same scan
- Expected: zero bare-ID claims; the two register-27-compliant joins must carry
  the denial **inside** the join string so an ID-keyed mapper cannot score it
  satisfied
- Actual: **0** node-name claims. The two `COVERS` joins read
  "COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH IS ITSELF DENIED…
  DO NOT MAP THE BARE ID AC-F36-48 TO THIS SCENARIO."
- Result: PASS
- Evidence: both docstrings, quoted above, in `backend/tests/test_abstention.py`

---

## What was scanned, and how

* **2,736 node IDs**, from `pytest --collect-only -q -o addopts=`. The
  `-o addopts=` matters: the project's `pytest.ini` already carries `-q`, so a
  second `-q` collapses collection output to per-file counts and suppresses the
  run summary line. Both figures were reconciled against the progress-character
  tally (`Counter({'.': 2736})`) rather than trusted from one source.
* **Every `test_*.py` in both trees**, walked with `ast` rather than grepped, so
  the docstring of each `test_`-prefixed function is read as a unit. Four
  `COVERS` docstrings name a declared criterion; all four deny it in the same
  sentence.

## Register entries checked

Registers **1–33**, verified present with no gaps. The two **open** registers
(3 and 4) are the ones whose disclosures the smoke test confirmed reach both the
auditor's screen and the auditor's file. Register **27**'s substitution gate is
satisfied by the two `AC-F36-48` joins carrying their own denial. Registers
**6**, **8**, **9** and **15** are exercised on the served pilot by smoke S4,
S9, S12 and S13 respectively.

## New this pass

`AC-F36-33` and `AC-F36-30` were built at `a1850a5` and `faf6117`. Neither is a
declared criterion, and neither new scenario claims one: the 44 added node IDs
were scanned with the same query and returned **zero** occurrences of any of the
five IDs.
