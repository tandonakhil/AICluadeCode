# Test evidence — architecture suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `solution-architect` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/architecture/run.sh`
**Exit code:** 0
**Scenarios: 28 — PASS 28, FAIL 0, SKIP 0** (27 at the previous run; **+1**)

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/architecture/run.sh`
- Expected: exit 0, not exit 3 or 4
- Actual: `scenarios: 1 file(s)`, 28 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: 28 dots, exit 0

### Scenario: the one added scenario — the guard is installed in the suites tree too
- Status: EXECUTED
- Input: the new
  `test_the_guard_against_the_live_ledger_is_installed_in_this_tree_too`,
  which builds a GES app the leaking way (`create_app(...)` with **no**
  `broker_factory`) and drives a real emission through it
- Expected: the request is refused, the refusal is recorded on the guard, and
  the message names `broker_factory`
- Actual: passes — `response.status_code != 200`, `live_ledger_guard.drain()`
  non-empty, `"broker_factory" in refused[0]`
- Result: PASS
- Evidence: this is the difference between "our fixture is wired correctly
  today" (the pass-15 scenario) and "the next fixture written the wrong way
  fails on the day it is written". The first was scoped to one fixture in one
  tree, which is exactly how the identical defect survived its first fix.

### Scenario: the scenario is driven through a real emission, not a fixture inspection
- Status: EXECUTED
- Input: `POST /ges/emit` with a full context, token and principal header
- Expected: the broker is resolved lazily inside the request handler, so only a
  real request reaches it
- Actual: the emission is what triggers construction and therefore the refusal
- Result: PASS
- Evidence: `an app built without a broker_factory and never asked for a
  decision touches nothing at all, which is exactly why most of this tree's
  broker-less apps were never leaking` — the scenario's own reasoning, and it
  is correct

### Scenario: the pass-15 file-size scenario still measures the real file
- Status: EXECUTED
- Input: `test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger`,
  which reads `live = default_store_path()` and compares `os.path.getsize(live)`
  before and after a real emission
- Expected: it measures the developer's actual ledger, not a redirect
- Actual: it does — `default_store_path()` is deliberately left unpatched, and
  the scenario additionally asserts
  `suite_broker.store.path != default_store_path()`
- Result: PASS
- Evidence: proved by simulation that a redirected `default_store_path` would
  make this check pass vacuously while the real ledger grew — see
  `unit-integration-2026-08-02.md`. `code-agent`'s stated reasoning holds.

### Scenario: MUTATION M3 reaches this suite too
- Status: EXECUTED
- Input: the refcount mutation described in `unit-integration-2026-08-02.md`
- Expected: under a shuffle, the suites-tree guard scenario fails as well
- Actual: at `seed:1` the failure set includes
  `tests/suites/architecture/test_architecture_conformance.py::test_the_guard_against_the_live_ledger_is_installed_in_this_tree_too`
- Result: PASS (the guard fired; the mutation was reverted)
- Evidence: `6 failed, 2768 passed` at `seed:1`; 0 failures after revert

### Scenario: the suite's own live-ledger delta
- Status: EXECUTED
- Input: `stat -f%z dev/var/broker_db.sqlite3` around every whole-tree run
- Expected: 0
- Actual: 0 across all nine whole-tree runs
- Result: PASS
- Evidence: `10371072` unchanged, mtime unchanged

### Scenario: register cross-check on this suite's 28 names
- Status: EXECUTED
- Input: all 28 node IDs and every `COVERS` join
- Expected: none of the five declared criteria claimed
- Actual: zero occurrences
- Result: PASS
- Evidence: see `register-cross-check-2026-08-02.md`
