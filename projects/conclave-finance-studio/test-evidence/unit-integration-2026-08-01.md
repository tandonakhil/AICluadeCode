# Test evidence — `unit-integration` suite

**Run date:** 2026-08-01 (Gate 8 · Test re-run, post-pass-5)  
**Commit under test:** `dev` @ `b1b5dde` — "The ID-to-scenario joins stop being inferred, and 186 + 77 stops being 262"  
**Project repo:** `6dae43e`  
**Suite owner:** `test-agent`  
**Entry point:** ``.venv/bin/python -m pytest` (pytest.ini testpaths, backend/tests half)`  
**Status:** `EXECUTED`  
**Exit code:** 0  
**Scenarios:** 1428 executed — 1428 PASS, 0 FAIL, 0 SKIPPED  
**Blocking:** yes (PROJECT_CONTEXT Active Team — "Test Policy: all suites blocking", no advisory exception)

This file REPLACES the `unit-integration-2026-07-31.md` written before the gate-8
loop-back. That file described a commit at which four detector families
(F26, F28, F9, F33) did not exist and in which scenario names it cited had
since been renamed. It was deleted rather than left beside this one.

---

## Per-scenario evidence

### Scenario: test_there_are_exactly_six_types_and_they_are_the_kbs_six
- Input: `backend/tests/test_abstention.py::test_there_are_exactly_six_types_and_they_are_the_kbs_six`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_there_are_exactly_six_types_and_they_are_the_kbs_six PASSED [  0%]`

### Scenario: test_every_type_names_its_trigger_and_who_computes_it
- Input: `backend/tests/test_abstention.py::test_every_type_names_its_trigger_and_who_computes_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_every_type_names_its_trigger_and_who_computes_it PASSED [  0%]`

### Scenario: test_the_type_set_is_closed
- Input: `backend/tests/test_abstention.py::test_the_type_set_is_closed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_type_set_is_closed PASSED     [  0%]`

### Scenario: test_an_abstention_must_name_its_gap_and_carry_one_resolving_action
- Input: `backend/tests/test_abstention.py::test_an_abstention_must_name_its_gap_and_carry_one_resolving_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstention_must_name_its_gap_and_carry_one_resolving_action PASSED [  0%]`

### Scenario: test_an_abstention_carries_no_confidence_score_or_severity
- Input: `backend/tests/test_abstention.py::test_an_abstention_carries_no_confidence_score_or_severity`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstention_carries_no_confidence_score_or_severity PASSED [  0%]`

### Scenario: test_there_are_four_states_and_unknown_is_one_of_them
- Input: `backend/tests/test_abstention.py::test_there_are_four_states_and_unknown_is_one_of_them`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_there_are_four_states_and_unknown_is_one_of_them PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB1]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB1] PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB2]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB2] PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB3]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB3]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB3] PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB4]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB4]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB4] PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB5]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB5]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB5] PASSED [  0%]`

### Scenario: test_no_abstention_type_ever_renders_as_a_negative_finding[AB6]
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB6]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB6] PASSED [  0%]`

### Scenario: test_unknown_is_not_in_the_negative_states_and_red_is
- Input: `backend/tests/test_abstention.py::test_unknown_is_not_in_the_negative_states_and_red_is`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_unknown_is_not_in_the_negative_states_and_red_is PASSED [  0%]`

### Scenario: test_the_mapping_from_type_to_state_is_total_and_constant
- Input: `backend/tests/test_abstention.py::test_the_mapping_from_type_to_state_is_total_and_constant`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_mapping_from_type_to_state_is_total_and_constant PASSED [  0%]`

### Scenario: test_is_negative_finding_is_computed_not_stored
- Input: `backend/tests/test_abstention.py::test_is_negative_finding_is_computed_not_stored`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_is_negative_finding_is_computed_not_stored PASSED [  1%]`

### Scenario: test_the_assurance_item_constructor_refuses_a_miscoloured_abstention
- Input: `backend/tests/test_abstention.py::test_the_assurance_item_constructor_refuses_a_miscoloured_abstention`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_assurance_item_constructor_refuses_a_miscoloured_abstention PASSED [  1%]`

### Scenario: test_a_fifth_state_is_refused
- Input: `backend/tests/test_abstention.py::test_a_fifth_state_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_a_fifth_state_is_refused PASSED   [  1%]`

### Scenario: test_conclusions_and_abstentions_render_through_the_same_object
- Input: `backend/tests/test_abstention.py::test_conclusions_and_abstentions_render_through_the_same_object`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_conclusions_and_abstentions_render_through_the_same_object PASSED [  1%]`

### Scenario: test_the_abstention_statement_says_could_not_and_names_the_action
- Input: `backend/tests/test_abstention.py::test_the_abstention_statement_says_could_not_and_names_the_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_abstention_statement_says_could_not_and_names_the_action PASSED [  1%]`

### Scenario: test_there_is_no_argument_to_a_conclusion_that_produces_unknown
- Input: `backend/tests/test_abstention.py::test_there_is_no_argument_to_a_conclusion_that_produces_unknown`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_there_is_no_argument_to_a_conclusion_that_produces_unknown PASSED [  1%]`

### Scenario: test_the_quality_denominator_is_concluded_items_only
- Input: `backend/tests/test_abstention.py::test_the_quality_denominator_is_concluded_items_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_quality_denominator_is_concluded_items_only PASSED [  1%]`

### Scenario: test_abstaining_more_does_not_move_precision
- Input: `backend/tests/test_abstention.py::test_abstaining_more_does_not_move_precision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_abstaining_more_does_not_move_precision PASSED [  1%]`

### Scenario: test_abstentions_are_reported_as_a_named_third_figure
- Input: `backend/tests/test_abstention.py::test_abstentions_are_reported_as_a_named_third_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_abstentions_are_reported_as_a_named_third_figure PASSED [  1%]`

### Scenario: test_no_function_in_the_module_divides_by_concluded_plus_abstained
- Input: `backend/tests/test_abstention.py::test_no_function_in_the_module_divides_by_concluded_plus_abstained`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_function_in_the_module_divides_by_concluded_plus_abstained PASSED [  1%]`

### Scenario: test_rates_refuses_more_correct_than_concluded
- Input: `backend/tests/test_abstention.py::test_rates_refuses_more_correct_than_concluded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_rates_refuses_more_correct_than_concluded PASSED [  1%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB1]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB1] PASSED [  1%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB2]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB2] PASSED [  1%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB3]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB3]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB3] PASSED [  1%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB4]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB4]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB4] PASSED [  2%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB5]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB5]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB5] PASSED [  2%]`

### Scenario: test_an_abstained_item_counts_as_covered_not_as_a_gap[AB6]
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB6]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB6] PASSED [  2%]`

### Scenario: test_an_abstention_costs_the_routing_budget_less_than_a_conclusion
- Input: `backend/tests/test_abstention.py::test_an_abstention_costs_the_routing_budget_less_than_a_conclusion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_abstention_costs_the_routing_budget_less_than_a_conclusion PASSED [  2%]`

### Scenario: test_weights_that_make_declining_as_expensive_as_concluding_are_refused
- Input: `backend/tests/test_abstention.py::test_weights_that_make_declining_as_expensive_as_concluding_are_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_weights_that_make_declining_as_expensive_as_concluding_are_refused PASSED [  2%]`

### Scenario: test_the_bundles_shipped_weights_satisfy_that_constraint
- Input: `backend/tests/test_abstention.py::test_the_bundles_shipped_weights_satisfy_that_constraint`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_bundles_shipped_weights_satisfy_that_constraint PASSED [  2%]`

### Scenario: test_zero_abstentions_over_a_period_is_a_control_finding
- Input: `backend/tests/test_abstention.py::test_zero_abstentions_over_a_period_is_a_control_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_zero_abstentions_over_a_period_is_a_control_finding PASSED [  2%]`

### Scenario: test_near_zero_is_also_a_control_finding_not_only_exact_zero
- Input: `backend/tests/test_abstention.py::test_near_zero_is_also_a_control_finding_not_only_exact_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_near_zero_is_also_a_control_finding_not_only_exact_zero PASSED [  2%]`

### Scenario: test_above_band_is_a_usefulness_finding_to_a_different_owner
- Input: `backend/tests/test_abstention.py::test_above_band_is_a_usefulness_finding_to_a_different_owner`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_above_band_is_a_usefulness_finding_to_a_different_owner PASSED [  2%]`

### Scenario: test_in_band_produces_no_finding
- Input: `backend/tests/test_abstention.py::test_in_band_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_in_band_produces_no_finding PASSED [  2%]`

### Scenario: test_the_two_tails_route_to_different_owners
- Input: `backend/tests/test_abstention.py::test_the_two_tails_route_to_different_owners`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_the_two_tails_route_to_different_owners PASSED [  2%]`

### Scenario: test_a_band_over_nothing_is_not_a_measurement
- Input: `backend/tests/test_abstention.py::test_a_band_over_nothing_is_not_a_measurement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_a_band_over_nothing_is_not_a_measurement PASSED [  2%]`

### Scenario: test_an_inverted_band_is_refused
- Input: `backend/tests/test_abstention.py::test_an_inverted_band_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_an_inverted_band_is_refused PASSED [  2%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[be_more_decisive]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[be_more_decisive]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[be_more_decisive] PASSED [  2%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[confidence_threshold]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_threshold]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_threshold] PASSED [  3%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[confidence_slider]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_slider]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_slider] PASSED [  3%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[abstention_rate_target]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[abstention_rate_target]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[abstention_rate_target] PASSED [  3%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[min_confidence]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[min_confidence]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[min_confidence] PASSED [  3%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[suppress_abstentions]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[suppress_abstentions]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[suppress_abstentions] PASSED [  3%]`

### Scenario: test_no_user_facing_setting_may_change_abstention_behaviour[auto_conclude_when_ambiguous]
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[auto_conclude_when_ambiguous]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[auto_conclude_when_ambiguous] PASSED [  3%]`

### Scenario: test_ordinary_settings_pass
- Input: `backend/tests/test_abstention.py::test_ordinary_settings_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_abstention.py::test_ordinary_settings_pass PASSED     [  3%]`

### Scenario: test_a_distinct_human_approver_is_accepted_and_records_its_decision
- Input: `backend/tests/test_authorship_closure.py::test_a_distinct_human_approver_is_accepted_and_records_its_decision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_a_distinct_human_approver_is_accepted_and_records_its_decision PASSED [  3%]`

### Scenario: test_the_author_may_not_approve_its_own_item
- Input: `backend/tests/test_authorship_closure.py::test_the_author_may_not_approve_its_own_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_the_author_may_not_approve_its_own_item PASSED [  3%]`

### Scenario: test_the_invoker_may_not_approve
- Input: `backend/tests/test_authorship_closure.py::test_the_invoker_may_not_approve`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_the_invoker_may_not_approve PASSED [  3%]`

### Scenario: test_author_and_invoker_may_not_be_the_same_identity
- Input: `backend/tests/test_authorship_closure.py::test_author_and_invoker_may_not_be_the_same_identity`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_author_and_invoker_may_not_be_the_same_identity PASSED [  3%]`

### Scenario: test_an_ineligible_approval_by_direct_api_produces_the_same_denial
- Input: `backend/tests/test_authorship_closure.py::test_an_ineligible_approval_by_direct_api_produces_the_same_denial`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_an_ineligible_approval_by_direct_api_produces_the_same_denial PASSED [  3%]`

### Scenario: test_eligibility_is_computed_from_authorship_not_from_a_role_list
- Input: `backend/tests/test_authorship_closure.py::test_eligibility_is_computed_from_authorship_not_from_a_role_list`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_eligibility_is_computed_from_authorship_not_from_a_role_list PASSED [  3%]`

### Scenario: test_an_item_with_no_eligible_approver_reports_an_empty_set
- Input: `backend/tests/test_authorship_closure.py::test_an_item_with_no_eligible_approver_reports_an_empty_set`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_an_item_with_no_eligible_approver_reports_an_empty_set PASSED [  3%]`

### Scenario: test_an_agent_principal_is_denied_the_approve_capability_before_any_rule
- Input: `backend/tests/test_authorship_closure.py::test_an_agent_principal_is_denied_the_approve_capability_before_any_rule`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_an_agent_principal_is_denied_the_approve_capability_before_any_rule PASSED [  3%]`

### Scenario: test_an_agent_approval_is_unrepresentable_even_by_raw_sql
- Input: `backend/tests/test_authorship_closure.py::test_an_agent_approval_is_unrepresentable_even_by_raw_sql`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_an_agent_approval_is_unrepresentable_even_by_raw_sql PASSED [  4%]`

### Scenario: test_the_kind_column_admits_only_human
- Input: `backend/tests/test_authorship_closure.py::test_the_kind_column_admits_only_human`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_the_kind_column_admits_only_human PASSED [  4%]`

### Scenario: test_a_service_principal_cannot_occupy_the_approver_field
- Input: `backend/tests/test_authorship_closure.py::test_a_service_principal_cannot_occupy_the_approver_field`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_a_service_principal_cannot_occupy_the_approver_field PASSED [  4%]`

### Scenario: test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p1]
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p1] PASSED [  4%]`

### Scenario: test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p2]
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p2] PASSED [  4%]`

### Scenario: test_every_collapsed_pair_is_refused_by_the_schema[p1-p1-p2]
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p1-p2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p1-p2] PASSED [  4%]`

### Scenario: test_an_approval_cannot_exist_without_a_decision
- Input: `backend/tests/test_authorship_closure.py::test_an_approval_cannot_exist_without_a_decision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_an_approval_cannot_exist_without_a_decision PASSED [  4%]`

### Scenario: test_one_approval_per_item
- Input: `backend/tests/test_authorship_closure.py::test_one_approval_per_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_one_approval_per_item PASSED [  4%]`

### Scenario: test_a_platform_admin_cannot_approve_a_finance_action
- Input: `backend/tests/test_authorship_closure.py::test_a_platform_admin_cannot_approve_a_finance_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_authorship_closure.py::test_a_platform_admin_cannot_approve_a_finance_action PASSED [  4%]`

### Scenario: test_the_run_cap_stops_production_and_records_the_trip
- Input: `backend/tests/test_blast_radius.py::test_the_run_cap_stops_production_and_records_the_trip`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_run_cap_stops_production_and_records_the_trip PASSED [  4%]`

### Scenario: test_a_denied_proposal_does_not_increment_the_counter
- Input: `backend/tests/test_blast_radius.py::test_a_denied_proposal_does_not_increment_the_counter`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_a_denied_proposal_does_not_increment_the_counter PASSED [  4%]`

### Scenario: test_individually_compliant_proposals_crossing_the_period_cap_are_denied
- Input: `backend/tests/test_blast_radius.py::test_individually_compliant_proposals_crossing_the_period_cap_are_denied`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_individually_compliant_proposals_crossing_the_period_cap_are_denied PASSED [  4%]`

### Scenario: test_the_period_cap_is_per_principal
- Input: `backend/tests/test_blast_radius.py::test_the_period_cap_is_per_principal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_period_cap_is_per_principal PASSED [  4%]`

### Scenario: test_a_proposal_exceeding_the_balance_proportion_is_denied_with_all_three_numbers
- Input: `backend/tests/test_blast_radius.py::test_a_proposal_exceeding_the_balance_proportion_is_denied_with_all_three_numbers`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_a_proposal_exceeding_the_balance_proportion_is_denied_with_all_three_numbers PASSED [  4%]`

### Scenario: test_a_proposal_exactly_at_the_proportion_cap_is_allowed
- Input: `backend/tests/test_blast_radius.py::test_a_proposal_exactly_at_the_proportion_cap_is_allowed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_a_proposal_exactly_at_the_proportion_cap_is_allowed PASSED [  5%]`

### Scenario: test_a_third_consecutive_same_account_proposal_escalates_and_names_all_three
- Input: `backend/tests/test_blast_radius.py::test_a_third_consecutive_same_account_proposal_escalates_and_names_all_three`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_a_third_consecutive_same_account_proposal_escalates_and_names_all_three PASSED [  5%]`

### Scenario: test_two_consecutive_periods_do_not_escalate
- Input: `backend/tests/test_blast_radius.py::test_two_consecutive_periods_do_not_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_two_consecutive_periods_do_not_escalate PASSED [  5%]`

### Scenario: test_a_gap_in_the_sequence_breaks_the_streak
- Input: `backend/tests/test_blast_radius.py::test_a_gap_in_the_sequence_breaks_the_streak`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_a_gap_in_the_sequence_breaks_the_streak PASSED [  5%]`

### Scenario: test_the_streak_is_per_period_stateful_not_per_invocation
- Input: `backend/tests/test_blast_radius.py::test_the_streak_is_per_period_stateful_not_per_invocation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_streak_is_per_period_stateful_not_per_invocation PASSED [  5%]`

### Scenario: test_the_direction_is_part_of_the_key
- Input: `backend/tests/test_blast_radius.py::test_the_direction_is_part_of_the_key`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_direction_is_part_of_the_key PASSED [  5%]`

### Scenario: test_the_cap_holds_under_real_concurrency
- Input: `backend/tests/test_blast_radius.py::test_the_cap_holds_under_real_concurrency`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_cap_holds_under_real_concurrency PASSED [  5%]`

### Scenario: test_the_same_workload_without_the_transaction_overruns_the_cap
- Input: `backend/tests/test_blast_radius.py::test_the_same_workload_without_the_transaction_overruns_the_cap`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_same_workload_without_the_transaction_overruns_the_cap PASSED [  5%]`

### Scenario: test_the_decision_and_the_counter_commit_together
- Input: `backend/tests/test_blast_radius.py::test_the_decision_and_the_counter_commit_together`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_blast_radius.py::test_the_decision_and_the_counter_commit_together PASSED [  5%]`

### Scenario: test_a_pair_that_nets_to_zero_produces_no_finding
- Input: `backend/tests/test_boundary_primitives.py::test_a_pair_that_nets_to_zero_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_pair_that_nets_to_zero_produces_no_finding PASSED [  5%]`

### Scenario: test_an_imbalanced_pair_names_both_entities_the_pair_and_the_amount
- Input: `backend/tests/test_boundary_primitives.py::test_an_imbalanced_pair_names_both_entities_the_pair_and_the_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_an_imbalanced_pair_names_both_entities_the_pair_and_the_amount PASSED [  5%]`

### Scenario: test_the_direction_names_the_other_entity_when_the_other_side_is_long
- Input: `backend/tests/test_boundary_primitives.py::test_the_direction_names_the_other_entity_when_the_other_side_is_long`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_direction_names_the_other_entity_when_the_other_side_is_long PASSED [  5%]`

### Scenario: test_a_one_sided_pair_is_not_reported_as_an_imbalance_of_the_whole_amount
- Input: `backend/tests/test_boundary_primitives.py::test_a_one_sided_pair_is_not_reported_as_an_imbalance_of_the_whole_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_one_sided_pair_is_not_reported_as_an_imbalance_of_the_whole_amount PASSED [  5%]`

### Scenario: test_the_primitive_claims_no_cause
- Input: `backend/tests/test_boundary_primitives.py::test_the_primitive_claims_no_cause`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_primitive_claims_no_cause PASSED [  5%]`

### Scenario: test_a_declared_pair_with_no_row_is_uncovered_and_named
- Input: `backend/tests/test_boundary_primitives.py::test_a_declared_pair_with_no_row_is_uncovered_and_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_declared_pair_with_no_row_is_uncovered_and_named PASSED [  6%]`

### Scenario: test_the_pair_tolerance_boundary_is_inclusive
- Input: `backend/tests/test_boundary_primitives.py::test_the_pair_tolerance_boundary_is_inclusive`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_pair_tolerance_boundary_is_inclusive PASSED [  6%]`

### Scenario: test_a_continuous_account_produces_no_finding
- Input: `backend/tests/test_boundary_primitives.py::test_a_continuous_account_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_continuous_account_produces_no_finding PASSED [  6%]`

### Scenario: test_a_break_names_the_account_entity_both_periods_and_the_amount
- Input: `backend/tests/test_boundary_primitives.py::test_a_break_names_the_account_entity_both_periods_and_the_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_break_names_the_account_entity_both_periods_and_the_amount PASSED [  6%]`

### Scenario: test_the_first_in_scope_period_is_not_evaluable_rather_than_broken
- Input: `backend/tests/test_boundary_primitives.py::test_the_first_in_scope_period_is_not_evaluable_rather_than_broken`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_first_in_scope_period_is_not_evaluable_rather_than_broken PASSED [  6%]`

### Scenario: test_an_incomplete_rollforward_row_is_not_evaluable
- Input: `backend/tests/test_boundary_primitives.py::test_an_incomplete_rollforward_row_is_not_evaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_an_incomplete_rollforward_row_is_not_evaluable PASSED [  6%]`

### Scenario: test_the_identity_is_checked_as_well_as_the_opening_balance
- Input: `backend/tests/test_boundary_primitives.py::test_the_identity_is_checked_as_well_as_the_opening_balance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_identity_is_checked_as_well_as_the_opening_balance PASSED [  6%]`

### Scenario: test_a_declared_account_with_no_rollforward_row_is_uncovered
- Input: `backend/tests/test_boundary_primitives.py::test_a_declared_account_with_no_rollforward_row_is_uncovered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_declared_account_with_no_rollforward_row_is_uncovered PASSED [  6%]`

### Scenario: test_a_correctly_applied_revaluation_produces_no_finding
- Input: `backend/tests/test_boundary_primitives.py::test_a_correctly_applied_revaluation_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_correctly_applied_revaluation_produces_no_finding PASSED [  6%]`

### Scenario: test_a_doubled_revaluation_names_the_multiple_and_the_duplicated_amount
- Input: `backend/tests/test_boundary_primitives.py::test_a_doubled_revaluation_names_the_multiple_and_the_duplicated_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_doubled_revaluation_names_the_multiple_and_the_duplicated_amount PASSED [  6%]`

### Scenario: test_a_non_integer_mismatch_reports_the_difference_and_claims_no_multiple
- Input: `backend/tests/test_boundary_primitives.py::test_a_non_integer_mismatch_reports_the_difference_and_claims_no_multiple`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_non_integer_mismatch_reports_the_difference_and_claims_no_multiple PASSED [  6%]`

### Scenario: test_a_zero_from_rate_is_not_evaluable_rather_than_a_division_error
- Input: `backend/tests/test_boundary_primitives.py::test_a_zero_from_rate_is_not_evaluable_rather_than_a_division_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_zero_from_rate_is_not_evaluable_rather_than_a_division_error PASSED [  6%]`

### Scenario: test_a_missing_input_is_not_evaluable_rather_than_a_silent_zero
- Input: `backend/tests/test_boundary_primitives.py::test_a_missing_input_is_not_evaluable_rather_than_a_silent_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_missing_input_is_not_evaluable_rather_than_a_silent_zero PASSED [  6%]`

### Scenario: test_the_rounding_tolerance_absorbs_a_cent_but_not_a_duplicate
- Input: `backend/tests/test_boundary_primitives.py::test_the_rounding_tolerance_absorbs_a_cent_but_not_a_duplicate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_rounding_tolerance_absorbs_a_cent_but_not_a_duplicate PASSED [  6%]`

### Scenario: test_a_formula_outside_the_closed_registry_raises_rather_than_skipping
- Input: `backend/tests/test_boundary_primitives.py::test_a_formula_outside_the_closed_registry_raises_rather_than_skipping`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_formula_outside_the_closed_registry_raises_rather_than_skipping PASSED [  7%]`

### Scenario: test_there_is_no_eval_in_the_recompute_module
- Input: `backend/tests/test_boundary_primitives.py::test_there_is_no_eval_in_the_recompute_module`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_there_is_no_eval_in_the_recompute_module PASSED [  7%]`

### Scenario: test_a_residual_within_its_threshold_produces_no_finding
- Input: `backend/tests/test_boundary_primitives.py::test_a_residual_within_its_threshold_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_residual_within_its_threshold_produces_no_finding PASSED [  7%]`

### Scenario: test_a_breach_states_the_residual_and_the_threshold_in_force
- Input: `backend/tests/test_boundary_primitives.py::test_a_breach_states_the_residual_and_the_threshold_in_force`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_breach_states_the_residual_and_the_threshold_in_force PASSED [  7%]`

### Scenario: test_the_threshold_comes_from_the_data_not_from_a_parameter
- Input: `backend/tests/test_boundary_primitives.py::test_the_threshold_comes_from_the_data_not_from_a_parameter`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_threshold_comes_from_the_data_not_from_a_parameter PASSED [  7%]`

### Scenario: test_a_negative_residual_is_compared_on_its_magnitude
- Input: `backend/tests/test_boundary_primitives.py::test_a_negative_residual_is_compared_on_its_magnitude`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_a_negative_residual_is_compared_on_its_magnitude PASSED [  7%]`

### Scenario: test_the_threshold_boundary_is_inclusive
- Input: `backend/tests/test_boundary_primitives.py::test_the_threshold_boundary_is_inclusive`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_threshold_boundary_is_inclusive PASSED [  7%]`

### Scenario: test_an_account_with_no_policy_threshold_is_not_evaluable
- Input: `backend/tests/test_boundary_primitives.py::test_an_account_with_no_policy_threshold_is_not_evaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_an_account_with_no_policy_threshold_is_not_evaluable PASSED [  7%]`

### Scenario: test_the_scope_statement_is_on_a_finding
- Input: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_finding PASSED [  7%]`

### Scenario: test_the_scope_statement_is_on_a_run_that_found_nothing_too
- Input: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_run_that_found_nothing_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_run_that_found_nothing_too PASSED [  7%]`

### Scenario: test_two_offsetting_items_net_within_threshold_and_are_not_detected
- Input: `backend/tests/test_boundary_primitives.py::test_two_offsetting_items_net_within_threshold_and_are_not_detected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_boundary_primitives.py::test_two_offsetting_items_net_within_threshold_and_are_not_detected PASSED [  7%]`

### Scenario: test_an_action_absent_from_the_allowlist_is_denied_without_any_prohibition
- Input: `backend/tests/test_broker_action_path.py::test_an_action_absent_from_the_allowlist_is_denied_without_any_prohibition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_action_absent_from_the_allowlist_is_denied_without_any_prohibition PASSED [  7%]`

### Scenario: test_the_allowlist_is_intersected_with_the_skill_definition
- Input: `backend/tests/test_broker_action_path.py::test_the_allowlist_is_intersected_with_the_skill_definition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_allowlist_is_intersected_with_the_skill_definition PASSED [  7%]`

### Scenario: test_deny_by_default_runs_before_rule_evaluation
- Input: `backend/tests/test_broker_action_path.py::test_deny_by_default_runs_before_rule_evaluation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_deny_by_default_runs_before_rule_evaluation PASSED [  7%]`

### Scenario: test_an_action_record_cannot_exist_without_its_decision
- Input: `backend/tests/test_broker_action_path.py::test_an_action_record_cannot_exist_without_its_decision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_action_record_cannot_exist_without_its_decision PASSED [  7%]`

### Scenario: test_an_action_record_with_no_decision_is_rejected_by_the_database
- Input: `backend/tests/test_broker_action_path.py::test_an_action_record_with_no_decision_is_rejected_by_the_database`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_action_record_with_no_decision_is_rejected_by_the_database PASSED [  8%]`

### Scenario: test_a_denied_decision_has_no_action_record
- Input: `backend/tests/test_broker_action_path.py::test_a_denied_decision_has_no_action_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_denied_decision_has_no_action_record PASSED [  8%]`

### Scenario: test_the_log_carries_one_record_per_attempted_action_and_no_non_events
- Input: `backend/tests/test_broker_action_path.py::test_the_log_carries_one_record_per_attempted_action_and_no_non_events`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_log_carries_one_record_per_attempted_action_and_no_non_events PASSED [  8%]`

### Scenario: test_the_boundary_behaves_as_the_declared_inclusivity_says
- Input: `backend/tests/test_broker_action_path.py::test_the_boundary_behaves_as_the_declared_inclusivity_says`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_boundary_behaves_as_the_declared_inclusivity_says PASSED [  8%]`

### Scenario: test_a_shadow_rule_does_not_block_and_names_itself
- Input: `backend/tests/test_broker_action_path.py::test_a_shadow_rule_does_not_block_and_names_itself`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_shadow_rule_does_not_block_and_names_itself PASSED [  8%]`

### Scenario: test_an_unresolvable_bundle_denies_every_action_and_names_it
- Input: `backend/tests/test_broker_action_path.py::test_an_unresolvable_bundle_denies_every_action_and_names_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_unresolvable_bundle_denies_every_action_and_names_it PASSED [  8%]`

### Scenario: test_there_is_no_cached_bundle_fallback
- Input: `backend/tests/test_broker_action_path.py::test_there_is_no_cached_bundle_fallback`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_there_is_no_cached_bundle_fallback PASSED [  8%]`

### Scenario: test_a_rule_that_cannot_be_evaluated_denies
- Input: `backend/tests/test_broker_action_path.py::test_a_rule_that_cannot_be_evaluated_denies`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_rule_that_cannot_be_evaluated_denies PASSED [  8%]`

### Scenario: test_an_agent_principal_cannot_be_authorised_to_approve
- Input: `backend/tests/test_broker_action_path.py::test_an_agent_principal_cannot_be_authorised_to_approve`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_agent_principal_cannot_be_authorised_to_approve PASSED [  8%]`

### Scenario: test_the_human_act_rule_is_evidenced_even_though_the_set_test_gets_there_first
- Input: `backend/tests/test_broker_action_path.py::test_the_human_act_rule_is_evidenced_even_though_the_set_test_gets_there_first`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_human_act_rule_is_evidenced_even_though_the_set_test_gets_there_first PASSED [  8%]`

### Scenario: test_a_human_principal_may_approve
- Input: `backend/tests/test_broker_action_path.py::test_a_human_principal_may_approve`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_human_principal_may_approve PASSED [  8%]`

### Scenario: test_an_approval_with_no_authorship_context_is_unevaluable_and_denies
- Input: `backend/tests/test_broker_action_path.py::test_an_approval_with_no_authorship_context_is_unevaluable_and_denies`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_approval_with_no_authorship_context_is_unevaluable_and_denies PASSED [  8%]`

### Scenario: test_an_override_requires_two_distinct_human_authorisers
- Input: `backend/tests/test_broker_action_path.py::test_an_override_requires_two_distinct_human_authorisers`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_override_requires_two_distinct_human_authorisers PASSED [  8%]`

### Scenario: test_a_self_authorised_override_is_rejected
- Input: `backend/tests/test_broker_action_path.py::test_a_self_authorised_override_is_rejected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_self_authorised_override_is_rejected PASSED [  8%]`

### Scenario: test_the_same_identity_cannot_be_both_authorisers
- Input: `backend/tests/test_broker_action_path.py::test_the_same_identity_cannot_be_both_authorisers`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_same_identity_cannot_be_both_authorisers PASSED [  9%]`

### Scenario: test_an_override_authorised_by_the_agents_own_author_is_rejected
- Input: `backend/tests/test_broker_action_path.py::test_an_override_authorised_by_the_agents_own_author_is_rejected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_override_authorised_by_the_agents_own_author_is_rejected PASSED [  9%]`

### Scenario: test_an_agent_cannot_be_an_override_authoriser
- Input: `backend/tests/test_broker_action_path.py::test_an_agent_cannot_be_an_override_authoriser`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_agent_cannot_be_an_override_authoriser PASSED [  9%]`

### Scenario: test_a_reason_code_outside_the_closed_list_is_rejected
- Input: `backend/tests/test_broker_action_path.py::test_a_reason_code_outside_the_closed_list_is_rejected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_reason_code_outside_the_closed_list_is_rejected PASSED [  9%]`

### Scenario: test_a_standing_scope_is_unrepresentable[kwargs0]
- Input: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs0] PASSED [  9%]`

### Scenario: test_a_standing_scope_is_unrepresentable[kwargs1]
- Input: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs1] PASSED [  9%]`

### Scenario: test_an_open_ended_expiry_has_no_column_to_live_in
- Input: `backend/tests/test_broker_action_path.py::test_an_open_ended_expiry_has_no_column_to_live_in`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_open_ended_expiry_has_no_column_to_live_in PASSED [  9%]`

### Scenario: test_an_override_applies_to_exactly_one_action
- Input: `backend/tests/test_broker_action_path.py::test_an_override_applies_to_exactly_one_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_override_applies_to_exactly_one_action PASSED [  9%]`

### Scenario: test_an_override_belonging_to_another_requester_is_refused
- Input: `backend/tests/test_broker_action_path.py::test_an_override_belonging_to_another_requester_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_override_belonging_to_another_requester_is_refused PASSED [  9%]`

### Scenario: test_a_zero_override_period_renders_an_explicit_zero_with_its_denominator
- Input: `backend/tests/test_broker_action_path.py::test_a_zero_override_period_renders_an_explicit_zero_with_its_denominator`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_a_zero_override_period_renders_an_explicit_zero_with_its_denominator PASSED [  9%]`

### Scenario: test_an_exercised_override_is_visible_in_the_rate
- Input: `backend/tests/test_broker_action_path.py::test_an_exercised_override_is_visible_in_the_rate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_an_exercised_override_is_visible_in_the_rate PASSED [  9%]`

### Scenario: test_every_path_through_the_machine_terminates
- Input: `backend/tests/test_broker_action_path.py::test_every_path_through_the_machine_terminates`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_every_path_through_the_machine_terminates PASSED [  9%]`

### Scenario: test_the_machine_refuses_a_transition_it_does_not_have
- Input: `backend/tests/test_broker_action_path.py::test_the_machine_refuses_a_transition_it_does_not_have`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_the_machine_refuses_a_transition_it_does_not_have PASSED [  9%]`

### Scenario: test_capability_check_is_not_skippable
- Input: `backend/tests/test_broker_action_path.py::test_capability_check_is_not_skippable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_capability_check_is_not_skippable PASSED [  9%]`

### Scenario: test_no_second_authorisation_path_exists
- Input: `backend/tests/test_broker_action_path.py::test_no_second_authorisation_path_exists`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_action_path.py::test_no_second_authorisation_path_exists PASSED [ 10%]`

### Scenario: test_the_committed_bundle_compiles_and_is_hash_addressed
- Input: `backend/tests/test_broker_bundle.py::test_the_committed_bundle_compiles_and_is_hash_addressed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_the_committed_bundle_compiles_and_is_hash_addressed PASSED [ 10%]`

### Scenario: test_compilation_is_deterministic
- Input: `backend/tests/test_broker_bundle.py::test_compilation_is_deterministic`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_compilation_is_deterministic PASSED [ 10%]`

### Scenario: test_editing_a_rule_produces_a_different_hash
- Input: `backend/tests/test_broker_bundle.py::test_editing_a_rule_produces_a_different_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_editing_a_rule_produces_a_different_hash PASSED [ 10%]`

### Scenario: test_the_document_handed_out_is_a_copy_not_a_write_path
- Input: `backend/tests/test_broker_bundle.py::test_the_document_handed_out_is_a_copy_not_a_write_path`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_the_document_handed_out_is_a_copy_not_a_write_path PASSED [ 10%]`

### Scenario: test_a_missing_cap_fails_the_build[max_proposals_per_run]
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_proposals_per_run]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_proposals_per_run] PASSED [ 10%]`

### Scenario: test_a_missing_cap_fails_the_build[max_aggregate_value_per_agent_period]
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_aggregate_value_per_agent_period]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_aggregate_value_per_agent_period] PASSED [ 10%]`

### Scenario: test_a_missing_cap_fails_the_build[max_consecutive_same_account_periods]
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_consecutive_same_account_periods]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_consecutive_same_account_periods] PASSED [ 10%]`

### Scenario: test_a_missing_cap_fails_the_build[max_footprint_pct_of_account_balance]
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_footprint_pct_of_account_balance]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_footprint_pct_of_account_balance] PASSED [ 10%]`

### Scenario: test_a_missing_cap_fails_the_build[max_lines_per_export_batch]
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_lines_per_export_batch]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_lines_per_export_batch] PASSED [ 10%]`

### Scenario: test_a_null_cap_fails_the_build
- Input: `backend/tests/test_broker_bundle.py::test_a_null_cap_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_null_cap_fails_the_build PASSED [ 10%]`

### Scenario: test_a_cap_edited_toward_disabled_fails_the_build[unbounded]
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[unbounded]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[unbounded] PASSED [ 10%]`

### Scenario: test_a_cap_edited_toward_disabled_fails_the_build[none]
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[none]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[none] PASSED [ 10%]`

### Scenario: test_a_cap_edited_toward_disabled_fails_the_build[off]
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[off]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[off] PASSED [ 10%]`

### Scenario: test_a_cap_edited_toward_disabled_fails_the_build[disabled]
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[disabled]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[disabled] PASSED [ 10%]`

### Scenario: test_a_non_positive_cap_is_not_a_bound[0]
- Input: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[0] PASSED [ 11%]`

### Scenario: test_a_non_positive_cap_is_not_a_bound[-1]
- Input: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[-1] PASSED [ 11%]`

### Scenario: test_an_unknown_cap_name_fails_rather_than_being_ignored
- Input: `backend/tests/test_broker_bundle.py::test_an_unknown_cap_name_fails_rather_than_being_ignored`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_an_unknown_cap_name_fails_rather_than_being_ignored PASSED [ 11%]`

### Scenario: test_a_compiled_bundle_offers_no_runtime_write_path_to_its_caps
- Input: `backend/tests/test_broker_bundle.py::test_a_compiled_bundle_offers_no_runtime_write_path_to_its_caps`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_compiled_bundle_offers_no_runtime_write_path_to_its_caps PASSED [ 11%]`

