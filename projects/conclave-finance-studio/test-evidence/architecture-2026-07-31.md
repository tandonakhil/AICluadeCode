# Test evidence — architecture suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 13 verification)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `solution-architect` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/architecture/run.sh`
**Exit code:** 0
**Scenarios: 26 — PASS 26, FAIL 0, SKIP 0**

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/architecture/run.sh`
- Expected: exit 0
- Actual: `scenarios: 1 file(s)`, 26 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: `..........................  [100%]` / `EXECUTED — suite passed`

### Scenario: the suite grew by three, and the three are the F1 fix at the pilot's own bootstrap
- Status: EXECUTED
- Input: set-wise node-ID diff `9d819c1` → `55878c9`
- Expected: a delta that is explained
- Actual: **23 → 26, +3 added, 0 removed**
- Result: PASS
- Evidence:
  ```
  + test_ARCH_05_the_pilots_own_bootstrap_migrates_a_warehouse_it_did_not_write
  + test_ARCH_05_the_certified_query_the_export_refused_on_now_executes
  + test_ARCH_05_a_persisted_warehouse_keeps_the_pilots_deliberate_omission
  ```

### Scenario: ARCH_05 drives the real bootstrap, not a convenient stand-in
- Status: EXECUTED (read as well as run)
- Input: the three scenarios and their `persisted_var_dir` fixture
- Expected: `pilot_transport.seeded_dev_warehouse()` — the exact call
  `backend/pilot.py` makes — rather than `SqliteWarehouse(tmp).seed()`, which the
  rest of the suite already covers and which is structurally blind to a file an
  earlier build left behind
- Actual: they call it. The fixture redirects the default path with
  `CONCLAVE_VAR_DIR` and asserts the redirect took, so the suite cannot write the
  developer's `var/`. The query scenario goes through `POST /ges/query` with a
  real principal and token, so what is asserted is that the export path's
  counterparty is readable — not merely that a column exists.
- Result: PASS
- Evidence: `assert path.startswith(str(tmp_path)), path`;
  `assert warehouse.last_migration is not None`;
  `assert all(row["period_status"] for row in rows)`;
  `with pytest.raises(sqlite3.OperationalError): warehouse.fetch("SELECT COUNT(*) AS n FROM fx_revaluation")`

### Scenario: ARCH_04 — the two-process deployment topology still has an executing witness
- Status: EXECUTED
- Input: `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
- Expected: a real child process on an ephemeral port, a real socket, no `TestClient`
- Actual: passes. Register 19 is unchanged by this pass — narrowed, not closed.
- Result: PASS
- Evidence: included in the 26 passing scenarios; the fixture reaps the child in
  a `finally` and fails loudly rather than skipping if GES does not bind

### Scenario: register 19's residual is still open and still stated
- Status: EXECUTED (read)
- Input: the register, and what the suite can witness
- Expected: no suite claims that an api-process module cannot `import ges.executor`
- Actual: none does. A suite runs in one interpreter with both packages on one
  `sys.path`, so the property is held by the static check and by deployment
  layout, exactly as register 19 records.
- Result: PASS (the limitation is disclosed, not claimed away)
- Evidence: register 19, `PROJECT_CONTEXT.md`
