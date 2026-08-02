# Test evidence — architecture conformance suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `solution-architect` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/architecture/run.sh`
**Exit code:** 0
**Scenarios: 27 — PASS 27, FAIL 0, SKIP 0** (1 scenario file)

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/architecture/run.sh`
- Expected: exit 0
- Actual: `scenarios: 1 file(s)`, 27 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: progress tally `Counter({'.': 27})`, exit 0

### Scenario: the new live-ledger guard fails with the fix reverted
- Status: EXECUTED
- Input: **Mutation.** `tests/suites/conftest.py`'s `ges_http` restored to
  `create_app(lambda: seeded_warehouse)` — i.e. the `broker_factory=lambda:
  suite_broker` argument removed — then
  `test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger` run.
- Expected: the guard fails, and fails on the right thing
- Actual: **FAILED** —
  `AssertionError: the app under test is not using the suite's broker` /
  `assert None is not None`, and the mutated run grew
  `dev/var/broker_db.sqlite3` by **4,096 bytes**, which is the defect itself
  reappearing on cue
- Result: PASS — this is `test-agent`'s own finding from the previous pass,
  re-verified rather than accepted on report
- Evidence: the FAILED line above plus `ledger delta under mutation = 4096`;
  `git checkout` restored the file and the tree was re-checked clean

### Scenario: the guard is driven by a real emission, not by inspecting a fixture
- Status: EXECUTED
- Input: reading the scenario — it `POST`s `/ges/emit` through `ges_http`,
  reads the returned `decision_id` back out of `suite_broker.store`, asserts
  `suite_broker.store.path != default_store_path()`, and asserts the live
  file's byte size is identical before and after
- Expected: the check is on where a request's decision actually landed, since
  the leak was a request handler resolving a default
- Actual: exactly that; `None` before and after is accepted as the correct
  state on a fresh clone where the file does not exist
- Result: PASS
- Evidence: `tests/suites/architecture/test_architecture_conformance.py`
  lines 686–744

### Scenario: no suite run touches the live ledger
- Status: EXECUTED
- Input: `stat` on `dev/var/broker_db.sqlite3` around each of the six suite
  entry points
- Expected: 0 bytes of growth for every suite
- Actual: `functional 0`, `red-team 0`, `architecture 0`, `security 0`,
  `industry 0`, `ux 0`
- Result: PASS
- Evidence: the per-suite deltas above. **The unit tree is a separate finding**
  — `pytest backend/tests` still grows the file by 32,768 bytes; see
  `unit-integration-2026-08-02.md`. That is reported, not fixed, and this
  suite's guard does not cover it because it is scoped to the suites' fixture.

### Scenario: the comparator is outside the agent runtime (RAI-ARCH-3)
- Status: EXECUTED
- Input: `ges/restatement.py` lives in the GES plane, is wired into
  `/ges/emit`, and is asserted from the AST to import nothing from `app.`
- Expected: the thing being measured cannot reach the measurement
- Actual: green, and **mutation-verified** — adding `from app import
  ges_client` fails the guard naming `app`
- Result: PASS
- Evidence: `unit-integration-2026-08-02.md`, first mutation

### Scenario: the suite passes under every collection order
- Status: EXECUTED
- Input: all six whole-tree orderings
- Expected: green in all six
- Actual: green in all six — every scenario of this suite passed in every
  ordering. The single failure of this pass, in the `reverse` ordering, is in
  the **functional** suite, not this one.
- Result: PASS
- Evidence: `order-independence-2026-08-02.md`

---

## Test-count delta

| | Before (`fc197a6`) | After (`75f5e27`) | Delta |
|---|---|---|---|
| architecture | 26 | **27** | **+1** |

**Added 1, removed 0, changed 0.** The one addition is
`test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger`
(`4e5ee47`). Node-ID set difference confirms no removal.
