# Test evidence — sampling sweep

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The sweep this file records

The sampling sweep looks for scenarios whose **name quantifies** ("each",
"every", "no…anywhere") over a population the scenario does not actually
traverse. Gate 8 raised two findings of this shape; both closed at pass 20 and
both remain closed. **No new finding of this shape was opened this pass.**

The sweep was re-run in its instrumented form — see
`vacuous-and-empty-parametrize-sweep-2026-08-04.md`, which measured the real
iteration count of all **426** assert-bearing loops rather than reading them.
The sampling below is the targeted half: the scenarios added this pass whose
names make a universal claim.

---

### Scenario: Finding B — the kind vocabulary compared to its own source
- Status: EXECUTED
- Input: `test_each_kind_labels_its_own_fields_in_its_own_words`, at `7757e0d`
- Expected: still pinned to `EXPECTED_KIND_WORDS`, still guarded by the key-set companion
- Actual: **CLOSED and unchanged.** Neither file was touched by any of the six commits in this range
- Result: PASS

### Scenario: Finding A — `AC-F40-16` quantifying over a one-row register
- Status: EXECUTED
- Input: `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`, at `7757e0d`
- Expected: still driving three real exports with `count >= 3` asserted before the loop
- Actual: **CLOSED and unchanged.** Instrumented count `[3, 3]`
- Result: PASS
- Evidence: `loops22.json`

---

## The scenarios added this pass whose names quantify

### Scenario: `test_AC_F41_22_the_three_elements_are_co_visible_and_nothing_here_approves`
- Status: EXECUTED
- Input: the name claims a property of *this screen* at *any permission level*
- Expected: the population is every awaiting finding screen reachable from `/`, at both personas, guarded so a traversal reaching nothing cannot pass
- Actual: **traversal iterates 47 URLs; the per-screen body runs 14 times; `assert len(checked) >= 8`; `assert seen_eligibility == {"true","false"}`** so it cannot pass by reaching only ineligible items
- Result: PASS

### Scenario: `test_every_evidential_element_of_the_screen_is_in_the_artefact_verbatim`
- Status: EXECUTED
- Input: "every … element" — over what?
- Expected: a real, guarded population, and the comparison target must not be the thing under test
- Actual: **iterates 7 elements, guarded by `assert len(region) >= 6`.** But the population is `pages.approval_evidential_region(...)` — **the region, not the rendered screen**. See the M3b advisory in `mutation-tests-2026-08-04.md`: the name reads as a claim about *the screen* and the assertion is about *the region*. **Not a vacuous pass and not a build defect** — the property does hold, verified screen-to-artefact over HTTP by smoke S32 — but the in-tree scenario's population is narrower than its name
- Result: PASS, with the naming/population mismatch reported as an advisory for `code-agent`

### Scenario: `test_every_dossier_in_the_export_carries_a_view_with_no_reference`
- Status: EXECUTED · Expected: a real dossier population · Actual: **iterates 6 dossiers, inner banned-construct loop 4 × 6** · Result: PASS

### Scenario: `test_every_name_in_the_not_retained_list_is_on_the_screen_with_a_reason`
- Status: EXECUTED · Expected: all 8 `NOT_RETAINED` entries · Actual: **iterates 8** · Result: PASS · Evidence: mutations M4 and M6 both fire on it

### Scenario: `test_AC_F41_06_every_reason_the_form_RENDERS_completes_a_rejection`
- Status: EXECUTED
- Input: "every reason the form RENDERS" — the population must come from the rendered form, not from a constant
- Expected: the six reasons are read off the rendered radios and each is driven to completion
- Actual: **it does exactly that**, and mutation M7 (value back to the row index) makes it fail at the store's 422 rather than at a string comparison. Independently corroborated in a real browser: six radios clicked, six `"Rejection recorded"`
- Result: PASS

### Scenario: `test_AC_F5_08_an_agent_known_only_by_authorship_is_LISTED_and_says_what_is_missing`
- Status: EXECUTED · Expected: all four authorship-only agents, not one · Actual: the four absent principals, each row checked for the stated value and the named gap; mutation M9 fires · Result: PASS

### Scenario: no scenario name added this pass claims "anywhere" or "no screen" without a walk
- Status: EXECUTED
- Input: all 54 added node ids, names scanned for universal quantifiers, each traced to its population
- Expected: every universal claim backed by a traversal or a guarded collection
- Actual: **no unbacked universal claim.** The only mismatch found is the region-vs-screen population noted above, which is reported rather than passed over
- Result: PASS
