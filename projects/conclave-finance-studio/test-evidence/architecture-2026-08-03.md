# Test evidence — architecture suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Suite owner:** `solution-architect` — scenarios authored by that agent, **executed and reported here by `test-agent`**
**Blocking:** yes (project Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**28 scenarios, 28 pass, 0 fail, 0 skip, exit 0.**

Entry point `dev/tests/suites/_runner.sh architecture`, which reported
`EXECUTED — suite passed` (exit 0). The same scenarios also ran inside all six
whole-tree runs (canonical, `file`, `reverse`, three salted shuffles) and inside
the AST-instrumented run.

## Test-count delta

| | Previous run (`e00a214`) | This run (`c428fe5`) | Delta |
|---|---|---|---|
| collected | 28 | **28** | **0 — unchanged** |
| added | — | — | 0 |
| removed | — | — | **0** |
| changed in place | — | — | 0 |

No scenario was removed from this suite.

---

### Scenario: test_ARCH_02_no_request_model_field_can_carry_a_statement
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_request_model_field_can_carry_a_statement`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_02_no_ges_route_declares_a_sql_parameter
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_ges_route_declares_a_sql_parameter`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT * FROM gl_je_lines]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[SELECT * FROM gl_je_lines]`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[gl.entries_by_recurrence; DROP TABLE gl_je_lines]`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1' OR '1'='1]
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_a_sql_string_posted_to_the_only_execution_route_is_refused[1' OR '1'='1]`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_02_no_application_function_accepts_a_parameter_named_sql
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_02_no_application_function_accepts_a_parameter_named_sql`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_full_population_conclusion_is_unconstructible_by_a_caller`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_no_exceptions_variant_exists_on_exactly_one_type`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_the_all_clear_phrases_appear_in_exactly_one_module`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_08_no_module_reaches_for_the_private_constructor_key
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_08_no_module_reaches_for_the_private_constructor_key`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_09_one_object_three_renderers_agree_on_coverage
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_09_one_object_three_renderers_agree_on_coverage`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_10_update_and_delete_fail_at_the_storage_layer
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_update_and_delete_fail_at_the_storage_layer`
- Expected: Both evidence tables refuse both mutations.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_10_a_refused_mutation_appends_a_control_event
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_10_a_refused_mutation_appends_a_control_event`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_11_an_altered_dossier_is_identified
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_an_altered_dossier_is_identified`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_11_anchors_record_that_the_signer_is_a_stub
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_11_anchors_record_that_the_signer_is_a_stub`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_manifest_naming_a_physical_table_fails_compilation`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_15_a_population_carries_a_source_class_not_a_table
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_a_population_carries_a_source_class_not_a_table`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_15_the_detector_runs_unchanged_against_a_non_erp_source_class`
- Expected: The seam, exercised rather than asserted.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_18_a_detector_run_observes_zero_model_invocations
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_detector_run_observes_zero_model_invocations`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_18_a_model_call_from_inside_a_detector_raises
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_18_a_model_call_from_inside_a_detector_raises`
- Expected: as stated by the scenario's own assertions
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_the_api_package_never_imports_the_ges_package
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package`
- Expected: A process boundary that a module import crosses is a module boundary.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
- Expected: `ARCHITECTURE_KB` §3.2 — the trust boundary is a PROCESS boundary.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused`
- Expected: The second process is not merely present, it is CLOSED.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_05_the_pilots_own_bootstrap_migrates_a_warehouse_it_did_not_write
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_05_the_pilots_own_bootstrap_migrates_a_warehouse_it_did_not_write`
- Expected: The exact call `backend/pilot.py` makes at start-up.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_05_the_certified_query_the_export_refused_on_now_executes
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_05_the_certified_query_the_export_refused_on_now_executes`
- Expected: `poar.export_basis@1`, over the migrated persisted warehouse.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_ARCH_05_a_persisted_warehouse_keeps_the_pilots_deliberate_omission
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_ARCH_05_a_persisted_warehouse_keeps_the_pilots_deliberate_omission`
- Expected: `AC-F28-07`'s "not run" state is a property of the pilot warehouse, and a persisted file written by a FULL seed silently puts the omitted object back — taking away the one state a reviewer most needs to recognise, with nothing failing.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger`
- Expected: The app under `ges_http` records its decisions in a tmp-path ledger.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders

### Scenario: test_the_guard_against_the_live_ledger_is_installed_in_this_tree_too
- Status: EXECUTED
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_guard_against_the_live_ledger_is_installed_in_this_tree_too`
- Expected: A GES app built the leaking way is REFUSED here, not merely absent here.
- Actual: executed, assertions held
- Result: PASS
- Evidence: `_runner.sh architecture` exit 0; same node id green in all six collection orders
