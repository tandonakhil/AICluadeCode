# Test evidence — the deferred-substitution register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> *Does any suite report a pass the register says cannot be true?*

**NO — for the third consecutive pass.**

**Method:** all 2,988 collected node IDs, plus every `COVERS` line in both test
trees, scanned for each of the eight forbidden criterion IDs in both hyphenated
and underscored form.

---

### Scenario: the register has 34 entries, 1–34, no gaps
- Status: EXECUTED
- Input: `PROJECT_CONTEXT.md` §"Deferred-substitution register", every numbered
  table row from line 3073 onward
- Expected: 34 contiguous entries
- Actual: **34 distinct numbers, contiguous 1–34.** Unchanged from the previous
  pass: pass 20 opened, closed and narrowed nothing
- Result: PASS
- Evidence: 58 numbered rows across the pass-ordered sections, resolving to the
  distinct set 1…34

### Scenario: `AC-F1-08` is claimed by nothing
- Status: EXECUTED · Expected: zero claims
- Actual: **1 node ID, self-denying** —
  `backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`,
  a parametrisation label on a scenario asserting the export is **refused**.
  **0 `COVERS` joins**
- Result: PASS
- Evidence: witnessed at runtime too — smoke S16, `/audit/export` names it unmet
  on the auditor's own screen (`F1-08=True`)

### Scenario: `AC-F1-11` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID**, the sibling label `[anchor-AC-F1-11]` on the same
  refusal scenario. **0 `COVERS` joins**
- Result: PASS · Evidence: smoke S16, `F1-11=True`

### Scenario: `AC-REFUSAL-11` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS

### Scenario: `AC-F40-17` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS

### Scenario: `AC-F36-48` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs. 2 `COVERS` lines mention it and both deny themselves in
  the same sentence** — *"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48,
  WHICH IS ITSELF DENIED"* (`backend/tests/test_abstention.py:331`) and
  *"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48 (its above-band tail)"*
  (`:360`)
- Result: PASS

### Scenario: `AC-F5-02` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **2 node IDs, both self-denying** —
  `test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory` and
  `test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`, which
  asserts the build does not claim it. **1 `COVERS` line, explicitly narrowed**:
  *"COVERS ONLY THE REGISTRATION CLAUSE OF AC-F5-02. It does NOT claim
  `AC-F5-02`, which this build does not meet"*
  (`tests/suites/functional/test_unclaimed_criteria.py:355`)
- Result: PASS

### Scenario: `AC-F5-03` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID**,
  `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`.
  **0 `COVERS` joins**
- Result: PASS

### Scenario: `AC-F5-05` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS

### Scenario: the claim surface did not move since the last pass
- Status: EXECUTED
- Input: the eight scans above, compared to the pass-19 record
- Expected: no criterion gained a claim
- Actual: **byte-identical outcome on all eight.** The only node-id change in
  the whole tree this pass is
  `test_every_kind_the_build_holds_has_its_words_written_out_in_this_file`,
  which references no criterion ID
- Result: PASS
- Evidence: the `+1 / −0` node-id delta recorded in the unit/integration file

---

## Register 34's three "built instead" claims, each held by a check that can fail

### Scenario: claim 1 — `/inventory` names the four and says `AC-F5-02` NOT met
- Status: EXECUTED
- Actual: **real, and observed three ways this pass** — in the test tree, over
  real HTTP (smoke S12: `absent=['agent.anomaly-detect',
  'agent.crossperiod-surveillance', 'agent.fidelity-check',
  'agent.omission-detector']`, `notice=True`), and in a real browser
  (rendered-UI: four `data-principal` values read off the rendered DOM)
- Result: PASS

### Scenario: claim 2 — the unqualified sentence is on NO reachable screen
- Status: EXECUTED
- Actual: **real.** Corroborated over real HTTP by a crawl from `/` following
  only rendered links — **46 URLs reached, zero offenders, all five agent pages
  among them** — so it cannot pass by reaching nothing. Also checked in the
  browser against rendered `innerText`, not source bytes
- Result: PASS — this is the correction to entry 34's *"gone from that screen"*,
  and it holds of the whole surface

### Scenario: claim 3 — `/inventory` links each absent agent to its agent page
- Status: EXECUTED
- Actual: **real, and driven rather than asserted.** Smoke S25 followed all four
  hrefs (four 200s, each `h1` equal to the principal id its row names), and the
  rendered-UI suite **clicked** all four in Chromium and read the resulting `h1`
- Result: PASS
