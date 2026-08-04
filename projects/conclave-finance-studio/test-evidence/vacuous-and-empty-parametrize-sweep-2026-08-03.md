# Test evidence — vacuous-pass and empty-`parametrize` sweep

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## What changed in this sweep, and why

Every earlier pass ran this sweep **statically** — an AST walk that flagged
loops over dynamic iterables and then hand-reviewed them. Gate 8's Finding A
was precisely a loop that read as a quantifier and ran over one row, and a
static reviewer had passed it four times. It was caught by an **instrumented
probe**, not by reading.

So this pass runs the sweep the way the finding was actually found. Every `for`
loop containing an `assert`, inside every `test_` function, in all 110 test
files, was rewritten by AST transform to record its **iteration count at
runtime**, and the whole tree was executed under that instrumentation in a
throwaway worktree. This is the same class of check as before, sharpened — not
a new class of defect hunt.

- Transform: `scratchpad/instrument.py`; recorder `scratchpad/ta_loops.py`;
  counts `scratchpad/loops.json`
- The instrumented tree **also passed 2,988/2,988** (`2988 passed in 223.10s`),
  which is itself a result: no scenario depends on the byte-level text of its
  own source file, since `ast.unparse` reformatted every one of them

---

### Scenario: no `parametrize` collects zero cases
- Status: EXECUTED
- Input: every `@pytest.mark.parametrize` argvalues expression, static, then
  cross-checked against the collected node ids
- Expected: none empty — an empty argvalues list collects zero cases and reports
  as a pass with pytest saying nothing about it
- Expected count reconciliation: 2,310 + 358 + 194 + 61 + 28 + 23 + 14 = 2,988
- Actual: **NONE empty.** Reconciliation **exact at 2,988**
- Result: PASS
- Evidence: sweep §1 → `NONE`. The build defends this itself as well:
  `test_the_vocabulary_is_the_three_sub_types_and_has_not_silently_emptied`
  exists so the `KIND_VOCABULARY` parametrisation cannot become vacuous, and it
  is one of the three scenarios that fired under mutation B-M2

### Scenario: no loop body in the tree fails to execute
- Status: EXECUTED
- Input: **397 instrumented loops**, min/max iteration counts recorded across a
  full 2,988-scenario run
- Expected: every loop containing an assertion actually iterates
- Actual: **396 of 397 iterate. One has max iterations 0** —
  `backend/tests/test_ui_typography_floor.py::test_no_screen_reachable_from_the_entry_point_carries_a_small_inline_size` L158,
  `[min 0, max 0, entered 47 times]`
- Result: PASS, with the one hit reviewed below and found not to be a defect
- Evidence: `loops.json`, 397 keys

### Scenario: the one zero-iteration loop, read in full
- Status: EXECUTED
- Input: `for value in re.findall(r"font-size:\s*([0-9.]+)px", body)` inside the
  reachable-screen sweep
- Expected: determine whether this is a criterion passing over an empty
  population, or a watchdog correctly finding nothing
- Actual: **a watchdog, not a quantifier.** The population the scenario asserts
  over is the *screens*, and that population is guarded on the line above:
  `urls = sorted(U.reachable_urls()); assert len(urls) > 8, urls`. The outer
  loop entered **47 times**. The inner loop is a search for inline
  `font-size` declarations, of which the build currently emits **zero** — which
  is the passing condition, not an absent population. The type floor itself is
  asserted positively elsewhere in the same file
  (`TestTheDeclaredStylesheet`, which reads `chrome.STYLESHEET` and asserts
  `max(others) <= chrome.MAX_NON_RISK_FONT_PX` and
  `at_top == [".riskband .big"]`)
- Result: PASS — reviewed, not a defect
- Evidence: `test_ui_typography_floor.py:152–159`; the guard is `assert
  len(urls) > 8` and the recorded outer-loop count is 47

### Scenario: loops that quantify over exactly one element
- Status: EXECUTED
- Input: the 17 loops whose maximum observed iteration count is 1 — the exact
  shape of Finding A
- Expected: each is either a genuinely singular object, or is guarded by a
  population assertion
- Actual: **17, all reviewed, none a defect.** Twelve are singular by
  construction (one dossier and its one back-reference; one credential-boundary
  message; one recall-bias label; one probe; one union metric). Three iterate a
  single row of a table whose size is asserted separately. The two worth naming:
  - `test_f36_47_abstention_on_three_surfaces.py::test_every_precision_figure_on_every_reachable_screen_carries_its_count` L255 —
    `[min 0, max 1, entered 94 times]`, i.e. most screens carry no precision
    figure. **This scenario already guards itself**: `assert seen >= 7,
    "expected the readiness screen and six dossiers, saw {}"`. Its own docstring
    states the reason — *"every element of the empty set has property P is the
    shape of a check that keeps passing after the component it was written for
    is removed"*
  - `tests/suites/functional/test_f40_criteria.py::…AC_F40_16…` — no longer in
    this list. It is now `[3, 3]`, which is the fix under test
- Result: PASS
- Evidence: `loops.json`; the 17 keys and their `[min, max, entered]` triples

### Scenario: no test function can pass without being able to fail
- Status: EXECUTED
- Input: functions with no `assert`, no `raise`, no `pytest.raises/warns`, no
  `fail/xfail/skip`
- Expected: any hit must delegate to a helper that itself asserts or raises
- Actual: **13 candidates, the same 13 as the previous pass, all 13 delegate.**
  No new candidate appeared
- Result: PASS — zero vacuous scenarios
- Evidence: sweep §2. The delegation targets are unchanged:
  `ab.assert_no_abstention_control`,
  `credentials.assert_api_process_holds_no_credentials`,
  `p.validate_published_figure`, `R.any_band_is_not_readable`,
  `canonical.content_hash` (refuses floats), `tokens.assert_no_green`,
  `U.fetch` (asserts 200), `cssmatch.compile_selector` (raises),
  `rendered_numbers.band_is_not_readable`

### Scenario: nothing in the tree is skipped or xfailed
- Status: EXECUTED
- Input: `pytest.skip`/`skipif`/`xfail` as calls and as decorators, across all
  110 files
- Expected: zero — a skip is a scenario that did not run
- Actual: **0**
- Result: PASS
- Evidence: sweep §3 → empty; and every run reports `0 skipped`

### Scenario: a suite with zero scenarios would be reported as such
- Status: EXECUTED
- Input: `tests/suites/_runner.sh` exit-code contract, and the six SME suites
- Expected: exit 3 for an empty suite, exit 4 for cannot-execute — never 0
- Actual: all six suites returned **exit 0 with `EXECUTED — suite passed`**;
  none returned 3 or 4, and each printed its own non-zero scenario file count
- Result: PASS
- Evidence: `_runner.sh` lines 26–33 (`NO SCENARIOS DEFINED … exit 3`) and the
  six runner transcripts
