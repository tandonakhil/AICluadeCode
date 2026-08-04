# Test evidence — the deferred-substitution register cross-check

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The standing question

> *Does any suite report a pass the register says cannot be true?*

**NO — for the second consecutive pass.**

**Method:** all 2,987 collected node IDs, plus every `COVERS` line in both test
trees, scanned for each of the eight forbidden criterion IDs in both hyphenated
and underscored form. Plus a full diff of every `AC-…` identifier referenced
anywhere in either tree, `1b1b56e` vs `e00a214`.

---

### Scenario: the register has 34 entries, 1–34, no gaps
- Status: EXECUTED
- Input: `PROJECT_CONTEXT.md` §"Deferred-substitution register"
- Expected: 34 contiguous entries
- Actual: **34, contiguous 1–34.** Pass 19 opened, closed and narrowed nothing;
  it appended three **corrections** to entries 33 and 34, which is the honest
  form for "accurate when written, no longer the whole picture"
- Result: PASS

### Scenario: `AC-F1-08` is claimed by nothing
- Status: EXECUTED · Expected: zero claims
- Actual: **1 node ID, self-denying** —
  `test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`,
  a parametrisation label on a scenario asserting the export is **refused**.
  **0 `COVERS` joins**
- Result: PASS
- Evidence: witnessed at runtime too — smoke S16, `/audit/export` names it unmet
  on the auditor's own screen (`F1-08=True`)

### Scenario: `AC-F1-11` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID, the sibling label `[anchor-AC-F1-11]` on the same refusal
  scenario. 0 `COVERS` joins**
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
  the same sentence** — *"COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH
  IS ITSELF DENIED"* (`test_abstention.py:331`, `:360`)
- Result: PASS

### Scenario: `AC-F5-02` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **2 node IDs, both self-denying** —
  `test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory` and
  the new `test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`,
  which asserts the build does not claim it. **1 `COVERS` line, explicitly
  narrowed**: *"COVERS ONLY THE REGISTRATION CLAUSE OF AC-F5-02. It does NOT
  claim `AC-F5-02`, which this build does not meet"*
- Result: PASS
- Note: the new node ID is the only change since last pass, and it moves in the
  right direction — a second scenario asserting the criterion is unclaimed

### Scenario: `AC-F5-03` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **1 node ID,
  `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`. 0
  `COVERS` joins**
- Result: PASS

### Scenario: `AC-F5-05` is claimed by nothing
- Status: EXECUTED · Expected: zero
- Actual: **0 node IDs, 0 `COVERS` joins**
- Result: PASS

---

## Register 34's three "built instead" claims, each now held by a check

### Scenario: claim 1 — `/inventory` names the four and says `AC-F5-02` NOT met
- Status: EXECUTED · Actual: **real, mutation-held**; also observed in the
  browser and over HTTP (smoke S12, rendered `absent` = the four ids)
- Result: PASS

### Scenario: claim 2 — the unqualified sentence is on NO reachable screen
- Status: EXECUTED
- Actual: **real, mutation-held in both directions** (M1 restores it and fails
  naming five pages; M2a cripples the traversal and fails on the containment
  half). Corroborated over real HTTP: 46 URLs crawled from `/`, zero offenders,
  five agent pages reached
- Result: PASS — this is the correction to entry 34's *"gone from that screen"*,
  and it is now true of the whole surface

### Scenario: claim 3 — `/inventory` links each absent agent to its agent page
- Status: EXECUTED
- Actual: **real and now mutation-held.** At `1b1b56e` this claim was carried by
  nothing: repointing all four hrefs at `/inventory` left 2,977 green. It now
  fails, and so does landing on the wrong agent
- Result: PASS — this was `PARTIAL` last pass and is now a full pass

### Scenario: claim 4 — `unregistered_actors` is the broker's answer
- Status: EXECUTED
- Actual: **corrected and held.** The field returned a bare `[]` from a source
  that structurally cannot hold the answer. It now returns register 33's
  convention-C2 UNKNOWN shape, is rendered on `/inventory`, and is asserted by
  two scenarios — one on the shape, one joining `computable: False` to the
  `LINEAGE_UNTRAVERSED` entry that justifies it. Four mutations caught
- Result: PASS — this was the ADVISORY finding last pass and is closed

## Criteria-reference diff, base vs head

### Scenario: no criterion silently stopped being named
- Status: EXECUTED
- Input: every `AC-[A-Z0-9]+-[0-9]+` in `backend/tests` + `tests/suites` at
  `1b1b56e` and at `e00a214`
- Expected: nothing lost
- Actual: **256 → 256. 0 lost, 0 gained**
- Result: PASS