### Scenario: test_a_rule_missing_a_fixture_fails_the_bundle_not_just_the_suite
- Input: `backend/tests/test_broker_bundle.py::test_a_rule_missing_a_fixture_fails_the_bundle_not_just_the_suite`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_rule_missing_a_fixture_fails_the_bundle_not_just_the_suite PASSED [ 11%]`

### Scenario: test_a_fixture_file_that_does_not_exist_fails_the_build
- Input: `backend/tests/test_broker_bundle.py::test_a_fixture_file_that_does_not_exist_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_fixture_file_that_does_not_exist_fails_the_build PASSED [ 11%]`

### Scenario: test_a_firing_fixture_that_does_not_fire_fails_the_build
- Input: `backend/tests/test_broker_bundle.py::test_a_firing_fixture_that_does_not_fire_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_firing_fixture_that_does_not_fire_fails_the_build PASSED [ 11%]`

### Scenario: test_a_non_firing_fixture_that_fires_fails_the_build
- Input: `backend/tests/test_broker_bundle.py::test_a_non_firing_fixture_that_fires_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_non_firing_fixture_that_fires_fails_the_build PASSED [ 11%]`

### Scenario: test_a_predicate_naming_an_unknown_field_fails_the_build
- Input: `backend/tests/test_broker_bundle.py::test_a_predicate_naming_an_unknown_field_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_predicate_naming_an_unknown_field_fails_the_build PASSED [ 11%]`

### Scenario: test_a_quantitative_rule_must_declare_its_inclusivity
- Input: `backend/tests/test_broker_bundle.py::test_a_quantitative_rule_must_declare_its_inclusivity`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_quantitative_rule_must_declare_its_inclusivity PASSED [ 11%]`

### Scenario: test_duplicate_rule_ids_fail_the_build
- Input: `backend/tests/test_broker_bundle.py::test_duplicate_rule_ids_fail_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_duplicate_rule_ids_fail_the_build PASSED [ 11%]`

### Scenario: test_an_absent_capability_allowlist_is_not_an_empty_one
- Input: `backend/tests/test_broker_bundle.py::test_an_absent_capability_allowlist_is_not_an_empty_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_an_absent_capability_allowlist_is_not_an_empty_one PASSED [ 11%]`

### Scenario: test_an_empty_allowlist_compiles_and_denies_everything
- Input: `backend/tests/test_broker_bundle.py::test_an_empty_allowlist_compiles_and_denies_everything`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_an_empty_allowlist_compiles_and_denies_everything PASSED [ 11%]`

### Scenario: test_the_routing_budget_must_live_in_the_bundle
- Input: `backend/tests/test_broker_bundle.py::test_the_routing_budget_must_live_in_the_bundle`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_the_routing_budget_must_live_in_the_bundle PASSED [ 11%]`

### Scenario: test_first_publication_is_classified_risk_increasing
- Input: `backend/tests/test_broker_bundle.py::test_first_publication_is_classified_risk_increasing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_first_publication_is_classified_risk_increasing PASSED [ 12%]`

### Scenario: test_widening_a_threshold_is_classified_risk_increasing_by_the_system
- Input: `backend/tests/test_broker_bundle.py::test_widening_a_threshold_is_classified_risk_increasing_by_the_system`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_widening_a_threshold_is_classified_risk_increasing_by_the_system PASSED [ 12%]`

### Scenario: test_raising_a_cap_is_classified_risk_increasing
- Input: `backend/tests/test_broker_bundle.py::test_raising_a_cap_is_classified_risk_increasing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_raising_a_cap_is_classified_risk_increasing PASSED [ 12%]`

### Scenario: test_broadening_the_allowlist_is_classified_risk_increasing
- Input: `backend/tests/test_broker_bundle.py::test_broadening_the_allowlist_is_classified_risk_increasing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_broadening_the_allowlist_is_classified_risk_increasing PASSED [ 12%]`

### Scenario: test_moving_a_rule_from_enforce_to_shadow_is_risk_increasing
- Input: `backend/tests/test_broker_bundle.py::test_moving_a_rule_from_enforce_to_shadow_is_risk_increasing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_moving_a_rule_from_enforce_to_shadow_is_risk_increasing PASSED [ 12%]`

### Scenario: test_removing_a_rule_is_risk_increasing
- Input: `backend/tests/test_broker_bundle.py::test_removing_a_rule_is_risk_increasing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_removing_a_rule_is_risk_increasing PASSED [ 12%]`

### Scenario: test_a_tightening_diff_is_not_risk_increasing_but_is_still_a_change
- Input: `backend/tests/test_broker_bundle.py::test_a_tightening_diff_is_not_risk_increasing_but_is_still_a_change`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_tightening_diff_is_not_risk_increasing_but_is_still_a_change PASSED [ 12%]`

### Scenario: test_a_zero_change_diff_is_detected_as_such
- Input: `backend/tests/test_broker_bundle.py::test_a_zero_change_diff_is_detected_as_such`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_zero_change_diff_is_detected_as_such PASSED [ 12%]`

### Scenario: test_a_structural_predicate_change_is_never_assumed_to_be_a_tightening
- Input: `backend/tests/test_broker_bundle.py::test_a_structural_predicate_change_is_never_assumed_to_be_a_tightening`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_bundle.py::test_a_structural_predicate_change_is_never_assumed_to_be_a_tightening PASSED [ 12%]`

### Scenario: test_a_clean_emission_is_allowed_and_records_one_decision
- Input: `backend/tests/test_broker_emission_path.py::test_a_clean_emission_is_allowed_and_records_one_decision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_a_clean_emission_is_allowed_and_records_one_decision PASSED [ 12%]`

### Scenario: test_the_emission_shares_the_action_legs_bundle_hash_and_id_scheme
- Input: `backend/tests/test_broker_emission_path.py::test_the_emission_shares_the_action_legs_bundle_hash_and_id_scheme`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_the_emission_shares_the_action_legs_bundle_hash_and_id_scheme PASSED [ 12%]`

### Scenario: test_an_emission_capability_absent_from_the_allowlist_is_denied
- Input: `backend/tests/test_broker_emission_path.py::test_an_emission_capability_absent_from_the_allowlist_is_denied`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_emission_capability_absent_from_the_allowlist_is_denied PASSED [ 12%]`

### Scenario: test_the_skill_allowlist_narrows_emissions_too
- Input: `backend/tests/test_broker_emission_path.py::test_the_skill_allowlist_narrows_emissions_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_the_skill_allowlist_narrows_emissions_too PASSED [ 12%]`

### Scenario: test_an_unresolvable_bundle_denies_every_emission
- Input: `backend/tests/test_broker_emission_path.py::test_an_unresolvable_bundle_denies_every_emission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_unresolvable_bundle_denies_every_emission PASSED [ 12%]`

### Scenario: test_decide_emission_has_no_override_parameter
- Input: `backend/tests/test_broker_emission_path.py::test_decide_emission_has_no_override_parameter`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_decide_emission_has_no_override_parameter PASSED [ 13%]`

### Scenario: test_no_emission_decision_ever_carries_an_override_reference
- Input: `backend/tests/test_broker_emission_path.py::test_no_emission_decision_ever_carries_an_override_reference`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_no_emission_decision_ever_carries_an_override_reference PASSED [ 13%]`

### Scenario: test_g_cite_a_an_uncited_classification_is_not_emitted
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_a_an_uncited_classification_is_not_emitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_a_an_uncited_classification_is_not_emitted PASSED [ 13%]`

### Scenario: test_g_cite_b_the_residual_after_citation_may_not_be_zero_by_omission
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_b_the_residual_after_citation_may_not_be_zero_by_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_b_the_residual_after_citation_may_not_be_zero_by_omission PASSED [ 13%]`

### Scenario: test_g_cite_c_the_treatment_claim_must_carry_its_own_ground
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_the_treatment_claim_must_carry_its_own_ground`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_c_the_treatment_claim_must_carry_its_own_ground PASSED [ 13%]`

### Scenario: test_g_cite_c_rejects_a_size_shaped_treatment_ground[magnitude]
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[magnitude]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[magnitude] PASSED [ 13%]`

### Scenario: test_g_cite_c_rejects_a_size_shaped_treatment_ground[threshold]
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[threshold]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[threshold] PASSED [ 13%]`

### Scenario: test_g_cite_c_rejects_a_size_shaped_treatment_ground[none]
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[none]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[none] PASSED [ 13%]`

### Scenario: test_g_cite_c_rejects_a_size_shaped_treatment_ground[]
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[] PASSED [ 13%]`

### Scenario: test_g_restate_prior_period_treatment_is_context_never_evidence
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_prior_period_treatment_is_context_never_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restate_prior_period_treatment_is_context_never_evidence PASSED [ 13%]`

### Scenario: test_g_restate_the_same_emission_passes_on_its_own_ground
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_the_same_emission_passes_on_its_own_ground`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restate_the_same_emission_passes_on_its_own_ground PASSED [ 13%]`

### Scenario: test_g_restate_third_consecutive_restatement_escalates_rather_than_denies
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_third_consecutive_restatement_escalates_rather_than_denies`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restate_third_consecutive_restatement_escalates_rather_than_denies PASSED [ 13%]`

### Scenario: test_g_restate_second_consecutive_restatement_does_not_escalate
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_second_consecutive_restatement_does_not_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restate_second_consecutive_restatement_does_not_escalate PASSED [ 13%]`

### Scenario: test_g_noex_an_absence_claim_over_partial_coverage_is_not_emitted
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_partial_coverage_is_not_emitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_partial_coverage_is_not_emitted PASSED [ 13%]`

### Scenario: test_g_noex_an_absence_claim_over_stale_but_full_coverage_is_declined
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_stale_but_full_coverage_is_declined`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_stale_but_full_coverage_is_declined PASSED [ 14%]`

### Scenario: test_g_noex_fires_as_a_denial_when_the_rule_is_reached_directly
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_fires_as_a_denial_when_the_rule_is_reached_directly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_noex_fires_as_a_denial_when_the_rule_is_reached_directly PASSED [ 14%]`

### Scenario: test_g_restype_a_declared_type_without_its_evidence_schema_declines
- Input: `backend/tests/test_broker_emission_path.py::test_g_restype_a_declared_type_without_its_evidence_schema_declines`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restype_a_declared_type_without_its_evidence_schema_declines PASSED [ 14%]`

### Scenario: test_g_restype_the_rule_still_fires_on_its_own_context
- Input: `backend/tests/test_broker_emission_path.py::test_g_restype_the_rule_still_fires_on_its_own_context`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_restype_the_rule_still_fires_on_its_own_context PASSED [ 14%]`

### Scenario: test_g_conf_materiality_markers_are_rejected_unconditionally[immaterial]
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[immaterial]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[immaterial] PASSED [ 14%]`

### Scenario: test_g_conf_materiality_markers_are_rejected_unconditionally[not_significant]
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[not_significant]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[not_significant] PASSED [ 14%]`

### Scenario: test_g_conf_materiality_markers_are_rejected_unconditionally[de_minimis]
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[de_minimis]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[de_minimis] PASSED [ 14%]`

### Scenario: test_g_conf_materiality_markers_are_rejected_unconditionally[below_threshold_no_action_needed]
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[below_threshold_no_action_needed]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[below_threshold_no_action_needed] PASSED [ 14%]`

### Scenario: test_g_conf_verified_requires_a_verification_record
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_verified_requires_a_verification_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_verified_requires_a_verification_record PASSED [ 14%]`

### Scenario: test_g_conf_confirmed_requires_a_two_sided_tie
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_confirmed_requires_a_two_sided_tie`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_confirmed_requires_a_two_sided_tie PASSED [ 14%]`

### Scenario: test_g_conf_does_not_constrain_how_well_the_agent_explains
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_does_not_constrain_how_well_the_agent_explains`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_conf_does_not_constrain_how_well_the_agent_explains PASSED [ 14%]`

### Scenario: test_g_selfref_the_agent_output_namespace_is_inadmissible
- Input: `backend/tests/test_broker_emission_path.py::test_g_selfref_the_agent_output_namespace_is_inadmissible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_selfref_the_agent_output_namespace_is_inadmissible PASSED [ 14%]`

### Scenario: test_g_selfref_a_human_disposition_is_admissible
- Input: `backend/tests/test_broker_emission_path.py::test_g_selfref_a_human_disposition_is_admissible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_selfref_a_human_disposition_is_admissible PASSED [ 14%]`

### Scenario: test_g_nohuman_asserted_agreement_needs_a_disposition_record
- Input: `backend/tests/test_broker_emission_path.py::test_g_nohuman_asserted_agreement_needs_a_disposition_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_nohuman_asserted_agreement_needs_a_disposition_record PASSED [ 14%]`

### Scenario: test_g_scope_drift_a_reference_outside_declared_scope_is_a_failure_not_a_caveat
- Input: `backend/tests/test_broker_emission_path.py::test_g_scope_drift_a_reference_outside_declared_scope_is_a_failure_not_a_caveat`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_scope_drift_a_reference_outside_declared_scope_is_a_failure_not_a_caveat PASSED [ 14%]`

### Scenario: test_g_inject_unquoted_ledger_text_is_not_emitted
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_unquoted_ledger_text_is_not_emitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_inject_unquoted_ledger_text_is_not_emitted PASSED [ 15%]`

### Scenario: test_g_inject_quoted_ledger_text_carrying_its_source_row_is_fine
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_quoted_ledger_text_carrying_its_source_row_is_fine`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_inject_quoted_ledger_text_carrying_its_source_row_is_fine PASSED [ 15%]`

### Scenario: test_g_inject_authorisation_leg_no_data_field_can_widen_a_capability
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_authorisation_leg_no_data_field_can_widen_a_capability`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_g_inject_authorisation_leg_no_data_field_can_widen_a_capability PASSED [ 15%]`

### Scenario: test_every_one_of_the_nine_guardrails_has_at_least_one_rule
- Input: `backend/tests/test_broker_emission_path.py::test_every_one_of_the_nine_guardrails_has_at_least_one_rule`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_every_one_of_the_nine_guardrails_has_at_least_one_rule PASSED [ 15%]`

### Scenario: test_every_emission_rule_names_its_guardrail
- Input: `backend/tests/test_broker_emission_path.py::test_every_emission_rule_names_its_guardrail`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_every_emission_rule_names_its_guardrail PASSED [ 15%]`

### Scenario: test_an_unevaluable_emission_check_denies_naming_the_check
- Input: `backend/tests/test_broker_emission_path.py::test_an_unevaluable_emission_check_denies_naming_the_check`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_unevaluable_emission_check_denies_naming_the_check PASSED [ 15%]`

### Scenario: test_ab3_out_of_population_returns_a_typed_decline_not_silence
- Input: `backend/tests/test_broker_emission_path.py::test_ab3_out_of_population_returns_a_typed_decline_not_silence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab3_out_of_population_returns_a_typed_decline_not_silence PASSED [ 15%]`

### Scenario: test_ab5_an_evidential_tie_is_reported_as_a_tie
- Input: `backend/tests/test_broker_emission_path.py::test_ab5_an_evidential_tie_is_reported_as_a_tie`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab5_an_evidential_tie_is_reported_as_a_tie PASSED [ 15%]`

### Scenario: test_ab5_takes_precedence_over_ab1
- Input: `backend/tests/test_broker_emission_path.py::test_ab5_takes_precedence_over_ab1`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab5_takes_precedence_over_ab1 PASSED [ 15%]`

### Scenario: test_ab6_conflicting_sources_are_named
- Input: `backend/tests/test_broker_emission_path.py::test_ab6_conflicting_sources_are_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab6_conflicting_sources_are_named PASSED [ 15%]`

### Scenario: test_ab1_evidence_schema_unsatisfied
- Input: `backend/tests/test_broker_emission_path.py::test_ab1_evidence_schema_unsatisfied`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab1_evidence_schema_unsatisfied PASSED [ 15%]`

### Scenario: test_ab2_coverage_or_staleness
- Input: `backend/tests/test_broker_emission_path.py::test_ab2_coverage_or_staleness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab2_coverage_or_staleness PASSED [ 15%]`

### Scenario: test_ab4_a_refused_emission_abstains_and_its_evidence_is_never_examined
- Input: `backend/tests/test_broker_emission_path.py::test_ab4_a_refused_emission_abstains_and_its_evidence_is_never_examined`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_ab4_a_refused_emission_abstains_and_its_evidence_is_never_examined PASSED [ 15%]`

### Scenario: test_all_six_abstention_types_are_reachable_through_the_broker
- Input: `backend/tests/test_broker_emission_path.py::test_all_six_abstention_types_are_reachable_through_the_broker`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_all_six_abstention_types_are_reachable_through_the_broker PASSED [ 15%]`

### Scenario: test_no_abstention_produced_by_the_broker_renders_as_a_negative_finding
- Input: `backend/tests/test_broker_emission_path.py::test_no_abstention_produced_by_the_broker_renders_as_a_negative_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_no_abstention_produced_by_the_broker_renders_as_a_negative_finding PASSED [ 16%]`

### Scenario: test_an_abstention_is_stored_as_abstain_not_as_deny
- Input: `backend/tests/test_broker_emission_path.py::test_an_abstention_is_stored_as_abstain_not_as_deny`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_abstention_is_stored_as_abstain_not_as_deny PASSED [ 16%]`

### Scenario: test_an_abstention_object_exists_on_the_decision_and_absent_otherwise
- Input: `backend/tests/test_broker_emission_path.py::test_an_abstention_object_exists_on_the_decision_and_absent_otherwise`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_abstention_object_exists_on_the_decision_and_absent_otherwise PASSED [ 16%]`

### Scenario: test_a_clean_request_triggers_no_abstention
- Input: `backend/tests/test_broker_emission_path.py::test_a_clean_request_triggers_no_abstention`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_a_clean_request_triggers_no_abstention PASSED [ 16%]`

### Scenario: test_the_trigger_precedence_is_ab3_ab5_ab6_ab1_ab2
- Input: `backend/tests/test_broker_emission_path.py::test_the_trigger_precedence_is_ab3_ab5_ab6_ab1_ab2`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_the_trigger_precedence_is_ab3_ab5_ab6_ab1_ab2 PASSED [ 16%]`

### Scenario: test_every_trigger_names_a_gap_and_exactly_one_resolving_action
- Input: `backend/tests/test_broker_emission_path.py::test_every_trigger_names_a_gap_and_exactly_one_resolving_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_every_trigger_names_a_gap_and_exactly_one_resolving_action PASSED [ 16%]`

### Scenario: test_an_unknown_emission_field_is_refused_at_construction
- Input: `backend/tests/test_broker_emission_path.py::test_an_unknown_emission_field_is_refused_at_construction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_an_unknown_emission_field_is_refused_at_construction PASSED [ 16%]`

### Scenario: test_there_is_no_field_on_which_the_agent_reports_its_own_compliance
- Input: `backend/tests/test_broker_emission_path.py::test_there_is_no_field_on_which_the_agent_reports_its_own_compliance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_emission_path.py::test_there_is_no_field_on_which_the_agent_reports_its_own_compliance PASSED [ 16%]`

### Scenario: test_comparison_membership_and_boolean_composition
- Input: `backend/tests/test_broker_expr.py::test_comparison_membership_and_boolean_composition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_comparison_membership_and_boolean_composition PASSED [ 16%]`

### Scenario: test_threshold_boundary_is_exact_because_money_is_decimal
- Input: `backend/tests/test_broker_expr.py::test_threshold_boundary_is_exact_because_money_is_decimal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_threshold_boundary_is_exact_because_money_is_decimal PASSED [ 16%]`

### Scenario: test_arithmetic_and_negation
- Input: `backend/tests/test_broker_expr.py::test_arithmetic_and_negation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_arithmetic_and_negation PASSED   [ 16%]`

### Scenario: test_effective_bound_fields_are_reported
- Input: `backend/tests/test_broker_expr.py::test_effective_bound_fields_are_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_effective_bound_fields_are_reported PASSED [ 16%]`

### Scenario: test_unknown_field_fails_at_compile_time_not_silently_at_runtime
- Input: `backend/tests/test_broker_expr.py::test_unknown_field_fails_at_compile_time_not_silently_at_runtime`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_unknown_field_fails_at_compile_time_not_silently_at_runtime PASSED [ 16%]`

### Scenario: test_a_typo_would_otherwise_produce_a_rule_that_never_fires
- Input: `backend/tests/test_broker_expr.py::test_a_typo_would_otherwise_produce_a_rule_that_never_fires`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_a_typo_would_otherwise_produce_a_rule_that_never_fires PASSED [ 16%]`

### Scenario: test_the_language_cannot_reach_python[__import__('os').system('true')]
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[__import__('os').system('true')]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[__import__('os').system('true')] PASSED [ 17%]`

### Scenario: test_the_language_cannot_reach_python[action.kind.__class__]
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind.__class__]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind.__class__] PASSED [ 17%]`

### Scenario: test_the_language_cannot_reach_python[open('/etc/passwd')]
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[open('/etc/passwd')]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[open('/etc/passwd')] PASSED [ 17%]`

