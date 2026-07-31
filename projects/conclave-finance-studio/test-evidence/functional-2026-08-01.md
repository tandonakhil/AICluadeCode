# Test evidence — `functional` suite

**Run date:** 2026-08-01 (Gate 8 · Test re-run, post-pass-5)  
**Commit under test:** `dev` @ `b1b5dde` — "The ID-to-scenario joins stop being inferred, and 186 + 77 stops being 262"  
**Project repo:** `6dae43e`  
**Suite owner:** `functional-agent`  
**Entry point:** `tests/suites/functional/run.sh`  
**Status:** `EXECUTED`  
**Exit code:** 0  
**Scenarios:** 96 executed — 96 PASS, 0 FAIL, 0 SKIPPED  
**Blocking:** yes (PROJECT_CONTEXT Active Team — "Test Policy: all suites blocking", no advisory exception)

This file REPLACES the `functional-2026-07-31.md` written before the gate-8
loop-back. That file described a commit at which four detector families
(F26, F28, F9, F33) did not exist and in which scenario names it cited had
since been renamed. It was deleted rather than left beside this one.

---

## Per-scenario evidence

### Scenario: test_AC_F29_01_omission_named_with_its_history
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_01_omission_named_with_its_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_01_omission_named_with_its_history PASSED [  1%]`

### Scenario: test_AC_F29_05_insufficient_history_is_not_evaluable_and_not_reported_clear
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_05_insufficient_history_is_not_evaluable_and_not_reported_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_05_insufficient_history_is_not_evaluable_and_not_reported_clear PASSED [  2%]`

### Scenario: test_AC_F29_06_a_present_in_range_entry_raises_no_omission
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_06_a_present_in_range_entry_raises_no_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_06_a_present_in_range_entry_raises_no_omission PASSED [  3%]`

### Scenario: test_AC_F29_07_a_present_out_of_range_entry_raises_no_omission
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_07_a_present_out_of_range_entry_raises_no_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_07_a_present_out_of_range_entry_raises_no_omission PASSED [  4%]`

### Scenario: test_AC_F29_08_and_AC_F42_04_paired_comparison_is_one_result
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_08_and_AC_F42_04_paired_comparison_is_one_result`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_08_and_AC_F42_04_paired_comparison_is_one_result PASSED [  5%]`

### Scenario: test_AC_F42_04_identical_selection_on_both_sides
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_04_identical_selection_on_both_sides`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_04_identical_selection_on_both_sides PASSED [  6%]`

### Scenario: test_AC_F29_09_and_AC_F38_02_no_population_means_the_run_does_not_start
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_09_and_AC_F38_02_no_population_means_the_run_does_not_start`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_09_and_AC_F38_02_no_population_means_the_run_does_not_start PASSED [  7%]`

### Scenario: test_AC_F29_11_findings_carry_a_dossier_and_a_coverage_statement
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_11_findings_carry_a_dossier_and_a_coverage_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_11_findings_carry_a_dossier_and_a_coverage_statement PASSED [  8%]`

### Scenario: test_AC_F38_03_coverage_names_the_unscanned_portions
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_03_coverage_names_the_unscanned_portions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_03_coverage_names_the_unscanned_portions PASSED [  9%]`

### Scenario: test_AC_F38_04_05_06_the_three_surfaces_are_qualified_identically
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_04_05_06_the_three_surfaces_are_qualified_identically`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_04_05_06_the_three_surfaces_are_qualified_identically PASSED [ 10%]`

### Scenario: test_AC_F38_07_a_full_and_a_partial_result_are_textually_different
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_07_a_full_and_a_partial_result_are_textually_different`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_07_a_full_and_a_partial_result_are_textually_different PASSED [ 11%]`

### Scenario: test_AC_F38_15_a_partial_run_carries_its_banner
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_15_a_partial_run_carries_its_banner`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_15_a_partial_run_carries_its_banner PASSED [ 12%]`

### Scenario: test_AC_F38_08_zero_coverage_produces_no_findings_conclusion
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_08_zero_coverage_produces_no_findings_conclusion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_08_zero_coverage_produces_no_findings_conclusion PASSED [ 13%]`

### Scenario: test_AC_F38_16_unclassified_columns_refuse_a_model_bound_run
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_16_unclassified_columns_refuse_a_model_bound_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_16_unclassified_columns_refuse_a_model_bound_run PASSED [ 14%]`

