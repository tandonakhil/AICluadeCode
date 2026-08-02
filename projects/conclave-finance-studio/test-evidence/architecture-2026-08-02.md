# Test evidence — architecture suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `solution-architect` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/architecture/run.sh`
**Exit code:** 0
**Scenarios: 26 — PASS 26, FAIL 0, SKIP 0** (1 scenario file)

`test-agent` does not author this suite. It ran it and reports the result.

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/architecture/run.sh`
- Expected: exit 0 (the shared runner exits **3** for an empty suite and **4**
  when it cannot execute, so exit 0 means scenarios really ran)
- Actual: 26 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: progress tally `Counter({'.': 26})`, exit 0

### Scenario: the suite passes under every collection order
- Status: EXECUTED
- Input: the suite as collected inside all six whole-tree orderings (file
  order, four uniform global shuffles, reversed)
- Expected: no scenario depends on what ran before it
- Actual: green in all six
- Result: PASS
- Evidence: `order-independence-2026-08-02.md`

### Scenario: the suite leaves the developer's decision ledger untouched
- Status: EXECUTED
- Input: `stat` on `dev/var/broker_db.sqlite3` immediately before and after the
  entry point
- Expected: 0 bytes of growth
- Actual: **0**
- Result: PASS
- Evidence: `architecture EXIT=0 var_delta=0`. Recorded because the `functional`
  suite is **not** clean on this check — see
  `order-independence-2026-08-02.md` §6b.

### Scenario: the two-process topology is witnessed here and nowhere else
- Status: EXECUTED
- Input: `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
- Expected: it executes and passes — it is the only executing witness for
  deferred-substitution register 19, because the pilot and every other suite run
  the in-process transport
- Actual: executed, passed
- Result: PASS
- Evidence: included in the 26 above; register 19 is unchanged by this run.


## Test-count delta

26 → 26. **0 added, 0 removed, 0 changed** since the previous run
(`dev` @ `55878c9`, 2026-07-31).
