# Test evidence — changed-scenario audit (the test-count delta, named)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`** ·
previous run at `dev` @ `6bf8ed9`
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Method:** node IDs collected at both commits (a detached worktree at
`6bf8ed9`, the same interpreter), sorted and diffed. Bodies compared with
`git diff 6bf8ed9 1b1b56e -- backend/tests tests/suites`.

| | count |
|---|---|
| previous total | **2,955** |
| added | **+25** |
| removed | **−3** |
| current total | **2,977** |
| changed (same node ID, changed body) | **3** |

2,955 + 25 − 3 = **2,977**. Matches the brief exactly.

Files touched: `cssmatch.py` (new, 200 lines), `test_ui_no_orphaned_style_rule.py`
(new, 246), `test_ui_boundaries.py` (+62), `test_ui_governance_screens.py` (+19),
`test_ui_brand.py` (±1), `uihelpers.py` (+12), `test_unclaimed_criteria.py` (+126).

---

## REMOVED — 3. A removed test is a coverage decision.

### Scenario: `test_AC_F5_02_every_agent_is_listed_with_identity_entitlements_and_version`
- Status: EXECUTED (verified absent from the 2,977)
- Was: `tests/suites/functional/test_unclaimed_criteria.py`
- Why removed: it asserted `inventory == principals.DIRECTORY` — the projection
  against its own source, **an equality that cannot fail for the reason the
  criterion is about**. Gate 8 blocked on it
- Replaced by: `test_the_inventory_needs_no_manual_registration_step`, which
  keeps the same equality but explicitly narrows its `COVERS` line to the
  registration clause and disclaims the criterion
- Result: **removal justified.** Net effect on claimed coverage: `AC-F5-02` goes
  from claimed-and-false to claimed-by-nothing

### Scenario: `test_AC_F5_03_a_lineage_result_STATES_that_it_is_complete_rather_than_sampled`
- Status: EXECUTED (verified absent)
- Why removed: it asserted `lineage["complete"] is True` for every agent while
  seven dossiers exist and zero appear in any lineage — a partial list returned
  labelled complete, which is what `AC-F5-05` forbids
- Replaced by: `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`
- Result: **removal justified**

### Scenario: `test_AC_F5_05_every_lineage_result_states_its_own_completeness`
- Status: EXECUTED (verified absent)
- Was: `backend/tests/test_ui_governance_screens.py`
- Why removed: **renamed**, not deleted — it is now
  `test_every_lineage_result_states_its_own_scope_and_completeness`, with a
  docstring opening *"NOT a claim on `AC-F5-05`"* and a **stronger** body
  (adds `data-scope` and `"Computed over"`)
- Result: **a rename that drops a criterion claim and strengthens the
  assertion.** This is the only one of the three that is not a net reduction

## ADDED — 25.

### Scenario: 19 in `backend/tests/test_ui_no_orphaned_style_rule.py`
- Status: EXECUTED, all 19 pass
- 5 parser (`every_selector_parses`, `selector_list_not_vacuous`,
  `at_rule_refused`, `sibling_combinator_refused`, `unparsable_compound_raises`)
- 8 matcher (`descendant_matches`, `descendant_not_sibling`,
  `child_refuses_grandchild`, `multi_class_needs_all`, `tag_qualified`,
  `attribute_value_compared`, `bare_attribute_presence`, `pseudo_element`)
- 6 build (`every_declared_selector_matches`, `would_have_caught_the_defect`,
  `no_selector_is_excused`, `both_themes_in_the_surface`,
  `context_line_is_styled_at_all`, `context_line_is_a_full_width_line`)
- Evidence: mutation-tested individually in `mutation-tests-2026-08-03.md`
- Note: `code-agent`'s hand-off says "22 scenarios" for this checker. **19 are
  in that file**; the other 3 of the 22 are the two alias scenarios and the
  lineage-rendering scenario below. All 22 exist; the file count is 19

### Scenario: 2 in `backend/tests/test_ui_boundaries.py`
- `test_every_alias_really_serves_ITS_OWN_CANONICAL_SCREEN` — the guard
- `test_the_alias_guard_rejects_a_forged_row` — its negative half
- Status: EXECUTED, both pass; independently reproduced by mutation M7
- Note: the old `test_the_merged_queue_serves_the_same_screen_under_all_three_addresses`
  is **subsumed, not removed** — it survives with the same node ID, refactored
  onto the shared `_screen_body` helper

### Scenario: 1 in `backend/tests/test_ui_governance_screens.py`
- `test_every_lineage_result_states_its_own_scope_and_completeness` (the rename
  target above)
- Status: EXECUTED, passes; mutation-held by D7

### Scenario: 3 in `tests/suites/functional/test_unclaimed_criteria.py`
- `test_the_inventory_needs_no_manual_registration_step`
- `test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory`
- `test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`
- Status: EXECUTED, all three pass; mutation-held in both directions (D1–D9)

## CHANGED — 3 (same node ID, changed body).

### Scenario: `test_ui_brand.py::test_the_brand_layer_is_present_in_the_one_inlined_stylesheet`
- Status: EXECUTED
- Change: marker list `(".lockup", ".statstrip", ".section-icon", ".artifact")`
  → `(… , ".opening")`
- Assessment: **neutral, and explained** — `.artifact` was one of the four
  orphaned selectors this pass removed, so a scenario asserting its presence
  would have contradicted the orphan sweep. Still four markers; not a weakening

### Scenario: `test_ui_governance_screens.py::test_AC_F5_04_a_version_that_touched_nothing_states_zero`
- Status: EXECUTED
- Change: `"Zero artefacts"` → `"Zero decisions in the decision ledger"`, plus a
  **new** assertion `"Artefacts touched 0" in …`
- Assessment: **strengthened**, and the string change follows the scope
  relabelling

### Scenario: `test_unclaimed_criteria.py::test_AC_F5_06_a_retired_agent_is_still_listed…`
- Status: EXECUTED
- Change: `assert retired["lineage"]["complete"] is True` replaced by
  `artefact_count == len(artefacts)` and `scope == "decision_ledger"`
- Assessment: **correctly narrowed.** `AC-F5-06`'s clause is *"its lineage still
  resolves"*, not *"is complete"* — keeping the old line would have made this a
  second carrier of the `AC-F5-05` claim the build cannot support. This is the
  right kind of change and is exactly the kind a pass/fail count hides

## The delta contains no unexplained drop
- Status: EXECUTED
- Expected: every removal accounted for
- Actual: **3 removals, 3 accounted for** — two deliberate retirements of false
  claims, one rename. No scenario disappeared without a successor or a stated
  reason
- Result: PASS