### Scenario: test_the_language_cannot_reach_python[lambda
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[lambda`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[lambda x: x] PASSED [ 17%]`

### Scenario: test_the_language_cannot_reach_python[[i
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[[i`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[[i for i in range(3)]] PASSED [ 17%]`

### Scenario: test_the_language_cannot_reach_python[action.kind
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind = 'x'] PASSED [ 17%]`

### Scenario: test_only_the_three_named_constructors_are_callable
- Input: `backend/tests/test_broker_expr.py::test_only_the_three_named_constructors_are_callable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_only_the_three_named_constructors_are_callable PASSED [ 17%]`

### Scenario: test_float_is_refused_rather_than_silently_compared
- Input: `backend/tests/test_broker_expr.py::test_float_is_refused_rather_than_silently_compared`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_float_is_refused_rather_than_silently_compared PASSED [ 17%]`

### Scenario: test_empty_predicate_is_not_a_predicate
- Input: `backend/tests/test_broker_expr.py::test_empty_predicate_is_not_a_predicate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_empty_predicate_is_not_a_predicate PASSED [ 17%]`

### Scenario: test_non_boolean_result_is_a_type_error_not_a_truthy_pass
- Input: `backend/tests/test_broker_expr.py::test_non_boolean_result_is_a_type_error_not_a_truthy_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_non_boolean_result_is_a_type_error_not_a_truthy_pass PASSED [ 17%]`

### Scenario: test_absent_context_field_is_unevaluable_and_not_false
- Input: `backend/tests/test_broker_expr.py::test_absent_context_field_is_unevaluable_and_not_false`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_absent_context_field_is_unevaluable_and_not_false PASSED [ 17%]`

### Scenario: test_null_is_not_silently_false
- Input: `backend/tests/test_broker_expr.py::test_null_is_not_silently_false`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_null_is_not_silently_false PASSED [ 17%]`

### Scenario: test_in_requires_a_list_on_the_right
- Input: `backend/tests/test_broker_expr.py::test_in_requires_a_list_on_the_right`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_in_requires_a_list_on_the_right PASSED [ 17%]`

### Scenario: test_trailing_tokens_are_a_syntax_error
- Input: `backend/tests/test_broker_expr.py::test_trailing_tokens_are_a_syntax_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_trailing_tokens_are_a_syntax_error PASSED [ 17%]`

### Scenario: test_unbalanced_parenthesis_is_a_syntax_error
- Input: `backend/tests/test_broker_expr.py::test_unbalanced_parenthesis_is_a_syntax_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_unbalanced_parenthesis_is_a_syntax_error PASSED [ 17%]`

### Scenario: test_division_by_zero_is_an_evaluation_error
- Input: `backend/tests/test_broker_expr.py::test_division_by_zero_is_an_evaluation_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_division_by_zero_is_an_evaluation_error PASSED [ 18%]`

### Scenario: test_subset_of_holds_only_when_every_member_is_admissible
- Input: `backend/tests/test_broker_expr.py::test_subset_of_holds_only_when_every_member_is_admissible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_subset_of_holds_only_when_every_member_is_admissible PASSED [ 18%]`

### Scenario: test_the_empty_list_is_a_subset_and_that_is_deliberate
- Input: `backend/tests/test_broker_expr.py::test_the_empty_list_is_a_subset_and_that_is_deliberate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_empty_list_is_a_subset_and_that_is_deliberate PASSED [ 18%]`

### Scenario: test_intersects_is_true_on_any_overlap_and_false_on_none
- Input: `backend/tests/test_broker_expr.py::test_intersects_is_true_on_any_overlap_and_false_on_none`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_intersects_is_true_on_any_overlap_and_false_on_none PASSED [ 18%]`

### Scenario: test_a_set_operator_against_a_scalar_is_unevaluable_not_false
- Input: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_scalar_is_unevaluable_not_false`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_scalar_is_unevaluable_not_false PASSED [ 18%]`

### Scenario: test_a_set_operator_against_a_missing_field_is_unevaluable_not_false
- Input: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_missing_field_is_unevaluable_not_false`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_missing_field_is_unevaluable_not_false PASSED [ 18%]`

### Scenario: test_the_new_operators_are_operators_not_values
- Input: `backend/tests/test_broker_expr.py::test_the_new_operators_are_operators_not_values`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_new_operators_are_operators_not_values PASSED [ 18%]`

### Scenario: test_the_new_operators_still_bind_against_the_declared_schema
- Input: `backend/tests/test_broker_expr.py::test_the_new_operators_still_bind_against_the_declared_schema`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_broker_expr.py::test_the_new_operators_still_bind_against_the_declared_schema PASSED [ 18%]`

### Scenario: test_the_author_of_a_rule_change_may_not_publish_the_bundle
- Input: `backend/tests/test_bundle_publication.py::test_the_author_of_a_rule_change_may_not_publish_the_bundle`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_the_author_of_a_rule_change_may_not_publish_the_bundle PASSED [ 18%]`

### Scenario: test_a_rejected_publication_leaves_the_prior_bundle_in_force
- Input: `backend/tests/test_bundle_publication.py::test_a_rejected_publication_leaves_the_prior_bundle_in_force`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_rejected_publication_leaves_the_prior_bundle_in_force PASSED [ 18%]`

### Scenario: test_the_rejection_is_recorded_as_a_control_event
- Input: `backend/tests/test_bundle_publication.py::test_the_rejection_is_recorded_as_a_control_event`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_the_rejection_is_recorded_as_a_control_event PASSED [ 18%]`

### Scenario: test_the_classification_names_the_specific_fields_that_triggered_it
- Input: `backend/tests/test_bundle_publication.py::test_the_classification_names_the_specific_fields_that_triggered_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_the_classification_names_the_specific_fields_that_triggered_it PASSED [ 18%]`

### Scenario: test_publication_does_not_complete_without_acknowledgement
- Input: `backend/tests/test_bundle_publication.py::test_publication_does_not_complete_without_acknowledgement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_publication_does_not_complete_without_acknowledgement PASSED [ 18%]`

### Scenario: test_acknowledging_a_different_classification_does_not_count
- Input: `backend/tests/test_bundle_publication.py::test_acknowledging_a_different_classification_does_not_count`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_acknowledging_a_different_classification_does_not_count PASSED [ 18%]`

### Scenario: test_a_risk_increasing_publication_records_its_fields
- Input: `backend/tests/test_bundle_publication.py::test_a_risk_increasing_publication_records_its_fields`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_risk_increasing_publication_records_its_fields PASSED [ 19%]`

### Scenario: test_a_tightening_diff_still_requires_two_distinct_identities
- Input: `backend/tests/test_bundle_publication.py::test_a_tightening_diff_still_requires_two_distinct_identities`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_tightening_diff_still_requires_two_distinct_identities PASSED [ 19%]`

### Scenario: test_a_zero_change_submission_is_rejected
- Input: `backend/tests/test_bundle_publication.py::test_a_zero_change_submission_is_rejected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_zero_change_submission_is_rejected PASSED [ 19%]`

### Scenario: test_the_first_run_reports_every_fixture_and_is_not_a_pass
- Input: `backend/tests/test_bundle_publication.py::test_the_first_run_reports_every_fixture_and_is_not_a_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_the_first_run_reports_every_fixture_and_is_not_a_pass PASSED [ 19%]`

### Scenario: test_a_second_run_with_a_baseline_passes
- Input: `backend/tests/test_bundle_publication.py::test_a_second_run_with_a_baseline_passes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_second_run_with_a_baseline_passes PASSED [ 19%]`

### Scenario: test_a_fixture_that_stops_firing_is_a_failure_naming_the_prior_run
- Input: `backend/tests/test_bundle_publication.py::test_a_fixture_that_stops_firing_is_a_failure_naming_the_prior_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_fixture_that_stops_firing_is_a_failure_naming_the_prior_run PASSED [ 19%]`

### Scenario: test_the_baseline_is_not_updated_by_the_run_that_observed_the_change
- Input: `backend/tests/test_bundle_publication.py::test_the_baseline_is_not_updated_by_the_run_that_observed_the_change`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_the_baseline_is_not_updated_by_the_run_that_observed_the_change PASSED [ 19%]`

### Scenario: test_a_missing_fixture_is_reported_by_name_as_unevidenced
- Input: `backend/tests/test_bundle_publication.py::test_a_missing_fixture_is_reported_by_name_as_unevidenced`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_missing_fixture_is_reported_by_name_as_unevidenced PASSED [ 19%]`

### Scenario: test_a_not_passed_run_raises_a_control_event
- Input: `backend/tests/test_bundle_publication.py::test_a_not_passed_run_raises_a_control_event`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_bundle_publication.py::test_a_not_passed_run_raises_a_control_event PASSED [ 19%]`

### Scenario: test_key_order_does_not_change_the_hash
- Input: `backend/tests/test_canonical.py::test_key_order_does_not_change_the_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_key_order_does_not_change_the_hash PASSED [ 19%]`

### Scenario: test_nested_key_order_does_not_change_the_hash
- Input: `backend/tests/test_canonical.py::test_nested_key_order_does_not_change_the_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_nested_key_order_does_not_change_the_hash PASSED [ 19%]`

### Scenario: test_list_order_does_change_the_hash
- Input: `backend/tests/test_canonical.py::test_list_order_does_change_the_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_list_order_does_change_the_hash PASSED [ 19%]`

### Scenario: test_decimals_serialise_as_plain_strings
- Input: `backend/tests/test_canonical.py::test_decimals_serialise_as_plain_strings`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_decimals_serialise_as_plain_strings PASSED [ 19%]`

### Scenario: test_a_float_raises_rather_than_hashing_irreproducibly
- Input: `backend/tests/test_canonical.py::test_a_float_raises_rather_than_hashing_irreproducibly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_a_float_raises_rather_than_hashing_irreproducibly PASSED [ 19%]`

### Scenario: test_a_nested_float_also_raises
- Input: `backend/tests/test_canonical.py::test_a_nested_float_also_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_a_nested_float_also_raises PASSED  [ 20%]`

### Scenario: test_tuples_and_lists_canonicalise_alike
- Input: `backend/tests/test_canonical.py::test_tuples_and_lists_canonicalise_alike`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_tuples_and_lists_canonicalise_alike PASSED [ 20%]`

### Scenario: test_unicode_is_not_escaped
- Input: `backend/tests/test_canonical.py::test_unicode_is_not_escaped`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_unicode_is_not_escaped PASSED      [ 20%]`

### Scenario: test_hash_bytes_is_sha256
- Input: `backend/tests/test_canonical.py::test_hash_bytes_is_sha256`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_canonical.py::test_hash_bytes_is_sha256 PASSED        [ 20%]`

### Scenario: test_a_certified_query_executes_and_carries_its_provenance
- Input: `backend/tests/test_certified_query_execution.py::test_a_certified_query_executes_and_carries_its_provenance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_certified_query_executes_and_carries_its_provenance PASSED [ 20%]`

### Scenario: test_amounts_come_back_as_text_not_float
- Input: `backend/tests/test_certified_query_execution.py::test_amounts_come_back_as_text_not_float`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_amounts_come_back_as_text_not_float PASSED [ 20%]`

### Scenario: test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[SELECT
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[SELECT`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[SELECT * FROM gl_je_lines] PASSED [ 20%]`

### Scenario: test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[gl.entries_by_recurrence;
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[gl.entries_by_recurrence;`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[gl.entries_by_recurrence; DROP TABLE gl_je_lines] PASSED [ 20%]`

### Scenario: test_a_sql_string_in_the_query_id_is_simply_an_unknown_query['
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query['`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[' OR 1=1 --] PASSED [ 20%]`

### Scenario: test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[]
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[] PASSED [ 20%]`

### Scenario: test_the_request_model_forbids_an_extra_field
- Input: `backend/tests/test_certified_query_execution.py::test_the_request_model_forbids_an_extra_field`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_request_model_forbids_an_extra_field PASSED [ 20%]`

### Scenario: test_no_field_of_the_request_model_can_carry_a_statement
- Input: `backend/tests/test_certified_query_execution.py::test_no_field_of_the_request_model_can_carry_a_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_no_field_of_the_request_model_can_carry_a_statement PASSED [ 20%]`

### Scenario: test_a_sql_string_bound_as_a_parameter_value_is_type_rejected
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_bound_as_a_parameter_value_is_type_rejected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_bound_as_a_parameter_value_is_type_rejected PASSED [ 20%]`

### Scenario: test_a_sql_string_in_a_string_parameter_is_bound_not_interpreted
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_a_string_parameter_is_bound_not_interpreted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_a_string_parameter_is_bound_not_interpreted PASSED [ 20%]`

### Scenario: test_personal_data_query_is_refused_before_execution_for_the_unentitled
- Input: `backend/tests/test_certified_query_execution.py::test_personal_data_query_is_refused_before_execution_for_the_unentitled`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_personal_data_query_is_refused_before_execution_for_the_unentitled PASSED [ 21%]`

### Scenario: test_the_same_query_executes_for_an_entitled_principal
- Input: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_for_an_entitled_principal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_for_an_entitled_principal PASSED [ 21%]`

### Scenario: test_entitlement_is_checked_before_parameter_validation
- Input: `backend/tests/test_certified_query_execution.py::test_entitlement_is_checked_before_parameter_validation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_entitlement_is_checked_before_parameter_validation PASSED [ 21%]`

### Scenario: test_no_agent_principal_holds_the_personal_data_entitlement
- Input: `backend/tests/test_certified_query_execution.py::test_no_agent_principal_holds_the_personal_data_entitlement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_no_agent_principal_holds_the_personal_data_entitlement PASSED [ 21%]`

### Scenario: test_model_bound_run_over_an_unclassified_column_is_refused_by_name
- Input: `backend/tests/test_certified_query_execution.py::test_model_bound_run_over_an_unclassified_column_is_refused_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_model_bound_run_over_an_unclassified_column_is_refused_by_name PASSED [ 21%]`

### Scenario: test_the_same_query_executes_on_a_non_model_bound_path
- Input: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_on_a_non_model_bound_path`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_on_a_non_model_bound_path PASSED [ 21%]`

### Scenario: test_a_model_bound_run_over_an_ineligible_query_is_refused
- Input: `backend/tests/test_certified_query_execution.py::test_a_model_bound_run_over_an_ineligible_query_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_model_bound_run_over_an_ineligible_query_is_refused PASSED [ 21%]`

### Scenario: test_a_missing_required_parameter_is_named
- Input: `backend/tests/test_certified_query_execution.py::test_a_missing_required_parameter_is_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_missing_required_parameter_is_named PASSED [ 21%]`

### Scenario: test_an_undeclared_parameter_is_named
- Input: `backend/tests/test_certified_query_execution.py::test_an_undeclared_parameter_is_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_an_undeclared_parameter_is_named PASSED [ 21%]`

### Scenario: test_a_period_outside_its_domain_is_refused[0]
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[0] PASSED [ 21%]`

### Scenario: test_a_period_outside_its_domain_is_refused[13]
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[13]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[13] PASSED [ 21%]`

### Scenario: test_a_period_outside_its_domain_is_refused[-1]
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[-1] PASSED [ 21%]`

### Scenario: test_a_period_outside_its_domain_is_refused[99]
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[99]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[99] PASSED [ 21%]`

### Scenario: test_the_period_domain_boundaries_are_inclusive[1]
- Input: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[1] PASSED [ 21%]`

### Scenario: test_the_period_domain_boundaries_are_inclusive[12]
- Input: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[12]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[12] PASSED [ 21%]`

### Scenario: test_a_bool_is_rejected_by_the_request_model_before_the_executor
- Input: `backend/tests/test_certified_query_execution.py::test_a_bool_is_rejected_by_the_request_model_before_the_executor`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_bool_is_rejected_by_the_request_model_before_the_executor PASSED [ 22%]`

### Scenario: test_a_numeric_string_is_not_silently_coerced_to_an_int
- Input: `backend/tests/test_certified_query_execution.py::test_a_numeric_string_is_not_silently_coerced_to_an_int`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_numeric_string_is_not_silently_coerced_to_an_int PASSED [ 22%]`

### Scenario: test_the_executor_also_guards_types_for_direct_callers
- Input: `backend/tests/test_certified_query_execution.py::test_the_executor_also_guards_types_for_direct_callers`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_executor_also_guards_types_for_direct_callers PASSED [ 22%]`

### Scenario: test_an_int_where_a_string_is_declared_is_refused
- Input: `backend/tests/test_certified_query_execution.py::test_an_int_where_a_string_is_declared_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_an_int_where_a_string_is_declared_is_refused PASSED [ 22%]`

### Scenario: test_an_unknown_version_of_a_known_query_is_refused
- Input: `backend/tests/test_certified_query_execution.py::test_an_unknown_version_of_a_known_query_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_an_unknown_version_of_a_known_query_is_refused PASSED [ 22%]`

### Scenario: test_query_over_http_returns_rows_for_the_detector
- Input: `backend/tests/test_certified_query_execution.py::test_query_over_http_returns_rows_for_the_detector`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_query_over_http_returns_rows_for_the_detector PASSED [ 22%]`

### Scenario: test_http_refusal_becomes_a_typed_client_exception
- Input: `backend/tests/test_certified_query_execution.py::test_http_refusal_becomes_a_typed_client_exception`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_http_refusal_becomes_a_typed_client_exception PASSED [ 22%]`

### Scenario: test_an_unresolvable_principal_is_refused_with_no_default_identity
- Input: `backend/tests/test_certified_query_execution.py::test_an_unresolvable_principal_is_refused_with_no_default_identity`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_an_unresolvable_principal_is_refused_with_no_default_identity PASSED [ 22%]`

### Scenario: test_a_wrong_client_token_is_rejected_before_the_principal_is_considered
- Input: `backend/tests/test_certified_query_execution.py::test_a_wrong_client_token_is_rejected_before_the_principal_is_considered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_a_wrong_client_token_is_rejected_before_the_principal_is_considered PASSED [ 22%]`

### Scenario: test_the_catalogue_omits_personal_data_queries_for_the_unentitled
- Input: `backend/tests/test_certified_query_execution.py::test_the_catalogue_omits_personal_data_queries_for_the_unentitled`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_catalogue_omits_personal_data_queries_for_the_unentitled PASSED [ 22%]`

### Scenario: test_the_catalogue_never_returns_sql_text
- Input: `backend/tests/test_certified_query_execution.py::test_the_catalogue_never_returns_sql_text`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_certified_query_execution.py::test_the_catalogue_never_returns_sql_text PASSED [ 22%]`

### Scenario: test_the_nine_new_populations_compile
- Input: `backend/tests/test_close_dataset_registry.py::test_the_nine_new_populations_compile`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_the_nine_new_populations_compile PASSED [ 22%]`

### Scenario: test_no_population_names_a_physical_object
- Input: `backend/tests/test_close_dataset_registry.py::test_no_population_names_a_physical_object`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_no_population_names_a_physical_object PASSED [ 22%]`

### Scenario: test_a_population_that_named_its_table_would_not_compile
- Input: `backend/tests/test_close_dataset_registry.py::test_a_population_that_named_its_table_would_not_compile`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_a_population_that_named_its_table_would_not_compile PASSED [ 22%]`

### Scenario: test_the_twelve_new_queries_compile_and_carry_a_committed_statement
- Input: `backend/tests/test_close_dataset_registry.py::test_the_twelve_new_queries_compile_and_carry_a_committed_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_the_twelve_new_queries_compile_and_carry_a_committed_statement PASSED [ 23%]`

### Scenario: test_no_new_query_declares_a_parameter_that_could_carry_a_predicate
- Input: `backend/tests/test_close_dataset_registry.py::test_no_new_query_declares_a_parameter_that_could_carry_a_predicate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_no_new_query_declares_a_parameter_that_could_carry_a_predicate PASSED [ 23%]`

### Scenario: test_the_narrative_leg_query_is_not_model_bound_eligible
- Input: `backend/tests/test_close_dataset_registry.py::test_the_narrative_leg_query_is_not_model_bound_eligible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_the_narrative_leg_query_is_not_model_bound_eligible PASSED [ 23%]`

### Scenario: test_every_new_query_is_reachable_only_by_id
- Input: `backend/tests/test_close_dataset_registry.py::test_every_new_query_is_reachable_only_by_id`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_every_new_query_is_reachable_only_by_id PASSED [ 23%]`

### Scenario: test_an_omitted_object_fails_the_query_rather_than_answering_it_with_zero_rows
- Input: `backend/tests/test_close_dataset_registry.py::test_an_omitted_object_fails_the_query_rather_than_answering_it_with_zero_rows`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_dataset_registry.py::test_an_omitted_object_fails_the_query_rather_than_answering_it_with_zero_rows PASSED [ 23%]`

### Scenario: test_an_unknown_family_is_an_error_not_a_silently_clean_fixture
- Input: `backend/tests/test_close_datasets.py::test_an_unknown_family_is_an_error_not_a_silently_clean_fixture`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_an_unknown_family_is_an_error_not_a_silently_clean_fixture PASSED [ 23%]`

### Scenario: test_generation_is_deterministic
- Input: `backend/tests/test_close_datasets.py::test_generation_is_deterministic`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_generation_is_deterministic PASSED [ 23%]`

### Scenario: test_the_seeded_divergences_are_exactly_the_declared_four
- Input: `backend/tests/test_close_datasets.py::test_the_seeded_divergences_are_exactly_the_declared_four`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_seeded_divergences_are_exactly_the_declared_four PASSED [ 23%]`

### Scenario: test_the_clean_world_ties_exactly
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_ties_exactly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_clean_world_ties_exactly PASSED [ 23%]`

### Scenario: test_the_two_worlds_differ_only_in_the_seeded_divergences
- Input: `backend/tests/test_close_datasets.py::test_the_two_worlds_differ_only_in_the_seeded_divergences`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_two_worlds_differ_only_in_the_seeded_divergences PASSED [ 23%]`

### Scenario: test_the_smallest_currency_unit_divergence_survives_as_a_decimal
- Input: `backend/tests/test_close_datasets.py::test_the_smallest_currency_unit_divergence_survives_as_a_decimal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_smallest_currency_unit_divergence_survives_as_a_decimal PASSED [ 23%]`

### Scenario: test_one_divergence_sits_in_the_earliest_period_and_one_in_the_latest
- Input: `backend/tests/test_close_datasets.py::test_one_divergence_sits_in_the_earliest_period_and_one_in_the_latest`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_one_divergence_sits_in_the_earliest_period_and_one_in_the_latest PASSED [ 23%]`

### Scenario: test_exactly_one_batch_never_arrived_and_it_names_what_it_would_have_fed
- Input: `backend/tests/test_close_datasets.py::test_exactly_one_batch_never_arrived_and_it_names_what_it_would_have_fed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_exactly_one_batch_never_arrived_and_it_names_what_it_would_have_fed PASSED [ 23%]`

### Scenario: test_a_missing_batch_is_distinct_from_a_batch_that_arrived_empty
- Input: `backend/tests/test_close_datasets.py::test_a_missing_batch_is_distinct_from_a_batch_that_arrived_empty`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_a_missing_batch_is_distinct_from_a_batch_that_arrived_empty PASSED [ 23%]`

### Scenario: test_every_batch_arrived_in_the_clean_world
- Input: `backend/tests/test_close_datasets.py::test_every_batch_arrived_in_the_clean_world`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_every_batch_arrived_in_the_clean_world PASSED [ 24%]`

### Scenario: test_one_batch_arrived_late_so_late_is_distinguishable_from_absent
- Input: `backend/tests/test_close_datasets.py::test_one_batch_arrived_late_so_late_is_distinguishable_from_absent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_one_batch_arrived_late_so_late_is_distinguishable_from_absent PASSED [ 24%]`

### Scenario: test_the_a6_break_is_one_subledger_in_one_period
- Input: `backend/tests/test_close_datasets.py::test_the_a6_break_is_one_subledger_in_one_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_a6_break_is_one_subledger_in_one_period PASSED [ 24%]`

### Scenario: test_the_a7_imbalance_is_one_pair_in_one_period
- Input: `backend/tests/test_close_datasets.py::test_the_a7_imbalance_is_one_pair_in_one_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_a7_imbalance_is_one_pair_in_one_period PASSED [ 24%]`

### Scenario: test_the_a8_discontinuity_breaks_the_identity_by_the_declared_amount
- Input: `backend/tests/test_close_datasets.py::test_the_a8_discontinuity_breaks_the_identity_by_the_declared_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_a8_discontinuity_breaks_the_identity_by_the_declared_amount PASSED [ 24%]`

### Scenario: test_the_a9_revaluation_is_applied_twice_exactly_once
- Input: `backend/tests/test_close_datasets.py::test_the_a9_revaluation_is_applied_twice_exactly_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_a9_revaluation_is_applied_twice_exactly_once PASSED [ 24%]`

### Scenario: test_the_a10_residual_exceeds_its_policy_threshold
- Input: `backend/tests/test_close_datasets.py::test_the_a10_residual_exceeds_its_policy_threshold`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_a10_residual_exceeds_its_policy_threshold PASSED [ 24%]`

### Scenario: test_the_accumulating_account_stays_under_threshold_every_period
- Input: `backend/tests/test_close_datasets.py::test_the_accumulating_account_stays_under_threshold_every_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_accumulating_account_stays_under_threshold_every_period PASSED [ 24%]`

### Scenario: test_the_accumulating_account_aggregates_to_the_declared_material_amount
- Input: `backend/tests/test_close_datasets.py::test_the_accumulating_account_aggregates_to_the_declared_material_amount`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_accumulating_account_aggregates_to_the_declared_material_amount PASSED [ 24%]`

### Scenario: test_the_one_short_variant_differs_in_exactly_one_movement
- Input: `backend/tests/test_close_datasets.py::test_the_one_short_variant_differs_in_exactly_one_movement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_one_short_variant_differs_in_exactly_one_movement PASSED [ 24%]`

### Scenario: test_the_alternating_account_does_not_accumulate
- Input: `backend/tests/test_close_datasets.py::test_the_alternating_account_does_not_accumulate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_alternating_account_does_not_accumulate PASSED [ 24%]`

### Scenario: test_the_narrative_account_repeats_verbatim_while_its_movements_alternate
- Input: `backend/tests/test_close_datasets.py::test_the_narrative_account_repeats_verbatim_while_its_movements_alternate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_narrative_account_repeats_verbatim_while_its_movements_alternate PASSED [ 24%]`

### Scenario: test_the_clean_world_gives_each_period_a_different_explanation
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_gives_each_period_a_different_explanation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_clean_world_gives_each_period_a_different_explanation PASSED [ 24%]`

### Scenario: test_two_explanations_were_never_recorded_rather_than_recorded_empty
- Input: `backend/tests/test_close_datasets.py::test_two_explanations_were_never_recorded_rather_than_recorded_empty`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_two_explanations_were_never_recorded_rather_than_recorded_empty PASSED [ 24%]`

### Scenario: test_one_account_has_a_single_period_of_history
- Input: `backend/tests/test_close_datasets.py::test_one_account_has_a_single_period_of_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_one_account_has_a_single_period_of_history PASSED [ 25%]`

### Scenario: test_the_five_miscodings_are_present_and_declared
- Input: `backend/tests/test_close_datasets.py::test_the_five_miscodings_are_present_and_declared`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_five_miscodings_are_present_and_declared PASSED [ 25%]`

### Scenario: test_three_of_the_five_are_declared_out_of_scope
- Input: `backend/tests/test_close_datasets.py::test_three_of_the_five_are_declared_out_of_scope`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_three_of_the_five_are_declared_out_of_scope PASSED [ 25%]`

### Scenario: test_the_peer_set_is_large_and_overwhelmingly_consistent
- Input: `backend/tests/test_close_datasets.py::test_the_peer_set_is_large_and_overwhelmingly_consistent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_peer_set_is_large_and_overwhelmingly_consistent PASSED [ 25%]`

### Scenario: test_the_held_out_period_carries_three_miscodings_of_which_two_are_labelled
- Input: `backend/tests/test_close_datasets.py::test_the_held_out_period_carries_three_miscodings_of_which_two_are_labelled`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_held_out_period_carries_three_miscodings_of_which_two_are_labelled PASSED [ 25%]`

### Scenario: test_the_clean_world_contains_the_peers_and_no_candidate_defects
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_contains_the_peers_and_no_candidate_defects`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_clean_world_contains_the_peers_and_no_candidate_defects PASSED [ 25%]`

### Scenario: test_the_cut_off_posting_disagrees_with_its_evidence_period
- Input: `backend/tests/test_close_datasets.py::test_the_cut_off_posting_disagrees_with_its_evidence_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_the_cut_off_posting_disagrees_with_its_evidence_period PASSED [ 25%]`

### Scenario: test_one_held_out_period_has_exactly_one_label_and_one_has_none
- Input: `backend/tests/test_close_datasets.py::test_one_held_out_period_has_exactly_one_label_and_one_has_none`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_close_datasets.py::test_one_held_out_period_has_exactly_one_label_and_one_has_none PASSED [ 25%]`

### Scenario: test_full_coverage_yields_the_full_population_type
- Input: `backend/tests/test_conclusion_type.py::test_full_coverage_yields_the_full_population_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_full_coverage_yields_the_full_population_type PASSED [ 25%]`

### Scenario: test_partial_coverage_yields_the_bounded_type
- Input: `backend/tests/test_conclusion_type.py::test_partial_coverage_yields_the_bounded_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_partial_coverage_yields_the_bounded_type PASSED [ 25%]`

### Scenario: test_zero_coverage_yields_the_no_scan_type
- Input: `backend/tests/test_conclusion_type.py::test_zero_coverage_yields_the_no_scan_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_zero_coverage_yields_the_no_scan_type PASSED [ 25%]`

### Scenario: test_the_union_is_closed
- Input: `backend/tests/test_conclusion_type.py::test_the_union_is_closed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_union_is_closed PASSED   [ 25%]`

### Scenario: test_no_exceptions_exists_only_on_the_full_population_type
- Input: `backend/tests/test_conclusion_type.py::test_no_exceptions_exists_only_on_the_full_population_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_no_exceptions_exists_only_on_the_full_population_type PASSED [ 25%]`

### Scenario: test_a_bounded_conclusion_has_no_no_exceptions_attribute_at_all
- Input: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_has_no_no_exceptions_attribute_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_has_no_no_exceptions_attribute_at_all PASSED [ 25%]`

### Scenario: test_a_no_scan_conclusion_has_no_no_exceptions_attribute_at_all
- Input: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_has_no_no_exceptions_attribute_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_has_no_no_exceptions_attribute_at_all PASSED [ 25%]`

### Scenario: test_the_attribute_cannot_be_attached_to_a_bounded_instance
- Input: `backend/tests/test_conclusion_type.py::test_the_attribute_cannot_be_attached_to_a_bounded_instance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_attribute_cannot_be_attached_to_a_bounded_instance PASSED [ 26%]`

### Scenario: test_a_no_scan_conclusion_carries_no_findings_at_all
- Input: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_carries_no_findings_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_carries_no_findings_at_all PASSED [ 26%]`

### Scenario: test_the_full_population_constructor_is_not_reachable_by_an_ordinary_caller
- Input: `backend/tests/test_conclusion_type.py::test_the_full_population_constructor_is_not_reachable_by_an_ordinary_caller`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_full_population_constructor_is_not_reachable_by_an_ordinary_caller PASSED [ 26%]`

### Scenario: test_the_other_variants_are_also_privately_constructed
- Input: `backend/tests/test_conclusion_type.py::test_the_other_variants_are_also_privately_constructed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_other_variants_are_also_privately_constructed PASSED [ 26%]`

### Scenario: test_the_invariant_is_rechecked_inside_the_constructor
- Input: `backend/tests/test_conclusion_type.py::test_the_invariant_is_rechecked_inside_the_constructor`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_invariant_is_rechecked_inside_the_constructor PASSED [ 26%]`

### Scenario: test_an_object_new_bypass_produces_an_unusable_instance
- Input: `backend/tests/test_conclusion_type.py::test_an_object_new_bypass_produces_an_unusable_instance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_an_object_new_bypass_produces_an_unusable_instance PASSED [ 26%]`

### Scenario: test_a_bounded_conclusion_cannot_be_built_with_an_empty_gap_set
- Input: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_cannot_be_built_with_an_empty_gap_set`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_cannot_be_built_with_an_empty_gap_set PASSED [ 26%]`

### Scenario: test_the_all_clear_phrases_appear_in_one_module_only
- Input: `backend/tests/test_conclusion_type.py::test_the_all_clear_phrases_appear_in_one_module_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_all_clear_phrases_appear_in_one_module_only PASSED [ 26%]`

### Scenario: test_no_module_reaches_for_the_private_factory_key
- Input: `backend/tests/test_conclusion_type.py::test_no_module_reaches_for_the_private_factory_key`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_no_module_reaches_for_the_private_factory_key PASSED [ 26%]`

### Scenario: test_the_lint_detects_a_planted_violation
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_violation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_violation PASSED [ 26%]`

### Scenario: test_the_lint_detects_a_planted_factory_key_import
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_factory_key_import`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_factory_key_import PASSED [ 26%]`

### Scenario: test_the_lint_does_not_fire_on_ordinary_words
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_does_not_fire_on_ordinary_words`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_lint_does_not_fire_on_ordinary_words PASSED [ 26%]`

### Scenario: test_all_three_surfaces_render_from_the_same_object
- Input: `backend/tests/test_conclusion_type.py::test_all_three_surfaces_render_from_the_same_object`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_all_three_surfaces_render_from_the_same_object PASSED [ 26%]`

### Scenario: test_a_partial_clean_result_never_renders_an_unqualified_all_clear
- Input: `backend/tests/test_conclusion_type.py::test_a_partial_clean_result_never_renders_an_unqualified_all_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_partial_clean_result_never_renders_an_unqualified_all_clear PASSED [ 26%]`

### Scenario: test_a_full_and_a_partial_result_differ_textually_on_every_surface
- Input: `backend/tests/test_conclusion_type.py::test_a_full_and_a_partial_result_differ_textually_on_every_surface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_full_and_a_partial_result_differ_textually_on_every_surface PASSED [ 27%]`

### Scenario: test_the_no_scan_result_renders_no_findings_region
- Input: `backend/tests/test_conclusion_type.py::test_the_no_scan_result_renders_no_findings_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_no_scan_result_renders_no_findings_region PASSED [ 27%]`

### Scenario: test_the_partial_run_banner_comes_from_the_type
- Input: `backend/tests/test_conclusion_type.py::test_the_partial_run_banner_comes_from_the_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_the_partial_run_banner_comes_from_the_type PASSED [ 27%]`

### Scenario: test_a_non_conclusion_cannot_be_rendered
- Input: `backend/tests/test_conclusion_type.py::test_a_non_conclusion_cannot_be_rendered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_a_non_conclusion_cannot_be_rendered PASSED [ 27%]`

### Scenario: test_full_coverage_with_findings_does_not_claim_an_all_clear
- Input: `backend/tests/test_conclusion_type.py::test_full_coverage_with_findings_does_not_claim_an_all_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_conclusion_type.py::test_full_coverage_with_findings_does_not_claim_an_all_clear PASSED [ 27%]`

### Scenario: test_emit_buffers_and_returns_the_event
- Input: `backend/tests/test_control_events.py::test_emit_buffers_and_returns_the_event`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_control_events.py::test_emit_buffers_and_returns_the_event PASSED [ 27%]`

### Scenario: test_buffered_filters_by_type
- Input: `backend/tests/test_control_events.py::test_buffered_filters_by_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_control_events.py::test_buffered_filters_by_type PASSED [ 27%]`

### Scenario: test_installed_sink_receives_events
- Input: `backend/tests/test_control_events.py::test_installed_sink_receives_events`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_control_events.py::test_installed_sink_receives_events PASSED [ 27%]`

### Scenario: test_a_failing_sink_does_not_break_the_caller_and_is_itself_recorded
- Input: `backend/tests/test_control_events.py::test_a_failing_sink_does_not_break_the_caller_and_is_itself_recorded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_control_events.py::test_a_failing_sink_does_not_break_the_caller_and_is_itself_recorded PASSED [ 27%]`

### Scenario: test_buffer_is_bounded
- Input: `backend/tests/test_control_events.py::test_buffer_is_bounded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_control_events.py::test_buffer_is_bounded PASSED      [ 27%]`

### Scenario: test_resolution_from_api_process_raises_and_is_recorded
- Input: `backend/tests/test_credential_boundary.py::test_resolution_from_api_process_raises_and_is_recorded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_resolution_from_api_process_raises_and_is_recorded PASSED [ 27%]`

### Scenario: test_resolution_with_unset_role_raises
- Input: `backend/tests/test_credential_boundary.py::test_resolution_with_unset_role_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_resolution_with_unset_role_raises PASSED [ 27%]`

### Scenario: test_boundary_violation_message_does_not_contain_a_value
- Input: `backend/tests/test_credential_boundary.py::test_boundary_violation_message_does_not_contain_a_value`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_boundary_violation_message_does_not_contain_a_value PASSED [ 27%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_PASSWORD]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_PASSWORD]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_PASSWORD] PASSED [ 27%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_USER]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_USER]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_USER] PASSED [ 28%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_TOKEN]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_TOKEN]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_TOKEN] PASSED [ 28%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[ORACLE_POSTING_PASSWORD]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_POSTING_PASSWORD]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_POSTING_PASSWORD] PASSED [ 28%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[ORACLE_JOURNAL_POST_TOKEN]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_JOURNAL_POST_TOKEN]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_JOURNAL_POST_TOKEN] PASSED [ 28%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[FUSION_POSTING_CLIENT_SECRET]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[FUSION_POSTING_CLIENT_SECRET]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[FUSION_POSTING_CLIENT_SECRET] PASSED [ 28%]`

### Scenario: test_posting_credential_never_resolves_even_inside_ges[GL_INTERFACE_SUBMIT_KEY]
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GL_INTERFACE_SUBMIT_KEY]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GL_INTERFACE_SUBMIT_KEY] PASSED [ 28%]`

### Scenario: test_undeclared_name_returns_none_and_is_recorded
- Input: `backend/tests/test_credential_boundary.py::test_undeclared_name_returns_none_and_is_recorded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_undeclared_name_returns_none_and_is_recorded PASSED [ 28%]`

### Scenario: test_declared_but_absent_returns_none_and_is_recorded
- Input: `backend/tests/test_credential_boundary.py::test_declared_but_absent_returns_none_and_is_recorded`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_declared_but_absent_returns_none_and_is_recorded PASSED [ 28%]`

### Scenario: test_declared_but_empty_string_is_treated_as_absent
- Input: `backend/tests/test_credential_boundary.py::test_declared_but_empty_string_is_treated_as_absent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_declared_but_empty_string_is_treated_as_absent PASSED [ 28%]`

### Scenario: test_declared_and_present_resolves_inside_ges
- Input: `backend/tests/test_credential_boundary.py::test_declared_and_present_resolves_inside_ges`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_declared_and_present_resolves_inside_ges PASSED [ 28%]`

### Scenario: test_forbidden_and_declared_sets_do_not_overlap
- Input: `backend/tests/test_credential_boundary.py::test_forbidden_and_declared_sets_do_not_overlap`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_forbidden_and_declared_sets_do_not_overlap PASSED [ 28%]`

### Scenario: test_api_startup_guard_passes_on_a_clean_environment
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_passes_on_a_clean_environment`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_api_startup_guard_passes_on_a_clean_environment PASSED [ 28%]`

### Scenario: test_api_startup_guard_refuses_on_a_leaked_credential
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_leaked_credential`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_leaked_credential PASSED [ 28%]`

### Scenario: test_api_startup_guard_refuses_on_a_posting_credential
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_posting_credential`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_posting_credential PASSED [ 28%]`

### Scenario: test_api_startup_guard_ignores_an_empty_value
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_ignores_an_empty_value`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_credential_boundary.py::test_api_startup_guard_ignores_an_empty_value PASSED [ 28%]`

### Scenario: test_the_committed_manifests_compile
- Input: `backend/tests/test_detector_manifests.py::test_the_committed_manifests_compile`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_the_committed_manifests_compile PASSED [ 29%]`

### Scenario: test_the_two_wedge_detectors_share_population_and_input
- Input: `backend/tests/test_detector_manifests.py::test_the_two_wedge_detectors_share_population_and_input`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_the_two_wedge_detectors_share_population_and_input PASSED [ 29%]`

### Scenario: test_the_omission_detector_does_not_permit_a_posting_resolution
- Input: `backend/tests/test_detector_manifests.py::test_the_omission_detector_does_not_permit_a_posting_resolution`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_the_omission_detector_does_not_permit_a_posting_resolution PASSED [ 29%]`

### Scenario: test_every_manifest_declares_both_fixtures
- Input: `backend/tests/test_detector_manifests.py::test_every_manifest_declares_both_fixtures`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_every_manifest_declares_both_fixtures PASSED [ 29%]`

### Scenario: test_the_manifest_hash_is_stable_and_changes_with_content
- Input: `backend/tests/test_detector_manifests.py::test_the_manifest_hash_is_stable_and_changes_with_content`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_the_manifest_hash_is_stable_and_changes_with_content PASSED [ 29%]`

### Scenario: test_a_manifest_naming_a_table_fails_compilation
- Input: `backend/tests/test_detector_manifests.py::test_a_manifest_naming_a_table_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_manifest_naming_a_table_fails_compilation PASSED [ 29%]`

### Scenario: test_a_manifest_with_a_table_key_fails_compilation
- Input: `backend/tests/test_detector_manifests.py::test_a_manifest_with_a_table_key_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_manifest_with_a_table_key_fails_compilation PASSED [ 29%]`

### Scenario: test_an_unregistered_evaluator_fails_compilation
- Input: `backend/tests/test_detector_manifests.py::test_an_unregistered_evaluator_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_unregistered_evaluator_fails_compilation PASSED [ 29%]`

### Scenario: test_all_eleven_specified_primitives_are_now_built
- Input: `backend/tests/test_detector_manifests.py::test_all_eleven_specified_primitives_are_now_built`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_all_eleven_specified_primitives_are_now_built PASSED [ 29%]`

### Scenario: test_a_specified_but_unimplemented_primitive_still_says_so
- Input: `backend/tests/test_detector_manifests.py::test_a_specified_but_unimplemented_primitive_still_says_so`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_specified_but_unimplemented_primitive_still_says_so PASSED [ 29%]`

### Scenario: test_no_unimplemented_primitive_is_secretly_registered
- Input: `backend/tests/test_detector_manifests.py::test_no_unimplemented_primitive_is_secretly_registered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_no_unimplemented_primitive_is_secretly_registered PASSED [ 29%]`

### Scenario: test_an_unknown_population_fails_compilation
- Input: `backend/tests/test_detector_manifests.py::test_an_unknown_population_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_unknown_population_fails_compilation PASSED [ 29%]`

### Scenario: test_an_uncertified_input_query_fails_compilation
- Input: `backend/tests/test_detector_manifests.py::test_an_uncertified_input_query_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_uncertified_input_query_fails_compilation PASSED [ 29%]`

### Scenario: test_an_input_query_incompatible_with_the_population_fails
- Input: `backend/tests/test_detector_manifests.py::test_an_input_query_incompatible_with_the_population_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_input_query_incompatible_with_the_population_fails PASSED [ 29%]`

### Scenario: test_more_than_one_input_fails_in_pass_1
- Input: `backend/tests/test_detector_manifests.py::test_more_than_one_input_fails_in_pass_1`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_more_than_one_input_fails_in_pass_1 PASSED [ 30%]`

### Scenario: test_an_input_without_a_version_fails
- Input: `backend/tests/test_detector_manifests.py::test_an_input_without_a_version_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_input_without_a_version_fails PASSED [ 30%]`

### Scenario: test_a_missing_fixture_fails_compilation[positive]
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[positive]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[positive] PASSED [ 30%]`

### Scenario: test_a_missing_fixture_fails_compilation[negative]
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[negative]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[negative] PASSED [ 30%]`

### Scenario: test_a_fixture_naming_an_undeclared_scenario_fails
- Input: `backend/tests/test_detector_manifests.py::test_a_fixture_naming_an_undeclared_scenario_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_fixture_naming_an_undeclared_scenario_fails PASSED [ 30%]`

### Scenario: test_a_resolution_type_outside_r1_to_r6_fails
- Input: `backend/tests/test_detector_manifests.py::test_a_resolution_type_outside_r1_to_r6_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_resolution_type_outside_r1_to_r6_fails PASSED [ 30%]`

### Scenario: test_no_permitted_resolution_types_fails
- Input: `backend/tests/test_detector_manifests.py::test_no_permitted_resolution_types_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_no_permitted_resolution_types_fails PASSED [ 30%]`

### Scenario: test_a_missing_finding_type_fails
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_finding_type_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_missing_finding_type_fails PASSED [ 30%]`

### Scenario: test_an_empty_manifests_directory_fails
- Input: `backend/tests/test_detector_manifests.py::test_an_empty_manifests_directory_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_an_empty_manifests_directory_fails PASSED [ 30%]`

### Scenario: test_a_duplicate_detector_ref_fails
- Input: `backend/tests/test_detector_manifests.py::test_a_duplicate_detector_ref_fails`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_a_duplicate_detector_ref_fails PASSED [ 30%]`

### Scenario: test_float_params_survive_compilation_and_reach_the_evaluator
- Input: `backend/tests/test_detector_manifests.py::test_float_params_survive_compilation_and_reach_the_evaluator`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_detector_manifests.py::test_float_params_survive_compilation_and_reach_the_evaluator PASSED [ 30%]`

### Scenario: test_a_complete_close_completes
- Input: `backend/tests/test_disposition.py::test_a_complete_close_completes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_complete_close_completes PASSED [ 30%]`

### Scenario: test_a_close_without_a_resolution_type_does_not_complete[None]
- Input: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[None]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[None] PASSED [ 30%]`

### Scenario: test_a_close_without_a_resolution_type_does_not_complete[]
- Input: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[] PASSED [ 30%]`

### Scenario: test_a_resolution_type_outside_r1_to_r6_is_refused
- Input: `backend/tests/test_disposition.py::test_a_resolution_type_outside_r1_to_r6_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_resolution_type_outside_r1_to_r6_is_refused PASSED [ 31%]`

### Scenario: test_the_schema_itself_refuses_a_disposition_with_no_resolution_type
- Input: `backend/tests/test_disposition.py::test_the_schema_itself_refuses_a_disposition_with_no_resolution_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_schema_itself_refuses_a_disposition_with_no_resolution_type PASSED [ 31%]`

### Scenario: test_an_item_can_be_closed_only_once
- Input: `backend/tests/test_disposition.py::test_an_item_can_be_closed_only_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_an_item_can_be_closed_only_once PASSED [ 31%]`

### Scenario: test_r1_without_an_expiry_does_not_complete
- Input: `backend/tests/test_disposition.py::test_r1_without_an_expiry_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r1_without_an_expiry_does_not_complete PASSED [ 31%]`

### Scenario: test_r1_with_an_expiry_completes
- Input: `backend/tests/test_disposition.py::test_r1_with_an_expiry_completes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r1_with_an_expiry_completes PASSED [ 31%]`

### Scenario: test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence0-missing0]
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence0-missing0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence0-missing0] PASSED [ 31%]`

### Scenario: test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence1-missing1]
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence1-missing1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence1-missing1] PASSED [ 31%]`

### Scenario: test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence2-missing2]
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence2-missing2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence2-missing2] PASSED [ 31%]`

### Scenario: test_r5_with_both_completes_and_records_them
- Input: `backend/tests/test_disposition.py::test_r5_with_both_completes_and_records_them`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r5_with_both_completes_and_records_them PASSED [ 31%]`

### Scenario: test_r6_changes_the_risk_grade_and_auto_pass_and_leaves_an_audit_record
- Input: `backend/tests/test_disposition.py::test_r6_changes_the_risk_grade_and_auto_pass_and_leaves_an_audit_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r6_changes_the_risk_grade_and_auto_pass_and_leaves_an_audit_record PASSED [ 31%]`

### Scenario: test_r6_without_the_control_state_change_itself_does_not_complete
- Input: `backend/tests/test_disposition.py::test_r6_without_the_control_state_change_itself_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_r6_without_the_control_state_change_itself_does_not_complete PASSED [ 31%]`

### Scenario: test_revoking_auto_pass_is_recordable_because_false_is_a_held_value
- Input: `backend/tests/test_disposition.py::test_revoking_auto_pass_is_recordable_because_false_is_a_held_value`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_revoking_auto_pass_is_recordable_because_false_is_a_held_value PASSED [ 31%]`

### Scenario: test_a_close_without_an_expected_clearing_period_does_not_complete
- Input: `backend/tests/test_disposition.py::test_a_close_without_an_expected_clearing_period_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_close_without_an_expected_clearing_period_does_not_complete PASSED [ 31%]`

### Scenario: test_it_is_a_hard_failure_not_a_bypassable_warning
- Input: `backend/tests/test_disposition.py::test_it_is_a_hard_failure_not_a_bypassable_warning`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_it_is_a_hard_failure_not_a_bypassable_warning PASSED [ 31%]`

### Scenario: test_the_column_is_not_null_so_the_prediction_cannot_be_retrofitted_away
- Input: `backend/tests/test_disposition.py::test_the_column_is_not_null_so_the_prediction_cannot_be_retrofitted_away`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_column_is_not_null_so_the_prediction_cannot_be_retrofitted_away PASSED [ 32%]`

### Scenario: test_a_clearing_period_at_or_before_the_current_period_does_not_save[12]
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[12]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[12] PASSED [ 32%]`

### Scenario: test_a_clearing_period_at_or_before_the_current_period_does_not_save[11]
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[11]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[11] PASSED [ 32%]`

### Scenario: test_a_clearing_period_at_or_before_the_current_period_does_not_save[0]
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[0] PASSED [ 32%]`

### Scenario: test_a_clearing_period_at_or_before_the_current_period_does_not_save[-1]
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[-1] PASSED [ 32%]`

### Scenario: test_the_earliest_permitted_period_saves
- Input: `backend/tests/test_disposition.py::test_the_earliest_permitted_period_saves`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_earliest_permitted_period_saves PASSED [ 32%]`

### Scenario: test_the_maximum_horizon_saves
- Input: `backend/tests/test_disposition.py::test_the_maximum_horizon_saves`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_maximum_horizon_saves PASSED [ 32%]`

### Scenario: test_beyond_the_maximum_horizon_does_not_save_and_states_the_maximum
- Input: `backend/tests/test_disposition.py::test_beyond_the_maximum_horizon_does_not_save_and_states_the_maximum`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_beyond_the_maximum_horizon_does_not_save_and_states_the_maximum PASSED [ 32%]`

### Scenario: test_a_failed_capture_write_leaves_the_item_open_with_no_disposition
- Input: `backend/tests/test_disposition.py::test_a_failed_capture_write_leaves_the_item_open_with_no_disposition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_failed_capture_write_leaves_the_item_open_with_no_disposition PASSED [ 32%]`

### Scenario: test_a_failed_r6_state_change_leaves_no_partial_record
- Input: `backend/tests/test_disposition.py::test_a_failed_r6_state_change_leaves_no_partial_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_failed_r6_state_change_leaves_no_partial_record PASSED [ 32%]`

### Scenario: test_the_capture_row_cannot_outlive_its_disposition
- Input: `backend/tests/test_disposition.py::test_the_capture_row_cannot_outlive_its_disposition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_capture_row_cannot_outlive_its_disposition PASSED [ 32%]`

### Scenario: test_a_lapsed_r1_reopens_labelled_with_its_original_explanation
- Input: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_labelled_with_its_original_explanation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_labelled_with_its_original_explanation PASSED [ 32%]`

### Scenario: test_an_r1_inside_its_expiry_does_not_reopen
- Input: `backend/tests/test_disposition.py::test_an_r1_inside_its_expiry_does_not_reopen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_an_r1_inside_its_expiry_does_not_reopen PASSED [ 32%]`

### Scenario: test_a_lapsed_r1_reopens_only_once
- Input: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_only_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_only_once PASSED [ 32%]`

### Scenario: test_other_resolution_types_do_not_lapse
- Input: `backend/tests/test_disposition.py::test_other_resolution_types_do_not_lapse`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_other_resolution_types_do_not_lapse PASSED [ 32%]`

### Scenario: test_the_job_runs_without_a_user_requesting_it
- Input: `backend/tests/test_disposition.py::test_the_job_runs_without_a_user_requesting_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_job_runs_without_a_user_requesting_it PASSED [ 33%]`

### Scenario: test_a_prediction_that_cleared_is_recorded_met
- Input: `backend/tests/test_disposition.py::test_a_prediction_that_cleared_is_recorded_met`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_prediction_that_cleared_is_recorded_met PASSED [ 33%]`

### Scenario: test_a_prediction_that_did_not_clear_is_recorded_missed
- Input: `backend/tests/test_disposition.py::test_a_prediction_that_did_not_clear_is_recorded_missed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_prediction_that_did_not_clear_is_recorded_missed PASSED [ 33%]`

### Scenario: test_a_missed_prediction_raises_the_risk_grade_and_revokes_auto_pass
- Input: `backend/tests/test_disposition.py::test_a_missed_prediction_raises_the_risk_grade_and_revokes_auto_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_missed_prediction_raises_the_risk_grade_and_revokes_auto_pass PASSED [ 33%]`

### Scenario: test_a_met_prediction_does_not_touch_the_account_state
- Input: `backend/tests/test_disposition.py::test_a_met_prediction_does_not_touch_the_account_state`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_met_prediction_does_not_touch_the_account_state PASSED [ 33%]`

### Scenario: test_a_period_with_nothing_due_records_zero_rather_than_nothing
- Input: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_records_zero_rather_than_nothing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_records_zero_rather_than_nothing PASSED [ 33%]`

### Scenario: test_a_period_not_yet_closed_records_a_deferral_and_verifies_nothing
- Input: `backend/tests/test_disposition.py::test_a_period_not_yet_closed_records_a_deferral_and_verifies_nothing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_period_not_yet_closed_records_a_deferral_and_verifies_nothing PASSED [ 33%]`

### Scenario: test_a_deferral_does_not_touch_the_account_state
- Input: `backend/tests/test_disposition.py::test_a_deferral_does_not_touch_the_account_state`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_deferral_does_not_touch_the_account_state PASSED [ 33%]`

### Scenario: test_a_verification_result_outside_the_closed_set_is_unstorable
- Input: `backend/tests/test_disposition.py::test_a_verification_result_outside_the_closed_set_is_unstorable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_verification_result_outside_the_closed_set_is_unstorable PASSED [ 33%]`

### Scenario: test_the_hit_rate_is_computed_over_predictions_due
- Input: `backend/tests/test_disposition.py::test_the_hit_rate_is_computed_over_predictions_due`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_hit_rate_is_computed_over_predictions_due PASSED [ 33%]`

### Scenario: test_a_bad_hit_rate_is_still_reported
- Input: `backend/tests/test_disposition.py::test_a_bad_hit_rate_is_still_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_bad_hit_rate_is_still_reported PASSED [ 33%]`

### Scenario: test_a_period_with_nothing_due_has_no_hit_rate_rather_than_one_hundred_percent
- Input: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_has_no_hit_rate_rather_than_one_hundred_percent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_has_no_hit_rate_rather_than_one_hundred_percent PASSED [ 33%]`

### Scenario: test_nothing_in_this_module_reaches_an_erp
- Input: `backend/tests/test_disposition.py::test_nothing_in_this_module_reaches_an_erp`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_nothing_in_this_module_reaches_an_erp PASSED [ 33%]`

### Scenario: test_the_disposition_schema_has_no_posting_column
- Input: `backend/tests/test_disposition.py::test_the_disposition_schema_has_no_posting_column`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_disposition.py::test_the_disposition_schema_has_no_posting_column PASSED [ 33%]`

### Scenario: test_absent_in_the_target_period_is_an_omission
- Input: `backend/tests/test_evaluator_primitives.py::test_absent_in_the_target_period_is_an_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_absent_in_the_target_period_is_an_omission PASSED [ 34%]`

### Scenario: test_present_in_the_target_period_is_not_an_omission
- Input: `backend/tests/test_evaluator_primitives.py::test_present_in_the_target_period_is_not_an_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_present_in_the_target_period_is_not_an_omission PASSED [ 34%]`

### Scenario: test_present_at_a_wildly_different_amount_is_still_not_an_omission
- Input: `backend/tests/test_evaluator_primitives.py::test_present_at_a_wildly_different_amount_is_still_not_an_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_present_at_a_wildly_different_amount_is_still_not_an_omission PASSED [ 34%]`

### Scenario: test_the_expected_amount_range_comes_from_the_history
- Input: `backend/tests/test_evaluator_primitives.py::test_the_expected_amount_range_comes_from_the_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_expected_amount_range_comes_from_the_history PASSED [ 34%]`

### Scenario: test_multiple_lines_in_one_period_are_summed_not_counted_twice
- Input: `backend/tests/test_evaluator_primitives.py::test_multiple_lines_in_one_period_are_summed_not_counted_twice`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_multiple_lines_in_one_period_are_summed_not_counted_twice PASSED [ 34%]`

