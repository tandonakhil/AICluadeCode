# Test evidence — the deferred-substitution register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> *Does any suite report a pass the register says cannot be true?*

**NO — for the fourth consecutive pass, and now over a forbidden set of NINE
rather than eight.**

**Method:** all **3,037** collected node IDs, plus every `COVERS` line in both
test trees (**297** of them), scanned for each forbidden criterion ID in both
hyphenated and underscored form.

**What changed since pass 20:** register entry 34 was **BROADENED** at gate 7
pass 21 to carry `AC-F5-07`, on `functional-design-agent`'s §28.2 ruling that
*each agent* quantifies over the agents that have **acted**, not over the
registry the Inventory projects. Reading it the other way makes the criterion
satisfiable by the projection of the registry onto itself — the tautology gate
8 already found in `AC-F5-02`, relocated one criterion to the right. **The
forbidden set is nine.** No entry was opened, closed or narrowed.

---

### Scenario: the register has 34 entries, 1–34, no gaps
- Status: EXECUTED
- Input: `PROJECT_CONTEXT.md` §"Deferred-substitution register", every numbered row
- Expected: 34 contiguous entries
- Actual: **34, contiguous 1–34.** Entries 6, 8, 10, 11, 13, 14, 16, 18 and 25 CLOSED; entry 34 broadened at pass 21
- Result: PASS

### Scenario: `AC-F1-08` is claimed by nothing
- Status: EXECUTED · Expected: zero claims
- Actual: **1 node ID, self-denying** — `test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`, a parametrisation label on a scenario asserting the export is **refused**. **0 `COVERS` joins**
- Result: PASS
- Evidence: witnessed at runtime too — smoke S16, `/audit/export` names it unmet on the auditor's own screen (`F1-08=True`)

### Scenario: `AC-F1-11` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID**, the sibling label `[anchor-AC-F1-11]` on the same refusal scenario. **0 `COVERS` joins**
- Result: PASS · Evidence: smoke S16, `F1-11=True`

### Scenario: `AC-REFUSAL-11` is claimed by nothing
- Status: EXECUTED · Expected: zero · Actual: **0 node IDs, 0 `COVERS` joins** · Result: PASS

### Scenario: `AC-F40-17` is claimed by nothing
- Status: EXECUTED · Expected: zero · Actual: **0 node IDs, 0 `COVERS` joins** · Result: PASS

### Scenario: `AC-F36-48` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs. 2 `COVERS` lines mention it and both deny themselves in the same sentence** — *"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH IS ITSELF DENIED"* (`test_abstention.py:331`) and *"…(its above-band tail)"* (`:360`)
- Result: PASS

### Scenario: `AC-F5-02` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **2 node IDs, both self-denying** — `test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory` and `test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`. **1 `COVERS` line, explicitly narrowed**: *"COVERS ONLY THE REGISTRATION CLAUSE OF AC-F5-02. It does NOT claim `AC-F5-02`, which this build does not meet"*
- Result: PASS

### Scenario: `AC-F5-03` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID**, `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`. **0 `COVERS` joins**
- Result: PASS

### Scenario: `AC-F5-05` is claimed by nothing
- Status: EXECUTED · Expected: zero · Actual: **0 node IDs, 0 `COVERS` joins** · Result: PASS

### Scenario: `AC-F5-07` is claimed by nothing — NEW to the forbidden set this pass
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID**, `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_IS_NOT_MET_the_agents_that_acted_have_no_real_version_or_entitlements` — the established `_IS_NOT_MET_` shape, which fails **in either direction**, including the day the ids are reconciled and the disclosure is left standing. **0 `COVERS` joins**
- Result: PASS
- Evidence: the two joins that previously scored it satisfied are **gone** — `pages.inventory`'s own docstring carried the bare ID as an unqualified claim (`afe9e88` removed it) and the test file's section header read "Inventory — `AC-F5-07`" (now "AC-F5-08 (met), AC-F5-07 (NOT MET, claimed by nothing)"). The two scenarios that quantified over **registered** agents were removed and replaced by explicitly `REGISTERED`-scoped ones (see the unit/integration removal table)

### Scenario: the claim surface did not move in the wrong direction since the last pass
- Status: EXECUTED
- Input: the nine scans above, compared to the pass-20 record
- Expected: no criterion gains a claim; the newly-forbidden one arrives already unclaimed
- Actual: **eight unchanged; `AC-F5-07` moved from claimed to recorded-unmet.** No criterion gained a claim
- Result: PASS

### Scenario: `AC-F41-13` is claimed by nothing, in either tree, including docstrings
- Status: EXECUTED · Expected: zero anywhere under `dev/`
- Actual: **0 node IDs, 0 `COVERS` lines, 0 source occurrences of any kind**
- Result: PASS · Evidence: `f41-13-ruling-2026-08-04.md` §1

---

## Register 34's "built instead" claims, each held by a check that can fail

### Scenario: claim 1 — `/inventory` names the four and says `AC-F5-02` NOT met
- Status: EXECUTED
- Actual: **real, observed three ways** — in the test tree; over real HTTP (smoke S12: four absent principals named, notice present); and in a real browser (four `data-principal` values read off the rendered DOM, four links clicked)
- Result: PASS

### Scenario: claim 2 — the unqualified sentence is on NO reachable screen
- Status: EXECUTED
- Actual: **real.** A crawl from `/` following only rendered links reached **46 URLs, zero offenders**, with all five agent pages among them — so it cannot pass by reaching nothing
- Result: PASS · Evidence: smoke S27

### Scenario: claim 3 (new at pass 21) — `AC-F5-08` is MET and does not imply `AC-F5-07`
- Status: EXECUTED
- Actual: **real.** Four authorship-only rows, each with `not recorded` naming the registry gap for version, entitlements and status; **24** "not recorded" statements on the served screen and **zero** blank/dash placeholders; and the screen states in its own words that this does **not** satisfy `AC-F5-07`
- Result: PASS · Evidence: smoke S36; mutation M9
