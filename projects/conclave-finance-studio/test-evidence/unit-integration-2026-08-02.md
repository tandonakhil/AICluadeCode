# Test evidence — unit/integration suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest backend/tests -q`
**Exit code:** 0
**Scenarios: 2,108 — PASS 2,108, FAIL 0, SKIP 0**

Both trees were also run together in one pytest session nine times (one control
plus eight orderings): **2,774 passed, exit 0, every time.** See
`order-independence-2026-08-02.md`.

---

### Scenario: the unit tree executes end to end
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest backend/tests -p no:cacheprovider -o addopts= -q`
- Expected: exit 0, no skips
- Actual: `2108 passed in 99.11s`
- Result: PASS
- Evidence: exit code 0; zero `s`/`x`/`F`/`E` in the progress tally

### Scenario: the unit tree no longer grows the developer's live decision ledger
- Status: EXECUTED
- Input: `stat -f%z dev/var/broker_db.sqlite3` immediately before and after the run
- Expected: 0-byte delta — the previous pass's open finding was that
  `backend/tests/conftest.py`'s `ges_app`/`ges_stack` added 17 decision rows and
  32,768 bytes per run
- Actual: `10371072 -> 10371072`, delta **0**, and the file's mtime was unchanged
- Result: PASS
- Evidence: `-rw-r--r-- 10371072 Aug 2 02:30 var/broker_db.sqlite3` before and
  after; the same 0-byte delta held across all nine whole-tree runs

### Scenario: the live-ledger guard refuses CONSTRUCTION over the live path
- Status: EXECUTED
- Input: `backend/tests/test_harness_live_ledger_guard.py` (12 scenarios) plus
  the suites' `tests/suites/architecture` (28), run together
- Expected: 40 pass
- Actual: `40 passed in 3.19s`
- Result: PASS
- Evidence: the guard patches `BrokerStore.__init__` and compares
  `os.path.abspath(str(path))` against `abspath(default_store_path())`, so a
  relative path or a `..` route to the same file is refused by the same rule

### Scenario: MUTATION M3 — the guard's refcounting is load-bearing
- Status: EXECUTED
- Input: `install()`'s early return removed —
  `_HOLDERS += 1; if _ACTIVE is not None: return _ACTIVE` reduced to
  `_HOLDERS += 1`, restoring exactly the defect `code-agent` describes (each
  caller builds a NEW `Guard` and lays a second patch over the first)
- Expected: the two scenarios written to pin this defect fail
- Actual: **3 failures in file order** and **6 under `seed:1`** —
  `test_a_second_holder_gets_the_same_guard_and_lays_no_second_patch`,
  `test_one_holder_letting_go_does_not_disarm_the_guard_for_the_other`,
  `test_a_ges_app_built_with_no_broker_factory_cannot_reach_the_live_ledger`,
  and under the shuffle also
  `test_the_guard_is_installed_for_this_session_over_the_real_path`,
  `test_opening_the_live_ledger_is_refused_and_recorded`, and the suites'
  `test_the_guard_against_the_live_ledger_is_installed_in_this_tree_too`
- Result: PASS (the guard fired; the mutation was reverted)
- Evidence: `3 failed, 2771 passed` in file order; `6 failed, 2768 passed` at
  `seed:1`. **Worth recording: the original defect was invisible in file order
  and this mutation is not** — the two pinning scenarios catch it in any
  ordering, which is a strict improvement on the condition that first exposed
  it. Reverted with `git checkout`; tree re-verified clean at `9d605b1`.

### Scenario: the guard deliberately does NOT patch `default_store_path`, and that reasoning holds
- Status: EXECUTED
- Input: the pass-15 file-size scenario
  (`test_the_suites_ges_app_does_not_write_to_the_live_decision_ledger`) reads
  `live = default_store_path()` and asserts `after == before` on that file's
  size. Simulated both ways with two temp files: an unpatched
  `default_store_path` and a redirected one, with a writer appending to the real
  file in both cases.
- Expected: if `default_store_path` were redirected, the check would pass while
  the real ledger grew — i.e. vacuously
- Actual: unpatched → check returns **False** (catches the write); patched →
  check returns **True** while the stand-in ledger grew 4,096 → 8,192 → 12,288
- Result: PASS — the reasoning holds exactly as `code-agent` states it
- Evidence: `UNPATCHED default_store_path -> check passes? False` /
  `PATCHED default_store_path -> check passes? True  <-- passes VACUOUSLY while
  the real ledger grew`

### Scenario: the guard is not a blanket refusal
- Status: EXECUTED
- Input: `test_a_tmp_path_ledger_is_built_normally`
- Expected: every legitimate tmp-path `BrokerStore` still constructs
- Actual: passes; and the 2,774-scenario tree, which builds these constantly,
  is green
- Result: PASS
- Evidence: a guard that refused all construction would fail thousands of
  scenarios rather than the three the M3 mutation moved

### Scenario: test-count delta against the previous run
- Status: EXECUTED
- Input: node IDs collected at `75f5e27` (in a throwaway `git worktree`, so
  nothing was checked out over the tree under test) and at `9d605b1`, then
  differenced as sets
- Expected: a stated delta, with removals named
- Actual: **2,736 → 2,774. Added 38, removed 0, changed 4.**
- Result: PASS (reported, not a pass/fail condition)
- Evidence: added accounted for exactly with no residue —
  `backend/tests/test_harness_rendered_numbers.py` 25,
  `backend/tests/test_harness_live_ledger_guard.py` 12,
  `tests/suites/architecture/test_architecture_conformance.py` 1. `comm -23`
  over the two sorted node-ID sets returns **empty**: nothing was removed, and
  no test file was deleted.

### Scenario: the 4 changed scenarios, and whether they assert more
- Status: EXECUTED
- Input: `git diff 75f5e27 9d605b1` over the three files holding an
  `AC-F12-15` numeric assertion
- Expected: each retains its prior substantive assertions
- Actual: the four are
  `test_ui_probe_surface.py::test_AC_F12_15_the_reviewer_facing_surfaces_do_not_expose_the_band_as_a_number`,
  `functional/test_f12_probe_criteria.py::test_AC_F12_15_no_api_response_or_header_holds_the_rate`,
  `functional/test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`,
  `ux/test_ux_flow.py::test_UX11_AC_F12_15_the_rate_in_force_is_not_readable_from_the_rendered_product`.
  Every prose ban (`"probe rate"`, `"probe_rate"`, `"injection rate"`), the
  percentage-near-"probe" window regex, the twelve-path sweep and the header
  sweep are all retained. Only the two endpoint substring assertions were
  replaced.
- Result: PASS — with the honest qualification recorded in
  `functional-2026-08-02.md`: the new form is **not a strict superset** of the
  old one, and the difference is measured there rather than asserted.
- Evidence: the diff; `+32/-17` lines across the three files, no assertion
  deleted without a replacement covering it.
