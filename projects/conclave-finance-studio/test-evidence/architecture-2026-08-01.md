# Test evidence — `architecture` suite

**Run date:** 2026-08-01 (Gate 8 · Test re-run, post-pass-5)  
**Commit under test:** `dev` @ `b1b5dde` — "The ID-to-scenario joins stop being inferred, and 186 + 77 stops being 262"  
**Project repo:** `6dae43e`  
**Suite owner:** `solution-architect`  
**Entry point:** `tests/suites/architecture/run.sh`  
**Status:** `EXECUTED`  
**Exit code:** 0  
**Scenarios:** 23 executed — 23 PASS, 0 FAIL, 0 SKIPPED  
**Blocking:** yes (PROJECT_CONTEXT Active Team — "Test Policy: all suites blocking", no advisory exception)

This file REPLACES the `architecture-2026-07-31.md` written before the gate-8
loop-back. That file described a commit at which four detector families
(F26, F28, F9, F33) did not exist and in which scenario names it cited had
since been renamed. It was deleted rather than left beside this one.

---

## Per-scenario evidence

### Scenario: test_ARCH_02_no_request_model_field_can_carry_a_statement
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_request_model_field_can_carry_a_statement`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_request_model_field_can_carry_a_statement PASSED [  4%]`

### Scenario: test_ARCH_02_no_ges_route_declares_a_sql_parameter
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_ges_route_declares_a_sql_parameter`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_ges_route_declares_a_sql_parameter PASSED [  8%]`

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT * FROM gl_je_lines] PASSED [ 13%]`

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence;
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence;`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines] PASSED [ 17%]`

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1'
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1'`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1' OR '1'='1] PASSED [ 21%]`

### Scenario: test_ARCH_02_no_application_function_accepts_a_parameter_named_sql
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_application_function_accepts_a_parameter_named_sql`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_application_function_accepts_a_parameter_named_sql PASSED [ 26%]`

### Scenario: test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller PASSED [ 30%]`

### Scenario: test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type PASSED [ 34%]`

### Scenario: test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module PASSED [ 39%]`

### Scenario: test_ARCH_08_no_module_reaches_for_the_private_constructor_key
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_no_module_reaches_for_the_private_constructor_key`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_no_module_reaches_for_the_private_constructor_key PASSED [ 43%]`

### Scenario: test_ARCH_09_one_object_three_renderers_agree_on_coverage
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_09_one_object_three_renderers_agree_on_coverage`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_09_one_object_three_renderers_agree_on_coverage PASSED [ 47%]`

### Scenario: test_ARCH_10_update_and_delete_fail_at_the_storage_layer
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_update_and_delete_fail_at_the_storage_layer`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_update_and_delete_fail_at_the_storage_layer PASSED [ 52%]`

### Scenario: test_ARCH_10_a_refused_mutation_appends_a_control_event
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_a_refused_mutation_appends_a_control_event`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_a_refused_mutation_appends_a_control_event PASSED [ 56%]`

### Scenario: test_ARCH_11_an_altered_dossier_is_identified
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_an_altered_dossier_is_identified`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_an_altered_dossier_is_identified PASSED [ 60%]`

### Scenario: test_ARCH_11_anchors_record_that_the_signer_is_a_stub
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_anchors_record_that_the_signer_is_a_stub`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_anchors_record_that_the_signer_is_a_stub PASSED [ 65%]`

### Scenario: test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation PASSED [ 69%]`

### Scenario: test_ARCH_15_a_population_carries_a_source_class_not_a_table
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_population_carries_a_source_class_not_a_table`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_population_carries_a_source_class_not_a_table PASSED [ 73%]`

### Scenario: test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class PASSED [ 78%]`

### Scenario: test_ARCH_18_a_detector_run_observes_zero_model_invocations
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_detector_run_observes_zero_model_invocations`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_detector_run_observes_zero_model_invocations PASSED [ 82%]`

### Scenario: test_ARCH_18_a_model_call_from_inside_a_detector_raises
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_model_call_from_inside_a_detector_raises`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_model_call_from_inside_a_detector_raises PASSED [ 86%]`

### Scenario: test_the_api_package_never_imports_the_ges_package
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package PASSED [ 91%]`

### Scenario: test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket PASSED [ 95%]`

### Scenario: test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused`
- Expected: the scenario's assertions hold against the code at `b1b5dde`
- Actual: pytest reported PASS
- Result: PASS
- Evidence: `tests/suites/architecture/run.sh` — pytest -v line: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused PASSED [100%]`
