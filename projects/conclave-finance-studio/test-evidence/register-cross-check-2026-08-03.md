# Test evidence — the deferred-substitution register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

**The standing question — *does any suite report a pass the register says cannot
be true?* — returns YES for the first time in eight passes.**

The five declared criteria are clean. The YES comes from a route the register
does not cover, surfaced by the pass-17 agent page: `AC-F5-02` and
`AC-F5-03`/`-05`. Detail in `functional-2026-08-03.md`.

---

### Scenario: the register has 33 entries, 1–33, no gaps
- Status: EXECUTED
- Input: `PROJECT_CONTEXT.md`'s "Deferred-substitution register" section
- Expected: 33 entries, numbered contiguously
- Actual: **33, contiguous.** Entries 6, 8, 10, 11, 13, 14, 16, 18 and 25 CLOSED;
  1–5, 7 and 9 stand as recorded at pass 1/2c; 3 and 4 remain the two that
  cannot quietly become "MVP1 ready"
- Result: PASS
- Evidence: register closing paragraph, verified against the per-pass subsections

### Scenario: `AC-F1-08` is claimed by nothing
- Status: EXECUTED
- Input: all 2,955 collected node IDs, plus every `COVERS` line
- Expected: zero claims
- Actual: **1 node ID contains the string, and it is self-denying** —
  `test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`,
  a parametrisation label on a scenario asserting the export is **refused**.
  **0 `COVERS` joins.**
- Result: PASS
- Evidence: also witnessed at runtime — smoke S16 confirms `/audit/export` names
  `AC-F1-08` as unmet on the auditor's own screen

### Scenario: `AC-F1-11` is claimed by nothing
- Status: EXECUTED
- Input: as above
- Expected: zero claims
- Actual: **1 node ID, the sibling parametrisation label
  `[anchor-AC-F1-11]` on the same refusal scenario. 0 `COVERS` joins.**
- Result: PASS
- Evidence: smoke S16 — both IDs named as unmet in the served page

### Scenario: `AC-REFUSAL-11` is claimed by nothing
- Status: EXECUTED
- Input: as above
- Expected: zero claims
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS
- Evidence: register 9's narrowing at pass 12 holds — the RT05 pass-throughs are
  asserted as pass-throughs in the red-team suite

### Scenario: `AC-F40-17` is claimed by nothing
- Status: EXECUTED
- Input: as above
- Expected: zero claims
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS
- Evidence: register 28; `AC-F40-18` is built and separately evidenced —
  smoke S15 returned `data-authorised-on="synthetic_attestation"`, a status
  distinct from `no_drift`

### Scenario: `AC-F36-48` is claimed by nothing
- Status: EXECUTED
- Input: as above
- Expected: zero claims
- Actual: **0 node IDs. 2 `COVERS` lines mention it and both deny themselves in
  the same sentence** — `"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48,
  WHICH IS ITSELF DENIED"` (`test_abstention.py:331`, `:360`)
- Result: PASS
- Evidence: register 27

### Scenario: the 200 NEW node IDs were scanned with the same query
- Status: EXECUTED
- Input: the 200 node IDs added since `9d605b1`
- Expected: none names any of the five
- Actual: **zero hits**
- Result: PASS
- Evidence: the pass-17 UI work introduced no new claim on a declared criterion

### Scenario: the register's OTHER unmet criteria are still unclaimed
- Status: EXECUTED
- Input: `AC-F41-08`, `AC-F12-05` (register 18, CLOSED at pass 12 — both now
  legitimately claimable and claimed), `AC-F26-05`/`AC-F38-11` (register 6,
  CLOSED at pass 11)
- Expected: the closures are real, so claims on these are legitimate
- Actual: legitimate; and the close-clock staleness is rendered on the served
  surface — `Close day Day 3`, `1 close day(s) behind the close clock`
- Result: PASS
- Evidence: visible in `ux-queue-desktop-1280-2026-08-03.png` masthead

### Scenario: **FINDING** — `AC-F5-02` is reported PASS and the build cannot support it
- Status: EXECUTED
- Input: `AC-F5-02`'s Given clause — *"an agent that has been deployed and has
  **performed at least one action**"* — against `/inventory`
- Expected: every agent that acted appears in the Inventory
- Actual: **four of the five agents that authored findings in the pilot run are
  absent from `/inventory`**, and the covering scenario passes because it
  compares the inventory to `principals.DIRECTORY` — the projection against its
  own source, an equality that cannot fail for this reason
- Result: **FAIL**
- Evidence: reproduced over HTTP against the served pilot as smoke **S12**.
  This is not in the 33-entry register; it has no entry, and on the evidence it
  needs one. It is the downstream half of the id disagreement `code-agent`
  disclosed **on the agent page only**.

### Scenario: **FINDING** — `AC-F5-03`/`-05` lineage completeness
- Status: EXECUTED
- Input: `AC-F5-05` — *"a partial list is never returned unlabelled"*
- Expected: an unresolvable lineage is labelled incomplete and names what could
  not be traversed
- Actual: seven dossiers exist; **zero appear in any lineage**; the union across
  all eleven inventory rows is 9 artefacts, none a dossier; **every row reports
  `complete=True`**, and the covering scenario asserts exactly that
- Result: **FAIL**
- Evidence: see `functional-2026-08-03.md`
