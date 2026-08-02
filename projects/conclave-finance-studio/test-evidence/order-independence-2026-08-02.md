# Test evidence — order independence (the gate-stopping condition)

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02 (run began 2026-08-01, crossed midnight mid-suite)
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

This file is the verification of the one condition that stopped gate 8 at the
previous pass. It is deliberately separate from the per-suite files: the
per-suite files answer "did the suite pass", this one answers "did it pass for
a reason that survives the collection order".

---

## 1. The plugin is mine, and it is a different generator

`code-agent` flagged the gap it could not close itself: its interleave plugin
is not `test-agent`'s, and the two measured different failure sets at
`55878c9` (it measured 0/1/2/1 where this agent measured 2/1/1/0). A verifier
that reuses the builder's permutations is not verifying, so this run used its
own.

Both plugins were read side by side (`code-agent`'s was still on disk in the
shared scratchpad):

| | `code-agent`'s | `test-agent`'s |
|---|---|---|
| Algorithm | **round-robin across shuffled buckets** — group by file, shuffle the file list, shuffle within each file, then emit one item per file per cycle | **uniform global Fisher–Yates** over all 2,692 items, no bucketing at all |
| Structure preserved | each file contributes exactly one item per cycle | none |
| Env var | `CONCLAVE_INTERLEAVE_SEED` | `TA_ORDER` |

These are different *classes* of permutation, not the same class at different
seeds — which is a stronger answer than the brief asked for.

**Measured proof they differ**: under a strict round-robin, two adjacent items
can never come from the same file while more than one bucket is non-empty. In
this agent's realised seed-1 order, **39 adjacent pairs come from the same
file**. That order is structurally unreachable by `code-agent`'s generator.

The realised order for every run was written to disk and fingerprinted, so the
permutation used is evidence rather than a claim:

| Ordering | SHA-1 of the realised node-id list (first 16) |
|---|---|
| `seed:1` | `b31c9d98856be496` |
| `seed:7` | `3f744be61621fdc0` |
| `seed:42` | `546d6faf3545cf2c` |
| `seed:20260731` | `2b0624f1c8bba047` |
| `reverse` | `1694d285798347f9` |

All five distinct.

The plugin lives outside the repository (in the session scratchpad, loaded via
`PYTHONPATH` and `-p ta_interleave`) so that the tree under test stayed clean
at `fc197a6` throughout. Verified: `git status --porcelain` empty at the start
and end of this run.

---