### Scenario: test_the_minimum_history_boundary[5-False]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[5-False]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[5-False] PASSED [ 34%]`

### Scenario: test_the_minimum_history_boundary[6-True]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[6-True]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[6-True] PASSED [ 34%]`

### Scenario: test_a_member_with_no_rows_at_all_is_not_evaluable_rather_than_omitted
- Input: `backend/tests/test_evaluator_primitives.py::test_a_member_with_no_rows_at_all_is_not_evaluable_rather_than_omitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_a_member_with_no_rows_at_all_is_not_evaluable_rather_than_omitted PASSED [ 34%]`

### Scenario: test_an_irregular_member_grounds_no_expectation_but_is_evaluable
- Input: `backend/tests/test_evaluator_primitives.py::test_an_irregular_member_grounds_no_expectation_but_is_evaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_an_irregular_member_grounds_no_expectation_but_is_evaluable PASSED [ 34%]`

### Scenario: test_the_hit_ratio_boundary_is_inclusive_of_the_required_value
- Input: `backend/tests/test_evaluator_primitives.py::test_the_hit_ratio_boundary_is_inclusive_of_the_required_value`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_hit_ratio_boundary_is_inclusive_of_the_required_value PASSED [ 34%]`

### Scenario: test_params_from_the_manifest_override_the_defaults
- Input: `backend/tests/test_evaluator_primitives.py::test_params_from_the_manifest_override_the_defaults`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_params_from_the_manifest_override_the_defaults PASSED [ 34%]`

### Scenario: test_no_value_in_a_finding_is_a_float
- Input: `backend/tests/test_evaluator_primitives.py::test_no_value_in_a_finding_is_a_float`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_no_value_in_a_finding_is_a_float PASSED [ 34%]`

### Scenario: test_declared_members_absent_from_the_rows_are_still_assessed
- Input: `backend/tests/test_evaluator_primitives.py::test_declared_members_absent_from_the_rows_are_still_assessed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_declared_members_absent_from_the_rows_are_still_assessed PASSED [ 34%]`

### Scenario: test_an_absence_produces_no_present_anomaly
- Input: `backend/tests/test_evaluator_primitives.py::test_an_absence_produces_no_present_anomaly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_an_absence_produces_no_present_anomaly PASSED [ 34%]`

### Scenario: test_a_value_far_above_the_range_is_an_anomaly
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_far_above_the_range_is_an_anomaly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_a_value_far_above_the_range_is_an_anomaly PASSED [ 35%]`

### Scenario: test_a_value_far_below_the_range_is_an_anomaly
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_far_below_the_range_is_an_anomaly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_a_value_far_below_the_range_is_an_anomaly PASSED [ 35%]`

### Scenario: test_a_value_inside_the_range_is_not_an_anomaly
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_inside_the_range_is_not_an_anomaly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_a_value_inside_the_range_is_not_an_anomaly PASSED [ 35%]`

### Scenario: test_the_threshold_is_determinate_and_exclusive[200-0]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200-0] PASSED [ 35%]`

### Scenario: test_the_threshold_is_determinate_and_exclusive[200.01-1]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200.01-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200.01-1] PASSED [ 35%]`

### Scenario: test_the_threshold_is_determinate_and_exclusive[199.99-0]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[199.99-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[199.99-0] PASSED [ 35%]`

### Scenario: test_the_threshold_is_determinate_and_exclusive[50-0]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[50-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[50-0] PASSED [ 35%]`

### Scenario: test_the_threshold_is_determinate_and_exclusive[49.99-1]
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[49.99-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[49.99-1] PASSED [ 35%]`

### Scenario: test_every_anomaly_states_the_threshold_in_force
- Input: `backend/tests/test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force PASSED [ 35%]`

### Scenario: test_insufficient_history_is_not_evaluable_here_either
- Input: `backend/tests/test_evaluator_primitives.py::test_insufficient_history_is_not_evaluable_here_either`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_insufficient_history_is_not_evaluable_here_either PASSED [ 35%]`

### Scenario: test_the_threshold_ratio_is_configurable_from_the_manifest
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_ratio_is_configurable_from_the_manifest`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_threshold_ratio_is_configurable_from_the_manifest PASSED [ 35%]`

### Scenario: test_no_value_in_an_anomaly_finding_is_a_float
- Input: `backend/tests/test_evaluator_primitives.py::test_no_value_in_an_anomaly_finding_is_a_float`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_no_value_in_an_anomaly_finding_is_a_float PASSED [ 35%]`

### Scenario: test_the_two_primitives_disagree_exactly_where_they_should
- Input: `backend/tests/test_evaluator_primitives.py::test_the_two_primitives_disagree_exactly_where_they_should`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evaluator_primitives.py::test_the_two_primitives_disagree_exactly_where_they_should PASSED [ 35%]`

### Scenario: test_store_exposes_no_update_or_delete_function
- Input: `backend/tests/test_evidence_store.py::test_store_exposes_no_update_or_delete_function`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_store_exposes_no_update_or_delete_function PASSED [ 35%]`

### Scenario: test_first_entry_of_a_period_links_to_genesis
- Input: `backend/tests/test_evidence_store.py::test_first_entry_of_a_period_links_to_genesis`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_first_entry_of_a_period_links_to_genesis PASSED [ 35%]`

### Scenario: test_entries_chain_within_a_period
- Input: `backend/tests/test_evidence_store.py::test_entries_chain_within_a_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_entries_chain_within_a_period PASSED [ 36%]`

### Scenario: test_chains_are_per_period_and_independent
- Input: `backend/tests/test_evidence_store.py::test_chains_are_per_period_and_independent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_chains_are_per_period_and_independent PASSED [ 36%]`

### Scenario: test_an_empty_period_verifies_as_ok_with_zero_entries
- Input: `backend/tests/test_evidence_store.py::test_an_empty_period_verifies_as_ok_with_zero_entries`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_an_empty_period_verifies_as_ok_with_zero_entries PASSED [ 36%]`

### Scenario: test_head_of_an_empty_period_is_genesis
- Input: `backend/tests/test_evidence_store.py::test_head_of_an_empty_period_is_genesis`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_head_of_an_empty_period_is_genesis PASSED [ 36%]`

### Scenario: test_the_content_hash_is_a_pure_function_of_the_payload
- Input: `backend/tests/test_evidence_store.py::test_the_content_hash_is_a_pure_function_of_the_payload`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_content_hash_is_a_pure_function_of_the_payload PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[dossier_id]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dossier_id]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dossier_id] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[run_id]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[run_id]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[run_id] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[tenant_id]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[tenant_id]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[tenant_id] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[period]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[period]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[period] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[detector_ref]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[detector_ref]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[detector_ref] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[population_ref]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[population_ref]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[population_ref] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[dataset_versions]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dataset_versions]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dataset_versions] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[registry_hash]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[registry_hash]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[registry_hash] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[coverage]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[coverage]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[coverage] PASSED [ 36%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[conclusion]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[conclusion]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[conclusion] PASSED [ 37%]`

### Scenario: test_a_dossier_missing_any_required_element_cannot_be_persisted[created_at]
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[created_at]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[created_at] PASSED [ 37%]`

### Scenario: test_the_refusal_is_recorded_as_a_control_event
- Input: `backend/tests/test_evidence_store.py::test_the_refusal_is_recorded_as_a_control_event`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_refusal_is_recorded_as_a_control_event PASSED [ 37%]`

### Scenario: test_update_is_refused_below_the_application[evidence_entry]
- Input: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_entry]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_entry] PASSED [ 37%]`

### Scenario: test_update_is_refused_below_the_application[evidence_anchor]
- Input: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_anchor]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_anchor] PASSED [ 37%]`

### Scenario: test_delete_is_refused_below_the_application[evidence_entry]
- Input: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_entry]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_entry] PASSED [ 37%]`

### Scenario: test_delete_is_refused_below_the_application[evidence_anchor]
- Input: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_anchor]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_anchor] PASSED [ 37%]`

### Scenario: test_a_refused_mutation_is_recorded_and_retyped
- Input: `backend/tests/test_evidence_store.py::test_a_refused_mutation_is_recorded_and_retyped`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_refused_mutation_is_recorded_and_retyped PASSED [ 37%]`

### Scenario: test_an_unrelated_database_error_is_not_recorded_as_a_mutation_attempt
- Input: `backend/tests/test_evidence_store.py::test_an_unrelated_database_error_is_not_recorded_as_a_mutation_attempt`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_an_unrelated_database_error_is_not_recorded_as_a_mutation_attempt PASSED [ 37%]`

### Scenario: test_an_altered_record_is_identified_by_name
- Input: `backend/tests/test_evidence_store.py::test_an_altered_record_is_identified_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_an_altered_record_is_identified_by_name PASSED [ 37%]`

### Scenario: test_recomputing_the_content_hash_forward_still_breaks_the_chain
- Input: `backend/tests/test_evidence_store.py::test_recomputing_the_content_hash_forward_still_breaks_the_chain`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_recomputing_the_content_hash_forward_still_breaks_the_chain PASSED [ 37%]`

### Scenario: test_an_anchor_covers_the_chain_head
- Input: `backend/tests/test_evidence_store.py::test_an_anchor_covers_the_chain_head`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_an_anchor_covers_the_chain_head PASSED [ 37%]`

### Scenario: test_an_anchor_over_an_empty_period_is_refused
- Input: `backend/tests/test_evidence_store.py::test_an_anchor_over_an_empty_period_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_an_anchor_over_an_empty_period_is_refused PASSED [ 37%]`

### Scenario: test_a_stub_anchor_is_permanently_self_identifying
- Input: `backend/tests/test_evidence_store.py::test_a_stub_anchor_is_permanently_self_identifying`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_stub_anchor_is_permanently_self_identifying PASSED [ 37%]`

### Scenario: test_the_stub_signer_verifies_its_own_output_and_rejects_others
- Input: `backend/tests/test_evidence_store.py::test_the_stub_signer_verifies_its_own_output_and_rejects_others`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_stub_signer_verifies_its_own_output_and_rejects_others PASSED [ 38%]`

### Scenario: test_the_stub_signer_refuses_to_exist_in_production
- Input: `backend/tests/test_evidence_store.py::test_the_stub_signer_refuses_to_exist_in_production`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_stub_signer_refuses_to_exist_in_production PASSED [ 38%]`

### Scenario: test_the_signer_interface_exposes_no_private_key_accessor
- Input: `backend/tests/test_evidence_store.py::test_the_signer_interface_exposes_no_private_key_accessor`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_signer_interface_exposes_no_private_key_accessor PASSED [ 38%]`

### Scenario: test_the_archive_stub_marks_every_object_as_unlocked
- Input: `backend/tests/test_evidence_store.py::test_the_archive_stub_marks_every_object_as_unlocked`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_archive_stub_marks_every_object_as_unlocked PASSED [ 38%]`

### Scenario: test_the_archive_interface_has_no_delete_method
- Input: `backend/tests/test_evidence_store.py::test_the_archive_interface_has_no_delete_method`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_archive_interface_has_no_delete_method PASSED [ 38%]`

### Scenario: test_the_archive_stub_refuses_to_exist_in_production
- Input: `backend/tests/test_evidence_store.py::test_the_archive_stub_refuses_to_exist_in_production`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_the_archive_stub_refuses_to_exist_in_production PASSED [ 38%]`

### Scenario: test_a_dossier_round_trips_complete
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_round_trips_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_dossier_round_trips_complete PASSED [ 38%]`

### Scenario: test_retention_expiry_is_stamped_seven_years_out
- Input: `backend/tests/test_evidence_store.py::test_retention_expiry_is_stamped_seven_years_out`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_retention_expiry_is_stamped_seven_years_out PASSED [ 38%]`

### Scenario: test_reading_an_unknown_dossier_raises
- Input: `backend/tests/test_evidence_store.py::test_reading_an_unknown_dossier_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_reading_an_unknown_dossier_raises PASSED [ 38%]`

### Scenario: test_a_payload_version_with_no_reader_refuses_rather_than_partially_materialising
- Input: `backend/tests/test_evidence_store.py::test_a_payload_version_with_no_reader_refuses_rather_than_partially_materialising`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_a_payload_version_with_no_reader_refuses_rather_than_partially_materialising PASSED [ 38%]`

### Scenario: test_writing_an_unknown_payload_version_is_refused
- Input: `backend/tests/test_evidence_store.py::test_writing_an_unknown_payload_version_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_writing_an_unknown_payload_version_is_refused PASSED [ 38%]`

### Scenario: test_every_required_key_list_has_a_reader
- Input: `backend/tests/test_evidence_store.py::test_every_required_key_list_has_a_reader`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_every_required_key_list_has_a_reader PASSED [ 38%]`

### Scenario: test_control_events_route_into_the_append_only_chain
- Input: `backend/tests/test_evidence_store.py::test_control_events_route_into_the_append_only_chain`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_evidence_store.py::test_control_events_route_into_the_append_only_chain PASSED [ 38%]`

### Scenario: test_all_three_surfaces_render_from_the_same_object
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_all_three_surfaces_render_from_the_same_object`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_all_three_surfaces_render_from_the_same_object PASSED [ 38%]`

### Scenario: test_the_three_payloads_differ_only_in_which_surface_they_name
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_three_payloads_differ_only_in_which_surface_they_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_three_payloads_differ_only_in_which_surface_they_name PASSED [ 39%]`

### Scenario: test_no_surface_can_be_rendered_without_a_label_source
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_no_surface_can_be_rendered_without_a_label_source`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_no_surface_can_be_rendered_without_a_label_source PASSED [ 39%]`

### Scenario: test_the_screen_leg_renders_the_label_source_adjacent_to_the_figure
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_screen_leg_renders_the_label_source_adjacent_to_the_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_screen_leg_renders_the_label_source_adjacent_to_the_figure PASSED [ 39%]`

### Scenario: test_the_dossier_leg_exists_and_carries_the_label_source
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_leg_exists_and_carries_the_label_source`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_leg_exists_and_carries_the_label_source PASSED [ 39%]`

### Scenario: test_the_dossier_label_source_is_inside_the_same_element_as_the_figure
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_label_source_is_inside_the_same_element_as_the_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_label_source_is_inside_the_same_element_as_the_figure PASSED [ 39%]`

### Scenario: test_the_dossier_still_carries_no_external_reference_after_the_addition
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_still_carries_no_external_reference_after_the_addition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_still_carries_no_external_reference_after_the_addition PASSED [ 39%]`

### Scenario: test_the_dossier_figure_is_the_acceptance_derived_variant_and_says_so
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_figure_is_the_acceptance_derived_variant_and_says_so`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_figure_is_the_acceptance_derived_variant_and_says_so PASSED [ 39%]`

### Scenario: test_the_export_leg_carries_the_label_source_and_survives_a_file
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_export_leg_carries_the_label_source_and_survives_a_file`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_export_leg_carries_the_label_source_and_survives_a_file PASSED [ 39%]`

### Scenario: test_a_hand_assembled_export_payload_without_a_label_source_is_refused
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_a_hand_assembled_export_payload_without_a_label_source_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_a_hand_assembled_export_payload_without_a_label_source_is_refused PASSED [ 39%]`

### Scenario: test_an_empty_label_source_is_refused_as_firmly_as_a_missing_one
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_an_empty_label_source_is_refused_as_firmly_as_a_missing_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_an_empty_label_source_is_refused_as_firmly_as_a_missing_one PASSED [ 39%]`

### Scenario: test_AC_F12_20_the_label_source_is_read_on_screen_in_a_dossier_and_in_an_export
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_AC_F12_20_the_label_source_is_read_on_screen_in_a_dossier_and_in_an_export`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_label_source_three_surfaces.py::test_AC_F12_20_the_label_source_is_read_on_screen_in_a_dossier_and_in_an_export PASSED [ 39%]`

### Scenario: test_a_precision_figure_cannot_be_constructed_without_a_label_source
- Input: `backend/tests/test_f12_precision.py::test_a_precision_figure_cannot_be_constructed_without_a_label_source`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_precision_figure_cannot_be_constructed_without_a_label_source PASSED [ 39%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[]
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[] PASSED [ 39%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[   ] PASSED [ 39%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[None]
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[None]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[None] PASSED [ 39%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[7]
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[7]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[7] PASSED [ 40%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[bad4]
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad4]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad4] PASSED [ 40%]`

### Scenario: test_an_absent_or_empty_label_source_is_refused[bad5]
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad5]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad5] PASSED [ 40%]`

### Scenario: test_the_label_source_set_is_closed
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_set_is_closed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_set_is_closed PASSED [ 40%]`

### Scenario: test_a_figure_cannot_be_relabelled_after_construction
- Input: `backend/tests/test_f12_precision.py::test_a_figure_cannot_be_relabelled_after_construction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_figure_cannot_be_relabelled_after_construction PASSED [ 40%]`

### Scenario: test_a_label_source_cannot_be_attached_to_an_instance_that_lacks_one
- Input: `backend/tests/test_f12_precision.py::test_a_label_source_cannot_be_attached_to_an_instance_that_lacks_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_label_source_cannot_be_attached_to_an_instance_that_lacks_one PASSED [ 40%]`

### Scenario: test_the_residual_hole_is_demonstrated_not_asserted_away
- Input: `backend/tests/test_f12_precision.py::test_the_residual_hole_is_demonstrated_not_asserted_away`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_residual_hole_is_demonstrated_not_asserted_away PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-screen]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-screen]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-screen] PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-dossier]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-dossier]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-dossier] PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-export]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-export]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-export] PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-screen]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-screen]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-screen] PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-dossier]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-dossier]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-dossier] PASSED [ 40%]`

### Scenario: test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-export]
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-export]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-export] PASSED [ 40%]`

### Scenario: test_the_three_surfaces_carry_identical_provenance
- Input: `backend/tests/test_f12_precision.py::test_the_three_surfaces_carry_identical_provenance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_three_surfaces_carry_identical_provenance PASSED [ 40%]`

### Scenario: test_the_acceptance_derived_statement_says_what_the_number_actually_measures
- Input: `backend/tests/test_f12_precision.py::test_the_acceptance_derived_statement_says_what_the_number_actually_measures`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_acceptance_derived_statement_says_what_the_number_actually_measures PASSED [ 41%]`

### Scenario: test_an_acceptance_derived_figure_is_never_promotion_evidence
- Input: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_never_promotion_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_never_promotion_evidence PASSED [ 41%]`

### Scenario: test_precision_is_over_concluded_items_only
- Input: `backend/tests/test_f12_precision.py::test_precision_is_over_concluded_items_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_precision_is_over_concluded_items_only PASSED [ 41%]`

### Scenario: test_a_period_with_no_conclusions_reports_none_not_zero
- Input: `backend/tests/test_f12_precision.py::test_a_period_with_no_conclusions_reports_none_not_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_period_with_no_conclusions_reports_none_not_zero PASSED [ 41%]`

### Scenario: test_a_published_payload_without_a_label_source_fails_the_report
- Input: `backend/tests/test_f12_precision.py::test_a_published_payload_without_a_label_source_fails_the_report`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_published_payload_without_a_label_source_fails_the_report PASSED [ 41%]`

### Scenario: test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business
- Input: `backend/tests/test_f12_precision.py::test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business PASSED [ 41%]`

### Scenario: test_every_render_passes_its_own_boundary_check
- Input: `backend/tests/test_f12_precision.py::test_every_render_passes_its_own_boundary_check`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_every_render_passes_its_own_boundary_check PASSED [ 41%]`

### Scenario: test_the_report_states_each_of_p1_to_p5_individually
- Input: `backend/tests/test_f12_precision.py::test_the_report_states_each_of_p1_to_p5_individually`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_report_states_each_of_p1_to_p5_individually PASSED [ 41%]`

### Scenario: test_a_report_missing_a_condition_cannot_be_constructed
- Input: `backend/tests/test_f12_precision.py::test_a_report_missing_a_condition_cannot_be_constructed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_report_missing_a_condition_cannot_be_constructed PASSED [ 41%]`

### Scenario: test_p1_and_p5_are_reported_not_yet_evaluable_and_name_the_deferral
- Input: `backend/tests/test_f12_precision.py::test_p1_and_p5_are_reported_not_yet_evaluable_and_name_the_deferral`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_p1_and_p5_are_reported_not_yet_evaluable_and_name_the_deferral PASSED [ 41%]`

### Scenario: test_a_caller_cannot_close_the_deferral_by_asserting_p1_or_p5
- Input: `backend/tests/test_f12_precision.py::test_a_caller_cannot_close_the_deferral_by_asserting_p1_or_p5`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_caller_cannot_close_the_deferral_by_asserting_p1_or_p5 PASSED [ 41%]`

### Scenario: test_the_report_is_never_ready_in_this_build
- Input: `backend/tests/test_f12_precision.py::test_the_report_is_never_ready_in_this_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_report_is_never_ready_in_this_build PASSED [ 41%]`

### Scenario: test_readiness_is_computed_from_the_conditions_and_never_from_precision
- Input: `backend/tests/test_f12_precision.py::test_readiness_is_computed_from_the_conditions_and_never_from_precision`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_readiness_is_computed_from_the_conditions_and_never_from_precision PASSED [ 41%]`

### Scenario: test_no_precision_value_moves_readiness
- Input: `backend/tests/test_f12_precision.py::test_no_precision_value_moves_readiness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_no_precision_value_moves_readiness PASSED [ 41%]`

### Scenario: test_readiness_does_not_read_the_figure_at_all
- Input: `backend/tests/test_f12_precision.py::test_readiness_does_not_read_the_figure_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_readiness_does_not_read_the_figure_at_all PASSED [ 42%]`

### Scenario: test_an_acceptance_derived_figure_is_refused_as_promotion_evidence
- Input: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_refused_as_promotion_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_refused_as_promotion_evidence PASSED [ 42%]`

### Scenario: test_a_short_evidence_window_reports_not_yet_evaluable_not_not_met
- Input: `backend/tests/test_f12_precision.py::test_a_short_evidence_window_reports_not_yet_evaluable_not_not_met`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_short_evidence_window_reports_not_yet_evaluable_not_not_met PASSED [ 42%]`

### Scenario: test_the_minimum_window_is_three_closed_periods
- Input: `backend/tests/test_f12_precision.py::test_the_minimum_window_is_three_closed_periods`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_minimum_window_is_three_closed_periods PASSED [ 42%]`

### Scenario: test_a_failed_condition_is_not_met_and_carries_its_reason
- Input: `backend/tests/test_f12_precision.py::test_a_failed_condition_is_not_met_and_carries_its_reason`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_failed_condition_is_not_met_and_carries_its_reason PASSED [ 42%]`

### Scenario: test_the_statement_names_every_blocking_condition
- Input: `backend/tests/test_f12_precision.py::test_the_statement_names_every_blocking_condition`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_the_statement_names_every_blocking_condition PASSED [ 42%]`

### Scenario: test_a_report_with_all_five_met_is_ready_so_the_property_is_not_vacuous
- Input: `backend/tests/test_f12_precision.py::test_a_report_with_all_five_met_is_ready_so_the_property_is_not_vacuous`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_a_report_with_all_five_met_is_ready_so_the_property_is_not_vacuous PASSED [ 42%]`

### Scenario: test_an_unknown_condition_state_is_refused
- Input: `backend/tests/test_f12_precision.py::test_an_unknown_condition_state_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f12_precision.py::test_an_unknown_condition_state_is_refused PASSED [ 42%]`

### Scenario: test_AC_F26_01_the_output_lists_exactly_the_seeded_divergences
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_the_output_lists_exactly_the_seeded_divergences`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_the_output_lists_exactly_the_seeded_divergences PASSED [ 42%]`

### Scenario: test_AC_F26_01_each_divergence_names_account_amount_and_direction
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_each_divergence_names_account_amount_and_direction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_each_divergence_names_account_amount_and_direction PASSED [ 42%]`

### Scenario: test_AC_F26_02_each_divergence_is_attributed_to_a_balance_segment_and_period
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_each_divergence_is_attributed_to_a_balance_segment_and_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_each_divergence_is_attributed_to_a_balance_segment_and_period PASSED [ 42%]`

### Scenario: test_AC_F26_02_the_run_reports_the_totals_it_compared_on_each_side
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_the_run_reports_the_totals_it_compared_on_each_side`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_the_run_reports_the_totals_it_compared_on_each_side PASSED [ 42%]`

### Scenario: test_AC_F26_03_a_tying_fixture_produces_a_stated_zero_at_full_coverage
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_a_tying_fixture_produces_a_stated_zero_at_full_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_a_tying_fixture_produces_a_stated_zero_at_full_coverage PASSED [ 42%]`

### Scenario: test_AC_F26_03_the_zero_conclusion_is_a_full_population_conclusion
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_the_zero_conclusion_is_a_full_population_conclusion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_the_zero_conclusion_is_a_full_population_conclusion PASSED [ 42%]`

### Scenario: test_AC_F26_04_the_missing_batch_names_its_schedule_and_its_population
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_04_the_missing_batch_names_its_schedule_and_its_population`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_04_the_missing_batch_names_its_schedule_and_its_population PASSED [ 42%]`

### Scenario: test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness
- Input: `backend/tests/test_f26_fidelity.py::test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness PASSED [ 43%]`

### Scenario: test_AC_F26_06_an_unavailable_control_extract_reports_not_run_and_names_it
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_an_unavailable_control_extract_reports_not_run_and_names_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_an_unavailable_control_extract_reports_not_run_and_names_it PASSED [ 43%]`

### Scenario: test_AC_F26_06_a_leg_that_did_not_run_reports_no_coverage_figure
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_a_leg_that_did_not_run_reports_no_coverage_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_a_leg_that_did_not_run_reports_no_coverage_figure PASSED [ 43%]`

### Scenario: test_a_refused_run_is_distinguishable_from_a_run_that_started_and_died
- Input: `backend/tests/test_f26_fidelity.py::test_a_refused_run_is_distinguishable_from_a_run_that_started_and_died`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_a_refused_run_is_distinguishable_from_a_run_that_started_and_died PASSED [ 43%]`

### Scenario: test_AC_F26_07_a_complete_f26_run_makes_zero_model_calls
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_07_a_complete_f26_run_makes_zero_model_calls`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_07_a_complete_f26_run_makes_zero_model_calls PASSED [ 43%]`

### Scenario: test_a_model_call_from_inside_an_f26_run_would_raise
- Input: `backend/tests/test_f26_fidelity.py::test_a_model_call_from_inside_an_f26_run_would_raise`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_a_model_call_from_inside_an_f26_run_would_raise PASSED [ 43%]`

### Scenario: test_AC_F26_08_the_smallest_unit_divergence_is_reported_exactly
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_08_the_smallest_unit_divergence_is_reported_exactly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_08_the_smallest_unit_divergence_is_reported_exactly PASSED [ 43%]`

### Scenario: test_AC_F26_09_the_earliest_and_latest_period_divergences_are_both_reported
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_09_the_earliest_and_latest_period_divergences_are_both_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_09_the_earliest_and_latest_period_divergences_are_both_reported PASSED [ 43%]`

### Scenario: test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen PASSED [ 43%]`

### Scenario: test_AC_F26_10_the_coverage_statement_is_on_the_same_screen
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_coverage_statement_is_on_the_same_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_coverage_statement_is_on_the_same_screen PASSED [ 43%]`

### Scenario: test_the_exceptions_screen_is_reachable_from_the_entry_point
- Input: `backend/tests/test_f26_fidelity.py::test_the_exceptions_screen_is_reachable_from_the_entry_point`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_the_exceptions_screen_is_reachable_from_the_entry_point PASSED [ 43%]`

### Scenario: test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen
- Input: `backend/tests/test_f26_fidelity.py::test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen PASSED [ 43%]`

### Scenario: test_the_totals_compared_on_each_side_are_rendered
- Input: `backend/tests/test_f26_fidelity.py::test_the_totals_compared_on_each_side_are_rendered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f26_fidelity.py::test_the_totals_compared_on_each_side_are_rendered PASSED [ 43%]`

### Scenario: test_precision_and_recall_are_numeric_values
- Input: `backend/tests/test_f33_backtest.py::test_precision_and_recall_are_numeric_values`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_precision_and_recall_are_numeric_values PASSED [ 43%]`

### Scenario: test_the_record_names_the_held_out_period_label_count_and_both_versions
- Input: `backend/tests/test_f33_backtest.py::test_the_record_names_the_held_out_period_label_count_and_both_versions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_the_record_names_the_held_out_period_label_count_and_both_versions PASSED [ 44%]`

### Scenario: test_precision_is_none_rather_than_one_when_nothing_was_predicted
- Input: `backend/tests/test_f33_backtest.py::test_precision_is_none_rather_than_one_when_nothing_was_predicted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_precision_is_none_rather_than_one_when_nothing_was_predicted PASSED [ 44%]`

### Scenario: test_a_record_with_no_label_is_invalid_and_raises
- Input: `backend/tests/test_f33_backtest.py::test_a_record_with_no_label_is_invalid_and_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_record_with_no_label_is_invalid_and_raises PASSED [ 44%]`

### Scenario: test_a_record_with_a_whitespace_label_is_invalid
- Input: `backend/tests/test_f33_backtest.py::test_a_record_with_a_whitespace_label_is_invalid`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_record_with_a_whitespace_label_is_invalid PASSED [ 44%]`

### Scenario: test_a_label_that_does_not_carry_the_meaning_is_invalid
- Input: `backend/tests/test_f33_backtest.py::test_a_label_that_does_not_carry_the_meaning_is_invalid`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_label_that_does_not_carry_the_meaning_is_invalid PASSED [ 44%]`

### Scenario: test_a_label_that_drops_the_unknown_clause_is_invalid
- Input: `backend/tests/test_f33_backtest.py::test_a_label_that_drops_the_unknown_clause_is_invalid`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_label_that_drops_the_unknown_clause_is_invalid PASSED [ 44%]`

### Scenario: test_the_default_label_is_the_module_constant
- Input: `backend/tests/test_f33_backtest.py::test_the_default_label_is_the_module_constant`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_the_default_label_is_the_module_constant PASSED [ 44%]`

### Scenario: test_the_label_travels_in_the_payload_beside_the_recall_figure
- Input: `backend/tests/test_f33_backtest.py::test_the_label_travels_in_the_payload_beside_the_recall_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_the_label_travels_in_the_payload_beside_the_recall_figure PASSED [ 44%]`

### Scenario: test_a_held_out_period_with_no_labels_emits_no_figures
- Input: `backend/tests/test_f33_backtest.py::test_a_held_out_period_with_no_labels_emits_no_figures`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_held_out_period_with_no_labels_emits_no_figures PASSED [ 44%]`

### Scenario: test_a_no_labels_result_says_which_period_and_why
- Input: `backend/tests/test_f33_backtest.py::test_a_no_labels_result_says_which_period_and_why`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_no_labels_result_says_which_period_and_why PASSED [ 44%]`

### Scenario: test_a_record_cannot_be_constructed_with_zero_labels_at_all
- Input: `backend/tests/test_f33_backtest.py::test_a_record_cannot_be_constructed_with_zero_labels_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_record_cannot_be_constructed_with_zero_labels_at_all PASSED [ 44%]`

### Scenario: test_one_label_produces_figures_carrying_a_label_count_of_one
- Input: `backend/tests/test_f33_backtest.py::test_one_label_produces_figures_carrying_a_label_count_of_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_one_label_produces_figures_carrying_a_label_count_of_one PASSED [ 44%]`

### Scenario: test_an_unretrievable_label_set_emits_no_accuracy_claim_of_any_kind
- Input: `backend/tests/test_f33_backtest.py::test_an_unretrievable_label_set_emits_no_accuracy_claim_of_any_kind`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_an_unretrievable_label_set_emits_no_accuracy_claim_of_any_kind PASSED [ 44%]`

### Scenario: test_could_not_run_is_a_different_type_from_no_labels
- Input: `backend/tests/test_f33_backtest.py::test_could_not_run_is_a_different_type_from_no_labels`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_could_not_run_is_a_different_type_from_no_labels PASSED [ 44%]`

### Scenario: test_neither_refusal_type_can_be_read_as_a_zero
- Input: `backend/tests/test_f33_backtest.py::test_neither_refusal_type_can_be_read_as_a_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_neither_refusal_type_can_be_read_as_a_zero PASSED [ 45%]`

### Scenario: test_duplicate_predictions_are_counted_once
- Input: `backend/tests/test_f33_backtest.py::test_duplicate_predictions_are_counted_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_duplicate_predictions_are_counted_once PASSED [ 45%]`

### Scenario: test_a_prediction_outside_the_label_set_lowers_precision_not_recall
- Input: `backend/tests/test_f33_backtest.py::test_a_prediction_outside_the_label_set_lowers_precision_not_recall`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_a_prediction_outside_the_label_set_lowers_precision_not_recall PASSED [ 45%]`

### Scenario: test_the_ratios_are_decimal_quantised_not_floats
- Input: `backend/tests/test_f33_backtest.py::test_the_ratios_are_decimal_quantised_not_floats`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_f33_backtest.py::test_the_ratios_are_decimal_quantised_not_floats PASSED [ 45%]`

### Scenario: test_generation_is_deterministic_for_a_seed
- Input: `backend/tests/test_fixture_and_warehouse.py::test_generation_is_deterministic_for_a_seed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_generation_is_deterministic_for_a_seed PASSED [ 45%]`

### Scenario: test_a_different_seed_gives_different_amounts
- Input: `backend/tests/test_fixture_and_warehouse.py::test_a_different_seed_gives_different_amounts`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_a_different_seed_gives_different_amounts PASSED [ 45%]`

### Scenario: test_the_rent_accrual_posts_in_periods_1_to_11_and_is_absent_in_12
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_rent_accrual_posts_in_periods_1_to_11_and_is_absent_in_12`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_rent_accrual_posts_in_periods_1_to_11_and_is_absent_in_12 PASSED [ 45%]`

### Scenario: test_the_insurance_accrual_posts_in_all_twelve_periods
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_insurance_accrual_posts_in_all_twelve_periods`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_insurance_accrual_posts_in_all_twelve_periods PASSED [ 45%]`

### Scenario: test_the_utilities_accrual_is_present_in_period_12_but_far_above_its_history
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_utilities_accrual_is_present_in_period_12_but_far_above_its_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_utilities_accrual_is_present_in_period_12_but_far_above_its_history PASSED [ 45%]`

### Scenario: test_the_bonus_accrual_has_less_than_six_periods_of_history
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_bonus_accrual_has_less_than_six_periods_of_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_bonus_accrual_has_less_than_six_periods_of_history PASSED [ 45%]`

### Scenario: test_injection_payloads_are_planted_in_line_descriptions
- Input: `backend/tests/test_fixture_and_warehouse.py::test_injection_payloads_are_planted_in_line_descriptions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_injection_payloads_are_planted_in_line_descriptions PASSED [ 45%]`

### Scenario: test_personal_data_columns_are_populated
- Input: `backend/tests/test_fixture_and_warehouse.py::test_personal_data_columns_are_populated`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_personal_data_columns_are_populated PASSED [ 45%]`

### Scenario: test_amounts_are_decimal_strings_never_floats
- Input: `backend/tests/test_fixture_and_warehouse.py::test_amounts_are_decimal_strings_never_floats`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_amounts_are_decimal_strings_never_floats PASSED [ 45%]`

### Scenario: test_balances_are_derived_from_the_lines
- Input: `backend/tests/test_fixture_and_warehouse.py::test_balances_are_derived_from_the_lines`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_balances_are_derived_from_the_lines PASSED [ 45%]`

### Scenario: test_background_traffic_exists_so_recurring_members_are_not_the_whole_ledger
- Input: `backend/tests/test_fixture_and_warehouse.py::test_background_traffic_exists_so_recurring_members_are_not_the_whole_ledger`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_background_traffic_exists_so_recurring_members_are_not_the_whole_ledger PASSED [ 46%]`

### Scenario: test_seeding_is_idempotent
- Input: `backend/tests/test_fixture_and_warehouse.py::test_seeding_is_idempotent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_seeding_is_idempotent PASSED [ 46%]`

### Scenario: test_the_read_connection_refuses_a_write
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_read_connection_refuses_a_write`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_read_connection_refuses_a_write PASSED [ 46%]`

### Scenario: test_fetch_binds_parameters
- Input: `backend/tests/test_fixture_and_warehouse.py::test_fetch_binds_parameters`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_fetch_binds_parameters PASSED [ 46%]`

### Scenario: test_no_warehouse_without_a_credential
- Input: `backend/tests/test_fixture_and_warehouse.py::test_no_warehouse_without_a_credential`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_no_warehouse_without_a_credential PASSED [ 46%]`

### Scenario: test_the_warehouse_credential_cannot_be_resolved_from_the_api_process
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_warehouse_credential_cannot_be_resolved_from_the_api_process`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_the_warehouse_credential_cannot_be_resolved_from_the_api_process PASSED [ 46%]`

### Scenario: test_a_non_sqlite_dsn_is_refused_rather_than_half_supported
- Input: `backend/tests/test_fixture_and_warehouse.py::test_a_non_sqlite_dsn_is_refused_rather_than_half_supported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_a_non_sqlite_dsn_is_refused_rather_than_half_supported PASSED [ 46%]`

### Scenario: test_from_credential_builds_a_usable_warehouse
- Input: `backend/tests/test_fixture_and_warehouse.py::test_from_credential_builds_a_usable_warehouse`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fixture_and_warehouse.py::test_from_credential_builds_a_usable_warehouse PASSED [ 46%]`

### Scenario: test_the_emission_leg_is_actually_reachable_before_anything_is_claimed_about_it
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_is_actually_reachable_before_anything_is_claimed_about_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_is_actually_reachable_before_anything_is_claimed_about_it PASSED [ 46%]`

