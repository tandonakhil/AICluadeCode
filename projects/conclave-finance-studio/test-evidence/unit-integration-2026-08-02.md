# Test evidence — unit/integration suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `test-agent` (authored and executed)
**Blocking:** yes (Test Policy: **all suites blocking**, no advisory exception recorded)
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest backend/tests`
**Exit code:** 0
**Scenarios: 2,071 — PASS 2,071, FAIL 0, SKIP 0** (76 scenario files)

The whole tree (`backend/tests` + `tests/suites`) collects **2,736** and passes
in file order in 178.7s, exit 0. The figure above is `backend/tests` alone.

**One failure exists in this pass and it is not in this suite:** the `reverse`
whole-tree ordering failed one **functional**-suite scenario. See
`functional-2026-08-02.md` and `order-independence-2026-08-02.md`.

Both trees were clean at the start and at the end of this pass: `dev` @
`75f5e27`, parent @ `21af9da`, `git status --short` empty on both. Every
mutation below was applied, observed and reverted with `git checkout`, and the
tree was re-checked clean after each.

---

### Scenario: the suite executes and passes in collection order
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest backend/tests -q -p no:cacheprovider`
- Expected: exit 0, every scenario passes, none skipped
- Actual: **2,071 passed, 0 failed, 0 skipped**, exit 0
- Result: PASS
- Evidence: progress-character tally `Counter({'.': 2071})` — no `F`, `E`, `s`
  or `x` anywhere in the run

