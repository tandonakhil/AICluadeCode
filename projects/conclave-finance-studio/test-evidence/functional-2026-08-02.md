# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `functional-agent` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/functional/run.sh`
**Exit code:** 0
**Scenarios: 354 — PASS 354, FAIL 0, SKIP 0** (19 scenario files)

`test-agent` does not author this suite. It ran it, read its scenario names and
docstrings against the deferred-substitution register, and reports the result.

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0
- Actual: `scenarios: 19 file(s)`, 354 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: progress tally `Counter({'.': 354})`, exit 0

### Scenario: the suite passes under every collection order
- Status: EXECUTED
- Input: the suite as collected inside all six whole-tree orderings
- Expected: no scenario depends on what ran before it
- Actual: green in all six
- Result: PASS
- Evidence: `order-independence-2026-08-02.md`

### Scenario: `AC-F36-29` now causes the ledger rows it reads
- Status: EXECUTED
- Input: `test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_field_not_a_guess`
- Expected: it produces its own action denial and emission denial through the
  two real routes, and asserts more than it did at `55878c9`
- Actual: **+3 assertions, −0**; all prior assertions retained
- Result: PASS
- Evidence: diff analysis in `order-independence-2026-08-02.md` §5

### Scenario: no scenario claims a criterion the register denies
- Status: EXECUTED
- Input: the suite's scenario names and `COVERS` lines
- Expected: `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`
  claimed nowhere
- Actual: claimed nowhere
- Result: PASS
- Evidence: `register-cross-check-2026-08-02.md`

---

## FINDING — this suite writes into the developer's live decision ledger

- Status: EXECUTED
- Actual: `tests/suites/functional/test_emission_gate_criteria.py` adds **3
  rows** per run to `dev/var/broker_db.sqlite3` (row count 4,575 → 4,578),
  because `tests/suites/conftest.py`'s `ges_http` builds `create_app(...)` with
  no `broker_factory` and so falls through to `default_store_path()`.
- Result: **FAIL against the conftest docstring's claim** that "a run never
  writes into the developer's live decision ledger" — reported as a finding.
  **Not blocking**: nothing reads that store order-dependently, and all six
  orderings are green.
- Evidence: full mechanism, per-suite and per-file localisation in
  `order-independence-2026-08-02.md` §6b. This is the only suite of the six
  with a non-zero `var/` delta.

## Test-count delta

354 → 354. **0 added, 0 removed, 1 changed** (`AC-F36-29`, above; it gained
assertions, so the file grew by 41 lines without gaining a node ID).
