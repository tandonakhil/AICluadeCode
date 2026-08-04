# Test evidence — mutation tests on the two pass-18 fixes

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Method:** every mutation applied in a **detached `git worktree` at `1b1b56e`**,
never in the working tree; reverted with `git checkout --` after each. The
working tree was verified clean at `1b1b56e` before and after. **19 mutations.**

The brief said *verify rather than accept*. Every claim `code-agent` made about
these fixes is restated below as a mutation that ought to break it. A fix whose
mutation still passes is not a fix, it is a description.

---

## Part A — the orphaned-style-rule checker

### Scenario: M1 — an exemption cannot be added without a scenario failing
- Status: EXECUTED
- Input: `NO_EXEMPTIONS = {".brand .ctx": "excused for the demo"}`
- Expected: at least one scenario fails
- Actual: **2 failed** — `test_no_selector_is_excused_from_this_check` and
  `test_the_check_would_have_caught_the_defect_it_was_written_for`
- Result: PASS
- Evidence: `2 failed, 17 passed`

### Scenario: M1b — exempting a selector that is NOT the regression rule
- Status: EXECUTED
- Input: `NO_EXEMPTIONS = {".seal": "cannot be exercised"}` — the shape someone
  would actually reach for, excusing a rule the traversal misses
- Expected: still caught, on the emptiness assertion alone
- Actual: **1 failed** — `test_no_selector_is_excused_from_this_check`
- Result: PASS
- Evidence: `1 failed, 18 passed`. **`NO_EXEMPTIONS` is empty, is passed empty,
  and is asserted empty. There is no exemption lever.**

### Scenario: M2 — the parser RAISES on an at-rule rather than going quiet
- Status: EXECUTED
- Input: `@media (max-width:600px){.lockup{display:none}}` appended to the real
  `chrome.STYLESHEET`, then `cssmatch.orphans(mutated, [], {})`
- Expected: raise, not `[]`
- Actual: **`UnparsedSelector: "the stylesheet has grown an at-rule; this parser
  does not nest. Extend it rather than letting the selector list go quiet."`**
  Also raised for `@import`, `@supports` and `@font-face`. It raises *before*
  matching, so an at-rule cannot produce a partial selector list
- Result: PASS
- Evidence: four at-rule forms, four raises, zero silent `[]`

### Scenario: M3 — the matcher can say NO (mutate `matches_tree` to always yes)
- Status: EXECUTED
- Input: `matches_tree` returns `True` unconditionally
- Expected: the negative scenarios fail
- Actual: **6 failed** — 5 of the 8 matcher scenarios (`descendant_not_sibling`,
  `child_refuses_grandchild`, `multi_class_needs_all`, `tag_qualified`,
  `attribute_value_compared`) plus the `.brand .ctx` regression scenario
- Result: PASS
- Evidence: `6 failed, 13 passed`

### Scenario: M3b — the matcher can say YES (mutate to always no)
- Status: EXECUTED
- Input: `matches_tree` returns `False` unconditionally
- Expected: the positive scenarios fail
- Actual: **9 failed**, including `every_declared_selector_matches_something`
  and `the_context_line_is_styled_at_all`
- Result: PASS
- Evidence: `9 failed, 10 passed`. **Both directions are held. The brief's "nine
  scenarios claim to prove the matcher can say NO" resolves as: 5 negative
  matcher scenarios + 3 parser-refusal scenarios + 1 regression scenario = 9,
  and all nine are mutation-proven below and above.**

### Scenario: M3c — a parser that SWALLOWS what it cannot read
- Status: EXECUTED
- Input: at-rule guard disabled and the sibling-combinator raise replaced by
  `return []`
- Expected: the refusal scenarios fail
- Actual: **2 failed** — `an_at_rule_is_refused_rather_than_half_read`,
  `a_sibling_combinator_is_refused_rather_than_mis_matched`
- Result: PASS
- Evidence: `2 failed, 17 passed`

### Scenario: M3d — the unparsable-compound path
- Status: EXECUTED
- Input (first attempt): replace the `else: raise` in `parse_compound` with
  `index += 1; continue`
