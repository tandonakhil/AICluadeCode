# Test evidence — `architecture` suite

**Project:** conclave-finance-studio  
**Gate:** 8 · Test (re-run)  
**Date:** 2026-08-01  
**Commit under test:** `dev` @ **`f56ab9f`** · parent repo @ **`8939ebb`**  
**Owner:** `solution-architect`  
**Blocking:** yes (no Test Policy exception is recorded for this project)  
**Status:** `EXECUTED`  
**Entry point:** `tests/suites/architecture/run.sh`  
**Interpreter:** `dev/.venv/bin/python` (Python 3.9)  
**Exit code:** 0  
**Scenarios: 23 — PASS 23, FAIL 0, skipped 0**

> This corpus was regenerated in full at `f56ab9f` and the `b1b5dde` corpus was
> deleted, not left beside it. Every entry below corresponds to a node ID
> that actually executed in this run; none is a static reading.

---

## `tests/suites/architecture/test_architecture_conformance.py`

### Scenario: ARCH 02 no request model field can carry a statement
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_request_model_field_can_carry_a_statement` executed under `dev/.venv/bin/python`
- Expected: ARCH 02 no request model field can carry a statement
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_request_model_field_can_carry_a_statement PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 02 no ges route declares a sql parameter
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_ges_route_declares_a_sql_parameter` executed under `dev/.venv/bin/python`
- Expected: ARCH 02 no ges route declares a sql parameter
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_ges_route_declares_a_sql_parameter PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 02 a sql string posted to the only execution route is refused[SELECT * FROM gl_je_lines]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT * FROM gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `SELECT * FROM gl_je_lines`
- Expected: ARCH 02 a sql string posted to the only execution route is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT * FROM gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 02 a sql string posted to the only execution route is refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines]` executed under `dev/.venv/bin/python`, parameter case `gl.entries_by_recurrence; DROP TABLE gl_je_lines`
- Expected: ARCH 02 a sql string posted to the only execution route is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 02 a sql string posted to the only execution route is refused[1' OR '1'='1]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1' OR '1'='1]` executed under `dev/.venv/bin/python`, parameter case `1' OR '1'='1`
- Expected: ARCH 02 a sql string posted to the only execution route is refused
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1' OR '1'='1] PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 02 no application function accepts a parameter named sql
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_application_function_accepts_a_parameter_named_sql` executed under `dev/.venv/bin/python`
- Expected: ARCH 02 no application function accepts a parameter named sql
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_application_function_accepts_a_parameter_named_sql PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 08 full population conclusion is unconstructible by a caller
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller` executed under `dev/.venv/bin/python`
- Expected: ARCH 08 full population conclusion is unconstructible by a caller
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 08 the no exceptions variant exists on exactly one type
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type` executed under `dev/.venv/bin/python`
- Expected: ARCH 08 the no exceptions variant exists on exactly one type
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 08 the all clear phrases appear in exactly one module
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module` executed under `dev/.venv/bin/python`
- Expected: ARCH 08 the all clear phrases appear in exactly one module
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 08 no module reaches for the private constructor key
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_no_module_reaches_for_the_private_constructor_key` executed under `dev/.venv/bin/python`
- Expected: ARCH 08 no module reaches for the private constructor key
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_no_module_reaches_for_the_private_constructor_key PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 09 one object three renderers agree on coverage
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_09_one_object_three_renderers_agree_on_coverage` executed under `dev/.venv/bin/python`
- Expected: ARCH 09 one object three renderers agree on coverage
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_09_one_object_three_renderers_agree_on_coverage PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 10 update and delete fail at the storage layer
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_update_and_delete_fail_at_the_storage_layer` executed under `dev/.venv/bin/python`
- Expected: Both evidence tables refuse both mutations.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_update_and_delete_fail_at_the_storage_layer PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 10 a refused mutation appends a control event
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_a_refused_mutation_appends_a_control_event` executed under `dev/.venv/bin/python`
- Expected: ARCH 10 a refused mutation appends a control event
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_a_refused_mutation_appends_a_control_event PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 11 an altered dossier is identified
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_an_altered_dossier_is_identified` executed under `dev/.venv/bin/python`
- Expected: ARCH 11 an altered dossier is identified
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_an_altered_dossier_is_identified PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 11 anchors record that the signer is a stub
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_anchors_record_that_the_signer_is_a_stub` executed under `dev/.venv/bin/python`
- Expected: ARCH 11 anchors record that the signer is a stub
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_anchors_record_that_the_signer_is_a_stub PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 15 a manifest naming a physical table fails compilation
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation` executed under `dev/.venv/bin/python`
- Expected: ARCH 15 a manifest naming a physical table fails compilation
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 15 a population carries a source class not a table
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_population_carries_a_source_class_not_a_table` executed under `dev/.venv/bin/python`
- Expected: ARCH 15 a population carries a source class not a table
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_population_carries_a_source_class_not_a_table PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 15 the detector runs unchanged against a non erp source class
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class` executed under `dev/.venv/bin/python`
- Expected: The seam, exercised rather than asserted.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 18 a detector run observes zero model invocations
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_detector_run_observes_zero_model_invocations` executed under `dev/.venv/bin/python`
- Expected: ARCH 18 a detector run observes zero model invocations
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_detector_run_observes_zero_model_invocations PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 18 a model call from inside a detector raises
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_model_call_from_inside_a_detector_raises` executed under `dev/.venv/bin/python`
- Expected: ARCH 18 a model call from inside a detector raises
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_model_call_from_inside_a_detector_raises PASSED` (verbatim from the `-v` node list of this run)

### Scenario: the api package never imports the ges package
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package` executed under `dev/.venv/bin/python`
- Expected: A process boundary that a module import crosses is a module boundary.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 04 the deployment topology is two processes talking over a socket
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket` executed under `dev/.venv/bin/python`
- Expected: `ARCHITECTURE_KB` §3.2 — the trust boundary is a PROCESS boundary.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket PASSED` (verbatim from the `-v` node list of this run)

### Scenario: ARCH 04 the socket is authenticated and an unheaded caller is refused
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused` executed under `dev/.venv/bin/python`
- Expected: The second process is not merely present, it is CLOSED.
- Actual: pytest reported **PASSED**
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused PASSED` (verbatim from the `-v` node list of this run)