### Scenario: the whole tree passes in file order (control)
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest` (no plugin), `dev/` @ `fc197a6`
- Expected: 2,692 collected, all pass, exit 0
- Actual: **2,692 passed, 0 failed, 0 skipped**, exit 0, **194.8s** wall
- Result: PASS
- Evidence: progress-character tally over the whole run — `Counter({'.': 2692})`,
  no `F`, `E`, `s` or `x`. Wall time from `/usr/bin/time -p`: `real 194.82`.

### Scenario: uniform global shuffle, seed 1
- Status: EXECUTED
- Input: `TA_ORDER=seed:1 pytest -p ta_interleave`
- Expected: 2,692 pass, exit 0
- Actual: `2692 passed in 193.66s`, exit 0
- Result: PASS
- Evidence: `seed:1 EXIT=0 WALL=200s`; order fingerprint `b31c9d98856be496`

### Scenario: uniform global shuffle, seed 7
- Status: EXECUTED
- Input: `TA_ORDER=seed:7 pytest -p ta_interleave`
- Expected: 2,692 pass, exit 0
- Actual: `2692 passed in 202.42s`, exit 0
- Result: PASS
- Evidence: `seed:7 EXIT=0 WALL=207s`; fingerprint `3f744be61621fdc0`

### Scenario: uniform global shuffle, seed 42
- Status: EXECUTED
- Input: `TA_ORDER=seed:42 pytest -p ta_interleave`
- Expected: 2,692 pass, exit 0
- Actual: `2692 passed in 203.76s`, exit 0
- Result: PASS
- Evidence: `seed:42 EXIT=0 WALL=212s`; fingerprint `546d6faf3545cf2c`

### Scenario: uniform global shuffle, seed 20260731
- Status: EXECUTED
- Input: `TA_ORDER=seed:20260731 pytest -p ta_interleave`
- Expected: 2,692 pass, exit 0
- Actual: `2692 passed in 199.02s`, exit 0
- Result: PASS
- Evidence: `seed:20260731 EXIT=0 WALL=209s`; fingerprint `2b0624f1c8bba047`

### Scenario: reversed collection order
- Status: EXECUTED
- Input: `TA_ORDER=reverse pytest -p ta_interleave`
- Expected: 2,692 pass, exit 0
- Actual: `2692 passed in 178.66s`, exit 0
- Result: PASS
- Evidence: `reverse EXIT=0 WALL=186s`; fingerprint `1694d285798347f9`

**Six orderings, six clean runs, 2,692 every time.** At `55878c9` the same
tree produced four different failure sets under four seeds. The gate-stopping
condition is closed.

---

## 2. Runtime: the trade is real and is not a hang

Recorded so nobody reads a long run as a stall. `code-agent` reported
56.1s → 168.7s in file order; this agent measured **194.8s** in file order and
**178.7–203.8s** interleaved, on a machine also doing other work. Same order of
magnitude, ~3×, consistent with a per-scenario GES rebuild plus close discard
at setup and teardown. Nothing here indicates a hang.

Note the previously reported 171–278s interleaved band came from
`code-agent`'s round-robin generator. A uniform global shuffle — which forces
far more module-scoped fixture teardown/rebuild — landed in a *narrower* band
(178–204s), so the widest interleaved times were not caused by the depth of
the interleave.

---

## 3. `code-agent`'s correction of this agent's diagnosis — CONFIRMED, both causes

This agent previously named the control-event sink. `code-agent` corrected it
to two different causes. Both were checked, and the correction is right; the
control-event sink was **not** the cause.

### Cause A — the snapshot was function-scoped and therefore taken too late

The claim: pytest builds higher-scoped fixtures before function-scoped ones, so
a module-scoped fixture that walks every screen follows the real
`/ask?tier=exploration` link and pollutes the process *before* the
function-scoped snapshot reads its "before" value; the restore then puts the
pollution faithfully back, permanently.

**The fixture the claim describes exists, and was located**:
`backend/tests/test_f36_47_abstention_on_three_surfaces.py:86` —

```python
@pytest.fixture(scope="module")
def surfaces():
    """Every screen reachable from `/` by following real links, parsed."""
    for url in sorted(U.reachable_urls()):