### Scenario: test_AC_F38_17_personal_data_query_is_unroutable_not_filtered
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_17_personal_data_query_is_unroutable_not_filtered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F38_17_personal_data_query_is_unroutable_not_filtered PASSED [ 15%]`

### Scenario: test_AC_F42_01_present_anomaly_named_with_its_historical_range
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_01_present_anomaly_named_with_its_historical_range`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_01_present_anomaly_named_with_its_historical_range PASSED [ 16%]`

### Scenario: test_AC_F42_07_the_threshold_in_force_is_stated
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_07_the_threshold_in_force_is_stated`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F42_07_the_threshold_in_force_is_stated PASSED [ 17%]`

### Scenario: test_AC_F29_10_and_AC_F42_06_a_lost_dataset_emits_no_conclusion
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_10_and_AC_F42_06_a_lost_dataset_emits_no_conclusion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F29_10_and_AC_F42_06_a_lost_dataset_emits_no_conclusion PASSED [ 18%]`

### Scenario: test_AC_F1_01_an_incomplete_dossier_cannot_be_persisted
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F1_01_an_incomplete_dossier_cannot_be_persisted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F1_01_an_incomplete_dossier_cannot_be_persisted PASSED [ 19%]`

### Scenario: test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp PASSED [ 20%]`

### Scenario: test_a_detector_run_makes_zero_model_calls
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_a_detector_run_makes_zero_model_calls`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_acceptance_criteria.py::test_a_detector_run_makes_zero_model_calls PASSED [ 21%]`

### Scenario: test_AC_F26_01_the_run_lists_exactly_the_seeded_divergences_no_more_no_fewer
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_01_the_run_lists_exactly_the_seeded_divergences_no_more_no_fewer`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_01_the_run_lists_exactly_the_seeded_divergences_no_more_no_fewer PASSED [ 22%]`

### Scenario: test_AC_F26_02_each_divergence_carries_balance_segment_period_and_both_totals
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_02_each_divergence_carries_balance_segment_period_and_both_totals`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_02_each_divergence_carries_balance_segment_period_and_both_totals PASSED [ 23%]`

### Scenario: test_AC_F26_03_a_tying_warehouse_states_zero_divergences_with_its_coverage
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_03_a_tying_warehouse_states_zero_divergences_with_its_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_03_a_tying_warehouse_states_zero_divergences_with_its_coverage PASSED [ 25%]`

### Scenario: test_AC_F26_04_the_missing_batch_names_its_expected_arrival_and_population
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_04_the_missing_batch_names_its_expected_arrival_and_population`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_04_the_missing_batch_names_its_expected_arrival_and_population PASSED [ 26%]`

### Scenario: test_the_staleness_leg_declares_that_it_has_no_close_clock_to_measure_against
- Input: `tests/suites/functional/test_f26_criteria.py::test_the_staleness_leg_declares_that_it_has_no_close_clock_to_measure_against`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_the_staleness_leg_declares_that_it_has_no_close_clock_to_measure_against PASSED [ 27%]`

### Scenario: test_AC_F26_06_an_absent_control_extract_reports_not_run_with_no_coverage_figure
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_06_an_absent_control_extract_reports_not_run_with_no_coverage_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_06_an_absent_control_extract_reports_not_run_with_no_coverage_figure PASSED [ 28%]`

### Scenario: test_AC_F26_07_a_complete_f26_run_observes_zero_model_invocations
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_complete_f26_run_observes_zero_model_invocations`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_complete_f26_run_observes_zero_model_invocations PASSED [ 29%]`

### Scenario: test_AC_F26_07_a_model_call_from_inside_the_f26_run_would_have_been_refused
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_model_call_from_inside_the_f26_run_would_have_been_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_07_a_model_call_from_inside_the_f26_run_would_have_been_refused PASSED [ 30%]`

