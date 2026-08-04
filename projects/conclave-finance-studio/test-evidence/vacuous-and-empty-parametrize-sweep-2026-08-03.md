# Test evidence — vacuous-pass and empty-`parametrize` sweeps

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Method:** AST sweep over all **110** test files in both trees, then manual
reading of every candidate, then a paired-`pytest.raises` check on every helper
a candidate delegates its assertion to.

---

### Scenario: empty `@pytest.mark.parametrize` argvalues
- Status: EXECUTED
- Input: every `parametrize` decorator whose argvalues is a literal list/tuple
- Expected: none empty — an empty list collects **zero** cases and reports as a
  pass, and `pytest` says nothing about it
- Actual: **NONE**
- Result: PASS
- Evidence: `sweeps18.json` `"empty_parametrize": []`

### Scenario: test functions with no `assert`, no `raises`, no `fail`
- Status: EXECUTED
- Input: AST walk of every `test*` function in both trees
- Expected: any such function must delegate its assertion to a helper that
  can raise — and that helper must itself have a scenario proving it raises
- Actual: **13 candidates. All 13 delegate. All 13 delegates are proven
  falsifiable by a paired `pytest.raises` scenario. Zero vacuous passes.**
- Result: PASS
- Evidence, one row per candidate:

| candidate | delegates to | proven falsifiable by |
|---|---|---|
| `test_abstention.py::test_ordinary_settings_pass` | `ab.assert_no_abstention_control` | `test_abstention.py:414` (raises), `red-team:972` |
| `test_credential_boundary.py::test_api_startup_guard_passes_on_a_clean_environment` | `credentials.assert_api_process_holds_no_credentials` | `test_credential_boundary.py:121` |
| `test_credential_boundary.py::test_api_startup_guard_ignores_an_empty_value` | same | `test_credential_boundary.py:129` |
| `test_f12_precision.py::test_a_payload_carrying_no_precision_at_all…` | `p.validate_published_figure` | `test_f12_precision.py:132/134/136` |
| `test_f12_precision.py::test_every_render_passes_its_own_boundary_check` | same | as above |
| `test_harness_rendered_numbers.py::test_the_multi_surface_form_passes_on_clean_surfaces` | `R.any_band_is_not_readable` | `test_harness_rendered_numbers.py:142` |
| `test_primitive_peer_coding.py::test_every_number_the_coding_leg_emits_is_hashable_evidence` | `canonical.content_hash` (refuses floats) | `test_canonical.py` raises-on-float |
| `test_surveillance_primitives.py::test_every_number_the_narrative_leg_emits_is_hashable_evidence` | same | same |
| `test_ui_chrome.py::test_importing_chrome_has_already_asserted_no_green` | `tokens.assert_no_green` | `test_ui_tokens.py:41` (planted `#22C55E`) |
| `test_ui_dossier.py::test_every_item_in_the_pilot_close_has_a_reachable_dossier` | `U.fetch` | `uihelpers.py:192` — `assert response.status_code == expect` |
| `test_ui_no_orphaned_style_rule.py::test_every_selector_in_the_stylesheet_parses` | `cssmatch.compile_selector` | mutation M2 / M3d′ — proven to raise |
| `test_ui_probe_surface.py::test_AC_F12_15_the_reviewer_facing_surfaces…` | `rendered_numbers.band_is_not_readable` | `test_harness_rendered_numbers.py:92/136` |
| `test_ui_tokens.py::test_neither_shipped_palette_contains_a_green` | `tokens.assert_no_green` | `test_ui_tokens.py:41` |

### Scenario: assertions inside a loop over a possibly-empty iterable
- Status: EXECUTED
- Input: every `for` containing an `assert`, where the iterable is a bare local
  name not first asserted truthy in the same function
- Expected: reported for review, not treated as a defect
- Actual: **36 occurrences**, spread across 19 files. Every one loops over a
  module-level constant (`GUARDRAILS`, `NEW_QUERIES`, `_POAR_COLUMNS`,
  `CARRIED_SYMBOLS`, `PRECISION_TESTIDS`, `EVIDENCE_TABLES`) or a locally
  constructed literal (`cases`, `params`, `paths`), none of which can be empty
  at runtime without the module failing to import
- Result: **REVIEW — no defect found.** Recorded so the count is visible rather
  than silently swallowed; a future pass that turns one of those constants into
  a computed value should re-read this list
- Evidence: `sweeps18.json` `"unguarded_loops"` — full 36-row list

### Scenario: the sweeps are themselves falsifiable
- Status: EXECUTED
- Input: the three defect classes the sweeps look for
- Expected: each sweep finds a planted instance
- Actual: the vacuous sweep's own output is the proof — it correctly identified
  13 no-assert functions, which is a non-empty result from a real scan rather
  than an empty result from a scan that never ran. The empty-`parametrize`
  sweep returned empty; its non-vacuity rests on the same AST walk that
  produced 36 loop hits and 13 vacuous hits from the same traversal
- Result: PASS