- Expected: `test_an_unparsable_compound_raises` fails
- Actual: **19 passed — NOT caught by that mutation alone.** Diagnosis: a
  *second* guard (`if tag is None and not classes and not attrs and not
  universal: raise`) catches it. Removing **both** guards then fails the
  scenario as it should
- Result: PASS (defence in depth, recorded because the single-guard mutation
  survived and a reader is entitled to know why)
- Evidence: both-guards-removed run → `1 failed, 18 passed`

### Scenario: M4 — the traversal genuinely reaches post-POST states
- Status: EXECUTED
- Input: delete `uihelpers.py` step 7b (the three fetches back to
  `/approvals/<id>`, `/proposal/<id>`, `/approvals` after the approval POST)
- Expected: `.seal` and `.card.approved` are reported as orphans
- Actual: **`AssertionError: ... ['.seal', '.card.approved']`**
- Result: PASS
- Evidence: the two rules that "looked dead" are reachable **only** through the
  post-POST re-traversal. `code-agent`'s claim is exact

### Scenario: M5 — `orphans()` returns `[]` unconditionally
- Status: EXECUTED
- Input: `def orphans(...): return []`
- Expected: the regression scenario fails
- Actual: **1 failed** — `the_check_would_have_caught_the_defect_it_was_written_for`
- Result: PASS
- Evidence: `assert [] == ['.brand .ctx']`

### Scenario: M6a — re-introduce the EXACT shipped defect into the real stylesheet
- Status: EXECUTED
- Input: `.lockup .ctx{...}` re-scoped back to `.brand .ctx{...}` in
  `backend/app/ui/chrome.py`
- Expected: reported
- Actual: **2 failed** — the orphan sweep names `.brand .ctx`, and
  `the_context_line_the_defect_was_about_is_styled_at_all` fails
- Result: PASS
- Evidence: **the regression scenario genuinely reports the re-added rule, on
  the real stylesheet and not only on a synthetic string**

### Scenario: M6b — the markup half of the defect (`.ctx` back inside the row)
- Status: EXECUTED
- Input: `.ctx` moved back inside the `.lockup-row` flex container in
  `chrome.lockup()`
- Expected: caught
- Actual: **1 failed** —
  `test_the_context_line_is_a_full_width_line_not_a_flex_column`
- Result: PASS
- Evidence: both halves of the compounding cause are now held by a scenario

## Part B — the alias forgery guard

### Scenario: M7 — my own forged alias row, injected into PRODUCT code
- Status: EXECUTED
- Input: `SCREEN_ALIASES["/refusals"] = "/queue"` added to
  `backend/app/ui/routes.py` — not to any test file
- Expected: refused
- Actual: **1 failed** —
  `test_every_alias_really_serves_ITS_OWN_CANONICAL_SCREEN`:
  *"'/refusals' is declared an alias of '/queue' and serves a DIFFERENT screen.
  An alias row is an assertion that two addresses reach one screen; a row that
  is merely two addresses that both return 200 excuses an orphan."*
- Result: PASS
- Evidence: this is gate 8's M3(d) reproduced independently, from the product
  side rather than by the built self-test

### Scenario: M7b/M7c — the full M3(d), and every dodge I could find
- Status: EXECUTED
- Input: `/refusals` de-linked from BOTH its nav entry and its in-page link,
  then three variants
- Expected: every variant refused
- Actual:
  - de-linked, no alias row → `test_every_route_the_app_serves_is_reachable_from_the_entry_point` FAILS
  - de-linked + **self-alias** `"/refusals": "/refusals"` → `test_every_alias_serves_a_screen_that_is_itself_reachable` FAILS
  - de-linked + forged alias to `/queue` → `test_every_alias_really_serves_ITS_OWN_CANONICAL_SCREEN` FAILS
- Result: PASS
- Evidence: **three independent guards, three different failures, no dodge got
  through.** The self-alias is the one I expected to slip and it does not

## Part C — `AC-F5-02`/`-03`/`-05`, falsifiable in BOTH directions

`code-agent` claims the replacement checks fail *if the gap widens* **and** *if
the ids are reconciled and the disclosure is left behind*. Both claims tested.

