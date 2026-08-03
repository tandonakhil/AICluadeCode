# Test evidence — architecture suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Suite owner:** `solution-architect`
**Executed by:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/architecture/run.sh`
**Exit code:** 0
**Scenarios: 28 — PASS 28, FAIL 0, SKIP 0**

Test-count delta against `9d605b1`: **0 added, 0 removed, 0 changed.** The
pass-17 redesign is confined to `app/ui/`; nothing in it touches the
architectural conformance surface.

---

### Scenario: the suite runs at its own entry point
- Status: EXECUTED
- Input: `dev/tests/suites/architecture/run.sh`
- Expected: exit 0
- Actual: exit 0
- Result: PASS
- Evidence: `28 passed in 2.64s`; `EXECUTED — suite passed`

### Scenario: ARCH-04 — the deployment topology is two processes over a socket
- Status: EXECUTED
- Input: the suite's own scenario, which starts `ges/run.py` as a real child
  process on an ephemeral port and drives a broker decision over stdlib HTTP
- Expected: a different pid holds the credential; the api-role test process is
  refused it; the untokened caller gets 401 across the socket
- Actual: passes
- Result: PASS
- Evidence: the one executing witness for register 19; the residual named in
  that entry (no suite can witness that an api-process module cannot
  `import ges.executor`, because a suite runs in one interpreter) is unchanged
  by this pass

### Scenario: register 19's residual is unchanged by the redesign
- Status: EXECUTED
- Input: the UI's import boundary, re-checked after 1,915 lines of new `app/ui/`
- Expected: `app/ui/` still imports nothing from `ges`
- Actual: the two AST-level scenarios still pass
- Result: PASS
- Evidence: `app/ui/graph.py`, `chrome.py`, `routes.py` and the four new object
  pages introduce no `ges` import; the new `test_ui_object_graph.py` resolves
  hrefs through `app.ui.graph`, which is in-package