### Scenario: test_override_is_not_in_the_forward_closure_of_any_emission_state
- Input: `backend/tests/test_fsm_emission_leg.py::test_override_is_not_in_the_forward_closure_of_any_emission_state`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_override_is_not_in_the_forward_closure_of_any_emission_state PASSED [ 46%]`

### Scenario: test_no_emission_state_is_an_ancestor_of_override
- Input: `backend/tests/test_fsm_emission_leg.py::test_no_emission_state_is_an_ancestor_of_override`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_no_emission_state_is_an_ancestor_of_override PASSED [ 46%]`

### Scenario: test_every_whole_path_that_touches_the_emission_leg_avoids_override
- Input: `backend/tests/test_fsm_emission_leg.py::test_every_whole_path_that_touches_the_emission_leg_avoids_override`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_every_whole_path_that_touches_the_emission_leg_avoids_override PASSED [ 46%]`

### Scenario: test_the_emission_leg_reaches_abstained_and_the_action_leg_does_not
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_reaches_abstained_and_the_action_leg_does_not`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_reaches_abstained_and_the_action_leg_does_not PASSED [ 46%]`

### Scenario: test_abstained_is_terminal_and_cannot_be_resumed_into_an_override
- Input: `backend/tests/test_fsm_emission_leg.py::test_abstained_is_terminal_and_cannot_be_resumed_into_an_override`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_abstained_is_terminal_and_cannot_be_resumed_into_an_override PASSED [ 46%]`

### Scenario: test_the_declared_emission_transitions_are_the_only_ones_out_of_the_leg
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_declared_emission_transitions_are_the_only_ones_out_of_the_leg`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_the_declared_emission_transitions_are_the_only_ones_out_of_the_leg PASSED [ 46%]`

### Scenario: test_terminal_states_map_to_distinct_outcome_values
- Input: `backend/tests/test_fsm_emission_leg.py::test_terminal_states_map_to_distinct_outcome_values`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_terminal_states_map_to_distinct_outcome_values PASSED [ 47%]`

### Scenario: test_an_abstention_and_a_denial_are_separate_rows_with_separate_outcomes
- Input: `backend/tests/test_fsm_emission_leg.py::test_an_abstention_and_a_denial_are_separate_rows_with_separate_outcomes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_an_abstention_and_a_denial_are_separate_rows_with_separate_outcomes PASSED [ 47%]`

### Scenario: test_the_outcome_column_admits_abstain_as_a_peer_of_deny_not_as_a_reason_string
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_outcome_column_admits_abstain_as_a_peer_of_deny_not_as_a_reason_string`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_the_outcome_column_admits_abstain_as_a_peer_of_deny_not_as_a_reason_string PASSED [ 47%]`

### Scenario: test_a_denial_count_over_a_period_excludes_abstentions
- Input: `backend/tests/test_fsm_emission_leg.py::test_a_denial_count_over_a_period_excludes_abstentions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_a_denial_count_over_a_period_excludes_abstentions PASSED [ 47%]`

### Scenario: test_abstentions_survive_the_mirror_into_the_evidence_chain_as_abstentions
- Input: `backend/tests/test_fsm_emission_leg.py::test_abstentions_survive_the_mirror_into_the_evidence_chain_as_abstentions`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_fsm_emission_leg.py::test_abstentions_survive_the_mirror_into_the_evidence_chain_as_abstentions PASSED [ 47%]`

### Scenario: test_the_route_is_on_the_ges_surface_and_the_health_report_names_it
- Input: `backend/tests/test_ges_decide_route.py::test_the_route_is_on_the_ges_surface_and_the_health_report_names_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_route_is_on_the_ges_surface_and_the_health_report_names_it PASSED [ 47%]`

### Scenario: test_an_allowed_action_comes_back_as_an_allow_with_a_decision_id
- Input: `backend/tests/test_ges_decide_route.py::test_an_allowed_action_comes_back_as_an_allow_with_a_decision_id`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_allowed_action_comes_back_as_an_allow_with_a_decision_id PASSED [ 47%]`

### Scenario: test_a_denial_is_a_two_hundred_carrying_the_reason_not_an_http_error
- Input: `backend/tests/test_ges_decide_route.py::test_a_denial_is_a_two_hundred_carrying_the_reason_not_an_http_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_a_denial_is_a_two_hundred_carrying_the_reason_not_an_http_error PASSED [ 47%]`

### Scenario: test_the_client_refuses_to_read_a_non_two_hundred_as_a_denial
- Input: `backend/tests/test_ges_decide_route.py::test_the_client_refuses_to_read_a_non_two_hundred_as_a_denial`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_client_refuses_to_read_a_non_two_hundred_as_a_denial PASSED [ 47%]`

### Scenario: test_an_unknown_principal_is_refused_rather_than_defaulted
- Input: `backend/tests/test_ges_decide_route.py::test_an_unknown_principal_is_refused_rather_than_defaulted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_unknown_principal_is_refused_rather_than_defaulted PASSED [ 47%]`

### Scenario: test_the_route_requires_the_loopback_client_token
- Input: `backend/tests/test_ges_decide_route.py::test_the_route_requires_the_loopback_client_token`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_route_requires_the_loopback_client_token PASSED [ 47%]`

### Scenario: test_naming_someone_else_as_the_approver_is_refused_as_impersonation
- Input: `backend/tests/test_ges_decide_route.py::test_naming_someone_else_as_the_approver_is_refused_as_impersonation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_naming_someone_else_as_the_approver_is_refused_as_impersonation PASSED [ 47%]`

### Scenario: test_an_agent_asking_to_approve_is_denied_before_any_rule_runs
- Input: `backend/tests/test_ges_decide_route.py::test_an_agent_asking_to_approve_is_denied_before_any_rule_runs`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_agent_asking_to_approve_is_denied_before_any_rule_runs PASSED [ 47%]`

### Scenario: test_an_approval_within_the_limit_is_allowed
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_within_the_limit_is_allowed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_approval_within_the_limit_is_allowed PASSED [ 47%]`

### Scenario: test_an_approval_above_the_limit_is_denied_and_is_override_eligible
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_above_the_limit_is_denied_and_is_override_eligible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_approval_above_the_limit_is_denied_and_is_override_eligible PASSED [ 48%]`

### Scenario: test_an_approval_exactly_at_the_limit_is_allowed_because_the_rule_is_inclusive
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_exactly_at_the_limit_is_allowed_because_the_rule_is_inclusive`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_approval_exactly_at_the_limit_is_allowed_because_the_rule_is_inclusive PASSED [ 48%]`

### Scenario: test_an_identity_denial_is_not_override_eligible
- Input: `backend/tests/test_ges_decide_route.py::test_an_identity_denial_is_not_override_eligible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_identity_denial_is_not_override_eligible PASSED [ 48%]`

### Scenario: test_an_override_presented_against_an_ineligible_denial_is_refused_at_the_broker
- Input: `backend/tests/test_ges_decide_route.py::test_an_override_presented_against_an_ineligible_denial_is_refused_at_the_broker`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_override_presented_against_an_ineligible_denial_is_refused_at_the_broker PASSED [ 48%]`

### Scenario: test_an_override_against_an_eligible_denial_is_consumed_exactly_once
- Input: `backend/tests/test_ges_decide_route.py::test_an_override_against_an_eligible_denial_is_consumed_exactly_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_an_override_against_an_eligible_denial_is_consumed_exactly_once PASSED [ 48%]`

### Scenario: test_a_reason_code_outside_the_closed_list_is_refused
- Input: `backend/tests/test_ges_decide_route.py::test_a_reason_code_outside_the_closed_list_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_a_reason_code_outside_the_closed_list_is_refused PASSED [ 48%]`

### Scenario: test_the_second_authoriser_may_not_be_the_requester
- Input: `backend/tests/test_ges_decide_route.py::test_the_second_authoriser_may_not_be_the_requester`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_second_authoriser_may_not_be_the_requester PASSED [ 48%]`

### Scenario: test_the_bundle_endpoint_serves_the_closed_reason_list_so_no_ui_holds_one
- Input: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_serves_the_closed_reason_list_so_no_ui_holds_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_serves_the_closed_reason_list_so_no_ui_holds_one PASSED [ 48%]`

### Scenario: test_the_bundle_endpoint_exposes_no_rule_source_and_no_secret
- Input: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_exposes_no_rule_source_and_no_secret`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_exposes_no_rule_source_and_no_secret PASSED [ 48%]`

### Scenario: test_the_decide_route_has_no_field_that_could_carry_a_statement
- Input: `backend/tests/test_ges_decide_route.py::test_the_decide_route_has_no_field_that_could_carry_a_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_the_decide_route_has_no_field_that_could_carry_a_statement PASSED [ 48%]`

### Scenario: test_a_sql_string_smuggled_through_the_payload_reaches_no_evaluator
- Input: `backend/tests/test_ges_decide_route.py::test_a_sql_string_smuggled_through_the_payload_reaches_no_evaluator`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ges_decide_route.py::test_a_sql_string_smuggled_through_the_payload_reaches_no_evaluator PASSED [ 48%]`

### Scenario: test_the_flag_is_off_by_default
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_off_by_default`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_the_flag_is_off_by_default PASSED [ 48%]`

### Scenario: test_the_flag_is_set_inside_and_cleared_after
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_set_inside_and_cleared_after`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_the_flag_is_set_inside_and_cleared_after PASSED [ 48%]`

### Scenario: test_the_flag_is_cleared_even_if_the_block_raises
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_cleared_even_if_the_block_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_the_flag_is_cleared_even_if_the_block_raises PASSED [ 48%]`

### Scenario: test_nesting_restores_the_outer_state
- Input: `backend/tests/test_model_guard.py::test_nesting_restores_the_outer_state`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_nesting_restores_the_outer_state PASSED [ 49%]`

### Scenario: test_a_model_call_from_a_deterministic_section_raises
- Input: `backend/tests/test_model_guard.py::test_a_model_call_from_a_deterministic_section_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_a_model_call_from_a_deterministic_section_raises PASSED [ 49%]`

### Scenario: test_a_forbidden_call_is_not_counted_as_an_invocation
- Input: `backend/tests/test_model_guard.py::test_a_forbidden_call_is_not_counted_as_an_invocation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_a_forbidden_call_is_not_counted_as_an_invocation PASSED [ 49%]`

### Scenario: test_a_call_outside_a_deterministic_section_is_counted_then_unimplemented
- Input: `backend/tests/test_model_guard.py::test_a_call_outside_a_deterministic_section_is_counted_then_unimplemented`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_a_call_outside_a_deterministic_section_is_counted_then_unimplemented PASSED [ 49%]`

### Scenario: test_the_flag_does_not_leak_across_threads
- Input: `backend/tests/test_model_guard.py::test_the_flag_does_not_leak_across_threads`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_model_guard.py::test_the_flag_does_not_leak_across_threads PASSED [ 49%]`

### Scenario: test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types0]
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types0] PASSED [ 49%]`

### Scenario: test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types1]
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types1] PASSED [ 49%]`

### Scenario: test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types2]
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types2] PASSED [ 49%]`

### Scenario: test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types3]
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types3]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types3] PASSED [ 49%]`

### Scenario: test_a_safe_option_existing_alongside_a_posting_one_does_not_make_it_cold
- Input: `backend/tests/test_policy_cold.py::test_a_safe_option_existing_alongside_a_posting_one_does_not_make_it_cold`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_safe_option_existing_alongside_a_posting_one_does_not_make_it_cold PASSED [ 49%]`

### Scenario: test_the_posting_capable_test_runs_before_any_rule_can_match
- Input: `backend/tests/test_policy_cold.py::test_the_posting_capable_test_runs_before_any_rule_can_match`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_posting_capable_test_runs_before_any_rule_can_match PASSED [ 49%]`

### Scenario: test_a_cold_rule_that_disposes_as_a_posting_type_is_not_constructible
- Input: `backend/tests/test_policy_cold.py::test_a_cold_rule_that_disposes_as_a_posting_type_is_not_constructible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_cold_rule_that_disposes_as_a_posting_type_is_not_constructible PASSED [ 49%]`

### Scenario: test_there_is_no_argument_that_makes_a_posting_capable_finding_cold
- Input: `backend/tests/test_policy_cold.py::test_there_is_no_argument_that_makes_a_posting_capable_finding_cold`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_there_is_no_argument_that_makes_a_posting_capable_finding_cold PASSED [ 49%]`

### Scenario: test_no_rule_matching_also_routes_hot
- Input: `backend/tests/test_policy_cold.py::test_no_rule_matching_also_routes_hot`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_no_rule_matching_also_routes_hot PASSED [ 49%]`

### Scenario: test_a_matched_finding_is_auto_disposed_and_records_its_provenance
- Input: `backend/tests/test_policy_cold.py::test_a_matched_finding_is_auto_disposed_and_records_its_provenance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_matched_finding_is_auto_disposed_and_records_its_provenance PASSED [ 50%]`

### Scenario: test_the_exception_row_carries_the_marker_the_rule_and_the_dossier_ref
- Input: `backend/tests/test_policy_cold.py::test_the_exception_row_carries_the_marker_the_rule_and_the_dossier_ref`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_exception_row_carries_the_marker_the_rule_and_the_dossier_ref PASSED [ 50%]`

### Scenario: test_a_hot_row_is_not_marked_auto_disposed
- Input: `backend/tests/test_policy_cold.py::test_a_hot_row_is_not_marked_auto_disposed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_hot_row_is_not_marked_auto_disposed PASSED [ 50%]`

### Scenario: test_the_first_matching_rule_wins_and_the_record_names_it
- Input: `backend/tests/test_policy_cold.py::test_the_first_matching_rule_wins_and_the_record_names_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_first_matching_rule_wins_and_the_record_names_it PASSED [ 50%]`

### Scenario: test_the_first_period_states_two_further_periods_would_escalate
- Input: `backend/tests/test_policy_cold.py::test_the_first_period_states_two_further_periods_would_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_first_period_states_two_further_periods_would_escalate PASSED [ 50%]`

### Scenario: test_exactly_two_consecutive_periods_raises_no_escalation_and_states_the_count
- Input: `backend/tests/test_policy_cold.py::test_exactly_two_consecutive_periods_raises_no_escalation_and_states_the_count`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_exactly_two_consecutive_periods_raises_no_escalation_and_states_the_count PASSED [ 50%]`

### Scenario: test_the_third_consecutive_period_escalates_hot_and_names_all_three
- Input: `backend/tests/test_policy_cold.py::test_the_third_consecutive_period_escalates_hot_and_names_all_three`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_third_consecutive_period_escalates_hot_and_names_all_three PASSED [ 50%]`

### Scenario: test_the_third_period_is_not_auto_disposed
- Input: `backend/tests/test_policy_cold.py::test_the_third_period_is_not_auto_disposed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_third_period_is_not_auto_disposed PASSED [ 50%]`

### Scenario: test_THE_control_the_escalation_holds_regardless_of_which_rule_disposed
- Input: `backend/tests/test_policy_cold.py::test_THE_control_the_escalation_holds_regardless_of_which_rule_disposed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_THE_control_the_escalation_holds_regardless_of_which_rule_disposed PASSED [ 50%]`

### Scenario: test_three_different_rules_still_escalate
- Input: `backend/tests/test_policy_cold.py::test_three_different_rules_still_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_three_different_rules_still_escalate PASSED [ 50%]`

### Scenario: test_the_escalation_counter_is_keyed_on_account_and_direction_only
- Input: `backend/tests/test_policy_cold.py::test_the_escalation_counter_is_keyed_on_account_and_direction_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_escalation_counter_is_keyed_on_account_and_direction_only PASSED [ 50%]`

### Scenario: test_a_gap_breaks_the_streak
- Input: `backend/tests/test_policy_cold.py::test_a_gap_breaks_the_streak`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_gap_breaks_the_streak PASSED   [ 50%]`

### Scenario: test_after_a_gap_three_fresh_consecutive_periods_escalate
- Input: `backend/tests/test_policy_cold.py::test_after_a_gap_three_fresh_consecutive_periods_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_after_a_gap_three_fresh_consecutive_periods_escalate PASSED [ 50%]`

### Scenario: test_consecutive_run_length[periods0-12-expected0]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods0-12-expected0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods0-12-expected0] PASSED [ 50%]`

### Scenario: test_consecutive_run_length[periods1-12-expected1]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods1-12-expected1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods1-12-expected1] PASSED [ 50%]`

### Scenario: test_consecutive_run_length[periods2-12-expected2]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods2-12-expected2]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods2-12-expected2] PASSED [ 51%]`

### Scenario: test_consecutive_run_length[periods3-12-expected3]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods3-12-expected3]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods3-12-expected3] PASSED [ 51%]`

### Scenario: test_consecutive_run_length[periods4-13-expected4]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods4-13-expected4]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods4-13-expected4] PASSED [ 51%]`

### Scenario: test_consecutive_run_length[periods5-12-expected5]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods5-12-expected5]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods5-12-expected5] PASSED [ 51%]`

### Scenario: test_consecutive_run_length[periods6-12-expected6]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods6-12-expected6]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods6-12-expected6] PASSED [ 51%]`

### Scenario: test_consecutive_run_length[periods7-12-expected7]
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods7-12-expected7]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods7-12-expected7] PASSED [ 51%]`

### Scenario: test_a_different_account_has_its_own_streak
- Input: `backend/tests/test_policy_cold.py::test_a_different_account_has_its_own_streak`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_different_account_has_its_own_streak PASSED [ 51%]`

### Scenario: test_the_other_direction_has_its_own_streak
- Input: `backend/tests/test_policy_cold.py::test_the_other_direction_has_its_own_streak`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_other_direction_has_its_own_streak PASSED [ 51%]`

### Scenario: test_the_same_account_and_direction_share_one_streak
- Input: `backend/tests/test_policy_cold.py::test_the_same_account_and_direction_share_one_streak`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_same_account_and_direction_share_one_streak PASSED [ 51%]`

### Scenario: test_a_finding_cannot_be_disposed_twice
- Input: `backend/tests/test_policy_cold.py::test_a_finding_cannot_be_disposed_twice`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_finding_cannot_be_disposed_twice PASSED [ 51%]`

### Scenario: test_a_hot_route_reason_outside_the_closed_set_is_unstorable
- Input: `backend/tests/test_policy_cold.py::test_a_hot_route_reason_outside_the_closed_set_is_unstorable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_a_hot_route_reason_outside_the_closed_set_is_unstorable PASSED [ 51%]`

### Scenario: test_an_unknown_resolution_type_is_refused_at_the_door
- Input: `backend/tests/test_policy_cold.py::test_an_unknown_resolution_type_is_refused_at_the_door`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_an_unknown_resolution_type_is_refused_at_the_door PASSED [ 51%]`

### Scenario: test_the_escalation_threshold_is_three_and_is_named_not_inlined
- Input: `backend/tests/test_policy_cold.py::test_the_escalation_threshold_is_three_and_is_named_not_inlined`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_policy_cold.py::test_the_escalation_threshold_is_three_and_is_named_not_inlined PASSED [ 51%]`

### Scenario: test_the_committed_population_compiles
- Input: `backend/tests/test_population_and_coverage.py::test_the_committed_population_compiles`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_the_committed_population_compiles PASSED [ 51%]`

### Scenario: test_the_population_object_has_no_attribute_that_could_hold_a_table_name
- Input: `backend/tests/test_population_and_coverage.py::test_the_population_object_has_no_attribute_that_could_hold_a_table_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_the_population_object_has_no_attribute_that_could_hold_a_table_name PASSED [ 52%]`

### Scenario: test_member_and_segment_extraction
- Input: `backend/tests/test_population_and_coverage.py::test_member_and_segment_extraction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_member_and_segment_extraction PASSED [ 52%]`

### Scenario: test_a_row_missing_a_member_key_component_raises_rather_than_defaulting
- Input: `backend/tests/test_population_and_coverage.py::test_a_row_missing_a_member_key_component_raises_rather_than_defaulting`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_row_missing_a_member_key_component_raises_rather_than_defaulting PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[table]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table] PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[table_name]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table_name]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table_name] PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[schema]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[schema]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[schema] PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[from]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[from]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[from] PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[sql_file]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[sql_file]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[sql_file] PASSED [ 52%]`

### Scenario: test_a_manifest_key_naming_where_data_lives_fails_the_build[view]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[view]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[view] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_je_lines]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_je_lines]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_je_lines] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_balances]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_balances]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_balances] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_je_lines]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_je_lines]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_je_lines] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_balances]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_balances]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_balances] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[wh_account_balances]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[wh_account_balances]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[wh_account_balances] PASSED [ 52%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[erp_control_extract]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[erp_control_extract]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[erp_control_extract] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[load_batches]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[load_batches]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[load_batches] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[subledger_control_tieout]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[subledger_control_tieout]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[subledger_control_tieout] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[intercompany_pairs]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[intercompany_pairs]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[intercompany_pairs] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[account_rollforward]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_rollforward]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_rollforward] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[fx_revaluation]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[fx_revaluation]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[fx_revaluation] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[suspense_residuals]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[suspense_residuals]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[suspense_residuals] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[account_movements]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_movements]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_movements] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[period_explanations]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[period_explanations]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[period_explanations] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[coded_postings]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[coded_postings]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[coded_postings] PASSED [ 53%]`

### Scenario: test_a_manifest_mentioning_a_physical_object_fails_the_build[reclass_labels]
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[reclass_labels]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[reclass_labels] PASSED [ 53%]`

### Scenario: test_a_nested_physical_object_reference_is_also_caught
- Input: `backend/tests/test_population_and_coverage.py::test_a_nested_physical_object_reference_is_also_caught`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_nested_physical_object_reference_is_also_caught PASSED [ 53%]`

### Scenario: test_source_class_is_a_closed_enum
- Input: `backend/tests/test_population_and_coverage.py::test_source_class_is_a_closed_enum`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_source_class_is_a_closed_enum PASSED [ 53%]`

### Scenario: test_phase_2_source_classes_are_already_permitted
- Input: `backend/tests/test_population_and_coverage.py::test_phase_2_source_classes_are_already_permitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_phase_2_source_classes_are_already_permitted PASSED [ 53%]`

### Scenario: test_a_missing_member_key_fails_the_build
- Input: `backend/tests/test_population_and_coverage.py::test_a_missing_member_key_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_missing_member_key_fails_the_build PASSED [ 53%]`

### Scenario: test_a_missing_resolver_query_fails_the_build
- Input: `backend/tests/test_population_and_coverage.py::test_a_missing_resolver_query_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_missing_resolver_query_fails_the_build PASSED [ 54%]`

### Scenario: test_a_segment_outside_the_member_key_fails_the_build
- Input: `backend/tests/test_population_and_coverage.py::test_a_segment_outside_the_member_key_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_segment_outside_the_member_key_fails_the_build PASSED [ 54%]`

### Scenario: test_a_duplicate_population_fails_the_build
- Input: `backend/tests/test_population_and_coverage.py::test_a_duplicate_population_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_a_duplicate_population_fails_the_build PASSED [ 54%]`

### Scenario: test_an_empty_population_directory_fails_the_build
- Input: `backend/tests/test_population_and_coverage.py::test_an_empty_population_directory_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_an_empty_population_directory_fails_the_build PASSED [ 54%]`

### Scenario: test_full_coverage
- Input: `backend/tests/test_population_and_coverage.py::test_full_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_full_coverage PASSED [ 54%]`

### Scenario: test_partial_coverage_names_its_gaps
- Input: `backend/tests/test_population_and_coverage.py::test_partial_coverage_names_its_gaps`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_partial_coverage_names_its_gaps PASSED [ 54%]`

### Scenario: test_zero_coverage
- Input: `backend/tests/test_population_and_coverage.py::test_zero_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_zero_coverage PASSED [ 54%]`

### Scenario: test_an_empty_declared_population_is_not_complete
- Input: `backend/tests/test_population_and_coverage.py::test_an_empty_declared_population_is_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_an_empty_declared_population_is_not_complete PASSED [ 54%]`

### Scenario: test_covering_an_undeclared_member_does_not_inflate_coverage
- Input: `backend/tests/test_population_and_coverage.py::test_covering_an_undeclared_member_does_not_inflate_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_covering_an_undeclared_member_does_not_inflate_coverage PASSED [ 54%]`

### Scenario: test_percent_rounds_down_so_a_bounded_run_never_reads_as_complete
- Input: `backend/tests/test_population_and_coverage.py::test_percent_rounds_down_so_a_bounded_run_never_reads_as_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_percent_rounds_down_so_a_bounded_run_never_reads_as_complete PASSED [ 54%]`

### Scenario: test_scope_serialises_with_its_gaps
- Input: `backend/tests/test_population_and_coverage.py::test_scope_serialises_with_its_gaps`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_population_and_coverage.py::test_scope_serialises_with_its_gaps PASSED [ 54%]`

### Scenario: test_a_batch_that_arrived_on_time_produces_no_finding
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_on_time_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_on_time_produces_no_finding PASSED [ 54%]`

### Scenario: test_a_batch_that_never_arrived_names_itself_its_schedule_and_its_population
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_never_arrived_names_itself_its_schedule_and_its_population`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_batch_that_never_arrived_names_itself_its_schedule_and_its_population PASSED [ 54%]`

### Scenario: test_a_batch_that_arrived_carrying_zero_rows_is_not_a_missing_batch
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_carrying_zero_rows_is_not_a_missing_batch`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_carrying_zero_rows_is_not_a_missing_batch PASSED [ 54%]`

### Scenario: test_a_late_batch_is_a_finding_of_its_own_kind
- Input: `backend/tests/test_primitive_freshness.py::test_a_late_batch_is_a_finding_of_its_own_kind`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_late_batch_is_a_finding_of_its_own_kind PASSED [ 55%]`

### Scenario: test_a_batch_arriving_exactly_on_its_expected_time_is_not_late
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_arriving_exactly_on_its_expected_time_is_not_late`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_batch_arriving_exactly_on_its_expected_time_is_not_late PASSED [ 55%]`

### Scenario: test_a_declared_batch_with_no_schedule_row_is_uncovered_and_named
- Input: `backend/tests/test_primitive_freshness.py::test_a_declared_batch_with_no_schedule_row_is_uncovered_and_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_declared_batch_with_no_schedule_row_is_uncovered_and_named PASSED [ 55%]`

### Scenario: test_an_empty_string_arrival_counts_as_never_arrived
- Input: `backend/tests/test_primitive_freshness.py::test_an_empty_string_arrival_counts_as_never_arrived`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_an_empty_string_arrival_counts_as_never_arrived PASSED [ 55%]`

### Scenario: test_every_run_states_that_staleness_is_not_close_clock_relative
- Input: `backend/tests/test_primitive_freshness.py::test_every_run_states_that_staleness_is_not_close_clock_relative`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_every_run_states_that_staleness_is_not_close_clock_relative PASSED [ 55%]`

### Scenario: test_the_summary_reports_no_close_clock_rather_than_a_close_relative_figure
- Input: `backend/tests/test_primitive_freshness.py::test_the_summary_reports_no_close_clock_rather_than_a_close_relative_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_the_summary_reports_no_close_clock_rather_than_a_close_relative_figure PASSED [ 55%]`

### Scenario: test_the_latest_arrival_is_reported_as_an_absolute_time_and_labelled_as_such
- Input: `backend/tests/test_primitive_freshness.py::test_the_latest_arrival_is_reported_as_an_absolute_time_and_labelled_as_such`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_the_latest_arrival_is_reported_as_an_absolute_time_and_labelled_as_such PASSED [ 55%]`

### Scenario: test_a_run_over_no_batches_still_reports_the_missing_close_clock
- Input: `backend/tests/test_primitive_freshness.py::test_a_run_over_no_batches_still_reports_the_missing_close_clock`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_freshness.py::test_a_run_over_no_batches_still_reports_the_missing_close_clock PASSED [ 55%]`

### Scenario: test_equal_sides_produce_no_finding_and_a_covered_member
- Input: `backend/tests/test_primitive_identity_tieout.py::test_equal_sides_produce_no_finding_and_a_covered_member`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_equal_sides_produce_no_finding_and_a_covered_member PASSED [ 55%]`

### Scenario: test_the_totals_are_reported_even_when_nothing_diverges
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_totals_are_reported_even_when_nothing_diverges`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_totals_are_reported_even_when_nothing_diverges PASSED [ 55%]`

### Scenario: test_a_divergence_names_its_amount_and_direction
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_divergence_names_its_amount_and_direction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_divergence_names_its_amount_and_direction PASSED [ 55%]`

### Scenario: test_the_other_direction_is_named_as_the_other_side
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_other_direction_is_named_as_the_other_side`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_other_direction_is_named_as_the_other_side PASSED [ 55%]`

### Scenario: test_the_smallest_currency_unit_is_reported_and_reported_exactly
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_smallest_currency_unit_is_reported_and_reported_exactly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_smallest_currency_unit_is_reported_and_reported_exactly PASSED [ 55%]`

### Scenario: test_the_default_tolerance_is_zero_so_a_one_cent_break_is_a_finding
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_default_tolerance_is_zero_so_a_one_cent_break_is_a_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_default_tolerance_is_zero_so_a_one_cent_break_is_a_finding PASSED [ 55%]`

### Scenario: test_the_tolerance_boundary_is_inclusive[0.99-0]
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[0.99-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[0.99-0] PASSED [ 56%]`

### Scenario: test_the_tolerance_boundary_is_inclusive[1.00-0]
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.00-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.00-0] PASSED [ 56%]`

### Scenario: test_the_tolerance_boundary_is_inclusive[1.01-1]
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.01-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.01-1] PASSED [ 56%]`

### Scenario: test_a_negative_difference_is_compared_on_its_magnitude
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_negative_difference_is_compared_on_its_magnitude`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_negative_difference_is_compared_on_its_magnitude PASSED [ 56%]`

### Scenario: test_a_member_present_on_the_left_only_is_a_one_sided_finding
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_left_only_is_a_one_sided_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_left_only_is_a_one_sided_finding PASSED [ 56%]`

### Scenario: test_a_member_present_on_the_right_only_names_the_other_side
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_right_only_names_the_other_side`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_right_only_names_the_other_side PASSED [ 56%]`

### Scenario: test_an_empty_string_is_treated_as_absent_not_as_zero
- Input: `backend/tests/test_primitive_identity_tieout.py::test_an_empty_string_is_treated_as_absent_not_as_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_an_empty_string_is_treated_as_absent_not_as_zero PASSED [ 56%]`

### Scenario: test_a_one_sided_member_is_still_covered
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_one_sided_member_is_still_covered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_one_sided_member_is_still_covered PASSED [ 56%]`

### Scenario: test_a_declared_member_with_no_row_is_uncovered_and_named
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_declared_member_with_no_row_is_uncovered_and_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_declared_member_with_no_row_is_uncovered_and_named PASSED [ 56%]`

### Scenario: test_a_missing_member_produces_no_finding_of_any_kind
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_missing_member_produces_no_finding_of_any_kind`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_a_missing_member_produces_no_finding_of_any_kind PASSED [ 56%]`

### Scenario: test_the_field_and_label_parameters_make_this_the_a6_check_too
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_field_and_label_parameters_make_this_the_a6_check_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_identity_tieout.py::test_the_field_and_label_parameters_make_this_the_a6_check_too PASSED [ 56%]`

### Scenario: test_a_cost_centre_divergence_names_both_codings_and_its_evidence
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cost_centre_divergence_names_both_codings_and_its_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_cost_centre_divergence_names_both_codings_and_its_evidence PASSED [ 56%]`

### Scenario: test_a_natural_account_divergence_confirms_both_are_in_the_same_caption
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_natural_account_divergence_confirms_both_are_in_the_same_caption`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_natural_account_divergence_confirms_both_are_in_the_same_caption PASSED [ 56%]`

### Scenario: test_a_correctly_coded_posting_produces_no_finding
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_correctly_coded_posting_produces_no_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_correctly_coded_posting_produces_no_finding PASSED [ 56%]`

### Scenario: test_an_intercompany_segment_miscoding_emits_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_segment_miscoding_emits_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_segment_miscoding_emits_no_proposal PASSED [ 57%]`

### Scenario: test_a_caption_crossing_emits_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_emits_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_emits_no_proposal PASSED [ 57%]`

### Scenario: test_a_cut_off_error_says_cut_off_resolution_is_not_proposed
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_error_says_cut_off_resolution_is_not_proposed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_error_says_cut_off_resolution_is_not_proposed PASSED [ 57%]`

### Scenario: test_the_proposal_field_is_ABSENT_rather_than_present_and_blocked
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_proposal_field_is_ABSENT_rather_than_present_and_blocked`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_the_proposal_field_is_ABSENT_rather_than_present_and_blocked PASSED [ 57%]`

### Scenario: test_a_caption_crossing_that_also_diverges_on_cost_centre_emits_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_that_also_diverges_on_cost_centre_emits_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_that_also_diverges_on_cost_centre_emits_no_proposal PASSED [ 57%]`

### Scenario: test_a_cut_off_that_also_diverges_on_cost_centre_emits_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_that_also_diverges_on_cost_centre_emits_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_that_also_diverges_on_cost_centre_emits_no_proposal PASSED [ 57%]`

### Scenario: test_an_intercompany_miscoding_that_also_diverges_on_account_emits_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_miscoding_that_also_diverges_on_account_emits_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_miscoding_that_also_diverges_on_account_emits_no_proposal PASSED [ 57%]`

### Scenario: test_exactly_one_finding_is_emitted_per_posting
- Input: `backend/tests/test_primitive_peer_coding.py::test_exactly_one_finding_is_emitted_per_posting`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_exactly_one_finding_is_emitted_per_posting PASSED [ 57%]`

### Scenario: test_too_few_peers_makes_the_posting_unevaluable_rather_than_a_finding
- Input: `backend/tests/test_primitive_peer_coding.py::test_too_few_peers_makes_the_posting_unevaluable_rather_than_a_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_too_few_peers_makes_the_posting_unevaluable_rather_than_a_finding PASSED [ 57%]`

### Scenario: test_the_peer_support_boundary_is_exact
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_peer_support_boundary_is_exact`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_the_peer_support_boundary_is_exact PASSED [ 57%]`

### Scenario: test_a_divided_peer_set_produces_no_proposal
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_divided_peer_set_produces_no_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_divided_peer_set_produces_no_proposal PASSED [ 57%]`

### Scenario: test_peers_are_context_and_are_not_counted_as_covered_members
- Input: `backend/tests/test_primitive_peer_coding.py::test_peers_are_context_and_are_not_counted_as_covered_members`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_peers_are_context_and_are_not_counted_as_covered_members PASSED [ 57%]`

### Scenario: test_only_earlier_periods_are_peers
- Input: `backend/tests/test_primitive_peer_coding.py::test_only_earlier_periods_are_peers`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_only_earlier_periods_are_peers PASSED [ 57%]`

### Scenario: test_a_declared_posting_with_no_row_is_named_not_silently_skipped
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_declared_posting_with_no_row_is_named_not_silently_skipped`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_a_declared_posting_with_no_row_is_named_not_silently_skipped PASSED [ 57%]`

### Scenario: test_natural_account_peers_are_scoped_to_the_same_caption
- Input: `backend/tests/test_primitive_peer_coding.py::test_natural_account_peers_are_scoped_to_the_same_caption`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_natural_account_peers_are_scoped_to_the_same_caption PASSED [ 57%]`

### Scenario: test_the_summary_declares_which_sub_types_are_in_scope
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_summary_declares_which_sub_types_are_in_scope`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_the_summary_declares_which_sub_types_are_in_scope PASSED [ 58%]`

### Scenario: test_every_number_the_coding_leg_emits_is_hashable_evidence
- Input: `backend/tests/test_primitive_peer_coding.py::test_every_number_the_coding_leg_emits_is_hashable_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_primitive_peer_coding.py::test_every_number_the_coding_leg_emits_is_hashable_evidence PASSED [ 58%]`

### Scenario: test_ges_run_refuses_when_role_is_not_ges
- Input: `backend/tests/test_process_entrypoints.py::test_ges_run_refuses_when_role_is_not_ges`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_ges_run_refuses_when_role_is_not_ges PASSED [ 58%]`

### Scenario: test_api_run_refuses_when_role_is_not_api
- Input: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_when_role_is_not_api`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_when_role_is_not_api PASSED [ 58%]`

### Scenario: test_api_run_refuses_to_start_holding_a_credential
- Input: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_to_start_holding_a_credential`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_to_start_holding_a_credential PASSED [ 58%]`

### Scenario: test_api_health_discloses_no_credential
- Input: `backend/tests/test_process_entrypoints.py::test_api_health_discloses_no_credential`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_api_health_discloses_no_credential PASSED [ 58%]`

### Scenario: test_ges_health_reports_role_but_no_secret
- Input: `backend/tests/test_process_entrypoints.py::test_ges_health_reports_role_but_no_secret`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_ges_health_reports_role_but_no_secret PASSED [ 58%]`

### Scenario: test_ges_loopback_auth_rejects_a_wrong_token
- Input: `backend/tests/test_process_entrypoints.py::test_ges_loopback_auth_rejects_a_wrong_token`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::test_ges_loopback_auth_rejects_a_wrong_token PASSED [ 58%]`

### Scenario: test_it_refuses_to_start_in_production
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_refuses_to_start_in_production`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_refuses_to_start_in_production PASSED [ 58%]`

### Scenario: test_it_names_the_boundary_it_collapses_rather_than_only_the_url
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_names_the_boundary_it_collapses_rather_than_only_the_url`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_names_the_boundary_it_collapses_rather_than_only_the_url PASSED [ 58%]`

### Scenario: test_the_api_entry_point_still_starts_no_broker
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_the_api_entry_point_still_starts_no_broker`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_the_api_entry_point_still_starts_no_broker PASSED [ 58%]`

### Scenario: test_the_registry_holds_exactly_a19_to_a25
- Input: `backend/tests/test_refusal_registry.py::test_the_registry_holds_exactly_a19_to_a25`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_the_registry_holds_exactly_a19_to_a25 PASSED [ 58%]`

