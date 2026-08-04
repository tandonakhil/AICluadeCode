# Test evidence — the deferred-substitution register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> *Does any suite report a pass the register says cannot be true?*

**It returns NO.** It returned **YES** last run, for the first time in seven
passes, on `AC-F5-02`/`-03`/`-05`. Pass 18 closed that, and every one of the
eight forbidden criteria is now claimed by nothing.

**This is not a clean sheet.** Three findings sit *beside* the register rather
than against it — the register is not contradicted by any of them, and all
three are in `functional-2026-08-03.md`. Finding 1 is the one that should stop
the gate: the disclosure register 34 credits was removed from one screen and
left standing on the four screens that screen links to.

**Method:** all 2,977 collected node IDs, plus every `COVERS` line in both test
trees, scanned for each criterion ID in both hyphenated and underscored form.

---

### Scenario: the register has 34 entries, 1–34, no gaps
- Status: EXECUTED
- Input: `PROJECT_CONTEXT.md` §"Deferred-substitution register"
- Expected: 34 entries, contiguous
- Actual: **34, contiguous 1–34.** Entry 34 is new since the last run
- Result: PASS
- Evidence: entry numbers extracted from the table rows: `1 2 3 … 33 34`

### Scenario: `AC-F1-08` is claimed by nothing
- Status: EXECUTED
- Expected: zero claims
- Actual: **1 node ID, and it is self-denying** —
  `test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`,
  a parametrisation label on a scenario asserting the export is **refused**.
  **0 `COVERS` joins**
- Result: PASS
- Evidence: also witnessed at runtime — smoke S16, `/audit/export` names it as
  unmet on the auditor's own screen

### Scenario: `AC-F1-11` is claimed by nothing
- Status: EXECUTED
- Expected: zero claims
- Actual: **1 node ID, the sibling label `[anchor-AC-F1-11]` on the same
  refusal scenario. 0 `COVERS` joins**
- Result: PASS
- Evidence: smoke S16 — both IDs named as unmet in the served page

### Scenario: `AC-REFUSAL-11` is claimed by nothing
- Status: EXECUTED · Expected: zero · Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS · Evidence: register 9's pass-12 narrowing holds

### Scenario: `AC-F40-17` is claimed by nothing
- Status: EXECUTED · Expected: zero · Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS · Evidence: register 28; `AC-F40-18` is separately evidenced —
  smoke S15 returned `data-authorised-on="synthetic_attestation"`

### Scenario: `AC-F36-48` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs. 2 `COVERS` lines mention it and both deny themselves in
  the same sentence** — *"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48,
  WHICH IS ITSELF DENIED"* (`test_abstention.py:331`, `:360`)
- Result: PASS · Evidence: register 27

### Scenario: `AC-F5-02` is claimed by nothing — **the new one**
- Status: EXECUTED
- Expected: zero claims
- Actual: **1 node ID, and it asserts the criterion is UNMET** —
  `test_unclaimed_criteria.py::test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory`.
  **1 `COVERS` line, and it narrows itself explicitly**: *"COVERS ONLY THE
  REGISTRATION CLAUSE OF AC-F5-02. It does NOT claim `AC-F5-02`, which this
  build does not meet"*
- Result: PASS
- Evidence: the two scenarios that DID claim it are gone — see
  `changed-scenario-audit-2026-08-03.md`

### Scenario: `AC-F5-03` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID, `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`
  — an assertion of unmet-ness. 0 `COVERS` joins**
- Result: PASS

### Scenario: `AC-F5-05` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs, 0 `COVERS` joins.** The unit scenario that used to
  carry the ID was renamed to
  `test_every_lineage_result_states_its_own_scope_and_completeness` and its
  docstring opens *"NOT a claim on `AC-F5-05`"*
- Result: PASS

### Scenario: the 25 NEW node IDs were scanned with the same query
- Status: EXECUTED
- Input: the 25 scenarios added since `6bf8ed9`
- Expected: none of them claims a forbidden criterion
- Actual: **none.** The only forbidden-criterion strings in the new IDs are the
  three `IS_NOT_MET` / `ARE_NOT_MET` names, which assert unmet-ness
- Result: PASS

### Scenario: register 34's three "built instead" claims, checked one by one
- Status: EXECUTED
- Expected: each is real and held by a scenario
- Actual: **2 of 3 real and mutation-held; 1 held by nothing**
  1. `/inventory` names the four, says `AC-F5-02` NOT met, unqualified sentence
     gone from that screen — **real, mutation-held** (D3, D4)
  2. every lineage row states scope + INCOMPLETE + untraversed classes —
     **real, mutation-held** (D5, D6, D7, D8)
  3. `/ges/inventory` returns `unregistered_actors` — **the field exists and
     returns `[]` while four unregistered actors exist; no scenario in either
     tree asserts it**
- Result: **PARTIAL** — recorded as such, not rounded up
- Evidence: `functional-2026-08-03.md` Finding 3

### Scenario: register 16's `AC-F5-07` — the question `code-agent` asked
- Status: EXECUTED
- Input: mutation F7-M, stripping the criterion's two fields from every agent
  row but the first
- Expected: something in 2,977 scenarios notices
- Actual: **nothing notices. 2,977 green**
- Result: **FAIL — the criterion is unheld.** `AC-F5-07` is currently *listed
  as met* on the strength of a scenario that inspects one member of a
  population the criterion quantifies over with "each"
- Evidence: `functional-2026-08-03.md` Finding 2. Register 16 records
  `AC-F5-07` as CLOSED at the pass that built the six missing screens; this
  finding does not reopen the screen question, it questions the check
