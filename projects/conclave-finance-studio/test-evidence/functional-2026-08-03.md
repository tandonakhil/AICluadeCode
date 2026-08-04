# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Suite owner:** `functional-agent` / `functional-design-agent` — scenarios authored by that agent, **executed and reported here by `test-agent`**
**Blocking:** yes (project Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**358 scenarios, 358 pass, 0 fail, 0 skip, exit 0.**

Entry point `dev/tests/suites/_runner.sh functional`, which reported
`EXECUTED — suite passed` (exit 0). The same scenarios also ran inside all six
whole-tree runs (canonical, `file`, `reverse`, three salted shuffles) and inside
the AST-instrumented run.

## Test-count delta

| | Previous run (`e00a214`) | This run (`c428fe5`) | Delta |
|---|---|---|---|
| collected | 358 | **358** | **0 — unchanged** |
| added | — | — | 0 |
| removed | — | — | **0** |
| changed in place | — | — | 1 (`test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`) plus 1 docstring-only (`test_the_broker_answers_the_population_question_UNKNOWN_and_not_none`) |

No scenario was removed. The two changed scenarios are the gate-8 findings under test; both mutations now fail (see `mutation-tests-2026-08-03.md`).

---

### Scenario: test_AC_F29_01_omission_named_with_its_history
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_01_omission_named_with_its_history`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_05_insufficient_history_is_not_evaluable_and_not_reported_clear
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_05_insufficient_history_is_not_evaluable_and_not_reported_clear`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_06_a_present_in_range_entry_raises_no_omission
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_06_a_present_in_range_entry_raises_no_omission`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_07_a_present_out_of_range_entry_raises_no_omission
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_07_a_present_out_of_range_entry_raises_no_omission`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_08_and_AC_F42_04_paired_comparison_is_one_result
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_08_and_AC_F42_04_paired_comparison_is_one_result`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_04_identical_selection_on_both_sides
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_04_identical_selection_on_both_sides`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_09_and_AC_F38_02_no_population_means_the_run_does_not_start
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_09_and_AC_F38_02_no_population_means_the_run_does_not_start`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_11_findings_carry_a_dossier_and_a_coverage_statement
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_11_findings_carry_a_dossier_and_a_coverage_statement`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_03_coverage_names_the_unscanned_portions
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_03_coverage_names_the_unscanned_portions`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_04_05_06_the_three_surfaces_are_qualified_identically
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_04_05_06_the_three_surfaces_are_qualified_identically`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_07_a_full_and_a_partial_result_are_textually_different
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_07_a_full_and_a_partial_result_are_textually_different`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_15_a_partial_run_carries_its_banner
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_15_a_partial_run_carries_its_banner`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_08_zero_coverage_produces_no_findings_conclusion
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_08_zero_coverage_produces_no_findings_conclusion`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_16_unclassified_columns_refuse_a_model_bound_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_16_unclassified_columns_refuse_a_model_bound_run`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_17_personal_data_query_is_unroutable_not_filtered
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_17_personal_data_query_is_unroutable_not_filtered`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_01_present_anomaly_named_with_its_historical_range
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_01_present_anomaly_named_with_its_historical_range`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_07_the_threshold_in_force_is_stated
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_07_the_threshold_in_force_is_stated`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_10_and_AC_F42_06_a_lost_dataset_emits_no_conclusion
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_10_and_AC_F42_06_a_lost_dataset_emits_no_conclusion`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_01_an_incomplete_dossier_cannot_be_persisted
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F1_01_an_incomplete_dossier_cannot_be_persisted`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp`
- Expected: `AC-F1-08` IS NOT SATISFIED BY THIS SCENARIO — do not map it to that ID.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_a_detector_run_makes_zero_model_calls
- Status: EXECUTED
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_a_detector_run_makes_zero_model_calls`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_03_an_impairment_or_reserve_request_returns_a_refusal_naming_A19[Assess the impairment on the Bakken CGU for this close.]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_03_an_impairment_or_reserve_request_returns_a_refusal_naming_A19[Assess the impairment on the Bakken CGU for this close.]`
- Expected: COVERS AC-REFUSAL-03.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_03_an_impairment_or_reserve_request_returns_a_refusal_naming_A19[What reserve estimate should we carry for the AR allowance?]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_03_an_impairment_or_reserve_request_returns_a_refusal_naming_A19[What reserve estimate should we carry for the AR allowance?]`
- Expected: COVERS AC-REFUSAL-03.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_03_the_A19_refusal_is_none_of_the_four_forbidden_responses
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_03_the_A19_refusal_is_none_of_the_four_forbidden_responses`
- Expected: COVERS AC-REFUSAL-03 (the Then clause's exclusions).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_03_the_refusal_is_recorded_as_a_control_event
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_03_the_refusal_is_recorded_as_a_control_event`
- Expected: COVERS AC-REFUSAL-03 (via AC-REFUSAL-04's recording, asserted here because a refusal nobody recorded is one no auditor can count).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Is this variance material enough to adjust?-A20-others0]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Is this variance material enough to adjust?-A20-others0]`
- Expected: COVERS AC-REFUSAL-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Please certify that the close is complete.-A21-others1]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Please certify that the close is complete.-A21-others1]`
- Expected: COVERS AC-REFUSAL-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Was the cut-off correct for the December shipments?-A22-others2]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_each_refused_capability_returns_its_own_A_number[Was the cut-off correct for the December shipments?-A22-others2]`
- Expected: COVERS AC-REFUSAL-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Is this variance material enough to adjust?]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Is this variance material enough to adjust?]`
- Expected: COVERS AC-REFUSAL-05 (the four named failures).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Please certify that the close is complete.]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Please certify that the close is complete.]`
- Expected: COVERS AC-REFUSAL-05 (the four named failures).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Was the cut-off correct for the December shipments?]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_05_none_of_the_three_returns_a_null_an_empty_set_or_a_generic_decline[Was the cut-off correct for the December shipments?]`
- Expected: COVERS AC-REFUSAL-05 (the four named failures).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_06_a_deferred_capability_request_states_not_in_this_release
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_06_a_deferred_capability_request_states_not_in_this_release`
- Expected: COVERS AC-REFUSAL-06.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_06_the_deferred_response_never_says_it_will_not_be_built
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_06_the_deferred_response_never_says_it_will_not_be_built`
- Expected: COVERS AC-REFUSAL-06 (the "rather than" clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_06_the_two_grammars_differ_on_the_same_surface
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_06_the_two_grammars_differ_on_the_same_surface`
- Expected: COVERS AC-REFUSAL-06 (distinguishability, both documents compared).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_06_a_deferral_is_recorded_under_its_own_event_kind
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_06_a_deferral_is_recorded_under_its_own_event_kind`
- Expected: COVERS AC-REFUSAL-06 (recording).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Reclassify this intercompany balance to the correct legal entity.-f33.legal_entity_and_intercompany]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Reclassify this intercompany balance to the correct legal entity.-f33.legal_entity_and_intercompany]`
- Expected: COVERS AC-REFUSAL-12.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Correct the opex coding on this batch to capex.-f33.opex_capex_caption_crossing]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Correct the opex coding on this batch to capex.-f33.opex_capex_caption_crossing]`
- Expected: COVERS AC-REFUSAL-12.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Reclass this invoice into the prior period to fix the cut-off.-f33.cutoff_resolution]
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_12_an_excluded_F33_sub_type_declines_in_the_deferred_grammar[Reclass this invoice into the prior period to fix the cut-off.-f33.cutoff_resolution]`
- Expected: COVERS AC-REFUSAL-12.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_12_the_decline_is_not_silent_not_empty_and_not_a_refusal
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_12_the_decline_is_not_silent_not_empty_and_not_a_refusal`
- Expected: COVERS AC-REFUSAL-12 (the three named failures).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_12_the_decline_is_recorded_as_a_control_event
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_AC_REFUSAL_12_the_decline_is_recorded_as_a_control_event`
- Expected: COVERS AC-REFUSAL-12 (the recording clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_holds_for_a_direct_post_that_never_rendered_the_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_the_refusal_holds_for_a_direct_post_that_never_rendered_the_screen`
- Expected: COVERS AC-REFUSAL-03 / AC-REFUSAL-05 (obligation M).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_api_process_holds_no_refusal_pattern_of_its_own
- Status: EXECUTED
- Input: `tests/suites/functional/test_ask_request_criteria.py::test_the_api_process_holds_no_refusal_pattern_of_its_own`
- Expected: COVERS AC-REFUSAL-05 (the enforcement point).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_11_every_screen_reached_from_the_entry_point_carries_the_staleness
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F38_11_every_screen_reached_from_the_entry_point_carries_the_staleness`
- Expected: COVERS AC-F38-11 (the "any surface" clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_11_the_staleness_is_beside_the_dataset_version_and_the_as_of
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F38_11_the_staleness_is_beside_the_dataset_version_and_the_as_of`
- Expected: COVERS AC-F38-11 (dataset version, provenance AND staleness, together).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_11_the_staleness_is_a_close_relative_sentence_not_a_bare_timestamp
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F38_11_the_staleness_is_a_close_relative_sentence_not_a_bare_timestamp`
- Expected: COVERS AC-F38-11 (the exclusion `PLAN` §5.6 makes binding).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_11_the_figure_is_computed_against_the_declared_calendar
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F38_11_the_figure_is_computed_against_the_declared_calendar`
- Expected: COVERS AC-F38-11 (the figure is a computation, not a literal).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F38_11_no_control_hides_the_staleness
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F38_11_no_control_hides_the_staleness`
- Expected: COVERS AC-F38-11 (visible, with no affordance that removes it).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_05_the_insufficient_history_state_names_the_measure_that_judged_it
- Status: EXECUTED
- Input: `tests/suites/functional/test_close_clock_criteria.py::test_AC_F9_05_the_insufficient_history_state_names_the_measure_that_judged_it`
- Expected: COVERS AC-F9-05 (the state, and what "periods of history" means).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_a_failing_emission_is_produced_at_all_so_the_gate_has_work
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_a_failing_emission_is_produced_at_all_so_the_gate_has_work`
- Expected: COVERS AC-F36-26 (the precondition clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_the_withheld_output_is_in_no_human_review_queue
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_the_withheld_output_is_in_no_human_review_queue`
- Expected: COVERS AC-F36-26 (no human review queue).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_the_withheld_output_has_no_dossier
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_the_withheld_output_has_no_dossier`
- Expected: COVERS AC-F36-26 (no dossier).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_the_withheld_output_is_on_no_surface_reachable_from_the_entry_point
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_the_withheld_output_is_on_no_surface_reachable_from_the_entry_point`
- Expected: COVERS AC-F36-26 (no surface).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_it_is_absent_rather_than_present_with_a_warning
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_it_is_absent_rather_than_present_with_a_warning`
- Expected: COVERS AC-F36-26 (not emitted with a warning, a badge or a caveat).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_the_denial_record_carries_hash_id_and_the_failed_check
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_the_denial_record_carries_hash_id_and_the_failed_check`
- Expected: COVERS AC-F36-26 (a denial record exists carrying all three).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_26_there_is_no_api_by_which_a_screen_could_obtain_the_withheld_payload
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_26_there_is_no_api_by_which_a_screen_could_obtain_the_withheld_payload`
- Expected: COVERS AC-F36-26 (the shape, not the discipline).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_28_the_same_output_is_not_returned_through_a_direct_api_call
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_28_the_same_output_is_not_returned_through_a_direct_api_call`
- Expected: COVERS AC-F36-28.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_28_the_direct_api_denial_is_identical_in_kind_to_the_front_ends
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_28_the_direct_api_denial_is_identical_in_kind_to_the_front_ends`
- Expected: COVERS AC-F36-28 (identical in kind, same bundle hash, a decision id).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_28_an_admitted_output_IS_returned_through_the_same_route
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_28_an_admitted_output_IS_returned_through_the_same_route`
- Expected: COVERS AC-F36-28 (the negative control).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_29_an_emission_denial_and_an_action_denial_share_one_store
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_29_an_emission_denial_and_an_action_denial_share_one_store`
- Expected: COVERS AC-F36-29.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_field_not_a_guess
- Status: EXECUTED
- Input: `tests/suites/functional/test_emission_gate_criteria.py::test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_field_not_a_guess`
- Expected: COVERS AC-F36-29 (each states whether it denied an action or an emission).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_08_probes_appear_in_the_review_queue
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F41_08_probes_appear_in_the_review_queue`
- Expected: COVERS AC-F41-08 (first clause: the probes appear in the queue).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_08_nothing_rendered_before_disposition_distinguishes_the_probe
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F41_08_nothing_rendered_before_disposition_distinguishes_the_probe`
- Expected: COVERS AC-F41-08 (second clause) and AC-F12-05 (third clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_08_the_count_presented_in_the_period_is_retrievable
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F41_08_the_count_presented_in_the_period_is_retrievable`
- Expected: COVERS AC-F41-08 (third clause). A count for a named period, on the controller's surface, retrievable rather than derivable.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_05_the_capture_identifies_the_probe_and_records_the_response
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_05_the_capture_identifies_the_probe_and_records_the_response`
- Expected: COVERS AC-F12-05, all three clauses together — and only because the third is discharged by the scenario above against a real probe rather than by the absence of one.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_05_an_incorrect_response_is_recorded_as_incorrect
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_05_an_incorrect_response_is_recorded_as_incorrect`
- Expected: The other half of clause 2. A column that is only ever written `1` is a column that records nothing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_11_the_programme_is_disclosed_before_any_item_is_worked
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_11_the_programme_is_disclosed_before_any_item_is_worked`
- Expected: COVERS AC-F12-11. The disclosure is on the queue screen, ahead of the item list, and states all four things the criterion names.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_12_the_reveal_appears_immediately_with_the_answer_and_the_reason
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_12_the_reveal_appears_immediately_with_the_answer_and_the_reason`
- Expected: COVERS AC-F12-12 (the probe leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_12_a_genuine_item_produces_no_reveal
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_12_a_genuine_item_produces_no_reveal`
- Expected: COVERS AC-F12-12 (the genuine leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_12_the_reveal_is_never_rendered_before_the_disposition
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_12_the_reveal_is_never_rendered_before_the_disposition`
- Expected: COVERS AC-F12-12 (the ordering leg). Checked on the item's own screen before anything is submitted, and on a submission the store refused.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_no_standing_role_holds_the_per_person_permission[administrator]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_no_standing_role_holds_the_per_person_permission[administrator]`
- Expected: COVERS AC-F12-13 (first clause). Every role in the system, including administrator, is checked — a table that omitted the most privileged role would satisfy the criterion by not asking the question.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_no_standing_role_holds_the_per_person_permission[controller]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_no_standing_role_holds_the_per_person_permission[controller]`
- Expected: COVERS AC-F12-13 (first clause). Every role in the system, including administrator, is checked — a table that omitted the most privileged role would satisfy the criterion by not asking the question.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_no_standing_role_holds_the_per_person_permission[reviewer]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_no_standing_role_holds_the_per_person_permission[reviewer]`
- Expected: COVERS AC-F12-13 (first clause). Every role in the system, including administrator, is checked — a table that omitted the most privileged role would satisfy the criterion by not asking the question.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_no_standing_role_holds_the_per_person_permission[staff accountant]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_no_standing_role_holds_the_per_person_permission[staff accountant]`
- Expected: COVERS AC-F12-13 (first clause). Every role in the system, including administrator, is checked — a table that omitted the most privileged role would satisfy the criterion by not asking the question.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_the_request_is_denied_by_direct_api_and_returns_nothing
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_the_request_is_denied_by_direct_api_and_returns_nothing`
- Expected: COVERS AC-F12-13 (the "by direct API" clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_no_management_surface_renders_a_per_named_person_probe_figure
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_no_management_surface_renders_a_per_named_person_probe_figure`
- Expected: COVERS AC-F12-13 (the "through any surface" clause), asserted after a real probe outcome exists so the check is about a suppressed figure rather than about an absent one.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_13_the_granted_exercise_is_itself_audited
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_13_the_granted_exercise_is_itself_audited`
- Expected: COVERS AC-F12-13 (second clause). The permission does not exist for any role, so the audited path is exercised at the store with the permission granted explicitly — which is what "granted for a documented, human-initiated review" means.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_14_a_sustained_out_of_band_miss_rate_raises_the_queues_control_state
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_14_a_sustained_out_of_band_miss_rate_raises_the_queues_control_state`
- Expected: COVERS AC-F12-14. Built by recording enough outcomes on one queue for a miss rate to mean anything, then reading the control review.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_14_no_finding_is_raised_against_a_person_and_no_personnel_action
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_14_no_finding_is_raised_against_a_person_and_no_personnel_action`
- Expected: COVERS AC-F12-14 (the clause that makes the control acceptable at all).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_15_no_configuration_value_holds_a_probe_rate
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_15_no_configuration_value_holds_a_probe_rate`
- Expected: COVERS AC-F12-15 (configuration leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_15_no_api_response_or_header_holds_the_rate
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_15_no_api_response_or_header_holds_the_rate`
- Expected: COVERS AC-F12-15 (API and header legs), over every screen the build serves rather than a sample.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_15_the_rendered_dom_carries_no_probe_rate
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`
- Expected: COVERS AC-F12-15 (DOM leg) on the two surfaces that mention the programme at all — the only two where a rate could plausibly appear.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_15_there_is_no_rate_held_anywhere_for_a_timing_to_leak
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_15_there_is_no_rate_held_anywhere_for_a_timing_to_leak`
- Expected: COVERS AC-F12-15 (timings leg), by construction rather than by a stopwatch. The rate is drawn inside `plan_injection` and discarded; the pre-disposition render path does not consult the probe registry at all, so rendering a probe and rendering a genuine finding execute the same code. A wall-clock comparison over a synthetic fixture would be a test of the machine, not of the product.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_16_the_probe_appears_in_none_of_the_five_named_sets
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_16_the_probe_appears_in_none_of_the_five_named_sets`
- Expected: COVERS AC-F12-16 (first clause). All five sets the criterion names, read in one scenario because the criterion asks for them "each".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_16_the_retained_disposition_record_marks_it_unmistakably
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_16_the_retained_disposition_record_marks_it_unmistakably`
- Expected: COVERS AC-F12-16 (second clause). Excluding it from the accuracy set and dropping it from the record are different acts, and only the first is what the criterion asks for.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_17_two_otherwise_identical_items_produce_identical_runtime_context
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_17_two_otherwise_identical_items_produce_identical_runtime_context`
- Expected: COVERS AC-F12-17 (first clause). The emission context is what the agent runtime is judged on, and the two differ only in their identifiers.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_17_no_pre_disposition_payload_contains_the_flag
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_17_no_pre_disposition_payload_contains_the_flag`
- Expected: COVERS AC-F12-17 (second clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_18_a_reviewer_sees_their_own_probe_outcomes
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_18_a_reviewer_sees_their_own_probe_outcomes`
- Expected: COVERS AC-F12-18.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_18_the_boundary_against_AC_F12_13_holds_at_the_store
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_18_the_boundary_against_AC_F12_13_holds_at_the_store`
- Expected: COVERS AC-F12-18 (the boundary clause). Own history is a request for oneself; the same function asked for somebody else refuses with the same exception `AC-F12-13` raises, so there is no second door.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_no_probe_surface_asserts_anything_about_explanation_quality
- Status: EXECUTED
- Input: `tests/suites/functional/test_f12_probe_criteria.py::test_no_probe_surface_asserts_anything_about_explanation_quality`
- Expected: §12's standing exclusion, held against the newest control on the review surface. `INDUSTRY_KB` §15.4 rules out the legibility route and names probes as the alternative: probes measure ATTENTION. No scenario, statement or aggregate here claims anything about how well an item was explained.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_04_the_export_is_a_parseable_file_served_from_a_real_route
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_04_the_export_is_a_parseable_file_served_from_a_real_route`
- Expected: COVERS AC-F1-04.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_04_it_contains_every_dossier_for_the_period
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_04_it_contains_every_dossier_for_the_period`
- Expected: COVERS AC-F1-04 (completeness) and AC-F12-16 (the export path).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_16_no_probe_reaches_the_export_and_the_exclusion_is_stated
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F12_16_no_probe_reaches_the_export_and_the_exclusion_is_stated`
- Expected: COVERS AC-F12-16 (the export path leg) and AC-F1-04 (the honesty of the completeness claim).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_04_NO_FIELD_RENDERS_ONLY_AS_AN_IN_APPLICATION_REFERENCE
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_04_NO_FIELD_RENDERS_ONLY_AS_AN_IN_APPLICATION_REFERENCE`
- Expected: COVERS AC-F1-04 (the clause an export is most likely to fail).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_05_the_five_reconstruction_facts_are_named_fields
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_05_the_five_reconstruction_facts_are_named_fields`
- Expected: COVERS AC-F1-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_05_re_execution_is_explicitly_NOT_claimed
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_05_re_execution_is_explicitly_NOT_claimed`
- Expected: COVERS AC-F1-05 (the criterion's own bold sentence).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_06_a_period_with_no_proposals_produces_a_whole_export
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_06_a_period_with_no_proposals_produces_a_whole_export`
- Expected: COVERS AC-F1-06.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_06_it_STATES_that_the_period_contained_no_proposals
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_06_it_STATES_that_the_period_contained_no_proposals`
- Expected: COVERS AC-F1-06 (the explicit statement).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_07_a_failure_part_way_presents_no_file_and_names_the_point
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_07_a_failure_part_way_presents_no_file_and_names_the_point`
- Expected: COVERS AC-F1-07.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_07_the_route_returns_no_artefact_when_the_export_cannot_complete
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_07_the_route_returns_no_artefact_when_the_export_cannot_complete`
- Expected: COVERS AC-F1-07 (from the route).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_10_the_produced_export_carries_no_active_content_anywhere
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_10_the_produced_export_carries_no_active_content_anywhere`
- Expected: COVERS AC-F1-10.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_10_an_export_containing_one_is_NOT_PRODUCED
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_10_an_export_containing_one_is_NOT_PRODUCED`
- Expected: COVERS AC-F1-10 (the criterion's own wording).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_12_no_key_is_returned_to_anything_inside_the_application
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_12_no_key_is_returned_to_anything_inside_the_application`
- Expected: COVERS AC-F1-12 (no key is returned).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_12_no_valid_signature_is_produced_by_anything_in_the_application
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_12_no_valid_signature_is_produced_by_anything_in_the_application`
- Expected: COVERS AC-F1-12 (no valid signature).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_12_the_attempt_is_recorded_as_a_control_event
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_12_the_attempt_is_recorded_as_a_control_event`
- Expected: COVERS AC-F1-12 (the attempt is recorded).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[delete_attempt]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[delete_attempt]`
- Expected: COVERS AC-F1-13.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[retention_shortening_attempt]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[retention_shortening_attempt]`
- Expected: COVERS AC-F1-13.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[lock_configuration_change]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_each_act_is_retrievable_from_the_separate_destination[lock_configuration_change]`
- Expected: COVERS AC-F1-13.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_the_three_acts_are_the_three_the_criterion_names
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_the_three_acts_are_the_three_the_criterion_names`
- Expected: COVERS AC-F1-13 (the guard on the group above).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_the_record_survives_the_application_deleting_its_OWN_log
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_the_record_survives_the_application_deleting_its_OWN_log`
- Expected: COVERS AC-F1-13 (the second clause, and the whole point of ruling 1).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_the_application_has_no_method_that_could_remove_the_record
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_the_application_has_no_method_that_could_remove_the_record`
- Expected: COVERS AC-F1-13 (why the survival above is structural, not lucky).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_13_the_interval_is_a_stated_number_rather_than_an_implied_eventually
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_13_the_interval_is_a_stated_number_rather_than_an_implied_eventually`
- Expected: COVERS AC-F1-13 ("within the stated interval").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_14_a_failure_to_ship_is_surfaced_as_a_finding_naming_the_interval
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_14_a_failure_to_ship_is_surfaced_as_a_finding_naming_the_interval`
- Expected: COVERS AC-F1-14.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_14_it_is_NOT_reported_as_satisfactory
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_14_it_is_NOT_reported_as_satisfactory`
- Expected: COVERS AC-F1-14 ("not reported as clean").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F1_14_it_is_NOT_silently_dropped
- Status: EXECUTED
- Input: `tests/suites/functional/test_f1_evidence_criteria.py::test_AC_F1_14_it_is_NOT_silently_dropped`
- Expected: COVERS AC-F1-14 ("not silently dropped").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_01_the_run_lists_exactly_the_seeded_divergences_no_more_no_fewer
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_01_the_run_lists_exactly_the_seeded_divergences_no_more_no_fewer`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_02_each_divergence_carries_balance_segment_period_and_both_totals
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_02_each_divergence_carries_balance_segment_period_and_both_totals`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_03_a_tying_warehouse_states_zero_divergences_with_its_coverage
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_03_a_tying_warehouse_states_zero_divergences_with_its_coverage`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_04_the_missing_batch_names_its_expected_arrival_and_population
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_04_the_missing_batch_names_its_expected_arrival_and_population`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_05_staleness_is_expressed_relative_to_the_close_clock
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_05_staleness_is_expressed_relative_to_the_close_clock`
- Expected: COVERS AC-F26-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_05_the_statement_is_not_an_absolute_timestamp_alone
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_05_the_statement_is_not_an_absolute_timestamp_alone`
- Expected: COVERS AC-F26-05 (the criterion's explicit exclusion).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_05_a_ledger_with_no_declared_calendar_still_states_the_absence
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_05_a_ledger_with_no_declared_calendar_still_states_the_absence`
- Expected: COVERS AC-F26-05 (the boundary the criterion's Given presupposes).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_06_an_absent_control_extract_reports_not_run_with_no_coverage_figure
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_06_an_absent_control_extract_reports_not_run_with_no_coverage_figure`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_07_a_complete_f26_run_observes_zero_model_invocations
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_complete_f26_run_observes_zero_model_invocations`
- Expected: F26's OWN count, over an F26 run.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_07_a_model_call_from_inside_the_f26_run_would_have_been_refused
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_model_call_from_inside_the_f26_run_would_have_been_refused`
- Expected: Zero observed calls means nothing unless a call would be counted.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_08_a_divergence_of_one_smallest_currency_unit_is_reported_exactly
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_08_a_divergence_of_one_smallest_currency_unit_is_reported_exactly`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_09_the_first_and_last_in_scope_periods_are_both_reported
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_09_the_first_and_last_in_scope_periods_are_both_reported`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F26_10_the_fidelity_findings_are_visible_on_the_run_report
- Status: EXECUTED
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_run_report`
- Expected: Rendered from the application's real entry point, not from the region.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_01_the_a6_check_names_the_control_account_subledger_and_difference
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_01_the_a6_check_names_the_control_account_subledger_and_difference`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_02_the_a7_check_names_both_entities_the_pair_and_the_direction
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_02_the_a7_check_names_both_entities_the_pair_and_the_direction`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_03_the_a8_check_names_the_account_entity_two_periods_and_the_gap
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_03_the_a8_check_names_the_account_entity_two_periods_and_the_gap`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_04_the_a9_check_names_the_account_and_the_duplicated_amount
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_04_the_a9_check_names_the_account_and_the_duplicated_amount`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_05_the_a10_check_names_the_account_residual_and_threshold_in_force
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_05_the_a10_check_names_the_account_residual_and_threshold_in_force`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_06_all_five_checks_are_listed_individually_with_their_coverage
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_all_five_checks_are_listed_individually_with_their_coverage`
- Expected: "a check that produced no finding is still listed, not omitted".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_06_a_run_at_full_coverage_with_no_findings_says_so_for_each_check
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_a_run_at_full_coverage_with_no_findings_says_so_for_each_check`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report`
- Expected: The criterion, driven by a warehouse with one object genuinely absent.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_07_the_overall_conclusion_is_not_stated_as_an_all_clear
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_the_overall_conclusion_is_not_stated_as_an_all_clear`
- Expected: The harder half: FOUR checks find nothing and the fifth cannot run.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all`
- Expected: `[]` is the same object a check that found nothing produces.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_08_a_complete_f28_run_observes_zero_model_invocations
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_complete_f28_run_observes_zero_model_invocations`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_08_a_model_call_from_inside_a_boundary_check_would_be_refused
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_model_call_from_inside_a_boundary_check_would_be_refused`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_09_a_failing_a10_result_states_that_it_covers_the_balance_only
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_a_failing_a10_result_states_that_it_covers_the_balance_only`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_09_an_a10_result_that_found_nothing_states_it_too
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_found_nothing_states_it_too`
- Expected: "A result OF ANY KIND" — including the one where nothing was found.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_09_an_a10_result_that_could_not_run_states_it_too
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_could_not_run_states_it_too`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_10_the_five_checks_are_visible_on_the_run_report_with_their_states
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_five_checks_are_visible_on_the_run_report_with_their_states`
- Expected: Rendered from the application's real entry point.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F28_10_the_run_statement_on_screen_does_not_claim_an_all_clear
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_run_statement_on_screen_does_not_claim_an_all_clear`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_run_report_carrying_these_checks_is_reachable_from_the_entry_point
- Status: EXECUTED
- Input: `tests/suites/functional/test_f28_criteria.py::test_the_run_report_carrying_these_checks_is_reachable_from_the_entry_point`
- Expected: The move is only a move if the destination is walkable from `/`.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_an_unreversed_journal_is_reported_naming_all_three_facts
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_an_unreversed_journal_is_reported_naming_all_three_facts`
- Expected: COVERS AC-F29-02.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_the_reported_set_is_EXACTLY_the_planted_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_the_reported_set_is_EXACTLY_the_planted_one`
- Expected: COVERS AC-F29-02 (specificity).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_a_partially_reversed_journal_reports_the_RESIDUAL
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_a_partially_reversed_journal_reports_the_RESIDUAL`
- Expected: COVERS AC-F29-02 (the boundary).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_the_clean_world_reports_no_unreversed_journal
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_the_clean_world_reports_no_unreversed_journal`
- Expected: COVERS AC-F29-02 (the declared negative fixture).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_an_obligation_not_yet_due_is_reported_as_UNASSESSED
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_an_obligation_not_yet_due_is_reported_as_UNASSESSED`
- Expected: COVERS AC-F29-02 (the empty-ish case that is not a pass).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_02_the_same_obligation_is_unassessed_before_it_falls_due_and_a_finding_after
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_02_the_same_obligation_is_unassessed_before_it_falls_due_and_a_finding_after`
- Expected: COVERS AC-F29-02 (the boundary, both sides, on ONE obligation).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_03_a_stopped_feed_is_reported_naming_all_three_facts
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_03_a_stopped_feed_is_reported_naming_all_three_facts`
- Expected: COVERS AC-F29-03.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_03_a_feed_still_delivering_is_not_reported
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_03_a_feed_still_delivering_is_not_reported`
- Expected: COVERS AC-F29-03 (specificity). The fixture has a live feed beside the stopped one, and the run must tell them apart.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_03_the_clean_world_reports_no_stopped_feed_entry
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_03_the_clean_world_reports_no_stopped_feed_entry`
- Expected: COVERS AC-F29-03 (the declared negative fixture).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_03_this_is_a_different_finding_from_F26s_missing_batch
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_03_this_is_a_different_finding_from_F26s_missing_batch`
- Expected: COVERS AC-F29-03 (the distinction the criterion turns on).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_04_a_one_sided_posting_names_both_entities_and_which_side_is_missing
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_04_a_one_sided_posting_names_both_entities_and_which_side_is_missing`
- Expected: COVERS AC-F29-04.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_04_a_two_sided_posting_is_not_reported
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_04_a_two_sided_posting_is_not_reported`
- Expected: COVERS AC-F29-04 (specificity).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_04_the_clean_world_reports_no_one_sided_posting
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_04_the_clean_world_reports_no_one_sided_posting`
- Expected: COVERS AC-F29-04 (the declared negative fixture).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F29_04_this_is_not_F28s_pair_imbalance
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_AC_F29_04_this_is_not_F28s_pair_imbalance`
- Expected: COVERS AC-F29-04 (the distinction).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_three_sub_types_share_one_reviewed_statement
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_the_three_sub_types_share_one_reviewed_statement`
- Expected: COVERS AC-F29-02, AC-F29-03, AC-F29-04 (the configuration bound).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_no_manifest_or_population_in_this_family_names_the_table_it_reads
- Status: EXECUTED
- Input: `tests/suites/functional/test_f29_omission_subtypes.py::test_no_manifest_or_population_in_this_family_names_the_table_it_reads`
- Expected: COVERS AC-F29-02, -03, -04 (the seam).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[model]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[model]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[prompt]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[prompt]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[tool_config]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[tool_config]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[corpus]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[corpus]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[dataset]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[dataset]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[guardrail_bundle_hash]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_any_single_missing_element_denies_and_the_denial_names_it[guardrail_bundle_hash]`
- Expected: COVERS AC-F2-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_the_six_elements_are_the_ones_the_criterion_names
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_the_six_elements_are_the_ones_the_criterion_names`
- Expected: COVERS AC-F2-08 (the guard on the group above).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_an_approval_carrying_no_stamp_at_all_is_denied
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_an_approval_carrying_no_stamp_at_all_is_denied`
- Expected: COVERS AC-F2-08 (the "absent" end of "absent or unresolvable").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_an_unresolvable_element_is_denied_and_named
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_an_unresolvable_element_is_denied_and_named`
- Expected: COVERS AC-F2-08 ("absent OR UNRESOLVABLE").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_the_closure_returns_the_EMPTY_SET_rather_than_a_partial_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_the_closure_returns_the_EMPTY_SET_rather_than_a_partial_one`
- Expected: COVERS AC-F2-08 ("the closure never returns eligible on an incomplete input set").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_08_a_complete_stamp_still_approves_so_the_control_is_not_a_blanket_denial
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_08_a_complete_stamp_still_approves_so_the_control_is_not_a_blanket_denial`
- Expected: COVERS AC-F2-08 (the negative control).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_09_an_unresolvable_registry_denies_the_approval_naming_it
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_09_an_unresolvable_registry_denies_the_approval_naming_it`
- Expected: COVERS AC-F2-09.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_09_no_approval_completes_on_the_strength_of_an_unstamped_artefact
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_09_no_approval_completes_on_the_strength_of_an_unstamped_artefact`
- Expected: COVERS AC-F2-09 ("no approval completes").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_02_a_stamp_read_back_after_a_version_change_shows_what_was_in_force
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_02_a_stamp_read_back_after_a_version_change_shows_what_was_in_force`
- Expected: COVERS AC-F2-02.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_02_the_stamp_the_screen_shows_and_the_stamp_the_closure_uses_are_one_object
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_02_the_stamp_the_screen_shows_and_the_stamp_the_closure_uses_are_one_object`
- Expected: COVERS AC-F2-02 (the drift this criterion is really about).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_02_the_two_declarations_of_the_six_elements_have_not_drifted
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_02_the_two_declarations_of_the_six_elements_have_not_drifted`
- Expected: COVERS AC-F2-02 (the boundary's cost, paid visibly).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_03_a_change_record_is_retrievable_from_the_changelog_for_the_period
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_03_a_change_record_is_retrievable_from_the_changelog_for_the_period`
- Expected: COVERS AC-F2-03. Read from the screen a user reaches, not the module.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_04_a_run_naming_an_unregistered_artefact_does_not_start
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_04_a_run_naming_an_unregistered_artefact_does_not_start`
- Expected: COVERS AC-F2-04.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_04_a_registered_stamp_does_not_block_the_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_04_a_registered_stamp_does_not_block_the_run`
- Expected: COVERS AC-F2-04 (the negative control).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_05_a_deprecated_version_is_stated_with_its_date_and_travels_with_the_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_05_a_deprecated_version_is_stated_with_its_date_and_travels_with_the_run`
- Expected: COVERS AC-F2-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_05_a_current_version_carries_no_deprecation_notice
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_05_a_current_version_carries_no_deprecation_notice`
- Expected: COVERS AC-F2-05 (the negative control). A notice on everything is a notice on nothing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_06_a_period_with_no_changes_STATES_so_on_the_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_06_a_period_with_no_changes_STATES_so_on_the_screen`
- Expected: COVERS AC-F2-06 — the empty case, which IS the criterion.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F2_06_the_statement_is_present_on_the_audit_screen_a_user_reaches
- Status: EXECUTED
- Input: `tests/suites/functional/test_f2_version_criteria.py::test_AC_F2_06_the_statement_is_present_on_the_audit_screen_a_user_reaches`
- Expected: COVERS AC-F2-06 (observable).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence`
- Expected: `AC-F33-01` requires the finding to NAME its evidence. It fixes no number.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_02_a_natural_account_divergence_confirms_the_shared_caption
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_02_a_natural_account_divergence_confirms_the_shared_caption`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_03_an_intercompany_miscoding_is_surfaced_with_no_proposal
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_03_an_intercompany_miscoding_is_surfaced_with_no_proposal`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_04_a_caption_crossing_is_surfaced_with_no_proposal
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_04_a_caption_crossing_is_surfaced_with_no_proposal`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_05_a_cut_off_error_states_that_cut_off_is_not_proposed
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_05_a_cut_off_error_states_that_cut_off_is_not_proposed`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_three_out_of_scope_sub_types_produce_no_proposal_between_them
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_three_out_of_scope_sub_types_produce_no_proposal_between_them`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions`
- Expected: `AC-F33-06` requires the figures to be REPORTED with their held-out period, label count and both versions. That is what is checked.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_backtest_measures_a_detector_that_actually_ran
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_backtest_measures_a_detector_that_actually_ran`
- Expected: Predictions come from re-running the real detector over the held-out period, not from a stored prediction set — a backtest against recorded predictions is a backtest of the recording, and its figure cannot fall when the detector gets worse.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_07_the_recall_bias_label_is_a_required_field_of_the_schema
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_the_recall_bias_label_is_a_required_field_of_the_schema`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_07_a_record_without_the_label_is_invalid_and_the_run_fails
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_a_record_without_the_label_is_invalid_and_the_run_fails`
- Expected: "a record in which that field is absent, empty, or does not carry that meaning is invalid, and the run that produced it fails".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_on_the_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_on_the_screen`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_in_a_dossier
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_a_dossier`
- Expected: The dossier leg. The backtest record is written into the dossier payload as one object, so a dossier carrying a recall figure carries the label by construction rather than by the writer remembering it.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_in_an_export
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_an_export`
- Expected: The export leg. A file is produced and read back, so "it would be in the export" is not the claim being made.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_08_no_surface_can_show_recall_without_the_label
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_no_surface_can_show_recall_without_the_label`
- Expected: The structural guarantee behind all three surfaces: the field cannot be absent from a valid record, so a surface reading the record cannot find a recall figure that has no label beside it.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_09_a_held_out_period_with_no_labels_emits_no_figures
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_a_held_out_period_with_no_labels_emits_no_figures`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_09_the_no_labels_state_is_visible_on_the_run_report
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_the_no_labels_state_is_visible_on_the_run_report`
- Expected: It is on the pilot screen deliberately: this is the result a reader is most likely to mistake for a good one.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_10_a_single_label_produces_figures_carrying_a_label_count_of_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_10_a_single_label_produces_figures_carrying_a_label_count_of_one`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_11_an_unretrievable_label_set_emits_no_accuracy_claim
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_11_an_unretrievable_label_set_emits_no_accuracy_claim`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_could_not_retrieve_is_distinguishable_from_a_period_with_no_labels
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_could_not_retrieve_is_distinguishable_from_a_period_with_no_labels`
- Expected: `AC-F33-09` and `AC-F33-11` are different criteria because they are different facts about a close, and a controller decides differently.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_12_the_coding_findings_are_visible_with_current_proposed_and_sub_type
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_coding_findings_are_visible_with_current_proposed_and_sub_type`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_12_an_out_of_scope_row_renders_no_proposed_coding
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_an_out_of_scope_row_renders_no_proposed_coding`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F33_12_the_backtest_figures_are_on_the_same_screen_as_the_findings
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_backtest_figures_are_on_the_same_screen_as_the_findings`
- Expected: "...for the model version that produced the findings". Both come out of one `CodingResult`, so a screen showing this period's findings beside another model's accuracy is not constructible here.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_run_report_carrying_the_coding_region_is_reachable
- Status: EXECUTED
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_run_report_carrying_the_coding_region_is_reachable`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_check_runs_before_resolution_unconditionally[Is this difference material?-A20]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_refusal_check_runs_before_resolution_unconditionally[Is this difference material?-A20]`
- Expected: The first of the two hard conditions the resolver was approved under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_check_runs_before_resolution_unconditionally[Is the suspense residual immaterial?-A20]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_refusal_check_runs_before_resolution_unconditionally[Is the suspense residual immaterial?-A20]`
- Expected: The first of the two hard conditions the resolver was approved under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_check_runs_before_resolution_unconditionally[Assess the impairment on this CGU.-A19]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_refusal_check_runs_before_resolution_unconditionally[Assess the impairment on this CGU.-A19]`
- Expected: The first of the two hard conditions the resolver was approved under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_check_runs_before_resolution_unconditionally[Certify that the close is complete.-A21]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_refusal_check_runs_before_resolution_unconditionally[Certify that the close is complete.-A21]`
- Expected: The first of the two hard conditions the resolver was approved under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_refusal_check_runs_before_resolution_unconditionally[Should this suspense balance be capitalised under ASC 360?-A22]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_refusal_check_runs_before_resolution_unconditionally[Should this suspense balance be capitalised under ASC 360?-A22]`
- Expected: The first of the two hard conditions the resolver was approved under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_a_deferred_capability_still_defers_rather_than_resolving
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_a_deferred_capability_still_defers_rather_than_resolving`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_route_resolves_only_what_triage_passed
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_route_resolves_only_what_triage_passed`
- Expected: Asserted on the module contract rather than only on behaviour: triage's third outcome is the ONLY one that reaches the resolver, and the resolver holds no refusal check of its own — a second copy would be a second thing to get wrong, and the one that mattered would eventually be the copy.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_03_an_unmappable_request_names_the_missing_dataset
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_03_an_unmappable_request_names_the_missing_dataset`
- Expected: COVERS AC-F39-03. The criterion asks for the metric, join or dataset by NAME; "we cannot answer that" is not a name.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_03_an_unmappable_request_names_a_missing_metric_or_join
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_03_an_unmappable_request_names_a_missing_metric_or_join`
- Expected: COVERS AC-F39-03. Three kinds are nameable and all three are reachable — a build that only ever named a missing dataset would satisfy the criterion for one third of its own wording.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_03_no_approximate_or_best_effort_answer_is_produced
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_03_no_approximate_or_best_effort_answer_is_produced`
- Expected: COVERS AC-F39-03's second clause, and A25's failure mode: the helpful assistant that has just been denied and reaches for the next best thing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_03_is_not_vacuous_because_other_requests_do_resolve
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_03_is_not_vacuous_because_other_requests_do_resolve`
- Expected: THE SCENARIO THAT STOPS THIS FILE BEING WHAT IT REPLACED. `AC-F39-03` was passing because every request was unmappable. It only means anything while some request is mappable, so that is asserted here, next to it.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_05_zero_rows_states_zero_rows_the_population_and_the_coverage
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_05_zero_rows_states_zero_rows_the_population_and_the_coverage`
- Expected: COVERS AC-F39-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_05_it_does_not_render_blank
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_05_it_does_not_render_blank`
- Expected: COVERS AC-F39-05 (the "does not render blank" clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_05_it_does_not_assert_the_population_is_free_of_exceptions
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_05_it_does_not_assert_the_population_is_free_of_exceptions`
- Expected: COVERS AC-F39-05 (the clause that matters). Zero rows returned and zero exceptions present are different facts, and the second is not available from a query that returned nothing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_05_a_population_without_a_member_resolver_says_coverage_is_unknown
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_05_a_population_without_a_member_resolver_says_coverage_is_unknown`
- Expected: Convention C2 in its coverage form: unknown coverage rendered as complete coverage is the most dangerous rounding in the product.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_06_an_unreachable_warehouse_produces_a_named_failure
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_06_an_unreachable_warehouse_produces_a_named_failure`
- Expected: COVERS AC-F39-06. Built by giving GES a warehouse factory that cannot produce one, which is the state the criterion is about.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_06_the_failure_is_not_reported_as_zero_rows
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_06_the_failure_is_not_reported_as_zero_rows`
- Expected: COVERS AC-F39-06 (the clause a build fails silently). "The source did not answer" and "the source answered nothing" are opposite facts, and collapsing them is convention C2's exact prohibition.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[Show the suspense residuals for December 2024.]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[Show the suspense residuals for December 2024.]`
- Expected: COVERS AC-F39-08. The refusal states the range the certified dataset actually covers — a refusal that does not say what IS covered trains its user to guess.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[What recurring accruals ran in FY2023?]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[What recurring accruals ran in FY2023?]`
- Expected: COVERS AC-F39-08. The refusal states the range the certified dataset actually covers — a refusal that does not say what IS covered trains its user to guess.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[Show me the movements for period 14.]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_08_a_period_outside_the_certified_range_is_refused_by_name[Show me the movements for period 14.]`
- Expected: COVERS AC-F39-08. The refusal states the range the certified dataset actually covers — a refusal that does not say what IS covered trains its user to guess.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_08_a_period_inside_the_range_is_not_refused
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_08_a_period_inside_the_range_is_not_refused`
- Expected: The other half. A range check that refused everything would pass the scenario above and be a different defect.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_08_the_declared_range_agrees_with_what_the_warehouse_holds
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_08_the_declared_range_agrees_with_what_the_warehouse_holds`
- Expected: The refusal is only correct if the declared range is. A declared range that has drifted from the data refuses periods the product can in fact answer, which is a control failing in the direction nobody notices.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_01_the_resolved_query_and_its_bound_values_travel_with_the_answer
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_01_the_resolved_query_and_its_bound_values_travel_with_the_answer`
- Expected: COVERS AC-F39-01 (the resolution is displayed). Now asserted against a real resolution rather than against a screen literal.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_the_answer_states_its_metric_and_join_versions
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_04_the_answer_states_its_metric_and_join_versions`
- Expected: COVERS AC-F39-04 on the resolving path. The versions travel out of the same call as the rows, so a consumer cannot obtain an answer without also obtaining what it was computed from.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_02_no_request_can_cause_a_statement_to_be_executed
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_02_no_request_can_cause_a_statement_to_be_executed`
- Expected: COVERS AC-F39-02. The engineered SQL string is not filtered — it is unroutable, because the resolver's only output is a `query_id` from a closed enum and there is no operation a statement could be addressed to.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_07_two_equally_good_candidates_are_named_and_nothing_is_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_AC_F39_07_two_equally_good_candidates_are_named_and_nothing_is_run`
- Expected: COVERS AC-F39-07 on the resolving path. Silently picking the first is the behaviour the criterion forbids, and it is the cheapest thing for a resolver to do.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_resolver_is_a_matcher_over_english_and_a_request_outside_it_declines
- Status: EXECUTED
- Input: `tests/suites/functional/test_f39_resolver_criteria.py::test_the_resolver_is_a_matcher_over_english_and_a_request_outside_it_declines`
- Expected: THE SUBSTITUTION, ASSERTED AS ITSELF. Intent selection is pattern matching against a committed table, not a model. A request phrased outside that vocabulary is unmappable — and that is the safe direction: the failure mode is "we did not answer", never "we answered approximately".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_06_the_export_states_all_three_clauses_with_the_date
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_06_the_export_states_all_three_clauses_with_the_date`
- Expected: COVERS AC-F40-06 (the export leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_06_the_produced_file_carries_the_same_statement
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_06_the_produced_file_carries_the_same_statement`
- Expected: COVERS AC-F40-06 (the export leg, on the artefact).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_06_a_file_built_with_no_verification_says_so_rather_than_nothing
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_06_a_file_built_with_no_verification_says_so_rather_than_nothing`
- Expected: COVERS AC-F40-06 (the boundary).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_06_the_dossier_states_the_same_three_clauses
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_06_the_dossier_states_the_same_three_clauses`
- Expected: COVERS AC-F40-06 (the dossier leg), reached by following links from `/`.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_09_a_generation_failure_leaves_the_approval_valid_and_recorded
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_09_a_generation_failure_leaves_the_approval_valid_and_recorded`
- Expected: COVERS AC-F40-09.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_09_the_broker_decision_record_is_unchanged_by_the_failure
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_09_the_broker_decision_record_is_unchanged_by_the_failure`
- Expected: COVERS AC-F40-09 (the "recorded" half).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_09_the_failure_is_recorded_as_a_control_event
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_09_the_failure_is_recorded_as_a_control_event`
- Expected: COVERS AC-F40-09 (the failure is shown, and countable).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_the_original_dossier_carries_a_linkage_to_the_reversal
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_the_original_dossier_carries_a_linkage_to_the_reversal`
- Expected: COVERS AC-F40-10 (the first clause), through the real evidence store.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_the_reversal_exists_as_its_own_record
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_the_reversal_exists_as_its_own_record`
- Expected: COVERS AC-F40-10 (the second clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_a_reversal_that_names_no_reason_is_refused
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_a_reversal_that_names_no_reason_is_refused`
- Expected: COVERS AC-F40-10 (the record is worth having).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_an_unrecognised_reversal_origin_is_refused
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_an_unrecognised_reversal_origin_is_refused`
- Expected: COVERS AC-F40-10 (whose reversal it was).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_the_linkage_is_visible_on_the_dossier_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_the_linkage_is_visible_on_the_dossier_screen`
- Expected: COVERS AC-F40-10 (observable).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_10_the_reversed_dossier_is_reachable_by_following_links
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_10_the_reversed_dossier_is_reachable_by_following_links`
- Expected: COVERS AC-F40-10 (observable: reached, not fetched by URL).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_18_a_probe_that_cannot_execute_refuses_the_export
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_18_a_probe_that_cannot_execute_refuses_the_export`
- Expected: COVERS AC-F40-18 (the refusal, and what it names).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_18_the_stored_verification_does_not_permit_the_export
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_18_the_stored_verification_does_not_permit_the_export`
- Expected: COVERS AC-F40-18 (the forbidden fallback).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_18_an_export_authorised_on_an_attestation_says_so_on_its_face
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_18_an_export_authorised_on_an_attestation_says_so_on_its_face`
- Expected: COVERS AC-F40-18 (the disclosure the pilot's operability is paid for with). Reached by driving the real controls on the suite's own app.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_12_a_moved_balance_refuses_the_export_and_invalidates_the_approval
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_12_a_moved_balance_refuses_the_export_and_invalidates_the_approval`
- Expected: COVERS AC-F40-12 (the balance leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_12_a_journal_newer_than_the_pinned_watermark_refuses
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_12_a_journal_newer_than_the_pinned_watermark_refuses`
- Expected: COVERS AC-F40-12 (the watermark leg, and the supersession).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_13_a_period_that_is_not_open_refuses_naming_it
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_13_a_period_that_is_not_open_refuses_naming_it`
- Expected: COVERS AC-F40-13.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_14_a_revalidation_that_cannot_run_refuses_and_produces_no_file
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_14_a_revalidation_that_cannot_run_refuses_and_produces_no_file`
- Expected: COVERS AC-F40-14.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_15_a_revalidation_that_agrees_still_leaves_a_record
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_15_a_revalidation_that_agrees_still_leaves_a_record`
- Expected: COVERS AC-F40-15.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`
- Expected: COVERS AC-F40-16.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F40_16_a_file_that_cannot_be_registered_is_not_released
- Status: EXECUTED
- Input: `tests/suites/functional/test_f40_criteria.py::test_AC_F40_16_a_file_that_cannot_be_registered_is_not_released`
- Expected: COVERS AC-F40-16 (the second clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_16_the_items_beyond_the_cap_are_not_routed
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_16_the_items_beyond_the_cap_are_not_routed`
- Expected: COVERS AC-F41-16.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_16_the_run_states_the_budget_was_reached_for_whom_and_how_many_held
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_16_the_run_states_the_budget_was_reached_for_whom_and_how_many_held`
- Expected: COVERS AC-F41-16 (all three clauses of the statement).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_16_the_held_items_are_returned_rather_than_dropped
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_16_the_held_items_are_returned_rather_than_dropped`
- Expected: COVERS AC-F41-16 (the thing the criterion does NOT say, and must not).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_16_the_cap_is_applied_to_a_DIRECT_api_caller_too
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_16_the_cap_is_applied_to_a_DIRECT_api_caller_too`
- Expected: COVERS AC-F41-16 (obligation M).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_controller_raise_records_identity_decision_id_caps_and_night
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_controller_raise_records_identity_decision_id_caps_and_night`
- Expected: COVERS AC-F41-17. All five fields the criterion names.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_the_decision_id_is_a_real_broker_decision_not_a_minted_string
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_the_decision_id_is_a_real_broker_decision_not_a_minted_string`
- Expected: COVERS AC-F41-17 (the decision id).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[human.platform.admin]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[human.platform.admin]`
- Expected: COVERS AC-F41-17 ("at any permission level including administrator").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.a.reyes]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.a.reyes]`
- Expected: COVERS AC-F41-17 ("at any permission level including administrator").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.j.mbeki]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.j.mbeki]`
- Expected: COVERS AC-F41-17 ("at any permission level including administrator").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.s.haddad]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[user.s.haddad]`
- Expected: COVERS AC-F41-17 ("at any permission level including administrator").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[agent.omission_detector@1]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_non_controller_raise_is_rejected_and_the_cap_holds[agent.omission_detector@1]`
- Expected: COVERS AC-F41-17 ("at any permission level including administrator").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_the_rejected_principals_are_every_non_holder_this_build_has
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_the_rejected_principals_are_every_non_holder_this_build_has`
- Expected: COVERS AC-F41-17 (the guard).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_a_raised_cap_changes_what_routes
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_a_raised_cap_changes_what_routes`
- Expected: COVERS AC-F41-17 (the raise does something).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_17_the_raise_applies_to_that_night_only
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_17_the_raise_applies_to_that_night_only`
- Expected: COVERS AC-F41-17 ("the night it applies to").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_18_at_and_below_the_cap_everything_routes_with_no_budget_event[3]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_18_at_and_below_the_cap_everything_routes_with_no_budget_event[3]`
- Expected: COVERS AC-F41-18 (N−1 and N).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_18_at_and_below_the_cap_everything_routes_with_no_budget_event[4]
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_18_at_and_below_the_cap_everything_routes_with_no_budget_event[4]`
- Expected: COVERS AC-F41-18 (N−1 and N).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_18_only_N_plus_1_records_a_budget_event_and_holds_an_item
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_18_only_N_plus_1_records_a_budget_event_and_holds_an_item`
- Expected: COVERS AC-F41-18 (N+1, the third count).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_18_the_three_counts_are_N_minus_1_N_and_N_plus_1_of_the_same_cap
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_18_the_three_counts_are_N_minus_1_N_and_N_plus_1_of_the_same_cap`
- Expected: COVERS AC-F41-18 (the guard on the group above).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_18_no_budget_control_event_is_emitted_under_cap
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_18_no_budget_control_event_is_emitted_under_cap`
- Expected: COVERS AC-F41-18 ("no budget event recorded").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_19_the_screen_shows_the_cap_the_broker_applied
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_routing_budget.py::test_AC_F41_19_the_screen_shows_the_cap_the_broker_applied`
- Expected: COVERS AC-F41-19.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_14_an_approval_on_a_run_whose_bound_dataset_moved_is_denied
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_14_an_approval_on_a_run_whose_bound_dataset_moved_is_denied`
- Expected: COVERS AC-F41-14's blocking clause.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_14_the_block_names_the_dataset_and_the_newer_as_of
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_14_the_block_names_the_dataset_and_the_newer_as_of`
- Expected: COVERS AC-F41-14's naming clause.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_14_the_block_is_the_same_loud_treatment_as_AC_F41_12_not_a_warning
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_14_the_block_is_the_same_loud_treatment_as_AC_F41_12_not_a_warning`
- Expected: COVERS AC-F41-14's *"not a dismissible warning"* clause.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_14_only_the_dataset_that_moved_is_named_not_every_bound_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_14_only_the_dataset_that_moved_is_named_not_every_bound_one`
- Expected: COVERS AC-F41-14's naming clause, negative side. This run bound two datasets; one moved. A block that named both would be telling a reviewer to re-check something that has not changed.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_14_a_caller_cannot_unblock_itself_by_sending_the_context_fields
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_14_a_caller_cannot_unblock_itself_by_sending_the_context_fields`
- Expected: COVERS AC-F41-14's blocking clause against the DIRECT API path.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_15_a_newer_watermark_on_an_unbound_dataset_does_not_block
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_15_a_newer_watermark_on_an_unbound_dataset_does_not_block`
- Expected: COVERS AC-F41-15's not-blocked clause.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_15_and_no_supersession_notice_is_shown
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_15_and_no_supersession_notice_is_shown`
- Expected: COVERS AC-F41-15's no-notice clause.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_15_a_build_that_blocked_on_ANY_watermark_movement_would_fail_here
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_15_a_build_that_blocked_on_ANY_watermark_movement_would_fail_here`
- Expected: COVERS AC-F41-15's stated failure mode, made executable.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_15_another_runs_binding_moving_does_not_block_this_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_15_another_runs_binding_moving_does_not_block_this_run`
- Expected: COVERS AC-F41-15's not-blocked clause, from the direction that would catch a run-blind implementation: a SECOND run binds the SAME dataset at a LATER watermark. That run is superseded when the warehouse moves past it; this one is judged on its own binding.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F41_15_a_run_that_bound_the_CURRENT_watermark_is_not_blocked
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_AC_F41_15_a_run_that_bound_the_CURRENT_watermark_is_not_blocked`
- Expected: COVERS AC-F41-15's not-blocked clause at the equality boundary — the common case, not an edge one, because a run that has just finished bound the watermark the worker is about to observe. `<` instead of `<=` here would block every approval the moment its own run's watermark arrived.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_control_is_at_the_broker_and_the_screen_is_only_display
- Status: EXECUTED
- Input: `tests/suites/functional/test_f41_supersession_by_data.py::test_the_control_is_at_the_broker_and_the_screen_is_only_display`
- Expected: Not a criterion — the constraint both criteria are enforced under.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_02_the_outlying_journal_is_named_with_the_attributes_that_made_it_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_02_the_outlying_journal_is_named_with_the_attributes_that_made_it_one`
- Expected: COVERS AC-F42-02.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_02_the_finding_carries_the_evidence_for_each_attribute
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_02_the_finding_carries_the_evidence_for_each_attribute`
- Expected: COVERS AC-F42-02 (the naming is checkable, not assertive).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_02_the_detector_is_silent_on_the_negative_fixture
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_02_the_detector_is_silent_on_the_negative_fixture`
- Expected: COVERS AC-F42-02 (specificity).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_02_the_two_F42_legs_report_different_things_about_the_same_period
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_02_the_two_F42_legs_report_different_things_about_the_same_period`
- Expected: COVERS AC-F42-02 (why it is a second detector).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_02_the_two_legs_run_over_different_declared_populations
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_02_the_two_legs_run_over_different_declared_populations`
- Expected: COVERS AC-F42-02 (the coverage statement stays meaningful).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_03_an_unresolvable_declared_population_stops_the_F42_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_03_an_unresolvable_declared_population_stops_the_F42_run`
- Expected: COVERS AC-F42-03 (the missing-population leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_03_an_uncertified_dataset_in_the_selection_stops_the_F42_run
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_03_an_uncertified_dataset_in_the_selection_stops_the_F42_run`
- Expected: COVERS AC-F42-03 (the uncertified-dataset leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_03_the_refusal_holds_for_a_direct_call_and_not_only_a_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_03_the_refusal_holds_for_a_direct_call_and_not_only_a_screen`
- Expected: COVERS AC-F42-03 (obligation M).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_05_a_clean_full_coverage_F42_run_states_both_halves
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_05_a_clean_full_coverage_F42_run_states_both_halves`
- Expected: COVERS AC-F42-05.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_05_the_same_statement_is_in_the_dossier
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_05_the_same_statement_is_in_the_dossier`
- Expected: COVERS AC-F42-05 (the record, not only the screen).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_05_a_bounded_run_makes_no_such_statement
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_05_a_bounded_run_makes_no_such_statement`
- Expected: COVERS AC-F42-05 (the contrast that gives it force).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F42_05_the_clean_full_coverage_world_is_a_declared_fixture
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_AC_F42_05_the_clean_full_coverage_world_is_a_declared_fixture`
- Expected: COVERS AC-F42-05 (the fixture is named, not improvised).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_thirteenth_primitive_is_declared_outside_the_KB_s_eleven
- Status: EXECUTED
- Input: `tests/suites/functional/test_f42_criteria.py::test_the_thirteenth_primitive_is_declared_outside_the_KB_s_eleven`
- Expected: COVERS AC-F42-02 (the disclosure that goes with it).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_01_the_numeric_leg_escalates_before_period_twelve_and_records_when
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_01_the_numeric_leg_escalates_before_period_twelve_and_records_when`
- Expected: Twelve sub-threshold same-direction movements aggregating to a material amount. The escalation must come BEFORE period twelve — a control that only fires once the year is over has not prevented anything — and the period at which it fired is a headline result on the record.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_02_the_iron_curtain_aggregate_is_the_primary_figure
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_iron_curtain_aggregate_is_the_primary_figure`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_02_the_single_period_delta_is_not_the_headline
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_single_period_delta_is_not_the_headline`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_03_the_narrative_leg_escalates_alone_with_the_numeric_leg_silent
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_leg_escalates_alone_with_the_numeric_leg_silent`
- Expected: The criterion's hardest clause: "in which the numeric leg has NOT tripped". The fixture's 13800 movements alternate in direction, so that is true by construction rather than by tuning a threshold.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_03_the_narrative_escalation_names_the_periods_and_quotes_the_assertion
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_escalation_names_the_periods_and_quotes_the_assertion`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_04_every_escalation_raises_the_risk_grade_and_revokes_auto_pass
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_every_escalation_raises_the_risk_grade_and_revokes_auto_pass`
- Expected: "an R6 control-state change readable on the account, rather than only a notification being emitted".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_04_the_change_is_recorded_with_its_cause_and_its_prior_value
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_the_change_is_recorded_with_its_cause_and_its_prior_value`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_04_holds_for_the_narrative_leg_as_well_as_the_numeric_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_holds_for_the_narrative_leg_as_well_as_the_numeric_one`
- Expected: The leg most likely to be treated as advisory. It is not.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_05_an_account_with_too_little_history_is_named_not_shown_as_monitored
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_an_account_with_too_little_history_is_named_not_shown_as_monitored`
- Expected: The criterion's state: named, with the periods available, and NOT shown as monitored-and-clear.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_05_the_unassessed_account_is_excluded_from_coverage
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_unassessed_account_is_excluded_from_coverage`
- Expected: Structural, not cosmetic: the run's conclusion is bounded and names it.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_05_the_state_is_visible_on_the_monitors_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_state_is_visible_on_the_monitors_screen`
- Expected: The state reaches a reader, from the real route.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_06_one_fixture_escalates_and_the_other_stops_one_period_short
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_one_fixture_escalates_and_the_other_stops_one_period_short`
- Expected: "two fixtures identical except that one reaches the configured consecutive-period count and the other stops one period short".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_06_the_record_that_did_not_escalate_states_how_many_periods_would
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_the_record_that_did_not_escalate_states_how_many_periods_would`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_07_alternating_sub_threshold_movements_raise_no_escalation
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_07_alternating_sub_threshold_movements_raise_no_escalation`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_08_the_monitors_screen_lists_escalations_with_account_aggregate_period_leg
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_monitors_screen_lists_escalations_with_account_aggregate_period_leg`
- Expected: Rendered from the application's real entry point.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_08_the_control_state_change_is_readable_on_the_row
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_control_state_change_is_readable_on_the_row`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_monitors_screen_is_reachable_from_the_entry_point
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_the_monitors_screen_is_reachable_from_the_entry_point`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_09_periods_with_no_recorded_explanation_are_named_not_evaluable
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_periods_with_no_recorded_explanation_are_named_not_evaluable`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_09_the_sequence_is_not_reported_as_having_been_checked
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_sequence_is_not_reported_as_having_been_checked`
- Expected: The structural half. The member is excluded from the narrative leg's evaluable set, so the run's conclusion is bounded and names it — rather than the account simply being absent from a findings list, which reads as "we looked and found nothing".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F9_09_the_named_periods_are_visible_on_the_monitors_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_named_periods_are_visible_on_the_monitors_screen`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_both_legs_run_over_the_same_declared_population
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_both_legs_run_over_the_same_declared_population`
- Expected: `DOMAIN_KB` §7.2.4 makes them peers. Two legs over two populations would let one silently cover fewer accounts than the other.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_a_numeric_leg_that_could_not_run_does_not_suppress_the_narrative_one
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_a_numeric_leg_that_could_not_run_does_not_suppress_the_narrative_one`
- Expected: An implementation in which the narrative leg only runs when the numeric one succeeded has quietly made it a detail of leg (i) again — which is exactly the outcome `DOMAIN_KB` §9 predicts and §7.2.4 forbids.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_narrative_leg_uses_a_query_that_cannot_reach_a_model
- Status: EXECUTED
- Input: `tests/suites/functional/test_f9_criteria.py::test_the_narrative_leg_uses_a_query_that_cannot_reach_a_model`
- Expected: Held by the REGISTRY, not by a convention in the primitive.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_the_answer_states_every_metric_it_was_computed_from
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_the_answer_states_every_metric_it_was_computed_from`
- Expected: COVERS AC-F39-04 (the displayed-answer leg).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_every_element_carries_its_version_and_not_only_its_name
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_every_element_carries_its_version_and_not_only_its_name`
- Expected: COVERS AC-F39-04 (the "version of each" clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_the_versions_come_from_the_registry_and_not_from_the_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_the_versions_come_from_the_registry_and_not_from_the_screen`
- Expected: COVERS AC-F39-04 (the source).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_the_dossier_screen_states_the_same_versions_as_the_answer
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_the_dossier_screen_states_the_same_versions_as_the_answer`
- Expected: COVERS AC-F39-04 (the dossier leg, on screen).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_a_written_dossier_cannot_omit_the_versions
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_a_written_dossier_cannot_omit_the_versions`
- Expected: COVERS AC-F39-04 (the dossier leg, in the record).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_a_real_run_stamps_the_versions_it_actually_used
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_a_real_run_stamps_the_versions_it_actually_used`
- Expected: COVERS AC-F39-04 (end to end, through the run harness).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F39_04_the_union_reports_one_metric_used_by_two_queries_once
- Status: EXECUTED
- Input: `tests/suites/functional/test_semantic_versions_criteria.py::test_AC_F39_04_the_union_reports_one_metric_used_by_two_queries_once`
- Expected: COVERS AC-F39-04 (the shape of "each").
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F35_03_an_R5_handoff_without_both_an_owner_and_a_due_date_does_not_close
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F35_03_an_R5_handoff_without_both_an_owner_and_a_due_date_does_not_close`
- Expected: COVERS AC-F35-03.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_04_a_capture_records_the_override_its_reason_code_and_the_decision_id
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_04_a_capture_records_the_override_its_reason_code_and_the_decision_id`
- Expected: COVERS AC-F12-04. All three fields, read back from the store.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_06_a_period_with_no_closes_STATES_zero_for_the_NAMED_period
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_06_a_period_with_no_closes_STATES_zero_for_the_NAMED_period`
- Expected: COVERS AC-F12-06 — the empty case, which IS the criterion.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_06_the_zero_flag_is_derived_and_cannot_disagree_with_the_count
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_06_the_zero_flag_is_derived_and_cannot_disagree_with_the_count`
- Expected: COVERS AC-F12-06 (the shape).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_19_a_warrant_label_is_attached_to_the_abstention_and_its_disposition
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_19_a_warrant_label_is_attached_to_the_abstention_and_its_disposition`
- Expected: COVERS AC-F12-19.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_19_the_label_set_is_counts_and_never_a_rate
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_19_the_label_set_is_counts_and_never_a_rate`
- Expected: COVERS AC-F12-19 (the shape the KB requires).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F12_19_not_yet_assessed_is_a_state_rather_than_a_default_to_unwarranted
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F12_19_not_yet_assessed_is_a_state_rather_than_a_default_to_unwarranted`
- Expected: COVERS AC-F12-19 (the boundary).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F32_05_a_clearing_period_at_or_before_the_current_one_does_not_save
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F32_05_a_clearing_period_at_or_before_the_current_one_does_not_save`
- Expected: COVERS AC-F32-05. P and P−1, not just P.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F32_06_the_earliest_permitted_period_and_the_maximum_horizon_both_save
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F32_06_the_earliest_permitted_period_and_the_maximum_horizon_both_save`
- Expected: COVERS AC-F32-06. P+1 and the horizon: the two ends of the permitted range, which is what the criterion asks for by name.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F32_06_beyond_the_maximum_horizon_does_not_save_and_STATES_the_maximum
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F32_06_beyond_the_maximum_horizon_does_not_save_and_STATES_the_maximum`
- Expected: COVERS AC-F32-06 (the far boundary, and the message).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F32_07_a_period_with_no_predictions_due_RECORDS_zero_rather_than_nothing
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F32_07_a_period_with_no_predictions_due_RECORDS_zero_rather_than_nothing`
- Expected: COVERS AC-F32-07 — an empty case, and the record is the criterion.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F32_08_a_period_not_yet_closed_records_a_DEFERRAL_and_no_verdict
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F32_08_a_period_not_yet_closed_records_a_DEFERRAL_and_no_verdict`
- Expected: COVERS AC-F32-08.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_01_two_agents_actions_are_separable_without_inference
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_01_two_agents_actions_are_separable_without_inference`
- Expected: COVERS AC-F5-01.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_inventory_needs_no_manual_registration_step
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_the_inventory_needs_no_manual_registration_step`
- Expected: COVERS ONLY THE REGISTRATION CLAUSE OF AC-F5-02. It does NOT claim `AC-F5-02`, which this build does not meet — see the two scenarios below.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory`
- Expected: `AC-F5-02` IS RECORDED UNMET — register entry 34. Claimed by nothing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`
- Expected: The claim of a criterion this build records UNMET is on no surface.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_broker_answers_the_population_question_UNKNOWN_and_not_none
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_the_broker_answers_the_population_question_UNKNOWN_and_not_none`
- Expected: NOT a claim on `AC-F5-02`. Register 33's convention C2, applied to the field register 34 credits as "the broker's own answer to the population question".
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_the_unregistered_actor_answer_is_not_computable_WHILE_findings_stay_off_the_ledger
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_the_unregistered_actor_answer_is_not_computable_WHILE_findings_stay_off_the_ledger`
- Expected: The join between the claim and its reason, so neither can move alone.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`
- Expected: `AC-F5-03` and `AC-F5-05` ARE RECORDED UNMET — register entry 34.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_06_a_retired_agent_is_still_listed_with_its_date_and_its_lineage_resolves
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_06_a_retired_agent_is_still_listed_with_its_date_and_its_lineage_resolves`
- Expected: COVERS AC-F5-06.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_06_retirement_removes_the_capability_and_not_only_the_label
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_06_retirement_removes_the_capability_and_not_only_the_label`
- Expected: COVERS AC-F5-06 (the half a display could fake).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_F5_06_the_retired_agent_is_visible_on_the_Inventory_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_F5_06_the_retired_agent_is_visible_on_the_Inventory_screen`
- Expected: COVERS AC-F5-06 (observable).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_13_A23_A24_and_A25_are_each_visible_by_name_on_the_Refusals_screen
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_13_A23_A24_and_A25_are_each_visible_by_name_on_the_Refusals_screen`
- Expected: COVERS AC-REFUSAL-13.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_13_each_carries_a_reason_and_the_by_design_wording
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_13_each_carries_a_reason_and_the_by_design_wording`
- Expected: COVERS AC-REFUSAL-13 (the second and third clauses).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_13_the_refusals_screen_is_reachable_from_the_entry_point
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_13_the_refusals_screen_is_reachable_from_the_entry_point`
- Expected: COVERS AC-REFUSAL-13 (observable-UI: reached, not fetched by URL).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_07_each_of_the_three_is_refused_by_design_and_recorded
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_07_each_of_the_three_is_refused_by_design_and_recorded`
- Expected: COVERS AC-REFUSAL-07.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders

### Scenario: test_AC_REFUSAL_07_the_refusals_are_registered_and_therefore_recordable
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py::test_AC_REFUSAL_07_the_refusals_are_registered_and_therefore_recordable`
- Expected: COVERS AC-REFUSAL-07 (the control-event clause).
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh functional` exit 0; same node id green in all six collection orders