### Scenario: test_AC_F26_08_a_divergence_of_one_smallest_currency_unit_is_reported_exactly
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_08_a_divergence_of_one_smallest_currency_unit_is_reported_exactly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_08_a_divergence_of_one_smallest_currency_unit_is_reported_exactly PASSED [ 31%]`

### Scenario: test_AC_F26_09_the_first_and_last_in_scope_periods_are_both_reported
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_09_the_first_and_last_in_scope_periods_are_both_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_09_the_first_and_last_in_scope_periods_are_both_reported PASSED [ 32%]`

### Scenario: test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen
- Input: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f26_criteria.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen PASSED [ 33%]`

### Scenario: test_AC_F28_01_the_a6_check_names_the_control_account_subledger_and_difference
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_01_the_a6_check_names_the_control_account_subledger_and_difference`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_01_the_a6_check_names_the_control_account_subledger_and_difference PASSED [ 34%]`

### Scenario: test_AC_F28_02_the_a7_check_names_both_entities_the_pair_and_the_direction
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_02_the_a7_check_names_both_entities_the_pair_and_the_direction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_02_the_a7_check_names_both_entities_the_pair_and_the_direction PASSED [ 35%]`

### Scenario: test_AC_F28_03_the_a8_check_names_the_account_entity_two_periods_and_the_gap
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_03_the_a8_check_names_the_account_entity_two_periods_and_the_gap`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_03_the_a8_check_names_the_account_entity_two_periods_and_the_gap PASSED [ 36%]`

### Scenario: test_AC_F28_04_the_a9_check_names_the_account_and_the_duplicated_amount
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_04_the_a9_check_names_the_account_and_the_duplicated_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_04_the_a9_check_names_the_account_and_the_duplicated_amount PASSED [ 37%]`

### Scenario: test_AC_F28_05_the_a10_check_names_the_account_residual_and_threshold_in_force
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_05_the_a10_check_names_the_account_residual_and_threshold_in_force`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_05_the_a10_check_names_the_account_residual_and_threshold_in_force PASSED [ 38%]`

### Scenario: test_AC_F28_06_all_five_checks_are_listed_individually_with_their_coverage
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_all_five_checks_are_listed_individually_with_their_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_all_five_checks_are_listed_individually_with_their_coverage PASSED [ 39%]`

### Scenario: test_AC_F28_06_a_run_at_full_coverage_with_no_findings_says_so_for_each_check
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_a_run_at_full_coverage_with_no_findings_says_so_for_each_check`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_06_a_run_at_full_coverage_with_no_findings_says_so_for_each_check PASSED [ 40%]`

### Scenario: test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report PASSED [ 41%]`

### Scenario: test_AC_F28_07_the_overall_conclusion_is_not_stated_as_an_all_clear
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_the_overall_conclusion_is_not_stated_as_an_all_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_the_overall_conclusion_is_not_stated_as_an_all_clear PASSED [ 42%]`

### Scenario: test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all PASSED [ 43%]`

### Scenario: test_AC_F28_08_a_complete_f28_run_observes_zero_model_invocations
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_complete_f28_run_observes_zero_model_invocations`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_complete_f28_run_observes_zero_model_invocations PASSED [ 44%]`

### Scenario: test_AC_F28_08_a_model_call_from_inside_a_boundary_check_would_be_refused
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_model_call_from_inside_a_boundary_check_would_be_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_08_a_model_call_from_inside_a_boundary_check_would_be_refused PASSED [ 45%]`

### Scenario: test_AC_F28_09_a_failing_a10_result_states_that_it_covers_the_balance_only
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_a_failing_a10_result_states_that_it_covers_the_balance_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_a_failing_a10_result_states_that_it_covers_the_balance_only PASSED [ 46%]`

### Scenario: test_AC_F28_09_an_a10_result_that_found_nothing_states_it_too
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_found_nothing_states_it_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_found_nothing_states_it_too PASSED [ 47%]`

### Scenario: test_AC_F28_09_an_a10_result_that_could_not_run_states_it_too
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_could_not_run_states_it_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_09_an_a10_result_that_could_not_run_states_it_too PASSED [ 48%]`

