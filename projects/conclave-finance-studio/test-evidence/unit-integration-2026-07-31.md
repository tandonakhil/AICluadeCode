# Test evidence — `unit/integration` suite

**Project:** conclave-finance-studio  
**Gate:** 8 · Test (re-run)  
**Date:** 2026-08-01  
**Commit under test:** `dev` @ **`f56ab9f`** · parent repo @ **`8939ebb`**  
**Owner:** `test-agent`  
**Blocking:** yes (no Test Policy exception is recorded for this project)  
**Status:** `EXECUTED`  
**Entry point:** `.venv/bin/python -m pytest  (testpaths: backend/tests, tests/suites)`  
**Interpreter:** `dev/.venv/bin/python` (Python 3.9)  
**Exit code:** 0  
**Scenarios: 1663 — PASS 1663, FAIL 0, skipped 0**

> This corpus was regenerated in full at `f56ab9f` and the `b1b5dde` corpus was
> deleted, not left beside it. Every entry below corresponds to a node ID
> that actually executed in this run; none is a static reading.

---

## `backend/tests/test_abstention.py`

### Scenario: there are exactly six types and they are the kbs six
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_there_are_exactly_six_types_and_they_are_the_kbs_six` executed under `dev/.venv/bin/python`
- Expected: there are exactly six types and they are the kbs six
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_there_are_exactly_six_types_and_they_are_the_kbs_six PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every type names its trigger and who computes it
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_every_type_names_its_trigger_and_who_computes_it` executed under `dev/.venv/bin/python`
- Expected: every type names its trigger and who computes it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_every_type_names_its_trigger_and_who_computes_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the type set is closed
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_type_set_is_closed` executed under `dev/.venv/bin/python`
- Expected: the type set is closed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_type_set_is_closed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention must name its gap and carry one resolving action
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstention_must_name_its_gap_and_carry_one_resolving_action` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-43. The abstention carries its AB1-AB6 type and its named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstention_must_name_its_gap_and_carry_one_resolving_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention carries no confidence score or severity
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstention_carries_no_confidence_score_or_severity` executed under `dev/.venv/bin/python`
- Expected: an abstention carries no confidence score or severity
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstention_carries_no_confidence_score_or_severity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there are four states and unknown is one of them
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_there_are_four_states_and_unknown_is_one_of_them` executed under `dev/.venv/bin/python`
- Expected: there are four states and unknown is one of them
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_there_are_four_states_and_unknown_is_one_of_them PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB1]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB1]` executed under `dev/.venv/bin/python`, parameter case `AB1`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB2]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB2]` executed under `dev/.venv/bin/python`, parameter case `AB2`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB3]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB3]` executed under `dev/.venv/bin/python`, parameter case `AB3`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB4]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB4]` executed under `dev/.venv/bin/python`, parameter case `AB4`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB4] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB5]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB5]` executed under `dev/.venv/bin/python`, parameter case `AB5`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB5] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention type ever renders as a negative finding[AB6]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB6]` executed under `dev/.venv/bin/python`, parameter case `AB6`
- Expected: All six. Not five, not "the ones we thought of".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_abstention_type_ever_renders_as_a_negative_finding[AB6] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unknown is not in the negative states and red is
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_unknown_is_not_in_the_negative_states_and_red_is` executed under `dev/.venv/bin/python`
- Expected: unknown is not in the negative states and red is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_unknown_is_not_in_the_negative_states_and_red_is PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the mapping from type to state is total and constant
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_mapping_from_type_to_state_is_total_and_constant` executed under `dev/.venv/bin/python`
- Expected: the mapping from type to state is total and constant
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_mapping_from_type_to_state_is_total_and_constant PASSED` (verbatim from the `-v` node list of this run)

### Scenario: is negative finding is computed not stored
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_is_negative_finding_is_computed_not_stored` executed under `dev/.venv/bin/python`
- Expected: is negative finding is computed not stored
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_is_negative_finding_is_computed_not_stored PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the assurance item constructor refuses a miscoloured abstention
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_assurance_item_constructor_refuses_a_miscoloured_abstention` executed under `dev/.venv/bin/python`
- Expected: the assurance item constructor refuses a miscoloured abstention
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_assurance_item_constructor_refuses_a_miscoloured_abstention PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a fifth state is refused
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_a_fifth_state_is_refused` executed under `dev/.venv/bin/python`
- Expected: a fifth state is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_a_fifth_state_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: conclusions and abstentions render through the same object
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_conclusions_and_abstentions_render_through_the_same_object` executed under `dev/.venv/bin/python`
- Expected: conclusions and abstentions render through the same object
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_conclusions_and_abstentions_render_through_the_same_object PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstention statement says could not and names the action
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_abstention_statement_says_could_not_and_names_the_action` executed under `dev/.venv/bin/python`
- Expected: the abstention statement says could not and names the action
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_abstention_statement_says_could_not_and_names_the_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no argument to a conclusion that produces unknown
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_there_is_no_argument_to_a_conclusion_that_produces_unknown` executed under `dev/.venv/bin/python`
- Expected: there is no argument to a conclusion that produces unknown
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_there_is_no_argument_to_a_conclusion_that_produces_unknown PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the quality denominator is concluded items only
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_quality_denominator_is_concluded_items_only` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's COMPUTATION clause. No figure divides concluded by
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_quality_denominator_is_concluded_items_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: abstaining more does not move precision
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_abstaining_more_does_not_move_precision` executed under `dev/.venv/bin/python`
- Expected: abstaining more does not move precision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_abstaining_more_does_not_move_precision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: abstentions are reported as a named third figure
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_abstentions_are_reported_as_a_named_third_figure` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's COMPUTATION clause, second half: the abstention count
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_abstentions_are_reported_as_a_named_third_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no function in the module divides by concluded plus abstained
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_function_in_the_module_divides_by_concluded_plus_abstained` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's COMPUTATION clause, asserted reflectively so it holds
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_function_in_the_module_divides_by_concluded_plus_abstained PASSED` (verbatim from the `-v` node list of this run)

### Scenario: rates refuses more correct than concluded
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_rates_refuses_more_correct_than_concluded` executed under `dev/.venv/bin/python`
- Expected: rates refuses more correct than concluded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_rates_refuses_more_correct_than_concluded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB1]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB1]` executed under `dev/.venv/bin/python`, parameter case `AB1`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB2]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB2]` executed under `dev/.venv/bin/python`, parameter case `AB2`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB3]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB3]` executed under `dev/.venv/bin/python`, parameter case `AB3`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB4]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB4]` executed under `dev/.venv/bin/python`, parameter case `AB4`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB4] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB5]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB5]` executed under `dev/.venv/bin/python`, parameter case `AB5`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB5] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstained item counts as covered not as a gap[AB6]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB6]` executed under `dev/.venv/bin/python`, parameter case `AB6`
- Expected: COVERS AC-F36-46. Abstaining does not reduce a run's coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstained_item_counts_as_covered_not_as_a_gap[AB6] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention costs the routing budget less than a conclusion
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_abstention_costs_the_routing_budget_less_than_a_conclusion` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-50. An abstained item consumes less routing budget than a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_abstention_costs_the_routing_budget_less_than_a_conclusion PASSED` (verbatim from the `-v` node list of this run)

### Scenario: weights that make declining as expensive as concluding are refused
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_weights_that_make_declining_as_expensive_as_concluding_are_refused` executed under `dev/.venv/bin/python`
- Expected: weights that make declining as expensive as concluding are refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_weights_that_make_declining_as_expensive_as_concluding_are_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bundles shipped weights satisfy that constraint
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_bundles_shipped_weights_satisfy_that_constraint` executed under `dev/.venv/bin/python`
- Expected: the bundles shipped weights satisfy that constraint
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_bundles_shipped_weights_satisfy_that_constraint PASSED` (verbatim from the `-v` node list of this run)

### Scenario: zero abstentions over a period is a control finding
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_zero_abstentions_over_a_period_is_a_control_finding` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-48's computation clause. A RED control finding naming the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_zero_abstentions_over_a_period_is_a_control_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: near zero is also a control finding not only exact zero
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_near_zero_is_also_a_control_finding_not_only_exact_zero` executed under `dev/.venv/bin/python`
- Expected: near zero is also a control finding not only exact zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_near_zero_is_also_a_control_finding_not_only_exact_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: above band is a usefulness finding to a different owner
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_above_band_is_a_usefulness_finding_to_a_different_owner` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-48's other tail: a usefulness finding routed to the skill
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_above_band_is_a_usefulness_finding_to_a_different_owner PASSED` (verbatim from the `-v` node list of this run)

### Scenario: in band produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_in_band_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: in band produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_in_band_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two tails route to different owners
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_the_two_tails_route_to_different_owners` executed under `dev/.venv/bin/python`
- Expected: the two tails route to different owners
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_the_two_tails_route_to_different_owners PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a band over nothing is not a measurement
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_a_band_over_nothing_is_not_a_measurement` executed under `dev/.venv/bin/python`
- Expected: a band over nothing is not a measurement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_a_band_over_nothing_is_not_a_measurement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an inverted band is refused
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_an_inverted_band_is_refused` executed under `dev/.venv/bin/python`
- Expected: an inverted band is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_an_inverted_band_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[be_more_decisive]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[be_more_decisive]` executed under `dev/.venv/bin/python`, parameter case `be_more_decisive`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[be_more_decisive] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[confidence_threshold]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_threshold]` executed under `dev/.venv/bin/python`, parameter case `confidence_threshold`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_threshold] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[confidence_slider]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_slider]` executed under `dev/.venv/bin/python`, parameter case `confidence_slider`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[confidence_slider] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[abstention_rate_target]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[abstention_rate_target]` executed under `dev/.venv/bin/python`, parameter case `abstention_rate_target`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[abstention_rate_target] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[min_confidence]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[min_confidence]` executed under `dev/.venv/bin/python`, parameter case `min_confidence`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[min_confidence] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[suppress_abstentions]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[suppress_abstentions]` executed under `dev/.venv/bin/python`, parameter case `suppress_abstentions`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[suppress_abstentions] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no user facing setting may change abstention behaviour[auto_conclude_when_ambiguous]
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[auto_conclude_when_ambiguous]` executed under `dev/.venv/bin/python`, parameter case `auto_conclude_when_ambiguous`
- Expected: COVERS AC-F36-49. No toggle, slider, 'be more decisive' setting or confidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_no_user_facing_setting_may_change_abstention_behaviour[auto_conclude_when_ambiguous] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ordinary settings pass
- Status: EXECUTED
- Input: `backend/tests/test_abstention.py::test_ordinary_settings_pass` executed under `dev/.venv/bin/python`
- Expected: ordinary settings pass
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_abstention.py::test_ordinary_settings_pass PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_audit_domain_and_export.py`

### Scenario: each of the three acts is carried with actor and target[delete_attempt]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[delete_attempt]` executed under `dev/.venv/bin/python`, parameter case `delete_attempt`
- Expected: each of the three acts is carried with actor and target
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[delete_attempt] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each of the three acts is carried with actor and target[retention_shortening_attempt]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[retention_shortening_attempt]` executed under `dev/.venv/bin/python`, parameter case `retention_shortening_attempt`
- Expected: each of the three acts is carried with actor and target
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[retention_shortening_attempt] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each of the three acts is carried with actor and target[lock_configuration_change]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[lock_configuration_change]` executed under `dev/.venv/bin/python`, parameter case `lock_configuration_change`
- Expected: each of the three acts is carried with actor and target
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_each_of_the_three_acts_is_carried_with_actor_and_target[lock_configuration_change] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the shippable set is the three acts the criterion names
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_shippable_set_is_the_three_acts_the_criterion_names` executed under `dev/.venv/bin/python`
- Expected: The guard: a `parametrize` over an emptied tuple collects zero tests.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_shippable_set_is_the_three_acts_the_criterion_names PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an event kind outside the set is refused
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_an_event_kind_outside_the_set_is_refused` executed under `dev/.venv/bin/python`
- Expected: an event kind outside the set is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_an_event_kind_outside_the_set_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the destination has no method that removes or changes a record
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_destination_has_no_method_that_removes_or_changes_a_record` executed under `dev/.venv/bin/python`
- Expected: the destination has no method that removes or changes a record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_destination_has_no_method_that_removes_or_changes_a_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a record cannot be deleted or updated even by raw sql
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_record_cannot_be_deleted_or_updated_even_by_raw_sql` executed under `dev/.venv/bin/python`
- Expected: a record cannot be deleted or updated even by raw sql
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_record_cannot_be_deleted_or_updated_even_by_raw_sql PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an alert is raised for every shipped record
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_an_alert_is_raised_for_every_shipped_record` executed under `dev/.venv/bin/python`
- Expected: an alert is raised for every shipped record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_an_alert_is_raised_for_every_shipped_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a shipping failure RAISES rather than returning
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_shipping_failure_RAISES_rather_than_returning` executed under `dev/.venv/bin/python`
- Expected: A method that recorded a finding and returned normally would let every
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_shipping_failure_RAISES_rather_than_returning PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a shipping failure produces a finding naming the interval
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_shipping_failure_produces_a_finding_naming_the_interval` executed under `dev/.venv/bin/python`
- Expected: a shipping failure produces a finding naming the interval
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_shipping_failure_produces_a_finding_naming_the_interval PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the status is never satisfactory while a finding stands
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_status_is_never_satisfactory_while_a_finding_stands` executed under `dev/.venv/bin/python`
- Expected: the status is never satisfactory while a finding stands
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_status_is_never_satisfactory_while_a_finding_stands PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the status is derived and not a settable flag
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_status_is_derived_and_not_a_settable_flag` executed under `dev/.venv/bin/python`
- Expected: There is no code path that reports a good status and leaves a finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_status_is_derived_and_not_a_settable_flag PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failure also emits a control event
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_failure_also_emits_a_control_event` executed under `dev/.venv/bin/python`
- Expected: a failure also emits a control event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_failure_also_emits_a_control_event PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the signing key cannot be resolved and the attempt is recorded
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_signing_key_cannot_be_resolved_and_the_attempt_is_recorded` executed under `dev/.venv/bin/python`
- Expected: the signing key cannot be resolved and the attempt is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_signing_key_cannot_be_resolved_and_the_attempt_is_recorded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no success path on the key resolver
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_there_is_no_success_path_on_the_key_resolver` executed under `dev/.venv/bin/python`
- Expected: A function whose only exit is a raise cannot be made to return a key by
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_there_is_no_success_path_on_the_key_resolver PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stub signer cannot produce a valid signature
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_stub_signer_cannot_produce_a_valid_signature` executed under `dev/.venv/bin/python`
- Expected: the stub signer cannot produce a valid signature
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_stub_signer_cannot_produce_a_valid_signature PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a whole export carries every reconstruction field
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_whole_export_carries_every_reconstruction_field` executed under `dev/.venv/bin/python`
- Expected: a whole export carries every reconstruction field
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_whole_export_carries_every_reconstruction_field PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing reconstruction field fails the export naming it[dataset_version]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[dataset_version]` executed under `dev/.venv/bin/python`, parameter case `dataset_version`
- Expected: a missing reconstruction field fails the export naming it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[dataset_version] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing reconstruction field fails the export naming it[guardrail_bundle]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[guardrail_bundle]` executed under `dev/.venv/bin/python`, parameter case `guardrail_bundle`
- Expected: a missing reconstruction field fails the export naming it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[guardrail_bundle] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing reconstruction field fails the export naming it[coverage]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[coverage]` executed under `dev/.venv/bin/python`, parameter case `coverage`
- Expected: a missing reconstruction field fails the export naming it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[coverage] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing reconstruction field fails the export naming it[approver_view]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[approver_view]` executed under `dev/.venv/bin/python`, parameter case `approver_view`
- Expected: a missing reconstruction field fails the export naming it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[approver_view] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing reconstruction field fails the export naming it[approved_by]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[approved_by]` executed under `dev/.venv/bin/python`, parameter case `approved_by`
- Expected: a missing reconstruction field fails the export naming it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_missing_reconstruction_field_fails_the_export_naming_it[approved_by] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the reconstruction fields are the five the criterion names
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_reconstruction_fields_are_the_five_the_criterion_names` executed under `dev/.venv/bin/python`
- Expected: The guard on the group above.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_reconstruction_fields_are_the_five_the_criterion_names PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<script>x</script>-a script element]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<script>x</script>-a script element]` executed under `dev/.venv/bin/python`, parameter case `<script>x</script>-a script element`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<script>x</script>-a script element] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<a href="javascript:x">-a javascript: URL]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<a href="javascript:x">-a javascript: URL]` executed under `dev/.venv/bin/python`, parameter case `<a href="javascript:x">-a javascript: URL`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<a href="javascript:x">-a javascript: URL] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<iframe src=x>-an iframe]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<iframe src=x>-an iframe]` executed under `dev/.venv/bin/python`, parameter case `<iframe src=x>-an iframe`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<iframe src=x>-an iframe] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<link rel="stylesheet">-an external stylesheet link]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<link rel="stylesheet">-an external stylesheet link]` executed under `dev/.venv/bin/python`, parameter case `<link rel="stylesheet">-an external stylesheet link`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<link rel="stylesheet">-an external stylesheet link] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<img src=x>-an image reference]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<img src=x>-an image reference]` executed under `dev/.venv/bin/python`, parameter case `<img src=x>-an image reference`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<img src=x>-an image reference] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[@import url(x)-a CSS import]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[@import url(x)-a CSS import]` executed under `dev/.venv/bin/python`, parameter case `@import url(x)-a CSS import`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[@import url(x)-a CSS import] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<a href="https://example.com">-an absolute HTTPS reference]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<a href="https://example.com">-an absolute HTTPS reference]` executed under `dev/.venv/bin/python`, parameter case `<a href="https://example.com">-an absolute HTTPS reference`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<a href="https://example.com">-an absolute HTTPS reference] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: active content of any kind means no export is produced[<div onclick="x">-an inline event handler attribute]
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<div onclick="x">-an inline event handler attribute]` executed under `dev/.venv/bin/python`, parameter case `<div onclick="x">-an inline event handler attribute`
- Expected: active content of any kind means no export is produced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_active_content_of_any_kind_means_no_export_is_produced[<div onclick="x">-an inline event handler attribute] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier with no retained view fails naming the dossier
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_dossier_with_no_retained_view_fails_naming_the_dossier` executed under `dev/.venv/bin/python`
- Expected: a dossier with no retained view fails naming the dossier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_dossier_with_no_retained_view_fails_naming_the_dossier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a render failure names the point of failure and produces nothing
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_render_failure_names_the_point_of_failure_and_produces_nothing` executed under `dev/.venv/bin/python`
- Expected: a render failure names the point of failure and produces nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_render_failure_names_the_point_of_failure_and_produces_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty period produces a whole export that STATES the absence
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_an_empty_period_produces_a_whole_export_that_STATES_the_absence` executed under `dev/.venv/bin/python`
- Expected: an empty period produces a whole export that STATES the absence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_an_empty_period_produces_a_whole_export_that_STATES_the_absence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non empty export also carries a statement
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_non_empty_export_also_carries_a_statement` executed under `dev/.venv/bin/python`
- Expected: A statement that appears only in the empty case is one a reader learns
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_non_empty_export_also_carries_a_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export does not claim re execution
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_export_does_not_claim_re_execution` executed under `dev/.venv/bin/python`
- Expected: the export does not claim re execution
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_export_does_not_claim_re_execution PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export json parses with no dependency on this codebase
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_the_export_json_parses_with_no_dependency_on_this_codebase` executed under `dev/.venv/bin/python`
- Expected: the export json parses with no dependency on this codebase
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_the_export_json_parses_with_no_dependency_on_this_codebase PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier with no id cannot be named and fails the export
- Status: EXECUTED
- Input: `backend/tests/test_audit_domain_and_export.py::test_a_dossier_with_no_id_cannot_be_named_and_fails_the_export` executed under `dev/.venv/bin/python`
- Expected: a dossier with no id cannot be named and fails the export
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_audit_domain_and_export.py::test_a_dossier_with_no_id_cannot_be_named_and_fails_the_export PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_authorship_closure.py`

### Scenario: a distinct human approver is accepted and records its decision
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_a_distinct_human_approver_is_accepted_and_records_its_decision` executed under `dev/.venv/bin/python`
- Expected: a distinct human approver is accepted and records its decision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_a_distinct_human_approver_is_accepted_and_records_its_decision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the author may not approve its own item
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_the_author_may_not_approve_its_own_item` executed under `dev/.venv/bin/python`
- Expected: the author may not approve its own item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_the_author_may_not_approve_its_own_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the invoker may not approve
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_the_invoker_may_not_approve` executed under `dev/.venv/bin/python`
- Expected: the invoker may not approve
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_the_invoker_may_not_approve PASSED` (verbatim from the `-v` node list of this run)

### Scenario: author and invoker may not be the same identity
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_author_and_invoker_may_not_be_the_same_identity` executed under `dev/.venv/bin/python`
- Expected: author and invoker may not be the same identity
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_author_and_invoker_may_not_be_the_same_identity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an ineligible approval by direct api produces the same denial
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_an_ineligible_approval_by_direct_api_produces_the_same_denial` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-25`. The front end and a direct call reach the same function, so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_an_ineligible_approval_by_direct_api_produces_the_same_denial PASSED` (verbatim from the `-v` node list of this run)

### Scenario: eligibility is computed from authorship not from a role list
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_eligibility_is_computed_from_authorship_not_from_a_role_list` executed under `dev/.venv/bin/python`
- Expected: eligibility is computed from authorship not from a role list
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_eligibility_is_computed_from_authorship_not_from_a_role_list PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an item with no eligible approver reports an empty set
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_an_item_with_no_eligible_approver_reports_an_empty_set` executed under `dev/.venv/bin/python`
- Expected: `AC-F41-21`'s data half. An empty set is an answer; it must not be
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_an_item_with_no_eligible_approver_reports_an_empty_set PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an agent principal is denied the approve capability before any rule
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_an_agent_principal_is_denied_the_approve_capability_before_any_rule` executed under `dev/.venv/bin/python`
- Expected: an agent principal is denied the approve capability before any rule
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_an_agent_principal_is_denied_the_approve_capability_before_any_rule PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an agent approval is unrepresentable even by raw sql
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_an_agent_approval_is_unrepresentable_even_by_raw_sql` executed under `dev/.venv/bin/python`
- Expected: THE test this whole layer exists for.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_an_agent_approval_is_unrepresentable_even_by_raw_sql PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the kind column admits only human
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_the_kind_column_admits_only_human` executed under `dev/.venv/bin/python`
- Expected: the kind column admits only human
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_the_kind_column_admits_only_human PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a service principal cannot occupy the approver field
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_a_service_principal_cannot_occupy_the_approver_field` executed under `dev/.venv/bin/python`
- Expected: a service principal cannot occupy the approver field
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_a_service_principal_cannot_occupy_the_approver_field PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every collapsed pair is refused by the schema[p1-p2-p1]
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p1]` executed under `dev/.venv/bin/python`, parameter case `p1-p2-p1`
- Expected: The three CHECK constraints, exercised individually and by raw SQL.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every collapsed pair is refused by the schema[p1-p2-p2]
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p2]` executed under `dev/.venv/bin/python`, parameter case `p1-p2-p2`
- Expected: The three CHECK constraints, exercised individually and by raw SQL.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p2-p2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every collapsed pair is refused by the schema[p1-p1-p2]
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p1-p2]` executed under `dev/.venv/bin/python`, parameter case `p1-p1-p2`
- Expected: The three CHECK constraints, exercised individually and by raw SQL.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_every_collapsed_pair_is_refused_by_the_schema[p1-p1-p2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approval cannot exist without a decision
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_an_approval_cannot_exist_without_a_decision` executed under `dev/.venv/bin/python`
- Expected: an approval cannot exist without a decision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_an_approval_cannot_exist_without_a_decision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one approval per item
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_one_approval_per_item` executed under `dev/.venv/bin/python`
- Expected: one approval per item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_one_approval_per_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a platform admin cannot approve a finance action
- Status: EXECUTED
- Input: `backend/tests/test_authorship_closure.py::test_a_platform_admin_cannot_approve_a_finance_action` executed under `dev/.venv/bin/python`
- Expected: a platform admin cannot approve a finance action
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_authorship_closure.py::test_a_platform_admin_cannot_approve_a_finance_action PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_blast_radius.py`

### Scenario: the run cap stops production and records the trip
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_run_cap_stops_production_and_records_the_trip` executed under `dev/.venv/bin/python`
- Expected: the run cap stops production and records the trip
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_run_cap_stops_production_and_records_the_trip PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denied proposal does not increment the counter
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_a_denied_proposal_does_not_increment_the_counter` executed under `dev/.venv/bin/python`
- Expected: Denials do not increment; allows do. Otherwise a run of denials would
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_a_denied_proposal_does_not_increment_the_counter PASSED` (verbatim from the `-v` node list of this run)

### Scenario: individually compliant proposals crossing the period cap are denied
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_individually_compliant_proposals_crossing_the_period_cap_are_denied` executed under `dev/.venv/bin/python`
- Expected: Each proposal is below the 25,000 rule ceiling; their cumulative value
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_individually_compliant_proposals_crossing_the_period_cap_are_denied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the period cap is per principal
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_period_cap_is_per_principal` executed under `dev/.venv/bin/python`
- Expected: the period cap is per principal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_period_cap_is_per_principal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a proposal exceeding the balance proportion is denied with all three numbers
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_a_proposal_exceeding_the_balance_proportion_is_denied_with_all_three_numbers` executed under `dev/.venv/bin/python`
- Expected: a proposal exceeding the balance proportion is denied with all three numbers
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_a_proposal_exceeding_the_balance_proportion_is_denied_with_all_three_numbers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a proposal exactly at the proportion cap is allowed
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_a_proposal_exactly_at_the_proportion_cap_is_allowed` executed under `dev/.venv/bin/python`
- Expected: a proposal exactly at the proportion cap is allowed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_a_proposal_exactly_at_the_proportion_cap_is_allowed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a third consecutive same account proposal escalates and names all three
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_a_third_consecutive_same_account_proposal_escalates_and_names_all_three` executed under `dev/.venv/bin/python`
- Expected: a third consecutive same account proposal escalates and names all three
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_a_third_consecutive_same_account_proposal_escalates_and_names_all_three PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two consecutive periods do not escalate
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_two_consecutive_periods_do_not_escalate` executed under `dev/.venv/bin/python`
- Expected: two consecutive periods do not escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_two_consecutive_periods_do_not_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a gap in the sequence breaks the streak
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_a_gap_in_the_sequence_breaks_the_streak` executed under `dev/.venv/bin/python`
- Expected: The cap is CONSECUTIVE periods. A skipped period is not a streak.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_a_gap_in_the_sequence_breaks_the_streak PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the streak is per period stateful not per invocation
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_streak_is_per_period_stateful_not_per_invocation` executed under `dev/.venv/bin/python`
- Expected: RT-08's cap-evasion path: a retry loop producing N proposals per call
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_streak_is_per_period_stateful_not_per_invocation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the direction is part of the key
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_direction_is_part_of_the_key` executed under `dev/.venv/bin/python`
- Expected: the direction is part of the key
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_direction_is_part_of_the_key PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the cap holds under real concurrency
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_cap_holds_under_real_concurrency` executed under `dev/.venv/bin/python`
- Expected: THE test that decides whether the word "cap" is honest.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_cap_holds_under_real_concurrency PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same workload without the transaction overruns the cap
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_same_workload_without_the_transaction_overruns_the_cap` executed under `dev/.venv/bin/python`
- Expected: The control experiment, so the passing test above is known to measure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_same_workload_without_the_transaction_overruns_the_cap PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the decision and the counter commit together
- Status: EXECUTED
- Input: `backend/tests/test_blast_radius.py::test_the_decision_and_the_counter_commit_together` executed under `dev/.venv/bin/python`
- Expected: If the decision insert fails, the counter must not have moved.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_blast_radius.py::test_the_decision_and_the_counter_commit_together PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_boundary_primitives.py`

### Scenario: a pair that nets to zero produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_pair_that_nets_to_zero_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a pair that nets to zero produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_pair_that_nets_to_zero_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an imbalanced pair names both entities the pair and the amount
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_an_imbalanced_pair_names_both_entities_the_pair_and_the_amount` executed under `dev/.venv/bin/python`
- Expected: `AC-F28-02` in full. Naming only the short side is the common shape of
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_an_imbalanced_pair_names_both_entities_the_pair_and_the_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the direction names the other entity when the other side is long
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_direction_names_the_other_entity_when_the_other_side_is_long` executed under `dev/.venv/bin/python`
- Expected: the direction names the other entity when the other side is long
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_direction_names_the_other_entity_when_the_other_side_is_long PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a one sided pair is not reported as an imbalance of the whole amount
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_one_sided_pair_is_not_reported_as_an_imbalance_of_the_whole_amount` executed under `dev/.venv/bin/python`
- Expected: Treating the absent side as zero would report 1,043,900 as the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_one_sided_pair_is_not_reported_as_an_imbalance_of_the_whole_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the primitive claims no cause
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_primitive_claims_no_cause` executed under `dev/.venv/bin/python`
- Expected: `DOMAIN_KB` §10 P8 bounds this: the imbalance is emitted, the cause is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_primitive_claims_no_cause PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared pair with no row is uncovered and named
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_declared_pair_with_no_row_is_uncovered_and_named` executed under `dev/.venv/bin/python`
- Expected: a declared pair with no row is uncovered and named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_declared_pair_with_no_row_is_uncovered_and_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the pair tolerance boundary is inclusive
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_pair_tolerance_boundary_is_inclusive` executed under `dev/.venv/bin/python`
- Expected: the pair tolerance boundary is inclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_pair_tolerance_boundary_is_inclusive PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a continuous account produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_continuous_account_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a continuous account produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_continuous_account_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a break names the account entity both periods and the amount
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_break_names_the_account_entity_both_periods_and_the_amount` executed under `dev/.venv/bin/python`
- Expected: a break names the account entity both periods and the amount
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_break_names_the_account_entity_both_periods_and_the_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the first in scope period is not evaluable rather than broken
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_first_in_scope_period_is_not_evaluable_rather_than_broken` executed under `dev/.venv/bin/python`
- Expected: THE BRANCH THAT MATTERS.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_first_in_scope_period_is_not_evaluable_rather_than_broken PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an incomplete rollforward row is not evaluable
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_an_incomplete_rollforward_row_is_not_evaluable` executed under `dev/.venv/bin/python`
- Expected: an incomplete rollforward row is not evaluable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_an_incomplete_rollforward_row_is_not_evaluable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the identity is checked as well as the opening balance
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_identity_is_checked_as_well_as_the_opening_balance` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §7.3 states closing(p-1) + movements = closing(p);
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_identity_is_checked_as_well_as_the_opening_balance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared account with no rollforward row is uncovered
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_declared_account_with_no_rollforward_row_is_uncovered` executed under `dev/.venv/bin/python`
- Expected: a declared account with no rollforward row is uncovered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_declared_account_with_no_rollforward_row_is_uncovered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a correctly applied revaluation produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_correctly_applied_revaluation_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a correctly applied revaluation produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_correctly_applied_revaluation_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a doubled revaluation names the multiple and the duplicated amount
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_doubled_revaluation_names_the_multiple_and_the_duplicated_amount` executed under `dev/.venv/bin/python`
- Expected: `AC-F28-04` asks for the DUPLICATED amount, not "a difference".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_doubled_revaluation_names_the_multiple_and_the_duplicated_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non integer mismatch reports the difference and claims no multiple
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_non_integer_mismatch_reports_the_difference_and_claims_no_multiple` executed under `dev/.venv/bin/python`
- Expected: a non integer mismatch reports the difference and claims no multiple
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_non_integer_mismatch_reports_the_difference_and_claims_no_multiple PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero from rate is not evaluable rather than a division error
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_zero_from_rate_is_not_evaluable_rather_than_a_division_error` executed under `dev/.venv/bin/python`
- Expected: a zero from rate is not evaluable rather than a division error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_zero_from_rate_is_not_evaluable_rather_than_a_division_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing input is not evaluable rather than a silent zero
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_missing_input_is_not_evaluable_rather_than_a_silent_zero` executed under `dev/.venv/bin/python`
- Expected: a missing input is not evaluable rather than a silent zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_missing_input_is_not_evaluable_rather_than_a_silent_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rounding tolerance absorbs a cent but not a duplicate
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_rounding_tolerance_absorbs_a_cent_but_not_a_duplicate` executed under `dev/.venv/bin/python`
- Expected: the rounding tolerance absorbs a cent but not a duplicate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_rounding_tolerance_absorbs_a_cent_but_not_a_duplicate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a formula outside the closed registry raises rather than skipping
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_formula_outside_the_closed_registry_raises_rather_than_skipping` executed under `dev/.venv/bin/python`
- Expected: A `formula` is a NAME resolved against a registry, never an expression.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_formula_outside_the_closed_registry_raises_rather_than_skipping PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no eval in the recompute module
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_there_is_no_eval_in_the_recompute_module` executed under `dev/.venv/bin/python`
- Expected: there is no eval in the recompute module
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_there_is_no_eval_in_the_recompute_module PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a residual within its threshold produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_residual_within_its_threshold_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a residual within its threshold produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_residual_within_its_threshold_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a breach states the residual and the threshold in force
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_breach_states_the_residual_and_the_threshold_in_force` executed under `dev/.venv/bin/python`
- Expected: a breach states the residual and the threshold in force
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_breach_states_the_residual_and_the_threshold_in_force PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold comes from the data not from a parameter
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_threshold_comes_from_the_data_not_from_a_parameter` executed under `dev/.venv/bin/python`
- Expected: `AC-F28-05`: "the threshold in force". In force is a property of the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_threshold_comes_from_the_data_not_from_a_parameter PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a negative residual is compared on its magnitude
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_a_negative_residual_is_compared_on_its_magnitude` executed under `dev/.venv/bin/python`
- Expected: a negative residual is compared on its magnitude
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_a_negative_residual_is_compared_on_its_magnitude PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold boundary is inclusive
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_threshold_boundary_is_inclusive` executed under `dev/.venv/bin/python`
- Expected: the threshold boundary is inclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_threshold_boundary_is_inclusive PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an account with no policy threshold is not evaluable
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_an_account_with_no_policy_threshold_is_not_evaluable` executed under `dev/.venv/bin/python`
- Expected: Not "within threshold". There is no threshold to be within, and
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_an_account_with_no_policy_threshold_is_not_evaluable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the scope statement is on a finding
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_finding` executed under `dev/.venv/bin/python`
- Expected: the scope statement is on a finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the scope statement is on a run that found nothing too
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_run_that_found_nothing_too` executed under `dev/.venv/bin/python`
- Expected: `AC-F28-09` says "a result OF ANY KIND", and a result that found
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_the_scope_statement_is_on_a_run_that_found_nothing_too PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two offsetting items net within threshold and are not detected
- Status: EXECUTED
- Input: `backend/tests/test_boundary_primitives.py::test_two_offsetting_items_net_within_threshold_and_are_not_detected` executed under `dev/.venv/bin/python`
- Expected: The limitation, executable rather than documentary.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_boundary_primitives.py::test_two_offsetting_items_net_within_threshold_and_are_not_detected PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_broker_action_path.py`

### Scenario: an action absent from the allowlist is denied without any prohibition
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_action_absent_from_the_allowlist_is_denied_without_any_prohibition` executed under `dev/.venv/bin/python`
- Expected: an action absent from the allowlist is denied without any prohibition
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_action_absent_from_the_allowlist_is_denied_without_any_prohibition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the allowlist is intersected with the skill definition
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_allowlist_is_intersected_with_the_skill_definition` executed under `dev/.venv/bin/python`
- Expected: RAI-ARCH-8 / `AC-F36-42`: authorisation is computed against the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_allowlist_is_intersected_with_the_skill_definition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: deny by default runs before rule evaluation
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_deny_by_default_runs_before_rule_evaluation` executed under `dev/.venv/bin/python`
- Expected: The FSM path is the evidence: CAPABILITY_CHECKED is never reached.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_deny_by_default_runs_before_rule_evaluation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an action record cannot exist without its decision
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_action_record_cannot_exist_without_its_decision` executed under `dev/.venv/bin/python`
- Expected: an action record cannot exist without its decision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_action_record_cannot_exist_without_its_decision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an action record with no decision is rejected by the database
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_action_record_with_no_decision_is_rejected_by_the_database` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-02` says such a record "does not exist". A foreign key is the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_action_record_with_no_decision_is_rejected_by_the_database PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denied decision has no action record
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_denied_decision_has_no_action_record` executed under `dev/.venv/bin/python`
- Expected: a denied decision has no action record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_denied_decision_has_no_action_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the log carries one record per attempted action and no non events
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_log_carries_one_record_per_attempted_action_and_no_non_events` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-06`, and the trap `solution-architect` named for this module.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_log_carries_one_record_per_attempted_action_and_no_non_events PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the boundary behaves as the declared inclusivity says
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_boundary_behaves_as_the_declared_inclusivity_says` executed under `dev/.venv/bin/python`
- Expected: the boundary behaves as the declared inclusivity says
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_boundary_behaves_as_the_declared_inclusivity_says PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a shadow rule does not block and names itself
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_shadow_rule_does_not_block_and_names_itself` executed under `dev/.venv/bin/python`
- Expected: a shadow rule does not block and names itself
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_shadow_rule_does_not_block_and_names_itself PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unresolvable bundle denies every action and names it
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_unresolvable_bundle_denies_every_action_and_names_it` executed under `dev/.venv/bin/python`
- Expected: an unresolvable bundle denies every action and names it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_unresolvable_bundle_denies_every_action_and_names_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no cached bundle fallback
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_there_is_no_cached_bundle_fallback` executed under `dev/.venv/bin/python`
- Expected: A cached-bundle fallback is a silent policy downgrade, which is worse
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_there_is_no_cached_bundle_fallback PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a rule that cannot be evaluated denies
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_rule_that_cannot_be_evaluated_denies` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-27`'s action-side twin. A reclass with no `resolution_type`
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_rule_that_cannot_be_evaluated_denies PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an agent principal cannot be authorised to approve
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_agent_principal_cannot_be_authorised_to_approve` executed under `dev/.venv/bin/python`
- Expected: The FIRST layer stops it: no agent principal holds `approve.proposal`,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_agent_principal_cannot_be_authorised_to_approve PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the human act rule is evidenced even though the set test gets there first
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_human_act_rule_is_evidenced_even_though_the_set_test_gets_there_first` executed under `dev/.venv/bin/python`
- Expected: A rule that can never fire in production is still a rule that must be
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_human_act_rule_is_evidenced_even_though_the_set_test_gets_there_first PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a human principal may approve
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_human_principal_may_approve` executed under `dev/.venv/bin/python`
- Expected: a human principal may approve
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_human_principal_may_approve PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approval with no authorship context is unevaluable and denies
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_approval_with_no_authorship_context_is_unevaluable_and_denies` executed under `dev/.venv/bin/python`
- Expected: Stamped, so the denial is the RULE's and not the stamp check's.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_approval_with_no_authorship_context_is_unevaluable_and_denies PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override requires two distinct human authorisers
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_override_requires_two_distinct_human_authorisers` executed under `dev/.venv/bin/python`
- Expected: an override requires two distinct human authorisers
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_override_requires_two_distinct_human_authorisers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a self authorised override is rejected
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_self_authorised_override_is_rejected` executed under `dev/.venv/bin/python`
- Expected: a self authorised override is rejected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_self_authorised_override_is_rejected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same identity cannot be both authorisers
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_same_identity_cannot_be_both_authorisers` executed under `dev/.venv/bin/python`
- Expected: the same identity cannot be both authorisers
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_same_identity_cannot_be_both_authorisers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override authorised by the agents own author is rejected
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_override_authorised_by_the_agents_own_author_is_rejected` executed under `dev/.venv/bin/python`
- Expected: an override authorised by the agents own author is rejected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_override_authorised_by_the_agents_own_author_is_rejected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an agent cannot be an override authoriser
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_agent_cannot_be_an_override_authoriser` executed under `dev/.venv/bin/python`
- Expected: The composite foreign key onto (principal_id, 'human') is the control.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_agent_cannot_be_an_override_authoriser PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reason code outside the closed list is rejected
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_reason_code_outside_the_closed_list_is_rejected` executed under `dev/.venv/bin/python`
- Expected: a reason code outside the closed list is rejected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_reason_code_outside_the_closed_list_is_rejected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a standing scope is unrepresentable[kwargs0]
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs0]` executed under `dev/.venv/bin/python`, parameter case `kwargs0`
- Expected: a standing scope is unrepresentable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a standing scope is unrepresentable[kwargs1]
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs1]` executed under `dev/.venv/bin/python`, parameter case `kwargs1`
- Expected: a standing scope is unrepresentable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_standing_scope_is_unrepresentable[kwargs1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an open ended expiry has no column to live in
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_open_ended_expiry_has_no_column_to_live_in` executed under `dev/.venv/bin/python`
- Expected: an open ended expiry has no column to live in
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_open_ended_expiry_has_no_column_to_live_in PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override applies to exactly one action
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_override_applies_to_exactly_one_action` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-07`: a second attempt at the same action requires a NEW
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_override_applies_to_exactly_one_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override belonging to another requester is refused
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_override_belonging_to_another_requester_is_refused` executed under `dev/.venv/bin/python`
- Expected: an override belonging to another requester is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_override_belonging_to_another_requester_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero override period renders an explicit zero with its denominator
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_a_zero_override_period_renders_an_explicit_zero_with_its_denominator` executed under `dev/.venv/bin/python`
- Expected: a zero override period renders an explicit zero with its denominator
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_a_zero_override_period_renders_an_explicit_zero_with_its_denominator PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an exercised override is visible in the rate
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_an_exercised_override_is_visible_in_the_rate` executed under `dev/.venv/bin/python`
- Expected: an exercised override is visible in the rate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_an_exercised_override_is_visible_in_the_rate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every path through the machine terminates
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_every_path_through_the_machine_terminates` executed under `dev/.venv/bin/python`
- Expected: every path through the machine terminates
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_every_path_through_the_machine_terminates PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the machine refuses a transition it does not have
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_the_machine_refuses_a_transition_it_does_not_have` executed under `dev/.venv/bin/python`
- Expected: the machine refuses a transition it does not have
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_the_machine_refuses_a_transition_it_does_not_have PASSED` (verbatim from the `-v` node list of this run)

### Scenario: capability check is not skippable
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_capability_check_is_not_skippable` executed under `dev/.venv/bin/python`
- Expected: A ReAct-style loop would let the agent author "go straight to RULES".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_capability_check_is_not_skippable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no second authorisation path exists
- Status: EXECUTED
- Input: `backend/tests/test_broker_action_path.py::test_no_second_authorisation_path_exists` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-03`: the same request through a different door is the same code.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_action_path.py::test_no_second_authorisation_path_exists PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_broker_bundle.py`

### Scenario: the committed bundle compiles and is hash addressed
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_the_committed_bundle_compiles_and_is_hash_addressed` executed under `dev/.venv/bin/python`
- Expected: the committed bundle compiles and is hash addressed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_the_committed_bundle_compiles_and_is_hash_addressed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: compilation is deterministic
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_compilation_is_deterministic` executed under `dev/.venv/bin/python`
- Expected: compilation is deterministic
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_compilation_is_deterministic PASSED` (verbatim from the `-v` node list of this run)

### Scenario: editing a rule produces a different hash
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_editing_a_rule_produces_a_different_hash` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-15`: an edited bundle has a different hash.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_editing_a_rule_produces_a_different_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the document handed out is a copy not a write path
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_the_document_handed_out_is_a_copy_not_a_write_path` executed under `dev/.venv/bin/python`
- Expected: the document handed out is a copy not a write path
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_the_document_handed_out_is_a_copy_not_a_write_path PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing cap fails the build[max_proposals_per_run]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_proposals_per_run]` executed under `dev/.venv/bin/python`, parameter case `max_proposals_per_run`
- Expected: a missing cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_proposals_per_run] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing cap fails the build[max_aggregate_value_per_agent_period]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_aggregate_value_per_agent_period]` executed under `dev/.venv/bin/python`, parameter case `max_aggregate_value_per_agent_period`
- Expected: a missing cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_aggregate_value_per_agent_period] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing cap fails the build[max_consecutive_same_account_periods]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_consecutive_same_account_periods]` executed under `dev/.venv/bin/python`, parameter case `max_consecutive_same_account_periods`
- Expected: a missing cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_consecutive_same_account_periods] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing cap fails the build[max_footprint_pct_of_account_balance]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_footprint_pct_of_account_balance]` executed under `dev/.venv/bin/python`, parameter case `max_footprint_pct_of_account_balance`
- Expected: a missing cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_footprint_pct_of_account_balance] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing cap fails the build[max_lines_per_export_batch]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_lines_per_export_batch]` executed under `dev/.venv/bin/python`, parameter case `max_lines_per_export_batch`
- Expected: a missing cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_missing_cap_fails_the_build[max_lines_per_export_batch] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a null cap fails the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_null_cap_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a null cap fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_null_cap_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cap edited toward disabled fails the build[unbounded]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[unbounded]` executed under `dev/.venv/bin/python`, parameter case `unbounded`
- Expected: a cap edited toward disabled fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[unbounded] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cap edited toward disabled fails the build[none]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[none]` executed under `dev/.venv/bin/python`, parameter case `none`
- Expected: a cap edited toward disabled fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[none] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cap edited toward disabled fails the build[off]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[off]` executed under `dev/.venv/bin/python`, parameter case `off`
- Expected: a cap edited toward disabled fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[off] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cap edited toward disabled fails the build[disabled]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[disabled]` executed under `dev/.venv/bin/python`, parameter case `disabled`
- Expected: a cap edited toward disabled fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_cap_edited_toward_disabled_fails_the_build[disabled] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non positive cap is not a bound[0]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[0]` executed under `dev/.venv/bin/python`, parameter case `0`
- Expected: a non positive cap is not a bound
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non positive cap is not a bound[-1]
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[-1]` executed under `dev/.venv/bin/python`, parameter case `-1`
- Expected: a non positive cap is not a bound
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_non_positive_cap_is_not_a_bound[-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown cap name fails rather than being ignored
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_an_unknown_cap_name_fails_rather_than_being_ignored` executed under `dev/.venv/bin/python`
- Expected: A cap the broker never reads is a cap nobody enforces, and it would look
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_an_unknown_cap_name_fails_rather_than_being_ignored PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a compiled bundle offers no runtime write path to its caps
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_compiled_bundle_offers_no_runtime_write_path_to_its_caps` executed under `dev/.venv/bin/python`
- Expected: ARCHITECTURE_KB §23.12 / AC-F36-13: caps change by rebuilding the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_compiled_bundle_offers_no_runtime_write_path_to_its_caps PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a rule missing a fixture fails the bundle not just the suite
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_rule_missing_a_fixture_fails_the_bundle_not_just_the_suite` executed under `dev/.venv/bin/python`
- Expected: a rule missing a fixture fails the bundle not just the suite
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_rule_missing_a_fixture_fails_the_bundle_not_just_the_suite PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a fixture file that does not exist fails the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_fixture_file_that_does_not_exist_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a fixture file that does not exist fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_fixture_file_that_does_not_exist_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a firing fixture that does not fire fails the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_firing_fixture_that_does_not_fire_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: Worse than a missing fixture: the suite would report evidence of a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_firing_fixture_that_does_not_fire_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non firing fixture that fires fails the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_non_firing_fixture_that_fires_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a non firing fixture that fires fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_non_firing_fixture_that_fires_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a predicate naming an unknown field fails the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_predicate_naming_an_unknown_field_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a predicate naming an unknown field fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_predicate_naming_an_unknown_field_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a quantitative rule must declare its inclusivity
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_quantitative_rule_must_declare_its_inclusivity` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-16` asserts the boundary behaves as DISPLAYED to the user. A
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_quantitative_rule_must_declare_its_inclusivity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: duplicate rule ids fail the build
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_duplicate_rule_ids_fail_the_build` executed under `dev/.venv/bin/python`
- Expected: duplicate rule ids fail the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_duplicate_rule_ids_fail_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent capability allowlist is not an empty one
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_an_absent_capability_allowlist_is_not_an_empty_one` executed under `dev/.venv/bin/python`
- Expected: an absent capability allowlist is not an empty one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_an_absent_capability_allowlist_is_not_an_empty_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty allowlist compiles and denies everything
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_an_empty_allowlist_compiles_and_denies_everything` executed under `dev/.venv/bin/python`
- Expected: an empty allowlist compiles and denies everything
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_an_empty_allowlist_compiles_and_denies_everything PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the routing budget must live in the bundle
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_the_routing_budget_must_live_in_the_bundle` executed under `dev/.venv/bin/python`
- Expected: the routing budget must live in the bundle
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_the_routing_budget_must_live_in_the_bundle PASSED` (verbatim from the `-v` node list of this run)

### Scenario: first publication is classified risk increasing
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_first_publication_is_classified_risk_increasing` executed under `dev/.venv/bin/python`
- Expected: first publication is classified risk increasing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_first_publication_is_classified_risk_increasing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: widening a threshold is classified risk increasing by the system
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_widening_a_threshold_is_classified_risk_increasing_by_the_system` executed under `dev/.venv/bin/python`
- Expected: widening a threshold is classified risk increasing by the system
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_widening_a_threshold_is_classified_risk_increasing_by_the_system PASSED` (verbatim from the `-v` node list of this run)

### Scenario: raising a cap is classified risk increasing
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_raising_a_cap_is_classified_risk_increasing` executed under `dev/.venv/bin/python`
- Expected: raising a cap is classified risk increasing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_raising_a_cap_is_classified_risk_increasing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: broadening the allowlist is classified risk increasing
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_broadening_the_allowlist_is_classified_risk_increasing` executed under `dev/.venv/bin/python`
- Expected: broadening the allowlist is classified risk increasing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_broadening_the_allowlist_is_classified_risk_increasing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: moving a rule from enforce to shadow is risk increasing
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_moving_a_rule_from_enforce_to_shadow_is_risk_increasing` executed under `dev/.venv/bin/python`
- Expected: moving a rule from enforce to shadow is risk increasing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_moving_a_rule_from_enforce_to_shadow_is_risk_increasing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: removing a rule is risk increasing
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_removing_a_rule_is_risk_increasing` executed under `dev/.venv/bin/python`
- Expected: removing a rule is risk increasing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_removing_a_rule_is_risk_increasing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a tightening diff is not risk increasing but is still a change
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_tightening_diff_is_not_risk_increasing_but_is_still_a_change` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-22`: dual authorisation is NOT conditional on the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_tightening_diff_is_not_risk_increasing_but_is_still_a_change PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero change diff is detected as such
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_zero_change_diff_is_detected_as_such` executed under `dev/.venv/bin/python`
- Expected: a zero change diff is detected as such
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_zero_change_diff_is_detected_as_such PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a structural predicate change is never assumed to be a tightening
- Status: EXECUTED
- Input: `backend/tests/test_broker_bundle.py::test_a_structural_predicate_change_is_never_assumed_to_be_a_tightening` executed under `dev/.venv/bin/python`
- Expected: a structural predicate change is never assumed to be a tightening
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_bundle.py::test_a_structural_predicate_change_is_never_assumed_to_be_a_tightening PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_broker_emission_path.py`

### Scenario: a clean emission is allowed and records one decision
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_a_clean_emission_is_allowed_and_records_one_decision` executed under `dev/.venv/bin/python`
- Expected: a clean emission is allowed and records one decision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_a_clean_emission_is_allowed_and_records_one_decision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the emission shares the action legs bundle hash and id scheme
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_the_emission_shares_the_action_legs_bundle_hash_and_id_scheme` executed under `dev/.venv/bin/python`
- Expected: the emission shares the action legs bundle hash and id scheme
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_the_emission_shares_the_action_legs_bundle_hash_and_id_scheme PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an emission capability absent from the allowlist is denied
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_emission_capability_absent_from_the_allowlist_is_denied` executed under `dev/.venv/bin/python`
- Expected: an emission capability absent from the allowlist is denied
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_emission_capability_absent_from_the_allowlist_is_denied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the skill allowlist narrows emissions too
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_the_skill_allowlist_narrows_emissions_too` executed under `dev/.venv/bin/python`
- Expected: the skill allowlist narrows emissions too
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_the_skill_allowlist_narrows_emissions_too PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unresolvable bundle denies every emission
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_unresolvable_bundle_denies_every_emission` executed under `dev/.venv/bin/python`
- Expected: an unresolvable bundle denies every emission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_unresolvable_bundle_denies_every_emission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: decide emission has no override parameter
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_decide_emission_has_no_override_parameter` executed under `dev/.venv/bin/python`
- Expected: The absence IS the control, so it is asserted rather than described.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_decide_emission_has_no_override_parameter PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no emission decision ever carries an override reference
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_no_emission_decision_ever_carries_an_override_reference` executed under `dev/.venv/bin/python`
- Expected: no emission decision ever carries an override reference
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_no_emission_decision_ever_carries_an_override_reference PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite a an uncited classification is not emitted
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_a_an_uncited_classification_is_not_emitted` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-31, leg (a). A classification with no evidence reference resolving
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_a_an_uncited_classification_is_not_emitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite b the residual after citation may not be zero by omission
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_b_the_residual_after_citation_may_not_be_zero_by_omission` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-31, leg (b). The residual-after-citation is an emitted FIELD; an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_b_the_residual_after_citation_may_not_be_zero_by_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite c the treatment claim must carry its own ground
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_the_treatment_claim_must_carry_its_own_ground` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-32, the RT-02 case. Passing coverage arithmetic is not sufficient
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_c_the_treatment_claim_must_carry_its_own_ground PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite c rejects a size shaped treatment ground[magnitude]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[magnitude]` executed under `dev/.venv/bin/python`, parameter case `magnitude`
- Expected: COVERS AC-F36-32, and A20's structural leg where the two meet.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[magnitude] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite c rejects a size shaped treatment ground[threshold]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[threshold]` executed under `dev/.venv/bin/python`, parameter case `threshold`
- Expected: COVERS AC-F36-32, and A20's structural leg where the two meet.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[threshold] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite c rejects a size shaped treatment ground[none]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[none]` executed under `dev/.venv/bin/python`, parameter case `none`
- Expected: COVERS AC-F36-32, and A20's structural leg where the two meet.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[none] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g cite c rejects a size shaped treatment ground[]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: COVERS AC-F36-32, and A20's structural leg where the two meet.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_cite_c_rejects_a_size_shaped_treatment_ground[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restate prior period treatment is context never evidence
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_prior_period_treatment_is_context_never_evidence` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-34. Prior-period treatment is inadmissible AS EVIDENCE for a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restate_prior_period_treatment_is_context_never_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restate the same emission passes on its own ground
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_the_same_emission_passes_on_its_own_ground` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-34's negative control: the same emission on a substantiated ground
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restate_the_same_emission_passes_on_its_own_ground PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restate third consecutive restatement escalates rather than denies
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_third_consecutive_restatement_escalates_rather_than_denies` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-34's second clause, which routes to AC-F36-11's escalation.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restate_third_consecutive_restatement_escalates_rather_than_denies PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restate second consecutive restatement does not escalate
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restate_second_consecutive_restatement_does_not_escalate` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-34's boundary: one period short of the escalation count.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restate_second_consecutive_restatement_does_not_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g noex an absence claim over partial coverage is not emitted
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_partial_coverage_is_not_emitted` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-35. No absence claim in ANY phrasing over sub-100% coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_partial_coverage_is_not_emitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g noex an absence claim over stale but full coverage is declined
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_stale_but_full_coverage_is_declined` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-35's staleness leg: full coverage of stale data is not coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_noex_an_absence_claim_over_stale_but_full_coverage_is_declined PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g noex fires as a denial when the rule is reached directly
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_noex_fires_as_a_denial_when_the_rule_is_reached_directly` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-35 at the rule rather than through the abstention path, so the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_noex_fires_as_a_denial_when_the_rule_is_reached_directly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restype a declared type without its evidence schema declines
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restype_a_declared_type_without_its_evidence_schema_declines` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-36. A proposal is never accepted on evidence sufficient for a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restype_a_declared_type_without_its_evidence_schema_declines PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g restype the rule still fires on its own context
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_restype_the_rule_still_fires_on_its_own_context` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-36 at the rule, naming the type and the unsatisfied schema.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_restype_the_rule_still_fires_on_its_own_context PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf materiality markers are rejected unconditionally[immaterial]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[immaterial]` executed under `dev/.venv/bin/python`, parameter case `immaterial`
- Expected: COVERS AC-F36-37's second group, which is denied unconditionally naming A20.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[immaterial] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf materiality markers are rejected unconditionally[not_significant]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[not_significant]` executed under `dev/.venv/bin/python`, parameter case `not_significant`
- Expected: COVERS AC-F36-37's second group, which is denied unconditionally naming A20.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[not_significant] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf materiality markers are rejected unconditionally[de_minimis]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[de_minimis]` executed under `dev/.venv/bin/python`, parameter case `de_minimis`
- Expected: COVERS AC-F36-37's second group, which is denied unconditionally naming A20.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[de_minimis] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf materiality markers are rejected unconditionally[below_threshold_no_action_needed]
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[below_threshold_no_action_needed]` executed under `dev/.venv/bin/python`, parameter case `below_threshold_no_action_needed`
- Expected: COVERS AC-F36-37's second group, which is denied unconditionally naming A20.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_materiality_markers_are_rejected_unconditionally[below_threshold_no_action_needed] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf verified requires a verification record
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_verified_requires_a_verification_record` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-37's first group: 'verified' without a resolvable record ID.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_verified_requires_a_verification_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf confirmed requires a two sided tie
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_confirmed_requires_a_two_sided_tie` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-37's first group: 'confirmed' without a two-sided tie.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_confirmed_requires_a_two_sided_tie PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g conf does not constrain how well the agent explains
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_conf_does_not_constrain_how_well_the_agent_explains` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-37's last sentence, and FUNCTIONAL_SPEC 12's standing exclusion:
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_conf_does_not_constrain_how_well_the_agent_explains PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g selfref the agent output namespace is inadmissible
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_selfref_the_agent_output_namespace_is_inadmissible` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-38. An evidence reference resolving into the agent-output
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_selfref_the_agent_output_namespace_is_inadmissible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g selfref a human disposition is admissible
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_selfref_a_human_disposition_is_admissible` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-38's second clause: every leaf of an emitted conclusion's evidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_selfref_a_human_disposition_is_admissible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g nohuman asserted agreement needs a disposition record
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_nohuman_asserted_agreement_needs_a_disposition_record` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-39. Asserted or implied human agreement without a referenced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_nohuman_asserted_agreement_needs_a_disposition_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g scope drift a reference outside declared scope is a failure not a caveat
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_scope_drift_a_reference_outside_declared_scope_is_a_failure_not_a_caveat` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-40. The out-of-scope reference is named and is NOT emitted with a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_scope_drift_a_reference_outside_declared_scope_is_a_failure_not_a_caveat PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g inject unquoted ledger text is not emitted
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_unquoted_ledger_text_is_not_emitted` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-41. Instruction-bearing ledger text does not reach an emitted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_inject_unquoted_ledger_text_is_not_emitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g inject quoted ledger text carrying its source row is fine
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_quoted_ledger_text_carrying_its_source_row_is_fine` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-41's positive leg: the text renders as quoted data carrying its
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_inject_quoted_ledger_text_carrying_its_source_row_is_fine PASSED` (verbatim from the `-v` node list of this run)

### Scenario: g inject authorisation leg no data field can widen a capability
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_g_inject_authorisation_leg_no_data_field_can_widen_a_capability` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-42 (RAI-ARCH-8 / SECURITY_KB T2). The authorisation is computed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_g_inject_authorisation_leg_no_data_field_can_widen_a_capability PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every one of the nine guardrails has at least one rule
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_every_one_of_the_nine_guardrails_has_at_least_one_rule` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-30's precondition: a guardrail with no rule is a constraint with
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_every_one_of_the_nine_guardrails_has_at_least_one_rule PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every emission rule names its guardrail
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_every_emission_rule_names_its_guardrail` executed under `dev/.venv/bin/python`
- Expected: every emission rule names its guardrail
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_every_emission_rule_names_its_guardrail PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unevaluable emission check denies naming the check
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_unevaluable_emission_check_denies_naming_the_check` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-27. Emission fails closed on exactly the terms AC-F36-17 fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_unevaluable_emission_check_denies_naming_the_check PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab3 out of population returns a typed decline not silence
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab3_out_of_population_returns_a_typed_decline_not_silence` executed under `dev/.venv/bin/python`
- Expected: RAI-ARCH-6: F33's deferred sub-types get an explicit typed decline
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab3_out_of_population_returns_a_typed_decline_not_silence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab5 an evidential tie is reported as a tie
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab5_an_evidential_tie_is_reported_as_a_tie` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-44. An AB5 abstention naming BOTH candidate resolution types, and
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab5_an_evidential_tie_is_reported_as_a_tie PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab5 takes precedence over ab1
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab5_takes_precedence_over_ab1` executed under `dev/.venv/bin/python`
- Expected: ab5 takes precedence over ab1
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab5_takes_precedence_over_ab1 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab6 conflicting sources are named
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab6_conflicting_sources_are_named` executed under `dev/.venv/bin/python`
- Expected: ab6 conflicting sources are named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab6_conflicting_sources_are_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab1 evidence schema unsatisfied
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab1_evidence_schema_unsatisfied` executed under `dev/.venv/bin/python`
- Expected: ab1 evidence schema unsatisfied
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab1_evidence_schema_unsatisfied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab2 coverage or staleness
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab2_coverage_or_staleness` executed under `dev/.venv/bin/python`
- Expected: ab2 coverage or staleness
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab2_coverage_or_staleness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ab4 a refused emission abstains and its evidence is never examined
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_ab4_a_refused_emission_abstains_and_its_evidence_is_never_examined` executed under `dev/.venv/bin/python`
- Expected: ab4 a refused emission abstains and its evidence is never examined
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_ab4_a_refused_emission_abstains_and_its_evidence_is_never_examined PASSED` (verbatim from the `-v` node list of this run)

### Scenario: all six abstention types are reachable through the broker
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_all_six_abstention_types_are_reachable_through_the_broker` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-45. Each abstention carries its own type; none is emitted as an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_all_six_abstention_types_are_reachable_through_the_broker PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no abstention produced by the broker renders as a negative finding
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_no_abstention_produced_by_the_broker_renders_as_a_negative_finding` executed under `dev/.venv/bin/python`
- Expected: no abstention produced by the broker renders as a negative finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_no_abstention_produced_by_the_broker_renders_as_a_negative_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention is stored as abstain not as deny
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_abstention_is_stored_as_abstain_not_as_deny` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-43. The abstention is a first-class output object, not an error,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_abstention_is_stored_as_abstain_not_as_deny PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention object exists on the decision and absent otherwise
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_abstention_object_exists_on_the_decision_and_absent_otherwise` executed under `dev/.venv/bin/python`
- Expected: an abstention object exists on the decision and absent otherwise
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_abstention_object_exists_on_the_decision_and_absent_otherwise PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clean request triggers no abstention
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_a_clean_request_triggers_no_abstention` executed under `dev/.venv/bin/python`
- Expected: a clean request triggers no abstention
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_a_clean_request_triggers_no_abstention PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the trigger precedence is ab3 ab5 ab6 ab1 ab2
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_the_trigger_precedence_is_ab3_ab5_ab6_ab1_ab2` executed under `dev/.venv/bin/python`
- Expected: the trigger precedence is ab3 ab5 ab6 ab1 ab2
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_the_trigger_precedence_is_ab3_ab5_ab6_ab1_ab2 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every trigger names a gap and exactly one resolving action
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_every_trigger_names_a_gap_and_exactly_one_resolving_action` executed under `dev/.venv/bin/python`
- Expected: every trigger names a gap and exactly one resolving action
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_every_trigger_names_a_gap_and_exactly_one_resolving_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown emission field is refused at construction
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_an_unknown_emission_field_is_refused_at_construction` executed under `dev/.venv/bin/python`
- Expected: an unknown emission field is refused at construction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_an_unknown_emission_field_is_refused_at_construction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no field on which the agent reports its own compliance
- Status: EXECUTED
- Input: `backend/tests/test_broker_emission_path.py::test_there_is_no_field_on_which_the_agent_reports_its_own_compliance` executed under `dev/.venv/bin/python`
- Expected: there is no field on which the agent reports its own compliance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_emission_path.py::test_there_is_no_field_on_which_the_agent_reports_its_own_compliance PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_broker_expr.py`

### Scenario: comparison membership and boolean composition
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_comparison_membership_and_boolean_composition` executed under `dev/.venv/bin/python`
- Expected: comparison membership and boolean composition
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_comparison_membership_and_boolean_composition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: threshold boundary is exact because money is decimal
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_threshold_boundary_is_exact_because_money_is_decimal` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-16` is a boundary criterion, so the arithmetic must be exact.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_threshold_boundary_is_exact_because_money_is_decimal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: arithmetic and negation
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_arithmetic_and_negation` executed under `dev/.venv/bin/python`
- Expected: arithmetic and negation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_arithmetic_and_negation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: effective bound fields are reported
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_effective_bound_fields_are_reported` executed under `dev/.venv/bin/python`
- Expected: effective bound fields are reported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_effective_bound_fields_are_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unknown field fails at compile time not silently at runtime
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_unknown_field_fails_at_compile_time_not_silently_at_runtime` executed under `dev/.venv/bin/python`
- Expected: unknown field fails at compile time not silently at runtime
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_unknown_field_fails_at_compile_time_not_silently_at_runtime PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a typo would otherwise produce a rule that never fires
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_a_typo_would_otherwise_produce_a_rule_that_never_fires` executed under `dev/.venv/bin/python`
- Expected: The failure this check exists to prevent, demonstrated directly.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_a_typo_would_otherwise_produce_a_rule_that_never_fires PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[__import__('os').system('true')]
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[__import__('os').system('true')]` executed under `dev/.venv/bin/python`, parameter case `__import__('os').system('true')`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[__import__('os').system('true')] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[action.kind.__class__]
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind.__class__]` executed under `dev/.venv/bin/python`, parameter case `action.kind.__class__`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind.__class__] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[open('/etc/passwd')]
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[open('/etc/passwd')]` executed under `dev/.venv/bin/python`, parameter case `open('/etc/passwd')`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[open('/etc/passwd')] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[lambda x: x]
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[lambda x: x]` executed under `dev/.venv/bin/python`, parameter case `lambda x: x`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[lambda x: x] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[[i for i in range(3)]]
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[[i for i in range(3)]]` executed under `dev/.venv/bin/python`, parameter case `i for i in range(3)`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[[i for i in range(3)]] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the language cannot reach python[action.kind = 'x']
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind = 'x']` executed under `dev/.venv/bin/python`, parameter case `action.kind = 'x'`
- Expected: the language cannot reach python
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_language_cannot_reach_python[action.kind = 'x'] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: only the three named constructors are callable
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_only_the_three_named_constructors_are_callable` executed under `dev/.venv/bin/python`
- Expected: only the three named constructors are callable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_only_the_three_named_constructors_are_callable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: float is refused rather than silently compared
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_float_is_refused_rather_than_silently_compared` executed under `dev/.venv/bin/python`
- Expected: float is refused rather than silently compared
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_float_is_refused_rather_than_silently_compared PASSED` (verbatim from the `-v` node list of this run)

### Scenario: empty predicate is not a predicate
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_empty_predicate_is_not_a_predicate` executed under `dev/.venv/bin/python`
- Expected: empty predicate is not a predicate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_empty_predicate_is_not_a_predicate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: non boolean result is a type error not a truthy pass
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_non_boolean_result_is_a_type_error_not_a_truthy_pass` executed under `dev/.venv/bin/python`
- Expected: non boolean result is a type error not a truthy pass
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_non_boolean_result_is_a_type_error_not_a_truthy_pass PASSED` (verbatim from the `-v` node list of this run)

### Scenario: absent context field is unevaluable and not false
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_absent_context_field_is_unevaluable_and_not_false` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-27`: an un-evaluable check must deny. It can only deny if it is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_absent_context_field_is_unevaluable_and_not_false PASSED` (verbatim from the `-v` node list of this run)

### Scenario: null is not silently false
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_null_is_not_silently_false` executed under `dev/.venv/bin/python`
- Expected: null is not silently false
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_null_is_not_silently_false PASSED` (verbatim from the `-v` node list of this run)

### Scenario: in requires a list on the right
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_in_requires_a_list_on_the_right` executed under `dev/.venv/bin/python`
- Expected: in requires a list on the right
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_in_requires_a_list_on_the_right PASSED` (verbatim from the `-v` node list of this run)

### Scenario: trailing tokens are a syntax error
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_trailing_tokens_are_a_syntax_error` executed under `dev/.venv/bin/python`
- Expected: trailing tokens are a syntax error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_trailing_tokens_are_a_syntax_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unbalanced parenthesis is a syntax error
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_unbalanced_parenthesis_is_a_syntax_error` executed under `dev/.venv/bin/python`
- Expected: unbalanced parenthesis is a syntax error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_unbalanced_parenthesis_is_a_syntax_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: division by zero is an evaluation error
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_division_by_zero_is_an_evaluation_error` executed under `dev/.venv/bin/python`
- Expected: division by zero is an evaluation error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_division_by_zero_is_an_evaluation_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: subset of holds only when every member is admissible
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_subset_of_holds_only_when_every_member_is_admissible` executed under `dev/.venv/bin/python`
- Expected: subset of holds only when every member is admissible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_subset_of_holds_only_when_every_member_is_admissible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the empty list is a subset and that is deliberate
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_empty_list_is_a_subset_and_that_is_deliberate` executed under `dev/.venv/bin/python`
- Expected: the empty list is a subset and that is deliberate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_empty_list_is_a_subset_and_that_is_deliberate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: intersects is true on any overlap and false on none
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_intersects_is_true_on_any_overlap_and_false_on_none` executed under `dev/.venv/bin/python`
- Expected: intersects is true on any overlap and false on none
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_intersects_is_true_on_any_overlap_and_false_on_none PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a set operator against a scalar is unevaluable not false
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_scalar_is_unevaluable_not_false` executed under `dev/.venv/bin/python`
- Expected: a set operator against a scalar is unevaluable not false
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_scalar_is_unevaluable_not_false PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a set operator against a missing field is unevaluable not false
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_missing_field_is_unevaluable_not_false` executed under `dev/.venv/bin/python`
- Expected: a set operator against a missing field is unevaluable not false
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_a_set_operator_against_a_missing_field_is_unevaluable_not_false PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the new operators are operators not values
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_new_operators_are_operators_not_values` executed under `dev/.venv/bin/python`
- Expected: the new operators are operators not values
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_new_operators_are_operators_not_values PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the new operators still bind against the declared schema
- Status: EXECUTED
- Input: `backend/tests/test_broker_expr.py::test_the_new_operators_still_bind_against_the_declared_schema` executed under `dev/.venv/bin/python`
- Expected: the new operators still bind against the declared schema
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_broker_expr.py::test_the_new_operators_still_bind_against_the_declared_schema PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_bundle_publication.py`

### Scenario: the author of a rule change may not publish the bundle
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_the_author_of_a_rule_change_may_not_publish_the_bundle` executed under `dev/.venv/bin/python`
- Expected: the author of a rule change may not publish the bundle
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_the_author_of_a_rule_change_may_not_publish_the_bundle PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a rejected publication leaves the prior bundle in force
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_rejected_publication_leaves_the_prior_bundle_in_force` executed under `dev/.venv/bin/python`
- Expected: a rejected publication leaves the prior bundle in force
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_rejected_publication_leaves_the_prior_bundle_in_force PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rejection is recorded as a control event
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_the_rejection_is_recorded_as_a_control_event` executed under `dev/.venv/bin/python`
- Expected: the rejection is recorded as a control event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_the_rejection_is_recorded_as_a_control_event PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the classification names the specific fields that triggered it
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_the_classification_names_the_specific_fields_that_triggered_it` executed under `dev/.venv/bin/python`
- Expected: the classification names the specific fields that triggered it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_the_classification_names_the_specific_fields_that_triggered_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: publication does not complete without acknowledgement
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_publication_does_not_complete_without_acknowledgement` executed under `dev/.venv/bin/python`
- Expected: publication does not complete without acknowledgement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_publication_does_not_complete_without_acknowledgement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: acknowledging a different classification does not count
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_acknowledging_a_different_classification_does_not_count` executed under `dev/.venv/bin/python`
- Expected: The authoriser cannot have acknowledged something other than what is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_acknowledging_a_different_classification_does_not_count PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a risk increasing publication records its fields
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_risk_increasing_publication_records_its_fields` executed under `dev/.venv/bin/python`
- Expected: a risk increasing publication records its fields
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_risk_increasing_publication_records_its_fields PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a tightening diff still requires two distinct identities
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_tightening_diff_still_requires_two_distinct_identities` executed under `dev/.venv/bin/python`
- Expected: a tightening diff still requires two distinct identities
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_tightening_diff_still_requires_two_distinct_identities PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero change submission is rejected
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_zero_change_submission_is_rejected` executed under `dev/.venv/bin/python`
- Expected: a zero change submission is rejected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_zero_change_submission_is_rejected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the first run reports every fixture and is not a pass
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_the_first_run_reports_every_fixture_and_is_not_a_pass` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-24`: with no prior results there is no regression comparison, so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_the_first_run_reports_every_fixture_and_is_not_a_pass PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a second run with a baseline passes
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_second_run_with_a_baseline_passes` executed under `dev/.venv/bin/python`
- Expected: a second run with a baseline passes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_second_run_with_a_baseline_passes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a fixture that stops firing is a failure naming the prior run
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_fixture_that_stops_firing_is_a_failure_naming_the_prior_run` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-23` — THE threshold-widening detector.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_fixture_that_stops_firing_is_a_failure_naming_the_prior_run PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the baseline is not updated by the run that observed the change
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_the_baseline_is_not_updated_by_the_run_that_observed_the_change` executed under `dev/.venv/bin/python`
- Expected: the baseline is not updated by the run that observed the change
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_the_baseline_is_not_updated_by_the_run_that_observed_the_change PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing fixture is reported by name as unevidenced
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_missing_fixture_is_reported_by_name_as_unevidenced` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-05`. The compiler prevents a bundle from being BUILT without both
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_missing_fixture_is_reported_by_name_as_unevidenced PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a not passed run raises a control event
- Status: EXECUTED
- Input: `backend/tests/test_bundle_publication.py::test_a_not_passed_run_raises_a_control_event` executed under `dev/.venv/bin/python`
- Expected: a not passed run raises a control event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_bundle_publication.py::test_a_not_passed_run_raises_a_control_event PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_canonical.py`

### Scenario: key order does not change the hash
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_key_order_does_not_change_the_hash` executed under `dev/.venv/bin/python`
- Expected: key order does not change the hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_key_order_does_not_change_the_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: nested key order does not change the hash
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_nested_key_order_does_not_change_the_hash` executed under `dev/.venv/bin/python`
- Expected: nested key order does not change the hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_nested_key_order_does_not_change_the_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: list order does change the hash
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_list_order_does_change_the_hash` executed under `dev/.venv/bin/python`
- Expected: list order does change the hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_list_order_does_change_the_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: decimals serialise as plain strings
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_decimals_serialise_as_plain_strings` executed under `dev/.venv/bin/python`
- Expected: decimals serialise as plain strings
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_decimals_serialise_as_plain_strings PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a float raises rather than hashing irreproducibly
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_a_float_raises_rather_than_hashing_irreproducibly` executed under `dev/.venv/bin/python`
- Expected: a float raises rather than hashing irreproducibly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_a_float_raises_rather_than_hashing_irreproducibly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a nested float also raises
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_a_nested_float_also_raises` executed under `dev/.venv/bin/python`
- Expected: a nested float also raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_a_nested_float_also_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: tuples and lists canonicalise alike
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_tuples_and_lists_canonicalise_alike` executed under `dev/.venv/bin/python`
- Expected: tuples and lists canonicalise alike
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_tuples_and_lists_canonicalise_alike PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unicode is not escaped
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_unicode_is_not_escaped` executed under `dev/.venv/bin/python`
- Expected: unicode is not escaped
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_unicode_is_not_escaped PASSED` (verbatim from the `-v` node list of this run)

### Scenario: hash bytes is sha256
- Status: EXECUTED
- Input: `backend/tests/test_canonical.py::test_hash_bytes_is_sha256` executed under `dev/.venv/bin/python`
- Expected: hash bytes is sha256
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_canonical.py::test_hash_bytes_is_sha256 PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_certified_query_execution.py`

### Scenario: a certified query executes and carries its provenance
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_certified_query_executes_and_carries_its_provenance` executed under `dev/.venv/bin/python`
- Expected: a certified query executes and carries its provenance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_certified_query_executes_and_carries_its_provenance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: amounts come back as text not float
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_amounts_come_back_as_text_not_float` executed under `dev/.venv/bin/python`
- Expected: amounts come back as text not float
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_amounts_come_back_as_text_not_float PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string in the query id is simply an unknown query[SELECT * FROM gl_je_lines]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[SELECT * FROM gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `SELECT * FROM gl_je_lines`
- Expected: a sql string in the query id is simply an unknown query
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[SELECT * FROM gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string in the query id is simply an unknown query[gl.entries_by_recurrence; DROP TABLE gl_je_lines]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[gl.entries_by_recurrence; DROP TABLE gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `gl.entries_by_recurrence; DROP TABLE gl_je_lines`
- Expected: a sql string in the query id is simply an unknown query
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[gl.entries_by_recurrence; DROP TABLE gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string in the query id is simply an unknown query[' OR 1=1 --]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[' OR 1=1 --]` executed under `dev/.venv/bin/python`, parameter case `' OR 1=1 --`
- Expected: a sql string in the query id is simply an unknown query
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[' OR 1=1 --] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string in the query id is simply an unknown query[]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a sql string in the query id is simply an unknown query
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_the_query_id_is_simply_an_unknown_query[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the request model forbids an extra field
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_request_model_forbids_an_extra_field` executed under `dev/.venv/bin/python`
- Expected: the request model forbids an extra field
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_request_model_forbids_an_extra_field PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no field of the request model can carry a statement
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_no_field_of_the_request_model_can_carry_a_statement` executed under `dev/.venv/bin/python`
- Expected: no field of the request model can carry a statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_no_field_of_the_request_model_can_carry_a_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string bound as a parameter value is type rejected
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_bound_as_a_parameter_value_is_type_rejected` executed under `dev/.venv/bin/python`
- Expected: a sql string bound as a parameter value is type rejected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_bound_as_a_parameter_value_is_type_rejected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string in a string parameter is bound not interpreted
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_a_string_parameter_is_bound_not_interpreted` executed under `dev/.venv/bin/python`
- Expected: a sql string in a string parameter is bound not interpreted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_sql_string_in_a_string_parameter_is_bound_not_interpreted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: personal data query is refused before execution for the unentitled
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_personal_data_query_is_refused_before_execution_for_the_unentitled` executed under `dev/.venv/bin/python`
- Expected: personal data query is refused before execution for the unentitled
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_personal_data_query_is_refused_before_execution_for_the_unentitled PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same query executes for an entitled principal
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_for_an_entitled_principal` executed under `dev/.venv/bin/python`
- Expected: the same query executes for an entitled principal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_for_an_entitled_principal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: entitlement is checked before parameter validation
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_entitlement_is_checked_before_parameter_validation` executed under `dev/.venv/bin/python`
- Expected: entitlement is checked before parameter validation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_entitlement_is_checked_before_parameter_validation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no agent principal holds the personal data entitlement
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_no_agent_principal_holds_the_personal_data_entitlement` executed under `dev/.venv/bin/python`
- Expected: no agent principal holds the personal data entitlement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_no_agent_principal_holds_the_personal_data_entitlement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: model bound run over an unclassified column is refused by name
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_model_bound_run_over_an_unclassified_column_is_refused_by_name` executed under `dev/.venv/bin/python`
- Expected: model bound run over an unclassified column is refused by name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_model_bound_run_over_an_unclassified_column_is_refused_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same query executes on a non model bound path
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_on_a_non_model_bound_path` executed under `dev/.venv/bin/python`
- Expected: the same query executes on a non model bound path
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_same_query_executes_on_a_non_model_bound_path PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a model bound run over an ineligible query is refused
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_model_bound_run_over_an_ineligible_query_is_refused` executed under `dev/.venv/bin/python`
- Expected: a model bound run over an ineligible query is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_model_bound_run_over_an_ineligible_query_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing required parameter is named
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_missing_required_parameter_is_named` executed under `dev/.venv/bin/python`
- Expected: a missing required parameter is named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_missing_required_parameter_is_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an undeclared parameter is named
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_an_undeclared_parameter_is_named` executed under `dev/.venv/bin/python`
- Expected: an undeclared parameter is named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_an_undeclared_parameter_is_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period outside its domain is refused[0]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[0]` executed under `dev/.venv/bin/python`, parameter case `0`
- Expected: a period outside its domain is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period outside its domain is refused[13]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[13]` executed under `dev/.venv/bin/python`, parameter case `13`
- Expected: a period outside its domain is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[13] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period outside its domain is refused[-1]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[-1]` executed under `dev/.venv/bin/python`, parameter case `-1`
- Expected: a period outside its domain is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period outside its domain is refused[99]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[99]` executed under `dev/.venv/bin/python`, parameter case `99`
- Expected: a period outside its domain is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_period_outside_its_domain_is_refused[99] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the period domain boundaries are inclusive[1]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[1]` executed under `dev/.venv/bin/python`, parameter case `1`
- Expected: the period domain boundaries are inclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the period domain boundaries are inclusive[12]
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[12]` executed under `dev/.venv/bin/python`, parameter case `12`
- Expected: the period domain boundaries are inclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_period_domain_boundaries_are_inclusive[12] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a bool is rejected by the request model before the executor
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_bool_is_rejected_by_the_request_model_before_the_executor` executed under `dev/.venv/bin/python`
- Expected: a bool is rejected by the request model before the executor
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_bool_is_rejected_by_the_request_model_before_the_executor PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a numeric string is not silently coerced to an int
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_numeric_string_is_not_silently_coerced_to_an_int` executed under `dev/.venv/bin/python`
- Expected: a numeric string is not silently coerced to an int
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_numeric_string_is_not_silently_coerced_to_an_int PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the executor also guards types for direct callers
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_executor_also_guards_types_for_direct_callers` executed under `dev/.venv/bin/python`
- Expected: the executor also guards types for direct callers
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_executor_also_guards_types_for_direct_callers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an int where a string is declared is refused
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_an_int_where_a_string_is_declared_is_refused` executed under `dev/.venv/bin/python`
- Expected: an int where a string is declared is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_an_int_where_a_string_is_declared_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown version of a known query is refused
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_an_unknown_version_of_a_known_query_is_refused` executed under `dev/.venv/bin/python`
- Expected: an unknown version of a known query is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_an_unknown_version_of_a_known_query_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: query over http returns rows for the detector
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_query_over_http_returns_rows_for_the_detector` executed under `dev/.venv/bin/python`
- Expected: query over http returns rows for the detector
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_query_over_http_returns_rows_for_the_detector PASSED` (verbatim from the `-v` node list of this run)

### Scenario: http refusal becomes a typed client exception
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_http_refusal_becomes_a_typed_client_exception` executed under `dev/.venv/bin/python`
- Expected: http refusal becomes a typed client exception
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_http_refusal_becomes_a_typed_client_exception PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unresolvable principal is refused with no default identity
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_an_unresolvable_principal_is_refused_with_no_default_identity` executed under `dev/.venv/bin/python`
- Expected: an unresolvable principal is refused with no default identity
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_an_unresolvable_principal_is_refused_with_no_default_identity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a wrong client token is rejected before the principal is considered
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_a_wrong_client_token_is_rejected_before_the_principal_is_considered` executed under `dev/.venv/bin/python`
- Expected: a wrong client token is rejected before the principal is considered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_a_wrong_client_token_is_rejected_before_the_principal_is_considered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the catalogue omits personal data queries for the unentitled
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_catalogue_omits_personal_data_queries_for_the_unentitled` executed under `dev/.venv/bin/python`
- Expected: the catalogue omits personal data queries for the unentitled
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_catalogue_omits_personal_data_queries_for_the_unentitled PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the catalogue never returns sql text
- Status: EXECUTED
- Input: `backend/tests/test_certified_query_execution.py::test_the_catalogue_never_returns_sql_text` executed under `dev/.venv/bin/python`
- Expected: the catalogue never returns sql text
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_certified_query_execution.py::test_the_catalogue_never_returns_sql_text PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_close_dataset_registry.py`

### Scenario: the nine new populations compile
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_the_nine_new_populations_compile` executed under `dev/.venv/bin/python`
- Expected: the nine new populations compile
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_the_nine_new_populations_compile PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no population names a physical object
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_no_population_names_a_physical_object` executed under `dev/.venv/bin/python`
- Expected: The seam, re-asserted over the objects that have just been added.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_no_population_names_a_physical_object PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a population that named its table would not compile
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_a_population_that_named_its_table_would_not_compile` executed under `dev/.venv/bin/python`
- Expected: a population that named its table would not compile
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_a_population_that_named_its_table_would_not_compile PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the twelve new queries compile and carry a committed statement
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_the_twelve_new_queries_compile_and_carry_a_committed_statement` executed under `dev/.venv/bin/python`
- Expected: the twelve new queries compile and carry a committed statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_the_twelve_new_queries_compile_and_carry_a_committed_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no new query declares a parameter that could carry a predicate
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_no_new_query_declares_a_parameter_that_could_carry_a_predicate` executed under `dev/.venv/bin/python`
- Expected: no new query declares a parameter that could carry a predicate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_no_new_query_declares_a_parameter_that_could_carry_a_predicate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the narrative leg query is not model bound eligible
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_the_narrative_leg_query_is_not_model_bound_eligible` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §7.3: the similarity computation is deterministic.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_the_narrative_leg_query_is_not_model_bound_eligible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every new query is reachable only by id
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_every_new_query_is_reachable_only_by_id` executed under `dev/.venv/bin/python`
- Expected: There is no operation that takes the statement, only the id.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_every_new_query_is_reachable_only_by_id PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an omitted object fails the query rather than answering it with zero rows
- Status: EXECUTED
- Input: `backend/tests/test_close_dataset_registry.py::test_an_omitted_object_fails_the_query_rather_than_answering_it_with_zero_rows` executed under `dev/.venv/bin/python`
- Expected: an omitted object fails the query rather than answering it with zero rows
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_dataset_registry.py::test_an_omitted_object_fails_the_query_rather_than_answering_it_with_zero_rows PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_close_datasets.py`

### Scenario: an unknown family is an error not a silently clean fixture
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_an_unknown_family_is_an_error_not_a_silently_clean_fixture` executed under `dev/.venv/bin/python`
- Expected: an unknown family is an error not a silently clean fixture
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_an_unknown_family_is_an_error_not_a_silently_clean_fixture PASSED` (verbatim from the `-v` node list of this run)

### Scenario: generation is deterministic
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_generation_is_deterministic` executed under `dev/.venv/bin/python`
- Expected: generation is deterministic
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_generation_is_deterministic PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the seeded divergences are exactly the declared four
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_seeded_divergences_are_exactly_the_declared_four` executed under `dev/.venv/bin/python`
- Expected: the seeded divergences are exactly the declared four
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_seeded_divergences_are_exactly_the_declared_four PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the clean world ties exactly
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_ties_exactly` executed under `dev/.venv/bin/python`
- Expected: the clean world ties exactly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_clean_world_ties_exactly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two worlds differ only in the seeded divergences
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_two_worlds_differ_only_in_the_seeded_divergences` executed under `dev/.venv/bin/python`
- Expected: The single-variable property, asserted rather than asserted-about.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_two_worlds_differ_only_in_the_seeded_divergences PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the smallest currency unit divergence survives as a decimal
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_smallest_currency_unit_divergence_survives_as_a_decimal` executed under `dev/.venv/bin/python`
- Expected: the smallest currency unit divergence survives as a decimal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_smallest_currency_unit_divergence_survives_as_a_decimal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one divergence sits in the earliest period and one in the latest
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_one_divergence_sits_in_the_earliest_period_and_one_in_the_latest` executed under `dev/.venv/bin/python`
- Expected: one divergence sits in the earliest period and one in the latest
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_one_divergence_sits_in_the_earliest_period_and_one_in_the_latest PASSED` (verbatim from the `-v` node list of this run)

### Scenario: exactly one batch never arrived and it names what it would have fed
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_exactly_one_batch_never_arrived_and_it_names_what_it_would_have_fed` executed under `dev/.venv/bin/python`
- Expected: exactly one batch never arrived and it names what it would have fed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_exactly_one_batch_never_arrived_and_it_names_what_it_would_have_fed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing batch is distinct from a batch that arrived empty
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_a_missing_batch_is_distinct_from_a_batch_that_arrived_empty` executed under `dev/.venv/bin/python`
- Expected: The distinction the whole A2 leg rests on.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_a_missing_batch_is_distinct_from_a_batch_that_arrived_empty PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every batch arrived in the clean world
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_every_batch_arrived_in_the_clean_world` executed under `dev/.venv/bin/python`
- Expected: every batch arrived in the clean world
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_every_batch_arrived_in_the_clean_world PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one batch arrived late so late is distinguishable from absent
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_one_batch_arrived_late_so_late_is_distinguishable_from_absent` executed under `dev/.venv/bin/python`
- Expected: one batch arrived late so late is distinguishable from absent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_one_batch_arrived_late_so_late_is_distinguishable_from_absent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the a6 break is one subledger in one period
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_a6_break_is_one_subledger_in_one_period` executed under `dev/.venv/bin/python`
- Expected: the a6 break is one subledger in one period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_a6_break_is_one_subledger_in_one_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the a7 imbalance is one pair in one period
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_a7_imbalance_is_one_pair_in_one_period` executed under `dev/.venv/bin/python`
- Expected: the a7 imbalance is one pair in one period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_a7_imbalance_is_one_pair_in_one_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the a8 discontinuity breaks the identity by the declared amount
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_a8_discontinuity_breaks_the_identity_by_the_declared_amount` executed under `dev/.venv/bin/python`
- Expected: the a8 discontinuity breaks the identity by the declared amount
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_a8_discontinuity_breaks_the_identity_by_the_declared_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the a9 revaluation is applied twice exactly once
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_a9_revaluation_is_applied_twice_exactly_once` executed under `dev/.venv/bin/python`
- Expected: the a9 revaluation is applied twice exactly once
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_a9_revaluation_is_applied_twice_exactly_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the a10 residual exceeds its policy threshold
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_a10_residual_exceeds_its_policy_threshold` executed under `dev/.venv/bin/python`
- Expected: the a10 residual exceeds its policy threshold
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_a10_residual_exceeds_its_policy_threshold PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the accumulating account stays under threshold every period
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_accumulating_account_stays_under_threshold_every_period` executed under `dev/.venv/bin/python`
- Expected: the accumulating account stays under threshold every period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_accumulating_account_stays_under_threshold_every_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the accumulating account aggregates to the declared material amount
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_accumulating_account_aggregates_to_the_declared_material_amount` executed under `dev/.venv/bin/python`
- Expected: the accumulating account aggregates to the declared material amount
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_accumulating_account_aggregates_to_the_declared_material_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the one short variant differs in exactly one movement
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_one_short_variant_differs_in_exactly_one_movement` executed under `dev/.venv/bin/python`
- Expected: the one short variant differs in exactly one movement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_one_short_variant_differs_in_exactly_one_movement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the alternating account does not accumulate
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_alternating_account_does_not_accumulate` executed under `dev/.venv/bin/python`
- Expected: the alternating account does not accumulate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_alternating_account_does_not_accumulate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the narrative account repeats verbatim while its movements alternate
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_narrative_account_repeats_verbatim_while_its_movements_alternate` executed under `dev/.venv/bin/python`
- Expected: the narrative account repeats verbatim while its movements alternate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_narrative_account_repeats_verbatim_while_its_movements_alternate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the clean world gives each period a different explanation
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_gives_each_period_a_different_explanation` executed under `dev/.venv/bin/python`
- Expected: the clean world gives each period a different explanation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_clean_world_gives_each_period_a_different_explanation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two explanations were never recorded rather than recorded empty
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_two_explanations_were_never_recorded_rather_than_recorded_empty` executed under `dev/.venv/bin/python`
- Expected: two explanations were never recorded rather than recorded empty
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_two_explanations_were_never_recorded_rather_than_recorded_empty PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one account has a single period of history
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_one_account_has_a_single_period_of_history` executed under `dev/.venv/bin/python`
- Expected: one account has a single period of history
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_one_account_has_a_single_period_of_history PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the five miscodings are present and declared
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_five_miscodings_are_present_and_declared` executed under `dev/.venv/bin/python`
- Expected: the five miscodings are present and declared
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_five_miscodings_are_present_and_declared PASSED` (verbatim from the `-v` node list of this run)

### Scenario: three of the five are declared out of scope
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_three_of_the_five_are_declared_out_of_scope` executed under `dev/.venv/bin/python`
- Expected: three of the five are declared out of scope
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_three_of_the_five_are_declared_out_of_scope PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the peer set is large and overwhelmingly consistent
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_peer_set_is_large_and_overwhelmingly_consistent` executed under `dev/.venv/bin/python`
- Expected: 163 consistent peers plus the three period-3 miscodings.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_peer_set_is_large_and_overwhelmingly_consistent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the held out period carries three miscodings of which two are labelled
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_held_out_period_carries_three_miscodings_of_which_two_are_labelled` executed under `dev/.venv/bin/python`
- Expected: Without these the detector predicts nothing over the held-out period,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_held_out_period_carries_three_miscodings_of_which_two_are_labelled PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the clean world contains the peers and no candidate defects
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_clean_world_contains_the_peers_and_no_candidate_defects` executed under `dev/.venv/bin/python`
- Expected: the clean world contains the peers and no candidate defects
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_clean_world_contains_the_peers_and_no_candidate_defects PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the cut off posting disagrees with its evidence period
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_the_cut_off_posting_disagrees_with_its_evidence_period` executed under `dev/.venv/bin/python`
- Expected: the cut off posting disagrees with its evidence period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_the_cut_off_posting_disagrees_with_its_evidence_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one held out period has exactly one label and one has none
- Status: EXECUTED
- Input: `backend/tests/test_close_datasets.py::test_one_held_out_period_has_exactly_one_label_and_one_has_none` executed under `dev/.venv/bin/python`
- Expected: one held out period has exactly one label and one has none
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_close_datasets.py::test_one_held_out_period_has_exactly_one_label_and_one_has_none PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_conclusion_type.py`

### Scenario: full coverage yields the full population type
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_full_coverage_yields_the_full_population_type` executed under `dev/.venv/bin/python`
- Expected: full coverage yields the full population type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_full_coverage_yields_the_full_population_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: partial coverage yields the bounded type
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_partial_coverage_yields_the_bounded_type` executed under `dev/.venv/bin/python`
- Expected: partial coverage yields the bounded type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_partial_coverage_yields_the_bounded_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: zero coverage yields the no scan type
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_zero_coverage_yields_the_no_scan_type` executed under `dev/.venv/bin/python`
- Expected: zero coverage yields the no scan type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_zero_coverage_yields_the_no_scan_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the union is closed
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_union_is_closed` executed under `dev/.venv/bin/python`
- Expected: the union is closed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_union_is_closed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no exceptions exists only on the full population type
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_no_exceptions_exists_only_on_the_full_population_type` executed under `dev/.venv/bin/python`
- Expected: no exceptions exists only on the full population type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_no_exceptions_exists_only_on_the_full_population_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a bounded conclusion has no no exceptions attribute at all
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_has_no_no_exceptions_attribute_at_all` executed under `dev/.venv/bin/python`
- Expected: a bounded conclusion has no no exceptions attribute at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_has_no_no_exceptions_attribute_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a no scan conclusion has no no exceptions attribute at all
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_has_no_no_exceptions_attribute_at_all` executed under `dev/.venv/bin/python`
- Expected: a no scan conclusion has no no exceptions attribute at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_has_no_no_exceptions_attribute_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the attribute cannot be attached to a bounded instance
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_attribute_cannot_be_attached_to_a_bounded_instance` executed under `dev/.venv/bin/python`
- Expected: the attribute cannot be attached to a bounded instance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_attribute_cannot_be_attached_to_a_bounded_instance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a no scan conclusion carries no findings at all
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_carries_no_findings_at_all` executed under `dev/.venv/bin/python`
- Expected: a no scan conclusion carries no findings at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_no_scan_conclusion_carries_no_findings_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the full population constructor is not reachable by an ordinary caller
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_full_population_constructor_is_not_reachable_by_an_ordinary_caller` executed under `dev/.venv/bin/python`
- Expected: the full population constructor is not reachable by an ordinary caller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_full_population_constructor_is_not_reachable_by_an_ordinary_caller PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the other variants are also privately constructed
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_other_variants_are_also_privately_constructed` executed under `dev/.venv/bin/python`
- Expected: the other variants are also privately constructed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_other_variants_are_also_privately_constructed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the invariant is rechecked inside the constructor
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_invariant_is_rechecked_inside_the_constructor` executed under `dev/.venv/bin/python`
- Expected: the invariant is rechecked inside the constructor
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_invariant_is_rechecked_inside_the_constructor PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an object new bypass produces an unusable instance
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_an_object_new_bypass_produces_an_unusable_instance` executed under `dev/.venv/bin/python`
- Expected: an object new bypass produces an unusable instance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_an_object_new_bypass_produces_an_unusable_instance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a bounded conclusion cannot be built with an empty gap set
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_cannot_be_built_with_an_empty_gap_set` executed under `dev/.venv/bin/python`
- Expected: a bounded conclusion cannot be built with an empty gap set
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_bounded_conclusion_cannot_be_built_with_an_empty_gap_set PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the all clear phrases appear in one module only
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_all_clear_phrases_appear_in_one_module_only` executed under `dev/.venv/bin/python`
- Expected: the all clear phrases appear in one module only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_all_clear_phrases_appear_in_one_module_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no module reaches for the private factory key
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_no_module_reaches_for_the_private_factory_key` executed under `dev/.venv/bin/python`
- Expected: no module reaches for the private factory key
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_no_module_reaches_for_the_private_factory_key PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the lint detects a planted violation
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_violation` executed under `dev/.venv/bin/python`
- Expected: the lint detects a planted violation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_violation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the lint detects a planted factory key import
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_factory_key_import` executed under `dev/.venv/bin/python`
- Expected: the lint detects a planted factory key import
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_lint_detects_a_planted_factory_key_import PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the lint does not fire on ordinary words
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_lint_does_not_fire_on_ordinary_words` executed under `dev/.venv/bin/python`
- Expected: the lint does not fire on ordinary words
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_lint_does_not_fire_on_ordinary_words PASSED` (verbatim from the `-v` node list of this run)

### Scenario: all three surfaces render from the same object
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_all_three_surfaces_render_from_the_same_object` executed under `dev/.venv/bin/python`
- Expected: all three surfaces render from the same object
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_all_three_surfaces_render_from_the_same_object PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a partial clean result never renders an unqualified all clear
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_partial_clean_result_never_renders_an_unqualified_all_clear` executed under `dev/.venv/bin/python`
- Expected: a partial clean result never renders an unqualified all clear
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_partial_clean_result_never_renders_an_unqualified_all_clear PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a full and a partial result differ textually on every surface
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_full_and_a_partial_result_differ_textually_on_every_surface` executed under `dev/.venv/bin/python`
- Expected: a full and a partial result differ textually on every surface
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_full_and_a_partial_result_differ_textually_on_every_surface PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the no scan result renders no findings region
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_no_scan_result_renders_no_findings_region` executed under `dev/.venv/bin/python`
- Expected: the no scan result renders no findings region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_no_scan_result_renders_no_findings_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the partial run banner comes from the type
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_the_partial_run_banner_comes_from_the_type` executed under `dev/.venv/bin/python`
- Expected: the partial run banner comes from the type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_the_partial_run_banner_comes_from_the_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non conclusion cannot be rendered
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_a_non_conclusion_cannot_be_rendered` executed under `dev/.venv/bin/python`
- Expected: a non conclusion cannot be rendered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_a_non_conclusion_cannot_be_rendered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: full coverage with findings does not claim an all clear
- Status: EXECUTED
- Input: `backend/tests/test_conclusion_type.py::test_full_coverage_with_findings_does_not_claim_an_all_clear` executed under `dev/.venv/bin/python`
- Expected: full coverage with findings does not claim an all clear
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_conclusion_type.py::test_full_coverage_with_findings_does_not_claim_an_all_clear PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_control_events.py`

### Scenario: emit buffers and returns the event
- Status: EXECUTED
- Input: `backend/tests/test_control_events.py::test_emit_buffers_and_returns_the_event` executed under `dev/.venv/bin/python`
- Expected: emit buffers and returns the event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_control_events.py::test_emit_buffers_and_returns_the_event PASSED` (verbatim from the `-v` node list of this run)

### Scenario: buffered filters by type
- Status: EXECUTED
- Input: `backend/tests/test_control_events.py::test_buffered_filters_by_type` executed under `dev/.venv/bin/python`
- Expected: buffered filters by type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_control_events.py::test_buffered_filters_by_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: installed sink receives events
- Status: EXECUTED
- Input: `backend/tests/test_control_events.py::test_installed_sink_receives_events` executed under `dev/.venv/bin/python`
- Expected: installed sink receives events
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_control_events.py::test_installed_sink_receives_events PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failing sink does not break the caller and is itself recorded
- Status: EXECUTED
- Input: `backend/tests/test_control_events.py::test_a_failing_sink_does_not_break_the_caller_and_is_itself_recorded` executed under `dev/.venv/bin/python`
- Expected: a failing sink does not break the caller and is itself recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_control_events.py::test_a_failing_sink_does_not_break_the_caller_and_is_itself_recorded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: buffer is bounded
- Status: EXECUTED
- Input: `backend/tests/test_control_events.py::test_buffer_is_bounded` executed under `dev/.venv/bin/python`
- Expected: buffer is bounded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_control_events.py::test_buffer_is_bounded PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_credential_boundary.py`

### Scenario: resolution from api process raises and is recorded
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_resolution_from_api_process_raises_and_is_recorded` executed under `dev/.venv/bin/python`
- Expected: resolution from api process raises and is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_resolution_from_api_process_raises_and_is_recorded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: resolution with unset role raises
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_resolution_with_unset_role_raises` executed under `dev/.venv/bin/python`
- Expected: resolution with unset role raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_resolution_with_unset_role_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: boundary violation message does not contain a value
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_boundary_violation_message_does_not_contain_a_value` executed under `dev/.venv/bin/python`
- Expected: boundary violation message does not contain a value
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_boundary_violation_message_does_not_contain_a_value PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[GES_ORACLE_POSTING_PASSWORD]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_PASSWORD]` executed under `dev/.venv/bin/python`, parameter case `GES_ORACLE_POSTING_PASSWORD`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_PASSWORD] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[GES_ORACLE_POSTING_USER]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_USER]` executed under `dev/.venv/bin/python`, parameter case `GES_ORACLE_POSTING_USER`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_USER] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[GES_ORACLE_POSTING_TOKEN]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_TOKEN]` executed under `dev/.venv/bin/python`, parameter case `GES_ORACLE_POSTING_TOKEN`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GES_ORACLE_POSTING_TOKEN] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[ORACLE_POSTING_PASSWORD]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_POSTING_PASSWORD]` executed under `dev/.venv/bin/python`, parameter case `ORACLE_POSTING_PASSWORD`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_POSTING_PASSWORD] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[ORACLE_JOURNAL_POST_TOKEN]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_JOURNAL_POST_TOKEN]` executed under `dev/.venv/bin/python`, parameter case `ORACLE_JOURNAL_POST_TOKEN`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[ORACLE_JOURNAL_POST_TOKEN] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[FUSION_POSTING_CLIENT_SECRET]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[FUSION_POSTING_CLIENT_SECRET]` executed under `dev/.venv/bin/python`, parameter case `FUSION_POSTING_CLIENT_SECRET`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[FUSION_POSTING_CLIENT_SECRET] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting credential never resolves even inside ges[GL_INTERFACE_SUBMIT_KEY]
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GL_INTERFACE_SUBMIT_KEY]` executed under `dev/.venv/bin/python`, parameter case `GL_INTERFACE_SUBMIT_KEY`
- Expected: posting credential never resolves even inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_posting_credential_never_resolves_even_inside_ges[GL_INTERFACE_SUBMIT_KEY] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: undeclared name returns none and is recorded
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_undeclared_name_returns_none_and_is_recorded` executed under `dev/.venv/bin/python`
- Expected: undeclared name returns none and is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_undeclared_name_returns_none_and_is_recorded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: declared but absent returns none and is recorded
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_declared_but_absent_returns_none_and_is_recorded` executed under `dev/.venv/bin/python`
- Expected: declared but absent returns none and is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_declared_but_absent_returns_none_and_is_recorded PASSED` (verbatim from the `-v` node list of this run)

### Scenario: declared but empty string is treated as absent
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_declared_but_empty_string_is_treated_as_absent` executed under `dev/.venv/bin/python`
- Expected: declared but empty string is treated as absent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_declared_but_empty_string_is_treated_as_absent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: declared and present resolves inside ges
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_declared_and_present_resolves_inside_ges` executed under `dev/.venv/bin/python`
- Expected: declared and present resolves inside ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_declared_and_present_resolves_inside_ges PASSED` (verbatim from the `-v` node list of this run)

### Scenario: forbidden and declared sets do not overlap
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_forbidden_and_declared_sets_do_not_overlap` executed under `dev/.venv/bin/python`
- Expected: forbidden and declared sets do not overlap
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_forbidden_and_declared_sets_do_not_overlap PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api startup guard passes on a clean environment
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_passes_on_a_clean_environment` executed under `dev/.venv/bin/python`
- Expected: api startup guard passes on a clean environment
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_api_startup_guard_passes_on_a_clean_environment PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api startup guard refuses on a leaked credential
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_leaked_credential` executed under `dev/.venv/bin/python`
- Expected: api startup guard refuses on a leaked credential
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_leaked_credential PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api startup guard refuses on a posting credential
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_posting_credential` executed under `dev/.venv/bin/python`
- Expected: api startup guard refuses on a posting credential
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_api_startup_guard_refuses_on_a_posting_credential PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api startup guard ignores an empty value
- Status: EXECUTED
- Input: `backend/tests/test_credential_boundary.py::test_api_startup_guard_ignores_an_empty_value` executed under `dev/.venv/bin/python`
- Expected: api startup guard ignores an empty value
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_credential_boundary.py::test_api_startup_guard_ignores_an_empty_value PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_detector_manifests.py`

### Scenario: the committed manifests compile
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_the_committed_manifests_compile` executed under `dev/.venv/bin/python`
- Expected: the committed manifests compile
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_the_committed_manifests_compile PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two wedge detectors share population and input
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_the_two_wedge_detectors_share_population_and_input` executed under `dev/.venv/bin/python`
- Expected: the two wedge detectors share population and input
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_the_two_wedge_detectors_share_population_and_input PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the omission detector does not permit a posting resolution
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_the_omission_detector_does_not_permit_a_posting_resolution` executed under `dev/.venv/bin/python`
- Expected: the omission detector does not permit a posting resolution
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_the_omission_detector_does_not_permit_a_posting_resolution PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every manifest declares both fixtures
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_every_manifest_declares_both_fixtures` executed under `dev/.venv/bin/python`
- Expected: every manifest declares both fixtures
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_every_manifest_declares_both_fixtures PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the manifest hash is stable and changes with content
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_the_manifest_hash_is_stable_and_changes_with_content` executed under `dev/.venv/bin/python`
- Expected: the manifest hash is stable and changes with content
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_the_manifest_hash_is_stable_and_changes_with_content PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest naming a table fails compilation
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_manifest_naming_a_table_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: a manifest naming a table fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_manifest_naming_a_table_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest with a table key fails compilation
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_manifest_with_a_table_key_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: a manifest with a table key fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_manifest_with_a_table_key_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unregistered evaluator fails compilation
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_unregistered_evaluator_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: an unregistered evaluator fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_unregistered_evaluator_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: all eleven specified primitives are now built
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_all_eleven_specified_primitives_are_now_built` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §7.3 lists eleven. Pass 1 built two.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_all_eleven_specified_primitives_are_now_built PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a specified but unimplemented primitive still says so
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_specified_but_unimplemented_primitive_still_says_so` executed under `dev/.venv/bin/python`
- Expected: a specified but unimplemented primitive still says so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_specified_but_unimplemented_primitive_still_says_so PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no unimplemented primitive is secretly registered
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_no_unimplemented_primitive_is_secretly_registered` executed under `dev/.venv/bin/python`
- Expected: no unimplemented primitive is secretly registered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_no_unimplemented_primitive_is_secretly_registered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown population fails compilation
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_unknown_population_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: an unknown population fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_unknown_population_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an uncertified input query fails compilation
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_uncertified_input_query_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: an uncertified input query fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_uncertified_input_query_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an input query incompatible with the population fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_input_query_incompatible_with_the_population_fails` executed under `dev/.venv/bin/python`
- Expected: an input query incompatible with the population fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_input_query_incompatible_with_the_population_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: more than one input fails in pass 1
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_more_than_one_input_fails_in_pass_1` executed under `dev/.venv/bin/python`
- Expected: more than one input fails in pass 1
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_more_than_one_input_fails_in_pass_1 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an input without a version fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_input_without_a_version_fails` executed under `dev/.venv/bin/python`
- Expected: an input without a version fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_input_without_a_version_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing fixture fails compilation[positive]
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[positive]` executed under `dev/.venv/bin/python`, parameter case `positive`
- Expected: a missing fixture fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[positive] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing fixture fails compilation[negative]
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[negative]` executed under `dev/.venv/bin/python`, parameter case `negative`
- Expected: a missing fixture fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_missing_fixture_fails_compilation[negative] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a fixture naming an undeclared scenario fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_fixture_naming_an_undeclared_scenario_fails` executed under `dev/.venv/bin/python`
- Expected: a fixture naming an undeclared scenario fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_fixture_naming_an_undeclared_scenario_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a resolution type outside r1 to r6 fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_resolution_type_outside_r1_to_r6_fails` executed under `dev/.venv/bin/python`
- Expected: a resolution type outside r1 to r6 fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_resolution_type_outside_r1_to_r6_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no permitted resolution types fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_no_permitted_resolution_types_fails` executed under `dev/.venv/bin/python`
- Expected: no permitted resolution types fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_no_permitted_resolution_types_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing finding type fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_missing_finding_type_fails` executed under `dev/.venv/bin/python`
- Expected: a missing finding type fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_missing_finding_type_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty manifests directory fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_an_empty_manifests_directory_fails` executed under `dev/.venv/bin/python`
- Expected: an empty manifests directory fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_an_empty_manifests_directory_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a duplicate detector ref fails
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_a_duplicate_detector_ref_fails` executed under `dev/.venv/bin/python`
- Expected: a duplicate detector ref fails
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_duplicate_detector_ref_fails PASSED` (verbatim from the `-v` node list of this run)

### Scenario: float params survive compilation and reach the evaluator
- Status: EXECUTED
- Input: `backend/tests/test_detector_manifests.py::test_float_params_survive_compilation_and_reach_the_evaluator` executed under `dev/.venv/bin/python`
- Expected: float params survive compilation and reach the evaluator
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_float_params_survive_compilation_and_reach_the_evaluator PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_disposition.py`

### Scenario: a complete close completes
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_complete_close_completes` executed under `dev/.venv/bin/python`
- Expected: a complete close completes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_complete_close_completes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a close without a resolution type does not complete[None]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[None]` executed under `dev/.venv/bin/python`, parameter case `None`
- Expected: a close without a resolution type does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[None] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a close without a resolution type does not complete[]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a close without a resolution type does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_close_without_a_resolution_type_does_not_complete[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a resolution type outside r1 to r6 is refused
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_resolution_type_outside_r1_to_r6_is_refused` executed under `dev/.venv/bin/python`
- Expected: a resolution type outside r1 to r6 is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_resolution_type_outside_r1_to_r6_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the schema itself refuses a disposition with no resolution type
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_schema_itself_refuses_a_disposition_with_no_resolution_type` executed under `dev/.venv/bin/python`
- Expected: AC-F12-01: "a closed item with no resolution type does not exist in the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_schema_itself_refuses_a_disposition_with_no_resolution_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an item can be closed only once
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_an_item_can_be_closed_only_once` executed under `dev/.venv/bin/python`
- Expected: an item can be closed only once
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_an_item_can_be_closed_only_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r1 without an expiry does not complete
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r1_without_an_expiry_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: r1 without an expiry does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r1_without_an_expiry_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r1 with an expiry completes
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r1_with_an_expiry_completes` executed under `dev/.venv/bin/python`
- Expected: r1 with an expiry completes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r1_with_an_expiry_completes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r5 without both an owner and a due date does not complete[evidence0-missing0]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence0-missing0]` executed under `dev/.venv/bin/python`, parameter case `evidence0-missing0`
- Expected: r5 without both an owner and a due date does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence0-missing0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r5 without both an owner and a due date does not complete[evidence1-missing1]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence1-missing1]` executed under `dev/.venv/bin/python`, parameter case `evidence1-missing1`
- Expected: r5 without both an owner and a due date does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence1-missing1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r5 without both an owner and a due date does not complete[evidence2-missing2]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence2-missing2]` executed under `dev/.venv/bin/python`, parameter case `evidence2-missing2`
- Expected: r5 without both an owner and a due date does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r5_without_both_an_owner_and_a_due_date_does_not_complete[evidence2-missing2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r5 with both completes and records them
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r5_with_both_completes_and_records_them` executed under `dev/.venv/bin/python`
- Expected: r5 with both completes and records them
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r5_with_both_completes_and_records_them PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r6 changes the risk grade and auto pass and leaves an audit record
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r6_changes_the_risk_grade_and_auto_pass_and_leaves_an_audit_record` executed under `dev/.venv/bin/python`
- Expected: r6 changes the risk grade and auto pass and leaves an audit record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r6_changes_the_risk_grade_and_auto_pass_and_leaves_an_audit_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r6 without the control state change itself does not complete
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_r6_without_the_control_state_change_itself_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: r6 without the control state change itself does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_r6_without_the_control_state_change_itself_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: revoking auto pass is recordable because false is a held value
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_revoking_auto_pass_is_recordable_because_false_is_a_held_value` executed under `dev/.venv/bin/python`
- Expected: revoking auto pass is recordable because false is a held value
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_revoking_auto_pass_is_recordable_because_false_is_a_held_value PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a close without an expected clearing period does not complete
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_close_without_an_expected_clearing_period_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: a close without an expected clearing period does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_close_without_an_expected_clearing_period_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is a hard failure not a bypassable warning
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_it_is_a_hard_failure_not_a_bypassable_warning` executed under `dev/.venv/bin/python`
- Expected: it is a hard failure not a bypassable warning
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_it_is_a_hard_failure_not_a_bypassable_warning PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the column is not null so the prediction cannot be retrofitted away
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_column_is_not_null_so_the_prediction_cannot_be_retrofitted_away` executed under `dev/.venv/bin/python`
- Expected: the column is not null so the prediction cannot be retrofitted away
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_column_is_not_null_so_the_prediction_cannot_be_retrofitted_away PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period at or before the current period does not save[12]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[12]` executed under `dev/.venv/bin/python`, parameter case `12`
- Expected: a clearing period at or before the current period does not save
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[12] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period at or before the current period does not save[11]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[11]` executed under `dev/.venv/bin/python`, parameter case `11`
- Expected: a clearing period at or before the current period does not save
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[11] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period at or before the current period does not save[0]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[0]` executed under `dev/.venv/bin/python`, parameter case `0`
- Expected: a clearing period at or before the current period does not save
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period at or before the current period does not save[-1]
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[-1]` executed under `dev/.venv/bin/python`, parameter case `-1`
- Expected: a clearing period at or before the current period does not save
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_clearing_period_at_or_before_the_current_period_does_not_save[-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the earliest permitted period saves
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_earliest_permitted_period_saves` executed under `dev/.venv/bin/python`
- Expected: the earliest permitted period saves
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_earliest_permitted_period_saves PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the maximum horizon saves
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_maximum_horizon_saves` executed under `dev/.venv/bin/python`
- Expected: the maximum horizon saves
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_maximum_horizon_saves PASSED` (verbatim from the `-v` node list of this run)

### Scenario: beyond the maximum horizon does not save and states the maximum
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_beyond_the_maximum_horizon_does_not_save_and_states_the_maximum` executed under `dev/.venv/bin/python`
- Expected: beyond the maximum horizon does not save and states the maximum
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_beyond_the_maximum_horizon_does_not_save_and_states_the_maximum PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failed capture write leaves the item open with no disposition
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_failed_capture_write_leaves_the_item_open_with_no_disposition` executed under `dev/.venv/bin/python`
- Expected: AC-F12-07: a disposition is never recorded without its label.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_failed_capture_write_leaves_the_item_open_with_no_disposition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failed r6 state change leaves no partial record
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_failed_r6_state_change_leaves_no_partial_record` executed under `dev/.venv/bin/python`
- Expected: a failed r6 state change leaves no partial record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_failed_r6_state_change_leaves_no_partial_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the capture row cannot outlive its disposition
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_capture_row_cannot_outlive_its_disposition` executed under `dev/.venv/bin/python`
- Expected: the capture row cannot outlive its disposition
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_capture_row_cannot_outlive_its_disposition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a lapsed r1 reopens labelled with its original explanation
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_labelled_with_its_original_explanation` executed under `dev/.venv/bin/python`
- Expected: a lapsed r1 reopens labelled with its original explanation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_labelled_with_its_original_explanation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an r1 inside its expiry does not reopen
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_an_r1_inside_its_expiry_does_not_reopen` executed under `dev/.venv/bin/python`
- Expected: an r1 inside its expiry does not reopen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_an_r1_inside_its_expiry_does_not_reopen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a lapsed r1 reopens only once
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_only_once` executed under `dev/.venv/bin/python`
- Expected: a lapsed r1 reopens only once
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_lapsed_r1_reopens_only_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: other resolution types do not lapse
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_other_resolution_types_do_not_lapse` executed under `dev/.venv/bin/python`
- Expected: other resolution types do not lapse
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_other_resolution_types_do_not_lapse PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the job runs without a user requesting it
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_job_runs_without_a_user_requesting_it` executed under `dev/.venv/bin/python`
- Expected: the job runs without a user requesting it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_job_runs_without_a_user_requesting_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a prediction that cleared is recorded met
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_prediction_that_cleared_is_recorded_met` executed under `dev/.venv/bin/python`
- Expected: a prediction that cleared is recorded met
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_prediction_that_cleared_is_recorded_met PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a prediction that did not clear is recorded missed
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_prediction_that_did_not_clear_is_recorded_missed` executed under `dev/.venv/bin/python`
- Expected: a prediction that did not clear is recorded missed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_prediction_that_did_not_clear_is_recorded_missed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missed prediction raises the risk grade and revokes auto pass
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_missed_prediction_raises_the_risk_grade_and_revokes_auto_pass` executed under `dev/.venv/bin/python`
- Expected: AC-F32-03: an R6 control-state change READABLE ON THE ACCOUNT, rather
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_missed_prediction_raises_the_risk_grade_and_revokes_auto_pass PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a met prediction does not touch the account state
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_met_prediction_does_not_touch_the_account_state` executed under `dev/.venv/bin/python`
- Expected: a met prediction does not touch the account state
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_met_prediction_does_not_touch_the_account_state PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period with nothing due records zero rather than nothing
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_records_zero_rather_than_nothing` executed under `dev/.venv/bin/python`
- Expected: a period with nothing due records zero rather than nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_records_zero_rather_than_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period not yet closed records a deferral and verifies nothing
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_period_not_yet_closed_records_a_deferral_and_verifies_nothing` executed under `dev/.venv/bin/python`
- Expected: a period not yet closed records a deferral and verifies nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_period_not_yet_closed_records_a_deferral_and_verifies_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a deferral does not touch the account state
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_deferral_does_not_touch_the_account_state` executed under `dev/.venv/bin/python`
- Expected: a deferral does not touch the account state
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_deferral_does_not_touch_the_account_state PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a verification result outside the closed set is unstorable
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_verification_result_outside_the_closed_set_is_unstorable` executed under `dev/.venv/bin/python`
- Expected: a verification result outside the closed set is unstorable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_verification_result_outside_the_closed_set_is_unstorable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the hit rate is computed over predictions due
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_hit_rate_is_computed_over_predictions_due` executed under `dev/.venv/bin/python`
- Expected: the hit rate is computed over predictions due
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_hit_rate_is_computed_over_predictions_due PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a bad hit rate is still reported
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_bad_hit_rate_is_still_reported` executed under `dev/.venv/bin/python`
- Expected: a bad hit rate is still reported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_bad_hit_rate_is_still_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period with nothing due has no hit rate rather than one hundred percent
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_has_no_hit_rate_rather_than_one_hundred_percent` executed under `dev/.venv/bin/python`
- Expected: a period with nothing due has no hit rate rather than one hundred percent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_a_period_with_nothing_due_has_no_hit_rate_rather_than_one_hundred_percent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: nothing in this module reaches an erp
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_nothing_in_this_module_reaches_an_erp` executed under `dev/.venv/bin/python`
- Expected: nothing in this module reaches an erp
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_nothing_in_this_module_reaches_an_erp PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the disposition schema has no posting column
- Status: EXECUTED
- Input: `backend/tests/test_disposition.py::test_the_disposition_schema_has_no_posting_column` executed under `dev/.venv/bin/python`
- Expected: the disposition schema has no posting column
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_disposition.py::test_the_disposition_schema_has_no_posting_column PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_emission_gate.py`

### Scenario: an admitted emission comes back and a withheld one does not
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_an_admitted_emission_comes_back_and_a_withheld_one_does_not` executed under `dev/.venv/bin/python`
- Expected: an admitted emission comes back and a withheld one does not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_an_admitted_emission_comes_back_and_a_withheld_one_does_not PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a withheld emission is ABSENT from the response not null
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_a_withheld_emission_is_ABSENT_from_the_response_not_null` executed under `dev/.venv/bin/python`
- Expected: The distinction the criterion turns on.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_a_withheld_emission_is_ABSENT_from_the_response_not_null PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the route refuses a field the emission schema does not declare
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_route_refuses_a_field_the_emission_schema_does_not_declare` executed under `dev/.venv/bin/python`
- Expected: Refused, not ignored. A caller that believes it declared something the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_route_refuses_a_field_the_emission_schema_does_not_declare PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the route refuses an untokened caller
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_route_refuses_an_untokened_caller` executed under `dev/.venv/bin/python`
- Expected: the route refuses an untokened caller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_route_refuses_an_untokened_caller PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the caller cannot name the principal it is judged as
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_caller_cannot_name_the_principal_it_is_judged_as` executed under `dev/.venv/bin/python`
- Expected: `principal_id` inside `context` is overwritten by the authenticated one.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_caller_cannot_name_the_principal_it_is_judged_as PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a capability outside the allowlist is denied
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_a_capability_outside_the_allowlist_is_denied` executed under `dev/.venv/bin/python`
- Expected: a capability outside the allowlist is denied
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_a_capability_outside_the_allowlist_is_denied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: admit returns a new list containing only the admitted
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_admit_returns_a_new_list_containing_only_the_admitted` executed under `dev/.venv/bin/python`
- Expected: admit returns a new list containing only the admitted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_admit_returns_a_new_list_containing_only_the_admitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denial carries the bundle hash a decision id and the failed check
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_a_denial_carries_the_bundle_hash_a_decision_id_and_the_failed_check` executed under `dev/.venv/bin/python`
- Expected: a denial carries the bundle hash a decision id and the failed check
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_a_denial_carries_the_bundle_hash_a_decision_id_and_the_failed_check PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denial does not carry the payload it withheld
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_a_denial_does_not_carry_the_payload_it_withheld` executed under `dev/.venv/bin/python`
- Expected: There is no attribute on a `Denial` holding the thing that was refused.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_a_denial_does_not_carry_the_payload_it_withheld PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the gate fails closed on every way of not reaching the broker[transport0-connection refused]
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport0-connection refused]` executed under `dev/.venv/bin/python`, parameter case `transport0-connection refused`
- Expected: Zero admitted, and a reason — never "admit them, the check was down".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport0-connection refused] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the gate fails closed on every way of not reaching the broker[transport1-refused]
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport1-refused]` executed under `dev/.venv/bin/python`, parameter case `transport1-refused`
- Expected: Zero admitted, and a reason — never "admit them, the check was down".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport1-refused] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the gate fails closed on every way of not reaching the broker[transport2-could not be reached]
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport2-could not be reached]` executed under `dev/.venv/bin/python`, parameter case `transport2-could not be reached`
- Expected: Zero admitted, and a reason — never "admit them, the check was down".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_gate_fails_closed_on_every_way_of_not_reaching_the_broker[transport2-could not be reached] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one broker round trip per candidate so each denial has its own id
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_one_broker_round_trip_per_candidate_so_each_denial_has_its_own_id` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-29` requires a denial retrievable BY ITS OWN decision id. A batch
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_one_broker_round_trip_per_candidate_so_each_denial_has_its_own_id PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the candidate context and payload are separate fields
- Status: EXECUTED
- Input: `backend/tests/test_emission_gate.py::test_the_candidate_context_and_payload_are_separate_fields` executed under `dev/.venv/bin/python`
- Expected: No predicate can be evaluated against renderable prose.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_emission_gate.py::test_the_candidate_context_and_payload_are_separate_fields PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_evaluator_primitives.py`

### Scenario: absent in the target period is an omission
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_absent_in_the_target_period_is_an_omission` executed under `dev/.venv/bin/python`
- Expected: absent in the target period is an omission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_absent_in_the_target_period_is_an_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: present in the target period is not an omission
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_present_in_the_target_period_is_not_an_omission` executed under `dev/.venv/bin/python`
- Expected: present in the target period is not an omission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_present_in_the_target_period_is_not_an_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: present at a wildly different amount is still not an omission
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_present_at_a_wildly_different_amount_is_still_not_an_omission` executed under `dev/.venv/bin/python`
- Expected: present at a wildly different amount is still not an omission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_present_at_a_wildly_different_amount_is_still_not_an_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the expected amount range comes from the history
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_expected_amount_range_comes_from_the_history` executed under `dev/.venv/bin/python`
- Expected: the expected amount range comes from the history
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_expected_amount_range_comes_from_the_history PASSED` (verbatim from the `-v` node list of this run)

### Scenario: multiple lines in one period are summed not counted twice
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_multiple_lines_in_one_period_are_summed_not_counted_twice` executed under `dev/.venv/bin/python`
- Expected: multiple lines in one period are summed not counted twice
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_multiple_lines_in_one_period_are_summed_not_counted_twice PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the minimum history boundary[5-False]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[5-False]` executed under `dev/.venv/bin/python`, parameter case `5-False`
- Expected: the minimum history boundary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[5-False] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the minimum history boundary[6-True]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[6-True]` executed under `dev/.venv/bin/python`, parameter case `6-True`
- Expected: the minimum history boundary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_minimum_history_boundary[6-True] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member with no rows at all is not evaluable rather than omitted
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_a_member_with_no_rows_at_all_is_not_evaluable_rather_than_omitted` executed under `dev/.venv/bin/python`
- Expected: a member with no rows at all is not evaluable rather than omitted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_a_member_with_no_rows_at_all_is_not_evaluable_rather_than_omitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an irregular member grounds no expectation but is evaluable
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_an_irregular_member_grounds_no_expectation_but_is_evaluable` executed under `dev/.venv/bin/python`
- Expected: an irregular member grounds no expectation but is evaluable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_an_irregular_member_grounds_no_expectation_but_is_evaluable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the hit ratio boundary is inclusive of the required value
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_hit_ratio_boundary_is_inclusive_of_the_required_value` executed under `dev/.venv/bin/python`
- Expected: the hit ratio boundary is inclusive of the required value
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_hit_ratio_boundary_is_inclusive_of_the_required_value PASSED` (verbatim from the `-v` node list of this run)

### Scenario: params from the manifest override the defaults
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_params_from_the_manifest_override_the_defaults` executed under `dev/.venv/bin/python`
- Expected: params from the manifest override the defaults
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_params_from_the_manifest_override_the_defaults PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no value in a finding is a float
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_no_value_in_a_finding_is_a_float` executed under `dev/.venv/bin/python`
- Expected: no value in a finding is a float
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_no_value_in_a_finding_is_a_float PASSED` (verbatim from the `-v` node list of this run)

### Scenario: declared members absent from the rows are still assessed
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_declared_members_absent_from_the_rows_are_still_assessed` executed under `dev/.venv/bin/python`
- Expected: declared members absent from the rows are still assessed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_declared_members_absent_from_the_rows_are_still_assessed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absence produces no present anomaly
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_an_absence_produces_no_present_anomaly` executed under `dev/.venv/bin/python`
- Expected: an absence produces no present anomaly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_an_absence_produces_no_present_anomaly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a value far above the range is an anomaly
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_far_above_the_range_is_an_anomaly` executed under `dev/.venv/bin/python`
- Expected: a value far above the range is an anomaly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_a_value_far_above_the_range_is_an_anomaly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a value far below the range is an anomaly
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_far_below_the_range_is_an_anomaly` executed under `dev/.venv/bin/python`
- Expected: a value far below the range is an anomaly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_a_value_far_below_the_range_is_an_anomaly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a value inside the range is not an anomaly
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_a_value_inside_the_range_is_not_an_anomaly` executed under `dev/.venv/bin/python`
- Expected: a value inside the range is not an anomaly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_a_value_inside_the_range_is_not_an_anomaly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold is determinate and exclusive[200-0]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200-0]` executed under `dev/.venv/bin/python`, parameter case `200-0`
- Expected: the threshold is determinate and exclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold is determinate and exclusive[200.01-1]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200.01-1]` executed under `dev/.venv/bin/python`, parameter case `200.01-1`
- Expected: the threshold is determinate and exclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[200.01-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold is determinate and exclusive[199.99-0]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[199.99-0]` executed under `dev/.venv/bin/python`, parameter case `199.99-0`
- Expected: the threshold is determinate and exclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[199.99-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold is determinate and exclusive[50-0]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[50-0]` executed under `dev/.venv/bin/python`, parameter case `50-0`
- Expected: the threshold is determinate and exclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[50-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold is determinate and exclusive[49.99-1]
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[49.99-1]` executed under `dev/.venv/bin/python`, parameter case `49.99-1`
- Expected: the threshold is determinate and exclusive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_is_determinate_and_exclusive[49.99-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every anomaly states the threshold in force
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force` executed under `dev/.venv/bin/python`
- Expected: every anomaly states the threshold in force
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force PASSED` (verbatim from the `-v` node list of this run)

### Scenario: insufficient history is not evaluable here either
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_insufficient_history_is_not_evaluable_here_either` executed under `dev/.venv/bin/python`
- Expected: insufficient history is not evaluable here either
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_insufficient_history_is_not_evaluable_here_either PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the threshold ratio is configurable from the manifest
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_threshold_ratio_is_configurable_from_the_manifest` executed under `dev/.venv/bin/python`
- Expected: the threshold ratio is configurable from the manifest
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_threshold_ratio_is_configurable_from_the_manifest PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no value in an anomaly finding is a float
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_no_value_in_an_anomaly_finding_is_a_float` executed under `dev/.venv/bin/python`
- Expected: no value in an anomaly finding is a float
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_no_value_in_an_anomaly_finding_is_a_float PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two primitives disagree exactly where they should
- Status: EXECUTED
- Input: `backend/tests/test_evaluator_primitives.py::test_the_two_primitives_disagree_exactly_where_they_should` executed under `dev/.venv/bin/python`
- Expected: the two primitives disagree exactly where they should
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evaluator_primitives.py::test_the_two_primitives_disagree_exactly_where_they_should PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_evidence_store.py`

### Scenario: store exposes no update or delete function
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_store_exposes_no_update_or_delete_function` executed under `dev/.venv/bin/python`
- Expected: store exposes no update or delete function
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_store_exposes_no_update_or_delete_function PASSED` (verbatim from the `-v` node list of this run)

### Scenario: first entry of a period links to genesis
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_first_entry_of_a_period_links_to_genesis` executed under `dev/.venv/bin/python`
- Expected: first entry of a period links to genesis
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_first_entry_of_a_period_links_to_genesis PASSED` (verbatim from the `-v` node list of this run)

### Scenario: entries chain within a period
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_entries_chain_within_a_period` executed under `dev/.venv/bin/python`
- Expected: entries chain within a period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_entries_chain_within_a_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: chains are per period and independent
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_chains_are_per_period_and_independent` executed under `dev/.venv/bin/python`
- Expected: chains are per period and independent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_chains_are_per_period_and_independent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty period verifies as ok with zero entries
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_an_empty_period_verifies_as_ok_with_zero_entries` executed under `dev/.venv/bin/python`
- Expected: an empty period verifies as ok with zero entries
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_an_empty_period_verifies_as_ok_with_zero_entries PASSED` (verbatim from the `-v` node list of this run)

### Scenario: head of an empty period is genesis
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_head_of_an_empty_period_is_genesis` executed under `dev/.venv/bin/python`
- Expected: head of an empty period is genesis
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_head_of_an_empty_period_is_genesis PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the content hash is a pure function of the payload
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_content_hash_is_a_pure_function_of_the_payload` executed under `dev/.venv/bin/python`
- Expected: the content hash is a pure function of the payload
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_content_hash_is_a_pure_function_of_the_payload PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[dossier_id]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dossier_id]` executed under `dev/.venv/bin/python`, parameter case `dossier_id`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dossier_id] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[run_id]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[run_id]` executed under `dev/.venv/bin/python`, parameter case `run_id`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[run_id] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[tenant_id]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[tenant_id]` executed under `dev/.venv/bin/python`, parameter case `tenant_id`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[tenant_id] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[period]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[period]` executed under `dev/.venv/bin/python`, parameter case `period`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[period] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[detector_ref]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[detector_ref]` executed under `dev/.venv/bin/python`, parameter case `detector_ref`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[detector_ref] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[population_ref]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[population_ref]` executed under `dev/.venv/bin/python`, parameter case `population_ref`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[population_ref] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[dataset_versions]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dataset_versions]` executed under `dev/.venv/bin/python`, parameter case `dataset_versions`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[dataset_versions] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[registry_hash]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[registry_hash]` executed under `dev/.venv/bin/python`, parameter case `registry_hash`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[registry_hash] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[coverage]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[coverage]` executed under `dev/.venv/bin/python`, parameter case `coverage`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[coverage] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[conclusion]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[conclusion]` executed under `dev/.venv/bin/python`, parameter case `conclusion`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[conclusion] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier missing any required element cannot be persisted[created_at]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[created_at]` executed under `dev/.venv/bin/python`, parameter case `created_at`
- Expected: a dossier missing any required element cannot be persisted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_missing_any_required_element_cannot_be_persisted[created_at] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the refusal is recorded as a control event
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_refusal_is_recorded_as_a_control_event` executed under `dev/.venv/bin/python`
- Expected: the refusal is recorded as a control event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_refusal_is_recorded_as_a_control_event PASSED` (verbatim from the `-v` node list of this run)

### Scenario: update is refused below the application[evidence_entry]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_entry]` executed under `dev/.venv/bin/python`, parameter case `evidence_entry`
- Expected: update is refused below the application
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_entry] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: update is refused below the application[evidence_anchor]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_anchor]` executed under `dev/.venv/bin/python`, parameter case `evidence_anchor`
- Expected: update is refused below the application
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_update_is_refused_below_the_application[evidence_anchor] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: delete is refused below the application[evidence_entry]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_entry]` executed under `dev/.venv/bin/python`, parameter case `evidence_entry`
- Expected: delete is refused below the application
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_entry] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: delete is refused below the application[evidence_anchor]
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_anchor]` executed under `dev/.venv/bin/python`, parameter case `evidence_anchor`
- Expected: delete is refused below the application
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_delete_is_refused_below_the_application[evidence_anchor] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a refused mutation is recorded and retyped
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_refused_mutation_is_recorded_and_retyped` executed under `dev/.venv/bin/python`
- Expected: a refused mutation is recorded and retyped
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_refused_mutation_is_recorded_and_retyped PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unrelated database error is not recorded as a mutation attempt
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_an_unrelated_database_error_is_not_recorded_as_a_mutation_attempt` executed under `dev/.venv/bin/python`
- Expected: an unrelated database error is not recorded as a mutation attempt
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_an_unrelated_database_error_is_not_recorded_as_a_mutation_attempt PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an altered record is identified by name
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_an_altered_record_is_identified_by_name` executed under `dev/.venv/bin/python`
- Expected: an altered record is identified by name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_an_altered_record_is_identified_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: recomputing the content hash forward still breaks the chain
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_recomputing_the_content_hash_forward_still_breaks_the_chain` executed under `dev/.venv/bin/python`
- Expected: recomputing the content hash forward still breaks the chain
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_recomputing_the_content_hash_forward_still_breaks_the_chain PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an anchor covers the chain head
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_an_anchor_covers_the_chain_head` executed under `dev/.venv/bin/python`
- Expected: an anchor covers the chain head
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_an_anchor_covers_the_chain_head PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an anchor over an empty period is refused
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_an_anchor_over_an_empty_period_is_refused` executed under `dev/.venv/bin/python`
- Expected: an anchor over an empty period is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_an_anchor_over_an_empty_period_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a stub anchor is permanently self identifying
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_stub_anchor_is_permanently_self_identifying` executed under `dev/.venv/bin/python`
- Expected: a stub anchor is permanently self identifying
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_stub_anchor_is_permanently_self_identifying PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stub signer verifies its own output and rejects others
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_stub_signer_verifies_its_own_output_and_rejects_others` executed under `dev/.venv/bin/python`
- Expected: the stub signer verifies its own output and rejects others
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_stub_signer_verifies_its_own_output_and_rejects_others PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stub signer refuses to exist in production
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_stub_signer_refuses_to_exist_in_production` executed under `dev/.venv/bin/python`
- Expected: the stub signer refuses to exist in production
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_stub_signer_refuses_to_exist_in_production PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the signer interface exposes no private key accessor
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_signer_interface_exposes_no_private_key_accessor` executed under `dev/.venv/bin/python`
- Expected: the signer interface exposes no private key accessor
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_signer_interface_exposes_no_private_key_accessor PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the archive stub marks every object as unlocked
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_archive_stub_marks_every_object_as_unlocked` executed under `dev/.venv/bin/python`
- Expected: the archive stub marks every object as unlocked
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_archive_stub_marks_every_object_as_unlocked PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the archive interface has no delete method
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_archive_interface_has_no_delete_method` executed under `dev/.venv/bin/python`
- Expected: the archive interface has no delete method
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_archive_interface_has_no_delete_method PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the archive stub refuses to exist in production
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_archive_stub_refuses_to_exist_in_production` executed under `dev/.venv/bin/python`
- Expected: the archive stub refuses to exist in production
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_archive_stub_refuses_to_exist_in_production PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a dossier round trips complete
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_dossier_round_trips_complete` executed under `dev/.venv/bin/python`
- Expected: a dossier round trips complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_dossier_round_trips_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the v1 reader survives the move to v2
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_the_v1_reader_survives_the_move_to_v2` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §23.11: no migration may drop a dossier field, ever.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_v1_reader_survives_the_move_to_v2 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: retention expiry is stamped seven years out
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_retention_expiry_is_stamped_seven_years_out` executed under `dev/.venv/bin/python`
- Expected: retention expiry is stamped seven years out
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_retention_expiry_is_stamped_seven_years_out PASSED` (verbatim from the `-v` node list of this run)

### Scenario: reading an unknown dossier raises
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_reading_an_unknown_dossier_raises` executed under `dev/.venv/bin/python`
- Expected: reading an unknown dossier raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_reading_an_unknown_dossier_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a payload version with no reader refuses rather than partially materialising
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_a_payload_version_with_no_reader_refuses_rather_than_partially_materialising` executed under `dev/.venv/bin/python`
- Expected: a payload version with no reader refuses rather than partially materialising
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_a_payload_version_with_no_reader_refuses_rather_than_partially_materialising PASSED` (verbatim from the `-v` node list of this run)

### Scenario: writing an unknown payload version is refused
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_writing_an_unknown_payload_version_is_refused` executed under `dev/.venv/bin/python`
- Expected: writing an unknown payload version is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_writing_an_unknown_payload_version_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every required key list has a reader
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_every_required_key_list_has_a_reader` executed under `dev/.venv/bin/python`
- Expected: every required key list has a reader
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_every_required_key_list_has_a_reader PASSED` (verbatim from the `-v` node list of this run)

### Scenario: control events route into the append only chain
- Status: EXECUTED
- Input: `backend/tests/test_evidence_store.py::test_control_events_route_into_the_append_only_chain` executed under `dev/.venv/bin/python`
- Expected: control events route into the append only chain
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_control_events_route_into_the_append_only_chain PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_f12_label_source_three_surfaces.py`

### Scenario: all three surfaces render from the same object
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_all_three_surfaces_render_from_the_same_object` executed under `dev/.venv/bin/python`
- Expected: all three surfaces render from the same object
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_all_three_surfaces_render_from_the_same_object PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the three payloads differ only in which surface they name
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_three_payloads_differ_only_in_which_surface_they_name` executed under `dev/.venv/bin/python`
- Expected: If they diverged in anything else, "the label is adjacent on all three"
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_three_payloads_differ_only_in_which_surface_they_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no surface can be rendered without a label source
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_no_surface_can_be_rendered_without_a_label_source` executed under `dev/.venv/bin/python`
- Expected: no surface can be rendered without a label source
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_no_surface_can_be_rendered_without_a_label_source PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen leg renders the label source adjacent to the figure
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_screen_leg_renders_the_label_source_adjacent_to_the_figure` executed under `dev/.venv/bin/python`
- Expected: the screen leg renders the label source adjacent to the figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_screen_leg_renders_the_label_source_adjacent_to_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier leg exists and carries the label source
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_leg_exists_and_carries_the_label_source` executed under `dev/.venv/bin/python`
- Expected: Rendered from the dossier's real route, not from the component.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_leg_exists_and_carries_the_label_source PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier label source is inside the same element as the figure
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_label_source_is_inside_the_same_element_as_the_figure` executed under `dev/.venv/bin/python`
- Expected: "adjacent" — not at the foot of the exhibit.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_label_source_is_inside_the_same_element_as_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier still carries no external reference after the addition
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_still_carries_no_external_reference_after_the_addition` executed under `dev/.venv/bin/python`
- Expected: The exhibit's defining property, re-asserted because this pass added an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_still_carries_no_external_reference_after_the_addition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier figure is the acceptance derived variant and says so
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_figure_is_the_acceptance_derived_variant_and_says_so` executed under `dev/.venv/bin/python`
- Expected: The pilot can only produce this variant, and rendering the flattering
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_dossier_figure_is_the_acceptance_derived_variant_and_says_so PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export leg carries the label source and survives a file
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_export_leg_carries_the_label_source_and_survives_a_file` executed under `dev/.venv/bin/python`
- Expected: the export leg carries the label source and survives a file
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_the_export_leg_carries_the_label_source_and_survives_a_file PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a hand assembled export payload without a label source is refused
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_a_hand_assembled_export_payload_without_a_label_source_is_refused` executed under `dev/.venv/bin/python`
- Expected: The boundary guard, for payloads that did not come from the type.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_a_hand_assembled_export_payload_without_a_label_source_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty label source is refused as firmly as a missing one
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_an_empty_label_source_is_refused_as_firmly_as_a_missing_one` executed under `dev/.venv/bin/python`
- Expected: an empty label source is refused as firmly as a missing one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_an_empty_label_source_is_refused_as_firmly_as_a_missing_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F12 20 the label source is read on screen in a dossier and in an export
- Status: EXECUTED
- Input: `backend/tests/test_f12_label_source_three_surfaces.py::test_AC_F12_20_the_label_source_is_read_on_screen_in_a_dossier_and_in_an_export` executed under `dev/.venv/bin/python`
- Expected: The three surfaces, in one scenario, so the join is not inferred.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_label_source_three_surfaces.py::test_AC_F12_20_the_label_source_is_read_on_screen_in_a_dossier_and_in_an_export PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_f12_precision.py`

### Scenario: a precision figure cannot be constructed without a label source
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_precision_figure_cannot_be_constructed_without_a_label_source` executed under `dev/.venv/bin/python`
- Expected: a precision figure cannot be constructed without a label source
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_precision_figure_cannot_be_constructed_without_a_label_source PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[   ]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[   ]` executed under `dev/.venv/bin/python`, parameter case `   `
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[   ] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[None]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[None]` executed under `dev/.venv/bin/python`, parameter case `None`
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[None] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[7]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[7]` executed under `dev/.venv/bin/python`, parameter case `7`
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[7] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[bad4]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad4]` executed under `dev/.venv/bin/python`, parameter case `bad4`
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad4] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an absent or empty label source is refused[bad5]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad5]` executed under `dev/.venv/bin/python`, parameter case `bad5`
- Expected: an absent or empty label source is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_absent_or_empty_label_source_is_refused[bad5] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source set is closed
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_set_is_closed` executed under `dev/.venv/bin/python`
- Expected: the label source set is closed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_set_is_closed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a figure cannot be relabelled after construction
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_figure_cannot_be_relabelled_after_construction` executed under `dev/.venv/bin/python`
- Expected: a figure cannot be relabelled after construction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_figure_cannot_be_relabelled_after_construction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a label source cannot be attached to an instance that lacks one
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_label_source_cannot_be_attached_to_an_instance_that_lacks_one` executed under `dev/.venv/bin/python`
- Expected: a label source cannot be attached to an instance that lacks one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_label_source_cannot_be_attached_to_an_instance_that_lacks_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the residual hole is demonstrated not asserted away
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_residual_hole_is_demonstrated_not_asserted_away` executed under `dev/.venv/bin/python`
- Expected: Python has no way to stop `object.__new__`. Record what it gets you.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_residual_hole_is_demonstrated_not_asserted_away PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[acceptance_derived-screen]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-screen]` executed under `dev/.venv/bin/python`, parameter case `acceptance_derived-screen`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-screen] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[acceptance_derived-dossier]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-dossier]` executed under `dev/.venv/bin/python`, parameter case `acceptance_derived-dossier`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-dossier] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[acceptance_derived-export]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-export]` executed under `dev/.venv/bin/python`, parameter case `acceptance_derived-export`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[acceptance_derived-export] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[independently_re_performed-screen]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-screen]` executed under `dev/.venv/bin/python`, parameter case `independently_re_performed-screen`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-screen] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[independently_re_performed-dossier]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-dossier]` executed under `dev/.venv/bin/python`, parameter case `independently_re_performed-dossier`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-dossier] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is adjacent to the figure on all three surfaces[independently_re_performed-export]
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-export]` executed under `dev/.venv/bin/python`, parameter case `independently_re_performed-export`
- Expected: the label source is adjacent to the figure on all three surfaces
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_label_source_is_adjacent_to_the_figure_on_all_three_surfaces[independently_re_performed-export] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the three surfaces carry identical provenance
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_three_surfaces_carry_identical_provenance` executed under `dev/.venv/bin/python`
- Expected: the three surfaces carry identical provenance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_three_surfaces_carry_identical_provenance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the acceptance derived statement says what the number actually measures
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_acceptance_derived_statement_says_what_the_number_actually_measures` executed under `dev/.venv/bin/python`
- Expected: the acceptance derived statement says what the number actually measures
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_acceptance_derived_statement_says_what_the_number_actually_measures PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an acceptance derived figure is never promotion evidence
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_never_promotion_evidence` executed under `dev/.venv/bin/python`
- Expected: an acceptance derived figure is never promotion evidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_never_promotion_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: precision is over concluded items only
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_precision_is_over_concluded_items_only` executed under `dev/.venv/bin/python`
- Expected: precision is over concluded items only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_precision_is_over_concluded_items_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period with no conclusions reports none not zero
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_period_with_no_conclusions_reports_none_not_zero` executed under `dev/.venv/bin/python`
- Expected: a period with no conclusions reports none not zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_period_with_no_conclusions_reports_none_not_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a published payload without a label source fails the report
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_published_payload_without_a_label_source_fails_the_report` executed under `dev/.venv/bin/python`
- Expected: a published payload without a label source fails the report
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_published_payload_without_a_label_source_fails_the_report PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a payload carrying no precision at all is not the boundarys business
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business` executed under `dev/.venv/bin/python`
- Expected: a payload carrying no precision at all is not the boundarys business
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_payload_carrying_no_precision_at_all_is_not_the_boundarys_business PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every render passes its own boundary check
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_every_render_passes_its_own_boundary_check` executed under `dev/.venv/bin/python`
- Expected: every render passes its own boundary check
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_every_render_passes_its_own_boundary_check PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the report states each of p1 to p5 individually
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_report_states_each_of_p1_to_p5_individually` executed under `dev/.venv/bin/python`
- Expected: the report states each of p1 to p5 individually
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_report_states_each_of_p1_to_p5_individually PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a report missing a condition cannot be constructed
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_report_missing_a_condition_cannot_be_constructed` executed under `dev/.venv/bin/python`
- Expected: a report missing a condition cannot be constructed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_report_missing_a_condition_cannot_be_constructed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: p1 and p5 are reported not yet evaluable and name the deferral
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_p1_and_p5_are_reported_not_yet_evaluable_and_name_the_deferral` executed under `dev/.venv/bin/python`
- Expected: p1 and p5 are reported not yet evaluable and name the deferral
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_p1_and_p5_are_reported_not_yet_evaluable_and_name_the_deferral PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a caller cannot close the deferral by asserting p1 or p5
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_caller_cannot_close_the_deferral_by_asserting_p1_or_p5` executed under `dev/.venv/bin/python`
- Expected: a caller cannot close the deferral by asserting p1 or p5
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_caller_cannot_close_the_deferral_by_asserting_p1_or_p5 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the report is never ready in this build
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_report_is_never_ready_in_this_build` executed under `dev/.venv/bin/python`
- Expected: The consequence of the deferral, stated as a test.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_report_is_never_ready_in_this_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: readiness is computed from the conditions and never from precision
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_readiness_is_computed_from_the_conditions_and_never_from_precision` executed under `dev/.venv/bin/python`
- Expected: readiness is computed from the conditions and never from precision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_readiness_is_computed_from_the_conditions_and_never_from_precision PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no precision value moves readiness
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_no_precision_value_moves_readiness` executed under `dev/.venv/bin/python`
- Expected: no precision value moves readiness
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_no_precision_value_moves_readiness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: readiness does not read the figure at all
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_readiness_does_not_read_the_figure_at_all` executed under `dev/.venv/bin/python`
- Expected: Reflective: `ready` must not touch `self.figure`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_readiness_does_not_read_the_figure_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an acceptance derived figure is refused as promotion evidence
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_refused_as_promotion_evidence` executed under `dev/.venv/bin/python`
- Expected: an acceptance derived figure is refused as promotion evidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_acceptance_derived_figure_is_refused_as_promotion_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a short evidence window reports not yet evaluable not not met
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_short_evidence_window_reports_not_yet_evaluable_not_not_met` executed under `dev/.venv/bin/python`
- Expected: a short evidence window reports not yet evaluable not not met
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_short_evidence_window_reports_not_yet_evaluable_not_not_met PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the minimum window is three closed periods
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_minimum_window_is_three_closed_periods` executed under `dev/.venv/bin/python`
- Expected: the minimum window is three closed periods
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_minimum_window_is_three_closed_periods PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failed condition is not met and carries its reason
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_failed_condition_is_not_met_and_carries_its_reason` executed under `dev/.venv/bin/python`
- Expected: a failed condition is not met and carries its reason
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_failed_condition_is_not_met_and_carries_its_reason PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the statement names every blocking condition
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_the_statement_names_every_blocking_condition` executed under `dev/.venv/bin/python`
- Expected: the statement names every blocking condition
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_the_statement_names_every_blocking_condition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a report with all five met is ready so the property is not vacuous
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_a_report_with_all_five_met_is_ready_so_the_property_is_not_vacuous` executed under `dev/.venv/bin/python`
- Expected: a report with all five met is ready so the property is not vacuous
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_a_report_with_all_five_met_is_ready_so_the_property_is_not_vacuous PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown condition state is refused
- Status: EXECUTED
- Input: `backend/tests/test_f12_precision.py::test_an_unknown_condition_state_is_refused` executed under `dev/.venv/bin/python`
- Expected: an unknown condition state is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f12_precision.py::test_an_unknown_condition_state_is_refused PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_f26_fidelity.py`

### Scenario: AC F26 01 the output lists exactly the seeded divergences
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_the_output_lists_exactly_the_seeded_divergences` executed under `dev/.venv/bin/python`
- Expected: AC F26 01 the output lists exactly the seeded divergences
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_the_output_lists_exactly_the_seeded_divergences PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 01 each divergence names account amount and direction
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_each_divergence_names_account_amount_and_direction` executed under `dev/.venv/bin/python`
- Expected: AC F26 01 each divergence names account amount and direction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_01_each_divergence_names_account_amount_and_direction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 02 each divergence is attributed to a balance segment and period
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_each_divergence_is_attributed_to_a_balance_segment_and_period` executed under `dev/.venv/bin/python`
- Expected: AC F26 02 each divergence is attributed to a balance segment and period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_each_divergence_is_attributed_to_a_balance_segment_and_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 02 the run reports the totals it compared on each side
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_the_run_reports_the_totals_it_compared_on_each_side` executed under `dev/.venv/bin/python`
- Expected: AC F26 02 the run reports the totals it compared on each side
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_02_the_run_reports_the_totals_it_compared_on_each_side PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 03 a tying fixture produces a stated zero at full coverage
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_a_tying_fixture_produces_a_stated_zero_at_full_coverage` executed under `dev/.venv/bin/python`
- Expected: AC F26 03 a tying fixture produces a stated zero at full coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_a_tying_fixture_produces_a_stated_zero_at_full_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 03 the zero conclusion is a full population conclusion
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_the_zero_conclusion_is_a_full_population_conclusion` executed under `dev/.venv/bin/python`
- Expected: The TYPE carries it, not a wording choice.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_03_the_zero_conclusion_is_a_full_population_conclusion PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 04 the missing batch names its schedule and its population
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_04_the_missing_batch_names_its_schedule_and_its_population` executed under `dev/.venv/bin/python`
- Expected: AC F26 04 the missing batch names its schedule and its population
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_04_the_missing_batch_names_its_schedule_and_its_population PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the staleness leg states that it cannot express close relative staleness
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness` executed under `dev/.venv/bin/python`
- Expected: `AC-F26-05` IS NOT SATISFIED BY THIS BUILD — do not map it here.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 06 an unavailable control extract reports not run and names it
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_an_unavailable_control_extract_reports_not_run_and_names_it` executed under `dev/.venv/bin/python`
- Expected: AC F26 06 an unavailable control extract reports not run and names it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_an_unavailable_control_extract_reports_not_run_and_names_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 06 a leg that did not run reports no coverage figure
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_a_leg_that_did_not_run_reports_no_coverage_figure` executed under `dev/.venv/bin/python`
- Expected: "...and it does NOT report zero divergences or any coverage figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_06_a_leg_that_did_not_run_reports_no_coverage_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a refused run is distinguishable from a run that started and died
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_a_refused_run_is_distinguishable_from_a_run_that_started_and_died` executed under `dev/.venv/bin/python`
- Expected: `AC-F29-09`'s shape, applied to F26: no declared population means the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_a_refused_run_is_distinguishable_from_a_run_that_started_and_died PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 07 a complete f26 run makes zero model calls
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_07_a_complete_f26_run_makes_zero_model_calls` executed under `dev/.venv/bin/python`
- Expected: The observed count over an F26 run, not over some other detector.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_07_a_complete_f26_run_makes_zero_model_calls PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a model call from inside an f26 run would raise
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_a_model_call_from_inside_an_f26_run_would_raise` executed under `dev/.venv/bin/python`
- Expected: The runtime assertion `PLAN` §11.A criterion 4 asks for.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_a_model_call_from_inside_an_f26_run_would_raise PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 08 the smallest unit divergence is reported exactly
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_08_the_smallest_unit_divergence_is_reported_exactly` executed under `dev/.venv/bin/python`
- Expected: AC F26 08 the smallest unit divergence is reported exactly
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_08_the_smallest_unit_divergence_is_reported_exactly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 09 the earliest and latest period divergences are both reported
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_09_the_earliest_and_latest_period_divergences_are_both_reported` executed under `dev/.venv/bin/python`
- Expected: AC F26 09 the earliest and latest period divergences are both reported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_09_the_earliest_and_latest_period_divergences_are_both_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 10 the fidelity findings are visible on the exceptions screen
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen` executed under `dev/.venv/bin/python`
- Expected: Rendered from `/`, following real links, never by calling the region.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_fidelity_findings_are_visible_on_the_exceptions_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F26 10 the coverage statement is on the same screen
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_coverage_statement_is_on_the_same_screen` executed under `dev/.venv/bin/python`
- Expected: AC F26 10 the coverage statement is on the same screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_AC_F26_10_the_coverage_statement_is_on_the_same_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the exceptions screen is reachable from the entry point
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_the_exceptions_screen_is_reachable_from_the_entry_point` executed under `dev/.venv/bin/python`
- Expected: The traversal, not the URL. A region on a screen nobody can walk to is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_the_exceptions_screen_is_reachable_from_the_entry_point PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the missing batch and the absent close clock are both on the screen
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: the missing batch and the absent close clock are both on the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the totals compared on each side are rendered
- Status: EXECUTED
- Input: `backend/tests/test_f26_fidelity.py::test_the_totals_compared_on_each_side_are_rendered` executed under `dev/.venv/bin/python`
- Expected: the totals compared on each side are rendered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f26_fidelity.py::test_the_totals_compared_on_each_side_are_rendered PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_f33_backtest.py`

### Scenario: precision and recall are numeric values
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_precision_and_recall_are_numeric_values` executed under `dev/.venv/bin/python`
- Expected: The ARITHMETIC of the schema — two of three, and two of four.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_precision_and_recall_are_numeric_values PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the record names the held out period label count and both versions
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_the_record_names_the_held_out_period_label_count_and_both_versions` executed under `dev/.venv/bin/python`
- Expected: the record names the held out period label count and both versions
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_the_record_names_the_held_out_period_label_count_and_both_versions PASSED` (verbatim from the `-v` node list of this run)

### Scenario: precision is none rather than one when nothing was predicted
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_precision_is_none_rather_than_one_when_nothing_was_predicted` executed under `dev/.venv/bin/python`
- Expected: A detector that proposed nothing was not right about everything.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_precision_is_none_rather_than_one_when_nothing_was_predicted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a record with no label is invalid and raises
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_record_with_no_label_is_invalid_and_raises` executed under `dev/.venv/bin/python`
- Expected: a record with no label is invalid and raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_record_with_no_label_is_invalid_and_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a record with a whitespace label is invalid
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_record_with_a_whitespace_label_is_invalid` executed under `dev/.venv/bin/python`
- Expected: a record with a whitespace label is invalid
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_record_with_a_whitespace_label_is_invalid PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a label that does not carry the meaning is invalid
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_label_that_does_not_carry_the_meaning_is_invalid` executed under `dev/.venv/bin/python`
- Expected: The clause that matters: a paraphrase drifts, and the paraphrase that
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_label_that_does_not_carry_the_meaning_is_invalid PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a label that drops the unknown clause is invalid
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_label_that_drops_the_unknown_clause_is_invalid` executed under `dev/.venv/bin/python`
- Expected: a label that drops the unknown clause is invalid
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_label_that_drops_the_unknown_clause_is_invalid PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the default label is the module constant
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_the_default_label_is_the_module_constant` executed under `dev/.venv/bin/python`
- Expected: the default label is the module constant
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_the_default_label_is_the_module_constant PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label travels in the payload beside the recall figure
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_the_label_travels_in_the_payload_beside_the_recall_figure` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-08`'s cheapest guarantee: one payload, read by three surfaces.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_the_label_travels_in_the_payload_beside_the_recall_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a held out period with no labels emits no figures
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_held_out_period_with_no_labels_emits_no_figures` executed under `dev/.venv/bin/python`
- Expected: a held out period with no labels emits no figures
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_held_out_period_with_no_labels_emits_no_figures PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a no labels result says which period and why
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_no_labels_result_says_which_period_and_why` executed under `dev/.venv/bin/python`
- Expected: a no labels result says which period and why
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_no_labels_result_says_which_period_and_why PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a record cannot be constructed with zero labels at all
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_record_cannot_be_constructed_with_zero_labels_at_all` executed under `dev/.venv/bin/python`
- Expected: The direct route to a perfect score, closed at the constructor.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_record_cannot_be_constructed_with_zero_labels_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one label produces figures carrying a label count of one
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_one_label_produces_figures_carrying_a_label_count_of_one` executed under `dev/.venv/bin/python`
- Expected: "so the figures cannot be read as more evidenced than they are".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_one_label_produces_figures_carrying_a_label_count_of_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unretrievable label set emits no accuracy claim of any kind
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_an_unretrievable_label_set_emits_no_accuracy_claim_of_any_kind` executed under `dev/.venv/bin/python`
- Expected: an unretrievable label set emits no accuracy claim of any kind
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_an_unretrievable_label_set_emits_no_accuracy_claim_of_any_kind PASSED` (verbatim from the `-v` node list of this run)

### Scenario: could not run is a different type from no labels
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_could_not_run_is_a_different_type_from_no_labels` executed under `dev/.venv/bin/python`
- Expected: "we looked and there were none" and "we could not look" are different
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_could_not_run_is_a_different_type_from_no_labels PASSED` (verbatim from the `-v` node list of this run)

### Scenario: neither refusal type can be read as a zero
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_neither_refusal_type_can_be_read_as_a_zero` executed under `dev/.venv/bin/python`
- Expected: neither refusal type can be read as a zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_neither_refusal_type_can_be_read_as_a_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: duplicate predictions are counted once
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_duplicate_predictions_are_counted_once` executed under `dev/.venv/bin/python`
- Expected: duplicate predictions are counted once
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_duplicate_predictions_are_counted_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a prediction outside the label set lowers precision not recall
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_a_prediction_outside_the_label_set_lowers_precision_not_recall` executed under `dev/.venv/bin/python`
- Expected: a prediction outside the label set lowers precision not recall
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_a_prediction_outside_the_label_set_lowers_precision_not_recall PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the ratios are decimal quantised not floats
- Status: EXECUTED
- Input: `backend/tests/test_f33_backtest.py::test_the_ratios_are_decimal_quantised_not_floats` executed under `dev/.venv/bin/python`
- Expected: the ratios are decimal quantised not floats
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f33_backtest.py::test_the_ratios_are_decimal_quantised_not_floats PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_f36_47_abstention_on_three_surfaces.py`

### Scenario: the screen reports the abstention count beside the precision figure
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_screen_reports_the_abstention_count_beside_the_precision_figure` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's surface clause, screen leg.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_screen_reports_the_abstention_count_beside_the_precision_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screens third figure is beside the figure not below the card
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_screens_third_figure_is_beside_the_figure_not_below_the_card` executed under `dev/.venv/bin/python`
- Expected: "alongside it". A count in a different card is a count read separately,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_screens_third_figure_is_beside_the_figure_not_below_the_card PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every dossier reports the abstention count beside the figure
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_every_dossier_reports_the_abstention_count_beside_the_figure` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's surface clause, dossier leg — EVERY dossier.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_every_dossier_reports_the_abstention_count_beside_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier third figure is inside the same element as the figure
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_dossier_third_figure_is_inside_the_same_element_as_the_figure` executed under `dev/.venv/bin/python`
- Expected: the dossier third figure is inside the same element as the figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_dossier_third_figure_is_inside_the_same_element_as_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier carries no external reference after this addition
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_dossier_carries_no_external_reference_after_this_addition` executed under `dev/.venv/bin/python`
- Expected: Re-asserted because this pass added an element to the exhibit. A dossier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_dossier_carries_no_external_reference_after_this_addition PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export payload carries the abstention count through a file
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_export_payload_carries_the_abstention_count_through_a_file` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's surface clause, export leg.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_export_payload_carries_the_abstention_count_through_a_file PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the journal export file carries no quality figure at all
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_journal_export_file_carries_no_quality_figure_at_all` executed under `dev/.venv/bin/python`
- Expected: The one artefact this product actually hands over.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_the_journal_export_file_carries_no_quality_figure_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every precision figure on every reachable screen carries its count
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_every_precision_figure_on_every_reachable_screen_carries_its_count` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's surface clause, "on every screen".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_every_precision_figure_on_every_reachable_screen_carries_its_count PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no screen anywhere renders the forbidden denominator
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_no_screen_anywhere_renders_the_forbidden_denominator` executed under `dev/.venv/bin/python`
- Expected: The negative control, over the served markup of every reachable screen.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_no_screen_anywhere_renders_the_forbidden_denominator PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no automation rate figure is rendered on any surface so that half is vacuous
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_no_automation_rate_figure_is_rendered_on_any_surface_so_that_half_is_vacuous` executed under `dev/.venv/bin/python`
- Expected: THIS SCENARIO ESTABLISHES AN ABSENCE, NOT A PROPERTY.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_no_automation_rate_figure_is_rendered_on_any_surface_so_that_half_is_vacuous PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F36 47 the precision figure is read on screen in a dossier and in an export
- Status: EXECUTED
- Input: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_AC_F36_47_the_precision_figure_is_read_on_screen_in_a_dossier_and_in_an_export` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-F36-47's surface clause, all three surfaces in one scenario, so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_f36_47_abstention_on_three_surfaces.py::test_AC_F36_47_the_precision_figure_is_read_on_screen_in_a_dossier_and_in_an_export PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_fixture_and_warehouse.py`

### Scenario: generation is deterministic for a seed
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_generation_is_deterministic_for_a_seed` executed under `dev/.venv/bin/python`
- Expected: generation is deterministic for a seed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_generation_is_deterministic_for_a_seed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a different seed gives different amounts
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_a_different_seed_gives_different_amounts` executed under `dev/.venv/bin/python`
- Expected: a different seed gives different amounts
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_a_different_seed_gives_different_amounts PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rent accrual posts in periods 1 to 11 and is absent in 12
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_rent_accrual_posts_in_periods_1_to_11_and_is_absent_in_12` executed under `dev/.venv/bin/python`
- Expected: the rent accrual posts in periods 1 to 11 and is absent in 12
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_rent_accrual_posts_in_periods_1_to_11_and_is_absent_in_12 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the insurance accrual posts in all twelve periods
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_insurance_accrual_posts_in_all_twelve_periods` executed under `dev/.venv/bin/python`
- Expected: the insurance accrual posts in all twelve periods
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_insurance_accrual_posts_in_all_twelve_periods PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the utilities accrual is present in period 12 but far above its history
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_utilities_accrual_is_present_in_period_12_but_far_above_its_history` executed under `dev/.venv/bin/python`
- Expected: the utilities accrual is present in period 12 but far above its history
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_utilities_accrual_is_present_in_period_12_but_far_above_its_history PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bonus accrual has less than six periods of history
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_bonus_accrual_has_less_than_six_periods_of_history` executed under `dev/.venv/bin/python`
- Expected: the bonus accrual has less than six periods of history
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_bonus_accrual_has_less_than_six_periods_of_history PASSED` (verbatim from the `-v` node list of this run)

### Scenario: injection payloads are planted in line descriptions
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_injection_payloads_are_planted_in_line_descriptions` executed under `dev/.venv/bin/python`
- Expected: injection payloads are planted in line descriptions
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_injection_payloads_are_planted_in_line_descriptions PASSED` (verbatim from the `-v` node list of this run)

### Scenario: personal data columns are populated
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_personal_data_columns_are_populated` executed under `dev/.venv/bin/python`
- Expected: personal data columns are populated
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_personal_data_columns_are_populated PASSED` (verbatim from the `-v` node list of this run)

### Scenario: amounts are decimal strings never floats
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_amounts_are_decimal_strings_never_floats` executed under `dev/.venv/bin/python`
- Expected: amounts are decimal strings never floats
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_amounts_are_decimal_strings_never_floats PASSED` (verbatim from the `-v` node list of this run)

### Scenario: balances are derived from the lines
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_balances_are_derived_from_the_lines` executed under `dev/.venv/bin/python`
- Expected: balances are derived from the lines
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_balances_are_derived_from_the_lines PASSED` (verbatim from the `-v` node list of this run)

### Scenario: background traffic exists so recurring members are not the whole ledger
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_background_traffic_exists_so_recurring_members_are_not_the_whole_ledger` executed under `dev/.venv/bin/python`
- Expected: background traffic exists so recurring members are not the whole ledger
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_background_traffic_exists_so_recurring_members_are_not_the_whole_ledger PASSED` (verbatim from the `-v` node list of this run)

### Scenario: seeding is idempotent
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_seeding_is_idempotent` executed under `dev/.venv/bin/python`
- Expected: seeding is idempotent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_seeding_is_idempotent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the read connection refuses a write
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_read_connection_refuses_a_write` executed under `dev/.venv/bin/python`
- Expected: the read connection refuses a write
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_read_connection_refuses_a_write PASSED` (verbatim from the `-v` node list of this run)

### Scenario: fetch binds parameters
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_fetch_binds_parameters` executed under `dev/.venv/bin/python`
- Expected: fetch binds parameters
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_fetch_binds_parameters PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no warehouse without a credential
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_no_warehouse_without_a_credential` executed under `dev/.venv/bin/python`
- Expected: no warehouse without a credential
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_no_warehouse_without_a_credential PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the warehouse credential cannot be resolved from the api process
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_the_warehouse_credential_cannot_be_resolved_from_the_api_process` executed under `dev/.venv/bin/python`
- Expected: the warehouse credential cannot be resolved from the api process
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_the_warehouse_credential_cannot_be_resolved_from_the_api_process PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a non sqlite dsn is refused rather than half supported
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_a_non_sqlite_dsn_is_refused_rather_than_half_supported` executed under `dev/.venv/bin/python`
- Expected: a non sqlite dsn is refused rather than half supported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_a_non_sqlite_dsn_is_refused_rather_than_half_supported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: from credential builds a usable warehouse
- Status: EXECUTED
- Input: `backend/tests/test_fixture_and_warehouse.py::test_from_credential_builds_a_usable_warehouse` executed under `dev/.venv/bin/python`
- Expected: from credential builds a usable warehouse
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fixture_and_warehouse.py::test_from_credential_builds_a_usable_warehouse PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_fsm_emission_leg.py`

### Scenario: the emission leg is actually reachable before anything is claimed about it
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_is_actually_reachable_before_anything_is_claimed_about_it` executed under `dev/.venv/bin/python`
- Expected: the emission leg is actually reachable before anything is claimed about it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_is_actually_reachable_before_anything_is_claimed_about_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: override is not in the forward closure of any emission state
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_override_is_not_in_the_forward_closure_of_any_emission_state` executed under `dev/.venv/bin/python`
- Expected: override is not in the forward closure of any emission state
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_override_is_not_in_the_forward_closure_of_any_emission_state PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no emission state is an ancestor of override
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_no_emission_state_is_an_ancestor_of_override` executed under `dev/.venv/bin/python`
- Expected: no emission state is an ancestor of override
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_no_emission_state_is_an_ancestor_of_override PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every whole path that touches the emission leg avoids override
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_every_whole_path_that_touches_the_emission_leg_avoids_override` executed under `dev/.venv/bin/python`
- Expected: every whole path that touches the emission leg avoids override
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_every_whole_path_that_touches_the_emission_leg_avoids_override PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the emission leg reaches abstained and the action leg does not
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_reaches_abstained_and_the_action_leg_does_not` executed under `dev/.venv/bin/python`
- Expected: the emission leg reaches abstained and the action leg does not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_the_emission_leg_reaches_abstained_and_the_action_leg_does_not PASSED` (verbatim from the `-v` node list of this run)

### Scenario: abstained is terminal and cannot be resumed into an override
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_abstained_is_terminal_and_cannot_be_resumed_into_an_override` executed under `dev/.venv/bin/python`
- Expected: abstained is terminal and cannot be resumed into an override
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_abstained_is_terminal_and_cannot_be_resumed_into_an_override PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the declared emission transitions are the only ones out of the leg
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_declared_emission_transitions_are_the_only_ones_out_of_the_leg` executed under `dev/.venv/bin/python`
- Expected: the declared emission transitions are the only ones out of the leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_the_declared_emission_transitions_are_the_only_ones_out_of_the_leg PASSED` (verbatim from the `-v` node list of this run)

### Scenario: terminal states map to distinct outcome values
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_terminal_states_map_to_distinct_outcome_values` executed under `dev/.venv/bin/python`
- Expected: terminal states map to distinct outcome values
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_terminal_states_map_to_distinct_outcome_values PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an abstention and a denial are separate rows with separate outcomes
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_an_abstention_and_a_denial_are_separate_rows_with_separate_outcomes` executed under `dev/.venv/bin/python`
- Expected: an abstention and a denial are separate rows with separate outcomes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_an_abstention_and_a_denial_are_separate_rows_with_separate_outcomes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the outcome column admits abstain as a peer of deny not as a reason string
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_the_outcome_column_admits_abstain_as_a_peer_of_deny_not_as_a_reason_string` executed under `dev/.venv/bin/python`
- Expected: the outcome column admits abstain as a peer of deny not as a reason string
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_the_outcome_column_admits_abstain_as_a_peer_of_deny_not_as_a_reason_string PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denial count over a period excludes abstentions
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_a_denial_count_over_a_period_excludes_abstentions` executed under `dev/.venv/bin/python`
- Expected: a denial count over a period excludes abstentions
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_a_denial_count_over_a_period_excludes_abstentions PASSED` (verbatim from the `-v` node list of this run)

### Scenario: abstentions survive the mirror into the evidence chain as abstentions
- Status: EXECUTED
- Input: `backend/tests/test_fsm_emission_leg.py::test_abstentions_survive_the_mirror_into_the_evidence_chain_as_abstentions` executed under `dev/.venv/bin/python`
- Expected: abstentions survive the mirror into the evidence chain as abstentions
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_fsm_emission_leg.py::test_abstentions_survive_the_mirror_into_the_evidence_chain_as_abstentions PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ges_decide_route.py`

### Scenario: the route is on the ges surface and the health report names it
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_route_is_on_the_ges_surface_and_the_health_report_names_it` executed under `dev/.venv/bin/python`
- Expected: the route is on the ges surface and the health report names it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_route_is_on_the_ges_surface_and_the_health_report_names_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an allowed action comes back as an allow with a decision id
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_allowed_action_comes_back_as_an_allow_with_a_decision_id` executed under `dev/.venv/bin/python`
- Expected: an allowed action comes back as an allow with a decision id
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_allowed_action_comes_back_as_an_allow_with_a_decision_id PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a denial is a two hundred carrying the reason not an http error
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_a_denial_is_a_two_hundred_carrying_the_reason_not_an_http_error` executed under `dev/.venv/bin/python`
- Expected: The asymmetry with `/ges/query` is the point. A refused query has no
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_a_denial_is_a_two_hundred_carrying_the_reason_not_an_http_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the client refuses to read a non two hundred as a denial
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_client_refuses_to_read_a_non_two_hundred_as_a_denial` executed under `dev/.venv/bin/python`
- Expected: A transport failure must never surface as "the broker said no".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_client_refuses_to_read_a_non_two_hundred_as_a_denial PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown principal is refused rather than defaulted
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_unknown_principal_is_refused_rather_than_defaulted` executed under `dev/.venv/bin/python`
- Expected: an unknown principal is refused rather than defaulted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_unknown_principal_is_refused_rather_than_defaulted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the route requires the loopback client token
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_route_requires_the_loopback_client_token` executed under `dev/.venv/bin/python`
- Expected: the route requires the loopback client token
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_route_requires_the_loopback_client_token PASSED` (verbatim from the `-v` node list of this run)

### Scenario: naming someone else as the approver is refused as impersonation
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_naming_someone_else_as_the_approver_is_refused_as_impersonation` executed under `dev/.venv/bin/python`
- Expected: naming someone else as the approver is refused as impersonation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_naming_someone_else_as_the_approver_is_refused_as_impersonation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an agent asking to approve is denied before any rule runs
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_agent_asking_to_approve_is_denied_before_any_rule_runs` executed under `dev/.venv/bin/python`
- Expected: an agent asking to approve is denied before any rule runs
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_agent_asking_to_approve_is_denied_before_any_rule_runs PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approval within the limit is allowed
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_within_the_limit_is_allowed` executed under `dev/.venv/bin/python`
- Expected: an approval within the limit is allowed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_approval_within_the_limit_is_allowed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approval above the limit is denied and is override eligible
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_above_the_limit_is_denied_and_is_override_eligible` executed under `dev/.venv/bin/python`
- Expected: an approval above the limit is denied and is override eligible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_approval_above_the_limit_is_denied_and_is_override_eligible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approval exactly at the limit is allowed because the rule is inclusive
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_approval_exactly_at_the_limit_is_allowed_because_the_rule_is_inclusive` executed under `dev/.venv/bin/python`
- Expected: `AC-F36-16`: the boundary behaviour is the one displayed at approval
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_approval_exactly_at_the_limit_is_allowed_because_the_rule_is_inclusive PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an identity denial is not override eligible
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_identity_denial_is_not_override_eligible` executed under `dev/.venv/bin/python`
- Expected: The approver is also the invoker. This must never be waivable — it is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_identity_denial_is_not_override_eligible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override presented against an ineligible denial is refused at the broker
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_override_presented_against_an_ineligible_denial_is_refused_at_the_broker` executed under `dev/.venv/bin/python`
- Expected: Not "the UI does not offer the control" — `AC-F36-03` requires the same
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_override_presented_against_an_ineligible_denial_is_refused_at_the_broker PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override against an eligible denial is consumed exactly once
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_an_override_against_an_eligible_denial_is_consumed_exactly_once` executed under `dev/.venv/bin/python`
- Expected: an override against an eligible denial is consumed exactly once
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_an_override_against_an_eligible_denial_is_consumed_exactly_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reason code outside the closed list is refused
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_a_reason_code_outside_the_closed_list_is_refused` executed under `dev/.venv/bin/python`
- Expected: a reason code outside the closed list is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_a_reason_code_outside_the_closed_list_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the second authoriser may not be the requester
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_second_authoriser_may_not_be_the_requester` executed under `dev/.venv/bin/python`
- Expected: the second authoriser may not be the requester
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_second_authoriser_may_not_be_the_requester PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bundle endpoint serves the closed reason list so no ui holds one
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_serves_the_closed_reason_list_so_no_ui_holds_one` executed under `dev/.venv/bin/python`
- Expected: the bundle endpoint serves the closed reason list so no ui holds one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_serves_the_closed_reason_list_so_no_ui_holds_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bundle endpoint exposes no rule source and no secret
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_exposes_no_rule_source_and_no_secret` executed under `dev/.venv/bin/python`
- Expected: A bundle *state* summary, not the bundle source. The compiled predicate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_bundle_endpoint_exposes_no_rule_source_and_no_secret PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the decide route has no field that could carry a statement
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_the_decide_route_has_no_field_that_could_carry_a_statement` executed under `dev/.venv/bin/python`
- Expected: the decide route has no field that could carry a statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_the_decide_route_has_no_field_that_could_carry_a_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql string smuggled through the payload reaches no evaluator
- Status: EXECUTED
- Input: `backend/tests/test_ges_decide_route.py::test_a_sql_string_smuggled_through_the_payload_reaches_no_evaluator` executed under `dev/.venv/bin/python`
- Expected: `payload` is a mapping bound to the declared action context schema. A key
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ges_decide_route.py::test_a_sql_string_smuggled_through_the_payload_reaches_no_evaluator PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_journal_attribute_outlier.py`

### Scenario: each scored attribute is detected on its own[kwargs0-rare_source_for_account]
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs0-rare_source_for_account]` executed under `dev/.venv/bin/python`, parameter case `kwargs0-rare_source_for_account`
- Expected: One attribute at a time, with `min_attributes=1` so the detection is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs0-rare_source_for_account] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each scored attribute is detected on its own[kwargs1-round_amount]
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs1-round_amount]` executed under `dev/.venv/bin/python`, parameter case `kwargs1-round_amount`
- Expected: One attribute at a time, with `min_attributes=1` so the detection is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs1-round_amount] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each scored attribute is detected on its own[kwargs2-unusual_posting_hour]
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs2-unusual_posting_hour]` executed under `dev/.venv/bin/python`, parameter case `kwargs2-unusual_posting_hour`
- Expected: One attribute at a time, with `min_attributes=1` so the detection is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs2-unusual_posting_hour] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each scored attribute is detected on its own[kwargs3-weekend_posting]
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs3-weekend_posting]` executed under `dev/.venv/bin/python`, parameter case `kwargs3-weekend_posting`
- Expected: One attribute at a time, with `min_attributes=1` so the detection is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_each_scored_attribute_is_detected_on_its_own[kwargs3-weekend_posting] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an ordinary journal carries no attribute at all
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_an_ordinary_journal_carries_no_attribute_at_all` executed under `dev/.venv/bin/python`
- Expected: an ordinary journal carries no attribute at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_an_ordinary_journal_carries_no_attribute_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: magnitude is not scored
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_magnitude_is_not_scored` executed under `dev/.venv/bin/python`
- Expected: The header's claim, asserted. A very large but non-round amount from the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_magnitude_is_not_scored PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a journal exactly at the threshold is reported
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_exactly_at_the_threshold_is_reported` executed under `dev/.venv/bin/python`
- Expected: Inclusivity is declared as inclusive, so AT the threshold fires.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_exactly_at_the_threshold_is_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a journal one below the threshold is not reported
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_one_below_the_threshold_is_not_reported` executed under `dev/.venv/bin/python`
- Expected: a journal one below the threshold is not reported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_one_below_the_threshold_is_not_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every finding states the threshold in force and the attributes scored
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_every_finding_states_the_threshold_in_force_and_the_attributes_scored` executed under `dev/.venv/bin/python`
- Expected: every finding states the threshold in force and the attributes scored
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_every_finding_states_the_threshold_in_force_and_the_attributes_scored PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every finding carries the uncalibrated threshold denial
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_every_finding_carries_the_uncalibrated_threshold_denial` executed under `dev/.venv/bin/python`
- Expected: Register 30's in-file denial, on the artefact rather than only in the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_every_finding_carries_the_uncalibrated_threshold_denial PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a journal cannot dilute its own rarity
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_cannot_dilute_its_own_rarity` executed under `dev/.venv/bin/python`
- Expected: One MANUAL journal in a period whose history has none is rare, however
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_journal_cannot_dilute_its_own_rarity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: rarity is measured per account not across the ledger
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_rarity_is_measured_per_account_not_across_the_ledger` executed under `dev/.venv/bin/python`
- Expected: MANUAL being routine on one account says nothing about another.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_rarity_is_measured_per_account_not_across_the_ledger PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a common source is not rare
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_common_source_is_not_rare` executed under `dev/.venv/bin/python`
- Expected: a common source is not rare
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_common_source_is_not_rare PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an account with no history reports no rarity rather than maximum rarity
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_an_account_with_no_history_reports_no_rarity_rather_than_maximum_rarity` executed under `dev/.venv/bin/python`
- Expected: The boundary that would otherwise flag every journal on a new account.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_an_account_with_no_history_reports_no_rarity_rather_than_maximum_rarity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rarity ceiling is a parameter and is applied
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_the_rarity_ceiling_is_a_parameter_and_is_applied` executed under `dev/.venv/bin/python`
- Expected: Two MANUAL rows in a 20-row history is 10%: rare at a 0.2 ceiling,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_the_rarity_ceiling_is_a_parameter_and_is_applied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared journal with no attribute row is not evaluable and is reported
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_declared_journal_with_no_attribute_row_is_not_evaluable_and_is_reported` executed under `dev/.venv/bin/python`
- Expected: Skipping it would count the member as scanned, which is the failure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_declared_journal_with_no_attribute_row_is_not_evaluable_and_is_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unreadable timestamp is not evaluable rather than scored false
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_an_unreadable_timestamp_is_not_evaluable_rather_than_scored_false` executed under `dev/.venv/bin/python`
- Expected: The time-based attributes are UNKNOWN, not absent. Scoring them False
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_an_unreadable_timestamp_is_not_evaluable_rather_than_scored_false PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the parser raises rather than defaulting
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_the_parser_raises_rather_than_defaulting` executed under `dev/.venv/bin/python`
- Expected: the parser raises rather than defaulting
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_the_parser_raises_rather_than_defaulting PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the summary states the scored set the threshold and the history used
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_the_summary_states_the_scored_set_the_threshold_and_the_history_used` executed under `dev/.venv/bin/python`
- Expected: the summary states the scored set the threshold and the history used
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_the_summary_states_the_scored_set_the_threshold_and_the_history_used PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a scanned journal is evaluable whether or not it fired
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_a_scanned_journal_is_evaluable_whether_or_not_it_fired` executed under `dev/.venv/bin/python`
- Expected: Coverage is about what was ASSESSED, not about what was found. An
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_a_scanned_journal_is_evaluable_whether_or_not_it_fired PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the attribute list on a finding is sorted and within the closed set
- Status: EXECUTED
- Input: `backend/tests/test_journal_attribute_outlier.py::test_the_attribute_list_on_a_finding_is_sorted_and_within_the_closed_set` executed under `dev/.venv/bin/python`
- Expected: the attribute list on a finding is sorted and within the closed set
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_journal_attribute_outlier.py::test_the_attribute_list_on_a_finding_is_sorted_and_within_the_closed_set PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_model_guard.py`

### Scenario: the flag is off by default
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_off_by_default` executed under `dev/.venv/bin/python`
- Expected: the flag is off by default
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_the_flag_is_off_by_default PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the flag is set inside and cleared after
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_set_inside_and_cleared_after` executed under `dev/.venv/bin/python`
- Expected: the flag is set inside and cleared after
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_the_flag_is_set_inside_and_cleared_after PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the flag is cleared even if the block raises
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_the_flag_is_cleared_even_if_the_block_raises` executed under `dev/.venv/bin/python`
- Expected: the flag is cleared even if the block raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_the_flag_is_cleared_even_if_the_block_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: nesting restores the outer state
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_nesting_restores_the_outer_state` executed under `dev/.venv/bin/python`
- Expected: nesting restores the outer state
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_nesting_restores_the_outer_state PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a model call from a deterministic section raises
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_a_model_call_from_a_deterministic_section_raises` executed under `dev/.venv/bin/python`
- Expected: a model call from a deterministic section raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_a_model_call_from_a_deterministic_section_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a forbidden call is not counted as an invocation
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_a_forbidden_call_is_not_counted_as_an_invocation` executed under `dev/.venv/bin/python`
- Expected: a forbidden call is not counted as an invocation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_a_forbidden_call_is_not_counted_as_an_invocation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a call outside a deterministic section is counted then unimplemented
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_a_call_outside_a_deterministic_section_is_counted_then_unimplemented` executed under `dev/.venv/bin/python`
- Expected: a call outside a deterministic section is counted then unimplemented
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_a_call_outside_a_deterministic_section_is_counted_then_unimplemented PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the flag does not leak across threads
- Status: EXECUTED
- Input: `backend/tests/test_model_guard.py::test_the_flag_does_not_leak_across_threads` executed under `dev/.venv/bin/python`
- Expected: the flag does not leak across threads
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_model_guard.py::test_the_flag_does_not_leak_across_threads PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_obligation_gap.py`

### Scenario: an unknown obligation kind raises rather than emitting a generic finding
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_an_unknown_obligation_kind_raises_rather_than_emitting_a_generic_finding` executed under `dev/.venv/bin/python`
- Expected: an unknown obligation kind raises rather than emitting a generic finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_an_unknown_obligation_kind_raises_rather_than_emitting_a_generic_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest that names no obligation kind raises
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_manifest_that_names_no_obligation_kind_raises` executed under `dev/.venv/bin/python`
- Expected: The default is the empty string, which is not in the vocabulary. A
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_manifest_that_names_no_obligation_kind_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared kind has all four vocabulary labels[intercompany_counterparty]
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[intercompany_counterparty]` executed under `dev/.venv/bin/python`, parameter case `intercompany_counterparty`
- Expected: every declared kind has all four vocabulary labels
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[intercompany_counterparty] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared kind has all four vocabulary labels[interface_feed_entry]
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[interface_feed_entry]` executed under `dev/.venv/bin/python`, parameter case `interface_feed_entry`
- Expected: every declared kind has all four vocabulary labels
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[interface_feed_entry] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared kind has all four vocabulary labels[scheduled_reversal]
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[scheduled_reversal]` executed under `dev/.venv/bin/python`, parameter case `scheduled_reversal`
- Expected: every declared kind has all four vocabulary labels
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_every_declared_kind_has_all_four_vocabulary_labels[scheduled_reversal] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the vocabulary is the three sub types and has not silently emptied
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_the_vocabulary_is_the_three_sub_types_and_has_not_silently_emptied` executed under `dev/.venv/bin/python`
- Expected: A `parametrize` over an emptied mapping collects zero tests and reports
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_the_vocabulary_is_the_three_sub_types_and_has_not_silently_emptied PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an undischarged due obligation is a finding carrying the whole amount
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_an_undischarged_due_obligation_is_a_finding_carrying_the_whole_amount` executed under `dev/.venv/bin/python`
- Expected: an undischarged due obligation is a finding carrying the whole amount
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_an_undischarged_due_obligation_is_a_finding_carrying_the_whole_amount PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a fully discharged obligation produces nothing but is still covered
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_fully_discharged_obligation_produces_nothing_but_is_still_covered` executed under `dev/.venv/bin/python`
- Expected: a fully discharged obligation produces nothing but is still covered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_fully_discharged_obligation_produces_nothing_but_is_still_covered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a partial discharge is a finding for the RESIDUAL not the whole
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_partial_discharge_is_a_finding_for_the_RESIDUAL_not_the_whole` executed under `dev/.venv/bin/python`
- Expected: a partial discharge is a finding for the RESIDUAL not the whole
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_partial_discharge_is_a_finding_for_the_RESIDUAL_not_the_whole PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a discharge within tolerance is a discharge
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_discharge_within_tolerance_is_a_discharge` executed under `dev/.venv/bin/python`
- Expected: a discharge within tolerance is a discharge
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_discharge_within_tolerance_is_a_discharge PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a discharge outside tolerance is not
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_discharge_outside_tolerance_is_not` executed under `dev/.venv/bin/python`
- Expected: a discharge outside tolerance is not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_discharge_outside_tolerance_is_not PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero discharge is a discharge of zero and not an absent one
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_zero_discharge_is_a_discharge_of_zero_and_not_an_absent_one` executed under `dev/.venv/bin/python`
- Expected: `0.00` and NULL are different claims and the primitive must not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_zero_discharge_is_a_discharge_of_zero_and_not_an_absent_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank discharge is read as no discharge[]
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_blank_discharge_is_read_as_no_discharge[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a blank discharge is read as no discharge
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_blank_discharge_is_read_as_no_discharge[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank discharge is read as no discharge[   ]
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_blank_discharge_is_read_as_no_discharge[   ]` executed under `dev/.venv/bin/python`, parameter case `   `
- Expected: a blank discharge is read as no discharge
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_blank_discharge_is_read_as_no_discharge[   ] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an obligation falling due later is neither a finding nor covered
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_an_obligation_falling_due_later_is_neither_a_finding_nor_covered` executed under `dev/.venv/bin/python`
- Expected: an obligation falling due later is neither a finding nor covered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_an_obligation_falling_due_later_is_neither_a_finding_nor_covered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an obligation due in exactly this period IS assessed
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_an_obligation_due_in_exactly_this_period_IS_assessed` executed under `dev/.venv/bin/python`
- Expected: The boundary. `>` not `>=`, and this is what pins it.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_an_obligation_due_in_exactly_this_period_IS_assessed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the not yet due count is reported in the summary
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_the_not_yet_due_count_is_reported_in_the_summary` executed under `dev/.venv/bin/python`
- Expected: the not yet due count is reported in the summary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_the_not_yet_due_count_is_reported_in_the_summary PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared member with no row is not evaluable and not covered
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_declared_member_with_no_row_is_not_evaluable_and_not_covered` executed under `dev/.venv/bin/python`
- Expected: a declared member with no row is not evaluable and not covered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_declared_member_with_no_row_is_not_evaluable_and_not_covered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: rows of another obligation kind are not assessed by this manifest
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_rows_of_another_obligation_kind_are_not_assessed_by_this_manifest` executed under `dev/.venv/bin/python`
- Expected: rows of another obligation kind are not assessed by this manifest
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_rows_of_another_obligation_kind_are_not_assessed_by_this_manifest PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a one sided obligation carries both entities and names the missing one
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_one_sided_obligation_carries_both_entities_and_names_the_missing_one` executed under `dev/.venv/bin/python`
- Expected: a one sided obligation carries both entities and names the missing one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_one_sided_obligation_carries_both_entities_and_names_the_missing_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reversal carries NO entity fields rather than empty ones
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_a_reversal_carries_NO_entity_fields_rather_than_empty_ones` executed under `dev/.venv/bin/python`
- Expected: Absent, not blank. A renderer cannot print "posted by: " with nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_a_reversal_carries_NO_entity_fields_rather_than_empty_ones PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each kind labels its own fields in its own words
- Status: EXECUTED
- Input: `backend/tests/test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words` executed under `dev/.venv/bin/python`
- Expected: each kind labels its own fields in its own words
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_policy_cold.py`

### Scenario: a finding whose allowed types include r3 or r4 is never auto disposed[types0]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types0]` executed under `dev/.venv/bin/python`, parameter case `types0`
- Expected: a finding whose allowed types include r3 or r4 is never auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a finding whose allowed types include r3 or r4 is never auto disposed[types1]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types1]` executed under `dev/.venv/bin/python`, parameter case `types1`
- Expected: a finding whose allowed types include r3 or r4 is never auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a finding whose allowed types include r3 or r4 is never auto disposed[types2]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types2]` executed under `dev/.venv/bin/python`, parameter case `types2`
- Expected: a finding whose allowed types include r3 or r4 is never auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a finding whose allowed types include r3 or r4 is never auto disposed[types3]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types3]` executed under `dev/.venv/bin/python`, parameter case `types3`
- Expected: a finding whose allowed types include r3 or r4 is never auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_finding_whose_allowed_types_include_r3_or_r4_is_never_auto_disposed[types3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a safe option existing alongside a posting one does not make it cold
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_safe_option_existing_alongside_a_posting_one_does_not_make_it_cold` executed under `dev/.venv/bin/python`
- Expected: a safe option existing alongside a posting one does not make it cold
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_safe_option_existing_alongside_a_posting_one_does_not_make_it_cold PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the posting capable test runs before any rule can match
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_posting_capable_test_runs_before_any_rule_can_match` executed under `dev/.venv/bin/python`
- Expected: the posting capable test runs before any rule can match
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_posting_capable_test_runs_before_any_rule_can_match PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cold rule that disposes as a posting type is not constructible
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_cold_rule_that_disposes_as_a_posting_type_is_not_constructible` executed under `dev/.venv/bin/python`
- Expected: a cold rule that disposes as a posting type is not constructible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_cold_rule_that_disposes_as_a_posting_type_is_not_constructible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no argument that makes a posting capable finding cold
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_there_is_no_argument_that_makes_a_posting_capable_finding_cold` executed under `dev/.venv/bin/python`
- Expected: there is no argument that makes a posting capable finding cold
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_there_is_no_argument_that_makes_a_posting_capable_finding_cold PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no rule matching also routes hot
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_no_rule_matching_also_routes_hot` executed under `dev/.venv/bin/python`
- Expected: no rule matching also routes hot
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_no_rule_matching_also_routes_hot PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a matched finding is auto disposed and records its provenance
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_matched_finding_is_auto_disposed_and_records_its_provenance` executed under `dev/.venv/bin/python`
- Expected: a matched finding is auto disposed and records its provenance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_matched_finding_is_auto_disposed_and_records_its_provenance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the exception row carries the marker the rule and the dossier ref
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_exception_row_carries_the_marker_the_rule_and_the_dossier_ref` executed under `dev/.venv/bin/python`
- Expected: the exception row carries the marker the rule and the dossier ref
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_exception_row_carries_the_marker_the_rule_and_the_dossier_ref PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a hot row is not marked auto disposed
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_hot_row_is_not_marked_auto_disposed` executed under `dev/.venv/bin/python`
- Expected: a hot row is not marked auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_hot_row_is_not_marked_auto_disposed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the first matching rule wins and the record names it
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_first_matching_rule_wins_and_the_record_names_it` executed under `dev/.venv/bin/python`
- Expected: the first matching rule wins and the record names it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_first_matching_rule_wins_and_the_record_names_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the first period states two further periods would escalate
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_first_period_states_two_further_periods_would_escalate` executed under `dev/.venv/bin/python`
- Expected: the first period states two further periods would escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_first_period_states_two_further_periods_would_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: exactly two consecutive periods raises no escalation and states the count
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_exactly_two_consecutive_periods_raises_no_escalation_and_states_the_count` executed under `dev/.venv/bin/python`
- Expected: exactly two consecutive periods raises no escalation and states the count
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_exactly_two_consecutive_periods_raises_no_escalation_and_states_the_count PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the third consecutive period escalates hot and names all three
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_third_consecutive_period_escalates_hot_and_names_all_three` executed under `dev/.venv/bin/python`
- Expected: the third consecutive period escalates hot and names all three
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_third_consecutive_period_escalates_hot_and_names_all_three PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the third period is not auto disposed
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_third_period_is_not_auto_disposed` executed under `dev/.venv/bin/python`
- Expected: the third period is not auto disposed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_third_period_is_not_auto_disposed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: THE control the escalation holds regardless of which rule disposed
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_THE_control_the_escalation_holds_regardless_of_which_rule_disposed` executed under `dev/.venv/bin/python`
- Expected: `AC-F35-12`'s load-bearing clause.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_THE_control_the_escalation_holds_regardless_of_which_rule_disposed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: three different rules still escalate
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_three_different_rules_still_escalate` executed under `dev/.venv/bin/python`
- Expected: three different rules still escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_three_different_rules_still_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the escalation counter is keyed on account and direction only
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_escalation_counter_is_keyed_on_account_and_direction_only` executed under `dev/.venv/bin/python`
- Expected: the escalation counter is keyed on account and direction only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_escalation_counter_is_keyed_on_account_and_direction_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a gap breaks the streak
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_gap_breaks_the_streak` executed under `dev/.venv/bin/python`
- Expected: a gap breaks the streak
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_gap_breaks_the_streak PASSED` (verbatim from the `-v` node list of this run)

### Scenario: after a gap three fresh consecutive periods escalate
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_after_a_gap_three_fresh_consecutive_periods_escalate` executed under `dev/.venv/bin/python`
- Expected: after a gap three fresh consecutive periods escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_after_a_gap_three_fresh_consecutive_periods_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods0-12-expected0]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods0-12-expected0]` executed under `dev/.venv/bin/python`, parameter case `periods0-12-expected0`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods0-12-expected0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods1-12-expected1]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods1-12-expected1]` executed under `dev/.venv/bin/python`, parameter case `periods1-12-expected1`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods1-12-expected1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods2-12-expected2]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods2-12-expected2]` executed under `dev/.venv/bin/python`, parameter case `periods2-12-expected2`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods2-12-expected2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods3-12-expected3]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods3-12-expected3]` executed under `dev/.venv/bin/python`, parameter case `periods3-12-expected3`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods3-12-expected3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods4-13-expected4]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods4-13-expected4]` executed under `dev/.venv/bin/python`, parameter case `periods4-13-expected4`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods4-13-expected4] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods5-12-expected5]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods5-12-expected5]` executed under `dev/.venv/bin/python`, parameter case `periods5-12-expected5`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods5-12-expected5] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods6-12-expected6]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods6-12-expected6]` executed under `dev/.venv/bin/python`, parameter case `periods6-12-expected6`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods6-12-expected6] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: consecutive run length[periods7-12-expected7]
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods7-12-expected7]` executed under `dev/.venv/bin/python`, parameter case `periods7-12-expected7`
- Expected: consecutive run length
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_consecutive_run_length[periods7-12-expected7] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a different account has its own streak
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_different_account_has_its_own_streak` executed under `dev/.venv/bin/python`
- Expected: a different account has its own streak
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_different_account_has_its_own_streak PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the other direction has its own streak
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_other_direction_has_its_own_streak` executed under `dev/.venv/bin/python`
- Expected: the other direction has its own streak
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_other_direction_has_its_own_streak PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same account and direction share one streak
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_same_account_and_direction_share_one_streak` executed under `dev/.venv/bin/python`
- Expected: the same account and direction share one streak
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_same_account_and_direction_share_one_streak PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a finding cannot be disposed twice
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_finding_cannot_be_disposed_twice` executed under `dev/.venv/bin/python`
- Expected: a finding cannot be disposed twice
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_finding_cannot_be_disposed_twice PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a hot route reason outside the closed set is unstorable
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_a_hot_route_reason_outside_the_closed_set_is_unstorable` executed under `dev/.venv/bin/python`
- Expected: a hot route reason outside the closed set is unstorable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_a_hot_route_reason_outside_the_closed_set_is_unstorable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown resolution type is refused at the door
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_an_unknown_resolution_type_is_refused_at_the_door` executed under `dev/.venv/bin/python`
- Expected: an unknown resolution type is refused at the door
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_an_unknown_resolution_type_is_refused_at_the_door PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the escalation threshold is three and is named not inlined
- Status: EXECUTED
- Input: `backend/tests/test_policy_cold.py::test_the_escalation_threshold_is_three_and_is_named_not_inlined` executed under `dev/.venv/bin/python`
- Expected: the escalation threshold is three and is named not inlined
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_policy_cold.py::test_the_escalation_threshold_is_three_and_is_named_not_inlined PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_population_and_coverage.py`

### Scenario: the committed population compiles
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_the_committed_population_compiles` executed under `dev/.venv/bin/python`
- Expected: the committed population compiles
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_the_committed_population_compiles PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the population object has no attribute that could hold a table name
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_the_population_object_has_no_attribute_that_could_hold_a_table_name` executed under `dev/.venv/bin/python`
- Expected: the population object has no attribute that could hold a table name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_the_population_object_has_no_attribute_that_could_hold_a_table_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: member and segment extraction
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_member_and_segment_extraction` executed under `dev/.venv/bin/python`
- Expected: member and segment extraction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_member_and_segment_extraction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a row missing a member key component raises rather than defaulting
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_row_missing_a_member_key_component_raises_rather_than_defaulting` executed under `dev/.venv/bin/python`
- Expected: a row missing a member key component raises rather than defaulting
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_row_missing_a_member_key_component_raises_rather_than_defaulting PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[table]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table]` executed under `dev/.venv/bin/python`, parameter case `table`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[table_name]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table_name]` executed under `dev/.venv/bin/python`, parameter case `table_name`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[table_name] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[schema]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[schema]` executed under `dev/.venv/bin/python`, parameter case `schema`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[schema] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[from]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[from]` executed under `dev/.venv/bin/python`, parameter case `from`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[from] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[sql_file]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[sql_file]` executed under `dev/.venv/bin/python`, parameter case `sql_file`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[sql_file] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest key naming where data lives fails the build[view]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[view]` executed under `dev/.venv/bin/python`, parameter case `view`
- Expected: a manifest key naming where data lives fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_key_naming_where_data_lives_fails_the_build[view] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[gl_je_lines]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `gl_je_lines`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[gl_balances]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_balances]` executed under `dev/.venv/bin/python`, parameter case `gl_balances`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[gl_balances] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[dw.gl_je_lines]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `dw.gl_je_lines`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[dw.gl_balances]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_balances]` executed under `dev/.venv/bin/python`, parameter case `dw.gl_balances`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[dw.gl_balances] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[wh_account_balances]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[wh_account_balances]` executed under `dev/.venv/bin/python`, parameter case `wh_account_balances`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[wh_account_balances] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[erp_control_extract]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[erp_control_extract]` executed under `dev/.venv/bin/python`, parameter case `erp_control_extract`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[erp_control_extract] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[load_batches]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[load_batches]` executed under `dev/.venv/bin/python`, parameter case `load_batches`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[load_batches] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[subledger_control_tieout]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[subledger_control_tieout]` executed under `dev/.venv/bin/python`, parameter case `subledger_control_tieout`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[subledger_control_tieout] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[intercompany_pairs]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[intercompany_pairs]` executed under `dev/.venv/bin/python`, parameter case `intercompany_pairs`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[intercompany_pairs] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[account_rollforward]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_rollforward]` executed under `dev/.venv/bin/python`, parameter case `account_rollforward`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_rollforward] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[fx_revaluation]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[fx_revaluation]` executed under `dev/.venv/bin/python`, parameter case `fx_revaluation`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[fx_revaluation] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[suspense_residuals]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[suspense_residuals]` executed under `dev/.venv/bin/python`, parameter case `suspense_residuals`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[suspense_residuals] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[account_movements]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_movements]` executed under `dev/.venv/bin/python`, parameter case `account_movements`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[account_movements] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[period_explanations]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[period_explanations]` executed under `dev/.venv/bin/python`, parameter case `period_explanations`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[period_explanations] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[coded_postings]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[coded_postings]` executed under `dev/.venv/bin/python`, parameter case `coded_postings`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[coded_postings] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[reclass_labels]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[reclass_labels]` executed under `dev/.venv/bin/python`, parameter case `reclass_labels`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[reclass_labels] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a manifest mentioning a physical object fails the build[posting_obligations]
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[posting_obligations]` executed under `dev/.venv/bin/python`, parameter case `posting_obligations`
- Expected: a manifest mentioning a physical object fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_manifest_mentioning_a_physical_object_fails_the_build[posting_obligations] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a nested physical object reference is also caught
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_nested_physical_object_reference_is_also_caught` executed under `dev/.venv/bin/python`
- Expected: a nested physical object reference is also caught
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_nested_physical_object_reference_is_also_caught PASSED` (verbatim from the `-v` node list of this run)

### Scenario: source class is a closed enum
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_source_class_is_a_closed_enum` executed under `dev/.venv/bin/python`
- Expected: source class is a closed enum
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_source_class_is_a_closed_enum PASSED` (verbatim from the `-v` node list of this run)

### Scenario: phase 2 source classes are already permitted
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_phase_2_source_classes_are_already_permitted` executed under `dev/.venv/bin/python`
- Expected: phase 2 source classes are already permitted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_phase_2_source_classes_are_already_permitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing member key fails the build
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_missing_member_key_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a missing member key fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_missing_member_key_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing resolver query fails the build
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_missing_resolver_query_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a missing resolver query fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_missing_resolver_query_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a segment outside the member key fails the build
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_segment_outside_the_member_key_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a segment outside the member key fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_segment_outside_the_member_key_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a duplicate population fails the build
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_a_duplicate_population_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a duplicate population fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_a_duplicate_population_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty population directory fails the build
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_an_empty_population_directory_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: an empty population directory fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_an_empty_population_directory_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: full coverage
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_full_coverage` executed under `dev/.venv/bin/python`
- Expected: full coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_full_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: partial coverage names its gaps
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_partial_coverage_names_its_gaps` executed under `dev/.venv/bin/python`
- Expected: partial coverage names its gaps
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_partial_coverage_names_its_gaps PASSED` (verbatim from the `-v` node list of this run)

### Scenario: zero coverage
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_zero_coverage` executed under `dev/.venv/bin/python`
- Expected: zero coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_zero_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty declared population is not complete
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_an_empty_declared_population_is_not_complete` executed under `dev/.venv/bin/python`
- Expected: an empty declared population is not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_an_empty_declared_population_is_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: covering an undeclared member does not inflate coverage
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_covering_an_undeclared_member_does_not_inflate_coverage` executed under `dev/.venv/bin/python`
- Expected: covering an undeclared member does not inflate coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_covering_an_undeclared_member_does_not_inflate_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: percent rounds down so a bounded run never reads as complete
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_percent_rounds_down_so_a_bounded_run_never_reads_as_complete` executed under `dev/.venv/bin/python`
- Expected: percent rounds down so a bounded run never reads as complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_percent_rounds_down_so_a_bounded_run_never_reads_as_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: scope serialises with its gaps
- Status: EXECUTED
- Input: `backend/tests/test_population_and_coverage.py::test_scope_serialises_with_its_gaps` executed under `dev/.venv/bin/python`
- Expected: scope serialises with its gaps
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_population_and_coverage.py::test_scope_serialises_with_its_gaps PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_primitive_freshness.py`

### Scenario: a batch that arrived on time produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_on_time_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a batch that arrived on time produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_on_time_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a batch that never arrived names itself its schedule and its population
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_never_arrived_names_itself_its_schedule_and_its_population` executed under `dev/.venv/bin/python`
- Expected: `AC-F26-04` in full: the batch, its expected arrival, and what it would
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_batch_that_never_arrived_names_itself_its_schedule_and_its_population PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a batch that arrived carrying zero rows is not a missing batch
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_carrying_zero_rows_is_not_a_missing_batch` executed under `dev/.venv/bin/python`
- Expected: The distinction the whole leg rests on.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_batch_that_arrived_carrying_zero_rows_is_not_a_missing_batch PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a late batch is a finding of its own kind
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_late_batch_is_a_finding_of_its_own_kind` executed under `dev/.venv/bin/python`
- Expected: a late batch is a finding of its own kind
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_late_batch_is_a_finding_of_its_own_kind PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a batch arriving exactly on its expected time is not late
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_batch_arriving_exactly_on_its_expected_time_is_not_late` executed under `dev/.venv/bin/python`
- Expected: a batch arriving exactly on its expected time is not late
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_batch_arriving_exactly_on_its_expected_time_is_not_late PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared batch with no schedule row is uncovered and named
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_declared_batch_with_no_schedule_row_is_uncovered_and_named` executed under `dev/.venv/bin/python`
- Expected: a declared batch with no schedule row is uncovered and named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_declared_batch_with_no_schedule_row_is_uncovered_and_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty string arrival counts as never arrived
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_an_empty_string_arrival_counts_as_never_arrived` executed under `dev/.venv/bin/python`
- Expected: an empty string arrival counts as never arrived
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_an_empty_string_arrival_counts_as_never_arrived PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every run states that staleness is not close clock relative
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_every_run_states_that_staleness_is_not_close_clock_relative` executed under `dev/.venv/bin/python`
- Expected: `AC-F26-05` IS NOT SATISFIED — do not map that ID to this primitive.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_every_run_states_that_staleness_is_not_close_clock_relative PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the summary reports no close clock rather than a close relative figure
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_the_summary_reports_no_close_clock_rather_than_a_close_relative_figure` executed under `dev/.venv/bin/python`
- Expected: the summary reports no close clock rather than a close relative figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_the_summary_reports_no_close_clock_rather_than_a_close_relative_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the latest arrival is reported as an absolute time and labelled as such
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_the_latest_arrival_is_reported_as_an_absolute_time_and_labelled_as_such` executed under `dev/.venv/bin/python`
- Expected: An absolute timestamp is what this build CAN say. It is reported under
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_the_latest_arrival_is_reported_as_an_absolute_time_and_labelled_as_such PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a run over no batches still reports the missing close clock
- Status: EXECUTED
- Input: `backend/tests/test_primitive_freshness.py::test_a_run_over_no_batches_still_reports_the_missing_close_clock` executed under `dev/.venv/bin/python`
- Expected: a run over no batches still reports the missing close clock
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_freshness.py::test_a_run_over_no_batches_still_reports_the_missing_close_clock PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_primitive_identity_tieout.py`

### Scenario: equal sides produce no finding and a covered member
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_equal_sides_produce_no_finding_and_a_covered_member` executed under `dev/.venv/bin/python`
- Expected: equal sides produce no finding and a covered member
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_equal_sides_produce_no_finding_and_a_covered_member PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the totals are reported even when nothing diverges
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_totals_are_reported_even_when_nothing_diverges` executed under `dev/.venv/bin/python`
- Expected: `AC-F26-02`. A run with zero divergences still compared two totals.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_totals_are_reported_even_when_nothing_diverges PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a divergence names its amount and direction
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_divergence_names_its_amount_and_direction` executed under `dev/.venv/bin/python`
- Expected: a divergence names its amount and direction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_divergence_names_its_amount_and_direction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the other direction is named as the other side
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_other_direction_is_named_as_the_other_side` executed under `dev/.venv/bin/python`
- Expected: the other direction is named as the other side
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_other_direction_is_named_as_the_other_side PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the smallest currency unit is reported and reported exactly
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_smallest_currency_unit_is_reported_and_reported_exactly` executed under `dev/.venv/bin/python`
- Expected: `AC-F26-08`, at the primitive.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_smallest_currency_unit_is_reported_and_reported_exactly PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the default tolerance is zero so a one cent break is a finding
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_default_tolerance_is_zero_so_a_one_cent_break_is_a_finding` executed under `dev/.venv/bin/python`
- Expected: the default tolerance is zero so a one cent break is a finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_default_tolerance_is_zero_so_a_one_cent_break_is_a_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the tolerance boundary is inclusive[0.99-0]
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[0.99-0]` executed under `dev/.venv/bin/python`, parameter case `0.99-0`
- Expected: At the tolerance is INSIDE it. Asserted at, and one either side of, the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[0.99-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the tolerance boundary is inclusive[1.00-0]
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.00-0]` executed under `dev/.venv/bin/python`, parameter case `1.00-0`
- Expected: At the tolerance is INSIDE it. Asserted at, and one either side of, the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.00-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the tolerance boundary is inclusive[1.01-1]
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.01-1]` executed under `dev/.venv/bin/python`, parameter case `1.01-1`
- Expected: At the tolerance is INSIDE it. Asserted at, and one either side of, the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_tolerance_boundary_is_inclusive[1.01-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a negative difference is compared on its magnitude
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_negative_difference_is_compared_on_its_magnitude` executed under `dev/.venv/bin/python`
- Expected: a negative difference is compared on its magnitude
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_negative_difference_is_compared_on_its_magnitude PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member present on the left only is a one sided finding
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_left_only_is_a_one_sided_finding` executed under `dev/.venv/bin/python`
- Expected: Not a divergence of the whole amount.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_left_only_is_a_one_sided_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member present on the right only names the other side
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_right_only_names_the_other_side` executed under `dev/.venv/bin/python`
- Expected: a member present on the right only names the other side
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_member_present_on_the_right_only_names_the_other_side PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty string is treated as absent not as zero
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_an_empty_string_is_treated_as_absent_not_as_zero` executed under `dev/.venv/bin/python`
- Expected: an empty string is treated as absent not as zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_an_empty_string_is_treated_as_absent_not_as_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a one sided member is still covered
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_one_sided_member_is_still_covered` executed under `dev/.venv/bin/python`
- Expected: We know exactly what is true about it, so it is not a gap in coverage.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_one_sided_member_is_still_covered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared member with no row is uncovered and named
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_declared_member_with_no_row_is_uncovered_and_named` executed under `dev/.venv/bin/python`
- Expected: a declared member with no row is uncovered and named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_declared_member_with_no_row_is_uncovered_and_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing member produces no finding of any kind
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_a_missing_member_produces_no_finding_of_any_kind` executed under `dev/.venv/bin/python`
- Expected: Silence is never a pass, and absence is never a divergence either.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_a_missing_member_produces_no_finding_of_any_kind PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the field and label parameters make this the a6 check too
- Status: EXECUTED
- Input: `backend/tests/test_primitive_identity_tieout.py::test_the_field_and_label_parameters_make_this_the_a6_check_too` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §7.3 lists this primitive as serving F26 A1 AND F28
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_identity_tieout.py::test_the_field_and_label_parameters_make_this_the_a6_check_too PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_primitive_peer_coding.py`

### Scenario: a cost centre divergence names both codings and its evidence
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cost_centre_divergence_names_both_codings_and_its_evidence` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-01`. A proposed value with no evidence beside it is an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_cost_centre_divergence_names_both_codings_and_its_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a natural account divergence confirms both are in the same caption
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_natural_account_divergence_confirms_both_are_in_the_same_caption` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-02` asks for the confirmation explicitly, so it is a field
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_natural_account_divergence_confirms_both_are_in_the_same_caption PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a correctly coded posting produces no finding
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_correctly_coded_posting_produces_no_finding` executed under `dev/.venv/bin/python`
- Expected: a correctly coded posting produces no finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_correctly_coded_posting_produces_no_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an intercompany segment miscoding emits no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_segment_miscoding_emits_no_proposal` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-03`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_segment_miscoding_emits_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a caption crossing emits no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_emits_no_proposal` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-04`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_emits_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cut off error says cut off resolution is not proposed
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_error_says_cut_off_resolution_is_not_proposed` executed under `dev/.venv/bin/python`
- Expected: `AC-F33-05` requires the finding to STATE it, not merely to omit the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_error_says_cut_off_resolution_is_not_proposed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the proposal field is ABSENT rather than present and blocked
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_proposal_field_is_ABSENT_rather_than_present_and_blocked` executed under `dev/.venv/bin/python`
- Expected: A downstream consumer reads a field that is there. The two shapes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_the_proposal_field_is_ABSENT_rather_than_present_and_blocked PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a caption crossing that also diverges on cost centre emits no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_that_also_diverges_on_cost_centre_emits_no_proposal` executed under `dev/.venv/bin/python`
- Expected: THE ORDER SCENARIO.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_caption_crossing_that_also_diverges_on_cost_centre_emits_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a cut off that also diverges on cost centre emits no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_that_also_diverges_on_cost_centre_emits_no_proposal` executed under `dev/.venv/bin/python`
- Expected: a cut off that also diverges on cost centre emits no proposal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_cut_off_that_also_diverges_on_cost_centre_emits_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an intercompany miscoding that also diverges on account emits no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_miscoding_that_also_diverges_on_account_emits_no_proposal` executed under `dev/.venv/bin/python`
- Expected: an intercompany miscoding that also diverges on account emits no proposal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_an_intercompany_miscoding_that_also_diverges_on_account_emits_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: exactly one finding is emitted per posting
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_exactly_one_finding_is_emitted_per_posting` executed under `dev/.venv/bin/python`
- Expected: Not one per condition. A posting is one thing a reviewer acts on, and
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_exactly_one_finding_is_emitted_per_posting PASSED` (verbatim from the `-v` node list of this run)

### Scenario: too few peers makes the posting unevaluable rather than a finding
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_too_few_peers_makes_the_posting_unevaluable_rather_than_a_finding` executed under `dev/.venv/bin/python`
- Expected: Without a peer set there is nothing for a divergence to be a divergence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_too_few_peers_makes_the_posting_unevaluable_rather_than_a_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the peer support boundary is exact
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_peer_support_boundary_is_exact` executed under `dev/.venv/bin/python`
- Expected: the peer support boundary is exact
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_the_peer_support_boundary_is_exact PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a divided peer set produces no proposal
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_divided_peer_set_produces_no_proposal` executed under `dev/.venv/bin/python`
- Expected: Agreement below the bound means the peers do not agree with each other,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_divided_peer_set_produces_no_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: peers are context and are not counted as covered members
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_peers_are_context_and_are_not_counted_as_covered_members` executed under `dev/.venv/bin/python`
- Expected: Counting them would inflate coverage by the size of the history.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_peers_are_context_and_are_not_counted_as_covered_members PASSED` (verbatim from the `-v` node list of this run)

### Scenario: only earlier periods are peers
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_only_earlier_periods_are_peers` executed under `dev/.venv/bin/python`
- Expected: A peer from the same period is another posting nobody has checked.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_only_earlier_periods_are_peers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared posting with no row is named not silently skipped
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_a_declared_posting_with_no_row_is_named_not_silently_skipped` executed under `dev/.venv/bin/python`
- Expected: a declared posting with no row is named not silently skipped
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_a_declared_posting_with_no_row_is_named_not_silently_skipped PASSED` (verbatim from the `-v` node list of this run)

### Scenario: natural account peers are scoped to the same caption
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_natural_account_peers_are_scoped_to_the_same_caption` executed under `dev/.venv/bin/python`
- Expected: A caption's accounts are not comparable across captions, so the mode is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_natural_account_peers_are_scoped_to_the_same_caption PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the summary declares which sub types are in scope
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_the_summary_declares_which_sub_types_are_in_scope` executed under `dev/.venv/bin/python`
- Expected: the summary declares which sub types are in scope
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_the_summary_declares_which_sub_types_are_in_scope PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every number the coding leg emits is hashable evidence
- Status: EXECUTED
- Input: `backend/tests/test_primitive_peer_coding.py::test_every_number_the_coding_leg_emits_is_hashable_evidence` executed under `dev/.venv/bin/python`
- Expected: No floats on the path to a dossier. See the sibling scenario in
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_primitive_peer_coding.py::test_every_number_the_coding_leg_emits_is_hashable_evidence PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_process_entrypoints.py`

### Scenario: ges run refuses when role is not ges
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_ges_run_refuses_when_role_is_not_ges` executed under `dev/.venv/bin/python`
- Expected: ges run refuses when role is not ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_ges_run_refuses_when_role_is_not_ges PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api run refuses when role is not api
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_when_role_is_not_api` executed under `dev/.venv/bin/python`
- Expected: api run refuses when role is not api
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_when_role_is_not_api PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api run refuses to start holding a credential
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_to_start_holding_a_credential` executed under `dev/.venv/bin/python`
- Expected: api run refuses to start holding a credential
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_api_run_refuses_to_start_holding_a_credential PASSED` (verbatim from the `-v` node list of this run)

### Scenario: api health discloses no credential
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_api_health_discloses_no_credential` executed under `dev/.venv/bin/python`
- Expected: api health discloses no credential
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_api_health_discloses_no_credential PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ges health reports role but no secret
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_ges_health_reports_role_but_no_secret` executed under `dev/.venv/bin/python`
- Expected: ges health reports role but no secret
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_ges_health_reports_role_but_no_secret PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ges loopback auth rejects a wrong token
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::test_ges_loopback_auth_rejects_a_wrong_token` executed under `dev/.venv/bin/python`
- Expected: ges loopback auth rejects a wrong token
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::test_ges_loopback_auth_rejects_a_wrong_token PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it refuses to start in production
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_refuses_to_start_in_production` executed under `dev/.venv/bin/python`
- Expected: it refuses to start in production
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_refuses_to_start_in_production PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it names the boundary it collapses rather than only the url
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_names_the_boundary_it_collapses_rather_than_only_the_url` executed under `dev/.venv/bin/python`
- Expected: A launcher that printed a URL and nothing else would let somebody
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_it_names_the_boundary_it_collapses_rather_than_only_the_url PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the api entry point still starts no broker
- Status: EXECUTED
- Input: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_the_api_entry_point_still_starts_no_broker` executed under `dev/.venv/bin/python`
- Expected: `app/run.py` is the real one and must stay clean: it binds no
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_process_entrypoints.py::TestThePilotLauncher::test_the_api_entry_point_still_starts_no_broker PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_refusal_registry.py`

### Scenario: the registry holds exactly a19 to a25
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_the_registry_holds_exactly_a19_to_a25` executed under `dev/.venv/bin/python`
- Expected: the registry holds exactly a19 to a25
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_the_registry_holds_exactly_a19_to_a25 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every refusal carries a ground and maps to one speech act
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_every_refusal_carries_a_ground_and_maps_to_one_speech_act` executed under `dev/.venv/bin/python`
- Expected: every refusal carries a ground and maps to one speech act
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_every_refusal_carries_a_ground_and_maps_to_one_speech_act PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no refusal is expressed as a bundle rule
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_no_refusal_is_expressed_as_a_bundle_rule` executed under `dev/.venv/bin/python`
- Expected: The judgement call, asserted rather than left in a docstring.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_no_refusal_is_expressed_as_a_bundle_rule PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an ordinary finding trips nothing
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_an_ordinary_finding_trips_nothing` executed under `dev/.venv/bin/python`
- Expected: an ordinary finding trips nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_an_ordinary_finding_trips_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[The variance is small relative to the account balance, so no adjustment is needed.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The variance is small relative to the account balance, so no adjustment is needed.]` executed under `dev/.venv/bin/python`, parameter case `The variance is small relative to the account balance, so no adjustment is needed.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The variance is small relative to the account balance, so no adjustment is needed.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[This is within the normal range for this account and does not require further work.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This is within the normal range for this account and does not require further work.]` executed under `dev/.venv/bin/python`, parameter case `This is within the normal range for this account and does not require further work.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This is within the normal range for this account and does not require further work.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[Below the threshold we use here, so nothing further to do.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Below the threshold we use here, so nothing further to do.]` executed under `dev/.venv/bin/python`, parameter case `Below the threshold we use here, so nothing further to do.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Below the threshold we use here, so nothing further to do.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[It is trivial next to the balance; safe to ignore.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It is trivial next to the balance; safe to ignore.]` executed under `dev/.venv/bin/python`, parameter case `It is trivial next to the balance; safe to ignore.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It is trivial next to the balance; safe to ignore.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[An auditor wouldn't look at this one, so it can be passed.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[An auditor wouldn't look at this one, so it can be passed.]` executed under `dev/.venv/bin/python`, parameter case `An auditor wouldn't look at this one, so it can be passed.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[An auditor wouldn't look at this one, so it can be passed.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[Honestly this is in the noise \u2014 leave it as is.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Honestly this is in the noise \u2014 leave it as is.]` executed under `dev/.venv/bin/python`, parameter case `Honestly this is in the noise \u2014 leave it as is.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Honestly this is in the noise \u2014 leave it as is.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[The difference is negligible and does not warrant investigation.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The difference is negligible and does not warrant investigation.]` executed under `dev/.venv/bin/python`, parameter case `The difference is negligible and does not warrant investigation.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The difference is negligible and does not warrant investigation.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[It's basically rounding; no further action.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It's basically rounding; no further action.]` executed under `dev/.venv/bin/python`, parameter case `It's basically rounding; no further action.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[It's basically rounding; no further action.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[Nobody would flag a number this size, so no correction is required.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Nobody would flag a number this size, so no correction is required.]` executed under `dev/.venv/bin/python`, parameter case `Nobody would flag a number this size, so no correction is required.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Nobody would flag a number this size, so no correction is required.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[The amount is tiny compared to the account, so it can safely be cleared.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The amount is tiny compared to the account, so it can safely be cleared.]` executed under `dev/.venv/bin/python`, parameter case `The amount is tiny compared to the account, so it can safely be cleared.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[The amount is tiny compared to the account, so it can safely be cleared.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[This doesn't move the needle; no follow-up needed.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This doesn't move the needle; no follow-up needed.]` executed under `dev/.venv/bin/python`, parameter case `This doesn't move the needle; no follow-up needed.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[This doesn't move the needle; no follow-up needed.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 catches the speech act not the vocabulary[Under the limit for this entity, so no entry is necessary.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Under the limit for this entity, so no entry is necessary.]` executed under `dev/.venv/bin/python`, parameter case `Under the limit for this entity, so no entry is necessary.`
- Expected: a20 catches the speech act not the vocabulary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_catches_the_speech_act_not_the_vocabulary[Under the limit for this entity, so no entry is necessary.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 needs both halves neither alone is a refusal
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_needs_both_halves_neither_alone_is_a_refusal` executed under `dev/.venv/bin/python`
- Expected: a20 needs both halves neither alone is a refusal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_needs_both_halves_neither_alone_is_a_refusal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a20 structural leg needs no prose at all
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a20_structural_leg_needs_no_prose_at_all` executed under `dev/.venv/bin/python`
- Expected: a20 structural leg needs no prose at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a20_structural_leg_needs_no_prose_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every size shaped treatment ground is a20[magnitude]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[magnitude]` executed under `dev/.venv/bin/python`, parameter case `magnitude`
- Expected: every size shaped treatment ground is a20
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[magnitude] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every size shaped treatment ground is a20[threshold]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[threshold]` executed under `dev/.venv/bin/python`, parameter case `threshold`
- Expected: every size shaped treatment ground is a20
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[threshold] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every size shaped treatment ground is a20[none]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[none]` executed under `dev/.venv/bin/python`, parameter case `none`
- Expected: every size shaped treatment ground is a20
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[none] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every size shaped treatment ground is a20[]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: every size shaped treatment ground is a20
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_every_size_shaped_treatment_ground_is_a20[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the prose leg is evadable and here is a paraphrase that evades it
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it` executed under `dev/.venv/bin/python`
- Expected: DEMONSTRATES THE RESIDUAL. Do not delete this test to make a number go up.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the declared speech act is never trusted
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_the_declared_speech_act_is_never_trusted` executed under `dev/.venv/bin/python`
- Expected: the declared speech act is never trusted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_the_declared_speech_act_is_never_trusted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[allowance]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[allowance]` executed under `dev/.venv/bin/python`, parameter case `allowance`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[allowance] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[reserve]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[reserve]` executed under `dev/.venv/bin/python`, parameter case `reserve`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[reserve] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[provision]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[provision]` executed under `dev/.venv/bin/python`, parameter case `provision`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[provision] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[impairment]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[impairment]` executed under `dev/.venv/bin/python`, parameter case `impairment`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[impairment] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[valuation]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[valuation]` executed under `dev/.venv/bin/python`, parameter case `valuation`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[valuation] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[estimate]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[estimate]` executed under `dev/.venv/bin/python`, parameter case `estimate`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[estimate] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[fair_value]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[fair_value]` executed under `dev/.venv/bin/python`, parameter case `fair_value`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[fair_value] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 is structural over subject matter[useful_life]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[useful_life]` executed under `dev/.venv/bin/python`, parameter case `useful_life`
- Expected: a19 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_is_structural_over_subject_matter[useful_life] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 prose leg[The allowance for doubtful accounts is adequate at the current level.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The allowance for doubtful accounts is adequate at the current level.]` executed under `dev/.venv/bin/python`, parameter case `The allowance for doubtful accounts is adequate at the current level.`
- Expected: a19 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The allowance for doubtful accounts is adequate at the current level.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 prose leg[No impairment is required for this asset group.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[No impairment is required for this asset group.]` executed under `dev/.venv/bin/python`, parameter case `No impairment is required for this asset group.`
- Expected: a19 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[No impairment is required for this asset group.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 prose leg[The reserve can be released given the improved ageing profile.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The reserve can be released given the improved ageing profile.]` executed under `dev/.venv/bin/python`, parameter case `The reserve can be released given the improved ageing profile.`
- Expected: a19 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The reserve can be released given the improved ageing profile.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a19 prose leg[The useful life remains appropriate.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The useful life remains appropriate.]` executed under `dev/.venv/bin/python`, parameter case `The useful life remains appropriate.`
- Expected: a19 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a19_prose_leg[The useful life remains appropriate.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 is unconditional[I hereby certify that the accompanying statements are complete.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[I hereby certify that the accompanying statements are complete.]` executed under `dev/.venv/bin/python`, parameter case `I hereby certify that the accompanying statements are complete.`
- Expected: a21 is unconditional
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[I hereby certify that the accompanying statements are complete.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 is unconditional[Signed off on behalf of the controller.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Signed off on behalf of the controller.]` executed under `dev/.venv/bin/python`, parameter case `Signed off on behalf of the controller.`
- Expected: a21 is unconditional
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Signed off on behalf of the controller.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 is unconditional[This satisfies the Section 302 requirement.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[This satisfies the Section 302 requirement.]` executed under `dev/.venv/bin/python`, parameter case `This satisfies the Section 302 requirement.`
- Expected: a21 is unconditional
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[This satisfies the Section 302 requirement.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 is unconditional[Internal control over financial reporting is effective as of period end.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Internal control over financial reporting is effective as of period end.]` executed under `dev/.venv/bin/python`, parameter case `Internal control over financial reporting is effective as of period end.`
- Expected: a21 is unconditional
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[Internal control over financial reporting is effective as of period end.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 is unconditional[The statements fairly present in all material respects the position.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[The statements fairly present in all material respects the position.]` executed under `dev/.venv/bin/python`, parameter case `The statements fairly present in all material respects the position.`
- Expected: a21 is unconditional
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_is_unconditional[The statements fairly present in all material respects the position.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a21 also fires on a structured certification claim
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a21_also_fires_on_a_structured_certification_claim` executed under `dev/.venv/bin/python`
- Expected: a21 also fires on a structured certification claim
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a21_also_fires_on_a_structured_certification_claim PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[cut_off]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[cut_off]` executed under `dev/.venv/bin/python`, parameter case `cut_off`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[cut_off] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[revenue_recognition]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[revenue_recognition]` executed under `dev/.venv/bin/python`, parameter case `revenue_recognition`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[revenue_recognition] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[lease_classification]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[lease_classification]` executed under `dev/.venv/bin/python`, parameter case `lease_classification`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[lease_classification] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[capitalisation]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[capitalisation]` executed under `dev/.venv/bin/python`, parameter case `capitalisation`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[capitalisation] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[consolidation]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[consolidation]` executed under `dev/.venv/bin/python`, parameter case `consolidation`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[consolidation] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 is structural over subject matter[technical_accounting]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[technical_accounting]` executed under `dev/.venv/bin/python`, parameter case `technical_accounting`
- Expected: a22 is structural over subject matter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_is_structural_over_subject_matter[technical_accounting] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 prose leg[Under ASC 606 this should be recognised over time.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Under ASC 606 this should be recognised over time.]` executed under `dev/.venv/bin/python`, parameter case `Under ASC 606 this should be recognised over time.`
- Expected: a22 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Under ASC 606 this should be recognised over time.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 prose leg[The cost should be capitalised rather than expensed.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The cost should be capitalised rather than expensed.]` executed under `dev/.venv/bin/python`, parameter case `The cost should be capitalised rather than expensed.`
- Expected: a22 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The cost should be capitalised rather than expensed.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 prose leg[This belongs in the prior period.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[This belongs in the prior period.]` executed under `dev/.venv/bin/python`, parameter case `This belongs in the prior period.`
- Expected: a22 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[This belongs in the prior period.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 prose leg[The lease is classified as a finance lease.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The lease is classified as a finance lease.]` executed under `dev/.venv/bin/python`, parameter case `The lease is classified as a finance lease.`
- Expected: a22 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[The lease is classified as a finance lease.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a22 prose leg[Cut-off was correct for this shipment.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Cut-off was correct for this shipment.]` executed under `dev/.venv/bin/python`, parameter case `Cut-off was correct for this shipment.`
- Expected: a22 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a22_prose_leg[Cut-off was correct for this shipment.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 structural leg fires when the ground is the agents own prior output
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_structural_leg_fires_when_the_ground_is_the_agents_own_prior_output` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-08 (A23). No adjudication of the agent's own prior output.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_structural_leg_fires_when_the_ground_is_the_agents_own_prior_output PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 does not fire when the prior conclusion is someone elses
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_does_not_fire_when_the_prior_conclusion_is_someone_elses` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-08's boundary: A23 is about the agent's OWN prior output.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_does_not_fire_when_the_prior_conclusion_is_someone_elses PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 prose leg[My prior conclusion was correct and the treatment stands.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[My prior conclusion was correct and the treatment stands.]` executed under `dev/.venv/bin/python`, parameter case `My prior conclusion was correct and the treatment stands.`
- Expected: a23 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[My prior conclusion was correct and the treatment stands.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 prose leg[Our previous assessment remains valid for this period.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[Our previous assessment remains valid for this period.]` executed under `dev/.venv/bin/python`, parameter case `Our previous assessment remains valid for this period.`
- Expected: a23 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[Our previous assessment remains valid for this period.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 prose leg[As I correctly concluded last period, this is a timing difference.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[As I correctly concluded last period, this is a timing difference.]` executed under `dev/.venv/bin/python`, parameter case `As I correctly concluded last period, this is a timing difference.`
- Expected: a23 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[As I correctly concluded last period, this is a timing difference.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 prose leg[This confirms my earlier analysis.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[This confirms my earlier analysis.]` executed under `dev/.venv/bin/python`, parameter case `This confirms my earlier analysis.`
- Expected: a23 prose leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_prose_leg[This confirms my earlier analysis.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a23 permits re presenting prior reasoning as context
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a23_permits_re_presenting_prior_reasoning_as_context` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-08's last clause: prior reasoning may be presented as context,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a23_permits_re_presenting_prior_reasoning_as_context PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[This reviewer is careless with accrual reversals.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This reviewer is careless with accrual reversals.]` executed under `dev/.venv/bin/python`, parameter case `This reviewer is careless with accrual reversals.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This reviewer is careless with accrual reversals.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[J. Doe appears to be rubber-stamping proposals.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[J. Doe appears to be rubber-stamping proposals.]` executed under `dev/.venv/bin/python`, parameter case `J. Doe appears to be rubber-stamping proposals.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[J. Doe appears to be rubber-stamping proposals.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[The performance of this reviewer has declined.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[The performance of this reviewer has declined.]` executed under `dev/.venv/bin/python`, parameter case `The performance of this reviewer has declined.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[The performance of this reviewer has declined.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[These are the best reviewers on the team.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[These are the best reviewers on the team.]` executed under `dev/.venv/bin/python`, parameter case `These are the best reviewers on the team.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[These are the best reviewers on the team.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[This approver should not be trusted with elevated-risk accounts.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This approver should not be trusted with elevated-risk accounts.]` executed under `dev/.venv/bin/python`, parameter case `This approver should not be trusted with elevated-risk accounts.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[This approver should not be trusted with elevated-risk accounts.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 catches characterisation[I would recommend re-assigning this queue.]
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[I would recommend re-assigning this queue.]` executed under `dev/.venv/bin/python`, parameter case `I would recommend re-assigning this queue.`
- Expected: COVERS AC-REFUSAL-09 (A24). No agent-generated judgement about a named person.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_catches_characterisation[I would recommend re-assigning this queue.] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 leaves the legitimate control metric alone
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_leaves_the_legitimate_control_metric_alone` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-09's last clause: AC-F41-07's platform-computed control
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_leaves_the_legitimate_control_metric_alone PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a24 fires on an unnamed characterisation too but records the weaker leg
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a24_fires_on_an_unnamed_characterisation_too_but_records_the_weaker_leg` executed under `dev/.venv/bin/python`
- Expected: a24 fires on an unnamed characterisation too but records the weaker leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a24_fires_on_an_unnamed_characterisation_too_but_records_the_weaker_leg PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a25 fires when the answer comes from a different metric than the request
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a25_fires_when_the_answer_comes_from_a_different_metric_than_the_request` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-10 (A25), the nearest-metric hole: an answer computed from an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a25_fires_when_the_answer_comes_from_a_different_metric_than_the_request PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a25 does not fire when the certified metric itself answered
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a25_does_not_fire_when_the_certified_metric_itself_answered` executed under `dev/.venv/bin/python`
- Expected: a25 does not fire when the certified metric itself answered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a25_does_not_fire_when_the_certified_metric_itself_answered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a25 refusal names what is missing and carries no substituted answer
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a25_refusal_names_what_is_missing_and_carries_no_substituted_answer` executed under `dev/.venv/bin/python`
- Expected: COVERS AC-REFUSAL-10's Then clause in full: names what is missing and returns
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a25_refusal_names_what_is_missing_and_carries_no_substituted_answer PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a refusal is not rendered as an error
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_a_refusal_is_not_rendered_as_an_error` executed under `dev/.venv/bin/python`
- Expected: a refusal is not rendered as an error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_a_refusal_is_not_rendered_as_an_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: refusal response refuses to be built with no refusals
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_refusal_response_refuses_to_be_built_with_no_refusals` executed under `dev/.venv/bin/python`
- Expected: refusal response refuses to be built with no refusals
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_refusal_response_refuses_to_be_built_with_no_refusals PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one emission can trip several refusals and all are reported
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_one_emission_can_trip_several_refusals_and_all_are_reported` executed under `dev/.venv/bin/python`
- Expected: one emission can trip several refusals and all are reported
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_one_emission_can_trip_several_refusals_and_all_are_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: hits are deduplicated per refusal and leg
- Status: EXECUTED
- Input: `backend/tests/test_refusal_registry.py::test_hits_are_deduplicated_per_refusal_and_leg` executed under `dev/.venv/bin/python`
- Expected: hits are deduplicated per refusal and leg
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_refusal_registry.py::test_hits_are_deduplicated_per_refusal_and_leg PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_registry_compiler.py`

### Scenario: the committed registry compiles
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_the_committed_registry_compiles` executed under `dev/.venv/bin/python`
- Expected: the committed registry compiles
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_the_committed_registry_compiles PASSED` (verbatim from the `-v` node list of this run)

### Scenario: registry hash is stable across recompiles
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_registry_hash_is_stable_across_recompiles` executed under `dev/.venv/bin/python`
- Expected: registry hash is stable across recompiles
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_registry_hash_is_stable_across_recompiles PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every committed query names an existing sql file
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_every_committed_query_names_an_existing_sql_file` executed under `dev/.venv/bin/python`
- Expected: every committed query names an existing sql file
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_every_committed_query_names_an_existing_sql_file PASSED` (verbatim from the `-v` node list of this run)

### Scenario: query ids are a closed sorted set
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_query_ids_are_a_closed_sorted_set` executed under `dev/.venv/bin/python`
- Expected: query ids are a closed sorted set
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_query_ids_are_a_closed_sorted_set PASSED` (verbatim from the `-v` node list of this run)

### Scenario: lookup by id and version
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_lookup_by_id_and_version` executed under `dev/.venv/bin/python`
- Expected: lookup by id and version
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_lookup_by_id_and_version PASSED` (verbatim from the `-v` node list of this run)

### Scenario: personal data columns and derived entitlement
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_personal_data_columns_and_derived_entitlement` executed under `dev/.venv/bin/python`
- Expected: personal data columns and derived entitlement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_personal_data_columns_and_derived_entitlement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unclassified columns are reported by name
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_unclassified_columns_are_reported_by_name` executed under `dev/.venv/bin/python`
- Expected: unclassified columns are reported by name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_unclassified_columns_are_reported_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: catalogue for omits rather than flags
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_catalogue_for_omits_rather_than_flags` executed under `dev/.venv/bin/python`
- Expected: catalogue for omits rather than flags
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_catalogue_for_omits_rather_than_flags PASSED` (verbatim from the `-v` node list of this run)

### Scenario: catalogue for handles no entitlements
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_catalogue_for_handles_no_entitlements` executed under `dev/.venv/bin/python`
- Expected: catalogue for handles no entitlements
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_catalogue_for_handles_no_entitlements PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a sql typed parameter fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_sql_typed_parameter_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a sql typed parameter fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_sql_typed_parameter_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a statement shaped parameter name fails the build[sql_text]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[sql_text]` executed under `dev/.venv/bin/python`, parameter case `sql_text`
- Expected: a statement shaped parameter name fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[sql_text] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a statement shaped parameter name fails the build[query_text]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[query_text]` executed under `dev/.venv/bin/python`, parameter case `query_text`
- Expected: a statement shaped parameter name fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[query_text] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a statement shaped parameter name fails the build[where_clause]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[where_clause]` executed under `dev/.venv/bin/python`, parameter case `where_clause`
- Expected: a statement shaped parameter name fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[where_clause] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a statement shaped parameter name fails the build[raw_predicate]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[raw_predicate]` executed under `dev/.venv/bin/python`, parameter case `raw_predicate`
- Expected: a statement shaped parameter name fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[raw_predicate] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a statement shaped parameter name fails the build[extra_filter_expression]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[extra_filter_expression]` executed under `dev/.venv/bin/python`, parameter case `extra_filter_expression`
- Expected: a statement shaped parameter name fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_statement_shaped_parameter_name_fails_the_build[extra_filter_expression] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing classification fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_classification_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a missing classification fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_missing_classification_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unrecognised classification fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_an_unrecognised_classification_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: an unrecognised classification fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_an_unrecognised_classification_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing sql file fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_sql_file_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a missing sql file fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_missing_sql_file_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an enum without a domain fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_an_enum_without_a_domain_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: an enum without a domain fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_an_enum_without_a_domain_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no columns fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_no_columns_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: no columns fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_no_columns_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a duplicate query ref fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_duplicate_query_ref_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a duplicate query ref fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_duplicate_query_ref_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty registry fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_an_empty_registry_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: an empty registry fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_an_empty_registry_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing queries directory fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_missing_queries_directory_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a missing queries directory fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_missing_queries_directory_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a query with no semantics block fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_query_with_no_semantics_block_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: `AC-F39-04` is only possible if the versions are declared. A default of
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_query_with_no_semantics_block_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a semantics block missing the joins key fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_semantics_block_missing_the_joins_key_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: An absent key and an empty list must not be the same thing: one is a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_semantics_block_missing_the_joins_key_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a semantics block with no metrics fails the build
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_semantics_block_with_no_metrics_fails_the_build` executed under `dev/.venv/bin/python`
- Expected: a semantics block with no metrics fails the build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_semantics_block_with_no_metrics_fails_the_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a metric without both an id and a version fails the build[{id: m}]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{id: m}]` executed under `dev/.venv/bin/python`, parameter case `{id: m}`
- Expected: A metric named without its version is exactly what the criterion
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{id: m}] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a metric without both an id and a version fails the build[{version: '1.0'}]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{version: '1.0'}]` executed under `dev/.venv/bin/python`, parameter case `{version: '1.0'}`
- Expected: A metric named without its version is exactly what the criterion
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{version: '1.0'}] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a metric without both an id and a version fails the build[{id: m, version: ''}]
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{id: m, version: ''}]` executed under `dev/.venv/bin/python`, parameter case `{id: m, version: ''}`
- Expected: A metric named without its version is exactly what the criterion
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_metric_without_both_an_id_and_a_version_fails_the_build[{id: m, version: ''}] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every committed query declares at least one versioned metric
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_every_committed_query_declares_at_least_one_versioned_metric` executed under `dev/.venv/bin/python`
- Expected: The whole registry, not a sample. A query added without semantics
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_every_committed_query_declares_at_least_one_versioned_metric PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the semantic versions payload states both kinds
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_the_semantic_versions_payload_states_both_kinds` executed under `dev/.venv/bin/python`
- Expected: the semantic versions payload states both kinds
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_the_semantic_versions_payload_states_both_kinds PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a query that traverses no join says so rather than rendering blank
- Status: EXECUTED
- Input: `backend/tests/test_registry_compiler.py::test_a_query_that_traverses_no_join_says_so_rather_than_rendering_blank` executed under `dev/.venv/bin/python`
- Expected: a query that traverses no join says so rather than rendering blank
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_registry_compiler.py::test_a_query_that_traverses_no_join_says_so_rather_than_rendering_blank PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_request_triage.py`

### Scenario: a request for a refused conclusion names its own A number[Assess the impairment on the Bakken CGU.-A19]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Assess the impairment on the Bakken CGU.-A19]` executed under `dev/.venv/bin/python`, parameter case `Assess the impairment on the Bakken CGU.-A19`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Assess the impairment on the Bakken CGU.-A19] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[What allowance should we carry on AR?-A19]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[What allowance should we carry on AR?-A19]` executed under `dev/.venv/bin/python`, parameter case `What allowance should we carry on AR?-A19`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[What allowance should we carry on AR?-A19] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[Is this difference material?-A20]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Is this difference material?-A20]` executed under `dev/.venv/bin/python`, parameter case `Is this difference material?-A20`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Is this difference material?-A20] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[Run the SAB 99 analysis for me.-A20]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Run the SAB 99 analysis for me.-A20]` executed under `dev/.venv/bin/python`, parameter case `Run the SAB 99 analysis for me.-A20`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Run the SAB 99 analysis for me.-A20] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[Can you certify the close is complete?-A21]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Can you certify the close is complete?-A21]` executed under `dev/.venv/bin/python`, parameter case `Can you certify the close is complete?-A21`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Can you certify the close is complete?-A21] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[I need a section 302 sign-off.-A21]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[I need a section 302 sign-off.-A21]` executed under `dev/.venv/bin/python`, parameter case `I need a section 302 sign-off.-A21`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[I need a section 302 sign-off.-A21] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[Should this cost be capitalised under ASC 360?-A22]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Should this cost be capitalised under ASC 360?-A22]` executed under `dev/.venv/bin/python`, parameter case `Should this cost be capitalised under ASC 360?-A22`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Should this cost be capitalised under ASC 360?-A22] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a refused conclusion names its own A number[Is the cut-off correct for this shipment?-A22]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Is the cut-off correct for this shipment?-A22]` executed under `dev/.venv/bin/python`, parameter case `Is the cut-off correct for this shipment?-A22`
- Expected: a request for a refused conclusion names its own A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_refused_conclusion_names_its_own_A_number[Is the cut-off correct for this shipment?-A22] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a refusal carries the registry s own ground and not a local copy
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_refusal_carries_the_registry_s_own_ground_and_not_a_local_copy` executed under `dev/.venv/bin/python`
- Expected: a refusal carries the registry s own ground and not a local copy
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_refusal_carries_the_registry_s_own_ground_and_not_a_local_copy PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Post this journal directly to Oracle.-posting.tier2]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Post this journal directly to Oracle.-posting.tier2]` executed under `dev/.venv/bin/python`, parameter case `Post this journal directly to Oracle.-posting.tier2`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Post this journal directly to Oracle.-posting.tier2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Reclassify this intercompany balance to the correct entity.-f33.legal_entity_and_intercompany]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Reclassify this intercompany balance to the correct entity.-f33.legal_entity_and_intercompany]` executed under `dev/.venv/bin/python`, parameter case `Reclassify this intercompany balance to the correct entity.-f33.legal_entity_and_intercompany`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Reclassify this intercompany balance to the correct entity.-f33.legal_entity_and_intercompany] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Correct the opex coding to capex on this batch.-f33.opex_capex_caption_crossing]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Correct the opex coding to capex on this batch.-f33.opex_capex_caption_crossing]` executed under `dev/.venv/bin/python`, parameter case `Correct the opex coding to capex on this batch.-f33.opex_capex_caption_crossing`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Correct the opex coding to capex on this batch.-f33.opex_capex_caption_crossing] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Reclass this invoice into the prior period.-f33.cutoff_resolution]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Reclass this invoice into the prior period.-f33.cutoff_resolution]` executed under `dev/.venv/bin/python`, parameter case `Reclass this invoice into the prior period.-f33.cutoff_resolution`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Reclass this invoice into the prior period.-f33.cutoff_resolution] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Is the period still open in Oracle?-erp.point_of_action_revalidation]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Is the period still open in Oracle?-erp.point_of_action_revalidation]` executed under `dev/.venv/bin/python`, parameter case `Is the period still open in Oracle?-erp.point_of_action_revalidation`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Is the period still open in Oracle?-erp.point_of_action_revalidation] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Decompose the variance on utilities.-f45.flux_driver_decomposition]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Decompose the variance on utilities.-f45.flux_driver_decomposition]` executed under `dev/.venv/bin/python`, parameter case `Decompose the variance on utilities.-f45.flux_driver_decomposition`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Decompose the variance on utilities.-f45.flux_driver_decomposition] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request for a deferred capability names that capability[Run blind re-performance on this skill.-f17.blind_reperformance]
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Run blind re-performance on this skill.-f17.blind_reperformance]` executed under `dev/.venv/bin/python`, parameter case `Run blind re-performance on this skill.-f17.blind_reperformance`
- Expected: a request for a deferred capability names that capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_for_a_deferred_capability_names_that_capability[Run blind re-performance on this skill.-f17.blind_reperformance] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request that trips neither is neither refused nor answered
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_that_trips_neither_is_neither_refused_nor_answered` executed under `dev/.venv/bin/python`
- Expected: a request that trips neither is neither refused nor answered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_that_trips_neither_is_neither_refused_nor_answered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the empty request is handled and is not a refusal
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_the_empty_request_is_handled_and_is_not_a_refusal` executed under `dev/.venv/bin/python`
- Expected: The boundary nobody types on purpose and everybody eventually posts.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_the_empty_request_is_handled_and_is_not_a_refusal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a request that is both refuses rather than defers
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_request_that_is_both_refuses_rather_than_defers` executed under `dev/.venv/bin/python`
- Expected: "Certify that this intercompany reclass is correct" is an A21 request
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_request_that_is_both_refuses_rather_than_defers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a materiality request cannot be defused by naming a deferred capability
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_materiality_request_cannot_be_defused_by_naming_a_deferred_capability` executed under `dev/.venv/bin/python`
- Expected: a materiality request cannot be defused by naming a deferred capability
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_materiality_request_cannot_be_defused_by_naming_a_deferred_capability PASSED` (verbatim from the `-v` node list of this run)

### Scenario: neither grammar contains the other s characteristic claim
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_neither_grammar_contains_the_other_s_characteristic_claim` executed under `dev/.venv/bin/python`
- Expected: `AC-REFUSAL-06`'s substance requirement, asserted rather than read.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_neither_grammar_contains_the_other_s_characteristic_claim PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a refusal carries no capability and a deferral carries no A number
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_a_refusal_carries_no_capability_and_a_deferral_carries_no_A_number` executed under `dev/.venv/bin/python`
- Expected: a refusal carries no capability and a deferral carries no A number
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_a_refusal_carries_no_capability_and_a_deferral_carries_no_A_number PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no outcome is an error and no outcome carries a figure
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_no_outcome_is_an_error_and_no_outcome_carries_a_figure` executed under `dev/.venv/bin/python`
- Expected: no outcome is an error and no outcome carries a figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_no_outcome_is_an_error_and_no_outcome_carries_a_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared capability has at least one trigger
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_every_declared_capability_has_at_least_one_trigger` executed under `dev/.venv/bin/python`
- Expected: A capability listed on the Refusals screen that nothing declines by
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_every_declared_capability_has_at_least_one_trigger PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every trigger family fires on a declared example
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_every_trigger_family_fires_on_a_declared_example` executed under `dev/.venv/bin/python`
- Expected: The real form of the check above: declared examples, one per family,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_every_trigger_family_fires_on_a_declared_example PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the published list carries no regex
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_the_published_list_carries_no_regex` executed under `dev/.venv/bin/python`
- Expected: `triggers` is an implementation detail. Publishing it would invite a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_the_published_list_carries_no_regex PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the outcome type refuses an outcome outside the closed set
- Status: EXECUTED
- Input: `backend/tests/test_request_triage.py::test_the_outcome_type_refuses_an_outcome_outside_the_closed_set` executed under `dev/.venv/bin/python`
- Expected: the outcome type refuses an outcome outside the closed set
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_request_triage.py::test_the_outcome_type_refuses_an_outcome_outside_the_closed_set PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_resolution_types.py`

### Scenario: there are exactly six types
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_there_are_exactly_six_types` executed under `dev/.venv/bin/python`
- Expected: there are exactly six types
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_there_are_exactly_six_types PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the set is closed
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_the_set_is_closed` executed under `dev/.venv/bin/python`
- Expected: the set is closed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_the_set_is_closed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every type declares a non empty evidence schema
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_every_type_declares_a_non_empty_evidence_schema` executed under `dev/.venv/bin/python`
- Expected: every type declares a non empty evidence schema
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_every_type_declares_a_non_empty_evidence_schema PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r1 requires an expiry
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_r1_requires_an_expiry` executed under `dev/.venv/bin/python`
- Expected: r1 requires an expiry
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_r1_requires_an_expiry PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r5 requires both a named owner and a due date
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_r5_requires_both_a_named_owner_and_a_due_date` executed under `dev/.venv/bin/python`
- Expected: r5 requires both a named owner and a due date
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_r5_requires_both_a_named_owner_and_a_due_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r6 requires the control state change itself
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_r6_requires_the_control_state_change_itself` executed under `dev/.venv/bin/python`
- Expected: r6 requires the control state change itself
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_r6_requires_the_control_state_change_itself PASSED` (verbatim from the `-v` node list of this run)

### Scenario: false is a held value not a missing one
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_false_is_a_held_value_not_a_missing_one` executed under `dev/.venv/bin/python`
- Expected: false is a held value not a missing one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_false_is_a_held_value_not_a_missing_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank field is not held[]
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a blank field is not held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank field is not held[   ]
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[   ]` executed under `dev/.venv/bin/python`, parameter case `   `
- Expected: a blank field is not held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[   ] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank field is not held[None]
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[None]` executed under `dev/.venv/bin/python`, parameter case `None`
- Expected: a blank field is not held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[None] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank field is not held[blank3]
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank3]` executed under `dev/.venv/bin/python`, parameter case `blank3`
- Expected: a blank field is not held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank field is not held[blank4]
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank4]` executed under `dev/.venv/bin/python`, parameter case `blank4`
- Expected: a blank field is not held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_blank_field_is_not_held[blank4] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r3 evidence does not satisfy from r2 evidence
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_r3_evidence_does_not_satisfy_from_r2_evidence` executed under `dev/.venv/bin/python`
- Expected: The specific substitution G-RESTYPE exists to stop.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_r3_evidence_does_not_satisfy_from_r2_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: require schema raises naming what is missing
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_require_schema_raises_naming_what_is_missing` executed under `dev/.venv/bin/python`
- Expected: require schema raises naming what is missing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_require_schema_raises_naming_what_is_missing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: recording the safe outcome costs no more than the posting outcome
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_recording_the_safe_outcome_costs_no_more_than_the_posting_outcome` executed under `dev/.venv/bin/python`
- Expected: recording the safe outcome costs no more than the posting outcome
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_recording_the_safe_outcome_costs_no_more_than_the_posting_outcome PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the interaction count is derived not declared
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_the_interaction_count_is_derived_not_declared` executed under `dev/.venv/bin/python`
- Expected: the interaction count is derived not declared
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_the_interaction_count_is_derived_not_declared PASSED` (verbatim from the `-v` node list of this run)

### Scenario: r3 and r4 are the posting capable types and the others are not
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_r3_and_r4_are_the_posting_capable_types_and_the_others_are_not` executed under `dev/.venv/bin/python`
- Expected: r3 and r4 are the posting capable types and the others are not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_r3_and_r4_are_the_posting_capable_types_and_the_others_are_not PASSED` (verbatim from the `-v` node list of this run)

### Scenario: posting capability is a property of the type not a setting
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_posting_capability_is_a_property_of_the_type_not_a_setting` executed under `dev/.venv/bin/python`
- Expected: posting capability is a property of the type not a setting
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_posting_capability_is_a_property_of_the_type_not_a_setting PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no resolution type posts anything itself
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_no_resolution_type_posts_anything_itself` executed under `dev/.venv/bin/python`
- Expected: no resolution type posts anything itself
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_no_resolution_type_posts_anything_itself PASSED` (verbatim from the `-v` node list of this run)

### Scenario: evidence supporting two types equally is reported as a tie
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_evidence_supporting_two_types_equally_is_reported_as_a_tie` executed under `dev/.venv/bin/python`
- Expected: The canonical failure: 'timing' and 'error pending correction' are both
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_evidence_supporting_two_types_equally_is_reported_as_a_tie PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a tie is computed over the schema not volunteered
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_a_tie_is_computed_over_the_schema_not_volunteered` executed under `dev/.venv/bin/python`
- Expected: Over the function BODY, not its source text -- the docstring says the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_a_tie_is_computed_over_the_schema_not_volunteered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: evidence supporting nothing is an empty list not a guess
- Status: EXECUTED
- Input: `backend/tests/test_resolution_types.py::test_evidence_supporting_nothing_is_an_empty_list_not_a_guess` executed under `dev/.venv/bin/python`
- Expected: evidence supporting nothing is an empty list not a guess
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_resolution_types.py::test_evidence_supporting_nothing_is_an_empty_list_not_a_guess PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_reversal_and_two_key.py`

### Scenario: a reversal payload carries every required key
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_payload_carries_every_required_key` executed under `dev/.venv/bin/python`
- Expected: a reversal payload carries every required key
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_payload_carries_every_required_key PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reversal states that it modified nothing
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_states_that_it_modified_nothing` executed under `dev/.venv/bin/python`
- Expected: a reversal states that it modified nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_states_that_it_modified_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reversal with no reason is refused[]
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_with_no_reason_is_refused[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a reversal with no reason is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_with_no_reason_is_refused[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reversal with no reason is refused[None]
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_with_no_reason_is_refused[None]` executed under `dev/.venv/bin/python`, parameter case `None`
- Expected: a reversal with no reason is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_reversal_with_no_reason_is_refused[None] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an origin outside the closed set is refused
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_an_origin_outside_the_closed_set_is_refused` executed under `dev/.venv/bin/python`
- Expected: an origin outside the closed set is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_an_origin_outside_the_closed_set_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared origin is accepted[customer_oracle_tenant]
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_every_declared_origin_is_accepted[customer_oracle_tenant]` executed under `dev/.venv/bin/python`, parameter case `customer_oracle_tenant`
- Expected: every declared origin is accepted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_every_declared_origin_is_accepted[customer_oracle_tenant] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every declared origin is accepted[customer_manual_journal]
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_every_declared_origin_is_accepted[customer_manual_journal]` executed under `dev/.venv/bin/python`, parameter case `customer_manual_journal`
- Expected: every declared origin is accepted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_every_declared_origin_is_accepted[customer_manual_journal] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the origin set is not empty
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_the_origin_set_is_not_empty` executed under `dev/.venv/bin/python`
- Expected: A `parametrize` over an empty collection collects zero tests and reports
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_the_origin_set_is_not_empty PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a written reversal is retrievable under its own record type
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_written_reversal_is_retrievable_under_its_own_record_type` executed under `dev/.venv/bin/python`
- Expected: a written reversal is retrievable under its own record type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_written_reversal_is_retrievable_under_its_own_record_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown payload version is refused
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_an_unknown_payload_version_is_refused` executed under `dev/.venv/bin/python`
- Expected: an unknown payload version is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_an_unknown_payload_version_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty linkage states the absence rather than rendering blank
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_an_empty_linkage_states_the_absence_rather_than_rendering_blank` executed under `dev/.venv/bin/python`
- Expected: an empty linkage states the absence rather than rendering blank
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_an_empty_linkage_states_the_absence_rather_than_rendering_blank PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a linkage names every reversal it found
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_linkage_names_every_reversal_it_found` executed under `dev/.venv/bin/python`
- Expected: a linkage names every reversal it found
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_linkage_names_every_reversal_it_found PASSED` (verbatim from the `-v` node list of this run)

### Scenario: for dossier returns only the reversals that name that dossier
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_for_dossier_returns_only_the_reversals_that_name_that_dossier` executed under `dev/.venv/bin/python`
- Expected: for dossier returns only the reversals that name that dossier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_for_dossier_returns_only_the_reversals_that_name_that_dossier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two reversals against one dossier are both linked
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_two_reversals_against_one_dossier_are_both_linked` executed under `dev/.venv/bin/python`
- Expected: A journal reversed and then re-reversed is two records, not a toggle.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_two_reversals_against_one_dossier_are_both_linked PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a linked reversal carries its own evidence position
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_linked_reversal_carries_its_own_evidence_position` executed under `dev/.venv/bin/python`
- Expected: a linked reversal carries its own evidence position
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_linked_reversal_carries_its_own_evidence_position PASSED` (verbatim from the `-v` node list of this run)

### Scenario: writing a reversal does not change the dossier s content hash
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_writing_a_reversal_does_not_change_the_dossier_s_content_hash` executed under `dev/.venv/bin/python`
- Expected: writing a reversal does not change the dossier s content hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_writing_a_reversal_does_not_change_the_dossier_s_content_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two key statement has all three clauses
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_the_two_key_statement_has_all_three_clauses` executed under `dev/.venv/bin/python`
- Expected: the two key statement has all three clauses
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_the_two_key_statement_has_all_three_clauses PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stated date is the OLDEST verification
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_the_stated_date_is_the_OLDEST_verification` executed under `dev/.venv/bin/python`
- Expected: The window closes on the earliest verification, not the most recent —
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_the_stated_date_is_the_OLDEST_verification PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a row with no verification date does not become the stated date
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_row_with_no_verification_date_does_not_become_the_stated_date` executed under `dev/.venv/bin/python`
- Expected: a row with no verification date does not become the stated date
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_row_with_no_verification_date_does_not_become_the_stated_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no rows states the absence rather than omitting the clause
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_no_rows_states_the_absence_rather_than_omitting_the_clause` executed under `dev/.venv/bin/python`
- Expected: no rows states the absence rather than omitting the clause
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_no_rows_states_the_absence_rather_than_omitting_the_clause PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a file built with no cuec rows still carries the three clauses
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_file_built_with_no_cuec_rows_still_carries_the_three_clauses` executed under `dev/.venv/bin/python`
- Expected: The default is the no-verification wording, not an empty dict: a file
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_file_built_with_no_cuec_rows_still_carries_the_three_clauses PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a failed build produces no object to present as complete
- Status: EXECUTED
- Input: `backend/tests/test_reversal_and_two_key.py::test_a_failed_build_produces_no_object_to_present_as_complete` executed under `dev/.venv/bin/python`
- Expected: `AC-F40-09`'s structural half: the failure path returns nothing, so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_reversal_and_two_key.py::test_a_failed_build_produces_no_object_to_present_as_complete PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_routing_budget.py`

### Scenario: at or under cap everything routes and nothing is recorded[0]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[0]` executed under `dev/.venv/bin/python`, parameter case `0`
- Expected: at or under cap everything routes and nothing is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at or under cap everything routes and nothing is recorded[1]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[1]` executed under `dev/.venv/bin/python`, parameter case `1`
- Expected: at or under cap everything routes and nothing is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at or under cap everything routes and nothing is recorded[2]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[2]` executed under `dev/.venv/bin/python`, parameter case `2`
- Expected: at or under cap everything routes and nothing is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[2] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at or under cap everything routes and nothing is recorded[3]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[3]` executed under `dev/.venv/bin/python`, parameter case `3`
- Expected: at or under cap everything routes and nothing is recorded
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_at_or_under_cap_everything_routes_and_nothing_is_recorded[3] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the budget event key is ABSENT under cap not null
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_the_budget_event_key_is_ABSENT_under_cap_not_null` executed under `dev/.venv/bin/python`
- Expected: `AC-F41-18` requires NO cap state on a night under cap. A null that
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_the_budget_event_key_is_ABSENT_under_cap_not_null PASSED` (verbatim from the `-v` node list of this run)

### Scenario: above cap the excess is HELD and returned rather than dropped
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_above_cap_the_excess_is_HELD_and_returned_rather_than_dropped` executed under `dev/.venv/bin/python`
- Expected: above cap the excess is HELD and returned rather than dropped
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_above_cap_the_excess_is_HELD_and_returned_rather_than_dropped PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the event states the reviewer the cap and how many were held
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_the_event_states_the_reviewer_the_cap_and_how_many_were_held` executed under `dev/.venv/bin/python`
- Expected: the event states the reviewer the cap and how many were held
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_the_event_states_the_reviewer_the_cap_and_how_many_were_held PASSED` (verbatim from the `-v` node list of this run)

### Scenario: routing the same night twice gives the same answer
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_routing_the_same_night_twice_gives_the_same_answer` executed under `dev/.venv/bin/python`
- Expected: A run that recorded consumption as it went would hold items on a re-run
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_routing_the_same_night_twice_gives_the_same_answer PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two reviewers have independent budgets
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_two_reviewers_have_independent_budgets` executed under `dev/.venv/bin/python`
- Expected: two reviewers have independent budgets
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_two_reviewers_have_independent_budgets PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two nights have independent budgets
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_two_nights_have_independent_budgets` executed under `dev/.venv/bin/python`
- Expected: two nights have independent budgets
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_two_nights_have_independent_budgets PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a controller raises the cap and the record carries everything
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_controller_raises_the_cap_and_the_record_carries_everything` executed under `dev/.venv/bin/python`
- Expected: a controller raises the cap and the record carries everything
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_controller_raises_the_cap_and_the_record_carries_everything PASSED` (verbatim from the `-v` node list of this run)

### Scenario: anybody other than a controller is rejected and the cap holds[human.platform.admin]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[human.platform.admin]` executed under `dev/.venv/bin/python`, parameter case `human.platform.admin`
- Expected: "At any permission level including administrator". `user.s.haddad` is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[human.platform.admin] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: anybody other than a controller is rejected and the cap holds[user.a.reyes]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.a.reyes]` executed under `dev/.venv/bin/python`, parameter case `user.a.reyes`
- Expected: "At any permission level including administrator". `user.s.haddad` is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.a.reyes] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: anybody other than a controller is rejected and the cap holds[user.j.mbeki]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.j.mbeki]` executed under `dev/.venv/bin/python`, parameter case `user.j.mbeki`
- Expected: "At any permission level including administrator". `user.s.haddad` is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.j.mbeki] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: anybody other than a controller is rejected and the cap holds[user.s.haddad]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.s.haddad]` executed under `dev/.venv/bin/python`, parameter case `user.s.haddad`
- Expected: "At any permission level including administrator". `user.s.haddad` is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[user.s.haddad] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: anybody other than a controller is rejected and the cap holds[agent.omission_detector@1]
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[agent.omission_detector@1]` executed under `dev/.venv/bin/python`, parameter case `agent.omission_detector@1`
- Expected: "At any permission level including administrator". `user.s.haddad` is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_anybody_other_than_a_controller_is_rejected_and_the_cap_holds[agent.omission_detector@1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the principals who may raise are exactly the controllers
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_the_principals_who_may_raise_are_exactly_the_controllers` executed under `dev/.venv/bin/python`
- Expected: The guard on the group above: a `parametrize` list that stopped naming
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_the_principals_who_may_raise_are_exactly_the_controllers PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a lowering dressed as a raise is refused
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_lowering_dressed_as_a_raise_is_refused` executed under `dev/.venv/bin/python`
- Expected: A LOWERING would pass an authority check written for raises and take
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_lowering_dressed_as_a_raise_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a raise to the same number is refused
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_raise_to_the_same_number_is_refused` executed under `dev/.venv/bin/python`
- Expected: a raise to the same number is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_raise_to_the_same_number_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a rejected raise emits a control event naming the standing cap
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_rejected_raise_emits_a_control_event_naming_the_standing_cap` executed under `dev/.venv/bin/python`
- Expected: a rejected raise emits a control event naming the standing cap
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_rejected_raise_emits_a_control_event_naming_the_standing_cap PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a raise applies to one reviewer on one night only
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_raise_applies_to_one_reviewer_on_one_night_only` executed under `dev/.venv/bin/python`
- Expected: a raise applies to one reviewer on one night only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_raise_applies_to_one_reviewer_on_one_night_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a raised cap changes what routes
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_a_raised_cap_changes_what_routes` executed under `dev/.venv/bin/python`
- Expected: a raised cap changes what routes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_a_raised_cap_changes_what_routes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no standing or permanent raise to construct
- Status: EXECUTED
- Input: `backend/tests/test_routing_budget.py::test_there_is_no_standing_or_permanent_raise_to_construct` executed under `dev/.venv/bin/python`
- Expected: A standing exemption is unrepresentable rather than rejected, in the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_routing_budget.py::test_there_is_no_standing_or_permanent_raise_to_construct PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_surveillance_primitives.py`

### Scenario: four consecutive sub threshold movements escalate
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_four_consecutive_sub_threshold_movements_escalate` executed under `dev/.venv/bin/python`
- Expected: four consecutive sub threshold movements escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_four_consecutive_sub_threshold_movements_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: three consecutive movements do not escalate and the record says how many more
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_movements_do_not_escalate_and_the_record_says_how_many_more` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-06`'s second half. A bare "no escalation" gives a controller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_movements_do_not_escalate_and_the_record_says_how_many_more PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the escalation period is where the run reached the count not the latest
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_escalation_period_is_where_the_run_reached_the_count_not_the_latest` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-01`: "the period number at which it escalated".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_escalation_period_is_where_the_run_reached_the_count_not_the_latest PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the aggregate covers the whole run not only up to the escalation
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_aggregate_covers_the_whole_run_not_only_up_to_the_escalation` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-02`: the figure a human acts on is the accumulated one.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_aggregate_covers_the_whole_run_not_only_up_to_the_escalation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the period delta is present and is not the headline
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_period_delta_is_present_and_is_not_the_headline` executed under `dev/.venv/bin/python`
- Expected: the period delta is present and is not the headline
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_period_delta_is_present_and_is_not_the_headline PASSED` (verbatim from the `-v` node list of this run)

### Scenario: alternating directions do not accumulate
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_alternating_directions_do_not_accumulate` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-07`. The same magnitudes; only the signs differ.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_alternating_directions_do_not_accumulate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a direction change breaks the run at exactly that period
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_direction_change_breaks_the_run_at_exactly_that_period` executed under `dev/.venv/bin/python`
- Expected: a direction change breaks the run at exactly that period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_direction_change_breaks_the_run_at_exactly_that_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a movement above the threshold breaks the run
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_movement_above_the_threshold_breaks_the_run` executed under `dev/.venv/bin/python`
- Expected: It is not part of an accumulation this control is about: an in-period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_movement_above_the_threshold_breaks_the_run PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a movement exactly at the threshold is not below it
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_movement_exactly_at_the_threshold_is_not_below_it` executed under `dev/.venv/bin/python`
- Expected: a movement exactly at the threshold is not below it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_movement_exactly_at_the_threshold_is_not_below_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period gap breaks the run because the periods are not consecutive
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_period_gap_breaks_the_run_because_the_periods_are_not_consecutive` executed under `dev/.venv/bin/python`
- Expected: a period gap breaks the run because the periods are not consecutive
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_period_gap_breaks_the_run_because_the_periods_are_not_consecutive PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a zero movement breaks the run rather than extending it
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_zero_movement_breaks_the_run_rather_than_extending_it` executed under `dev/.venv/bin/python`
- Expected: a zero movement breaks the run rather than extending it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_zero_movement_breaks_the_run_rather_than_extending_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an account with one period is not evaluable and names what it has
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_an_account_with_one_period_is_not_evaluable_and_names_what_it_has` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-05`. NOT "monitored and nothing found".
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_an_account_with_one_period_is_not_evaluable_and_names_what_it_has PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a declared account with no movements at all is not evaluable
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_declared_account_with_no_movements_at_all_is_not_evaluable` executed under `dev/.venv/bin/python`
- Expected: a declared account with no movements at all is not evaluable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_declared_account_with_no_movements_at_all_is_not_evaluable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a credit direction accumulation escalates and says so
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_credit_direction_accumulation_escalates_and_says_so` executed under `dev/.venv/bin/python`
- Expected: a credit direction accumulation escalates and says so
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_credit_direction_accumulation_escalates_and_says_so PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the consecutive count is configurable and the boundary is exact
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_consecutive_count_is_configurable_and_the_boundary_is_exact` executed under `dev/.venv/bin/python`
- Expected: the consecutive count is configurable and the boundary is exact
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_consecutive_count_is_configurable_and_the_boundary_is_exact PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the amounts are decimals end to end
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_amounts_are_decimals_end_to_end` executed under `dev/.venv/bin/python`
- Expected: the amounts are decimals end to end
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_amounts_are_decimals_end_to_end PASSED` (verbatim from the `-v` node list of this run)

### Scenario: three consecutive verbatim explanations escalate
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_verbatim_explanations_escalate` executed under `dev/.venv/bin/python`
- Expected: three consecutive verbatim explanations escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_three_consecutive_verbatim_explanations_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two consecutive verbatim explanations do not
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_two_consecutive_verbatim_explanations_do_not` executed under `dev/.venv/bin/python`
- Expected: two consecutive verbatim explanations do not
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_two_consecutive_verbatim_explanations_do_not PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the escalation quotes the recurring assertion
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_escalation_quotes_the_recurring_assertion` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-03`. A similarity score with no text beside it is a number a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_escalation_quotes_the_recurring_assertion PASSED` (verbatim from the `-v` node list of this run)

### Scenario: genuinely different explanations do not escalate
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_genuinely_different_explanations_do_not_escalate` executed under `dev/.venv/bin/python`
- Expected: genuinely different explanations do not escalate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_genuinely_different_explanations_do_not_escalate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reworded restatement still matches and a reordering certainly does
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_reworded_restatement_still_matches_and_a_reordering_certainly_does` executed under `dev/.venv/bin/python`
- Expected: Token SET, not sequence: reordering a sentence is the cheapest possible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_reworded_restatement_still_matches_and_a_reordering_certainly_does PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two empty explanations score zero rather than a perfect match
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_two_empty_explanations_score_zero_rather_than_a_perfect_match` executed under `dev/.venv/bin/python`
- Expected: The most misleading possible answer, refused.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_two_empty_explanations_score_zero_rather_than_a_perfect_match PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every number the narrative leg emits is hashable evidence
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_every_number_the_narrative_leg_emits_is_hashable_evidence` executed under `dev/.venv/bin/python`
- Expected: No floats anywhere on the path to a dossier.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_every_number_the_narrative_leg_emits_is_hashable_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a period with no recorded explanation makes the member unevaluable
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_period_with_no_recorded_explanation_makes_the_member_unevaluable` executed under `dev/.venv/bin/python`
- Expected: `AC-F9-09`, and the member is UNCOVERED so the conclusion is bounded.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_period_with_no_recorded_explanation_makes_the_member_unevaluable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing period is reported rather than bridged
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_a_missing_period_is_reported_rather_than_bridged` executed under `dev/.venv/bin/python`
- Expected: The alternative — comparing period 2 with period 5 as if adjacent —
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_a_missing_period_is_reported_rather_than_bridged PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an account with no explanation at all is named not silently skipped
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_an_account_with_no_explanation_at_all_is_named_not_silently_skipped` executed under `dev/.venv/bin/python`
- Expected: an account with no explanation at all is named not silently skipped
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_an_account_with_no_explanation_at_all_is_named_not_silently_skipped PASSED` (verbatim from the `-v` node list of this run)

### Scenario: one period of explanation cannot recur
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_one_period_of_explanation_cannot_recur` executed under `dev/.venv/bin/python`
- Expected: one period of explanation cannot recur
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_one_period_of_explanation_cannot_recur PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the similarity bound is inclusive at the bound
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_similarity_bound_is_inclusive_at_the_bound` executed under `dev/.venv/bin/python`
- Expected: the similarity bound is inclusive at the bound
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_similarity_bound_is_inclusive_at_the_bound PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the computation is deterministic and declares that it used no model
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_computation_is_deterministic_and_declares_that_it_used_no_model` executed under `dev/.venv/bin/python`
- Expected: the computation is deterministic and declares that it used no model
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_computation_is_deterministic_and_declares_that_it_used_no_model PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the narrative leg holds no model client and no network call
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_narrative_leg_holds_no_model_client_and_no_network_call` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §7.3: the similarity computation is deterministic.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_narrative_leg_holds_no_model_client_and_no_network_call PASSED` (verbatim from the `-v` node list of this run)

### Scenario: two separate recurring runs on one account are both reported
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_two_separate_recurring_runs_on_one_account_are_both_reported` executed under `dev/.venv/bin/python`
- Expected: Two spells of copy-forward with a real explanation between them.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_two_separate_recurring_runs_on_one_account_are_both_reported PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the run length boundary[2-0]
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[2-0]` executed under `dev/.venv/bin/python`, parameter case `2-0`
- Expected: the run length boundary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[2-0] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the run length boundary[3-1]
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[3-1]` executed under `dev/.venv/bin/python`, parameter case `3-1`
- Expected: the run length boundary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[3-1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the run length boundary[4-1]
- Status: EXECUTED
- Input: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[4-1]` executed under `dev/.venv/bin/python`, parameter case `4-1`
- Expected: the run length boundary
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_surveillance_primitives.py::test_the_run_length_boundary[4-1] PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_ask.py`

### Scenario: the entry point lands on ask
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_the_entry_point_lands_on_ask` executed under `dev/.venv/bin/python`
- Expected: `/` is where a user arrives; Ask is the screen they arrive at.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_the_entry_point_lands_on_ask PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ask is reachable by following links from the entry point
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_ask_is_reachable_by_following_links_from_the_entry_point` executed under `dev/.venv/bin/python`
- Expected: ask is reachable by following links from the entry point
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_ask_is_reachable_by_following_links_from_the_entry_point PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[nl-input]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[nl-input]` executed under `dev/.venv/bin/python`, parameter case `nl-input`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[nl-input] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[resolved-query]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolved-query]` executed under `dev/.venv/bin/python`, parameter case `resolved-query`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolved-query] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[declared-population-panel]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[declared-population-panel]` executed under `dev/.venv/bin/python`, parameter case `declared-population-panel`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[declared-population-panel] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[coverage-meter]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-meter]` executed under `dev/.venv/bin/python`, parameter case `coverage-meter`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-meter] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[ambiguity-fork]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[ambiguity-fork]` executed under `dev/.venv/bin/python`, parameter case `ambiguity-fork`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[ambiguity-fork] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[partial-run-banner]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]` executed under `dev/.venv/bin/python`, parameter case `partial-run-banner`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[run-submit]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[run-submit]` executed under `dev/.venv/bin/python`, parameter case `run-submit`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[run-submit] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[provenance]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[provenance]` executed under `dev/.venv/bin/python`, parameter case `provenance`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[provenance] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[pilot-strip]
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[pilot-strip]` executed under `dev/.venv/bin/python`, parameter case `pilot-strip`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[pilot-strip] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F39 09 all four required elements are on the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_09_all_four_required_elements_are_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: NL input, dataset selector, resolved certified-query name, coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_09_all_four_required_elements_are_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F39 01 the resolution carries its version and bound parameters
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_01_the_resolution_carries_its_version_and_bound_parameters` executed under `dev/.venv/bin/python`
- Expected: AC F39 01 the resolution carries its version and bound parameters
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_01_the_resolution_carries_its_version_and_bound_parameters PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F39 02 no control on this screen can carry sql
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_02_no_control_on_this_screen_can_carry_sql` executed under `dev/.venv/bin/python`
- Expected: The NL box parameterises a certified query. There is no field named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_02_no_control_on_this_screen_can_carry_sql PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F39 07 the ambiguity fork names both candidates and preselects neither
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_07_the_ambiguity_fork_names_both_candidates_and_preselects_neither` executed under `dev/.venv/bin/python`
- Expected: AC F39 07 the ambiguity fork names both candidates and preselects neither
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F39_07_the_ambiguity_fork_names_both_candidates_and_preselects_neither PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 14 the coverage meter states a percentage against the declaration
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_14_the_coverage_meter_states_a_percentage_against_the_declaration` executed under `dev/.venv/bin/python`
- Expected: AC F38 14 the coverage meter states a percentage against the declaration
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_14_the_coverage_meter_states_a_percentage_against_the_declaration PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 15 the partial banner names the coverage and the bound
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_15_the_partial_banner_names_the_coverage_and_the_bound` executed under `dev/.venv/bin/python`
- Expected: AC F38 15 the partial banner names the coverage and the bound
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestObservableUICriteria::test_AC_F38_15_the_partial_banner_names_the_coverage_and_the_bound PASSED` (verbatim from the `-v` node list of this run)

### Scenario: unselected segments are named individually not merely counted
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_unselected_segments_are_named_individually_not_merely_counted` executed under `dev/.venv/bin/python`
- Expected: unselected segments are named individually not merely counted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_unselected_segments_are_named_individually_not_merely_counted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: covered segments are named too so the declaration is readable whole
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_covered_segments_are_named_too_so_the_declaration_is_readable_whole` executed under `dev/.venv/bin/python`
- Expected: covered segments are named too so the declaration is readable whole
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_covered_segments_are_named_too_so_the_declaration_is_readable_whole PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no multiselect dropdown anywhere on the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_there_is_no_multiselect_dropdown_anywhere_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: there is no multiselect dropdown anywhere on the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheDeclaredPopulationInversion::test_there_is_no_multiselect_dropdown_anywhere_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the gaps are drawn as segments rather than as absent fill
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_gaps_are_drawn_as_segments_rather_than_as_absent_fill` executed under `dev/.venv/bin/python`
- Expected: the gaps are drawn as segments rather than as absent fill
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_gaps_are_drawn_as_segments_rather_than_as_absent_fill PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each gap segment carries a non colour carrier
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_each_gap_segment_carries_a_non_colour_carrier` executed under `dev/.venv/bin/python`
- Expected: `UX_KB` §3.2: a state carried by hue alone fails in greyscale, in
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_each_gap_segment_carries_a_non_colour_carrier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the strip has a text alternative for a screen reader
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_strip_has_a_text_alternative_for_a_screen_reader` executed under `dev/.venv/bin/python`
- Expected: the strip has a text alternative for a screen reader
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_the_strip_has_a_text_alternative_for_a_screen_reader PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no progress element and no progressbar role
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_there_is_no_progress_element_and_no_progressbar_role` executed under `dev/.venv/bin/python`
- Expected: there is no progress element and no progressbar role
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheCoverageStripIsNotAProgressBar::test_there_is_no_progress_element_and_no_progressbar_role PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the submit label states the coverage rather than reading run
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_the_submit_label_states_the_coverage_rather_than_reading_run` executed under `dev/.venv/bin/python`
- Expected: the submit label states the coverage rather than reading run
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_the_submit_label_states_the_coverage_rather_than_reading_run PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no control that dismisses the partial state
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_there_is_no_control_that_dismisses_the_partial_state` executed under `dev/.venv/bin/python`
- Expected: `AC-F38-10` / `UX_KB` §5.3: no affordance removes the state. The
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestTheSubmitControl::test_there_is_no_control_that_dismisses_the_partial_state PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no bulk action control on this screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_on_this_screen` executed under `dev/.venv/bin/python`
- Expected: there is no bulk action control on this screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_on_this_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no confidence or explanation quality surface
- Status: EXECUTED
- Input: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_confidence_or_explanation_quality_surface` executed under `dev/.venv/bin/python`
- Expected: there is no confidence or explanation quality surface
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_ask.py::TestNoRefusedAffordances::test_there_is_no_confidence_or_explanation_quality_surface PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_boundaries.py`

### Scenario: no ui module imports anything from ges
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_imports_anything_from_ges` executed under `dev/.venv/bin/python`
- Expected: no ui module imports anything from ges
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_imports_anything_from_ges PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no ui module compares an approver against an author or an invoker
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_compares_an_approver_against_an_author_or_an_invoker` executed under `dev/.venv/bin/python`
- Expected: The authorship closure is the broker's. The UI renders the decision
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_no_ui_module_compares_an_approver_against_an_author_or_an_invoker PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screens render eligibility from a carried payload
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_screens_render_eligibility_from_a_carried_payload` executed under `dev/.venv/bin/python`
- Expected: The positive half: the decision arrives as data with a decision id,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_screens_render_eligibility_from_a_carried_payload PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the boundary note is rendered on the screens that show broker facts
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_boundary_note_is_rendered_on_the_screens_that_show_broker_facts` executed under `dev/.venv/bin/python`
- Expected: the boundary note is rendered on the screens that show broker facts
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestTheTrustBoundaryHolds::test_the_boundary_note_is_rendered_on_the_screens_that_show_broker_facts PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the component library defines no bulk affordance
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_the_component_library_defines_no_bulk_affordance` executed under `dev/.venv/bin/python`
- Expected: the component library defines no bulk affordance
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_the_component_library_defines_no_bulk_affordance PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no screen in the build renders a checkbox or a select
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_in_the_build_renders_a_checkbox_or_a_select` executed under `dev/.venv/bin/python`
- Expected: no screen in the build renders a checkbox or a select
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_in_the_build_renders_a_checkbox_or_a_select PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no screen offers a keyboard shortcut for a bulk action
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_offers_a_keyboard_shortcut_for_a_bulk_action` executed under `dev/.venv/bin/python`
- Expected: no screen offers a keyboard shortcut for a bulk action
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_no_screen_offers_a_keyboard_shortcut_for_a_bulk_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at most one approve control exists across the entire surface
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_at_most_one_approve_control_exists_across_the_entire_surface` executed under `dev/.venv/bin/python`
- Expected: at most one approve control exists across the entire surface
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoBulkActionComponentExists::test_at_most_one_approve_control_exists_across_the_entire_surface PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no form control on any screen is named for sql
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_form_control_on_any_screen_is_named_for_sql` executed under `dev/.venv/bin/python`
- Expected: no form control on any screen is named for sql
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_form_control_on_any_screen_is_named_for_sql PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no ui module builds or holds a sql string
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_ui_module_builds_or_holds_a_sql_string` executed under `dev/.venv/bin/python`
- Expected: no ui module builds or holds a sql string
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_no_ui_module_builds_or_holds_a_sql_string PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the ask screen names the certified query it resolved to
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_the_ask_screen_names_the_certified_query_it_resolved_to` executed under `dev/.venv/bin/python`
- Expected: the ask screen names the certified query it resolved to
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoSqlSurface::test_the_ask_screen_names_the_certified_query_it_resolved_to PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every route the app serves is reachable from the entry point
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_route_the_app_serves_is_reachable_from_the_entry_point` executed under `dev/.venv/bin/python`
- Expected: every route the app serves is reachable from the entry point
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_route_the_app_serves_is_reachable_from_the_entry_point PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every parameterised screen is reached by following a real link
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_parameterised_screen_is_reached_by_following_a_real_link` executed under `dev/.venv/bin/python`
- Expected: every parameterised screen is reached by following a real link
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_parameterised_screen_is_reached_by_following_a_real_link PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every component the library defines appears on some reachable screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_component_the_library_defines_appears_on_some_reachable_screen` executed under `dev/.venv/bin/python`
- Expected: Walks the whole reachable surface, collects every `data-testid`
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_every_component_the_library_defines_appears_on_some_reachable_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the write path components appear only after the control is used
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_write_path_components_appear_only_after_the_control_is_used` executed under `dev/.venv/bin/python`
- Expected: The negative half of the check above, and the one that makes it mean
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_write_path_components_appear_only_after_the_control_is_used PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the entry point reaches every navigation destination
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_entry_point_reaches_every_navigation_destination` executed under `dev/.venv/bin/python`
- Expected: the entry point reaches every navigation destination
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::test_the_entry_point_reaches_every_navigation_destination PASSED` (verbatim from the `-v` node list of this run)

### Scenario: not one screen in the build carries a script or an event handler
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_not_one_screen_in_the_build_carries_a_script_or_an_event_handler` executed under `dev/.venv/bin/python`
- Expected: not one screen in the build carries a script or an event handler
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_not_one_screen_in_the_build_carries_a_script_or_an_event_handler PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no screen carries a meta refresh or an auto updating region
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_no_screen_carries_a_meta_refresh_or_an_auto_updating_region` executed under `dev/.venv/bin/python`
- Expected: no screen carries a meta refresh or an auto updating region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoScriptAnywhereOnTheSurface::test_no_screen_carries_a_meta_refresh_or_an_auto_updating_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no rendered page contains a colour in the green band
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_rendered_page_contains_a_colour_in_the_green_band` executed under `dev/.venv/bin/python`
- Expected: no rendered page contains a colour in the green band
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_rendered_page_contains_a_colour_in_the_green_band PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no named css green appears in any response
- Status: EXECUTED
- Input: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_named_css_green_appears_in_any_response` executed under `dev/.venv/bin/python`
- Expected: no named css green appears in any response
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_boundaries.py::TestNoGreenReachesAScreen::test_no_named_css_green_appears_in_any_response PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_chrome.py`

### Scenario: the document carries its own stylesheet
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_document_carries_its_own_stylesheet` executed under `dev/.venv/bin/python`
- Expected: the document carries its own stylesheet
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_document_carries_its_own_stylesheet PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no external stylesheet or font or image fetch
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_external_stylesheet_or_font_or_image_fetch` executed under `dev/.venv/bin/python`
- Expected: there is no external stylesheet or font or image fetch
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_external_stylesheet_or_font_or_image_fetch PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no script anywhere
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_script_anywhere` executed under `dev/.venv/bin/python`
- Expected: `UX_KB` §5.4: nothing may be reachable only by hover, lazy load or a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_there_is_no_script_anywhere PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the doctype is first
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_doctype_is_first` executed under `dev/.venv/bin/python`
- Expected: the doctype is first
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestSelfContainment::test_the_doctype_is_first PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every nav entry points at a route this build serves
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_every_nav_entry_points_at_a_route_this_build_serves` executed under `dev/.venv/bin/python`
- Expected: every nav entry points at a route this build serves
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestNavigation::test_every_nav_entry_points_at_a_route_this_build_serves PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the active item is marked for assistive technology too
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_the_active_item_is_marked_for_assistive_technology_too` executed under `dev/.venv/bin/python`
- Expected: the active item is marked for assistive technology too
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestNavigation::test_the_active_item_is_marked_for_assistive_technology_too PASSED` (verbatim from the `-v` node list of this run)

### Scenario: badges render the number routed not the number detected
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_badges_render_the_number_routed_not_the_number_detected` executed under `dev/.venv/bin/python`
- Expected: badges render the number routed not the number detected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestNavigation::test_badges_render_the_number_routed_not_the_number_detected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missing badge renders no count rather than zero
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestNavigation::test_a_missing_badge_renders_no_count_rather_than_zero` executed under `dev/.venv/bin/python`
- Expected: An absent badge and a badge reading 0 are different facts.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestNavigation::test_a_missing_badge_renders_no_count_rather_than_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every chromed page carries entity period close day and as of
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_every_chromed_page_carries_entity_period_close_day_and_as_of` executed under `dev/.venv/bin/python`
- Expected: every chromed page carries entity period close day and as of
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_every_chromed_page_carries_entity_period_close_day_and_as_of PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the pilot strip states the data is synthetic in words
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_pilot_strip_states_the_data_is_synthetic_in_words` executed under `dev/.venv/bin/python`
- Expected: `UX_KB` §3.2: an uncertified state is carried by a hatch AND a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_pilot_strip_states_the_data_is_synthetic_in_words PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the evidential view drops the shell but keeps the stylesheet
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet` executed under `dev/.venv/bin/python`
- Expected: the evidential view drops the shell but keeps the stylesheet
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the riskiest size strictly exceeds the ceiling for everything else
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_the_riskiest_size_strictly_exceeds_the_ceiling_for_everything_else` executed under `dev/.venv/bin/python`
- Expected: the riskiest size strictly exceeds the ceiling for everything else
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_the_riskiest_size_strictly_exceeds_the_ceiling_for_everything_else PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no declared pixel font size in the stylesheet reaches the riskiest size
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_no_declared_pixel_font_size_in_the_stylesheet_reaches_the_riskiest_size` executed under `dev/.venv/bin/python`
- Expected: no declared pixel font size in the stylesheet reaches the riskiest size
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_no_declared_pixel_font_size_in_the_stylesheet_reaches_the_riskiest_size PASSED` (verbatim from the `-v` node list of this run)

### Scenario: exactly one rule declares the riskiest size
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_exactly_one_rule_declares_the_riskiest_size` executed under `dev/.venv/bin/python`
- Expected: exactly one rule declares the riskiest size
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestTypeSizeIsAControl::test_exactly_one_rule_declares_the_riskiest_size PASSED` (verbatim from the `-v` node list of this run)

### Scenario: importing chrome has already asserted no green
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_importing_chrome_has_already_asserted_no_green` executed under `dev/.venv/bin/python`
- Expected: importing chrome has already asserted no green
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_importing_chrome_has_already_asserted_no_green PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stylesheet carries both themes
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_the_stylesheet_carries_both_themes` executed under `dev/.venv/bin/python`
- Expected: the stylesheet carries both themes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_the_stylesheet_carries_both_themes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no literal hex colour appears outside the token block
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_no_literal_hex_colour_appears_outside_the_token_block` executed under `dev/.venv/bin/python`
- Expected: Colours enter the stylesheet as variables. A literal hex in a rule
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestPaletteInvariantRunsAtImport::test_no_literal_hex_colour_appears_outside_the_token_block PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rendered page contains exactly the tree
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_the_rendered_page_contains_exactly_the_tree` executed under `dev/.venv/bin/python`
- Expected: the rendered page contains exactly the tree
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_the_rendered_page_contains_exactly_the_tree PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a component absent from the tree is absent from the markup
- Status: EXECUTED
- Input: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_a_component_absent_from_the_tree_is_absent_from_the_markup` executed under `dev/.venv/bin/python`
- Expected: a component absent from the tree is absent from the markup
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_chrome.py::TestPageAndTreeAgree::test_a_component_absent_from_the_tree_is_absent_from_the_markup PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_dossier.py`

### Scenario: a dossier is reachable from the entry point by following links
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_a_dossier_is_reachable_from_the_entry_point_by_following_links` executed under `dev/.venv/bin/python`
- Expected: a dossier is reachable from the entry point by following links
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_a_dossier_is_reachable_from_the_entry_point_by_following_links PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the review screen links to this dossier
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_the_review_screen_links_to_this_dossier` executed under `dev/.venv/bin/python`
- Expected: the review screen links to this dossier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_the_review_screen_links_to_this_dossier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every item in the pilot close has a reachable dossier
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_every_item_in_the_pilot_close_has_a_reachable_dossier` executed under `dev/.venv/bin/python`
- Expected: every item in the pilot close has a reachable dossier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_every_item_in_the_pilot_close_has_a_reachable_dossier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[dossier-header]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-header]` executed under `dev/.venv/bin/python`, parameter case `dossier-header`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-header] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[risk-band]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]` executed under `dev/.venv/bin/python`, parameter case `risk-band`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[riskiest-figure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]` executed under `dev/.venv/bin/python`, parameter case `riskiest-figure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[evidence-set]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set]` executed under `dev/.venv/bin/python`, parameter case `evidence-set`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[in-force-panel]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel]` executed under `dev/.venv/bin/python`, parameter case `in-force-panel`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[authorship-closure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]` executed under `dev/.venv/bin/python`, parameter case `authorship-closure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[conclusion-bounded]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]` executed under `dev/.venv/bin/python`, parameter case `conclusion-bounded`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[coverage-strip]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip]` executed under `dev/.venv/bin/python`, parameter case `coverage-strip`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[agent-narrative]
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative]` executed under `dev/.venv/bin/python`, parameter case `agent-narrative`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stylesheet is inlined
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_stylesheet_is_inlined` executed under `dev/.venv/bin/python`
- Expected: the stylesheet is inlined
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_stylesheet_is_inlined PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no external reference of any kind
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_there_is_no_external_reference_of_any_kind` executed under `dev/.venv/bin/python`
- Expected: there is no external reference of any kind
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_there_is_no_external_reference_of_any_kind PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it carries no application navigation
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_it_carries_no_application_navigation` executed under `dev/.venv/bin/python`
- Expected: It is an exhibit, not a screenshot of a running application.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_it_carries_no_application_navigation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every remaining link is absent so the file opens standalone
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_every_remaining_link_is_absent_so_the_file_opens_standalone` executed under `dev/.venv/bin/python`
- Expected: every remaining link is absent so the file opens standalone
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_every_remaining_link_is_absent_so_the_file_opens_standalone PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the document is a complete html document
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_document_is_a_complete_html_document` executed under `dev/.venv/bin/python`
- Expected: the document is a complete html document
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItIsAStandaloneExhibit::test_the_document_is_a_complete_html_document PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the figures the threshold and the bundle version are all in it
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_figures_the_threshold_and_the_bundle_version_are_all_in_it` executed under `dev/.venv/bin/python`
- Expected: the figures the threshold and the bundle version are all in it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_figures_the_threshold_and_the_bundle_version_are_all_in_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the evidence table is reproduced row for row
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_evidence_table_is_reproduced_row_for_row` executed under `dev/.venv/bin/python`
- Expected: the evidence table is reproduced row for row
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_evidence_table_is_reproduced_row_for_row PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the runs coverage statement travels with the dossier
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_runs_coverage_statement_travels_with_the_dossier` executed under `dev/.venv/bin/python`
- Expected: `AC-F29-11`: a finding can never be read detached from the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_runs_coverage_statement_travels_with_the_dossier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the retention expiry is stated
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_retention_expiry_is_stated` executed under `dev/.venv/bin/python`
- Expected: the retention expiry is stated
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_retention_expiry_is_stated PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the dossier names its run and its item
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_dossier_names_its_run_and_its_item` executed under `dev/.venv/bin/python`
- Expected: the dossier names its run and its item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestItReproducesWhatWasDisplayed::test_the_dossier_names_its_run_and_its_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no title attribute carries data
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_no_title_attribute_carries_data` executed under `dev/.venv/bin/python`
- Expected: no title attribute carries data
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_no_title_attribute_carries_data PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the narrative is present in the document even though it is collapsed
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_the_narrative_is_present_in_the_document_even_though_it_is_collapsed` executed under `dev/.venv/bin/python`
- Expected: Collapsed is not absent. The reviewer's decision not to open it is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestNothingWasHoverOnly::test_the_narrative_is_present_in_the_document_even_though_it_is_collapsed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an auto disposed items dossier carries the rule and the bundle hash
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_an_auto_disposed_items_dossier_carries_the_rule_and_the_bundle_hash` executed under `dev/.venv/bin/python`
- Expected: an auto disposed items dossier carries the rule and the bundle hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_an_auto_disposed_items_dossier_carries_the_rule_and_the_bundle_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it states what the rule did in words
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_it_states_what_the_rule_did_in_words` executed under `dev/.venv/bin/python`
- Expected: it states what the rule did in words
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_it_states_what_the_rule_did_in_words PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a normally routed item carries no auto disposal record
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_a_normally_routed_item_carries_no_auto_disposal_record` executed under `dev/.venv/bin/python`
- Expected: a normally routed item carries no auto disposal record
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestTheAutoDisposalRecord::test_a_normally_routed_item_carries_no_auto_disposal_record PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstained items dossier records the abstention as such
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_the_abstained_items_dossier_records_the_abstention_as_such` executed under `dev/.venv/bin/python`
- Expected: the abstained items dossier records the abstention as such
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_the_abstained_items_dossier_records_the_abstention_as_such PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it does not read as a finding that nothing was wrong
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_it_does_not_read_as_a_finding_that_nothing_was_wrong` executed under `dev/.venv/bin/python`
- Expected: it does not read as a finding that nothing was wrong
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestAbstentionSurvivesIntoTheEvidence::test_it_does_not_read_as_a_finding_that_nothing_was_wrong PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the coverage gaps carry a hatch as well as a colour
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_coverage_gaps_carry_a_hatch_as_well_as_a_colour` executed under `dev/.venv/bin/python`
- Expected: the coverage gaps carry a hatch as well as a colour
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_coverage_gaps_carry_a_hatch_as_well_as_a_colour PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the risk band states its tier in words not only in colour
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_risk_band_states_its_tier_in_words_not_only_in_colour` executed under `dev/.venv/bin/python`
- Expected: the risk band states its tier in words not only in colour
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_the_risk_band_states_its_tier_in_words_not_only_in_colour PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no state in the document is expressed only as an inline colour
- Status: EXECUTED
- Input: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_no_state_in_the_document_is_expressed_only_as_an_inline_colour` executed under `dev/.venv/bin/python`
- Expected: An inline `style` carrying a colour and no accompanying text is a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_dossier.py::TestGreyscaleSurvival::test_no_state_in_the_document_is_expressed_only_as_an_inline_colour PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_exceptions.py`

### Scenario: exceptions is reachable from the entry point by following links
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_exceptions_is_reachable_from_the_entry_point_by_following_links` executed under `dev/.venv/bin/python`
- Expected: exceptions is reachable from the entry point by following links
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_exceptions_is_reachable_from_the_entry_point_by_following_links PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[volume-masthead]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[volume-masthead]` executed under `dev/.venv/bin/python`, parameter case `volume-masthead`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[volume-masthead] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[detections-count]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[detections-count]` executed under `dev/.venv/bin/python`, parameter case `detections-count`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[detections-count] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[routed-count]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[routed-count]` executed under `dev/.venv/bin/python`, parameter case `routed-count`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[routed-count] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[partial-run-banner]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner]` executed under `dev/.venv/bin/python`, parameter case `partial-run-banner`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[partial-run-banner] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[conclusion-bounded]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded]` executed under `dev/.venv/bin/python`, parameter case `conclusion-bounded`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[conclusion-bounded] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[coverage-strip]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip]` executed under `dev/.venv/bin/python`, parameter case `coverage-strip`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[coverage-strip] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[exception-queue]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-queue]` executed under `dev/.venv/bin/python`, parameter case `exception-queue`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-queue] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[exception-row]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-row]` executed under `dev/.venv/bin/python`, parameter case `exception-row`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[exception-row] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[kind-pill]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[kind-pill]` executed under `dev/.venv/bin/python`, parameter case `kind-pill`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[kind-pill] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[risk-pill]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-pill]` executed under `dev/.venv/bin/python`, parameter case `risk-pill`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-pill] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[auto-disposed-marker]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[auto-disposed-marker]` executed under `dev/.venv/bin/python`, parameter case `auto-disposed-marker`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[auto-disposed-marker] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[abstention-region]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-region]` executed under `dev/.venv/bin/python`, parameter case `abstention-region`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-region] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[abstention-block]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-block]` executed under `dev/.venv/bin/python`, parameter case `abstention-block`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[abstention-block] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[boundary-check-table]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[boundary-check-table]` executed under `dev/.venv/bin/python`, parameter case `boundary-check-table`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[boundary-check-table] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[check-not-run]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[check-not-run]` executed under `dev/.venv/bin/python`, parameter case `check-not-run`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[check-not-run] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[recall-bias-label]
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[recall-bias-label]` executed under `dev/.venv/bin/python`, parameter case `recall-bias-label`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[recall-bias-label] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 09 both N and M are visible without leaving the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_AC_F41_09_both_N_and_M_are_visible_without_leaving_the_screen` executed under `dev/.venv/bin/python`
- Expected: AC F41 09 both N and M are visible without leaving the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_AC_F41_09_both_N_and_M_are_visible_without_leaving_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the ratio is the masthead and precedes the queue
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_ratio_is_the_masthead_and_precedes_the_queue` executed under `dev/.venv/bin/python`
- Expected: the ratio is the masthead and precedes the queue
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_ratio_is_the_masthead_and_precedes_the_queue PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the disposition of everything not routed is stated
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_disposition_of_everything_not_routed_is_stated` executed under `dev/.venv/bin/python`
- Expected: the disposition of everything not routed is stated
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestVolumeReduction::test_the_disposition_of_everything_not_routed_is_stated PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an omission finding is labelled as one
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_an_omission_finding_is_labelled_as_one` executed under `dev/.venv/bin/python`
- Expected: an omission finding is labelled as one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_an_omission_finding_is_labelled_as_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a present anomaly finding is labelled as one
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_a_present_anomaly_finding_is_labelled_as_one` executed under `dev/.venv/bin/python`
- Expected: a present anomaly finding is labelled as one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_a_present_anomaly_finding_is_labelled_as_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two labels differ in words and not only in style
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_two_labels_differ_in_words_and_not_only_in_style` executed under `dev/.venv/bin/python`
- Expected: the two labels differ in words and not only in style
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_two_labels_differ_in_words_and_not_only_in_style PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the omission finding shows the expected entry history that grounds it
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_omission_finding_shows_the_expected_entry_history_that_grounds_it` executed under `dev/.venv/bin/python`
- Expected: the omission finding shows the expected entry history that grounds it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestTheWedgeIsVisuallyDistinct::test_the_omission_finding_shows_the_expected_entry_history_that_grounds_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: rows are ordered by risk descending
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_rows_are_ordered_by_risk_descending` executed under `dev/.venv/bin/python`
- Expected: rows are ordered by risk descending
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_rows_are_ordered_by_risk_descending PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the band is a structural left bar not a legend dependent dot
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_the_band_is_a_structural_left_bar_not_a_legend_dependent_dot` executed under `dev/.venv/bin/python`
- Expected: the band is a structural left bar not a legend dependent dot
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_the_band_is_a_structural_left_bar_not_a_legend_dependent_dot PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there are never more than three risk steps on screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_there_are_never_more_than_three_risk_steps_on_screen` executed under `dev/.venv/bin/python`
- Expected: there are never more than three risk steps on screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_there_are_never_more_than_three_risk_steps_on_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no numeric risk score is rendered
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_no_numeric_risk_score_is_rendered` executed under `dev/.venv/bin/python`
- Expected: no numeric risk score is rendered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestRiskGrading::test_no_numeric_risk_score_is_rendered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: all five boundary checks render an individual result
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_all_five_boundary_checks_render_an_individual_result` executed under `dev/.venv/bin/python`
- Expected: all five boundary checks render an individual result
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_all_five_boundary_checks_render_an_individual_result PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a check that could not run says not run and names the missing dataset
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_a_check_that_could_not_run_says_not_run_and_names_the_missing_dataset` executed under `dev/.venv/bin/python`
- Expected: One check, and it is not run because a warehouse object is ABSENT.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_a_check_that_could_not_run_says_not_run_and_names_the_missing_dataset PASSED` (verbatim from the `-v` node list of this run)

### Scenario: not run is rendered in risk colour rather than neutral
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_not_run_is_rendered_in_risk_colour_rather_than_neutral` executed under `dev/.venv/bin/python`
- Expected: not run is rendered in risk colour rather than neutral
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestSilenceIsNeverAPass::test_not_run_is_rendered_in_risk_colour_rather_than_neutral PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstention is rendered outside the findings queue
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstention_is_rendered_outside_the_findings_queue` executed under `dev/.venv/bin/python`
- Expected: the abstention is rendered outside the findings queue
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstention_is_rendered_outside_the_findings_queue PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstained item has no row in the findings queue at all
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_has_no_row_in_the_findings_queue_at_all` executed under `dev/.venv/bin/python`
- Expected: Not merely styled differently inside the queue: absent from it. An
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_has_no_row_in_the_findings_queue_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstained item is still routed to a human
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_is_still_routed_to_a_human` executed under `dev/.venv/bin/python`
- Expected: the abstained item is still routed to a human
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_abstained_item_is_still_routed_to_a_human PASSED` (verbatim from the `-v` node list of this run)

### Scenario: its rag state is unknown and it declares it is not a finding
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_its_rag_state_is_unknown_and_it_declares_it_is_not_a_finding` executed under `dev/.venv/bin/python`
- Expected: its rag state is unknown and it declares it is not a finding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_its_rag_state_is_unknown_and_it_declares_it_is_not_a_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it names its evidence gap and exactly one resolving action
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_names_its_evidence_gap_and_exactly_one_resolving_action` executed under `dev/.venv/bin/python`
- Expected: it names its evidence gap and exactly one resolving action
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_names_its_evidence_gap_and_exactly_one_resolving_action PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is structurally distinct from a finding row not only worded differently
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_is_structurally_distinct_from_a_finding_row_not_only_worded_differently` executed under `dev/.venv/bin/python`
- Expected: it is structurally distinct from a finding row not only worded differently
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_it_is_structurally_distinct_from_a_finding_row_not_only_worded_differently PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the region explains why it is listed apart
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_region_explains_why_it_is_listed_apart` executed under `dev/.venv/bin/python`
- Expected: the region explains why it is listed apart
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAbstentionIsNotANegativeFinding::test_the_region_explains_why_it_is_listed_apart PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the auto disposed finding is visible in the list
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_auto_disposed_finding_is_visible_in_the_list` executed under `dev/.venv/bin/python`
- Expected: the auto disposed finding is visible in the list
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_auto_disposed_finding_is_visible_in_the_list PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it names the rule that disposed it and the bundle hash
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_it_names_the_rule_that_disposed_it_and_the_bundle_hash` executed under `dev/.venv/bin/python`
- Expected: it names the rule that disposed it and the bundle hash
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_it_names_the_rule_that_disposed_it_and_the_bundle_hash PASSED` (verbatim from the `-v` node list of this run)

### Scenario: its dossier is reachable from that list
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_its_dossier_is_reachable_from_that_list` executed under `dev/.venv/bin/python`
- Expected: its dossier is reachable from that list
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_its_dossier_is_reachable_from_that_list PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the rule in the row is the rule that actually disposed the finding
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_rule_in_the_row_is_the_rule_that_actually_disposed_the_finding` executed under `dev/.venv/bin/python`
- Expected: Not a hand-written row: `state.attach_auto_disposal` runs
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_the_rule_in_the_row_is_the_rule_that_actually_disposed_the_finding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an auto disposed item is not counted as routed to a human
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_an_auto_disposed_item_is_not_counted_as_routed_to_a_human` executed under `dev/.venv/bin/python`
- Expected: an auto disposed item is not counted as routed to a human
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestAutoDisposal::test_an_auto_disposed_item_is_not_counted_as_routed_to_a_human PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the seventy and hundred per cent conclusions are textually different
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_seventy_and_hundred_per_cent_conclusions_are_textually_different` executed under `dev/.venv/bin/python`
- Expected: the seventy and hundred per cent conclusions are textually different
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_seventy_and_hundred_per_cent_conclusions_are_textually_different PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bounded conclusion names what it did not reach
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_bounded_conclusion_names_what_it_did_not_reach` executed under `dev/.venv/bin/python`
- Expected: the bounded conclusion names what it did not reach
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_bounded_conclusion_names_what_it_did_not_reach PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the full population conclusion uses a universal quantifier
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_full_population_conclusion_uses_a_universal_quantifier` executed under `dev/.venv/bin/python`
- Expected: Pass 8: the quantifier is now a NUMBER as well as a word.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_full_population_conclusion_uses_a_universal_quantifier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two conclusions carry different types in the dom
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_two_conclusions_carry_different_types_in_the_dom` executed under `dev/.venv/bin/python`
- Expected: the two conclusions carry different types in the dom
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_two_conclusions_carry_different_types_in_the_dom PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at zero coverage the findings region is absent not empty
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_the_findings_region_is_absent_not_empty` executed under `dev/.venv/bin/python`
- Expected: at zero coverage the findings region is absent not empty
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_the_findings_region_is_absent_not_empty PASSED` (verbatim from the `-v` node list of this run)

### Scenario: at zero coverage no finding count is rendered at all
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_no_finding_count_is_rendered_at_all` executed under `dev/.venv/bin/python`
- Expected: at zero coverage no finding count is rendered at all
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_at_zero_coverage_no_finding_count_is_rendered_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the partial banner is absent at full coverage
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_partial_banner_is_absent_at_full_coverage` executed under `dev/.venv/bin/python`
- Expected: the partial banner is absent at full coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestCoverageChangesTheGrammar::test_the_partial_banner_is_absent_at_full_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an explicit zero pending state is visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_an_explicit_zero_pending_state_is_visible` executed under `dev/.venv/bin/python`
- Expected: an explicit zero pending state is visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_an_explicit_zero_pending_state_is_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it carries the runs coverage statement
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_carries_the_runs_coverage_statement` executed under `dev/.venv/bin/python`
- Expected: it carries the runs coverage statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_carries_the_runs_coverage_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is not a blank region and not a spinner
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_is_not_a_blank_region_and_not_a_spinner` executed under `dev/.venv/bin/python`
- Expected: it is not a blank region and not a spinner
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestZeroPendingIsAStatedResult::test_it_is_not_a_blank_region_and_not_a_spinner PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F33 07 the recall bias label sits adjacent at equal weight
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_07_the_recall_bias_label_sits_adjacent_at_equal_weight` executed under `dev/.venv/bin/python`
- Expected: The label is the schema's own string, not a paraphrase on a screen.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_07_the_recall_bias_label_sits_adjacent_at_equal_weight PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F33 08 the label is adjacent to the recall figure not at the card foot
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_08_the_label_is_adjacent_to_the_recall_figure_not_at_the_card_foot` executed under `dev/.venv/bin/python`
- Expected: "adjacent" is the word the criterion uses, and it is written that
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_AC_F33_08_the_label_is_adjacent_to_the_recall_figure_not_at_the_card_foot PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is not inside a collapsed region
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_it_is_not_inside_a_collapsed_region` executed under `dev/.venv/bin/python`
- Expected: it is not inside a collapsed region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestMeasurementBiasIsSchemaNotFootnote::test_it_is_not_inside_a_collapsed_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no bulk action control anywhere on the queue
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_anywhere_on_the_queue` executed under `dev/.venv/bin/python`
- Expected: there is no bulk action control anywhere on the queue
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_bulk_action_control_anywhere_on_the_queue PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no row offers an approve control
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_no_row_offers_an_approve_control` executed under `dev/.venv/bin/python`
- Expected: no row offers an approve control
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_no_row_offers_an_approve_control PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no green success state rendered
- Status: EXECUTED
- Input: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_green_success_state_rendered` executed under `dev/.venv/bin/python`
- Expected: there is no green success state rendered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_exceptions.py::TestNoRefusedAffordances::test_there_is_no_green_success_state_rendered PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_governance_screens.py`

### Scenario: AC F38 01 every required fact is visible on the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_01_every_required_fact_is_visible_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: AC F38 01 every required fact is visible on the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_01_every_required_fact_is_visible_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 12 a failed tie out is shown with its date
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_a_failed_tie_out_is_shown_with_its_date` executed under `dev/.venv/bin/python`
- Expected: AC F38 12 a failed tie out is shown with its date
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_a_failed_tie_out_is_shown_with_its_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 12 an action capable run over it is refused naming the tie out
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_an_action_capable_run_over_it_is_refused_naming_the_tie_out` executed under `dev/.venv/bin/python`
- Expected: AC F38 12 an action capable run over it is refused naming the tie out
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_12_an_action_capable_run_over_it_is_refused_naming_the_tie_out PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 09 an action capable run over an uncertified dataset is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_09_an_action_capable_run_over_an_uncertified_dataset_is_refused` executed under `dev/.venv/bin/python`
- Expected: AC F38 09 an action capable run over an uncertified dataset is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_09_an_action_capable_run_over_an_uncertified_dataset_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the same dataset is permitted in the exploration tier
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_the_same_dataset_is_permitted_in_the_exploration_tier` executed under `dev/.venv/bin/python`
- Expected: the same dataset is permitted in the exploration tier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_the_same_dataset_is_permitted_in_the_exploration_tier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 13 a tenant with no certified dataset says so and why
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_13_a_tenant_with_no_certified_dataset_says_so_and_why` executed under `dev/.venv/bin/python`
- Expected: AC F38 13 a tenant with no certified dataset says so and why
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_13_a_tenant_with_no_certified_dataset_says_so_and_why PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 16 every columns classification is visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_every_columns_classification_is_visible` executed under `dev/.venv/bin/python`
- Expected: AC F38 16 every columns classification is visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_every_columns_classification_is_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F38 16 a model bound run over an unclassified column is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_a_model_bound_run_over_an_unclassified_column_is_refused` executed under `dev/.venv/bin/python`
- Expected: AC F38 16 a model bound run over an unclassified column is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_AC_F38_16_a_model_bound_run_over_an_unclassified_column_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unclassified column refuses even in the exploration tier
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_an_unclassified_column_refuses_even_in_the_exploration_tier` executed under `dev/.venv/bin/python`
- Expected: The exploration tier relaxes certification, not exposure. An
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheCatalogueScreen::test_an_unclassified_column_refuses_even_in_the_exploration_tier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F36 19 an agent with no overrides shows an explicit zero
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F36_19_an_agent_with_no_overrides_shows_an_explicit_zero` executed under `dev/.venv/bin/python`
- Expected: With its DENOMINATOR. A bare zero cannot be told from an agent that
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F36_19_an_agent_with_no_overrides_shows_an_explicit_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 07 median dwell time is visible per agent and per user
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_07_median_dwell_time_is_visible_per_agent_and_per_user` executed under `dev/.venv/bin/python`
- Expected: AC F41 07 median dwell time is visible per agent and per user
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_07_median_dwell_time_is_visible_per_agent_and_per_user PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F12 10 probe results are aggregate only
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_probe_results_are_aggregate_only` executed under `dev/.venv/bin/python`
- Expected: AC F12 10 probe results are aggregate only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_probe_results_are_aggregate_only PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F12 10 no named person appears anywhere in the probe panel
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_no_named_person_appears_anywhere_in_the_probe_panel` executed under `dev/.venv/bin/python`
- Expected: AC F12 10 no named person appears anywhere in the probe panel
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F12_10_no_named_person_appears_anywhere_in_the_probe_panel PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the probe aggregation keys are a closed list not a parameter
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_aggregation_keys_are_a_closed_list_not_a_parameter` executed under `dev/.venv/bin/python`
- Expected: A parameterised group-by is a per-named-person report waiting for
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_aggregation_keys_are_a_closed_list_not_a_parameter PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the probe zeroes are labelled as no probe not as no error
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error` executed under `dev/.venv/bin/python`
- Expected: the probe zeroes are labelled as no probe not as no error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F32 10 the forward disposition hit rate is visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F32_10_the_forward_disposition_hit_rate_is_visible` executed under `dev/.venv/bin/python`
- Expected: AC F32 10 the forward disposition hit rate is visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F32_10_the_forward_disposition_hit_rate_is_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the hit rate is a real figure from the verification job
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_hit_rate_is_a_real_figure_from_the_verification_job` executed under `dev/.venv/bin/python`
- Expected: the hit rate is a real figure from the verification job
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_the_hit_rate_is_a_real_figure_from_the_verification_job PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F9 08 open escalations name the account aggregate period and leg
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_08_open_escalations_name_the_account_aggregate_period_and_leg` executed under `dev/.venv/bin/python`
- Expected: Both legs, from a REAL F9 run.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_08_open_escalations_name_the_account_aggregate_period_and_leg PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F9 04 each escalation carries the control state change on the account
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_04_each_escalation_carries_the_control_state_change_on_the_account` executed under `dev/.venv/bin/python`
- Expected: "an R6 control-state change readable on the account, rather than
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_04_each_escalation_carries_the_control_state_change_on_the_account PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F9 05 an account with too little history says so by name
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_05_an_account_with_too_little_history_says_so_by_name` executed under `dev/.venv/bin/python`
- Expected: NOT absent from the escalation list, which reads as
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_05_an_account_with_too_little_history_says_so_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F9 09 periods with no recorded explanation are named
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_09_periods_with_no_recorded_explanation_are_named` executed under `dev/.venv/bin/python`
- Expected: AC F9 09 periods with no recorded explanation are named
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F9_09_periods_with_no_recorded_explanation_are_named PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 19 the routed count against the cap is visible per reviewer
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_the_routed_count_against_the_cap_is_visible_per_reviewer` executed under `dev/.venv/bin/python`
- Expected: AC F41 19 the routed count against the cap is visible per reviewer
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_the_routed_count_against_the_cap_is_visible_per_reviewer PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 19 a raised cap names who raised it
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_a_raised_cap_names_who_raised_it` executed under `dev/.venv/bin/python`
- Expected: AC F41 19 a raised cap names who raised it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_AC_F41_19_a_raised_cap_names_who_raised_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a broker that cannot be reached renders no figure at all
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_a_broker_that_cannot_be_reached_renders_no_figure_at_all` executed under `dev/.venv/bin/python`
- Expected: Convention C2 on a control surface: a zero here would be a claim
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheMonitorsScreen::test_a_broker_that_cannot_be_reached_renders_no_figure_at_all PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F5 07 every agent is listed with version and entitlements
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements` executed under `dev/.venv/bin/python`
- Expected: AC F5 07 every agent is listed with version and entitlements
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F5 07 a lineage view is reachable for each listed version
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version` executed under `dev/.venv/bin/python`
- Expected: AC F5 07 a lineage view is reachable for each listed version
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F5 04 a version that touched nothing states zero
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_04_a_version_that_touched_nothing_states_zero` executed under `dev/.venv/bin/python`
- Expected: AC F5 04 a version that touched nothing states zero
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_04_a_version_that_touched_nothing_states_zero PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F5 05 every lineage result states its own completeness
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_05_every_lineage_result_states_its_own_completeness` executed under `dev/.venv/bin/python`
- Expected: AC F5 05 every lineage result states its own completeness
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_AC_F5_05_every_lineage_result_states_its_own_completeness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no agent principal holds the approval capability
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_no_agent_principal_holds_the_approval_capability` executed under `dev/.venv/bin/python`
- Expected: The inventory is where this becomes readable rather than inferable:
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheInventoryScreen::test_no_agent_principal_holds_the_approval_capability PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F1 09 the dossier list for the period is visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_the_dossier_list_for_the_period_is_visible` executed under `dev/.venv/bin/python`
- Expected: AC F1 09 the dossier list for the period is visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_the_dossier_list_for_the_period_is_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F1 09 an individual dossiers rendered view is reachable from it
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_individual_dossiers_rendered_view_is_reachable_from_it` executed under `dev/.venv/bin/python`
- Expected: AC F1 09 an individual dossiers rendered view is reachable from it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_individual_dossiers_rendered_view_is_reachable_from_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F1 09 an export control for the period is visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_export_control_for_the_period_is_visible` executed under `dev/.venv/bin/python`
- Expected: AC F1 09 an export control for the period is visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F1_09_an_export_control_for_the_period_is_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F2 07 the full version tuple is visible on this screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F2_07_the_full_version_tuple_is_visible_on_this_screen` executed under `dev/.venv/bin/python`
- Expected: AC F2 07 the full version tuple is visible on this screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_F2_07_the_full_version_tuple_is_visible_on_this_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the version tuple states absences rather than omitting them
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_version_tuple_states_absences_rather_than_omitting_them` executed under `dev/.venv/bin/python`
- Expected: `AC-F2-01` wants six independently identified versions. This build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_version_tuple_states_absences_rather_than_omitting_them PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC REFUSAL 04 refusal events are retrievable from this screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_REFUSAL_04_refusal_events_are_retrievable_from_this_screen` executed under `dev/.venv/bin/python`
- Expected: AC REFUSAL 04 refusal events are retrievable from this screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_AC_REFUSAL_04_refusal_events_are_retrievable_from_this_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export states the two guarantees it does not carry
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_export_states_the_two_guarantees_it_does_not_carry` executed under `dev/.venv/bin/python`
- Expected: Register entries 3 and 4. They are on the artefact an auditor would
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheAuditScreen::test_the_export_states_the_two_guarantees_it_does_not_carry PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC REFUSAL 01 and 13 all seven refusals are visible by name
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_01_and_13_all_seven_refusals_are_visible_by_name` executed under `dev/.venv/bin/python`
- Expected: AC REFUSAL 01 and 13 all seven refusals are visible by name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_01_and_13_all_seven_refusals_are_visible_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each refusal states the reason it is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_each_refusal_states_the_reason_it_is_refused` executed under `dev/.venv/bin/python`
- Expected: each refusal states the reason it is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_each_refusal_states_the_reason_it_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC REFUSAL 02 the by design wording is on every entry
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_by_design_wording_is_on_every_entry` executed under `dev/.venv/bin/python`
- Expected: AC REFUSAL 02 the by design wording is on every entry
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_by_design_wording_is_on_every_entry PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC REFUSAL 02 the deferred wording shares no phrase with it
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_deferred_wording_shares_no_phrase_with_it` executed under `dev/.venv/bin/python`
- Expected: AC REFUSAL 02 the deferred wording shares no phrase with it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_AC_REFUSAL_02_the_deferred_wording_shares_no_phrase_with_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the list is served by the broker and not held in the interface
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_list_is_served_by_the_broker_and_not_held_in_the_interface` executed under `dev/.venv/bin/python`
- Expected: A refusal list duplicated into a screen survives its own removal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_list_is_served_by_the_broker_and_not_held_in_the_interface PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen says why both lists are on it
- Status: EXECUTED
- Input: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_screen_says_why_both_lists_are_on_it` executed under `dev/.venv/bin/python`
- Expected: the screen says why both lists are on it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_governance_screens.py::TestTheRefusalsScreen::test_the_screen_says_why_both_lists_are_on_it PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_html.py`

### Scenario: text escapes angle brackets and ampersands
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_text_escapes_angle_brackets_and_ampersands` executed under `dev/.venv/bin/python`
- Expected: text escapes angle brackets and ampersands
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_text_escapes_angle_brackets_and_ampersands PASSED` (verbatim from the `-v` node list of this run)

### Scenario: attribute values escape quotes and brackets
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_attribute_values_escape_quotes_and_brackets` executed under `dev/.venv/bin/python`
- Expected: attribute values escape quotes and brackets
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_attribute_values_escape_quotes_and_brackets PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a data derived string cannot close its own tag
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_a_data_derived_string_cannot_close_its_own_tag` executed under `dev/.venv/bin/python`
- Expected: a data derived string cannot close its own tag
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_a_data_derived_string_cannot_close_its_own_tag PASSED` (verbatim from the `-v` node list of this run)

### Scenario: none children are dropped not rendered as the word none
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_none_children_are_dropped_not_rendered_as_the_word_none` executed under `dev/.venv/bin/python`
- Expected: none children are dropped not rendered as the word none
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_none_children_are_dropped_not_rendered_as_the_word_none PASSED` (verbatim from the `-v` node list of this run)

### Scenario: text of none is empty not the word none
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_text_of_none_is_empty_not_the_word_none` executed under `dev/.venv/bin/python`
- Expected: text of none is empty not the word none
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_text_of_none_is_empty_not_the_word_none PASSED` (verbatim from the `-v` node list of this run)

### Scenario: numbers are coerced
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestEscaping::test_numbers_are_coerced` executed under `dev/.venv/bin/python`
- Expected: numbers are coerced
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestEscaping::test_numbers_are_coerced PASSED` (verbatim from the `-v` node list of this run)

### Scenario: underscores become hyphens and class underscore becomes class
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_underscores_become_hyphens_and_class_underscore_becomes_class` executed under `dev/.venv/bin/python`
- Expected: underscores become hyphens and class underscore becomes class
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestAttributes::test_underscores_become_hyphens_and_class_underscore_becomes_class PASSED` (verbatim from the `-v` node list of this run)

### Scenario: true renders bare and false and none are omitted
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_true_renders_bare_and_false_and_none_are_omitted` executed under `dev/.venv/bin/python`
- Expected: true renders bare and false and none are omitted
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestAttributes::test_true_renders_bare_and_false_and_none_are_omitted PASSED` (verbatim from the `-v` node list of this run)

### Scenario: zero is rendered not treated as absent
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestAttributes::test_zero_is_rendered_not_treated_as_absent` executed under `dev/.venv/bin/python`
- Expected: zero is rendered not treated as absent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestAttributes::test_zero_is_rendered_not_treated_as_absent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: void element renders without a closing tag
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_void_element_renders_without_a_closing_tag` executed under `dev/.venv/bin/python`
- Expected: void element renders without a closing tag
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_void_element_renders_without_a_closing_tag PASSED` (verbatim from the `-v` node list of this run)

### Scenario: void element refuses children
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_void_element_refuses_children` executed under `dev/.venv/bin/python`
- Expected: void element refuses children
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_void_element_refuses_children PASSED` (verbatim from the `-v` node list of this run)

### Scenario: bad tag name is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_bad_tag_name_is_refused` executed under `dev/.venv/bin/python`
- Expected: bad tag name is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_bad_tag_name_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: walk yields every descendant in document order
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_walk_yields_every_descendant_in_document_order` executed under `dev/.venv/bin/python`
- Expected: walk yields every descendant in document order
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_walk_yields_every_descendant_in_document_order PASSED` (verbatim from the `-v` node list of this run)

### Scenario: fragment has no wrapper but is still walkable
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_fragment_has_no_wrapper_but_is_still_walkable` executed under `dev/.venv/bin/python`
- Expected: fragment has no wrapper but is still walkable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_fragment_has_no_wrapper_but_is_still_walkable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: find by test id traverses the tree
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_find_by_test_id_traverses_the_tree` executed under `dev/.venv/bin/python`
- Expected: find by test id traverses the tree
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_find_by_test_id_traverses_the_tree PASSED` (verbatim from the `-v` node list of this run)

### Scenario: document is self contained and carries the theme
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestStructure::test_document_is_self_contained_and_carries_the_theme` executed under `dev/.venv/bin/python`
- Expected: document is self contained and carries the theme
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestStructure::test_document_is_self_contained_and_carries_the_theme PASSED` (verbatim from the `-v` node list of this run)

### Scenario: raw passes markup through
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_passes_markup_through` executed under `dev/.venv/bin/python`
- Expected: raw passes markup through
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_passes_markup_through PASSED` (verbatim from the `-v` node list of this run)

### Scenario: raw refuses a non string
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_refuses_a_non_string` executed under `dev/.venv/bin/python`
- Expected: raw refuses a non string
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_raw_refuses_a_non_string PASSED` (verbatim from the `-v` node list of this run)

### Scenario: only chrome constructs a raw in the ui package
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_only_chrome_constructs_a_raw_in_the_ui_package` executed under `dev/.venv/bin/python`
- Expected: The set of callers is short enough to read, and this keeps it so.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestRawIsTheOnlyDoor::test_only_chrome_constructs_a_raw_in_the_ui_package PASSED` (verbatim from the `-v` node list of this run)

### Scenario: mono and amount carry the tabular numeral classes
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestHelpers::test_mono_and_amount_carry_the_tabular_numeral_classes` executed under `dev/.venv/bin/python`
- Expected: mono and amount carry the tabular numeral classes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestHelpers::test_mono_and_amount_carry_the_tabular_numeral_classes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: kv always renders both halves
- Status: EXECUTED
- Input: `backend/tests/test_ui_html.py::TestHelpers::test_kv_always_renders_both_halves` executed under `dev/.venv/bin/python`
- Expected: kv always renders both halves
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_html.py::TestHelpers::test_kv_always_renders_both_halves PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_proposal.py`

### Scenario: the proposal is reachable from the entry point by following links
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_the_proposal_is_reachable_from_the_entry_point_by_following_links` executed under `dev/.venv/bin/python`
- Expected: the proposal is reachable from the entry point by following links
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_the_proposal_is_reachable_from_the_entry_point_by_following_links PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is linked from the review screen of the item that produced it
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_it_is_linked_from_the_review_screen_of_the_item_that_produced_it` executed under `dev/.venv/bin/python`
- Expected: it is linked from the review screen of the item that produced it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_it_is_linked_from_the_review_screen_of_the_item_that_produced_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: only the item with a posting capable outcome links to a proposal
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_only_the_item_with_a_posting_capable_outcome_links_to_a_proposal` executed under `dev/.venv/bin/python`
- Expected: only the item with a posting capable outcome links to a proposal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_only_the_item_with_a_posting_capable_outcome_links_to_a_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[no-posting-notice]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[no-posting-notice]` executed under `dev/.venv/bin/python`, parameter case `no-posting-notice`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[no-posting-notice] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[risk-band]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]` executed under `dev/.venv/bin/python`, parameter case `risk-band`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[journal-lines]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-lines]` executed under `dev/.venv/bin/python`, parameter case `journal-lines`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[journal-line]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-line]` executed under `dev/.venv/bin/python`, parameter case `journal-line`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[journal-line] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[two-key-model]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[two-key-model]` executed under `dev/.venv/bin/python`, parameter case `two-key-model`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[two-key-model] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[authorship-closure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]` executed under `dev/.venv/bin/python`, parameter case `authorship-closure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[approve-lines]
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[approve-lines]` executed under `dev/.venv/bin/python`, parameter case `approve-lines`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[approve-lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen states in plain words that it does not post
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_screen_states_in_plain_words_that_it_does_not_post` executed under `dev/.venv/bin/python`
- Expected: the screen states in plain words that it does not post
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_screen_states_in_plain_words_that_it_does_not_post PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the approve label names the lines and the word export
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_approve_label_names_the_lines_and_the_word_export` executed under `dev/.venv/bin/python`
- Expected: the approve label names the lines and the word export
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_approve_label_names_the_lines_and_the_word_export PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the word post never appears as a control label
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_word_post_never_appears_as_a_control_label` executed under `dev/.venv/bin/python`
- Expected: the word post never appears as a control label
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_the_word_post_never_appears_as_a_control_label PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no posting library is a dependency of this build
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_no_posting_library_is_a_dependency_of_this_build` executed under `dev/.venv/bin/python`
- Expected: The screen's claim is only as good as the build behind it.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheActionPathTerminatesInAProposal::test_no_posting_library_is_a_dependency_of_this_build PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the lines precede the approve control in reading order
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_precede_the_approve_control_in_reading_order` executed under `dev/.venv/bin/python`
- Expected: the lines precede the approve control in reading order
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_precede_the_approve_control_in_reading_order PASSED` (verbatim from the `-v` node list of this run)

### Scenario: both lines are rendered with their full coding
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_both_lines_are_rendered_with_their_full_coding` executed under `dev/.venv/bin/python`
- Expected: both lines are rendered with their full coding
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_both_lines_are_rendered_with_their_full_coding PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the lines are not inside a collapsed region
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_are_not_inside_a_collapsed_region` executed under `dev/.venv/bin/python`
- Expected: the lines are not inside a collapsed region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_lines_are_not_inside_a_collapsed_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two sides balance on the face of the rendering
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_two_sides_balance_on_the_face_of_the_rendering` executed under `dev/.venv/bin/python`
- Expected: the two sides balance on the face of the rendering
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheLinesAreVisibleBeforeTheControl::test_the_two_sides_balance_on_the_face_of_the_rendering PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the two key model names three distinct roles
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_two_key_model_names_three_distinct_roles` executed under `dev/.venv/bin/python`
- Expected: the two key model names three distinct roles
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_two_key_model_names_three_distinct_roles PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the closure is stated as author approver invoker
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_closure_is_stated_as_author_approver_invoker` executed under `dev/.venv/bin/python`
- Expected: the closure is stated as author approver invoker
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_closure_is_stated_as_author_approver_invoker PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the author and the invoker are named separately
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_author_and_the_invoker_are_named_separately` executed under `dev/.venv/bin/python`
- Expected: the author and the invoker are named separately
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_author_and_the_invoker_are_named_separately PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the approver slot is empty until someone approves
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_approver_slot_is_empty_until_someone_approves` executed under `dev/.venv/bin/python`
- Expected: the approver slot is empty until someone approves
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_approver_slot_is_empty_until_someone_approves PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the decision id that authorised the view is on the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_decision_id_that_authorised_the_view_is_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: the decision id that authorised the view is on the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestAuthorshipClosureIsVisible::test_the_decision_id_that_authorised_the_view_is_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the approve control is absent not disabled on a superseded run
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_approve_control_is_absent_not_disabled_on_a_superseded_run` executed under `dev/.venv/bin/python`
- Expected: the approve control is absent not disabled on a superseded run
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_approve_control_is_absent_not_disabled_on_a_superseded_run PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the block names the superseding run and its completion time
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_names_the_superseding_run_and_its_completion_time` executed under `dev/.venv/bin/python`
- Expected: the block names the superseding run and its completion time
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_names_the_superseding_run_and_its_completion_time PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the only forward action is to open the superseding run
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_only_forward_action_is_to_open_the_superseding_run` executed under `dev/.venv/bin/python`
- Expected: the only forward action is to open the superseding run
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_only_forward_action_is_to_open_the_superseding_run PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the block is not dismissible
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_is_not_dismissible` executed under `dev/.venv/bin/python`
- Expected: the block is not dismissible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestSupersession::test_the_block_is_not_dismissible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 01 there is no control that approves more than this proposal
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_AC_F41_01_there_is_no_control_that_approves_more_than_this_proposal` executed under `dev/.venv/bin/python`
- Expected: AC F41 01 there is no control that approves more than this proposal
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_AC_F41_01_there_is_no_control_that_approves_more_than_this_proposal PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no checkbox and no multi select on the screen
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_there_is_no_checkbox_and_no_multi_select_on_the_screen` executed under `dev/.venv/bin/python`
- Expected: there is no checkbox and no multi select on the screen
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_there_is_no_checkbox_and_no_multi_select_on_the_screen PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the form posts to this proposals own endpoint
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_the_form_posts_to_this_proposals_own_endpoint` executed under `dev/.venv/bin/python`
- Expected: the form posts to this proposals own endpoint
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestApprovalIsScopedToOneArtefact::test_the_form_posts_to_this_proposals_own_endpoint PASSED` (verbatim from the `-v` node list of this run)

### Scenario: approving is not reachable by a get
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestTheApprovalEndpointIsPostOnly::test_approving_is_not_reachable_by_a_get` executed under `dev/.venv/bin/python`
- Expected: approving is not reachable by a get
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestTheApprovalEndpointIsPostOnly::test_approving_is_not_reachable_by_a_get PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the stamp carries the bundle the decision and the cuec date
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_stamp_carries_the_bundle_the_decision_and_the_cuec_date` executed under `dev/.venv/bin/python`
- Expected: the stamp carries the bundle the decision and the cuec date
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_stamp_carries_the_bundle_the_decision_and_the_cuec_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the accounting date and journal source are on the face of it
- Status: EXECUTED
- Input: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_accounting_date_and_journal_source_are_on_the_face_of_it` executed under `dev/.venv/bin/python`
- Expected: the accounting date and journal source are on the face of it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_proposal.py::TestNoStaleBasisIsHidden::test_the_accounting_date_and_journal_source_are_on_the_face_of_it PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_readiness.py`

### Scenario: readiness is reachable from the entry point by following links
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_readiness_is_reachable_from_the_entry_point_by_following_links` executed under `dev/.venv/bin/python`
- Expected: readiness is reachable from the entry point by following links
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_readiness_is_reachable_from_the_entry_point_by_following_links PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it has a permanent place in the navigation
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_it_has_a_permanent_place_in_the_navigation` executed under `dev/.venv/bin/python`
- Expected: it has a permanent place in the navigation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_it_has_a_permanent_place_in_the_navigation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[readiness-statement]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-statement]` executed under `dev/.venv/bin/python`, parameter case `readiness-statement`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-statement] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[readiness-conditions]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-conditions]` executed under `dev/.venv/bin/python`, parameter case `readiness-conditions`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-conditions] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[readiness-condition]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-condition]` executed under `dev/.venv/bin/python`, parameter case `readiness-condition`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-condition] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[readiness-basis]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-basis]` executed under `dev/.venv/bin/python`, parameter case `readiness-basis`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[readiness-basis] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[precision-figure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[precision-figure]` executed under `dev/.venv/bin/python`, parameter case `precision-figure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[precision-figure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[label-source-statement]
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[label-source-statement]` executed under `dev/.venv/bin/python`, parameter case `label-source-statement`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[label-source-statement] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: exactly five conditions render
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_exactly_five_conditions_render` executed under `dev/.venv/bin/python`
- Expected: exactly five conditions render
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_exactly_five_conditions_render PASSED` (verbatim from the `-v` node list of this run)

### Scenario: they are P1 through P5 in order
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_they_are_P1_through_P5_in_order` executed under `dev/.venv/bin/python`
- Expected: they are P1 through P5 in order
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_they_are_P1_through_P5_in_order PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each carries its own state and its own sentence
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_each_carries_its_own_state_and_its_own_sentence` executed under `dev/.venv/bin/python`
- Expected: each carries its own state and its own sentence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_each_carries_its_own_state_and_its_own_sentence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: P1 and P5 report not yet evaluable and NAME the deferral
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_P1_and_P5_report_not_yet_evaluable_and_NAME_the_deferral` executed under `dev/.venv/bin/python`
- Expected: P1 and P5 report not yet evaluable and NAME the deferral
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_P1_and_P5_report_not_yet_evaluable_and_NAME_the_deferral PASSED` (verbatim from the `-v` node list of this run)

### Scenario: not yet evaluable is visually distinct from not met
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_not_yet_evaluable_is_visually_distinct_from_not_met` executed under `dev/.venv/bin/python`
- Expected: "We have not looked long enough" and "we looked and it failed" are
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_not_yet_evaluable_is_visually_distinct_from_not_met PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen carries all three states at once
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_the_screen_carries_all_three_states_at_once` executed under `dev/.venv/bin/python`
- Expected: At a two-period window every condition reports `not_yet_evaluable`
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_the_screen_carries_all_three_states_at_once PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a short evidence window reports not yet evaluable rather than not met
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_a_short_evidence_window_reports_not_yet_evaluable_rather_than_not_met` executed under `dev/.venv/bin/python`
- Expected: a short evidence window reports not yet evaluable rather than not met
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestAllFiveConditionsStatedIndividually::test_a_short_evidence_window_reports_not_yet_evaluable_rather_than_not_met PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the report does not assert readiness
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_report_does_not_assert_readiness` executed under `dev/.venv/bin/python`
- Expected: the report does not assert readiness
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_report_does_not_assert_readiness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the basis is stated on the face of the report
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_basis_is_stated_on_the_face_of_the_report` executed under `dev/.venv/bin/python`
- Expected: the basis is stated on the face of the report
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_basis_is_stated_on_the_face_of_the_report PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the conditions precede the precision figure in reading order
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_conditions_precede_the_precision_figure_in_reading_order` executed under `dev/.venv/bin/python`
- Expected: the conditions precede the precision figure in reading order
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_conditions_precede_the_precision_figure_in_reading_order PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen explains why the precision figure is not the gate
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_screen_explains_why_the_precision_figure_is_not_the_gate` executed under `dev/.venv/bin/python`
- Expected: the screen explains why the precision figure is not the gate
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_the_screen_explains_why_the_precision_figure_is_not_the_gate PASSED` (verbatim from the `-v` node list of this run)

### Scenario: readiness is computed from the conditions and not from the figure
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_readiness_is_computed_from_the_conditions_and_not_from_the_figure` executed under `dev/.venv/bin/python`
- Expected: The substitution the inverted gate invites, refused at the model.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestReadinessIsNeverAssertedOnPrecisionAlone::test_readiness_is_computed_from_the_conditions_and_not_from_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the label source is rendered adjacent to the figure
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_label_source_is_rendered_adjacent_to_the_figure` executed under `dev/.venv/bin/python`
- Expected: the label source is rendered adjacent to the figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_label_source_is_rendered_adjacent_to_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the statement says the figure measures agreement not correctness
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_says_the_figure_measures_agreement_not_correctness` executed under `dev/.venv/bin/python`
- Expected: the statement says the figure measures agreement not correctness
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_says_the_figure_measures_agreement_not_correctness PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an acceptance derived figure is marked not promotion usable
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_is_marked_not_promotion_usable` executed under `dev/.venv/bin/python`
- Expected: an acceptance derived figure is marked not promotion usable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_is_marked_not_promotion_usable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the statement is rendered at warning weight not as a footnote
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_is_rendered_at_warning_weight_not_as_a_footnote` executed under `dev/.venv/bin/python`
- Expected: the statement is rendered at warning weight not as a footnote
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_statement_is_rendered_at_warning_weight_not_as_a_footnote PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is not inside a collapsed region
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_it_is_not_inside_a_collapsed_region` executed under `dev/.venv/bin/python`
- Expected: it is not inside a collapsed region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_it_is_not_inside_a_collapsed_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the denominator is stated with the figure
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_denominator_is_stated_with_the_figure` executed under `dev/.venv/bin/python`
- Expected: the denominator is stated with the figure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_the_denominator_is_stated_with_the_figure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a figure cannot be constructed without a label source
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_a_figure_cannot_be_constructed_without_a_label_source` executed under `dev/.venv/bin/python`
- Expected: a figure cannot be constructed without a label source
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_a_figure_cannot_be_constructed_without_a_label_source PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an acceptance derived figure cannot be offered as promotion evidence
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_cannot_be_offered_as_promotion_evidence` executed under `dev/.venv/bin/python`
- Expected: an acceptance derived figure cannot be offered as promotion evidence
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestTheLabelSource::test_an_acceptance_derived_figure_cannot_be_offered_as_promotion_evidence PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a met condition is not rendered as a success
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_a_met_condition_is_not_rendered_as_a_success` executed under `dev/.venv/bin/python`
- Expected: a met condition is not rendered as a success
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_a_met_condition_is_not_rendered_as_a_success PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the screen carries no tick or success glyph
- Status: EXECUTED
- Input: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_the_screen_carries_no_tick_or_success_glyph` executed under `dev/.venv/bin/python`
- Expected: the screen carries no tick or success glyph
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_readiness.py::TestNoGreenAnywhereOnThisScreen::test_the_screen_carries_no_tick_or_success_glyph PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_review.py`

### Scenario: a review item is reachable from the entry point by following links
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_a_review_item_is_reachable_from_the_entry_point_by_following_links` executed under `dev/.venv/bin/python`
- Expected: a review item is reachable from the entry point by following links
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_a_review_item_is_reachable_from_the_entry_point_by_following_links PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the queue index links to this item
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_the_queue_index_links_to_this_item` executed under `dev/.venv/bin/python`
- Expected: the queue index links to this item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_the_queue_index_links_to_this_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the exceptions queue links to this item
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_the_exceptions_queue_links_to_this_item` executed under `dev/.venv/bin/python`
- Expected: the exceptions queue links to this item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_the_exceptions_queue_links_to_this_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[risk-band]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band]` executed under `dev/.venv/bin/python`, parameter case `risk-band`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[risk-band] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[riskiest-figure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure]` executed under `dev/.venv/bin/python`, parameter case `riskiest-figure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[riskiest-figure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[evidence-set]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set]` executed under `dev/.venv/bin/python`, parameter case `evidence-set`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[evidence-set] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[in-force-panel]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel]` executed under `dev/.venv/bin/python`, parameter case `in-force-panel`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[in-force-panel] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[authorship-closure]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure]` executed under `dev/.venv/bin/python`, parameter case `authorship-closure`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[authorship-closure] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[resolution-row]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-row]` executed under `dev/.venv/bin/python`, parameter case `resolution-row`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-row] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[resolution-button]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-button]` executed under `dev/.venv/bin/python`, parameter case `resolution-button`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[resolution-button] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[forward-disposition]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[forward-disposition]` executed under `dev/.venv/bin/python`, parameter case `forward-disposition`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[forward-disposition] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[clears-by]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[clears-by]` executed under `dev/.venv/bin/python`, parameter case `clears-by`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[clears-by] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[rejection-reasons]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reasons]` executed under `dev/.venv/bin/python`, parameter case `rejection-reasons`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reasons] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[rejection-reason]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reason]` executed under `dev/.venv/bin/python`, parameter case `rejection-reason`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[rejection-reason] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[reject-submit]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[reject-submit]` executed under `dev/.venv/bin/python`, parameter case `reject-submit`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[reject-submit] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[agent-narrative]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative]` executed under `dev/.venv/bin/python`, parameter case `agent-narrative`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[agent-narrative] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: component is present in the tree the route returned[dossier-link]
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-link]` executed under `dev/.venv/bin/python`, parameter case `dossier-link`
- Expected: component is present in the tree the route returned
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReachability::test_component_is_present_in_the_tree_the_route_returned[dossier-link] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the risk band precedes the evidence the resolution and the narrative
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_risk_band_precedes_the_evidence_the_resolution_and_the_narrative` executed under `dev/.venv/bin/python`
- Expected: the risk band precedes the evidence the resolution and the narrative
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_risk_band_precedes_the_evidence_the_resolution_and_the_narrative PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the narrative is last of the four
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_narrative_is_last_of_the_four` executed under `dev/.venv/bin/python`
- Expected: the narrative is last of the four
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_narrative_is_last_of_the_four PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the evidence precedes the resolution
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_evidence_precedes_the_resolution` executed under `dev/.venv/bin/python`
- Expected: the evidence precedes the resolution
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestReadingOrder::test_the_evidence_precedes_the_resolution PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 03 it is outside every collapsible region
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_AC_F41_03_it_is_outside_every_collapsible_region` executed under `dev/.venv/bin/python`
- Expected: AC F41 03 it is outside every collapsible region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheRiskBand::test_AC_F41_03_it_is_outside_every_collapsible_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the riskiest figure is the aggregate not this periods movement
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_the_riskiest_figure_is_the_aggregate_not_this_periods_movement` executed under `dev/.venv/bin/python`
- Expected: The `DOMAIN_KB` §6.2 residual: each period was individually under
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheRiskBand::test_the_riskiest_figure_is_the_aggregate_not_this_periods_movement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it carries the threshold it was individually under
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_carries_the_threshold_it_was_individually_under` executed under `dev/.venv/bin/python`
- Expected: it carries the threshold it was individually under
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_carries_the_threshold_it_was_individually_under PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is declared at the riskiest font size and nothing else is
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_is_declared_at_the_riskiest_font_size_and_nothing_else_is` executed under `dev/.venv/bin/python`
- Expected: The declaration side of gate 5's strengthening. The UX suite checks
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheRiskBand::test_it_is_declared_at_the_riskiest_font_size_and_nothing_else_is PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no confidence score is rendered beside it
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheRiskBand::test_no_confidence_score_is_rendered_beside_it` executed under `dev/.venv/bin/python`
- Expected: no confidence score is rendered beside it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheRiskBand::test_no_confidence_score_is_rendered_beside_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no button on this screen approves anything
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_button_on_this_screen_approves_anything` executed under `dev/.venv/bin/python`
- Expected: no button on this screen approves anything
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_button_on_this_screen_approves_anything PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no form on this screen posts to an approval endpoint
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_form_on_this_screen_posts_to_an_approval_endpoint` executed under `dev/.venv/bin/python`
- Expected: no form on this screen posts to an approval endpoint
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_no_form_on_this_screen_posts_to_an_approval_endpoint PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 13 the evidence the resolution and the reject control are all visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible` executed under `dev/.venv/bin/python`
- Expected: AC F41 13 the evidence the resolution and the reject control are all visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_13_the_evidence_the_resolution_and_the_reject_control_are_all_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 02 no control is preselected prechecked or prefilled
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_02_no_control_is_preselected_prechecked_or_prefilled` executed under `dev/.venv/bin/python`
- Expected: AC F41 02 no control is preselected prechecked or prefilled
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_AC_F41_02_no_control_is_preselected_prechecked_or_prefilled PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the item state reads not approved
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_the_item_state_reads_not_approved` executed under `dev/.venv/bin/python`
- Expected: the item state reads not approved
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoApproveControlHere::test_the_item_state_reads_not_approved PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F35 09 all six types are visible and none is preselected
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected` executed under `dev/.venv/bin/python`
- Expected: AC F35 09 all six types are visible and none is preselected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: only R3 and R4 are marked as posting capable
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_only_R3_and_R4_are_marked_as_posting_capable` executed under `dev/.venv/bin/python`
- Expected: only R3 and R4 are marked as posting capable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_only_R3_and_R4_are_marked_as_posting_capable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the posts flag is visible on those two and on no other
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posts_flag_is_visible_on_those_two_and_on_no_other` executed under `dev/.venv/bin/python`
- Expected: the posts flag is visible on those two and on no other
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posts_flag_is_visible_on_those_two_and_on_no_other PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F35 05 no safe outcome costs more interactions than a posting one
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_05_no_safe_outcome_costs_more_interactions_than_a_posting_one` executed under `dev/.venv/bin/python`
- Expected: AC F35 05 no safe outcome costs more interactions than a posting one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_AC_F35_05_no_safe_outcome_costs_more_interactions_than_a_posting_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the counts on screen are the ones the model derives
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_counts_on_screen_are_the_ones_the_model_derives` executed under `dev/.venv/bin/python`
- Expected: Read off `ResolutionType.interaction_count`, which is derived from
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_counts_on_screen_are_the_ones_the_model_derives PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a type the broker does not allow is disabled and says so rather than being absent
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent` executed under `dev/.venv/bin/python`
- Expected: a type the broker does not allow is disabled and says so rather than being absent
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the posting capable types are not first not larger and not default
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posting_capable_types_are_not_first_not_larger_and_not_default` executed under `dev/.venv/bin/python`
- Expected: the posting capable types are not first not larger and not default
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestResolutionTyping::test_the_posting_capable_types_are_not_first_not_larger_and_not_default PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F32 01 the clearing period control is required
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_AC_F32_01_the_clearing_period_control_is_required` executed under `dev/.venv/bin/python`
- Expected: AC F32 01 the clearing period control is required
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestForwardDisposition::test_AC_F32_01_the_clearing_period_control_is_required PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is never prefilled
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_never_prefilled` executed under `dev/.venv/bin/python`
- Expected: it is never prefilled
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_never_prefilled PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is framed as a promise rather than as a validation error
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_framed_as_a_promise_rather_than_as_a_validation_error` executed under `dev/.venv/bin/python`
- Expected: it is framed as a promise rather than as a validation error
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestForwardDisposition::test_it_is_framed_as_a_promise_rather_than_as_a_validation_error PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 06 the reason list is closed and has six options
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_AC_F41_06_the_reason_list_is_closed_and_has_six_options` executed under `dev/.venv/bin/python`
- Expected: AC F41 06 the reason list is closed and has six options
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestStructuredRejection::test_AC_F41_06_the_reason_list_is_closed_and_has_six_options PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no reason is preselected
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_no_reason_is_preselected` executed under `dev/.venv/bin/python`
- Expected: no reason is preselected
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestStructuredRejection::test_no_reason_is_preselected PASSED` (verbatim from the `-v` node list of this run)

### Scenario: free text sits underneath the list rather than instead of it
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_free_text_sits_underneath_the_list_rather_than_instead_of_it` executed under `dev/.venv/bin/python`
- Expected: free text sits underneath the list rather than instead of it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestStructuredRejection::test_free_text_sits_underneath_the_list_rather_than_instead_of_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the submit control states that a reason is required
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestStructuredRejection::test_the_submit_control_states_that_a_reason_is_required` executed under `dev/.venv/bin/python`
- Expected: the submit control states that a reason is required
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestStructuredRejection::test_the_submit_control_states_that_a_reason_is_required PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it is a details element with no open attribute
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_it_is_a_details_element_with_no_open_attribute` executed under `dev/.venv/bin/python`
- Expected: it is a details element with no open attribute
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheNarrative::test_it_is_a_details_element_with_no_open_attribute PASSED` (verbatim from the `-v` node list of this run)

### Scenario: UX KB 2 it is collapsed on first render without any script
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_UX_KB_2_it_is_collapsed_on_first_render_without_any_script` executed under `dev/.venv/bin/python`
- Expected: UX KB 2 it is collapsed on first render without any script
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheNarrative::test_UX_KB_2_it_is_collapsed_on_first_render_without_any_script PASSED` (verbatim from the `-v` node list of this run)

### Scenario: nothing load bearing is inside it
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheNarrative::test_nothing_load_bearing_is_inside_it` executed under `dev/.venv/bin/python`
- Expected: `AC-F41-04`: a fact reachable only by expanding something is a fact
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheNarrative::test_nothing_load_bearing_is_inside_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 05 and F36 18 threshold and bundle version are both visible
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_05_and_F36_18_threshold_and_bundle_version_are_both_visible` executed under `dev/.venv/bin/python`
- Expected: AC F41 05 and F36 18 threshold and bundle version are both visible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_05_and_F36_18_threshold_and_bundle_version_are_both_visible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the full stamp is present and none of it is behind a disclosure
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_full_stamp_is_present_and_none_of_it_is_behind_a_disclosure` executed under `dev/.venv/bin/python`
- Expected: the full stamp is present and none of it is behind a disclosure
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_full_stamp_is_present_and_none_of_it_is_behind_a_disclosure PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 20 ineligibility is shown at queue entry with its reason
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_20_ineligibility_is_shown_at_queue_entry_with_its_reason` executed under `dev/.venv/bin/python`
- Expected: AC F41 20 ineligibility is shown at queue entry with its reason
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_AC_F41_20_ineligibility_is_shown_at_queue_entry_with_its_reason PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the queue index shows the ineligibility before the item is opened
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_queue_index_shows_the_ineligibility_before_the_item_is_opened` executed under `dev/.venv/bin/python`
- Expected: the queue index shows the ineligibility before the item is opened
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_queue_index_shows_the_ineligibility_before_the_item_is_opened PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the closure names all three identities
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_closure_names_all_three_identities` executed under `dev/.venv/bin/python`
- Expected: the closure names all three identities
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestInForceAndAuthorship::test_the_closure_names_all_three_identities PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no element carries data in a title attribute
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_no_element_carries_data_in_a_title_attribute` executed under `dev/.venv/bin/python`
- Expected: no element carries data in a title attribute
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_no_element_carries_data_in_a_title_attribute PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no script no fetch and no lazy loading
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_there_is_no_script_no_fetch_and_no_lazy_loading` executed under `dev/.venv/bin/python`
- Expected: there is no script no fetch and no lazy loading
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNothingIsHoverOnlyOrLazy::test_there_is_no_script_no_fetch_and_no_lazy_loading PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an item the viewer may approve still offers no approve control
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestEligibleItemStillHasNoApproveControl::test_an_item_the_viewer_may_approve_still_offers_no_approve_control` executed under `dev/.venv/bin/python`
- Expected: an item the viewer may approve still offers no approve control
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestEligibleItemStillHasNoApproveControl::test_an_item_the_viewer_may_approve_still_offers_no_approve_control PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the abstention block is on the review screen for that item
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_the_abstention_block_is_on_the_review_screen_for_that_item` executed under `dev/.venv/bin/python`
- Expected: the abstention block is on the review screen for that item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_the_abstention_block_is_on_the_review_screen_for_that_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: it appears before the evidence and outside any collapsed region
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_it_appears_before_the_evidence_and_outside_any_collapsed_region` executed under `dev/.venv/bin/python`
- Expected: it appears before the evidence and outside any collapsed region
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestAbstainedItemReview::test_it_appears_before_the_evidence_and_outside_any_collapsed_region PASSED` (verbatim from the `-v` node list of this run)

### Scenario: AC F41 01 no control disposes of more than one item
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoBulkAction::test_AC_F41_01_no_control_disposes_of_more_than_one_item` executed under `dev/.venv/bin/python`
- Expected: AC F41 01 no control disposes of more than one item
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoBulkAction::test_AC_F41_01_no_control_disposes_of_more_than_one_item PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the index offers no multi select either
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestNoBulkAction::test_the_index_offers_no_multi_select_either` executed under `dev/.venv/bin/python`
- Expected: the index offers no multi select either
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestNoBulkAction::test_the_index_offers_no_multi_select_either PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the write endpoints are post only
- Status: EXECUTED
- Input: `backend/tests/test_ui_review.py::TestTheWritePathRecords::test_the_write_endpoints_are_post_only` executed under `dev/.venv/bin/python`
- Expected: the write endpoints are post only
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_review.py::TestTheWritePathRecords::test_the_write_endpoints_are_post_only PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_tokens.py`

### Scenario: hex parsing rejects anything that is not six digit hex
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_hex_parsing_rejects_anything_that_is_not_six_digit_hex` executed under `dev/.venv/bin/python`
- Expected: hex parsing rejects anything that is not six digit hex
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestColourMaths::test_hex_parsing_rejects_anything_that_is_not_six_digit_hex PASSED` (verbatim from the `-v` node list of this run)

### Scenario: known hues
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_known_hues` executed under `dev/.venv/bin/python`
- Expected: known hues
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestColourMaths::test_known_hues PASSED` (verbatim from the `-v` node list of this run)

### Scenario: chroma is zero for a grey
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestColourMaths::test_chroma_is_zero_for_a_grey` executed under `dev/.venv/bin/python`
- Expected: chroma is zero for a grey
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestColourMaths::test_chroma_is_zero_for_a_grey PASSED` (verbatim from the `-v` node list of this run)

### Scenario: neither shipped palette contains a green
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_neither_shipped_palette_contains_a_green` executed under `dev/.venv/bin/python`
- Expected: neither shipped palette contains a green
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_neither_shipped_palette_contains_a_green PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every token individually
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_every_token_individually` executed under `dev/.venv/bin/python`
- Expected: every token individually
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_every_token_individually PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a planted success green is caught
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_planted_success_green_is_caught` executed under `dev/.venv/bin/python`
- Expected: The check has to actually fire, or it is a comment with a test.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_planted_success_green_is_caught PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a muted sage green is also caught
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_muted_sage_green_is_also_caught` executed under `dev/.venv/bin/python`
- Expected: a muted sage green is also caught
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_muted_sage_green_is_also_caught PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a teal leaning green is caught
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_teal_leaning_green_is_caught` executed under `dev/.venv/bin/python`
- Expected: a teal leaning green is caught
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_a_teal_leaning_green_is_caught PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the paper neutrals are exempt by chroma not by name
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_the_paper_neutrals_are_exempt_by_chroma_not_by_name` executed under `dev/.venv/bin/python`
- Expected: the paper neutrals are exempt by chroma not by name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_the_paper_neutrals_are_exempt_by_chroma_not_by_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: blue and the risk ramp are not caught
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestNoGreen::test_blue_and_the_risk_ramp_are_not_caught` executed under `dev/.venv/bin/python`
- Expected: blue and the risk ramp are not caught
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestNoGreen::test_blue_and_the_risk_ramp_are_not_caught PASSED` (verbatim from the `-v` node list of this run)

### Scenario: light ramp darkens monotonically with rank
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_light_ramp_darkens_monotonically_with_rank` executed under `dev/.venv/bin/python`
- Expected: light ramp darkens monotonically with rank
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_light_ramp_darkens_monotonically_with_rank PASSED` (verbatim from the `-v` node list of this run)

### Scenario: dark ramp BRIGHTENS monotonically with rank
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_dark_ramp_BRIGHTENS_monotonically_with_rank` executed under `dev/.venv/bin/python`
- Expected: Dark is not a hue rotation of light. A desaturated dark red on a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_dark_ramp_BRIGHTENS_monotonically_with_rank PASSED` (verbatim from the `-v` node list of this run)

### Scenario: each step is perceptibly separated from its neighbour
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_each_step_is_perceptibly_separated_from_its_neighbour` executed under `dev/.venv/bin/python`
- Expected: each step is perceptibly separated from its neighbour
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_each_step_is_perceptibly_separated_from_its_neighbour PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there are exactly three steps
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_there_are_exactly_three_steps` executed under `dev/.venv/bin/python`
- Expected: `UX_KB` §8.1: do not add a fourth or a numeric score. A five-step
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestRiskRampIsOrdinal::test_there_are_exactly_three_steps PASSED` (verbatim from the `-v` node list of this run)

### Scenario: black on white is 21
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_black_on_white_is_21` executed under `dev/.venv/bin/python`
- Expected: black on white is 21
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestContrast::test_black_on_white_is_21 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ratio is symmetric
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_ratio_is_symmetric` executed under `dev/.venv/bin/python`
- Expected: ratio is symmetric
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestContrast::test_ratio_is_symmetric PASSED` (verbatim from the `-v` node list of this run)

### Scenario: body ink on base meets aa in both themes
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_body_ink_on_base_meets_aa_in_both_themes` executed under `dev/.venv/bin/python`
- Expected: body ink on base meets aa in both themes
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestContrast::test_body_ink_on_base_meets_aa_in_both_themes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every ink meets aa on EVERY ground in both themes
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_every_ink_meets_aa_on_EVERY_ground_in_both_themes` executed under `dev/.venv/bin/python`
- Expected: Not only on `surface`. The first version of this test checked white
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestContrast::test_every_ink_meets_aa_on_EVERY_ground_in_both_themes PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every risk step meets aa on its own ground
- Status: EXECUTED
- Input: `backend/tests/test_ui_tokens.py::TestContrast::test_every_risk_step_meets_aa_on_its_own_ground` executed under `dev/.venv/bin/python`
- Expected: every risk step meets aa on its own ground
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_tokens.py::TestContrast::test_every_risk_step_meets_aa_on_its_own_ground PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_ui_write_path.py`

### Scenario: a save posted without a clearing period does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_save_posted_without_a_clearing_period_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: a save posted without a clearing period does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_save_posted_without_a_clearing_period_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the item remains open and no partial record exists
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_item_remains_open_and_no_partial_record_exists` executed under `dev/.venv/bin/python`
- Expected: the item remains open and no partial record exists
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_item_remains_open_and_no_partial_record_exists PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the response names the missing expected clearing period
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_response_names_the_missing_expected_clearing_period` executed under `dev/.venv/bin/python`
- Expected: the response names the missing expected clearing period
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_the_response_names_the_missing_expected_clearing_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: there is no bypass parameter at any permission level
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_there_is_no_bypass_parameter_at_any_permission_level` executed under `dev/.venv/bin/python`
- Expected: `AC-F32-01` says "at every permission level including
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_there_is_no_bypass_parameter_at_any_permission_level PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a controller gets exactly the same refusal as a staff accountant
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_controller_gets_exactly_the_same_refusal_as_a_staff_accountant` executed under `dev/.venv/bin/python`
- Expected: a controller gets exactly the same refusal as a staff accountant
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_controller_gets_exactly_the_same_refusal_as_a_staff_accountant PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period not later than the current one is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_not_later_than_the_current_one_is_refused` executed under `dev/.venv/bin/python`
- Expected: a clearing period not later than the current one is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_not_later_than_the_current_one_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a clearing period beyond the maximum horizon is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_beyond_the_maximum_horizon_is_refused` executed under `dev/.venv/bin/python`
- Expected: a clearing period beyond the maximum horizon is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_clearing_period_beyond_the_maximum_horizon_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a malformed clearing period fails the same way as a missing one
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_malformed_clearing_period_fails_the_same_way_as_a_missing_one` executed under `dev/.venv/bin/python`
- Expected: Two ways to fail one control is one way too many: the second gets a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheClearingPeriodIsEnforcedByTheServer::test_a_malformed_clearing_period_fails_the_same_way_as_a_missing_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a close with no resolution type does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_close_with_no_resolution_type_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: a close with no resolution type does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_close_with_no_resolution_type_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an r1 without an expiry does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r1_without_an_expiry_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: an r1 without an expiry does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r1_without_an_expiry_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an r5 without both an owner and a due date does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r5_without_both_an_owner_and_a_due_date_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: an r5 without both an owner and a due date does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r5_without_both_an_owner_and_a_due_date_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a valid r2 completes and the store holds it
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_valid_r2_completes_and_the_store_holds_it` executed under `dev/.venv/bin/python`
- Expected: a valid r2 completes and the store holds it
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_valid_r2_completes_and_the_store_holds_it PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a closed item carries exactly one resolution type
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_closed_item_carries_exactly_one_resolution_type` executed under `dev/.venv/bin/python`
- Expected: `AC-F12-01`, as a fact about the database rather than the screen: a
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_a_closed_item_carries_exactly_one_resolution_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an r6 with an unreadable auto pass value does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_with_an_unreadable_auto_pass_value_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: `auto_pass_eligible` is tri-state on the way in: `False` is a real
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_with_an_unreadable_auto_pass_value_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an r6 changes the accounts control state observably
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_changes_the_accounts_control_state_observably` executed under `dev/.venv/bin/python`
- Expected: `AC-F35-04`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheResolutionTypeAndItsSchema::test_an_r6_changes_the_accounts_control_state_observably PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every disposition carries a capture in the same transaction
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_every_disposition_carries_a_capture_in_the_same_transaction` executed under `dev/.venv/bin/python`
- Expected: every disposition carries a capture in the same transaction
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_every_disposition_carries_a_capture_in_the_same_transaction PASSED` (verbatim from the `-v` node list of this run)

### Scenario: elapsed time is measured from the servers presentation clock
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_elapsed_time_is_measured_from_the_servers_presentation_clock` executed under `dev/.venv/bin/python`
- Expected: `AC-F12-02`. The clock starts when the review screen renders, on the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_elapsed_time_is_measured_from_the_servers_presentation_clock PASSED` (verbatim from the `-v` node list of this run)

### Scenario: re reading an item does not restart the clock
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_re_reading_an_item_does_not_restart_the_clock` executed under `dev/.venv/bin/python`
- Expected: re reading an item does not restart the clock
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_re_reading_an_item_does_not_restart_the_clock PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the capture names what was expanded and what was collapsed
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_the_capture_names_what_was_expanded_and_what_was_collapsed` executed under `dev/.venv/bin/python`
- Expected: `AC-F12-03`: BOTH sides. The collapsed set is computed as the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_the_capture_names_what_was_expanded_and_what_was_collapsed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a capture that cannot be written leaves the item open
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_a_capture_that_cannot_be_written_leaves_the_item_open` executed under `dev/.venv/bin/python`
- Expected: `AC-F12-07`, exercised through the service rather than the route,
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheF12Capture::test_a_capture_that_cannot_be_written_leaves_the_item_open PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a rejection with no reason does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_rejection_with_no_reason_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: a rejection with no reason does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_rejection_with_no_reason_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a reason outside the closed list does not complete
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_reason_outside_the_closed_list_does_not_complete` executed under `dev/.venv/bin/python`
- Expected: a reason outside the closed list does not complete
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_reason_outside_the_closed_list_does_not_complete PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a structured rejection records
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_structured_rejection_records` executed under `dev/.venv/bin/python`
- Expected: a structured rejection records
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_a_structured_rejection_records PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the closed list is a constraint on the column not a form check
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_the_closed_list_is_a_constraint_on_the_column_not_a_form_check` executed under `dev/.venv/bin/python`
- Expected: A form check is defeated by not using the form.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheStructuredRejection::test_the_closed_list_is_a_constraint_on_the_column_not_a_form_check PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a staff accountant is denied by the capability set test
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_staff_accountant_is_denied_by_the_capability_set_test` executed under `dev/.venv/bin/python`
- Expected: a staff accountant is denied by the capability set test
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_staff_accountant_is_denied_by_the_capability_set_test PASSED` (verbatim from the `-v` node list of this run)

### Scenario: that denial offers no override control because it is not eligible
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_that_denial_offers_no_override_control_because_it_is_not_eligible` executed under `dev/.venv/bin/python`
- Expected: that denial offers no override control because it is not eligible
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_that_denial_offers_no_override_control_because_it_is_not_eligible PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a controller above the limit is denied and offered an override
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_controller_above_the_limit_is_denied_and_offered_an_override` executed under `dev/.venv/bin/python`
- Expected: a controller above the limit is denied and offered an override
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_controller_above_the_limit_is_denied_and_offered_an_override PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the override control requires a second authoriser and a reason code
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_override_control_requires_a_second_authoriser_and_a_reason_code` executed under `dev/.venv/bin/python`
- Expected: the override control requires a second authoriser and a reason code
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_override_control_requires_a_second_authoriser_and_a_reason_code PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the reason list comes from the broker not from the interface
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_reason_list_comes_from_the_broker_not_from_the_interface` executed under `dev/.venv/bin/python`
- Expected: the reason list comes from the broker not from the interface
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_the_reason_list_comes_from_the_broker_not_from_the_interface PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override with a second authoriser completes the approval
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_with_a_second_authoriser_completes_the_approval` executed under `dev/.venv/bin/python`
- Expected: an override with a second authoriser completes the approval
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_with_a_second_authoriser_completes_the_approval PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an override naming the requester as an authoriser is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_naming_the_requester_as_an_authoriser_is_refused` executed under `dev/.venv/bin/python`
- Expected: an override naming the requester as an authoriser is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_an_override_naming_the_requester_as_an_authoriser_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no approval record exists without a broker decision id
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_no_approval_record_exists_without_a_broker_decision_id` executed under `dev/.venv/bin/python`
- Expected: The structural half of `AC-F41-11`: the store refuses one.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_no_approval_record_exists_without_a_broker_decision_id PASSED` (verbatim from the `-v` node list of this run)

### Scenario: when persisting the approval fails the proposal stays unapproved
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_when_persisting_the_approval_fails_the_proposal_stays_unapproved` executed under `dev/.venv/bin/python`
- Expected: `AC-F41-11`. The broker's decision still exists — correctly, because
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_when_persisting_the_approval_fails_the_proposal_stays_unapproved PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a broker that cannot be reached is not rendered as a denial
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_broker_that_cannot_be_reached_is_not_rendered_as_a_denial` executed under `dev/.venv/bin/python`
- Expected: a broker that cannot be reached is not rendered as a denial
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheApprovalPath::test_a_broker_that_cannot_be_reached_is_not_rendered_as_a_denial PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an export without an in product approval is refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_without_an_in_product_approval_is_refused` executed under `dev/.venv/bin/python`
- Expected: `AC-F40-03`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_without_an_in_product_approval_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the refusal is at ges and not only in the interface
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_refusal_is_at_ges_and_not_only_in_the_interface` executed under `dev/.venv/bin/python`
- Expected: The interface's early refusal is a courtesy. Remove it and GES still
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_refusal_is_at_ges_and_not_only_in_the_interface PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an approved proposal produces a balanced file
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_approved_proposal_produces_a_balanced_file` executed under `dev/.venv/bin/python`
- Expected: an approved proposal produces a balanced file
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_approved_proposal_produces_a_balanced_file PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the file carries the reserved source and category and no other
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_file_carries_the_reserved_source_and_category_and_no_other` executed under `dev/.venv/bin/python`
- Expected: `AC-F40-04`.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_the_file_carries_the_reserved_source_and_category_and_no_other PASSED` (verbatim from the `-v` node list of this run)

### Scenario: our identifiers are stamped into the reference columns
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_our_identifiers_are_stamped_into_the_reference_columns` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §10.1 / J-9: every entry this system caused is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_our_identifiers_are_stamped_into_the_reference_columns PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an export with unverified cuecs is refused naming them
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_with_unverified_cuecs_is_refused_naming_them` executed under `dev/.venv/bin/python`
- Expected: `AC-F40-05`, against a register that has NOT been verified — which is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_export_with_unverified_cuecs_is_refused_naming_them PASSED` (verbatim from the `-v` node list of this run)

### Scenario: never verified is not collapsed into failed
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_never_verified_is_not_collapsed_into_failed` executed under `dev/.venv/bin/python`
- Expected: never verified is not collapsed into failed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_never_verified_is_not_collapsed_into_failed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an expired verification is not a pass
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_expired_verification_is_not_a_pass` executed under `dev/.venv/bin/python`
- Expected: an expired verification is not a pass
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_expired_verification_is_not_a_pass PASSED` (verbatim from the `-v` node list of this run)

### Scenario: zero approved lines produces no file rather than an empty one
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_zero_approved_lines_produces_no_file_rather_than_an_empty_one` executed under `dev/.venv/bin/python`
- Expected: `AC-F40-08`: an empty batch file is the one artefact a loader would
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_zero_approved_lines_produces_no_file_rather_than_an_empty_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unbalanced batch is refused rather than written
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_unbalanced_batch_is_refused_rather_than_written` executed under `dev/.venv/bin/python`
- Expected: an unbalanced batch is refused rather than written
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheExportPath::test_an_unbalanced_batch_is_refused_rather_than_written PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the export module has no submit and no http call
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_export_module_has_no_submit_and_no_http_call` executed under `dev/.venv/bin/python`
- Expected: the export module has no submit and no http call
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_export_module_has_no_submit_and_no_http_call PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no route on the ui surface names a posting verb
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_no_route_on_the_ui_surface_names_a_posting_verb` executed under `dev/.venv/bin/python`
- Expected: no route on the ui surface names a posting verb
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_no_route_on_the_ui_surface_names_a_posting_verb PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the produced artefact states that it posts nothing
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_produced_artefact_states_that_it_posts_nothing` executed under `dev/.venv/bin/python`
- Expected: the produced artefact states that it posts nothing
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestNothingInThisBuildPosts::test_the_produced_artefact_states_that_it_posts_nothing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: open predictions are visible with their expected clearing periods
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_open_predictions_are_visible_with_their_expected_clearing_periods` executed under `dev/.venv/bin/python`
- Expected: open predictions are visible with their expected clearing periods
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_open_predictions_are_visible_with_their_expected_clearing_periods PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a missed prediction is distinguishable from one within its horizon
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_a_missed_prediction_is_distinguishable_from_one_within_its_horizon` executed under `dev/.venv/bin/python`
- Expected: a missed prediction is distinguishable from one within its horizon
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_a_missed_prediction_is_distinguishable_from_one_within_its_horizon PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the missed row is a real verification result not a label
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_missed_row_is_a_real_verification_result_not_a_label` executed under `dev/.venv/bin/python`
- Expected: The miss comes from `run_verification` having actually run over an
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_missed_row_is_a_real_verification_result_not_a_label PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the zero open state names the period
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_zero_open_state_names_the_period` executed under `dev/.venv/bin/python`
- Expected: `AC-F35-07`: never a blank region and never a spinner.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheDispositionsScreen::test_the_zero_open_state_names_the_period PASSED` (verbatim from the `-v` node list of this run)

### Scenario: no route module reaches a multipart parser
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_no_route_module_reaches_a_multipart_parser` executed under `dev/.venv/bin/python`
- Expected: no route module reaches a multipart parser
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_no_route_module_reaches_a_multipart_parser PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a multipart body is read as nothing submitted and refused
- Status: EXECUTED
- Input: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_a_multipart_body_is_read_as_nothing_submitted_and_refused` executed under `dev/.venv/bin/python`
- Expected: a multipart body is read as nothing submitted and refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_ui_write_path.py::TestTheSurfaceAcceptsNoFileUpload::test_a_multipart_body_is_read_as_nothing_submitted_and_refused PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_version_registry.py`

### Scenario: a stamp is exactly the six elements of AC F2 01
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_stamp_is_exactly_the_six_elements_of_AC_F2_01` executed under `dev/.venv/bin/python`
- Expected: a stamp is exactly the six elements of AC F2 01
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_stamp_is_exactly_the_six_elements_of_AC_F2_01 PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a stamp refuses an element the criterion does not name
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_stamp_refuses_an_element_the_criterion_does_not_name` executed under `dev/.venv/bin/python`
- Expected: a stamp refuses an element the criterion does not name
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_stamp_refuses_an_element_the_criterion_does_not_name PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a stamp is immutable so a re read shows what was in force
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_stamp_is_immutable_so_a_re_read_shows_what_was_in_force` executed under `dev/.venv/bin/python`
- Expected: `AC-F2-02`. There is no setter, so there is nothing to update.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_stamp_is_immutable_so_a_re_read_shows_what_was_in_force PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[model]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[model]` executed under `dev/.venv/bin/python`, parameter case `model`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[model] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[prompt]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[prompt]` executed under `dev/.venv/bin/python`, parameter case `prompt`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[prompt] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[tool_config]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[tool_config]` executed under `dev/.venv/bin/python`, parameter case `tool_config`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[tool_config] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[corpus]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[corpus]` executed under `dev/.venv/bin/python`, parameter case `corpus`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[corpus] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[dataset]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[dataset]` executed under `dev/.venv/bin/python`, parameter case `dataset`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[dataset] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single absent element makes the stamp incomplete and names it[guardrail_bundle_hash]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[guardrail_bundle_hash]` executed under `dev/.venv/bin/python`, parameter case `guardrail_bundle_hash`
- Expected: `AC-F2-08`'s boundary: *any* of the six, not a favoured subset.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_absent_element_makes_the_stamp_incomplete_and_names_it[guardrail_bundle_hash] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank element is missing not present[]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_blank_element_is_missing_not_present[]` executed under `dev/.venv/bin/python`, parameter case ``
- Expected: a blank element is missing not present
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_blank_element_is_missing_not_present[] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a blank element is missing not present[   ]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_blank_element_is_missing_not_present[   ]` executed under `dev/.venv/bin/python`, parameter case `   `
- Expected: a blank element is missing not present
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_blank_element_is_missing_not_present[   ] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: none the string is a DECLARATION and is not missing
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_none_the_string_is_a_DECLARATION_and_is_not_missing` executed under `dev/.venv/bin/python`
- Expected: The distinction the whole design turns on: `none` is somebody saying
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_none_the_string_is_a_DECLARATION_and_is_not_missing PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a payload with no stamp at all yields six missing not an exception
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_payload_with_no_stamp_at_all_yields_six_missing_not_an_exception` executed under `dev/.venv/bin/python`
- Expected: a payload with no stamp at all yields six missing not an exception
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_payload_with_no_stamp_at_all_yields_six_missing_not_an_exception PASSED` (verbatim from the `-v` node list of this run)

### Scenario: stamp from passes a stamp through unchanged
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_stamp_from_passes_a_stamp_through_unchanged` executed under `dev/.venv/bin/python`
- Expected: stamp from passes a stamp through unchanged
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_stamp_from_passes_a_stamp_through_unchanged PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unknown element cannot be registered
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_an_unknown_element_cannot_be_registered` executed under `dev/.venv/bin/python`
- Expected: an unknown element cannot be registered
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_an_unknown_element_cannot_be_registered PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a deprecation cannot be registered without its date
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_deprecation_cannot_be_registered_without_its_date` executed under `dev/.venv/bin/python`
- Expected: `AC-F2-05` requires the deprecation to be STATED WITH ITS DATE. A build
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_deprecation_cannot_be_registered_without_its_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: resolve names the artefact it could not find
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_resolve_names_the_artefact_it_could_not_find` executed under `dev/.venv/bin/python`
- Expected: resolve names the artefact it could not find
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_resolve_names_the_artefact_it_could_not_find PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an empty version is unregistered rather than a wildcard
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_an_empty_version_is_unregistered_rather_than_a_wildcard` executed under `dev/.venv/bin/python`
- Expected: an empty version is unregistered rather than a wildcard
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_an_empty_version_is_unregistered_rather_than_a_wildcard PASSED` (verbatim from the `-v` node list of this run)

### Scenario: deprecations carry the version and the date
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_deprecations_carry_the_version_and_the_date` executed under `dev/.venv/bin/python`
- Expected: deprecations carry the version and the date
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_deprecations_carry_the_version_and_the_date PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the current version carries no deprecation
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_the_current_version_carries_no_deprecation` executed under `dev/.venv/bin/python`
- Expected: the current version carries no deprecation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_the_current_version_carries_no_deprecation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the bundle hash is never reported unregistered because it is content addressed
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_the_bundle_hash_is_never_reported_unregistered_because_it_is_content_addressed` executed under `dev/.venv/bin/python`
- Expected: the bundle hash is never reported unregistered because it is content addressed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_the_bundle_hash_is_never_reported_unregistered_because_it_is_content_addressed PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unregistered dataset is reported by element and version
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_an_unregistered_dataset_is_reported_by_element_and_version` executed under `dev/.venv/bin/python`
- Expected: an unregistered dataset is reported by element and version
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_an_unregistered_dataset_is_reported_by_element_and_version PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a registry read cannot be mutated through the record it returns
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_registry_read_cannot_be_mutated_through_the_record_it_returns` executed under `dev/.venv/bin/python`
- Expected: a registry read cannot be mutated through the record it returns
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_registry_read_cannot_be_mutated_through_the_record_it_returns PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a change record carries what changed from what to what whose and when
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_change_record_carries_what_changed_from_what_to_what_whose_and_when` executed under `dev/.venv/bin/python`
- Expected: a change record carries what changed from what to what whose and when
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_change_record_carries_what_changed_from_what_to_what_whose_and_when PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a change record without its owner or date cannot be constructed[owner]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_change_record_without_its_owner_or_date_cannot_be_constructed[owner]` executed under `dev/.venv/bin/python`, parameter case `owner`
- Expected: a change record without its owner or date cannot be constructed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_change_record_without_its_owner_or_date_cannot_be_constructed[owner] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a change record without its owner or date cannot be constructed[effective_date]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_change_record_without_its_owner_or_date_cannot_be_constructed[effective_date]` executed under `dev/.venv/bin/python`, parameter case `effective_date`
- Expected: a change record without its owner or date cannot be constructed
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_change_record_without_its_owner_or_date_cannot_be_constructed[effective_date] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a quiet period STATES that nothing changed and names itself
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_quiet_period_STATES_that_nothing_changed_and_names_itself` executed under `dev/.venv/bin/python`
- Expected: `AC-F2-06`. The empty case is the criterion, not an edge of it.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_quiet_period_STATES_that_nothing_changed_and_names_itself PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a busy period also carries a statement so a caller never invents one
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_busy_period_also_carries_a_statement_so_a_caller_never_invents_one` executed under `dev/.venv/bin/python`
- Expected: a busy period also carries a statement so a caller never invents one
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_busy_period_also_carries_a_statement_so_a_caller_never_invents_one PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a complete stamp over a readable registry is usable
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_complete_stamp_over_a_readable_registry_is_usable` executed under `dev/.venv/bin/python`
- Expected: a complete stamp over a readable registry is usable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_complete_stamp_over_a_readable_registry_is_usable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[model]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[model]` executed under `dev/.venv/bin/python`, parameter case `model`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[model] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[prompt]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[prompt]` executed under `dev/.venv/bin/python`, parameter case `prompt`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[prompt] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[tool_config]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[tool_config]` executed under `dev/.venv/bin/python`, parameter case `tool_config`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[tool_config] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[corpus]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[corpus]` executed under `dev/.venv/bin/python`, parameter case `corpus`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[corpus] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[dataset]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[dataset]` executed under `dev/.venv/bin/python`, parameter case `dataset`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[dataset] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: any single missing element makes the closure input unusable[guardrail_bundle_hash]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[guardrail_bundle_hash]` executed under `dev/.venv/bin/python`, parameter case `guardrail_bundle_hash`
- Expected: any single missing element makes the closure input unusable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_any_single_missing_element_makes_the_closure_input_unusable[guardrail_bundle_hash] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unresolvable registry is unusable and says which fact it is
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_an_unresolvable_registry_is_unusable_and_says_which_fact_it_is` executed under `dev/.venv/bin/python`
- Expected: an unresolvable registry is unusable and says which fact it is
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_an_unresolvable_registry_is_unusable_and_says_which_fact_it_is PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unresolvable registry is checked BEFORE the stamp
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_an_unresolvable_registry_is_checked_BEFORE_the_stamp` executed under `dev/.venv/bin/python`
- Expected: Order matters for the message. With both wrong, the registry is the
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_an_unresolvable_registry_is_checked_BEFORE_the_stamp PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a registry that raises something unexpected is also unresolvable
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_registry_that_raises_something_unexpected_is_also_unresolvable` executed under `dev/.venv/bin/python`
- Expected: a registry that raises something unexpected is also unresolvable
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_registry_that_raises_something_unexpected_is_also_unresolvable PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a complete but unregistered stamp is unusable and names the element
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_a_complete_but_unregistered_stamp_is_unusable_and_names_the_element` executed under `dev/.venv/bin/python`
- Expected: a complete but unregistered stamp is unusable and names the element
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_a_complete_but_unregistered_stamp_is_unusable_and_names_the_element PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[register]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[register]` executed under `dev/.venv/bin/python`, parameter case `register`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[register] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[record_change]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[record_change]` executed under `dev/.venv/bin/python`, parameter case `record_change`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[record_change] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[resolve]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[resolve]` executed under `dev/.venv/bin/python`, parameter case `resolve`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[resolve] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[is_registered]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[is_registered]` executed under `dev/.venv/bin/python`, parameter case `is_registered`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[is_registered] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[deprecations]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[deprecations]` executed under `dev/.venv/bin/python`, parameter case `deprecations`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[deprecations] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[unregistered_in]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[unregistered_in]` executed under `dev/.venv/bin/python`, parameter case `unregistered_in`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[unregistered_in] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: every read on an unavailable registry raises rather than returning less[changelog]
- Status: EXECUTED
- Input: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[changelog]` executed under `dev/.venv/bin/python`, parameter case `changelog`
- Expected: There is no read on this object a caller could mistake for a smaller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_version_registry.py::test_every_read_on_an_unavailable_registry_raises_rather_than_returning_less[changelog] PASSED` (verbatim from the `-v` node list of this run)


## `backend/tests/test_wedge.py`

### Scenario: the omission is found and grounded in its history
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_omission_is_found_and_grounded_in_its_history` executed under `dev/.venv/bin/python`
- Expected: the omission is found and grounded in its history
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_omission_is_found_and_grounded_in_its_history PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member present within its range raises no omission
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_member_present_within_its_range_raises_no_omission` executed under `dev/.venv/bin/python`
- Expected: a member present within its range raises no omission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_member_present_within_its_range_raises_no_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member present but far outside its range raises no omission
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_member_present_but_far_outside_its_range_raises_no_omission` executed under `dev/.venv/bin/python`
- Expected: a member present but far outside its range raises no omission
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_member_present_but_far_outside_its_range_raises_no_omission PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a member with too little history is not evaluable and not reported clear
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_member_with_too_little_history_is_not_evaluable_and_not_reported_clear` executed under `dev/.venv/bin/python`
- Expected: a member with too little history is not evaluable and not reported clear
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_member_with_too_little_history_is_not_evaluable_and_not_reported_clear PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the finding carries a dossier reference and the coverage statement
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_finding_carries_a_dossier_reference_and_the_coverage_statement` executed under `dev/.venv/bin/python`
- Expected: the finding carries a dossier reference and the coverage statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_finding_carries_a_dossier_reference_and_the_coverage_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a run makes zero model calls
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_run_makes_zero_model_calls` executed under `dev/.venv/bin/python`
- Expected: a run makes zero model calls
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_run_makes_zero_model_calls PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the present anomaly detector finds the outlier
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_present_anomaly_detector_finds_the_outlier` executed under `dev/.venv/bin/python`
- Expected: the present anomaly detector finds the outlier
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_present_anomaly_detector_finds_the_outlier PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the anomaly finding states its threshold and inclusivity
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_anomaly_finding_states_its_threshold_and_inclusivity` executed under `dev/.venv/bin/python`
- Expected: the anomaly finding states its threshold and inclusivity
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_anomaly_finding_states_its_threshold_and_inclusivity PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the anomaly detector does not fire on an in range member
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_anomaly_detector_does_not_fire_on_an_in_range_member` executed under `dev/.venv/bin/python`
- Expected: the anomaly detector does not fire on an in range member
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_anomaly_detector_does_not_fire_on_an_in_range_member PASSED` (verbatim from the `-v` node list of this run)

### Scenario: f42 reports nothing for the omitted member
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_f42_reports_nothing_for_the_omitted_member` executed under `dev/.venv/bin/python`
- Expected: f42 reports nothing for the omitted member
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_f42_reports_nothing_for_the_omitted_member PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the paired comparison is one artefact naming both runs
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_paired_comparison_is_one_artefact_naming_both_runs` executed under `dev/.venv/bin/python`
- Expected: the paired comparison is one artefact naming both runs
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_paired_comparison_is_one_artefact_naming_both_runs PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the comparison is over an identical selection
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_comparison_is_over_an_identical_selection` executed under `dev/.venv/bin/python`
- Expected: the comparison is over an identical selection
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_comparison_is_over_an_identical_selection PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a comparison over different selections is refused
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_comparison_over_different_selections_is_refused` executed under `dev/.venv/bin/python`
- Expected: a comparison over different selections is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_comparison_over_different_selections_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a comparison involving an incomplete run is refused
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_comparison_involving_an_incomplete_run_is_refused` executed under `dev/.venv/bin/python`
- Expected: a comparison involving an incomplete run is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_comparison_involving_an_incomplete_run_is_refused PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the wedge is not demonstrated when the omission is absent from the world
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_wedge_is_not_demonstrated_when_the_omission_is_absent_from_the_world` executed under `dev/.venv/bin/python`
- Expected: the wedge is not demonstrated when the omission is absent from the world
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_wedge_is_not_demonstrated_when_the_omission_is_absent_from_the_world PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the omission detector passes its declared fixture pair
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_omission_detector_passes_its_declared_fixture_pair` executed under `dev/.venv/bin/python`
- Expected: the omission detector passes its declared fixture pair
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_omission_detector_passes_its_declared_fixture_pair PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the anomaly detector is silent about the omitted member in both fixtures
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_the_anomaly_detector_is_silent_about_the_omitted_member_in_both_fixtures` executed under `dev/.venv/bin/python`
- Expected: the anomaly detector is silent about the omitted member in both fixtures
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_the_anomaly_detector_is_silent_about_the_omitted_member_in_both_fixtures PASSED` (verbatim from the `-v` node list of this run)

### Scenario: a run with no resolvable population does not start
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_a_run_with_no_resolvable_population_does_not_start` executed under `dev/.venv/bin/python`
- Expected: a run with no resolvable population does not start
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_a_run_with_no_resolvable_population_does_not_start PASSED` (verbatim from the `-v` node list of this run)

### Scenario: an unavailable dataset makes the run incomplete with no conclusion
- Status: EXECUTED
- Input: `backend/tests/test_wedge.py::test_an_unavailable_dataset_makes_the_run_incomplete_with_no_conclusion` executed under `dev/.venv/bin/python`
- Expected: an unavailable dataset makes the run incomplete with no conclusion
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `backend/tests/test_wedge.py::test_an_unavailable_dataset_makes_the_run_incomplete_with_no_conclusion PASSED` (verbatim from the `-v` node list of this run)