### Scenario: test_every_refusal_carries_a_ground_and_maps_to_one_speech_act
- Input: `backend/tests/test_refusal_registry.py::test_every_refusal_carries_a_ground_and_maps_to_one_speech_act`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_every_refusal_carries_a_ground_and_maps_to_one_speech_act PASSED [ 58%]`

### Scenario: test_no_refusal_is_expressed_as_a_bundle_rule
- Input: `backend/tests/test_refusal_registry.py::test_no_refusal_is_expressed_as_a_bundle_rule`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_no_refusal_is_expressed_as_a_bundle_rule PASSED [ 58%]`

### Scenario: test_an_ordinary_finding_trips_nothing
- Input: `backend/tests/test_refusal_registry.py::test_an_ordinary_finding_trips_nothing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_an_ordinary_finding_trips_nothing PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[The
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The variance is small relative to the account balance, so no adjustment is needed.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[This
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This is within the normal range for this account and does not require further work.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[Below
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Below`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Below the threshold we use here, so nothing further to do.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[It
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It is trivial next to the balance; safe to ignore.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[An
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[An`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[An auditor wouldn't look at this one, so it can be passed.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[Honestly
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Honestly`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Honestly this is in the noise \u2014 leave it as is.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[The
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The difference is negligible and does not warrant investigation.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[It's
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It's`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It's basically rounding; no further action.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[Nobody
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Nobody`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Nobody would flag a number this size, so no correction is required.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[The
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The amount is tiny compared to the account, so it can safely be cleared.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[This
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This doesn't move the needle; no follow-up needed.] PASSED [ 59%]`

### Scenario: test_a20_catches_the_speech_act_not_the_vocabulary[Under
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Under`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Under the limit for this entity, so no entry is necessary.] PASSED [ 59%]`

### Scenario: test_a20_needs_both_halves_neither_alone_is_a_refusal
- Input: `backend/tests/test_refusal_registry.py::test_a20_needs_both_halves_neither_alone_is_a_refusal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_needs_both_halves_neither_alone_is_a_refusal PASSED [ 59%]`

### Scenario: test_a20_structural_leg_needs_no_prose_at_all
- Input: `backend/tests/test_refusal_registry.py::test_a20_structural_leg_needs_no_prose_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a20_structural_leg_needs_no_prose_at_all PASSED [ 60%]`

### Scenario: test_every_size_shaped_treatment_ground_is_a20[magnitude]
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[magnitude]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[magnitude] PASSED [ 60%]`

### Scenario: test_every_size_shaped_treatment_ground_is_a20[threshold]
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[threshold]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[threshold] PASSED [ 60%]`

### Scenario: test_every_size_shaped_treatment_ground_is_a20[none]
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[none]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[none] PASSED [ 60%]`

### Scenario: test_every_size_shaped_treatment_ground_is_a20[]
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[] PASSED [ 60%]`

### Scenario: test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it
- Input: `backend/tests/test_refusal_registry.py::test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it PASSED [ 60%]`

### Scenario: test_the_declared_speech_act_is_never_trusted
- Input: `backend/tests/test_refusal_registry.py::test_the_declared_speech_act_is_never_trusted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_the_declared_speech_act_is_never_trusted PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[allowance]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[allowance]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[allowance] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[reserve]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[reserve]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[reserve] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[provision]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[provision]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[provision] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[impairment]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[impairment]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[impairment] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[valuation]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[valuation]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[valuation] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[estimate]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[estimate]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[estimate] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[fair_value]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[fair_value]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[fair_value] PASSED [ 60%]`

### Scenario: test_a19_is_structural_over_subject_matter[useful_life]
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[useful_life]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[useful_life] PASSED [ 60%]`

### Scenario: test_a19_prose_leg[The
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The allowance for doubtful accounts is adequate at the current level.] PASSED [ 61%]`

### Scenario: test_a19_prose_leg[No
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[No`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[No impairment is required for this asset group.] PASSED [ 61%]`

### Scenario: test_a19_prose_leg[The
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The reserve can be released given the improved ageing profile.] PASSED [ 61%]`

### Scenario: test_a19_prose_leg[The
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The useful life remains appropriate.] PASSED [ 61%]`

### Scenario: test_a21_is_unconditional[I
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[I`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[I hereby certify that the accompanying statements are complete.] PASSED [ 61%]`

### Scenario: test_a21_is_unconditional[Signed
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Signed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Signed off on behalf of the controller.] PASSED [ 61%]`

### Scenario: test_a21_is_unconditional[This
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[This satisfies the Section 302 requirement.] PASSED [ 61%]`

### Scenario: test_a21_is_unconditional[Internal
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Internal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Internal control over financial reporting is effective as of period end.] PASSED [ 61%]`

### Scenario: test_a21_is_unconditional[The
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[The statements fairly present in all material respects the position.] PASSED [ 61%]`

### Scenario: test_a21_also_fires_on_a_structured_certification_claim
- Input: `backend/tests/test_refusal_registry.py::test_a21_also_fires_on_a_structured_certification_claim`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a21_also_fires_on_a_structured_certification_claim PASSED [ 61%]`

### Scenario: test_a22_is_structural_over_subject_matter[cut_off]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[cut_off]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[cut_off] PASSED [ 61%]`

### Scenario: test_a22_is_structural_over_subject_matter[revenue_recognition]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[revenue_recognition]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[revenue_recognition] PASSED [ 61%]`

### Scenario: test_a22_is_structural_over_subject_matter[lease_classification]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[lease_classification]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[lease_classification] PASSED [ 61%]`

### Scenario: test_a22_is_structural_over_subject_matter[capitalisation]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[capitalisation]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[capitalisation] PASSED [ 61%]`

### Scenario: test_a22_is_structural_over_subject_matter[consolidation]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[consolidation]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[consolidation] PASSED [ 62%]`

### Scenario: test_a22_is_structural_over_subject_matter[technical_accounting]
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[technical_accounting]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[technical_accounting] PASSED [ 62%]`

### Scenario: test_a22_prose_leg[Under
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Under`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Under ASC 606 this should be recognised over time.] PASSED [ 62%]`

### Scenario: test_a22_prose_leg[The
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The cost should be capitalised rather than expensed.] PASSED [ 62%]`

### Scenario: test_a22_prose_leg[This
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[This belongs in the prior period.] PASSED [ 62%]`

### Scenario: test_a22_prose_leg[The
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The lease is classified as a finance lease.] PASSED [ 62%]`

### Scenario: test_a22_prose_leg[Cut-off
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Cut-off`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Cut-off was correct for this shipment.] PASSED [ 62%]`

### Scenario: test_a23_structural_leg_fires_when_the_ground_is_the_agents_own_prior_output
- Input: `backend/tests/test_refusal_registry.py::test_a23_structural_leg_fires_when_the_ground_is_the_agents_own_prior_output`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_structural_leg_fires_when_the_ground_is_the_agents_own_prior_output PASSED [ 62%]`

### Scenario: test_a23_does_not_fire_when_the_prior_conclusion_is_someone_elses
- Input: `backend/tests/test_refusal_registry.py::test_a23_does_not_fire_when_the_prior_conclusion_is_someone_elses`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_does_not_fire_when_the_prior_conclusion_is_someone_elses PASSED [ 62%]`

### Scenario: test_a23_prose_leg[My
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[My`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[My prior conclusion was correct and the treatment stands.] PASSED [ 62%]`

### Scenario: test_a23_prose_leg[Our
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[Our`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[Our previous assessment remains valid for this period.] PASSED [ 62%]`

### Scenario: test_a23_prose_leg[As
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[As`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[As I correctly concluded last period, this is a timing difference.] PASSED [ 62%]`

### Scenario: test_a23_prose_leg[This
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[This confirms my earlier analysis.] PASSED [ 62%]`

### Scenario: test_a23_permits_re_presenting_prior_reasoning_as_context
- Input: `backend/tests/test_refusal_registry.py::test_a23_permits_re_presenting_prior_reasoning_as_context`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a23_permits_re_presenting_prior_reasoning_as_context PASSED [ 62%]`

### Scenario: test_a24_catches_characterisation[This
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This reviewer is careless with accrual reversals.] PASSED [ 63%]`

### Scenario: test_a24_catches_characterisation[J.
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[J.`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[J. Doe appears to be rubber-stamping proposals.] PASSED [ 63%]`

### Scenario: test_a24_catches_characterisation[The
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[The`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[The performance of this reviewer has declined.] PASSED [ 63%]`

### Scenario: test_a24_catches_characterisation[These
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[These`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[These are the best reviewers on the team.] PASSED [ 63%]`

### Scenario: test_a24_catches_characterisation[This
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This approver should not be trusted with elevated-risk accounts.] PASSED [ 63%]`

### Scenario: test_a24_catches_characterisation[I
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[I`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[I would recommend re-assigning this queue.] PASSED [ 63%]`

### Scenario: test_a24_leaves_the_legitimate_control_metric_alone
- Input: `backend/tests/test_refusal_registry.py::test_a24_leaves_the_legitimate_control_metric_alone`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_leaves_the_legitimate_control_metric_alone PASSED [ 63%]`

### Scenario: test_a24_fires_on_an_unnamed_characterisation_too_but_records_the_weaker_leg
- Input: `backend/tests/test_refusal_registry.py::test_a24_fires_on_an_unnamed_characterisation_too_but_records_the_weaker_leg`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a24_fires_on_an_unnamed_characterisation_too_but_records_the_weaker_leg PASSED [ 63%]`

### Scenario: test_a25_fires_when_the_answer_comes_from_a_different_metric_than_the_request
- Input: `backend/tests/test_refusal_registry.py::test_a25_fires_when_the_answer_comes_from_a_different_metric_than_the_request`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a25_fires_when_the_answer_comes_from_a_different_metric_than_the_request PASSED [ 63%]`

### Scenario: test_a25_does_not_fire_when_the_certified_metric_itself_answered
- Input: `backend/tests/test_refusal_registry.py::test_a25_does_not_fire_when_the_certified_metric_itself_answered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a25_does_not_fire_when_the_certified_metric_itself_answered PASSED [ 63%]`

### Scenario: test_a25_refusal_names_what_is_missing_and_carries_no_substituted_answer
- Input: `backend/tests/test_refusal_registry.py::test_a25_refusal_names_what_is_missing_and_carries_no_substituted_answer`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a25_refusal_names_what_is_missing_and_carries_no_substituted_answer PASSED [ 63%]`

### Scenario: test_a_refusal_is_not_rendered_as_an_error
- Input: `backend/tests/test_refusal_registry.py::test_a_refusal_is_not_rendered_as_an_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_a_refusal_is_not_rendered_as_an_error PASSED [ 63%]`

### Scenario: test_refusal_response_refuses_to_be_built_with_no_refusals
- Input: `backend/tests/test_refusal_registry.py::test_refusal_response_refuses_to_be_built_with_no_refusals`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_refusal_response_refuses_to_be_built_with_no_refusals PASSED [ 63%]`

### Scenario: test_one_emission_can_trip_several_refusals_and_all_are_reported
- Input: `backend/tests/test_refusal_registry.py::test_one_emission_can_trip_several_refusals_and_all_are_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_one_emission_can_trip_several_refusals_and_all_are_reported PASSED [ 63%]`

### Scenario: test_hits_are_deduplicated_per_refusal_and_leg
- Input: `backend/tests/test_refusal_registry.py::test_hits_are_deduplicated_per_refusal_and_leg`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_refusal_registry.py::test_hits_are_deduplicated_per_refusal_and_leg PASSED [ 64%]`

### Scenario: test_the_committed_registry_compiles
- Input: `backend/tests/test_registry_compiler.py::test_the_committed_registry_compiles`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_the_committed_registry_compiles PASSED [ 64%]`

### Scenario: test_registry_hash_is_stable_across_recompiles
- Input: `backend/tests/test_registry_compiler.py::test_registry_hash_is_stable_across_recompiles`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_registry_hash_is_stable_across_recompiles PASSED [ 64%]`

### Scenario: test_every_committed_query_names_an_existing_sql_file
- Input: `backend/tests/test_registry_compiler.py::test_every_committed_query_names_an_existing_sql_file`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_every_committed_query_names_an_existing_sql_file PASSED [ 64%]`

### Scenario: test_query_ids_are_a_closed_sorted_set
- Input: `backend/tests/test_registry_compiler.py::test_query_ids_are_a_closed_sorted_set`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_query_ids_are_a_closed_sorted_set PASSED [ 64%]`

### Scenario: test_lookup_by_id_and_version
- Input: `backend/tests/test_registry_compiler.py::test_lookup_by_id_and_version`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_lookup_by_id_and_version PASSED [ 64%]`

### Scenario: test_personal_data_columns_and_derived_entitlement
- Input: `backend/tests/test_registry_compiler.py::test_personal_data_columns_and_derived_entitlement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_personal_data_columns_and_derived_entitlement PASSED [ 64%]`

### Scenario: test_unclassified_columns_are_reported_by_name
- Input: `backend/tests/test_registry_compiler.py::test_unclassified_columns_are_reported_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_unclassified_columns_are_reported_by_name PASSED [ 64%]`

### Scenario: test_catalogue_for_omits_rather_than_flags
- Input: `backend/tests/test_registry_compiler.py::test_catalogue_for_omits_rather_than_flags`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_catalogue_for_omits_rather_than_flags PASSED [ 64%]`

### Scenario: test_catalogue_for_handles_no_entitlements
- Input: `backend/tests/test_registry_compiler.py::test_catalogue_for_handles_no_entitlements`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_catalogue_for_handles_no_entitlements PASSED [ 64%]`

### Scenario: test_a_sql_typed_parameter_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_a_sql_typed_parameter_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_sql_typed_parameter_fails_the_build PASSED [ 64%]`

### Scenario: test_a_statement_shaped_parameter_name_fails_the_build[sql_text]
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[sql_text]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[sql_text] PASSED [ 64%]`

### Scenario: test_a_statement_shaped_parameter_name_fails_the_build[query_text]
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[query_text]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[query_text] PASSED [ 64%]`

### Scenario: test_a_statement_shaped_parameter_name_fails_the_build[where_clause]
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[where_clause]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[where_clause] PASSED [ 64%]`

### Scenario: test_a_statement_shaped_parameter_name_fails_the_build[raw_predicate]
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[raw_predicate]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[raw_predicate] PASSED [ 64%]`

### Scenario: test_a_statement_shaped_parameter_name_fails_the_build[extra_filter_expression]
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[extra_filter_expression]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[extra_filter_expression] PASSED [ 65%]`

### Scenario: test_a_missing_classification_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_classification_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_missing_classification_fails_the_build PASSED [ 65%]`

### Scenario: test_an_unrecognised_classification_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_an_unrecognised_classification_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_an_unrecognised_classification_fails_the_build PASSED [ 65%]`

### Scenario: test_a_missing_sql_file_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_sql_file_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_missing_sql_file_fails_the_build PASSED [ 65%]`

### Scenario: test_an_enum_without_a_domain_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_an_enum_without_a_domain_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_an_enum_without_a_domain_fails_the_build PASSED [ 65%]`

### Scenario: test_no_columns_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_no_columns_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_no_columns_fails_the_build PASSED [ 65%]`

### Scenario: test_a_duplicate_query_ref_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_a_duplicate_query_ref_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_duplicate_query_ref_fails_the_build PASSED [ 65%]`

### Scenario: test_an_empty_registry_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_an_empty_registry_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_an_empty_registry_fails_the_build PASSED [ 65%]`

### Scenario: test_a_missing_queries_directory_fails_the_build
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_queries_directory_fails_the_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_registry_compiler.py::test_a_missing_queries_directory_fails_the_build PASSED [ 65%]`

### Scenario: test_there_are_exactly_six_types
- Input: `backend/tests/test_resolution_types.py::test_there_are_exactly_six_types`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_there_are_exactly_six_types PASSED [ 65%]`

### Scenario: test_the_set_is_closed
- Input: `backend/tests/test_resolution_types.py::test_the_set_is_closed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_the_set_is_closed PASSED    [ 65%]`

### Scenario: test_every_type_declares_a_non_empty_evidence_schema
- Input: `backend/tests/test_resolution_types.py::test_every_type_declares_a_non_empty_evidence_schema`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_every_type_declares_a_non_empty_evidence_schema PASSED [ 65%]`

### Scenario: test_r1_requires_an_expiry
- Input: `backend/tests/test_resolution_types.py::test_r1_requires_an_expiry`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_r1_requires_an_expiry PASSED [ 65%]`

### Scenario: test_r5_requires_both_a_named_owner_and_a_due_date
- Input: `backend/tests/test_resolution_types.py::test_r5_requires_both_a_named_owner_and_a_due_date`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_r5_requires_both_a_named_owner_and_a_due_date PASSED [ 65%]`

### Scenario: test_r6_requires_the_control_state_change_itself
- Input: `backend/tests/test_resolution_types.py::test_r6_requires_the_control_state_change_itself`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_r6_requires_the_control_state_change_itself PASSED [ 66%]`

### Scenario: test_false_is_a_held_value_not_a_missing_one
- Input: `backend/tests/test_resolution_types.py::test_false_is_a_held_value_not_a_missing_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_false_is_a_held_value_not_a_missing_one PASSED [ 66%]`

### Scenario: test_a_blank_field_is_not_held[]
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[] PASSED [ 66%]`

### Scenario: test_a_blank_field_is_not_held[
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[   ] PASSED [ 66%]`

### Scenario: test_a_blank_field_is_not_held[None]
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[None]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[None] PASSED [ 66%]`

### Scenario: test_a_blank_field_is_not_held[blank3]
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank3]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank3] PASSED [ 66%]`

### Scenario: test_a_blank_field_is_not_held[blank4]
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank4]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank4] PASSED [ 66%]`

### Scenario: test_r3_evidence_does_not_satisfy_from_r2_evidence
- Input: `backend/tests/test_resolution_types.py::test_r3_evidence_does_not_satisfy_from_r2_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_r3_evidence_does_not_satisfy_from_r2_evidence PASSED [ 66%]`

### Scenario: test_require_schema_raises_naming_what_is_missing
- Input: `backend/tests/test_resolution_types.py::test_require_schema_raises_naming_what_is_missing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_require_schema_raises_naming_what_is_missing PASSED [ 66%]`

### Scenario: test_recording_the_safe_outcome_costs_no_more_than_the_posting_outcome
- Input: `backend/tests/test_resolution_types.py::test_recording_the_safe_outcome_costs_no_more_than_the_posting_outcome`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_recording_the_safe_outcome_costs_no_more_than_the_posting_outcome PASSED [ 66%]`

### Scenario: test_the_interaction_count_is_derived_not_declared
- Input: `backend/tests/test_resolution_types.py::test_the_interaction_count_is_derived_not_declared`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_the_interaction_count_is_derived_not_declared PASSED [ 66%]`

### Scenario: test_r3_and_r4_are_the_posting_capable_types_and_the_others_are_not
- Input: `backend/tests/test_resolution_types.py::test_r3_and_r4_are_the_posting_capable_types_and_the_others_are_not`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_r3_and_r4_are_the_posting_capable_types_and_the_others_are_not PASSED [ 66%]`

### Scenario: test_posting_capability_is_a_property_of_the_type_not_a_setting
- Input: `backend/tests/test_resolution_types.py::test_posting_capability_is_a_property_of_the_type_not_a_setting`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_posting_capability_is_a_property_of_the_type_not_a_setting PASSED [ 66%]`

### Scenario: test_no_resolution_type_posts_anything_itself
- Input: `backend/tests/test_resolution_types.py::test_no_resolution_type_posts_anything_itself`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_no_resolution_type_posts_anything_itself PASSED [ 66%]`

### Scenario: test_evidence_supporting_two_types_equally_is_reported_as_a_tie
- Input: `backend/tests/test_resolution_types.py::test_evidence_supporting_two_types_equally_is_reported_as_a_tie`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_evidence_supporting_two_types_equally_is_reported_as_a_tie PASSED [ 67%]`

### Scenario: test_a_tie_is_computed_over_the_schema_not_volunteered
- Input: `backend/tests/test_resolution_types.py::test_a_tie_is_computed_over_the_schema_not_volunteered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_a_tie_is_computed_over_the_schema_not_volunteered PASSED [ 67%]`

### Scenario: test_evidence_supporting_nothing_is_an_empty_list_not_a_guess
- Input: `backend/tests/test_resolution_types.py::test_evidence_supporting_nothing_is_an_empty_list_not_a_guess`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_resolution_types.py::test_evidence_supporting_nothing_is_an_empty_list_not_a_guess PASSED [ 67%]`

### Scenario: test_four_consecutive_sub_threshold_movements_escalate
- Input: `backend/tests/test_surveillance_primitives.py::test_four_consecutive_sub_threshold_movements_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_four_consecutive_sub_threshold_movements_escalate PASSED [ 67%]`

### Scenario: test_three_consecutive_movements_do_not_escalate_and_the_record_says_how_many_more
- Input: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_movements_do_not_escalate_and_the_record_says_how_many_more`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_movements_do_not_escalate_and_the_record_says_how_many_more PASSED [ 67%]`

### Scenario: test_the_escalation_period_is_where_the_run_reached_the_count_not_the_latest
- Input: `backend/tests/test_surveillance_primitives.py::test_the_escalation_period_is_where_the_run_reached_the_count_not_the_latest`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_escalation_period_is_where_the_run_reached_the_count_not_the_latest PASSED [ 67%]`

### Scenario: test_the_aggregate_covers_the_whole_run_not_only_up_to_the_escalation
- Input: `backend/tests/test_surveillance_primitives.py::test_the_aggregate_covers_the_whole_run_not_only_up_to_the_escalation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_aggregate_covers_the_whole_run_not_only_up_to_the_escalation PASSED [ 67%]`

### Scenario: test_the_period_delta_is_present_and_is_not_the_headline
- Input: `backend/tests/test_surveillance_primitives.py::test_the_period_delta_is_present_and_is_not_the_headline`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_period_delta_is_present_and_is_not_the_headline PASSED [ 67%]`

### Scenario: test_alternating_directions_do_not_accumulate
- Input: `backend/tests/test_surveillance_primitives.py::test_alternating_directions_do_not_accumulate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_alternating_directions_do_not_accumulate PASSED [ 67%]`

### Scenario: test_a_direction_change_breaks_the_run_at_exactly_that_period
- Input: `backend/tests/test_surveillance_primitives.py::test_a_direction_change_breaks_the_run_at_exactly_that_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_direction_change_breaks_the_run_at_exactly_that_period PASSED [ 67%]`

### Scenario: test_a_movement_above_the_threshold_breaks_the_run
- Input: `backend/tests/test_surveillance_primitives.py::test_a_movement_above_the_threshold_breaks_the_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_movement_above_the_threshold_breaks_the_run PASSED [ 67%]`

### Scenario: test_a_movement_exactly_at_the_threshold_is_not_below_it
- Input: `backend/tests/test_surveillance_primitives.py::test_a_movement_exactly_at_the_threshold_is_not_below_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_movement_exactly_at_the_threshold_is_not_below_it PASSED [ 67%]`

### Scenario: test_a_period_gap_breaks_the_run_because_the_periods_are_not_consecutive
- Input: `backend/tests/test_surveillance_primitives.py::test_a_period_gap_breaks_the_run_because_the_periods_are_not_consecutive`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_period_gap_breaks_the_run_because_the_periods_are_not_consecutive PASSED [ 67%]`

### Scenario: test_a_zero_movement_breaks_the_run_rather_than_extending_it
- Input: `backend/tests/test_surveillance_primitives.py::test_a_zero_movement_breaks_the_run_rather_than_extending_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_zero_movement_breaks_the_run_rather_than_extending_it PASSED [ 67%]`

### Scenario: test_an_account_with_one_period_is_not_evaluable_and_names_what_it_has
- Input: `backend/tests/test_surveillance_primitives.py::test_an_account_with_one_period_is_not_evaluable_and_names_what_it_has`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_an_account_with_one_period_is_not_evaluable_and_names_what_it_has PASSED [ 67%]`

### Scenario: test_a_declared_account_with_no_movements_at_all_is_not_evaluable
- Input: `backend/tests/test_surveillance_primitives.py::test_a_declared_account_with_no_movements_at_all_is_not_evaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_declared_account_with_no_movements_at_all_is_not_evaluable PASSED [ 68%]`

### Scenario: test_a_credit_direction_accumulation_escalates_and_says_so
- Input: `backend/tests/test_surveillance_primitives.py::test_a_credit_direction_accumulation_escalates_and_says_so`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_credit_direction_accumulation_escalates_and_says_so PASSED [ 68%]`

### Scenario: test_the_consecutive_count_is_configurable_and_the_boundary_is_exact
- Input: `backend/tests/test_surveillance_primitives.py::test_the_consecutive_count_is_configurable_and_the_boundary_is_exact`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_consecutive_count_is_configurable_and_the_boundary_is_exact PASSED [ 68%]`

### Scenario: test_the_amounts_are_decimals_end_to_end
- Input: `backend/tests/test_surveillance_primitives.py::test_the_amounts_are_decimals_end_to_end`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_amounts_are_decimals_end_to_end PASSED [ 68%]`

### Scenario: test_three_consecutive_verbatim_explanations_escalate
- Input: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_verbatim_explanations_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_verbatim_explanations_escalate PASSED [ 68%]`

### Scenario: test_two_consecutive_verbatim_explanations_do_not
- Input: `backend/tests/test_surveillance_primitives.py::test_two_consecutive_verbatim_explanations_do_not`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_two_consecutive_verbatim_explanations_do_not PASSED [ 68%]`

### Scenario: test_the_escalation_quotes_the_recurring_assertion
- Input: `backend/tests/test_surveillance_primitives.py::test_the_escalation_quotes_the_recurring_assertion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_escalation_quotes_the_recurring_assertion PASSED [ 68%]`

### Scenario: test_genuinely_different_explanations_do_not_escalate
- Input: `backend/tests/test_surveillance_primitives.py::test_genuinely_different_explanations_do_not_escalate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_genuinely_different_explanations_do_not_escalate PASSED [ 68%]`

### Scenario: test_a_reworded_restatement_still_matches_and_a_reordering_certainly_does
- Input: `backend/tests/test_surveillance_primitives.py::test_a_reworded_restatement_still_matches_and_a_reordering_certainly_does`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_reworded_restatement_still_matches_and_a_reordering_certainly_does PASSED [ 68%]`

### Scenario: test_two_empty_explanations_score_zero_rather_than_a_perfect_match
- Input: `backend/tests/test_surveillance_primitives.py::test_two_empty_explanations_score_zero_rather_than_a_perfect_match`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_two_empty_explanations_score_zero_rather_than_a_perfect_match PASSED [ 68%]`

### Scenario: test_every_number_the_narrative_leg_emits_is_hashable_evidence
- Input: `backend/tests/test_surveillance_primitives.py::test_every_number_the_narrative_leg_emits_is_hashable_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_every_number_the_narrative_leg_emits_is_hashable_evidence PASSED [ 68%]`

### Scenario: test_a_period_with_no_recorded_explanation_makes_the_member_unevaluable
- Input: `backend/tests/test_surveillance_primitives.py::test_a_period_with_no_recorded_explanation_makes_the_member_unevaluable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_period_with_no_recorded_explanation_makes_the_member_unevaluable PASSED [ 68%]`

### Scenario: test_a_missing_period_is_reported_rather_than_bridged
- Input: `backend/tests/test_surveillance_primitives.py::test_a_missing_period_is_reported_rather_than_bridged`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_a_missing_period_is_reported_rather_than_bridged PASSED [ 68%]`

### Scenario: test_an_account_with_no_explanation_at_all_is_named_not_silently_skipped
- Input: `backend/tests/test_surveillance_primitives.py::test_an_account_with_no_explanation_at_all_is_named_not_silently_skipped`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_an_account_with_no_explanation_at_all_is_named_not_silently_skipped PASSED [ 68%]`

### Scenario: test_one_period_of_explanation_cannot_recur
- Input: `backend/tests/test_surveillance_primitives.py::test_one_period_of_explanation_cannot_recur`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_one_period_of_explanation_cannot_recur PASSED [ 69%]`

### Scenario: test_the_similarity_bound_is_inclusive_at_the_bound
- Input: `backend/tests/test_surveillance_primitives.py::test_the_similarity_bound_is_inclusive_at_the_bound`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_similarity_bound_is_inclusive_at_the_bound PASSED [ 69%]`

### Scenario: test_the_computation_is_deterministic_and_declares_that_it_used_no_model
- Input: `backend/tests/test_surveillance_primitives.py::test_the_computation_is_deterministic_and_declares_that_it_used_no_model`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_computation_is_deterministic_and_declares_that_it_used_no_model PASSED [ 69%]`

### Scenario: test_the_narrative_leg_holds_no_model_client_and_no_network_call
- Input: `backend/tests/test_surveillance_primitives.py::test_the_narrative_leg_holds_no_model_client_and_no_network_call`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_narrative_leg_holds_no_model_client_and_no_network_call PASSED [ 69%]`

### Scenario: test_two_separate_recurring_runs_on_one_account_are_both_reported
- Input: `backend/tests/test_surveillance_primitives.py::test_two_separate_recurring_runs_on_one_account_are_both_reported`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_two_separate_recurring_runs_on_one_account_are_both_reported PASSED [ 69%]`

### Scenario: test_the_run_length_boundary[2-0]
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[2-0]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[2-0] PASSED [ 69%]`

### Scenario: test_the_run_length_boundary[3-1]
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[3-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[3-1] PASSED [ 69%]`

### Scenario: test_the_run_length_boundary[4-1]
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[4-1]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[4-1] PASSED [ 69%]`

### Scenario: test_the_entry_point_lands_on_ask
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_the_entry_point_lands_on_ask`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_the_entry_point_lands_on_ask PASSED [ 69%]`

### Scenario: test_ask_is_reachable_by_following_links_from_the_entry_point
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_ask_is_reachable_by_following_links_from_the_entry_point`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_ask_is_reachable_by_following_links_from_the_entry_point PASSED [ 69%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[nl-input]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[nl-input]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[nl-input] PASSED [ 69%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[resolved-query]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolved-query]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolved-query] PASSED [ 69%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[declared-population-panel]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[declared-population-panel]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[declared-population-panel] PASSED [ 69%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[coverage-meter]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-meter]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-meter] PASSED [ 69%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[ambiguity-fork]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[ambiguity-fork]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[ambiguity-fork] PASSED [ 70%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner] PASSED [ 70%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[run-submit]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[run-submit]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[run-submit] PASSED [ 70%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[provenance]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[provenance]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[provenance] PASSED [ 70%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[pilot-strip]
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[pilot-strip]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[pilot-strip] PASSED [ 70%]`

### Scenario: test_AC_F39_09_all_four_required_elements_are_on_the_screen
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_09_all_four_required_elements_are_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_09_all_four_required_elements_are_on_the_screen PASSED [ 70%]`

### Scenario: test_AC_F39_01_the_resolution_carries_its_version_and_bound_parameters
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_01_the_resolution_carries_its_version_and_bound_parameters`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_01_the_resolution_carries_its_version_and_bound_parameters PASSED [ 70%]`

### Scenario: test_AC_F39_02_no_control_on_this_screen_can_carry_sql
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_02_no_control_on_this_screen_can_carry_sql`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_02_no_control_on_this_screen_can_carry_sql PASSED [ 70%]`

### Scenario: test_AC_F39_07_the_ambiguity_fork_names_both_candidates_and_preselects_neither
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_07_the_ambiguity_fork_names_both_candidates_and_preselects_neither`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_07_the_ambiguity_fork_names_both_candidates_and_preselects_neither PASSED [ 70%]`

### Scenario: test_AC_F38_14_the_coverage_meter_states_a_percentage_against_the_declaration
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_14_the_coverage_meter_states_a_percentage_against_the_declaration`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_14_the_coverage_meter_states_a_percentage_against_the_declaration PASSED [ 70%]`

### Scenario: test_AC_F38_15_the_partial_banner_names_the_coverage_and_the_bound
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_15_the_partial_banner_names_the_coverage_and_the_bound`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_15_the_partial_banner_names_the_coverage_and_the_bound PASSED [ 70%]`

### Scenario: test_unselected_segments_are_named_individually_not_merely_counted
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_unselected_segments_are_named_individually_not_merely_counted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_unselected_segments_are_named_individually_not_merely_counted PASSED [ 70%]`

### Scenario: test_covered_segments_are_named_too_so_the_declaration_is_readable_whole
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_covered_segments_are_named_too_so_the_declaration_is_readable_whole`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_covered_segments_are_named_too_so_the_declaration_is_readable_whole PASSED [ 70%]`

### Scenario: test_there_is_no_multiselect_dropdown_anywhere_on_the_screen
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_there_is_no_multiselect_dropdown_anywhere_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_there_is_no_multiselect_dropdown_anywhere_on_the_screen PASSED [ 70%]`

### Scenario: test_the_gaps_are_drawn_as_segments_rather_than_as_absent_fill
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_gaps_are_drawn_as_segments_rather_than_as_absent_fill`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_gaps_are_drawn_as_segments_rather_than_as_absent_fill PASSED [ 71%]`

### Scenario: test_each_gap_segment_carries_a_non_colour_carrier
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_each_gap_segment_carries_a_non_colour_carrier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_each_gap_segment_carries_a_non_colour_carrier PASSED [ 71%]`

### Scenario: test_the_strip_has_a_text_alternative_for_a_screen_reader
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_strip_has_a_text_alternative_for_a_screen_reader`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_strip_has_a_text_alternative_for_a_screen_reader PASSED [ 71%]`

### Scenario: test_there_is_no_progress_element_and_no_progressbar_role
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_there_is_no_progress_element_and_no_progressbar_role`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_there_is_no_progress_element_and_no_progressbar_role PASSED [ 71%]`

### Scenario: test_the_submit_label_states_the_coverage_rather_than_reading_run
- Input: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_the_submit_label_states_the_coverage_rather_than_reading_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_the_submit_label_states_the_coverage_rather_than_reading_run PASSED [ 71%]`

### Scenario: test_there_is_no_control_that_dismisses_the_partial_state
- Input: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_there_is_no_control_that_dismisses_the_partial_state`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_there_is_no_control_that_dismisses_the_partial_state PASSED [ 71%]`

### Scenario: test_there_is_no_bulk_action_control_on_this_screen
- Input: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_on_this_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_on_this_screen PASSED [ 71%]`

### Scenario: test_there_is_no_confidence_or_explanation_quality_surface
- Input: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_confidence_or_explanation_quality_surface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_confidence_or_explanation_quality_surface PASSED [ 71%]`

### Scenario: test_no_ui_module_imports_anything_from_ges
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_imports_anything_from_ges`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_imports_anything_from_ges PASSED [ 71%]`

### Scenario: test_no_ui_module_compares_an_approver_against_an_author_or_an_invoker
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_compares_an_approver_against_an_author_or_an_invoker`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_compares_an_approver_against_an_author_or_an_invoker PASSED [ 71%]`

### Scenario: test_the_screens_render_eligibility_from_a_carried_payload
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_screens_render_eligibility_from_a_carried_payload`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_screens_render_eligibility_from_a_carried_payload PASSED [ 71%]`

### Scenario: test_the_boundary_note_is_rendered_on_the_screens_that_show_broker_facts
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_boundary_note_is_rendered_on_the_screens_that_show_broker_facts`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_boundary_note_is_rendered_on_the_screens_that_show_broker_facts PASSED [ 71%]`

### Scenario: test_the_component_library_defines_no_bulk_affordance
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_the_component_library_defines_no_bulk_affordance`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_the_component_library_defines_no_bulk_affordance PASSED [ 71%]`

### Scenario: test_no_screen_in_the_build_renders_a_checkbox_or_a_select
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_in_the_build_renders_a_checkbox_or_a_select`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_in_the_build_renders_a_checkbox_or_a_select PASSED [ 71%]`

### Scenario: test_no_screen_offers_a_keyboard_shortcut_for_a_bulk_action
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_offers_a_keyboard_shortcut_for_a_bulk_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_offers_a_keyboard_shortcut_for_a_bulk_action PASSED [ 71%]`

### Scenario: test_at_most_one_approve_control_exists_across_the_entire_surface
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_at_most_one_approve_control_exists_across_the_entire_surface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_at_most_one_approve_control_exists_across_the_entire_surface PASSED [ 72%]`

### Scenario: test_no_form_control_on_any_screen_is_named_for_sql
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_form_control_on_any_screen_is_named_for_sql`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_form_control_on_any_screen_is_named_for_sql PASSED [ 72%]`

### Scenario: test_no_ui_module_builds_or_holds_a_sql_string
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_ui_module_builds_or_holds_a_sql_string`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_ui_module_builds_or_holds_a_sql_string PASSED [ 72%]`

### Scenario: test_the_ask_screen_names_the_certified_query_it_resolved_to
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_the_ask_screen_names_the_certified_query_it_resolved_to`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_the_ask_screen_names_the_certified_query_it_resolved_to PASSED [ 72%]`

### Scenario: test_every_route_the_app_serves_is_reachable_from_the_entry_point
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_route_the_app_serves_is_reachable_from_the_entry_point`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_route_the_app_serves_is_reachable_from_the_entry_point PASSED [ 72%]`

### Scenario: test_every_parameterised_screen_is_reached_by_following_a_real_link
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_parameterised_screen_is_reached_by_following_a_real_link`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_parameterised_screen_is_reached_by_following_a_real_link PASSED [ 72%]`

### Scenario: test_every_component_the_library_defines_appears_on_some_reachable_screen
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_component_the_library_defines_appears_on_some_reachable_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_component_the_library_defines_appears_on_some_reachable_screen PASSED [ 72%]`

### Scenario: test_the_write_path_components_appear_only_after_the_control_is_used
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_write_path_components_appear_only_after_the_control_is_used`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_write_path_components_appear_only_after_the_control_is_used PASSED [ 72%]`

### Scenario: test_the_entry_point_reaches_every_navigation_destination
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_entry_point_reaches_every_navigation_destination`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_entry_point_reaches_every_navigation_destination PASSED [ 72%]`

### Scenario: test_not_one_screen_in_the_build_carries_a_script_or_an_event_handler
- Input: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_not_one_screen_in_the_build_carries_a_script_or_an_event_handler`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_not_one_screen_in_the_build_carries_a_script_or_an_event_handler PASSED [ 72%]`

### Scenario: test_no_screen_carries_a_meta_refresh_or_an_auto_updating_region
- Input: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_no_screen_carries_a_meta_refresh_or_an_auto_updating_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_no_screen_carries_a_meta_refresh_or_an_auto_updating_region PASSED [ 72%]`

### Scenario: test_no_rendered_page_contains_a_colour_in_the_green_band
- Input: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_rendered_page_contains_a_colour_in_the_green_band`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_rendered_page_contains_a_colour_in_the_green_band PASSED [ 72%]`

### Scenario: test_no_named_css_green_appears_in_any_response
- Input: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_named_css_green_appears_in_any_response`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_named_css_green_appears_in_any_response PASSED [ 72%]`

### Scenario: test_the_document_carries_its_own_stylesheet
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_document_carries_its_own_stylesheet`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_document_carries_its_own_stylesheet PASSED [ 72%]`

### Scenario: test_there_is_no_external_stylesheet_or_font_or_image_fetch
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_external_stylesheet_or_font_or_image_fetch`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_external_stylesheet_or_font_or_image_fetch PASSED [ 73%]`

### Scenario: test_there_is_no_script_anywhere
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_script_anywhere`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_script_anywhere PASSED [ 73%]`

### Scenario: test_the_doctype_is_first
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_doctype_is_first`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_doctype_is_first PASSED [ 73%]`

### Scenario: test_every_nav_entry_points_at_a_route_this_build_serves
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_every_nav_entry_points_at_a_route_this_build_serves`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestNavigation::test_every_nav_entry_points_at_a_route_this_build_serves PASSED [ 73%]`

### Scenario: test_the_active_item_is_marked_for_assistive_technology_too
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_the_active_item_is_marked_for_assistive_technology_too`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestNavigation::test_the_active_item_is_marked_for_assistive_technology_too PASSED [ 73%]`

### Scenario: test_badges_render_the_number_routed_not_the_number_detected
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_badges_render_the_number_routed_not_the_number_detected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestNavigation::test_badges_render_the_number_routed_not_the_number_detected PASSED [ 73%]`

### Scenario: test_a_missing_badge_renders_no_count_rather_than_zero
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_a_missing_badge_renders_no_count_rather_than_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestNavigation::test_a_missing_badge_renders_no_count_rather_than_zero PASSED [ 73%]`

### Scenario: test_every_chromed_page_carries_entity_period_close_day_and_as_of
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_every_chromed_page_carries_entity_period_close_day_and_as_of`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_every_chromed_page_carries_entity_period_close_day_and_as_of PASSED [ 73%]`

### Scenario: test_the_pilot_strip_states_the_data_is_synthetic_in_words
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_pilot_strip_states_the_data_is_synthetic_in_words`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_pilot_strip_states_the_data_is_synthetic_in_words PASSED [ 73%]`

### Scenario: test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet PASSED [ 73%]`

### Scenario: test_the_riskiest_size_strictly_exceeds_the_ceiling_for_everything_else
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_the_riskiest_size_strictly_exceeds_the_ceiling_for_everything_else`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_the_riskiest_size_strictly_exceeds_the_ceiling_for_everything_else PASSED [ 73%]`

### Scenario: test_no_declared_pixel_font_size_in_the_stylesheet_reaches_the_riskiest_size
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_no_declared_pixel_font_size_in_the_stylesheet_reaches_the_riskiest_size`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_no_declared_pixel_font_size_in_the_stylesheet_reaches_the_riskiest_size PASSED [ 73%]`

### Scenario: test_exactly_one_rule_declares_the_riskiest_size
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_exactly_one_rule_declares_the_riskiest_size`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_exactly_one_rule_declares_the_riskiest_size PASSED [ 73%]`

### Scenario: test_importing_chrome_has_already_asserted_no_green
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_importing_chrome_has_already_asserted_no_green`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_importing_chrome_has_already_asserted_no_green PASSED [ 73%]`

### Scenario: test_the_stylesheet_carries_both_themes
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_the_stylesheet_carries_both_themes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_the_stylesheet_carries_both_themes PASSED [ 74%]`

### Scenario: test_no_literal_hex_colour_appears_outside_the_token_block
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_no_literal_hex_colour_appears_outside_the_token_block`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_no_literal_hex_colour_appears_outside_the_token_block PASSED [ 74%]`

### Scenario: test_the_rendered_page_contains_exactly_the_tree
- Input: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_the_rendered_page_contains_exactly_the_tree`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_the_rendered_page_contains_exactly_the_tree PASSED [ 74%]`

### Scenario: test_a_component_absent_from_the_tree_is_absent_from_the_markup
- Input: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_a_component_absent_from_the_tree_is_absent_from_the_markup`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_a_component_absent_from_the_tree_is_absent_from_the_markup PASSED [ 74%]`

### Scenario: test_a_dossier_is_reachable_from_the_entry_point_by_following_links
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_a_dossier_is_reachable_from_the_entry_point_by_following_links`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_a_dossier_is_reachable_from_the_entry_point_by_following_links PASSED [ 74%]`

### Scenario: test_the_review_screen_links_to_this_dossier
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_the_review_screen_links_to_this_dossier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_the_review_screen_links_to_this_dossier PASSED [ 74%]`

### Scenario: test_every_item_in_the_pilot_close_has_a_reachable_dossier
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_every_item_in_the_pilot_close_has_a_reachable_dossier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_every_item_in_the_pilot_close_has_a_reachable_dossier PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[dossier-header]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-header]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-header] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[risk-band]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[evidence-set]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[in-force-panel]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[authorship-closure]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded] PASSED [ 74%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[coverage-strip]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip] PASSED [ 75%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[agent-narrative]
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative] PASSED [ 75%]`

### Scenario: test_the_stylesheet_is_inlined
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_stylesheet_is_inlined`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_stylesheet_is_inlined PASSED [ 75%]`

### Scenario: test_there_is_no_external_reference_of_any_kind
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_there_is_no_external_reference_of_any_kind`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_there_is_no_external_reference_of_any_kind PASSED [ 75%]`

### Scenario: test_it_carries_no_application_navigation
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_it_carries_no_application_navigation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_it_carries_no_application_navigation PASSED [ 75%]`

### Scenario: test_every_remaining_link_is_absent_so_the_file_opens_standalone
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_every_remaining_link_is_absent_so_the_file_opens_standalone`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_every_remaining_link_is_absent_so_the_file_opens_standalone PASSED [ 75%]`

### Scenario: test_the_document_is_a_complete_html_document
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_document_is_a_complete_html_document`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_document_is_a_complete_html_document PASSED [ 75%]`

### Scenario: test_the_figures_the_threshold_and_the_bundle_version_are_all_in_it
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_figures_the_threshold_and_the_bundle_version_are_all_in_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_figures_the_threshold_and_the_bundle_version_are_all_in_it PASSED [ 75%]`

### Scenario: test_the_evidence_table_is_reproduced_row_for_row
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_evidence_table_is_reproduced_row_for_row`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_evidence_table_is_reproduced_row_for_row PASSED [ 75%]`

### Scenario: test_the_runs_coverage_statement_travels_with_the_dossier
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_runs_coverage_statement_travels_with_the_dossier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_runs_coverage_statement_travels_with_the_dossier PASSED [ 75%]`

### Scenario: test_the_retention_expiry_is_stated
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_retention_expiry_is_stated`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_retention_expiry_is_stated PASSED [ 75%]`

### Scenario: test_the_dossier_names_its_run_and_its_item
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_dossier_names_its_run_and_its_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_dossier_names_its_run_and_its_item PASSED [ 75%]`

### Scenario: test_no_title_attribute_carries_data
- Input: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_no_title_attribute_carries_data`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_no_title_attribute_carries_data PASSED [ 75%]`

### Scenario: test_the_narrative_is_present_in_the_document_even_though_it_is_collapsed
- Input: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_the_narrative_is_present_in_the_document_even_though_it_is_collapsed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_the_narrative_is_present_in_the_document_even_though_it_is_collapsed PASSED [ 75%]`

### Scenario: test_an_auto_disposed_items_dossier_carries_the_rule_and_the_bundle_hash
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_an_auto_disposed_items_dossier_carries_the_rule_and_the_bundle_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_an_auto_disposed_items_dossier_carries_the_rule_and_the_bundle_hash PASSED [ 75%]`

### Scenario: test_it_states_what_the_rule_did_in_words
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_it_states_what_the_rule_did_in_words`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_it_states_what_the_rule_did_in_words PASSED [ 76%]`

### Scenario: test_a_normally_routed_item_carries_no_auto_disposal_record
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_a_normally_routed_item_carries_no_auto_disposal_record`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_a_normally_routed_item_carries_no_auto_disposal_record PASSED [ 76%]`

### Scenario: test_the_abstained_items_dossier_records_the_abstention_as_such
- Input: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_the_abstained_items_dossier_records_the_abstention_as_such`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_the_abstained_items_dossier_records_the_abstention_as_such PASSED [ 76%]`

### Scenario: test_it_does_not_read_as_a_finding_that_nothing_was_wrong
- Input: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_it_does_not_read_as_a_finding_that_nothing_was_wrong`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_it_does_not_read_as_a_finding_that_nothing_was_wrong PASSED [ 76%]`

### Scenario: test_the_coverage_gaps_carry_a_hatch_as_well_as_a_colour
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_coverage_gaps_carry_a_hatch_as_well_as_a_colour`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_coverage_gaps_carry_a_hatch_as_well_as_a_colour PASSED [ 76%]`

### Scenario: test_the_risk_band_states_its_tier_in_words_not_only_in_colour
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_risk_band_states_its_tier_in_words_not_only_in_colour`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_risk_band_states_its_tier_in_words_not_only_in_colour PASSED [ 76%]`

### Scenario: test_no_state_in_the_document_is_expressed_only_as_an_inline_colour
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_no_state_in_the_document_is_expressed_only_as_an_inline_colour`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_no_state_in_the_document_is_expressed_only_as_an_inline_colour PASSED [ 76%]`

### Scenario: test_exceptions_is_reachable_from_the_entry_point_by_following_links
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_exceptions_is_reachable_from_the_entry_point_by_following_links`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_exceptions_is_reachable_from_the_entry_point_by_following_links PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[volume-masthead]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[volume-masthead]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[volume-masthead] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[detections-count]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[detections-count]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[detections-count] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[routed-count]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[routed-count]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[routed-count] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[coverage-strip]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip] PASSED [ 76%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[exception-queue]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-queue]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-queue] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[exception-row]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-row]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-row] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[kind-pill]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[kind-pill]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[kind-pill] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[risk-pill]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-pill]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-pill] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[auto-disposed-marker]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[auto-disposed-marker]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[auto-disposed-marker] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[abstention-region]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-region]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-region] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[abstention-block]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-block]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-block] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[boundary-check-table]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[boundary-check-table]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[boundary-check-table] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[check-not-run]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[check-not-run]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[check-not-run] PASSED [ 77%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[recall-bias-label]
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[recall-bias-label]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[recall-bias-label] PASSED [ 77%]`

### Scenario: test_AC_F41_09_both_N_and_M_are_visible_without_leaving_the_screen
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_AC_F41_09_both_N_and_M_are_visible_without_leaving_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_AC_F41_09_both_N_and_M_are_visible_without_leaving_the_screen PASSED [ 77%]`

### Scenario: test_the_ratio_is_the_masthead_and_precedes_the_queue
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_ratio_is_the_masthead_and_precedes_the_queue`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_ratio_is_the_masthead_and_precedes_the_queue PASSED [ 77%]`

### Scenario: test_the_disposition_of_everything_not_routed_is_stated
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_disposition_of_everything_not_routed_is_stated`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_disposition_of_everything_not_routed_is_stated PASSED [ 77%]`

### Scenario: test_an_omission_finding_is_labelled_as_one
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_an_omission_finding_is_labelled_as_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_an_omission_finding_is_labelled_as_one PASSED [ 77%]`

### Scenario: test_a_present_anomaly_finding_is_labelled_as_one
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_a_present_anomaly_finding_is_labelled_as_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_a_present_anomaly_finding_is_labelled_as_one PASSED [ 78%]`

### Scenario: test_the_two_labels_differ_in_words_and_not_only_in_style
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_two_labels_differ_in_words_and_not_only_in_style`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_two_labels_differ_in_words_and_not_only_in_style PASSED [ 78%]`

### Scenario: test_the_omission_finding_shows_the_expected_entry_history_that_grounds_it
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_omission_finding_shows_the_expected_entry_history_that_grounds_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_omission_finding_shows_the_expected_entry_history_that_grounds_it PASSED [ 78%]`

### Scenario: test_rows_are_ordered_by_risk_descending
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_rows_are_ordered_by_risk_descending`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_rows_are_ordered_by_risk_descending PASSED [ 78%]`

### Scenario: test_the_band_is_a_structural_left_bar_not_a_legend_dependent_dot
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_the_band_is_a_structural_left_bar_not_a_legend_dependent_dot`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_the_band_is_a_structural_left_bar_not_a_legend_dependent_dot PASSED [ 78%]`

### Scenario: test_there_are_never_more_than_three_risk_steps_on_screen
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_there_are_never_more_than_three_risk_steps_on_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_there_are_never_more_than_three_risk_steps_on_screen PASSED [ 78%]`

### Scenario: test_no_numeric_risk_score_is_rendered
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_no_numeric_risk_score_is_rendered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_no_numeric_risk_score_is_rendered PASSED [ 78%]`

### Scenario: test_all_five_boundary_checks_render_an_individual_result
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_all_five_boundary_checks_render_an_individual_result`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_all_five_boundary_checks_render_an_individual_result PASSED [ 78%]`

### Scenario: test_a_check_that_could_not_run_says_not_run_and_names_the_missing_dataset
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_a_check_that_could_not_run_says_not_run_and_names_the_missing_dataset`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_a_check_that_could_not_run_says_not_run_and_names_the_missing_dataset PASSED [ 78%]`

### Scenario: test_not_run_is_rendered_in_risk_colour_rather_than_neutral
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_not_run_is_rendered_in_risk_colour_rather_than_neutral`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_not_run_is_rendered_in_risk_colour_rather_than_neutral PASSED [ 78%]`

### Scenario: test_the_abstention_is_rendered_outside_the_findings_queue
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstention_is_rendered_outside_the_findings_queue`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstention_is_rendered_outside_the_findings_queue PASSED [ 78%]`

### Scenario: test_the_abstained_item_has_no_row_in_the_findings_queue_at_all
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_has_no_row_in_the_findings_queue_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_has_no_row_in_the_findings_queue_at_all PASSED [ 78%]`

### Scenario: test_the_abstained_item_is_still_routed_to_a_human
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_is_still_routed_to_a_human`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_is_still_routed_to_a_human PASSED [ 78%]`

### Scenario: test_its_rag_state_is_unknown_and_it_declares_it_is_not_a_finding
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_its_rag_state_is_unknown_and_it_declares_it_is_not_a_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_its_rag_state_is_unknown_and_it_declares_it_is_not_a_finding PASSED [ 78%]`

### Scenario: test_it_names_its_evidence_gap_and_exactly_one_resolving_action
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_names_its_evidence_gap_and_exactly_one_resolving_action`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_names_its_evidence_gap_and_exactly_one_resolving_action PASSED [ 78%]`

### Scenario: test_it_is_structurally_distinct_from_a_finding_row_not_only_worded_differently
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_is_structurally_distinct_from_a_finding_row_not_only_worded_differently`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_is_structurally_distinct_from_a_finding_row_not_only_worded_differently PASSED [ 79%]`

### Scenario: test_the_region_explains_why_it_is_listed_apart
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_region_explains_why_it_is_listed_apart`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_region_explains_why_it_is_listed_apart PASSED [ 79%]`

### Scenario: test_the_auto_disposed_finding_is_visible_in_the_list
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_auto_disposed_finding_is_visible_in_the_list`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_auto_disposed_finding_is_visible_in_the_list PASSED [ 79%]`

### Scenario: test_it_names_the_rule_that_disposed_it_and_the_bundle_hash
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_it_names_the_rule_that_disposed_it_and_the_bundle_hash`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_it_names_the_rule_that_disposed_it_and_the_bundle_hash PASSED [ 79%]`

### Scenario: test_its_dossier_is_reachable_from_that_list
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_its_dossier_is_reachable_from_that_list`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_its_dossier_is_reachable_from_that_list PASSED [ 79%]`

### Scenario: test_the_rule_in_the_row_is_the_rule_that_actually_disposed_the_finding
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_rule_in_the_row_is_the_rule_that_actually_disposed_the_finding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_rule_in_the_row_is_the_rule_that_actually_disposed_the_finding PASSED [ 79%]`

### Scenario: test_an_auto_disposed_item_is_not_counted_as_routed_to_a_human
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_an_auto_disposed_item_is_not_counted_as_routed_to_a_human`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_an_auto_disposed_item_is_not_counted_as_routed_to_a_human PASSED [ 79%]`

### Scenario: test_the_seventy_and_hundred_per_cent_conclusions_are_textually_different
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_seventy_and_hundred_per_cent_conclusions_are_textually_different`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_seventy_and_hundred_per_cent_conclusions_are_textually_different PASSED [ 79%]`

### Scenario: test_the_bounded_conclusion_names_what_it_did_not_reach
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_bounded_conclusion_names_what_it_did_not_reach`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_bounded_conclusion_names_what_it_did_not_reach PASSED [ 79%]`

### Scenario: test_the_full_population_conclusion_uses_a_universal_quantifier
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_full_population_conclusion_uses_a_universal_quantifier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_full_population_conclusion_uses_a_universal_quantifier PASSED [ 79%]`

### Scenario: test_the_two_conclusions_carry_different_types_in_the_dom
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_two_conclusions_carry_different_types_in_the_dom`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_two_conclusions_carry_different_types_in_the_dom PASSED [ 79%]`

### Scenario: test_at_zero_coverage_the_findings_region_is_absent_not_empty
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_the_findings_region_is_absent_not_empty`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_the_findings_region_is_absent_not_empty PASSED [ 79%]`

### Scenario: test_at_zero_coverage_no_finding_count_is_rendered_at_all
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_no_finding_count_is_rendered_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_no_finding_count_is_rendered_at_all PASSED [ 79%]`

### Scenario: test_the_partial_banner_is_absent_at_full_coverage
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_partial_banner_is_absent_at_full_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_partial_banner_is_absent_at_full_coverage PASSED [ 79%]`

### Scenario: test_an_explicit_zero_pending_state_is_visible
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_an_explicit_zero_pending_state_is_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_an_explicit_zero_pending_state_is_visible PASSED [ 80%]`

### Scenario: test_it_carries_the_runs_coverage_statement
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_carries_the_runs_coverage_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_carries_the_runs_coverage_statement PASSED [ 80%]`

### Scenario: test_it_is_not_a_blank_region_and_not_a_spinner
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_is_not_a_blank_region_and_not_a_spinner`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_is_not_a_blank_region_and_not_a_spinner PASSED [ 80%]`

### Scenario: test_AC_F33_07_the_recall_bias_label_sits_adjacent_at_equal_weight
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_07_the_recall_bias_label_sits_adjacent_at_equal_weight`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_07_the_recall_bias_label_sits_adjacent_at_equal_weight PASSED [ 80%]`

### Scenario: test_AC_F33_08_the_label_is_adjacent_to_the_recall_figure_not_at_the_card_foot
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_08_the_label_is_adjacent_to_the_recall_figure_not_at_the_card_foot`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_08_the_label_is_adjacent_to_the_recall_figure_not_at_the_card_foot PASSED [ 80%]`

### Scenario: test_it_is_not_inside_a_collapsed_region
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_it_is_not_inside_a_collapsed_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_it_is_not_inside_a_collapsed_region PASSED [ 80%]`

### Scenario: test_there_is_no_bulk_action_control_anywhere_on_the_queue
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_anywhere_on_the_queue`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_anywhere_on_the_queue PASSED [ 80%]`

### Scenario: test_no_row_offers_an_approve_control
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_no_row_offers_an_approve_control`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_no_row_offers_an_approve_control PASSED [ 80%]`

### Scenario: test_there_is_no_green_success_state_rendered
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_green_success_state_rendered`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_green_success_state_rendered PASSED [ 80%]`

### Scenario: test_AC_F38_01_every_required_fact_is_visible_on_the_screen
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_01_every_required_fact_is_visible_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_01_every_required_fact_is_visible_on_the_screen PASSED [ 80%]`

### Scenario: test_AC_F38_12_a_failed_tie_out_is_shown_with_its_date
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_a_failed_tie_out_is_shown_with_its_date`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_a_failed_tie_out_is_shown_with_its_date PASSED [ 80%]`

### Scenario: test_AC_F38_12_an_action_capable_run_over_it_is_refused_naming_the_tie_out
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_an_action_capable_run_over_it_is_refused_naming_the_tie_out`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_an_action_capable_run_over_it_is_refused_naming_the_tie_out PASSED [ 80%]`

### Scenario: test_AC_F38_09_an_action_capable_run_over_an_uncertified_dataset_is_refused
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_09_an_action_capable_run_over_an_uncertified_dataset_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_09_an_action_capable_run_over_an_uncertified_dataset_is_refused PASSED [ 80%]`

### Scenario: test_the_same_dataset_is_permitted_in_the_exploration_tier
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_the_same_dataset_is_permitted_in_the_exploration_tier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_the_same_dataset_is_permitted_in_the_exploration_tier PASSED [ 80%]`

### Scenario: test_AC_F38_13_a_tenant_with_no_certified_dataset_says_so_and_why
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_13_a_tenant_with_no_certified_dataset_says_so_and_why`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_13_a_tenant_with_no_certified_dataset_says_so_and_why PASSED [ 81%]`

### Scenario: test_AC_F38_16_every_columns_classification_is_visible
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_every_columns_classification_is_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_every_columns_classification_is_visible PASSED [ 81%]`

### Scenario: test_AC_F38_16_a_model_bound_run_over_an_unclassified_column_is_refused
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_a_model_bound_run_over_an_unclassified_column_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_a_model_bound_run_over_an_unclassified_column_is_refused PASSED [ 81%]`

### Scenario: test_an_unclassified_column_refuses_even_in_the_exploration_tier
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_an_unclassified_column_refuses_even_in_the_exploration_tier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_an_unclassified_column_refuses_even_in_the_exploration_tier PASSED [ 81%]`

### Scenario: test_AC_F36_19_an_agent_with_no_overrides_shows_an_explicit_zero
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F36_19_an_agent_with_no_overrides_shows_an_explicit_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F36_19_an_agent_with_no_overrides_shows_an_explicit_zero PASSED [ 81%]`

### Scenario: test_AC_F41_07_median_dwell_time_is_visible_per_agent_and_per_user
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_07_median_dwell_time_is_visible_per_agent_and_per_user`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_07_median_dwell_time_is_visible_per_agent_and_per_user PASSED [ 81%]`

### Scenario: test_AC_F12_10_probe_results_are_aggregate_only
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_probe_results_are_aggregate_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_probe_results_are_aggregate_only PASSED [ 81%]`

### Scenario: test_AC_F12_10_no_named_person_appears_anywhere_in_the_probe_panel
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_no_named_person_appears_anywhere_in_the_probe_panel`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_no_named_person_appears_anywhere_in_the_probe_panel PASSED [ 81%]`

### Scenario: test_the_probe_aggregation_keys_are_a_closed_list_not_a_parameter
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_aggregation_keys_are_a_closed_list_not_a_parameter`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_aggregation_keys_are_a_closed_list_not_a_parameter PASSED [ 81%]`

### Scenario: test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error PASSED [ 81%]`

### Scenario: test_AC_F32_10_the_forward_disposition_hit_rate_is_visible
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F32_10_the_forward_disposition_hit_rate_is_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F32_10_the_forward_disposition_hit_rate_is_visible PASSED [ 81%]`

### Scenario: test_the_hit_rate_is_a_real_figure_from_the_verification_job
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_hit_rate_is_a_real_figure_from_the_verification_job`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_hit_rate_is_a_real_figure_from_the_verification_job PASSED [ 81%]`

### Scenario: test_AC_F9_08_open_escalations_name_the_account_aggregate_period_and_leg
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_08_open_escalations_name_the_account_aggregate_period_and_leg`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_08_open_escalations_name_the_account_aggregate_period_and_leg PASSED [ 81%]`

### Scenario: test_AC_F9_04_each_escalation_carries_the_control_state_change_on_the_account
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_04_each_escalation_carries_the_control_state_change_on_the_account`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_04_each_escalation_carries_the_control_state_change_on_the_account PASSED [ 81%]`

### Scenario: test_AC_F9_05_an_account_with_too_little_history_says_so_by_name
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_05_an_account_with_too_little_history_says_so_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_05_an_account_with_too_little_history_says_so_by_name PASSED [ 82%]`

### Scenario: test_AC_F9_09_periods_with_no_recorded_explanation_are_named
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_09_periods_with_no_recorded_explanation_are_named`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_09_periods_with_no_recorded_explanation_are_named PASSED [ 82%]`

### Scenario: test_AC_F41_19_the_routed_count_against_the_cap_is_visible_per_reviewer
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_the_routed_count_against_the_cap_is_visible_per_reviewer`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_the_routed_count_against_the_cap_is_visible_per_reviewer PASSED [ 82%]`

### Scenario: test_AC_F41_19_a_raised_cap_names_who_raised_it
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_a_raised_cap_names_who_raised_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_a_raised_cap_names_who_raised_it PASSED [ 82%]`

### Scenario: test_a_broker_that_cannot_be_reached_renders_no_figure_at_all
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_a_broker_that_cannot_be_reached_renders_no_figure_at_all`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_a_broker_that_cannot_be_reached_renders_no_figure_at_all PASSED [ 82%]`

### Scenario: test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements PASSED [ 82%]`

### Scenario: test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version PASSED [ 82%]`

### Scenario: test_AC_F5_04_a_version_that_touched_nothing_states_zero
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_04_a_version_that_touched_nothing_states_zero`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_04_a_version_that_touched_nothing_states_zero PASSED [ 82%]`

### Scenario: test_AC_F5_05_every_lineage_result_states_its_own_completeness
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_05_every_lineage_result_states_its_own_completeness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_05_every_lineage_result_states_its_own_completeness PASSED [ 82%]`

### Scenario: test_no_agent_principal_holds_the_approval_capability
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_no_agent_principal_holds_the_approval_capability`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_no_agent_principal_holds_the_approval_capability PASSED [ 82%]`

### Scenario: test_AC_F1_09_the_dossier_list_for_the_period_is_visible
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_the_dossier_list_for_the_period_is_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_the_dossier_list_for_the_period_is_visible PASSED [ 82%]`

### Scenario: test_AC_F1_09_an_individual_dossiers_rendered_view_is_reachable_from_it
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_individual_dossiers_rendered_view_is_reachable_from_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_individual_dossiers_rendered_view_is_reachable_from_it PASSED [ 82%]`

### Scenario: test_AC_F1_09_an_export_control_for_the_period_is_visible
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_export_control_for_the_period_is_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_export_control_for_the_period_is_visible PASSED [ 82%]`

### Scenario: test_AC_F2_07_the_full_version_tuple_is_visible_on_this_screen
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F2_07_the_full_version_tuple_is_visible_on_this_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F2_07_the_full_version_tuple_is_visible_on_this_screen PASSED [ 82%]`

### Scenario: test_the_version_tuple_states_absences_rather_than_omitting_them
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_version_tuple_states_absences_rather_than_omitting_them`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_version_tuple_states_absences_rather_than_omitting_them PASSED [ 82%]`

### Scenario: test_AC_REFUSAL_04_refusal_events_are_retrievable_from_this_screen
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_REFUSAL_04_refusal_events_are_retrievable_from_this_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_REFUSAL_04_refusal_events_are_retrievable_from_this_screen PASSED [ 83%]`

### Scenario: test_the_export_states_the_two_guarantees_it_does_not_carry
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_export_states_the_two_guarantees_it_does_not_carry`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_export_states_the_two_guarantees_it_does_not_carry PASSED [ 83%]`

### Scenario: test_AC_REFUSAL_01_and_13_all_seven_refusals_are_visible_by_name
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_01_and_13_all_seven_refusals_are_visible_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_01_and_13_all_seven_refusals_are_visible_by_name PASSED [ 83%]`

### Scenario: test_each_refusal_states_the_reason_it_is_refused
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_each_refusal_states_the_reason_it_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_each_refusal_states_the_reason_it_is_refused PASSED [ 83%]`

### Scenario: test_AC_REFUSAL_02_the_by_design_wording_is_on_every_entry
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_by_design_wording_is_on_every_entry`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_by_design_wording_is_on_every_entry PASSED [ 83%]`

### Scenario: test_AC_REFUSAL_02_the_deferred_wording_shares_no_phrase_with_it
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_deferred_wording_shares_no_phrase_with_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_deferred_wording_shares_no_phrase_with_it PASSED [ 83%]`

### Scenario: test_the_list_is_served_by_the_broker_and_not_held_in_the_interface
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_list_is_served_by_the_broker_and_not_held_in_the_interface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_list_is_served_by_the_broker_and_not_held_in_the_interface PASSED [ 83%]`

### Scenario: test_the_screen_says_why_both_lists_are_on_it
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_screen_says_why_both_lists_are_on_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_screen_says_why_both_lists_are_on_it PASSED [ 83%]`

### Scenario: test_text_escapes_angle_brackets_and_ampersands
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_text_escapes_angle_brackets_and_ampersands`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_text_escapes_angle_brackets_and_ampersands PASSED [ 83%]`

### Scenario: test_attribute_values_escape_quotes_and_brackets
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_attribute_values_escape_quotes_and_brackets`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_attribute_values_escape_quotes_and_brackets PASSED [ 83%]`

### Scenario: test_a_data_derived_string_cannot_close_its_own_tag
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_a_data_derived_string_cannot_close_its_own_tag`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_a_data_derived_string_cannot_close_its_own_tag PASSED [ 83%]`

### Scenario: test_none_children_are_dropped_not_rendered_as_the_word_none
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_none_children_are_dropped_not_rendered_as_the_word_none`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_none_children_are_dropped_not_rendered_as_the_word_none PASSED [ 83%]`

### Scenario: test_text_of_none_is_empty_not_the_word_none
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_text_of_none_is_empty_not_the_word_none`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_text_of_none_is_empty_not_the_word_none PASSED [ 83%]`

### Scenario: test_numbers_are_coerced
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_numbers_are_coerced`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestEscaping::test_numbers_are_coerced PASSED [ 83%]`

### Scenario: test_underscores_become_hyphens_and_class_underscore_becomes_class
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_underscores_become_hyphens_and_class_underscore_becomes_class`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestAttributes::test_underscores_become_hyphens_and_class_underscore_becomes_class PASSED [ 84%]`

### Scenario: test_true_renders_bare_and_false_and_none_are_omitted
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_true_renders_bare_and_false_and_none_are_omitted`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestAttributes::test_true_renders_bare_and_false_and_none_are_omitted PASSED [ 84%]`

### Scenario: test_zero_is_rendered_not_treated_as_absent
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_zero_is_rendered_not_treated_as_absent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestAttributes::test_zero_is_rendered_not_treated_as_absent PASSED [ 84%]`

### Scenario: test_void_element_renders_without_a_closing_tag
- Input: `backend/tests/test_ui_html.py::TestStructure::test_void_element_renders_without_a_closing_tag`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_void_element_renders_without_a_closing_tag PASSED [ 84%]`

### Scenario: test_void_element_refuses_children
- Input: `backend/tests/test_ui_html.py::TestStructure::test_void_element_refuses_children`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_void_element_refuses_children PASSED [ 84%]`

### Scenario: test_bad_tag_name_is_refused
- Input: `backend/tests/test_ui_html.py::TestStructure::test_bad_tag_name_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_bad_tag_name_is_refused PASSED [ 84%]`

### Scenario: test_walk_yields_every_descendant_in_document_order
- Input: `backend/tests/test_ui_html.py::TestStructure::test_walk_yields_every_descendant_in_document_order`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_walk_yields_every_descendant_in_document_order PASSED [ 84%]`

### Scenario: test_fragment_has_no_wrapper_but_is_still_walkable
- Input: `backend/tests/test_ui_html.py::TestStructure::test_fragment_has_no_wrapper_but_is_still_walkable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_fragment_has_no_wrapper_but_is_still_walkable PASSED [ 84%]`

### Scenario: test_find_by_test_id_traverses_the_tree
- Input: `backend/tests/test_ui_html.py::TestStructure::test_find_by_test_id_traverses_the_tree`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_find_by_test_id_traverses_the_tree PASSED [ 84%]`

### Scenario: test_document_is_self_contained_and_carries_the_theme
- Input: `backend/tests/test_ui_html.py::TestStructure::test_document_is_self_contained_and_carries_the_theme`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestStructure::test_document_is_self_contained_and_carries_the_theme PASSED [ 84%]`

### Scenario: test_raw_passes_markup_through
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_passes_markup_through`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_passes_markup_through PASSED [ 84%]`

### Scenario: test_raw_refuses_a_non_string
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_refuses_a_non_string`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_refuses_a_non_string PASSED [ 84%]`

### Scenario: test_only_chrome_constructs_a_raw_in_the_ui_package
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_only_chrome_constructs_a_raw_in_the_ui_package`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_only_chrome_constructs_a_raw_in_the_ui_package PASSED [ 84%]`

### Scenario: test_mono_and_amount_carry_the_tabular_numeral_classes
- Input: `backend/tests/test_ui_html.py::TestHelpers::test_mono_and_amount_carry_the_tabular_numeral_classes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestHelpers::test_mono_and_amount_carry_the_tabular_numeral_classes PASSED [ 84%]`

### Scenario: test_kv_always_renders_both_halves
- Input: `backend/tests/test_ui_html.py::TestHelpers::test_kv_always_renders_both_halves`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_html.py::TestHelpers::test_kv_always_renders_both_halves PASSED [ 85%]`

### Scenario: test_the_proposal_is_reachable_from_the_entry_point_by_following_links
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_the_proposal_is_reachable_from_the_entry_point_by_following_links`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_the_proposal_is_reachable_from_the_entry_point_by_following_links PASSED [ 85%]`

### Scenario: test_it_is_linked_from_the_review_screen_of_the_item_that_produced_it
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_it_is_linked_from_the_review_screen_of_the_item_that_produced_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_it_is_linked_from_the_review_screen_of_the_item_that_produced_it PASSED [ 85%]`

### Scenario: test_only_the_item_with_a_posting_capable_outcome_links_to_a_proposal
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_only_the_item_with_a_posting_capable_outcome_links_to_a_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_only_the_item_with_a_posting_capable_outcome_links_to_a_proposal PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[no-posting-notice]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[no-posting-notice]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[no-posting-notice] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[risk-band]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[journal-lines]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-lines]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-lines] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[journal-line]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-line]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-line] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[two-key-model]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[two-key-model]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[two-key-model] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[authorship-closure]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED [ 85%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[approve-lines]
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[approve-lines]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[approve-lines] PASSED [ 85%]`

### Scenario: test_the_screen_states_in_plain_words_that_it_does_not_post
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_screen_states_in_plain_words_that_it_does_not_post`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_screen_states_in_plain_words_that_it_does_not_post PASSED [ 85%]`

### Scenario: test_the_approve_label_names_the_lines_and_the_word_export
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_approve_label_names_the_lines_and_the_word_export`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_approve_label_names_the_lines_and_the_word_export PASSED [ 85%]`

### Scenario: test_the_word_post_never_appears_as_a_control_label
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_word_post_never_appears_as_a_control_label`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_word_post_never_appears_as_a_control_label PASSED [ 85%]`

### Scenario: test_no_posting_library_is_a_dependency_of_this_build
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_no_posting_library_is_a_dependency_of_this_build`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_no_posting_library_is_a_dependency_of_this_build PASSED [ 85%]`

### Scenario: test_the_lines_precede_the_approve_control_in_reading_order
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_precede_the_approve_control_in_reading_order`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_precede_the_approve_control_in_reading_order PASSED [ 86%]`

### Scenario: test_both_lines_are_rendered_with_their_full_coding
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_both_lines_are_rendered_with_their_full_coding`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_both_lines_are_rendered_with_their_full_coding PASSED [ 86%]`

### Scenario: test_the_lines_are_not_inside_a_collapsed_region
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_are_not_inside_a_collapsed_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_are_not_inside_a_collapsed_region PASSED [ 86%]`

### Scenario: test_the_two_sides_balance_on_the_face_of_the_rendering
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_two_sides_balance_on_the_face_of_the_rendering`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_two_sides_balance_on_the_face_of_the_rendering PASSED [ 86%]`

### Scenario: test_the_two_key_model_names_three_distinct_roles
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_two_key_model_names_three_distinct_roles`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_two_key_model_names_three_distinct_roles PASSED [ 86%]`

### Scenario: test_the_closure_is_stated_as_author_approver_invoker
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_closure_is_stated_as_author_approver_invoker`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_closure_is_stated_as_author_approver_invoker PASSED [ 86%]`

### Scenario: test_the_author_and_the_invoker_are_named_separately
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_author_and_the_invoker_are_named_separately`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_author_and_the_invoker_are_named_separately PASSED [ 86%]`

### Scenario: test_the_approver_slot_is_empty_until_someone_approves
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_approver_slot_is_empty_until_someone_approves`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_approver_slot_is_empty_until_someone_approves PASSED [ 86%]`

### Scenario: test_the_decision_id_that_authorised_the_view_is_on_the_screen
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_decision_id_that_authorised_the_view_is_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_decision_id_that_authorised_the_view_is_on_the_screen PASSED [ 86%]`

### Scenario: test_the_approve_control_is_absent_not_disabled_on_a_superseded_run
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_approve_control_is_absent_not_disabled_on_a_superseded_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_approve_control_is_absent_not_disabled_on_a_superseded_run PASSED [ 86%]`

### Scenario: test_the_block_names_the_superseding_run_and_its_completion_time
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_names_the_superseding_run_and_its_completion_time`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_names_the_superseding_run_and_its_completion_time PASSED [ 86%]`

### Scenario: test_the_only_forward_action_is_to_open_the_superseding_run
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_only_forward_action_is_to_open_the_superseding_run`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_only_forward_action_is_to_open_the_superseding_run PASSED [ 86%]`

### Scenario: test_the_block_is_not_dismissible
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_is_not_dismissible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_is_not_dismissible PASSED [ 86%]`

### Scenario: test_AC_F41_01_there_is_no_control_that_approves_more_than_this_proposal
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_AC_F41_01_there_is_no_control_that_approves_more_than_this_proposal`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_AC_F41_01_there_is_no_control_that_approves_more_than_this_proposal PASSED [ 86%]`

### Scenario: test_there_is_no_checkbox_and_no_multi_select_on_the_screen
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_there_is_no_checkbox_and_no_multi_select_on_the_screen`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_there_is_no_checkbox_and_no_multi_select_on_the_screen PASSED [ 87%]`

### Scenario: test_the_form_posts_to_this_proposals_own_endpoint
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_the_form_posts_to_this_proposals_own_endpoint`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_the_form_posts_to_this_proposals_own_endpoint PASSED [ 87%]`

### Scenario: test_approving_is_not_reachable_by_a_get
- Input: `backend/tests/test_ui_proposal.py::TestTheApprovalEndpointIsPostOnly::test_approving_is_not_reachable_by_a_get`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestTheApprovalEndpointIsPostOnly::test_approving_is_not_reachable_by_a_get PASSED [ 87%]`

### Scenario: test_the_stamp_carries_the_bundle_the_decision_and_the_cuec_date
- Input: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_stamp_carries_the_bundle_the_decision_and_the_cuec_date`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_stamp_carries_the_bundle_the_decision_and_the_cuec_date PASSED [ 87%]`

### Scenario: test_the_accounting_date_and_journal_source_are_on_the_face_of_it
- Input: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_accounting_date_and_journal_source_are_on_the_face_of_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_accounting_date_and_journal_source_are_on_the_face_of_it PASSED [ 87%]`

### Scenario: test_readiness_is_reachable_from_the_entry_point_by_following_links
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_readiness_is_reachable_from_the_entry_point_by_following_links`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_readiness_is_reachable_from_the_entry_point_by_following_links PASSED [ 87%]`

### Scenario: test_it_has_a_permanent_place_in_the_navigation
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_it_has_a_permanent_place_in_the_navigation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_it_has_a_permanent_place_in_the_navigation PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[readiness-statement]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-statement]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-statement] PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[readiness-conditions]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-conditions]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-conditions] PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[readiness-condition]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-condition]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-condition] PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[readiness-basis]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-basis]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-basis] PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[precision-figure]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[precision-figure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[precision-figure] PASSED [ 87%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[label-source-statement]
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[label-source-statement]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[label-source-statement] PASSED [ 87%]`

### Scenario: test_exactly_five_conditions_render
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_exactly_five_conditions_render`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_exactly_five_conditions_render PASSED [ 87%]`

### Scenario: test_they_are_P1_through_P5_in_order
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_they_are_P1_through_P5_in_order`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_they_are_P1_through_P5_in_order PASSED [ 88%]`

### Scenario: test_each_carries_its_own_state_and_its_own_sentence
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_each_carries_its_own_state_and_its_own_sentence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_each_carries_its_own_state_and_its_own_sentence PASSED [ 88%]`

### Scenario: test_P1_and_P5_report_not_yet_evaluable_and_NAME_the_deferral
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_P1_and_P5_report_not_yet_evaluable_and_NAME_the_deferral`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_P1_and_P5_report_not_yet_evaluable_and_NAME_the_deferral PASSED [ 88%]`

### Scenario: test_not_yet_evaluable_is_visually_distinct_from_not_met
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_not_yet_evaluable_is_visually_distinct_from_not_met`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_not_yet_evaluable_is_visually_distinct_from_not_met PASSED [ 88%]`

### Scenario: test_the_screen_carries_all_three_states_at_once
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_the_screen_carries_all_three_states_at_once`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_the_screen_carries_all_three_states_at_once PASSED [ 88%]`

### Scenario: test_a_short_evidence_window_reports_not_yet_evaluable_rather_than_not_met
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_a_short_evidence_window_reports_not_yet_evaluable_rather_than_not_met`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_a_short_evidence_window_reports_not_yet_evaluable_rather_than_not_met PASSED [ 88%]`

### Scenario: test_the_report_does_not_assert_readiness
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_report_does_not_assert_readiness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_report_does_not_assert_readiness PASSED [ 88%]`

### Scenario: test_the_basis_is_stated_on_the_face_of_the_report
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_basis_is_stated_on_the_face_of_the_report`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_basis_is_stated_on_the_face_of_the_report PASSED [ 88%]`

### Scenario: test_the_conditions_precede_the_precision_figure_in_reading_order
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_conditions_precede_the_precision_figure_in_reading_order`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_conditions_precede_the_precision_figure_in_reading_order PASSED [ 88%]`

### Scenario: test_the_screen_explains_why_the_precision_figure_is_not_the_gate
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_screen_explains_why_the_precision_figure_is_not_the_gate`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_screen_explains_why_the_precision_figure_is_not_the_gate PASSED [ 88%]`

### Scenario: test_readiness_is_computed_from_the_conditions_and_not_from_the_figure
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_readiness_is_computed_from_the_conditions_and_not_from_the_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_readiness_is_computed_from_the_conditions_and_not_from_the_figure PASSED [ 88%]`

### Scenario: test_the_label_source_is_rendered_adjacent_to_the_figure
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_label_source_is_rendered_adjacent_to_the_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_label_source_is_rendered_adjacent_to_the_figure PASSED [ 88%]`

### Scenario: test_the_statement_says_the_figure_measures_agreement_not_correctness
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_says_the_figure_measures_agreement_not_correctness`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_says_the_figure_measures_agreement_not_correctness PASSED [ 88%]`

### Scenario: test_an_acceptance_derived_figure_is_marked_not_promotion_usable
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_is_marked_not_promotion_usable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_is_marked_not_promotion_usable PASSED [ 88%]`

### Scenario: test_the_statement_is_rendered_at_warning_weight_not_as_a_footnote
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_is_rendered_at_warning_weight_not_as_a_footnote`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_is_rendered_at_warning_weight_not_as_a_footnote PASSED [ 89%]`

### Scenario: test_it_is_not_inside_a_collapsed_region
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_it_is_not_inside_a_collapsed_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_it_is_not_inside_a_collapsed_region PASSED [ 89%]`

### Scenario: test_the_denominator_is_stated_with_the_figure
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_denominator_is_stated_with_the_figure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_denominator_is_stated_with_the_figure PASSED [ 89%]`

### Scenario: test_a_figure_cannot_be_constructed_without_a_label_source
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_a_figure_cannot_be_constructed_without_a_label_source`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_a_figure_cannot_be_constructed_without_a_label_source PASSED [ 89%]`

### Scenario: test_an_acceptance_derived_figure_cannot_be_offered_as_promotion_evidence
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_cannot_be_offered_as_promotion_evidence`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_cannot_be_offered_as_promotion_evidence PASSED [ 89%]`

### Scenario: test_a_met_condition_is_not_rendered_as_a_success
- Input: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_a_met_condition_is_not_rendered_as_a_success`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_a_met_condition_is_not_rendered_as_a_success PASSED [ 89%]`

### Scenario: test_the_screen_carries_no_tick_or_success_glyph
- Input: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_the_screen_carries_no_tick_or_success_glyph`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_the_screen_carries_no_tick_or_success_glyph PASSED [ 89%]`

### Scenario: test_a_review_item_is_reachable_from_the_entry_point_by_following_links
- Input: `backend/tests/test_ui_review.py::TestReachability::test_a_review_item_is_reachable_from_the_entry_point_by_following_links`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_a_review_item_is_reachable_from_the_entry_point_by_following_links PASSED [ 89%]`

### Scenario: test_the_queue_index_links_to_this_item
- Input: `backend/tests/test_ui_review.py::TestReachability::test_the_queue_index_links_to_this_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_the_queue_index_links_to_this_item PASSED [ 89%]`

### Scenario: test_the_exceptions_queue_links_to_this_item
- Input: `backend/tests/test_ui_review.py::TestReachability::test_the_exceptions_queue_links_to_this_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_the_exceptions_queue_links_to_this_item PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[risk-band]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure] PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[evidence-set]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set] PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[in-force-panel]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel] PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[authorship-closure]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED [ 89%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[resolution-row]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-row]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-row] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[resolution-button]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-button]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-button] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[forward-disposition]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[forward-disposition]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[forward-disposition] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[clears-by]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[clears-by]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[clears-by] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[rejection-reasons]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reasons]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reasons] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[rejection-reason]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reason]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reason] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[reject-submit]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[reject-submit]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[reject-submit] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[agent-narrative]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative] PASSED [ 90%]`

### Scenario: test_component_is_present_in_the_tree_the_route_returned[dossier-link]
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-link]`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-link] PASSED [ 90%]`

### Scenario: test_the_risk_band_precedes_the_evidence_the_resolution_and_the_narrative
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_risk_band_precedes_the_evidence_the_resolution_and_the_narrative`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_risk_band_precedes_the_evidence_the_resolution_and_the_narrative PASSED [ 90%]`

### Scenario: test_the_narrative_is_last_of_the_four
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_narrative_is_last_of_the_four`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_narrative_is_last_of_the_four PASSED [ 90%]`

### Scenario: test_the_evidence_precedes_the_resolution
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_evidence_precedes_the_resolution`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_evidence_precedes_the_resolution PASSED [ 90%]`

### Scenario: test_AC_F41_03_it_is_outside_every_collapsible_region
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_AC_F41_03_it_is_outside_every_collapsible_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheRiskBand::test_AC_F41_03_it_is_outside_every_collapsible_region PASSED [ 90%]`

