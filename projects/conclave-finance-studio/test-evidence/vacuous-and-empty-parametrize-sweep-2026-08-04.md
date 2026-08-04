# Test evidence — vacuous-pass and empty-`parametrize` sweep

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Method — instrumented, not read

Every `for` loop containing an `assert`, inside every `test_` function, in all
**112** test files, was rewritten by AST transform to record its **iteration
count at runtime**, and the whole tree was executed under that instrumentation
in a throwaway detached worktree. This is the shape in which gate 8's Finding A
was actually found; a static reviewer had passed that loop four times.

- Transform: `scratchpad/instrument.py`; recorder `scratchpad/ta_loops.py`;
  counts `scratchpad/loops22.json`
- **426 loops instrumented** (pass 20: 397 — **+29**, all in the new files)
- The instrumented tree **also passed 3,037/3,037** (`3037 passed in 232.42s`),
  which is itself a result: no scenario depends on the byte-level text of its
  own source file, since `ast.unparse` reformatted every one of them

One harness correction: the transform inserted its import at index 0, ahead of
`from __future__ import annotations`, which is a `SyntaxError`. It now inserts
after the module docstring and after any `__future__` import. This was a defect
in the instrumentation, not in the build, and is recorded because the first
attempt produced 112 collection errors that could have been mistaken for one.

---

### Scenario: no `parametrize` collects zero cases
- Status: EXECUTED
- Input: every `@pytest.mark.parametrize` argvalues expression, static, then cross-checked against the collected node ids
- Expected: none empty — an empty argvalues list collects zero cases and reports as a pass with pytest saying nothing about it
- Expected count reconciliation: 2,352 + 365 + 194 + 61 + 28 + 23 + 14 = 3,037
- Actual: **NONE empty.** Reconciliation **exact at 3,037**
- Result: PASS
- Evidence: sweep §1 → `NONE`. The widened parametrisation this pass (`test_the_approval_object_mounts_its_components`, 2 → 4 cases) is visible as four collected node ids, not one

### Scenario: no loop body in the tree fails to execute
- Status: EXECUTED
- Input: **426 instrumented loops**, min/max iteration counts recorded across a full 3,037-scenario run
- Expected: every loop containing an assertion actually iterates
- Actual: **425 of 426 iterate. One has max iterations 0** — `backend/tests/test_ui_typography_floor.py::test_no_screen_reachable_from_the_entry_point_carries_a_small_inline_size` L158, `[min 0, max 0, entered 47 times]`
- Result: PASS, with the one hit reviewed below
- Evidence: `loops22.json`, 426 keys

### Scenario: the one zero-iteration loop, read in full
- Status: EXECUTED
- Input: `for value in re.findall(r"font-size:\s*([0-9.]+)px", body)` inside the reachable-screen sweep
- Expected: determine whether this is a criterion passing over an empty population, or a watchdog correctly finding nothing
- Actual: **a watchdog, not a quantifier** — unchanged from pass 20. The population the scenario asserts over is the *screens*, guarded on the line above by `assert len(urls) > 8`; the outer loop entered **47 times**. The inner loop searches for inline `font-size` declarations, of which the build emits zero — the passing condition, not an absent population. The type floor is asserted positively elsewhere (`TestTheDeclaredStylesheet`)
- Result: PASS — reviewed, not a defect

### Scenario: loops that quantify over exactly one element
- Status: EXECUTED
- Input: the **17** loops whose maximum observed iteration count is 1 — the exact shape of Finding A
- Expected: each is either a genuinely singular object, or is guarded by a population assertion
- Actual: **17, all reviewed, none a defect** — the same population as pass 20 (line numbers shifted where files grew). Twelve are singular by construction (one dossier and its one back-reference; one credential-boundary message; one recall-bias label; one probe; one union metric). Three iterate a single row of a table whose size is asserted separately. The one worth naming again: `test_f36_47_abstention_on_three_surfaces.py::test_every_precision_figure_on_every_reachable_screen_carries_its_count` L255 `[min 0, max 1, entered 94 times]` — most screens carry no precision figure, and the scenario guards itself with `assert seen >= 7`
- Result: PASS
- Evidence: `loops22.json`; the 17 keys and their `[min, max, entered]` triples

### Scenario: the loops added this pass are not vacuous
- Status: EXECUTED
- Input: every instrumented loop in the five files that gained scenarios
- Expected: real, non-trivial populations
- Actual: **all real.** `AC-F41-22`'s traversal iterates **47** URLs and its per-screen loop **14** times; `AC-F41-23`'s four loops iterate 2 / 12 / 21 / 5; `AC-F41-24`'s two iterate 2 / 2; the export scenarios iterate **6 dossiers**; `test_every_evidential_element_of_the_screen_is_in_the_artefact_verbatim` iterates **7** elements (guarded by `assert len(region) >= 6`); `test_every_name_in_the_not_retained_list_is_on_the_screen_with_a_reason` iterates **8**
- Result: PASS
- Evidence: `loops22.json`

### Scenario: no test function can pass without being able to fail
- Status: EXECUTED
- Input: functions with no `assert`, no `raise`, no `pytest.raises/warns`, no `fail/xfail/skip`
- Expected: any hit must delegate to a helper that itself asserts or raises
- Actual: **13 candidates, the same 13 as the previous pass, all 13 delegate.** No new candidate appeared, and **none of the 54 scenarios added this pass is among them** — all 54 carry an `assert` or `pytest.raises`
- Result: PASS — zero vacuous scenarios
- Evidence: sweep §2; delegation targets unchanged (`ab.assert_no_abstention_control`, `credentials.assert_api_process_holds_no_credentials`, `p.validate_published_figure`, `R.any_band_is_not_readable`, `canonical.content_hash`, `tokens.assert_no_green`, `U.fetch`, `cssmatch.compile_selector`, `rendered_numbers.band_is_not_readable`)

### Scenario: nothing in the tree is skipped or xfailed
- Status: EXECUTED
- Input: `pytest.skip`/`skipif`/`xfail` as calls and as decorators, across all 112 files
- Expected: zero — a skip is a scenario that did not run
- Actual: **0**
- Result: PASS
- Evidence: sweep §3 → empty; every run reports `0 skipped`

### Scenario: a suite with zero scenarios would be reported as such
- Status: EXECUTED
- Input: `tests/suites/_runner.sh`'s exit-code contract, and the six SME suites
- Expected: exit 3 for an empty suite, exit 4 for cannot-execute — never 0
- Actual: all six suites returned **exit 0 with `EXECUTED — suite passed`**; none returned 3 or 4
- Result: PASS