### Scenario: D1 — the ids ARE reconciled, disclosure left behind
- Status: EXECUTED
- Input: the four author ids registered as principals in `ges/principals.py`,
  disclosure untouched
- Expected: fail
- Actual: **`test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory` FAILS**
- Result: PASS
- Evidence: `1 failed, 23 passed`. **The claim holds in the direction that
  matters most — a build that quietly closes the gap and keeps the "NOT MET"
  banner is caught**

### Scenario: D2 — the gap WIDENS
- Status: EXECUTED
- Input: `agent.coding-detect` (the one acting agent that IS listed) removed
  from the directory, making the absent set five
- Expected: fail
- Actual: **same scenario FAILS**
- Result: PASS

### Scenario: D3 — the disclosure is removed, gap unchanged
- Status: EXECUTED
- Input: `_acting_agents_absent_from_inventory` returns `[]`
- Expected: fail
- Actual: **FAILS**
- Result: PASS

### Scenario: D4 — the unqualified sentence comes back to `/inventory`
- Status: EXECUTED
- Input: `"An agent that can act is an agent that is listed."` re-inserted into
  the inventory page
- Expected: fail
- Actual: **FAILS**
- Result: PASS

### Scenario: D5 — `LINEAGE_UNTRAVERSED` emptied (lineage declares itself complete)
- Status: EXECUTED
- Input: `untraversed = []` in `ges/main.py:inventory`
- Expected: fail
- Actual: **`test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage` FAILS**
- Result: PASS

### Scenario: D6 — `complete` hard-coded `True` with `untraversed` kept
- Status: EXECUTED
- Input: `"complete": True` replacing `"complete": not untraversed`
- Expected: fail
- Actual: **FAILS** — this is the exact old defect and it is now held
- Result: PASS

### Scenario: D7 — the scope label dropped from the rendered row
- Status: EXECUTED
- Input: `data_scope=` removed from the `lineage-view` element
- Expected: fail
- Actual: **2 failures, one in each tree** — the functional scenario AND
  `test_every_lineage_result_states_its_own_scope_and_completeness`
- Result: PASS

### Scenario: D8 — `data-complete` hard-coded `"true"` in the renderer
- Status: EXECUTED
- Input: `data_complete="true"` unconditionally
- Expected: fail
- Actual: **the functional scenario FAILS.** The unit scenario does NOT — by
  design; its docstring disclaims the `AC-F5-05` claim and asserts only that
  the attribute is one of two values
- Result: PASS (both behaved exactly as their docstrings say they will)

### Scenario: D9 — the dossier index emptied, so the gap "disappears"
- Status: EXECUTED
- Input: `_dossier_index` returns `[]`
- Expected: fail rather than pass on a zero
- Actual: **FAILS** on `assert len(dossiers) >= 7`
- Result: PASS
- Evidence: **a zero over a zero cannot make this scenario green**, which is
  the failure mode that made the old version worthless

---

## Part D — `AC-F5-07` (register 16), the question `code-agent` declined

`code-agent` asked whether `test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements`
— which reads `agents[0]` for two words and never consults the population — has
the same defect as the one just fixed, and did not touch it, calling it a
Plan-gate call. **It is not left as an opinion here; it is measured.**

### Scenario: F7-M — strip Version/Entitlements from every agent row but the first
- Status: EXECUTED
- Input: the inventory renderer relabelled to `"Ver."`/`"Rights"` for every
  agent row after index 0 — so 3 of 4 agent rows no longer carry the two words
  `AC-F5-07` requires
- Expected: something, anywhere in 2,977 scenarios, notices
- Actual: **NOTHING NOTICES. 2,302 passed (unit) + 675 passed (all six SME
  suites) = 2,977 green**, with three quarters of the agent inventory missing
  the fields the criterion names
- Result: **FAIL — the criterion is unheld**
- Evidence: `AC-F5-07` reads *"listing **each** agent, its version and its
  entitlements"*. See `functional-2026-08-03.md` §"Finding 2" for the verdict
  and the distinction from the `AC-F5-02` case. **Not fixed — reported.**