### Scenario: test_the_riskiest_figure_is_the_aggregate_not_this_periods_movement
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_the_riskiest_figure_is_the_aggregate_not_this_periods_movement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheRiskBand::test_the_riskiest_figure_is_the_aggregate_not_this_periods_movement PASSED [ 90%]`

### Scenario: test_it_carries_the_threshold_it_was_individually_under
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_carries_the_threshold_it_was_individually_under`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_carries_the_threshold_it_was_individually_under PASSED [ 91%]`

### Scenario: test_it_is_declared_at_the_riskiest_font_size_and_nothing_else_is
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_is_declared_at_the_riskiest_font_size_and_nothing_else_is`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_is_declared_at_the_riskiest_font_size_and_nothing_else_is PASSED [ 91%]`

### Scenario: test_no_confidence_score_is_rendered_beside_it
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_no_confidence_score_is_rendered_beside_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheRiskBand::test_no_confidence_score_is_rendered_beside_it PASSED [ 91%]`

### Scenario: test_no_button_on_this_screen_approves_anything
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_button_on_this_screen_approves_anything`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_button_on_this_screen_approves_anything PASSED [ 91%]`

### Scenario: test_no_form_on_this_screen_posts_to_an_approval_endpoint
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_form_on_this_screen_posts_to_an_approval_endpoint`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_form_on_this_screen_posts_to_an_approval_endpoint PASSED [ 91%]`