### Scenario: test_AC_F28_10_the_five_checks_are_visible_on_the_exceptions_screen_with_their_states
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_five_checks_are_visible_on_the_exceptions_screen_with_their_states`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_five_checks_are_visible_on_the_exceptions_screen_with_their_states PASSED [ 50%]`

### Scenario: test_AC_F28_10_the_run_statement_on_screen_does_not_claim_an_all_clear
- Input: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_run_statement_on_screen_does_not_claim_an_all_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_AC_F28_10_the_run_statement_on_screen_does_not_claim_an_all_clear PASSED [ 51%]`

### Scenario: test_the_exceptions_screen_carrying_these_checks_is_reachable_from_the_entry_point
- Input: `tests/suites/functional/test_f28_criteria.py::test_the_exceptions_screen_carrying_these_checks_is_reachable_from_the_entry_point`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f28_criteria.py::test_the_exceptions_screen_carrying_these_checks_is_reachable_from_the_entry_point PASSED [ 52%]`

### Scenario: test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence PASSED [ 53%]`

### Scenario: test_AC_F33_02_a_natural_account_divergence_confirms_the_shared_caption
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_02_a_natural_account_divergence_confirms_the_shared_caption`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_02_a_natural_account_divergence_confirms_the_shared_caption PASSED [ 54%]`

### Scenario: test_AC_F33_03_an_intercompany_miscoding_is_surfaced_with_no_proposal
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_03_an_intercompany_miscoding_is_surfaced_with_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_03_an_intercompany_miscoding_is_surfaced_with_no_proposal PASSED [ 55%]`

### Scenario: test_AC_F33_04_a_caption_crossing_is_surfaced_with_no_proposal
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_04_a_caption_crossing_is_surfaced_with_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_04_a_caption_crossing_is_surfaced_with_no_proposal PASSED [ 56%]`

### Scenario: test_AC_F33_05_a_cut_off_error_states_that_cut_off_is_not_proposed
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_05_a_cut_off_error_states_that_cut_off_is_not_proposed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_05_a_cut_off_error_states_that_cut_off_is_not_proposed PASSED [ 57%]`

### Scenario: test_the_three_out_of_scope_sub_types_produce_no_proposal_between_them
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_three_out_of_scope_sub_types_produce_no_proposal_between_them`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_the_three_out_of_scope_sub_types_produce_no_proposal_between_them PASSED [ 58%]`

### Scenario: test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions PASSED [ 59%]`

### Scenario: test_the_backtest_measures_a_detector_that_actually_ran
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_backtest_measures_a_detector_that_actually_ran`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_the_backtest_measures_a_detector_that_actually_ran PASSED [ 60%]`

### Scenario: test_AC_F33_07_the_recall_bias_label_is_a_required_field_of_the_schema
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_the_recall_bias_label_is_a_required_field_of_the_schema`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_the_recall_bias_label_is_a_required_field_of_the_schema PASSED [ 61%]`

### Scenario: test_AC_F33_07_a_record_without_the_label_is_invalid_and_the_run_fails
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_a_record_without_the_label_is_invalid_and_the_run_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_07_a_record_without_the_label_is_invalid_and_the_run_fails PASSED [ 62%]`

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_on_the_screen
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_on_the_screen PASSED [ 63%]`

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_in_a_dossier
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_a_dossier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_a_dossier PASSED [ 64%]`

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_recall_in_an_export
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_an_export`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_the_label_is_adjacent_to_recall_in_an_export PASSED [ 65%]`

### Scenario: test_AC_F33_08_no_surface_can_show_recall_without_the_label
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_no_surface_can_show_recall_without_the_label`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_08_no_surface_can_show_recall_without_the_label PASSED [ 66%]`

### Scenario: test_AC_F33_09_a_held_out_period_with_no_labels_emits_no_figures
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_a_held_out_period_with_no_labels_emits_no_figures`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_a_held_out_period_with_no_labels_emits_no_figures PASSED [ 67%]`

### Scenario: test_AC_F33_09_the_no_labels_state_is_visible_on_the_exceptions_screen
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_the_no_labels_state_is_visible_on_the_exceptions_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_09_the_no_labels_state_is_visible_on_the_exceptions_screen PASSED [ 68%]`

