# Test evidence — the changed-scenario audit (brief item 1)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED` (read scenario by scenario against the diff, then
confirmed by mutation where a claim was checkable that way)

The brief's single most important question: **did any observable-UI criterion's
check get weakened to fit the new layout?** `code-agent` tabulates eight changed
groups in `PROJECT_CONTEXT.md` and asserts none is a weakening. Each row was
verified against `git diff 9d605b1..6bf8ed9` rather than against the table.

**Verdict: no weakening found in any of the eight. Two are recorded as
conflicts rather than resolutions (see `functional-2026-08-03.md`), and one
prose/assertion mismatch is noted.**

---

### Scenario: row 1 — `test_ui_dossier`, "no links at all" → "exactly one link"
- Input: `git diff` of `backend/tests/test_ui_dossier.py`
- Expected: the fetch-nothing substance is a separate scenario and is untouched
- Actual: `test_there_is_no_external_reference_of_any_kind` — which bans
  `<link`, `<img`, `<script`, `@import`, `url(`, `srcset` — **does not appear in
  the diff at all.** Untouched. The changed scenario became **two** scenarios,
  and the new one adds a relative/same-origin check that did not exist.
- Result: PASS (not a weakening)
- Evidence: the diff shows `-1/+35` on the file: one assertion removed, two
  scenarios added. Independently confirmed in a real browser — see R1 in
  `rendered-ui-2026-08-03.md`: the served dossier saved to disk and opened as
  `file://` issued **zero** requests off `file://`, rendered still styled
  (`risk-band` background `rgb(246, 228, 227)`), and carried exactly one inert
  anchor.

### Scenario: row 2 — F26/F28/F33 re-pointed from `/exceptions` to the run report
- Input: `git diff` of `test_f26_fidelity.py`, `test_ui_exceptions.py`,
  `functional/test_f26_criteria.py`, `test_f28_criteria.py`, `test_f33_criteria.py`
- Expected: every element that moved screens is still asserted visible, in the
  same state, on its new screen; reachability of the new screen asserted too
- Actual: every assertion body is character-identical apart from the fixture it
  reads (`screen` → `run_report`). The parametrised reachability list went from
  **3 ids to 6** (adds `fidelity-region`, `boundary-region`, `coding-region`).
  A new scenario `test_the_queue_is_no_longer_the_union_of_every_criterion_that_named_it`
  asserts the three are ABSENT from the queue, so the move is checked from both
  ends. `test_the_run_report_is_reachable_from_the_entry_point_by_following_links`
  asserts the traversal.
- Result: PASS (strengthened)
- Evidence: `test_the_exceptions_screen_is_reachable_from_the_entry_point` became
  `test_the_run_report_is_reachable_from_the_entry_point` and asserts **both**
  `assert "/exceptions" in reachable` **and** `assert U.RUN_REPORT in reachable`
  — strictly more than before

### Scenario: row 3 — `test_ui_proposal`, approve-control scenarios re-pointed
- Input: `git diff` of `backend/tests/test_ui_proposal.py`
- Expected: `AC-F40-11`'s lines-before-control ordering and both supersession
  removals moved with the control, none relaxed
- Actual: `test_the_lines_precede_the_approve_control_in_reading_order` now reads
  the approval screen, and the approval screen renders the lines too. Both
  supersession scenarios gained assertions rather than moving:
  `?superseded=1` now asserts `not approval_screen.has("approve-lines")` AND
  `approval_screen.has("approval-blocked-by-run")` **in addition to** the two
  original assertions on the proposal screen. `AC-F41-15`'s no-movement case now
  pins **two** screens' markup byte-for-byte where it pinned one.
- Result: PASS (strengthened)
- Evidence: net `+53/-…` on the file with every original assertion retained;
  `AC-F41-14` gained `approval-blocked-by-data`

### Scenario: row 4 — "`/` renders Ask" → "`/` links to Ask, one click away"
- Input: `git diff` of `test_ui_ask.py`, `test_ui_ask_resolver.py`, `test_ux_journey.py`
- Expected: "reached by following a link" is a stronger claim than "the browser
  landed on it"
- Actual: `test_the_entry_point_lands_on_ask` had 2 assertions; its successor has
  5 — the entry point renders the queue, carries no `nl-input`, links `/ask`,
  and `/ask` still carries `nl-input` and `aria-current="page"`. The resolver
  scenario added `assert "/ask" in U.reachable_urls()`, which is a traversal
  claim the old form did not make.