### Scenario: test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible PASSED [ 91%]`

### Scenario: test_AC_F41_02_no_control_is_preselected_prechecked_or_prefilled
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_02_no_control_is_preselected_prechecked_or_prefilled`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_02_no_control_is_preselected_prechecked_or_prefilled PASSED [ 91%]`

### Scenario: test_the_item_state_reads_not_approved
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_the_item_state_reads_not_approved`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_the_item_state_reads_not_approved PASSED [ 91%]`

### Scenario: test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected PASSED [ 91%]`

### Scenario: test_only_R3_and_R4_are_marked_as_posting_capable
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_only_R3_and_R4_are_marked_as_posting_capable`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_only_R3_and_R4_are_marked_as_posting_capable PASSED [ 91%]`

### Scenario: test_the_posts_flag_is_visible_on_those_two_and_on_no_other
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posts_flag_is_visible_on_those_two_and_on_no_other`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posts_flag_is_visible_on_those_two_and_on_no_other PASSED [ 91%]`

### Scenario: test_AC_F35_05_no_safe_outcome_costs_more_interactions_than_a_posting_one
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_05_no_safe_outcome_costs_more_interactions_than_a_posting_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_05_no_safe_outcome_costs_more_interactions_than_a_posting_one PASSED [ 91%]`

### Scenario: test_the_counts_on_screen_are_the_ones_the_model_derives
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_counts_on_screen_are_the_ones_the_model_derives`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_counts_on_screen_are_the_ones_the_model_derives PASSED [ 91%]`

### Scenario: test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent PASSED [ 91%]`

### Scenario: test_the_posting_capable_types_are_not_first_not_larger_and_not_default
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posting_capable_types_are_not_first_not_larger_and_not_default`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posting_capable_types_are_not_first_not_larger_and_not_default PASSED [ 92%]`

### Scenario: test_AC_F32_01_the_clearing_period_control_is_required
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_AC_F32_01_the_clearing_period_control_is_required`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestForwardDisposition::test_AC_F32_01_the_clearing_period_control_is_required PASSED [ 92%]`

### Scenario: test_it_is_never_prefilled
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_never_prefilled`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_never_prefilled PASSED [ 92%]`

### Scenario: test_it_is_framed_as_a_promise_rather_than_as_a_validation_error
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_framed_as_a_promise_rather_than_as_a_validation_error`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_framed_as_a_promise_rather_than_as_a_validation_error PASSED [ 92%]`

### Scenario: test_AC_F41_06_the_reason_list_is_closed_and_has_six_options
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_AC_F41_06_the_reason_list_is_closed_and_has_six_options`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestStructuredRejection::test_AC_F41_06_the_reason_list_is_closed_and_has_six_options PASSED [ 92%]`

### Scenario: test_no_reason_is_preselected
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_no_reason_is_preselected`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestStructuredRejection::test_no_reason_is_preselected PASSED [ 92%]`

### Scenario: test_free_text_sits_underneath_the_list_rather_than_instead_of_it
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_free_text_sits_underneath_the_list_rather_than_instead_of_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestStructuredRejection::test_free_text_sits_underneath_the_list_rather_than_instead_of_it PASSED [ 92%]`

### Scenario: test_the_submit_control_states_that_a_reason_is_required
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_the_submit_control_states_that_a_reason_is_required`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestStructuredRejection::test_the_submit_control_states_that_a_reason_is_required PASSED [ 92%]`

### Scenario: test_it_is_a_details_element_with_no_open_attribute
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_it_is_a_details_element_with_no_open_attribute`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheNarrative::test_it_is_a_details_element_with_no_open_attribute PASSED [ 92%]`

### Scenario: test_UX_KB_2_it_is_collapsed_on_first_render_without_any_script
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_UX_KB_2_it_is_collapsed_on_first_render_without_any_script`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheNarrative::test_UX_KB_2_it_is_collapsed_on_first_render_without_any_script PASSED [ 92%]`

### Scenario: test_nothing_load_bearing_is_inside_it
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_nothing_load_bearing_is_inside_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheNarrative::test_nothing_load_bearing_is_inside_it PASSED [ 92%]`

### Scenario: test_AC_F41_05_and_F36_18_threshold_and_bundle_version_are_both_visible
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_05_and_F36_18_threshold_and_bundle_version_are_both_visible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_05_and_F36_18_threshold_and_bundle_version_are_both_visible PASSED [ 92%]`

### Scenario: test_the_full_stamp_is_present_and_none_of_it_is_behind_a_disclosure
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_full_stamp_is_present_and_none_of_it_is_behind_a_disclosure`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_full_stamp_is_present_and_none_of_it_is_behind_a_disclosure PASSED [ 92%]`

### Scenario: test_AC_F41_20_ineligibility_is_shown_at_queue_entry_with_its_reason
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_20_ineligibility_is_shown_at_queue_entry_with_its_reason`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_20_ineligibility_is_shown_at_queue_entry_with_its_reason PASSED [ 92%]`

### Scenario: test_the_queue_index_shows_the_ineligibility_before_the_item_is_opened
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_queue_index_shows_the_ineligibility_before_the_item_is_opened`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_queue_index_shows_the_ineligibility_before_the_item_is_opened PASSED [ 92%]`

### Scenario: test_the_closure_names_all_three_identities
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_closure_names_all_three_identities`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_closure_names_all_three_identities PASSED [ 93%]`

### Scenario: test_no_element_carries_data_in_a_title_attribute
- Input: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_no_element_carries_data_in_a_title_attribute`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_no_element_carries_data_in_a_title_attribute PASSED [ 93%]`

### Scenario: test_there_is_no_script_no_fetch_and_no_lazy_loading
- Input: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_there_is_no_script_no_fetch_and_no_lazy_loading`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_there_is_no_script_no_fetch_and_no_lazy_loading PASSED [ 93%]`

### Scenario: test_an_item_the_viewer_may_approve_still_offers_no_approve_control
- Input: `backend/tests/test_ui_review.py::TestEligibleItemStillHasNoApproveControl::test_an_item_the_viewer_may_approve_still_offers_no_approve_control`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestEligibleItemStillHasNoApproveControl::test_an_item_the_viewer_may_approve_still_offers_no_approve_control PASSED [ 93%]`

### Scenario: test_the_abstention_block_is_on_the_review_screen_for_that_item
- Input: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_the_abstention_block_is_on_the_review_screen_for_that_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_the_abstention_block_is_on_the_review_screen_for_that_item PASSED [ 93%]`

### Scenario: test_it_appears_before_the_evidence_and_outside_any_collapsed_region
- Input: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_it_appears_before_the_evidence_and_outside_any_collapsed_region`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_it_appears_before_the_evidence_and_outside_any_collapsed_region PASSED [ 93%]`

### Scenario: test_AC_F41_01_no_control_disposes_of_more_than_one_item
- Input: `backend/tests/test_ui_review.py::TestNoBulkAction::test_AC_F41_01_no_control_disposes_of_more_than_one_item`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoBulkAction::test_AC_F41_01_no_control_disposes_of_more_than_one_item PASSED [ 93%]`

### Scenario: test_the_index_offers_no_multi_select_either
- Input: `backend/tests/test_ui_review.py::TestNoBulkAction::test_the_index_offers_no_multi_select_either`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestNoBulkAction::test_the_index_offers_no_multi_select_either PASSED [ 93%]`

### Scenario: test_the_write_endpoints_are_post_only
- Input: `backend/tests/test_ui_review.py::TestTheWritePathRecords::test_the_write_endpoints_are_post_only`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_review.py::TestTheWritePathRecords::test_the_write_endpoints_are_post_only PASSED [ 93%]`

### Scenario: test_hex_parsing_rejects_anything_that_is_not_six_digit_hex
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_hex_parsing_rejects_anything_that_is_not_six_digit_hex`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestColourMaths::test_hex_parsing_rejects_anything_that_is_not_six_digit_hex PASSED [ 93%]`

### Scenario: test_known_hues
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_known_hues`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestColourMaths::test_known_hues PASSED [ 93%]`

### Scenario: test_chroma_is_zero_for_a_grey
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_chroma_is_zero_for_a_grey`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestColourMaths::test_chroma_is_zero_for_a_grey PASSED [ 93%]`

### Scenario: test_neither_shipped_palette_contains_a_green
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_neither_shipped_palette_contains_a_green`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_neither_shipped_palette_contains_a_green PASSED [ 93%]`

### Scenario: test_every_token_individually
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_every_token_individually`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_every_token_individually PASSED [ 93%]`

### Scenario: test_a_planted_success_green_is_caught
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_planted_success_green_is_caught`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_planted_success_green_is_caught PASSED [ 94%]`

### Scenario: test_a_muted_sage_green_is_also_caught
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_muted_sage_green_is_also_caught`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_muted_sage_green_is_also_caught PASSED [ 94%]`

### Scenario: test_a_teal_leaning_green_is_caught
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_teal_leaning_green_is_caught`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_teal_leaning_green_is_caught PASSED [ 94%]`

### Scenario: test_the_paper_neutrals_are_exempt_by_chroma_not_by_name
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_the_paper_neutrals_are_exempt_by_chroma_not_by_name`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_the_paper_neutrals_are_exempt_by_chroma_not_by_name PASSED [ 94%]`

### Scenario: test_blue_and_the_risk_ramp_are_not_caught
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_blue_and_the_risk_ramp_are_not_caught`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestNoGreen::test_blue_and_the_risk_ramp_are_not_caught PASSED [ 94%]`

### Scenario: test_light_ramp_darkens_monotonically_with_rank
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_light_ramp_darkens_monotonically_with_rank`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_light_ramp_darkens_monotonically_with_rank PASSED [ 94%]`

### Scenario: test_dark_ramp_BRIGHTENS_monotonically_with_rank
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_dark_ramp_BRIGHTENS_monotonically_with_rank`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_dark_ramp_BRIGHTENS_monotonically_with_rank PASSED [ 94%]`

### Scenario: test_each_step_is_perceptibly_separated_from_its_neighbour
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_each_step_is_perceptibly_separated_from_its_neighbour`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_each_step_is_perceptibly_separated_from_its_neighbour PASSED [ 94%]`

### Scenario: test_there_are_exactly_three_steps
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_there_are_exactly_three_steps`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_there_are_exactly_three_steps PASSED [ 94%]`

### Scenario: test_black_on_white_is_21
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_black_on_white_is_21`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestContrast::test_black_on_white_is_21 PASSED [ 94%]`

### Scenario: test_ratio_is_symmetric
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_ratio_is_symmetric`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestContrast::test_ratio_is_symmetric PASSED [ 94%]`

### Scenario: test_body_ink_on_base_meets_aa_in_both_themes
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_body_ink_on_base_meets_aa_in_both_themes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestContrast::test_body_ink_on_base_meets_aa_in_both_themes PASSED [ 94%]`

### Scenario: test_every_ink_meets_aa_on_EVERY_ground_in_both_themes
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_every_ink_meets_aa_on_EVERY_ground_in_both_themes`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestContrast::test_every_ink_meets_aa_on_EVERY_ground_in_both_themes PASSED [ 94%]`

### Scenario: test_every_risk_step_meets_aa_on_its_own_ground
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_every_risk_step_meets_aa_on_its_own_ground`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_tokens.py::TestContrast::test_every_risk_step_meets_aa_on_its_own_ground PASSED [ 94%]`

### Scenario: test_a_save_posted_without_a_clearing_period_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_save_posted_without_a_clearing_period_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_save_posted_without_a_clearing_period_does_not_complete PASSED [ 95%]`

### Scenario: test_the_item_remains_open_and_no_partial_record_exists
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_item_remains_open_and_no_partial_record_exists`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_item_remains_open_and_no_partial_record_exists PASSED [ 95%]`

### Scenario: test_the_response_names_the_missing_expected_clearing_period
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_response_names_the_missing_expected_clearing_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_response_names_the_missing_expected_clearing_period PASSED [ 95%]`

### Scenario: test_there_is_no_bypass_parameter_at_any_permission_level
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_there_is_no_bypass_parameter_at_any_permission_level`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_there_is_no_bypass_parameter_at_any_permission_level PASSED [ 95%]`

### Scenario: test_a_controller_gets_exactly_the_same_refusal_as_a_staff_accountant
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_controller_gets_exactly_the_same_refusal_as_a_staff_accountant`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_controller_gets_exactly_the_same_refusal_as_a_staff_accountant PASSED [ 95%]`

### Scenario: test_a_clearing_period_not_later_than_the_current_one_is_refused
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_not_later_than_the_current_one_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_not_later_than_the_current_one_is_refused PASSED [ 95%]`

### Scenario: test_a_clearing_period_beyond_the_maximum_horizon_is_refused
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_beyond_the_maximum_horizon_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_beyond_the_maximum_horizon_is_refused PASSED [ 95%]`

### Scenario: test_a_malformed_clearing_period_fails_the_same_way_as_a_missing_one
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_malformed_clearing_period_fails_the_same_way_as_a_missing_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_malformed_clearing_period_fails_the_same_way_as_a_missing_one PASSED [ 95%]`

### Scenario: test_a_close_with_no_resolution_type_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_close_with_no_resolution_type_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_close_with_no_resolution_type_does_not_complete PASSED [ 95%]`

### Scenario: test_an_r1_without_an_expiry_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r1_without_an_expiry_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r1_without_an_expiry_does_not_complete PASSED [ 95%]`

### Scenario: test_an_r5_without_both_an_owner_and_a_due_date_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r5_without_both_an_owner_and_a_due_date_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r5_without_both_an_owner_and_a_due_date_does_not_complete PASSED [ 95%]`

### Scenario: test_a_valid_r2_completes_and_the_store_holds_it
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_valid_r2_completes_and_the_store_holds_it`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_valid_r2_completes_and_the_store_holds_it PASSED [ 95%]`

### Scenario: test_a_closed_item_carries_exactly_one_resolution_type
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_closed_item_carries_exactly_one_resolution_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_closed_item_carries_exactly_one_resolution_type PASSED [ 95%]`

### Scenario: test_an_r6_with_an_unreadable_auto_pass_value_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_with_an_unreadable_auto_pass_value_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_with_an_unreadable_auto_pass_value_does_not_complete PASSED [ 95%]`

### Scenario: test_an_r6_changes_the_accounts_control_state_observably
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_changes_the_accounts_control_state_observably`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_changes_the_accounts_control_state_observably PASSED [ 96%]`

### Scenario: test_every_disposition_carries_a_capture_in_the_same_transaction
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_every_disposition_carries_a_capture_in_the_same_transaction`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_every_disposition_carries_a_capture_in_the_same_transaction PASSED [ 96%]`

### Scenario: test_elapsed_time_is_measured_from_the_servers_presentation_clock
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_elapsed_time_is_measured_from_the_servers_presentation_clock`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_elapsed_time_is_measured_from_the_servers_presentation_clock PASSED [ 96%]`

### Scenario: test_re_reading_an_item_does_not_restart_the_clock
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_re_reading_an_item_does_not_restart_the_clock`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_re_reading_an_item_does_not_restart_the_clock PASSED [ 96%]`

### Scenario: test_the_capture_names_what_was_expanded_and_what_was_collapsed
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_the_capture_names_what_was_expanded_and_what_was_collapsed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_the_capture_names_what_was_expanded_and_what_was_collapsed PASSED [ 96%]`

### Scenario: test_a_capture_that_cannot_be_written_leaves_the_item_open
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_a_capture_that_cannot_be_written_leaves_the_item_open`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_a_capture_that_cannot_be_written_leaves_the_item_open PASSED [ 96%]`

### Scenario: test_a_rejection_with_no_reason_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_rejection_with_no_reason_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_rejection_with_no_reason_does_not_complete PASSED [ 96%]`

### Scenario: test_a_reason_outside_the_closed_list_does_not_complete
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_reason_outside_the_closed_list_does_not_complete`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_reason_outside_the_closed_list_does_not_complete PASSED [ 96%]`

### Scenario: test_a_structured_rejection_records
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_structured_rejection_records`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_structured_rejection_records PASSED [ 96%]`

### Scenario: test_the_closed_list_is_a_constraint_on_the_column_not_a_form_check
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_the_closed_list_is_a_constraint_on_the_column_not_a_form_check`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_the_closed_list_is_a_constraint_on_the_column_not_a_form_check PASSED [ 96%]`

### Scenario: test_a_staff_accountant_is_denied_by_the_capability_set_test
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_staff_accountant_is_denied_by_the_capability_set_test`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_staff_accountant_is_denied_by_the_capability_set_test PASSED [ 96%]`

### Scenario: test_that_denial_offers_no_override_control_because_it_is_not_eligible
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_that_denial_offers_no_override_control_because_it_is_not_eligible`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_that_denial_offers_no_override_control_because_it_is_not_eligible PASSED [ 96%]`

### Scenario: test_a_controller_above_the_limit_is_denied_and_offered_an_override
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_controller_above_the_limit_is_denied_and_offered_an_override`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_controller_above_the_limit_is_denied_and_offered_an_override PASSED [ 96%]`

### Scenario: test_the_override_control_requires_a_second_authoriser_and_a_reason_code
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_override_control_requires_a_second_authoriser_and_a_reason_code`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_override_control_requires_a_second_authoriser_and_a_reason_code PASSED [ 96%]`

### Scenario: test_the_reason_list_comes_from_the_broker_not_from_the_interface
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_reason_list_comes_from_the_broker_not_from_the_interface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_reason_list_comes_from_the_broker_not_from_the_interface PASSED [ 96%]`

### Scenario: test_an_override_with_a_second_authoriser_completes_the_approval
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_with_a_second_authoriser_completes_the_approval`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_with_a_second_authoriser_completes_the_approval PASSED [ 97%]`

### Scenario: test_an_override_naming_the_requester_as_an_authoriser_is_refused
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_naming_the_requester_as_an_authoriser_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_naming_the_requester_as_an_authoriser_is_refused PASSED [ 97%]`

### Scenario: test_no_approval_record_exists_without_a_broker_decision_id
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_no_approval_record_exists_without_a_broker_decision_id`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_no_approval_record_exists_without_a_broker_decision_id PASSED [ 97%]`

### Scenario: test_when_persisting_the_approval_fails_the_proposal_stays_unapproved
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_when_persisting_the_approval_fails_the_proposal_stays_unapproved`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_when_persisting_the_approval_fails_the_proposal_stays_unapproved PASSED [ 97%]`

### Scenario: test_a_broker_that_cannot_be_reached_is_not_rendered_as_a_denial
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_broker_that_cannot_be_reached_is_not_rendered_as_a_denial`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_broker_that_cannot_be_reached_is_not_rendered_as_a_denial PASSED [ 97%]`

### Scenario: test_an_export_without_an_in_product_approval_is_refused
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_without_an_in_product_approval_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_without_an_in_product_approval_is_refused PASSED [ 97%]`

### Scenario: test_the_refusal_is_at_ges_and_not_only_in_the_interface
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_refusal_is_at_ges_and_not_only_in_the_interface`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_refusal_is_at_ges_and_not_only_in_the_interface PASSED [ 97%]`

### Scenario: test_an_approved_proposal_produces_a_balanced_file
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_approved_proposal_produces_a_balanced_file`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_approved_proposal_produces_a_balanced_file PASSED [ 97%]`

### Scenario: test_the_file_carries_the_reserved_source_and_category_and_no_other
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_file_carries_the_reserved_source_and_category_and_no_other`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_file_carries_the_reserved_source_and_category_and_no_other PASSED [ 97%]`

### Scenario: test_our_identifiers_are_stamped_into_the_reference_columns
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_our_identifiers_are_stamped_into_the_reference_columns`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_our_identifiers_are_stamped_into_the_reference_columns PASSED [ 97%]`

### Scenario: test_an_export_with_unverified_cuecs_is_refused_naming_them
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_with_unverified_cuecs_is_refused_naming_them`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_with_unverified_cuecs_is_refused_naming_them PASSED [ 97%]`

### Scenario: test_never_verified_is_not_collapsed_into_failed
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_never_verified_is_not_collapsed_into_failed`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_never_verified_is_not_collapsed_into_failed PASSED [ 97%]`

### Scenario: test_an_expired_verification_is_not_a_pass
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_expired_verification_is_not_a_pass`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_expired_verification_is_not_a_pass PASSED [ 97%]`

### Scenario: test_zero_approved_lines_produces_no_file_rather_than_an_empty_one
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_zero_approved_lines_produces_no_file_rather_than_an_empty_one`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_zero_approved_lines_produces_no_file_rather_than_an_empty_one PASSED [ 97%]`

### Scenario: test_an_unbalanced_batch_is_refused_rather_than_written
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_unbalanced_batch_is_refused_rather_than_written`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_unbalanced_batch_is_refused_rather_than_written PASSED [ 98%]`

### Scenario: test_the_export_module_has_no_submit_and_no_http_call
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_export_module_has_no_submit_and_no_http_call`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_export_module_has_no_submit_and_no_http_call PASSED [ 98%]`

### Scenario: test_no_route_on_the_ui_surface_names_a_posting_verb
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_no_route_on_the_ui_surface_names_a_posting_verb`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_no_route_on_the_ui_surface_names_a_posting_verb PASSED [ 98%]`

### Scenario: test_the_produced_artefact_states_that_it_posts_nothing
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_produced_artefact_states_that_it_posts_nothing`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_produced_artefact_states_that_it_posts_nothing PASSED [ 98%]`

### Scenario: test_open_predictions_are_visible_with_their_expected_clearing_periods
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_open_predictions_are_visible_with_their_expected_clearing_periods`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_open_predictions_are_visible_with_their_expected_clearing_periods PASSED [ 98%]`

### Scenario: test_a_missed_prediction_is_distinguishable_from_one_within_its_horizon
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_a_missed_prediction_is_distinguishable_from_one_within_its_horizon`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_a_missed_prediction_is_distinguishable_from_one_within_its_horizon PASSED [ 98%]`

### Scenario: test_the_missed_row_is_a_real_verification_result_not_a_label
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_missed_row_is_a_real_verification_result_not_a_label`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_missed_row_is_a_real_verification_result_not_a_label PASSED [ 98%]`

### Scenario: test_the_zero_open_state_names_the_period
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_zero_open_state_names_the_period`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_zero_open_state_names_the_period PASSED [ 98%]`

### Scenario: test_no_route_module_reaches_a_multipart_parser
- Input: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_no_route_module_reaches_a_multipart_parser`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_no_route_module_reaches_a_multipart_parser PASSED [ 98%]`

### Scenario: test_a_multipart_body_is_read_as_nothing_submitted_and_refused
- Input: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_a_multipart_body_is_read_as_nothing_submitted_and_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_a_multipart_body_is_read_as_nothing_submitted_and_refused PASSED [ 98%]`

### Scenario: test_the_omission_is_found_and_grounded_in_its_history
- Input: `backend/tests/test_wedge.py::test_the_omission_is_found_and_grounded_in_its_history`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_omission_is_found_and_grounded_in_its_history PASSED [ 98%]`

### Scenario: test_a_member_present_within_its_range_raises_no_omission
- Input: `backend/tests/test_wedge.py::test_a_member_present_within_its_range_raises_no_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_member_present_within_its_range_raises_no_omission PASSED [ 98%]`

### Scenario: test_a_member_present_but_far_outside_its_range_raises_no_omission
- Input: `backend/tests/test_wedge.py::test_a_member_present_but_far_outside_its_range_raises_no_omission`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_member_present_but_far_outside_its_range_raises_no_omission PASSED [ 98%]`

### Scenario: test_a_member_with_too_little_history_is_not_evaluable_and_not_reported_clear
- Input: `backend/tests/test_wedge.py::test_a_member_with_too_little_history_is_not_evaluable_and_not_reported_clear`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_member_with_too_little_history_is_not_evaluable_and_not_reported_clear PASSED [ 98%]`

### Scenario: test_the_finding_carries_a_dossier_reference_and_the_coverage_statement
- Input: `backend/tests/test_wedge.py::test_the_finding_carries_a_dossier_reference_and_the_coverage_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_finding_carries_a_dossier_reference_and_the_coverage_statement PASSED [ 99%]`

### Scenario: test_a_run_makes_zero_model_calls
- Input: `backend/tests/test_wedge.py::test_a_run_makes_zero_model_calls`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_run_makes_zero_model_calls PASSED    [ 99%]`

### Scenario: test_the_present_anomaly_detector_finds_the_outlier
- Input: `backend/tests/test_wedge.py::test_the_present_anomaly_detector_finds_the_outlier`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_present_anomaly_detector_finds_the_outlier PASSED [ 99%]`

### Scenario: test_the_anomaly_finding_states_its_threshold_and_inclusivity
- Input: `backend/tests/test_wedge.py::test_the_anomaly_finding_states_its_threshold_and_inclusivity`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_anomaly_finding_states_its_threshold_and_inclusivity PASSED [ 99%]`

### Scenario: test_the_anomaly_detector_does_not_fire_on_an_in_range_member
- Input: `backend/tests/test_wedge.py::test_the_anomaly_detector_does_not_fire_on_an_in_range_member`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_anomaly_detector_does_not_fire_on_an_in_range_member PASSED [ 99%]`

### Scenario: test_f42_reports_nothing_for_the_omitted_member
- Input: `backend/tests/test_wedge.py::test_f42_reports_nothing_for_the_omitted_member`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_f42_reports_nothing_for_the_omitted_member PASSED [ 99%]`

### Scenario: test_the_paired_comparison_is_one_artefact_naming_both_runs
- Input: `backend/tests/test_wedge.py::test_the_paired_comparison_is_one_artefact_naming_both_runs`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_paired_comparison_is_one_artefact_naming_both_runs PASSED [ 99%]`

### Scenario: test_the_comparison_is_over_an_identical_selection
- Input: `backend/tests/test_wedge.py::test_the_comparison_is_over_an_identical_selection`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_comparison_is_over_an_identical_selection PASSED [ 99%]`

### Scenario: test_a_comparison_over_different_selections_is_refused
- Input: `backend/tests/test_wedge.py::test_a_comparison_over_different_selections_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_comparison_over_different_selections_is_refused PASSED [ 99%]`

### Scenario: test_a_comparison_involving_an_incomplete_run_is_refused
- Input: `backend/tests/test_wedge.py::test_a_comparison_involving_an_incomplete_run_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_comparison_involving_an_incomplete_run_is_refused PASSED [ 99%]`

### Scenario: test_the_wedge_is_not_demonstrated_when_the_omission_is_absent_from_the_world
- Input: `backend/tests/test_wedge.py::test_the_wedge_is_not_demonstrated_when_the_omission_is_absent_from_the_world`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_wedge_is_not_demonstrated_when_the_omission_is_absent_from_the_world PASSED [ 99%]`

### Scenario: test_the_omission_detector_passes_its_declared_fixture_pair
- Input: `backend/tests/test_wedge.py::test_the_omission_detector_passes_its_declared_fixture_pair`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_omission_detector_passes_its_declared_fixture_pair PASSED [ 99%]`

### Scenario: test_the_anomaly_detector_is_silent_about_the_omitted_member_in_both_fixtures
- Input: `backend/tests/test_wedge.py::test_the_anomaly_detector_is_silent_about_the_omitted_member_in_both_fixtures`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_the_anomaly_detector_is_silent_about_the_omitted_member_in_both_fixtures PASSED [ 99%]`

### Scenario: test_a_run_with_no_resolvable_population_does_not_start
- Input: `backend/tests/test_wedge.py::test_a_run_with_no_resolvable_population_does_not_start`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_a_run_with_no_resolvable_population_does_not_start PASSED [ 99%]`

### Scenario: test_an_unavailable_dataset_makes_the_run_incomplete_with_no_conclusion
- Input: `backend/tests/test_wedge.py::test_an_unavailable_dataset_makes_the_run_incomplete_with_no_conclusion`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: ``.venv/bin/python` — pytest -v line: `backend/tests/test_wedge.py::test_an_unavailable_dataset_makes_the_run_incomplete_with_no_conclusion PASSED [100%]`