### Scenario: test_AC_F33_10_a_single_label_produces_figures_carrying_a_label_count_of_one
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_10_a_single_label_produces_figures_carrying_a_label_count_of_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_10_a_single_label_produces_figures_carrying_a_label_count_of_one PASSED [ 69%]`

### Scenario: test_AC_F33_11_an_unretrievable_label_set_emits_no_accuracy_claim
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_11_an_unretrievable_label_set_emits_no_accuracy_claim`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_11_an_unretrievable_label_set_emits_no_accuracy_claim PASSED [ 70%]`

### Scenario: test_could_not_retrieve_is_distinguishable_from_a_period_with_no_labels
- Input: `tests/suites/functional/test_f33_criteria.py::test_could_not_retrieve_is_distinguishable_from_a_period_with_no_labels`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_could_not_retrieve_is_distinguishable_from_a_period_with_no_labels PASSED [ 71%]`

### Scenario: test_AC_F33_12_the_coding_findings_are_visible_with_current_proposed_and_sub_type
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_coding_findings_are_visible_with_current_proposed_and_sub_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_coding_findings_are_visible_with_current_proposed_and_sub_type PASSED [ 72%]`

### Scenario: test_AC_F33_12_an_out_of_scope_row_renders_no_proposed_coding
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_an_out_of_scope_row_renders_no_proposed_coding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_an_out_of_scope_row_renders_no_proposed_coding PASSED [ 73%]`

### Scenario: test_AC_F33_12_the_backtest_figures_are_on_the_same_screen_as_the_findings
- Input: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_backtest_figures_are_on_the_same_screen_as_the_findings`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_AC_F33_12_the_backtest_figures_are_on_the_same_screen_as_the_findings PASSED [ 75%]`

### Scenario: test_the_exceptions_screen_carrying_the_coding_region_is_reachable
- Input: `tests/suites/functional/test_f33_criteria.py::test_the_exceptions_screen_carrying_the_coding_region_is_reachable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f33_criteria.py::test_the_exceptions_screen_carrying_the_coding_region_is_reachable PASSED [ 76%]`

### Scenario: test_AC_F9_01_the_numeric_leg_escalates_before_period_twelve_and_records_when
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_01_the_numeric_leg_escalates_before_period_twelve_and_records_when`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_01_the_numeric_leg_escalates_before_period_twelve_and_records_when PASSED [ 77%]`

### Scenario: test_AC_F9_02_the_iron_curtain_aggregate_is_the_primary_figure
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_iron_curtain_aggregate_is_the_primary_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_iron_curtain_aggregate_is_the_primary_figure PASSED [ 78%]`

### Scenario: test_AC_F9_02_the_single_period_delta_is_not_the_headline
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_single_period_delta_is_not_the_headline`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_02_the_single_period_delta_is_not_the_headline PASSED [ 79%]`

### Scenario: test_AC_F9_03_the_narrative_leg_escalates_alone_with_the_numeric_leg_silent
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_leg_escalates_alone_with_the_numeric_leg_silent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_leg_escalates_alone_with_the_numeric_leg_silent PASSED [ 80%]`

### Scenario: test_AC_F9_03_the_narrative_escalation_names_the_periods_and_quotes_the_assertion
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_escalation_names_the_periods_and_quotes_the_assertion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_03_the_narrative_escalation_names_the_periods_and_quotes_the_assertion PASSED [ 81%]`

### Scenario: test_AC_F9_04_every_escalation_raises_the_risk_grade_and_revokes_auto_pass
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_every_escalation_raises_the_risk_grade_and_revokes_auto_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_every_escalation_raises_the_risk_grade_and_revokes_auto_pass PASSED [ 82%]`

### Scenario: test_AC_F9_04_the_change_is_recorded_with_its_cause_and_its_prior_value
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_the_change_is_recorded_with_its_cause_and_its_prior_value`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_the_change_is_recorded_with_its_cause_and_its_prior_value PASSED [ 83%]`