```

`U.reachable_urls()` traverses from `/` following real hrefs and form actions,
which reaches the exploration-tier link. It is the only module-scoped fixture
in the tree that traverses; the other six module-scoped fixtures fetch a single
named screen.

#### Scenario: the setup-side half of the restore is load-bearing
- Status: EXECUTED
- Input: a throwaway probe module reproducing the shape — a module-scoped
  fixture calling `U.reachable_urls()`, and a test asserting the process is
  **not** in the exploration tier when the body starts — run twice: once
  against `fc197a6` unmodified, once with the setup-side
  `pilot_test_binding.restore()` removed from `backend/tests/conftest.py` so
  only the teardown-side call remained.
- Expected: passes unmodified; fails with the setup-side call removed. If it
  passed both ways, the setup-side half would be decoration and cause A's
  timing argument would be unsupported.
- Actual: **unmodified — 2 passed**. **Teardown-only — 1 failed, 1 passed**,
  the failure being exactly the tier assertion.
- Result: **PASS — cause A confirmed**
- Evidence: `AssertionError: the module-scoped traversal left the process in
  the exploration tier and the function-scoped restore did not clean it before
  the body ran`. The probe's own negative control
  (`test_the_traversal_really_does_select_the_tier`) passed in **both** runs,
  so the probe was not passing by failing to reach the link. The probe file was
  deleted and the mutation reverted; `git status --porcelain` empty afterwards.

#### Scenario: how much the setup-side half is currently exercised
- Status: EXECUTED
- Input: the **whole tree** under `TA_ORDER=seed:1` with the setup-side restore
  removed from both conftests
- Expected: unknown — this was run to find out
- Actual: **2,692 passed in 151.64s**, exit 0
- Result: PASS (reported as a **finding**, not as a defect)
- Evidence: no scenario in the current tree, at this permutation, depends on
  the setup-side call. The window it protects is narrow — only the first
  scenario within a polluting higher-scoped fixture's scope — and no assertion
  currently falls inside it. So the setup-side half is correct, cheap and
  justified by the probe above, but it is **insurance rather than a currently
  failing case**. Recorded so a future reader does not mistake "it passed with
  the guard removed" for "the guard was unnecessary": the probe shows it
  changes what a scenario observes.

### Cause B — two session fixtures each bound a transport, last-one-wins

#### Scenario: the two independent bindings existed at `55878c9`
- Status: EXECUTED
- Input: `git show 55878c9:backend/tests/conftest.py` and
  `git show 55878c9:tests/suites/conftest.py`
- Expected: two `scope="session", autouse=True` fixtures, each constructing its
  own `BrokerStore` and each calling `pilot_transport.install(...)`
- Actual: exactly that —
  `backend/tests/conftest.py:312 @pytest.fixture(scope="session", autouse=True)`
  → `:335 BrokerStore(str(directory / "broker_db.sqlite3"))` → `:364
  pilot_transport.install(ges_app=app)`; and
  `tests/suites/conftest.py:112` → `:158 BrokerStore(...)` → `:168
  pilot_transport.install(...)`
- Result: **PASS — cause B confirmed**
- Evidence: binding is last-one-wins, so which store the application recorded
  into was decided by which tree's first scenario ran first. At `fc197a6` both
  fixtures instead call `pilot_test_binding.bind()`, which is idempotent and
  returns the first caller's store through a `_StoreProxy`.

---

## 4. The AST guard is a classification — MUTATION-TESTED

The brief required this to be mutation-tested rather than read. It was, twice,
because a classifier that only recognised `{}` would wave through the shape a
real new holder actually takes (`_X = None`, built lazily).

### Scenario: an undeclared module-level dict fails the guard
- Status: EXECUTED
- Input: appended `_TA_MUTATION_CACHE = {}` to `backend/app/ui/state.py`, then
  `pytest backend/tests/test_pilot_process_state.py`
- Expected: the guard fails and NAMES the binding
- Actual: **2 failed, 15 passed**
- Result: PASS
- Evidence: `AssertionError: these module-level bindings in app.ui.state could
  accumulate state across scenarios and are in neither PROCESS_STATE_HOLDERS
  nor FROZEN_MODULE_TABLES: ['_TA_MUTATION_CACHE']`. The guard's own negative
  control (`test_the_guard_would_notice_a_new_binding`) failed alongside it, as
  designed.

### Scenario: an undeclared lazily-built holder fails the guard too
- Status: EXECUTED
- Input: appended `_TA_LAZY_HOLDER = None` to `backend/app/pilot_close.py` (the
  *other* participating module, and the shape every existing holder uses), then
  the same run
- Expected: the guard fails and names it
- Actual: **2 failed, 15 passed**
- Result: PASS
- Evidence: `... in app.pilot_close ... : ['_TA_LAZY_HOLDER']` and
  `assert {'_CACHE', '_TA_LAZY_HOLDER'} == {'_CACHE'}`
- Both mutations were reverted with `git checkout`; tree verified clean at
  `fc197a6` after each.

**Conclusion:** the guard is a real classification over the AST of every
participating module, not an enumeration of known mutations, and it fires on
both shapes in both participating modules.

**One scope limit, recorded (not blocking):** the guard classifies bindings
*within* `PROCESS_STATE_MODULES`, but the **set of participating modules is
itself an enumeration** (`("app.ui.state", "app.pilot_close")`). A holder added
to a third module is invisible to it. `test_nothing_hangs_pilot_close_state_off_
a_module_that_does_not_participate` partially covers this by asserting the
stores hang off the discarded `PilotState`, but it does not scan other modules.
See §6.

---

## 5. `AC-F36-29` asserts MORE, not less — CONFIRMED

### Scenario: the strengthened scenario
- Status: EXECUTED
- Input: `git diff 55878c9..fc197a6 -- tests/suites/functional/test_emission_gate_criteria.py`
- Expected: it now causes the rows it reads, and no existing assertion was
  dropped
- Actual: confirmed. **Every prior assertion is retained** (`assert rows`,
  `subject` subset of `{action, emission}`, `"emission" in subjects`) and the
  scenario gained:
  - a new call to `_an_action_denial_and_an_emission_denial()`, which itself
    asserts `not action.allowed` and `not emission.admitted` — two assertions
    that did not exist before;
  - a new final `assert "action" in {r["subject"] for r in rows}`.
- Result: **PASS — +3 assertions, −0**
- Evidence: the diff is purely additive on this scenario (`+` lines only inside
  the test body; no `-` line touches an assertion). Previously it read the
  ledger as it found it, so it was really asserting that the scenario collected
  before it had run first; it now produces both denials through the two real
  routes (`ges_gateway.client_for(...).decide(...)` and `.emit(...)`).

---

## 6. Carried, unfixed, NOT blocking

### 6a. `ges_gateway._HTTP` restored by named snapshot — carried, with a correction to the count

`code-agent` named this as the next one that will bite, in "three
function-scoped fixtures". That is right about the fixtures and **undercounts
the sites**: there are **six** occurrences of the `previous = ges_gateway._HTTP`
… `ges_gateway.reset(previous)` pattern.

| Site | Form | Scope |
|---|---|---|
| `backend/tests/test_cuec_export_probe.py:200` (`swapped_transport`) | fixture | function |
| `tests/suites/functional/test_f40_criteria.py:621` (`transport_without_an_attestation`) | fixture | function |
| `tests/suites/functional/test_f40_criteria.py:736` (`poar_world`) | fixture | function |
| `backend/tests/test_ui_governance_screens.py:325` | inline `try/finally` in a test body | function |
| `backend/tests/test_ui_write_path.py:476` | inline `try/finally` in a test body | function |
| `tests/suites/ux/test_ux_accessibility.py:293` | inline `try/finally` in a test body | function |

All six are function-scoped, so all six are **correct today** for exactly the
reason `code-agent` gives. The three inline ones are marginally safer still
(the snapshot and the restore are in one function body). Recorded, not
blocking. The failure mode is the same one cause A describes: it becomes wrong
the day any of these moves to module or session scope, and it will fail
silently as an unrelated screen rendering an outage.

Note also that `app.ges_gateway` holds two module-level mutable bindings
(`_HTTP = None`, `_CLIENTS: Dict[str, GesClient] = {}`) and is **not** in
`PROCESS_STATE_MODULES`, so §4's guard does not see them. That is the same
enumeration limit noted above.

### 6b. NEW, found this run: the test suite writes into the developer's live decision ledger

Not previously recorded, same class as 6a, **not blocking**.

- Status: EXECUTED
- Input: `stat` + a row count on `dev/var/broker_db.sqlite3` before and after
  `pytest tests/suites/functional/test_emission_gate_criteria.py`
- Expected (per the conftest docstrings, which state the broker "points at a
  session tmp path so a run never writes into the developer's live decision
  ledger"): no change
- Actual: **the file grows and gains rows**. `decision` row count **4,575 →
  4,578** (+3) for one run of one file; file size +8,192 bytes. The file
  currently holds **4,578 accumulated rows / 9.3 MB**.
- Result: **FAIL against the docstring's claim** — reported as a finding, not
  as a suite failure
- Evidence: measured per suite, the write is localised to exactly one suite and
  one file — `functional` (`var_delta=4096`), all five other suites
  `var_delta=0`; within `functional`, `test_emission_gate_criteria.py`
  (`delta=8192`), the two other `ges_http` users `delta=0`.

**Mechanism**: `tests/suites/conftest.py`'s `ges_http` fixture calls
`create_app(lambda: seeded_warehouse)` with **no `broker_factory`**, so
`ges/main.py:default_broker_factory()` resolves
`ges/broker/store.py:default_store_path()` = `var/broker_db.sqlite3`. The
warehouse is injected; the broker store is not.

**Why it is not blocking**: nothing currently reads that store in an
order-dependent way — every scenario that reads a ledger reads
`ges_transport.decisions()`, which is the `_StoreProxy` onto the rebuilt
tmp-path store. All six orderings are green.

**Why it should still be recorded**: this store sits *outside* the rebuild
mechanism entirely — it is neither tmp-pathed, nor rebuilt between scenarios,
nor discarded by `restore()`. It accumulates across scenarios, across runs, and
it is **the same file `backend/pilot.py` uses**, so a smoke-test pilot run and a
pytest run share one ledger. A fresh clone (empty `var/`) and this machine
(4,578 rows) are therefore different starting states for any future scenario
that counts rows there. `_broker_cache` in `create_app` was checked and is
correctly closure-local, so the defect is only the missing injection.
