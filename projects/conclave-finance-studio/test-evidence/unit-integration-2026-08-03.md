# Test evidence — unit / integration

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest -o addopts= -p no:cacheprovider -q backend/tests`
**Exit code:** 0
**Scenarios: 2,281 — PASS 2,281, FAIL 0, SKIP 0**

Whole-tree collection is **2,955**; `backend/tests` is 2,281 of it and the six
SME suite directories are the other 674. 2,281 + 674 = 2,955 exactly, so no
scenario is counted twice and none is uncollected.

## Test-count delta — the baseline is this agent's last verified run

Baseline: `dev` @ `9d605b1`, **2,774** collected — the tree `test-agent` last
verified, not `code-agent`'s pass-16 baseline `b38214d` (2,785). The 11 between
them is `test_ui_typography_floor.py`, added at `b38214d`, which no `test-agent`
run has previously seen.

Computed by differencing **collected node-ID sets** between a throwaway `git
worktree` at `9d605b1` and the tree at `6bf8ed9`.

| | Count |
|---|---|
| baseline (`9d605b1`) | 2,774 |
| current (`6bf8ed9`) | 2,955 |
| **added** | **200** |
| **removed** | **19** |
| net | +181 |

`code-agent` reports "**0 tests deleted**". At node-ID level that is **not
accurate: 19 node IDs no longer exist.** No test *file* was deleted and no
coverage was abandoned, but 19 named scenarios are gone and each one is
accounted for below. The distinction matters because "0 deleted" and "19 renamed
or re-pointed" read the same in a summary and are not the same claim.

### The 19 removed node IDs, each with its successor

| # | Removed | Successor | Verdict |
|---|---|---|---|
| 1 | `test_f26_fidelity::test_AC_F26_10_…_on_the_exceptions_screen` | `…_on_the_run_report` | RENAMED + re-pointed |
| 2 | `test_f26_fidelity::test_the_exceptions_screen_is_reachable…` | `test_the_run_report_is_reachable…` | STRENGTHENED — asserts **both** `/exceptions` and the run report reachable |
| 3 | `test_ui_ask::TestReachability::test_the_entry_point_lands_on_ask` | `test_the_entry_point_lands_on_the_queue_and_ask_is_one_link_away` | STRENGTHENED — 4 assertions where there were 2 |
| 4 | `test_ui_ask_resolver::test_the_ask_screen_is_the_entry_point…` | `test_the_ask_screen_is_reached_from_the_entry_point…` | STRENGTHENED — reachability by traversal added |
| 5 | `test_ui_dossier::…test_every_remaining_link_is_absent…` | `test_the_only_link_is_the_back_reference…` + `test_the_back_reference_is_relative_and_fetches_nothing` | 1 → 2 scenarios; see the conflict note in `functional-2026-08-03.md` |
| 6–8 | `test_ui_exceptions::TestReachability::test_component_is_present…[boundary-check-table\|check-not-run\|recall-bias-label]` | `test_the_moved_module_is_present_on_the_run_it_is_a_property_of[…]` — **6 params, not 3** | STRENGTHENED — `fidelity-region`, `boundary-region`, `coding-region` added |
| 9 | `test_ui_proposal::TestReachability::…[approve-lines]` | `…[proposal-approval-link]` + `test_the_approve_control_is_on_the_approval_screen_and_reachable_from_here` | STRENGTHENED — the control's presence is now asserted **and** its reachability |
| 10 | `test_ui_readiness::test_it_has_a_permanent_place_in_the_navigation` | `test_it_is_reached_from_the_agent_it_is_a_property_of` | **PROPERTY DELIBERATELY REVERSED** — see below |
| 11 | `functional::test_f26_criteria::…exceptions_screen` | `…run_report` | RENAMED + re-pointed |
| 12–13 | `functional::test_f28_criteria::…exceptions_screen` ×2 | `…run_report` ×2 | RENAMED + re-pointed |
| 14–15 | `functional::test_f33_criteria::…exceptions_screen` ×2 | `…run_report` ×2 | RENAMED + re-pointed |
| 16 | `ux::test_ux_journey::…reachable_from_the_exceptions_screen` | `…reachable_from_the_queue` | RENAMED |
| 17 | `ux::test_ux_journey::test_readiness_is_reachable_from_the_navigation_on_every_screen` | `test_every_agent_has_its_own_readiness_address` + `test_readiness_is_reached_from_the_agent_it_is_a_property_of` | **PROPERTY DELIBERATELY REVERSED** — 1 → 2 scenarios |
| 18 | `ux::…test_submitting_the_run_lands_on_the_exceptions_queue` | `…lands_on_the_queue` | RENAMED |
| 19 | `ux::…test_the_entry_point_is_the_ask_screen` | `…test_the_entry_point_is_the_queue_and_ask_is_one_click_from_it` | STRENGTHENED |

**17 of 19 are pure renames or screen re-points.** The two exceptions (#10, #17)
assert a property the approved redesign deliberately reversed: `/readiness` was
a permanent navigation slot hard-bound to one agent, and `UX_KB` A2.2 demotes it
to a property of an agent. Both have replacements asserting the *stronger*
property — that **every** agent has its own linkable readiness address, which
the old build could not satisfy for four of five agents. Recorded as a coverage
decision in front of the human, not folded into a rename.

## The independent check on "no observable-UI criterion was weakened"

Two whole-tree set differences, neither of which depends on reading
`code-agent`'s table.

### Every `data-testid` asserted, before and after

Extracted every id passed to `.has()`, `.one()`, `.all()`, `.inside()`,
`.inside_any()`, `.order_of()` across `backend/tests` and `tests/suites`, at both
commits.

- asserted at `9d605b1`: **133**
- asserted at `6bf8ed9`: **171**
- **asserted before and no longer asserted after: exactly one — `nav-readiness`**

`nav-readiness` is the demoted navigation slot. It appears **nowhere in
`backend/app/` any more**, so no element lost an assertion it still has a
rendering for. Every other observable element the suite asserted before is still
asserted, and 38 new ones were added.

### Every criterion ID, before and after

- AC IDs named by some node ID: **175 at `9d605b1`, 175 at `6bf8ed9`** —
  set-identical, zero lost, zero gained
- `COVERS AC-…` joins: **103 at `9d605b1`, 103 at `6bf8ed9`** — set-identical

**No criterion lost its named scenario and no criterion lost its `COVERS`
join.** Combined with the testid delta above, `code-agent`'s claim that no
observable-UI criterion's check was weakened holds under independent
measurement.

---

### Scenario: whole-tree control run, file order
- Status: EXECUTED
- Input: `.venv/bin/python -m pytest -o addopts= -p no:cacheprovider -q`
- Expected: 2,955 collected, all pass, exit 0
- Actual: **2,955 passed in 209.38s**, exit 0
- Result: PASS
- Evidence: `2955 passed in 209.38s (0:03:29)`; `dev/var/broker_db.sqlite3`
  byte-identical before and after (10,559,488 bytes, mtime unchanged)

### Scenario: `backend/tests` alone, at its own entry point
- Status: EXECUTED
- Input: `pytest -o addopts= -p no:cacheprovider -q backend/tests`
- Expected: exit 0
- Actual: **2,281 passed in 125.70s**, exit 0
- Result: PASS
- Evidence: `2281 passed in 125.70s (0:02:05)`

### Scenario: the per-suite collections sum to the whole-tree collection
- Status: EXECUTED
- Input: node-ID collection, partitioned by directory
- Expected: unit + six suites = whole tree, exactly
- Actual: 2,281 + 354 + 28 + 14 + 61 + 23 + 194 = **2,955**
- Result: PASS
- Evidence: whole-tree `--collect-only` returns 2,955 node IDs

### Scenario: the live-ledger guard holds across every run
- Status: EXECUTED
- Input: md5 and size of `dev/var/broker_db.sqlite3` before and after each of
  the eight whole-tree runs
- Expected: byte-identical every time — no test writes the developer's ledger
- Actual: **identical on all eight**
- Result: PASS
- Evidence: `ledger_same=yes` on all six ordering runs; 10,559,488 bytes with
  mtime `Aug 3 15:51` unchanged through the control run and the vacuous-pass run

### Scenario: empty-`parametrize` sweep
- Status: EXECUTED
- Input: AST walk over every `test_*.py` in both trees, looking for
  `@pytest.mark.parametrize` whose argvalues is an empty list, tuple, set or dict
- Expected: zero — a `parametrize` over an empty sequence collects zero tests and
  reports green
- Actual: **0 sites**
- Result: PASS
- Evidence: `empty parametrize sites: 0` over 99 test modules

### Scenario: vacuous-pass sweep, executed rather than inferred
- Status: EXECUTED
- Input: a whole-tree run under an out-of-tree plugin that wraps
  `uihelpers.Document.all` and `.tags`, recording every call that returned an
  EMPTY result, per scenario, alongside that scenario's outcome
- Expected: no scenario passes having checked nothing
- Actual: **484 scenarios make document queries; 15 passed with every query
  empty; all 15 are negative-assertion scenarios where the empty result IS the
  claim** ("there is no approve control on the queue", "there is no
  `<select>`", "the three analytical regions are gone from the queue")
- Result: PASS
- Evidence: the three IA-relevant ones each have a positive counterpart on the
  other screen — `test_the_queue_is_no_longer_the_union_of_every_criterion_that_named_it`
  asserts `fidelity-region`/`boundary-region`/`coding-region` ABSENT from
  `/exceptions` while `test_the_moved_module_is_present_on_the_run_it_is_a_property_of`
  asserts the same three PRESENT on the run report, so neither can pass on a
  page that failed to render. Full record: `scratchpad/vacuous.json`,
  2,955 passed in 209.50s under the instrumentation