- Result: PASS (strengthened)
- Evidence: confirmed over HTTP against the served pilot — smoke S4

### Scenario: row 5 — `review-queue` → `exception-queue`
- Input: `git diff` of `test_ui_probe_surface.py`, `test_f12_probe_criteria.py`, `test_ux_flow.py`
- Expected: the parallel `<ul>` was removed by the merge; the ordering and
  row-shape claims survive against the list that remains
- Actual: the merged queue carries **6 rows** where the review queue carried
  fewer, so the row-shape and ordering claims are asserted over a strictly larger
  population. New scenarios in `TestTheQueueIsThePage` add per-row assertions
  (risk, amount, age, kind, severity rail, periods-not-wall-clock) that did not
  exist on either list before.
- Result: PASS (strengthened)
- Evidence: `test_every_row_carries_risk_amount_age_and_kind` iterates every
  `exception-row` and fails naming the item id

### Scenario: row 6 — the probe render-path check reads the AST instead of grepping source text
- Input: `git diff` of `test_ui_probe_surface.py` (+77 lines)
- Expected: the criterion is about what the CODE does, not what the prose says
- Actual: the merged queue's own disclosure legitimately contains the word
  "probe" (visible in `ux-queue-desktop-1280-2026-08-03.png` — "BEFORE YOU
  START: THIS QUEUE CONTAINS PROBES"), so a source-text grep would now fail for
  a reason unrelated to the criterion. An AST check over the render path is a
  **stricter** test of the same property: it cannot be satisfied by renaming a
  variable, which a grep can.
- Result: PASS (not a weakening — the substitute is strictly harder to fool)
- Evidence: `AC-F12-15`'s other three sites, the percentage-window regex, the
  twelve-path sweep and the header sweep are all retained

### Scenario: row 7 — reachability allows declared aliases
- Input: `git diff` of `test_ui_boundaries.py`
- Expected: the allowance is read from product code, and each alias's target is
  separately asserted reachable
- Actual: the allowance reads `routes.SCREEN_ALIASES`; two new scenarios were
  added (`test_every_alias_serves_a_screen_that_is_itself_reachable`,
  `test_the_merged_queue_serves_the_same_screen_under_all_three_addresses`), and
  `test_every_parameterised_screen_is_reached_by_following_a_real_link` gained
  four new object-route assertions.
- Result: PASS as written, **with a residual gap** — see
  `mutation-tests-2026-08-03.md` M3. The claim "an alias cannot be added by
  widening a test constant" is literally true; the property it secures is not
  fully held.
- Evidence: mutation-proved both ways

### Scenario: row 8 — `test_ui_approvals` gold selectors widened from three to five
- Input: `git diff`, plus a mutation
- Expected: same meaning — a human decision — under the brand's own colour law
- Actual: `GOLD_RULES` is `(".btn.approve", ".seal", ".card.approved", ".pull",
  ".pull-dot")` and the assertion is **set equality**, not containment, so the
  set is still closed. The two added selectors are one concept (the Council
  Mark's pull-line and its terminus dot). A separate scenario asserts the
  colour law's negative half — `.thread` and `.core-dot` must not carry
  `--gold`.
- Result: PASS (widened but still closed; mutation-proved)
- Evidence: mutation M4 — `.thread{stroke:var(--gold)}` failed **3** scenarios
  including the set-equality one. Independently confirmed in a real browser:
  R7 in `rendered-ui-2026-08-03.md` found 28 gold-painted elements across 12
  renders and **every one** is `.pull`, `.pull-dot` or `.btn.approve`.

### Scenario: prose/assertion mismatch in row 8's docstring
- Input: `backend/tests/test_ui_approvals.py::TestGoldIsUsedHereAndNowhereElse`
- Expected: the docstring describes what the assertion checks
- Actual: the docstring says "**THE COUNCIL MARK'S PULL-LINE IS THE FOURTH AND
  LAST PLACE**" while `GOLD_RULES` has **five** entries
- Result: PASS (not a defect — four *places*, the fourth implemented as two
  selectors) but **recorded**, because "the docstring claims something the
  assertion does not check" is the exact class of defect the previous pass
  raised twice against this file's neighbours
- Evidence: `GOLD_RULES = (".btn.approve", ".seal", ".card.approved", ".pull", ".pull-dot")`