### Scenario: the whole tree passes together
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest` (testpaths = `backend/tests tests/suites`)
- Expected: 2,736 collected, all pass
- Actual: **2,736 passed**, exit 0, `real 2:58.66` (128s user, 31s system)
- Result: PASS
- Evidence: `Counter({'.': 2736})`

### Scenario: the collected count is what it is claimed to be
- Status: EXECUTED
- Input: `pytest --collect-only -q -o addopts=`, summed per tree
- Expected: 2,736, matching the brief
- Actual: `backend/tests 2071`, `functional 354`, `red-team 61`,
  `architecture 27`, `security 14`, `industry 23`, `ux 186` — **total 2,736**
- Result: PASS
- Evidence: `2736 tests collected in 0.29s`; the seven per-suite figures sum to
  the whole-tree collection exactly, with no residue

### Scenario: the result does not depend on collection order
- Status: EXECUTED
- Input: six orderings under this agent's own plugin (file, seeds 1/7/42/
  20260731, reversed)
- Expected: 2,736 pass in all six
- Actual: **2,736 pass in five; `reverse` gave 2,735 pass + 1 FAIL.** Every
  `backend/tests` scenario passed in all six — the single failure is in the
  **functional** suite
  (`test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`) and is an
  intermittent substring assertion colliding with a rendered timestamp, not an
  order dependence and not a product defect.
- Result: **FAIL** for the tree as a whole; PASS for this suite
- Evidence: `order-independence-2026-08-02.md`, which is the full record and
  the full diagnosis

---

## `AC-F36-33` — the G-RESTATE comparator, verified by mutation

`ges/restatement.py` is new at `a1850a5`. Every claim it rests on was checked
by **breaking it and watching the guard fail**, not by reading it.

### Scenario: the comparator cannot reach the agent runtime (RAI-ARCH-3)
- Status: EXECUTED
- Input: `test_the_comparator_reaches_nothing_in_the_agent_runtime` asserts from
  the **AST** that `ges/restatement.py`'s imports are exactly
  `{__future__, re, typing, common}`. **Mutation:** `from app import
  ges_client` added to the module.
- Expected: the guard fails, naming `app`
- Actual: **FAILED** —
  `AssertionError: assert {...} == {...}` / `Extra items in the left set: 'app'`
- Result: PASS (the guard is load-bearing, not decorative)
- Evidence: `FAILED backend/tests/test_restatement_comparator.py::test_the_comparator_reaches_nothing_in_the_agent_runtime`;
  restored with `git checkout`, tree clean

### Scenario: all three agent write paths fail
- Status: EXECUTED
- Input: constructor (`EmissionRequest(restates_periods=…)`), attribute
  assignment (`request.restates_periods = []`), HTTP body (`POST /ges/emit`
  with the field in `context`), plus the `__slots__ = ()` subclass route
- Expected: each raises `RestatementFieldNotWritable` / returns 403
  `restatement_field_not_agent_writable`; a *clear* is refused too and the
  prior value survives
- Actual: all three refuse; `test_AC_F36_33_clearing_the_field_after_the_comparator_set_it_is_refused`
  additionally asserts `[11]` survived the attempt
- Result: PASS
- Evidence: 32 node IDs in `test_restatement_comparator.py`, all green

### Scenario: each refused write records a control event
- Status: EXECUTED
- Input: **Mutation:** `refuse_agent_write` still raises but the
  `control_events.emit("restatement_field_write_attempt", …)` call is disabled.
- Expected: the constructor, attribute-assignment and HTTP-body scenarios all
  fail — a refusal nobody is told about is not a control
- Actual: **6 FAILED** — `test_AC_F36_33_the_constructor_refuses_a_supplied_restatement_state`,
  `…_the_consecutive_count_too`, `…_attribute_assignment_is_refused[restates_periods]`,
  `[restates_consecutive_periods]`, `…_clearing_the_field_after_the_comparator_set_it_is_refused`,
  `…_the_route_refuses_a_body_that_names_the_field`
- Result: PASS — every path's control event is asserted, not just the first
- Evidence: the six FAILED lines above; `path` is asserted per path
  (`EmissionRequest(**kwargs)`, `attribute assignment`, `POST /ges/emit`)

### Scenario: `/ges/emit` records a narrative only on an ALLOW
- Status: EXECUTED
- Input: **Mutation:** `restatement_comparator.record(...)` moved out of the
  `if decision.allowed:` block so every outcome is recorded.
- Expected: the withheld-emission scenario fails — an agent must not be able to
  seed a narrative history out of an emission it was never permitted to make
- Actual: **FAILED** —
  `test_a_withheld_emission_does_not_become_a_prior_period_narrative`,
  `assert [12] == []`
- Result: PASS
- Evidence: the denied emission became a prior-period narrative under the
  mutation and does not under `75f5e27`

### Scenario: the consecutive count is the comparator's, and an off-by-one fails
- Status: EXECUTED
- Input: **Mutation:** the `consecutive += 1` that counts the emission being
  judged removed from `NarrativeComparator.compare`.
- Expected: the escalation scenario and its boundary both fail
- Actual: **2 FAILED** —
  `test_g_restate_third_consecutive_restatement_escalates_rather_than_denies`
  and `test_g_restate_second_consecutive_restatement_does_not_escalate`
  (`assert 1 == 2`)
- Result: PASS — the count of 3 is now an off-by-one the comparator can fail,
  which it could not be while the scenarios supplied the number themselves
- Evidence: the two FAILED lines above

---

## `AC-F36-30` — the negative-control suite's failing case, verified by mutation

### Scenario: the failing case fails for the missing fixture, not for `AC-F36-24`'s inconclusive
- Status: EXECUTED
- Input: `test_AC_F36_30_an_emission_constraint_missing_a_fixture_is_named_unevidenced_and_the_suite_fails`,
  parametrised over `firing` and `non_firing`. It asserts the suite is **PASS
  before the removal** (a baseline is seeded first), then removes
  `fx/grestate_context.<kind>.json` and asserts `result == FAIL`,
  `result != PASS`, the rule id and `unevidenced` in the detail.
- Expected: the failure is attributable to the missing fixture alone
- Actual: green; and the ordering assertion is real — `run_suite` checks
  `unevidenced` **before** `prior is None`
- Result: PASS
- Evidence: **Mutation:** the inconclusive branch moved ahead of the
  unevidenced branch →
  `FAILED …test_AC_F36_30_a_missing_emission_fixture_fails_the_suite_even_with_no_baseline`,
  `assert 'inconclusive' == 'fail'`

### Scenario: `unevaluable` is not `did_not_fire`
- Status: EXECUTED
- Input: **Mutation:** `UNEVALUABLE = "did_not_fire"`.
- Expected: the scenario that separates them fails — an unreadable fixture that
  looked like a constraint behaving correctly would report green over a control
  never evaluated
- Actual: **FAILED** —
  `test_AC_F36_30_a_missing_emission_fixture_is_not_read_as_the_constraint_holding`,
  `assert 'did_not_fire' != 'did_not_fire'`
- Result: PASS
- Evidence: the FAILED line above

### Scenario: the scenarios are about the LIVE bundle, not a copy that drifted
- Status: EXECUTED
- Input: `test_AC_F36_30_the_copy_the_removal_scenarios_use_is_the_live_bundle`
  asserts `compile_bundle(copy).bundle_hash == bundle.bundle_hash`
- Expected: the copy the removals work on compiles to the bundle in force
- Actual: green; the emission leg is additionally asserted `>= 9` rules, so a
  build where it collapsed to zero could not make the loop vacuously true
- Result: PASS
- Evidence: bundle hash `68f505847f…ece3c`, version `2026.07.31-1`, the same
  hash the pilot served during the smoke test

---

## `PROCESS_STATE_MODULES` was split, not widened

### Scenario: the gateway is guarded *and* deliberately not discarded
- Status: EXECUTED
- Input: `test_the_gateway_is_guarded_without_being_discarded` and
  `test_restoring_does_not_reset_the_externally_restored_modules`
- Expected: `app.ges_gateway` ∈ `EXTERNALLY_RESTORED_MODULES` and ∈
  `GUARDED_MODULES`, ∉ `PROCESS_STATE_MODULES`, and `restore()` leaves
  `ges_gateway._HTTP` identical
- Actual: all four assertions green; the classifier is parametrised over
  `GUARDED_MODULES`, so the gateway's `_HTTP`/`_CLIENTS` are now scanned
- Result: PASS
- Evidence: **Mutation:** `app.ges_gateway` added to `PROCESS_STATE_MODULES` →
  **11 FAILED**, led by
  `test_the_gateway_is_guarded_without_being_discarded`
  (`assert 'app.ges_gateway' not in ('app.ui.state', 'app.pilot_close', 'app.ges_gateway')`)
  and every `test_restore_drops_…` scenario. Moving it into the discarded set
  **cannot** read as a tightening: it fails loudly and would unbind the GES
  application every screen is reached through.

---

## FINDING (non-blocking, not a regression) — `backend/tests` still writes to the developer's live decision ledger

The live-ledger leak I reported last pass is **fixed in `tests/suites`** and is
**still present in `backend/tests`**. This is my own finding, re-verified, and
it is reported rather than fixed.

- Status: EXECUTED
- Input: `stat` on `dev/var/broker_db.sqlite3` before and after each suite's
  entry point, and after `pytest backend/tests`
- Expected (of the fix): 0 bytes of growth
- Actual: `functional 0`, `red-team 0`, `architecture 0`, `security 0`,
  `industry 0`, `ux 0` — and **`unit-integration +32,768 bytes`**
- Result: the suites-tree fix **PASSES**; the unit tree is a **new finding**
- Evidence: traced by measuring `SELECT COUNT(*) FROM decision` around each
  suspect file — **`backend/tests/test_emission_gate.py` adds 17 rows per run**
  to `dev/var/broker_db.sqlite3` (rows stamped `run_id=RUN-TEST-1`,
  `principal_id=agent.omission_detector@1`, `ts=2026-08-02T06:29:…`). Cause is
  the same shape as the one fixed: `backend/tests/conftest.py`'s `ges_app`
  (line 167) and `ges_stack` (line 151) call
  `create_app(lambda: seeded_warehouse)` with **no `broker_factory`**, so they
  fall through to `default_store_path()`. Only `ges_broker_http` (line 299) was
  given a tmp-path broker.
- Why it matters, and why it is not the same bug closing twice: the new
  architecture guard
  (`test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger`) is
  scoped to the **suites'** `ges_http` fixture, so it passes while the unit
  tree keeps appending. That is the "enumeration that reads as complete but is
  not" shape this pass closed twice already.
- Not blocking: no scenario asserts anything about the file's contents, the
  file was deliberately left in place, and nothing observed depends on it.

---

## Test-count delta — against the previous run (`dev` @ `fc197a6`, 2026-08-02)

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 2,028 | **2,071** | **+43** |
| functional | 354 | 354 | — |
| red-team | 61 | 61 | — |
| architecture | 26 | **27** | **+1** |
| security | 14 | 14 | — |
| industry | 23 | 23 | — |
| ux | 186 | 186 | — |
| **total collected** | **2,692** | **2,736** | **+44** |

**Tests added: 44. Tests removed: 0. Tests changed: 7.**

Computed by collecting node IDs at both commits — `fc197a6` via a throwaway
`git worktree`, so nothing was checked out over the tree under test — and
diffing the two sets: `HEAD 2736`, `PREV 2692`, added 44, removed **0**.

The +44 is accounted for exactly, with no residue:

* `backend/tests/test_restatement_comparator.py` — **32 node IDs** (new file,
  `a1850a5`): the comparator, the three write paths, the AST guard, and the
  over-the-wire leg.
* `backend/tests/test_bundle_publication.py` — **7 node IDs** (`faf6117`):
  `AC-F36-30`'s failing case (parametrised both directions), the
  `unevaluable`/`did_not_fire` separation, the no-baseline case, the control
  event, and the live-bundle join.
* `backend/tests/test_pilot_process_state.py` — **4 node IDs** (`4e5ee47`):
  three new functions plus one new parametrisation of
  `test_every_module_level_mutable_binding_is_classified` over
  `app.ges_gateway`.
* `tests/suites/architecture/test_architecture_conformance.py` — **1 node ID**
  (`4e5ee47`): the live-ledger guard.

**Removed: none.** Verified two ways — the node-ID set difference `PREV − HEAD`
is empty, and `git diff fc197a6..HEAD -- backend/tests tests/suites` contains
**zero** removed `def test_` or `class Test` lines and deletes no file.

**Changed: 7, and every one asserts at least as much as before.**

| Changed scenario | Change | Asserts less? |
|---|---|---|
| `test_g_restate_prior_period_treatment_is_context_never_evidence` | state now derived from the real comparator; priors `[9,10,11]` → `[6,7,8]` (non-adjacent, so only the rule under test fires); `assert list(request.restates_periods) == [6, 7, 8]` added | No — `DENY` + reason retained, +1 assertion. The old form supplied no consecutive count either, so no escalation coverage was lost. |
| `test_g_restate_the_same_emission_passes_on_its_own_ground` | same, ALLOW leg | No — `ALLOW` retained, +1 assertion |
| `test_g_restate_third_consecutive_restatement_escalates_rather_than_denies` | count of 3 now **derived**; `assert request.restates_consecutive_periods == 3` added | No — `ESCALATE`, `fsm_path[-1]`, reason and all four control-event assertions retained, +1 |
| `test_g_restate_second_consecutive_restatement_does_not_escalate` | count of 2 now derived; `assert … == 2` added | No — `ALLOW` retained, +1 |
| `test_every_participating_module_declares_the_same_three_things` | iterates `guarded_modules()` instead of `modules()` | No — strictly a superset (3 modules instead of 2) |
| `test_every_module_level_mutable_binding_is_classified` | parametrised over `GUARDED_MODULES` | No — superset; the extra node ID is counted in the +44 |
| `test_the_guard_would_notice_a_new_binding` | +2 assertions naming `ges_gateway`'s `_HTTP`/`_CLIENTS` | No — additions only |

`_denial(broker, emitter, **kwargs)` is a one-line wrapper around
`broker.decide_emission(emission(**kwargs), emitter)`, so the four G-RESTATE
scenarios moving off it lost no setup.

This is a delta against a real previous run, not a baseline.