### Scenario: test_AC_F9_04_holds_for_the_narrative_leg_as_well_as_the_numeric_one
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_holds_for_the_narrative_leg_as_well_as_the_numeric_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_04_holds_for_the_narrative_leg_as_well_as_the_numeric_one PASSED [ 84%]`

### Scenario: test_AC_F9_05_an_account_with_too_little_history_is_named_not_shown_as_monitored
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_an_account_with_too_little_history_is_named_not_shown_as_monitored`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_an_account_with_too_little_history_is_named_not_shown_as_monitored PASSED [ 85%]`

### Scenario: test_AC_F9_05_the_unassessed_account_is_excluded_from_coverage
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_unassessed_account_is_excluded_from_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_unassessed_account_is_excluded_from_coverage PASSED [ 86%]`

### Scenario: test_AC_F9_05_the_state_is_visible_on_the_monitors_screen
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_state_is_visible_on_the_monitors_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_05_the_state_is_visible_on_the_monitors_screen PASSED [ 87%]`

### Scenario: test_AC_F9_06_one_fixture_escalates_and_the_other_stops_one_period_short
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_one_fixture_escalates_and_the_other_stops_one_period_short`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_one_fixture_escalates_and_the_other_stops_one_period_short PASSED [ 88%]`

### Scenario: test_AC_F9_06_the_record_that_did_not_escalate_states_how_many_periods_would
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_the_record_that_did_not_escalate_states_how_many_periods_would`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_06_the_record_that_did_not_escalate_states_how_many_periods_would PASSED [ 89%]`

### Scenario: test_AC_F9_07_alternating_sub_threshold_movements_raise_no_escalation
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_07_alternating_sub_threshold_movements_raise_no_escalation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_07_alternating_sub_threshold_movements_raise_no_escalation PASSED [ 90%]`

### Scenario: test_AC_F9_08_the_monitors_screen_lists_escalations_with_account_aggregate_period_leg
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_monitors_screen_lists_escalations_with_account_aggregate_period_leg`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_monitors_screen_lists_escalations_with_account_aggregate_period_leg PASSED [ 91%]`

### Scenario: test_AC_F9_08_the_control_state_change_is_readable_on_the_row
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_control_state_change_is_readable_on_the_row`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_08_the_control_state_change_is_readable_on_the_row PASSED [ 92%]`

### Scenario: test_the_monitors_screen_is_reachable_from_the_entry_point
- Input: `tests/suites/functional/test_f9_criteria.py::test_the_monitors_screen_is_reachable_from_the_entry_point`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_the_monitors_screen_is_reachable_from_the_entry_point PASSED [ 93%]`

### Scenario: test_AC_F9_09_periods_with_no_recorded_explanation_are_named_not_evaluable
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_periods_with_no_recorded_explanation_are_named_not_evaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_periods_with_no_recorded_explanation_are_named_not_evaluable PASSED [ 94%]`

### Scenario: test_AC_F9_09_the_sequence_is_not_reported_as_having_been_checked
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_sequence_is_not_reported_as_having_been_checked`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_sequence_is_not_reported_as_having_been_checked PASSED [ 95%]`

### Scenario: test_AC_F9_09_the_named_periods_are_visible_on_the_monitors_screen
- Input: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_named_periods_are_visible_on_the_monitors_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_AC_F9_09_the_named_periods_are_visible_on_the_monitors_screen PASSED [ 96%]`

### Scenario: test_both_legs_run_over_the_same_declared_population
- Input: `tests/suites/functional/test_f9_criteria.py::test_both_legs_run_over_the_same_declared_population`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_both_legs_run_over_the_same_declared_population PASSED [ 97%]`

### Scenario: test_a_numeric_leg_that_could_not_run_does_not_suppress_the_narrative_one
- Input: `tests/suites/functional/test_f9_criteria.py::test_a_numeric_leg_that_could_not_run_does_not_suppress_the_narrative_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_a_numeric_leg_that_could_not_run_does_not_suppress_the_narrative_one PASSED [ 98%]`

### Scenario: test_the_narrative_leg_uses_a_query_that_cannot_reach_a_model
- Input: `tests/suites/functional/test_f9_criteria.py::test_the_narrative_leg_uses_a_query_that_cannot_reach_a_model`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/functional/run.sh` — pytest -v line: `tests/suites/functional/test_f9_criteria.py::test_the_narrative_leg_uses_a_query_that_cannot_reach_a_model PASSED [100%]`
