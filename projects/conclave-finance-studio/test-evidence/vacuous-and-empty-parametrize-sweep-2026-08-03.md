# Test evidence — vacuous-pass and empty-`parametrize` sweep

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

AST sweep over every `test_*.py` in `backend/tests` and `tests/suites`.
Script `scratchpad/sweeps18.py`, output `scratchpad/p19/sweeps.out`.

---

### Scenario: no `parametrize` collects zero cases
- Status: EXECUTED
- Input: every `@pytest.mark.parametrize` argvalues expression, static and then
  cross-checked against the collected node ids
- Expected: none empty — an empty argvalues list collects zero cases and reports
  as a pass with pytest saying nothing about it
- Actual: **NONE.** And the collected count reconciles exactly:
  2,309 + 358 + 194 + 61 + 28 + 23 + 14 = 2,987
- Result: PASS
- Evidence: `sweeps.out` §1 — `NONE`. The build also defends this itself:
  `test_the_vocabulary_is_the_three_sub_types_and_has_not_silently_emptied`
  exists specifically so the `KIND_VOCABULARY` parametrisation cannot become
  vacuous

### Scenario: no test function can pass without being able to fail
- Status: EXECUTED
- Input: functions with no `assert`, no `raise`, no `pytest.raises/warns`, no
  `fail/xfail/skip`
- Expected: any hit must delegate to a helper that itself asserts or raises
- Actual: **13 candidates, all 13 delegate.** Read in full:

| Candidate | Delegates to |
|---|---|
| `test_ordinary_settings_pass` | `ab.assert_no_abstention_control(...)` |
| `test_api_startup_guard_passes_on_a_clean_environment` | `credentials.assert_api_process_holds_no_credentials()` |
| `test_api_startup_guard_ignores_an_empty_value` | same |
| `test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business` | `p.validate_published_figure(...)` |
| `test_every_render_passes_its_own_boundary_check` | same, over `LABEL_SOURCES × SURFACES` |
| `test_the_multi_surface_form_passes_on_clean_surfaces` | `R.any_band_is_not_readable(...)` |
| `test_every_number_the_coding_leg_emits_is_hashable_evidence` | `canonical.content_hash(...)` — refuses floats |
| `test_every_number_the_narrative_leg_emits_is_hashable_evidence` | same |
| `test_importing_chrome_has_already_asserted_no_green` | `tokens.assert_no_green()` |
| `test_every_item_in_the_pilot_close_has_a_reachable_dossier` | `U.fetch()` — asserts status 200 |
| `test_every_selector_in_the_stylesheet_parses` | `cssmatch.compile_selector()` — raises if unimplemented |
| `test_AC_F12_15_the_reviewer_facing_surfaces_do_not_expose_the_band_as_a_number` | `rendered_numbers.band_is_not_readable(...)` over a 3-element literal tuple |
| `test_neither_shipped_palette_contains_a_green` | `tokens.assert_no_green()` |

- Result: PASS — **zero vacuous scenarios**

### Scenario: loops over possibly-empty iterables
- Status: EXECUTED
- Expected: reported as REVIEW, not as defect — many are guarded elsewhere
- Actual: **25 flagged.** Every one iterates either a module-level literal
  constant (`CARRIED_SYMBOLS`, `_POAR_COLUMNS`, `EVIDENCE_TABLES`) or a
  collection the same function first asserts non-empty. Two of the 25 are the
  pass-19 additions (`AC-F38-01`'s cards, `AC-F5-07`'s agent rows) and **both**
  assert the population against the broker's payload before looping —
  `assert payload, "no agent in the inventory payload, so the criterion is
  untested"` and `assert {cards} == set(rows)`
- Result: PASS (review complete, no defect)

### Scenario: a suite with zero scenarios would be reported as such
- Status: EXECUTED
- Input: `tests/suites/_runner.sh` exit-code contract
- Expected: exit 3 for an empty suite, 4 for cannot-execute — never 0
- Actual: **no suite returned 3 or 4.** All six returned 0 with a non-zero
  scenario count
- Result: PASS
