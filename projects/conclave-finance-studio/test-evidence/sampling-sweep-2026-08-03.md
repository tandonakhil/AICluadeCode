# Test evidence — the sampling sweep, run INDEPENDENTLY

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Why this was re-run rather than accepted

Pass 19 reported a sweep of **39 candidates, 5 real, 34 dismissed as
legitimate**. A dismissal list is a judgement, and the judgement was made by the
agent whose own scenario started the sweep. This is an independent pass with a
**deliberately different and broader heuristic**, so the two disagree by
construction rather than by luck.

## Method (mine, not `code-agent`'s)

AST scan over every `test_*.py` in `backend/tests` and `tests/suites`. A
function is a candidate when its **name or docstring** quantifies
(`each|every|all|both|any|none|no_two|per_`) **and** its body performs a
constant-index read (`[0]`, `[-1]`, `[1]`…) **or** calls a sampler
(`pop`, `first`, `one`, `next`, `min`, `max`). Candidates are then ranked by
whether the function contains any loop, comprehension or `parametrize` at all.

Broader than pass 19's on three axes: it reads docstrings as well as names, it
counts sampler *calls* and not only subscripts, and it treats a scenario with no
iteration construct whatsoever as the hot subset.

Script: `scratchpad/p19/sampsweep.py`; raw output `scratchpad/p19/sweep.json`.

## Counts

| | |
|---|---|
| candidates flagged | **60** (pass 19: 39) |
| hot subset — no loop, no comprehension, no `parametrize` | **28** |
| dismissed as `.one()` — a helper that *asserts exactly one* | 6 |
| dismissed as size-pinned (`assert len(...) == 1` in the same body) | 5 |
| read in full by eye | 17 |
| **real defects confirmed** | **2** |

`uihelpers.Document.one()` asserts `len(found) == 1` before returning, so every
`.one()` hit is a false positive of my heuristic and is recorded as such rather
than counted as a dismissal of substance.

## Agreement with pass 19's five

Four of the five were verified fixed **by mutation** — see
`mutation-tests-2026-08-03.md` (S1, S2, S4, S5 all caught). The fifth,
`AC-F40-16`, is Finding A below. Pass 19's 34 dismissals are not contradicted by
my 58: every one I read in full was a scenario whose quantifier word belongs to
its *docstring prose* or to a two-element tuple, not to a plural population.

---

## Finding A — `AC-F40-16`'s "every produced file" runs over a population of one

### Scenario: S3 — strip the three facts from every register entry but the last
- Status: EXECUTED
- Input: `ExportRegister.as_dict` blanks `approval_decision_id` and
  `export_decision_id` on `rows[:-1]`
- Expected: `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`
  fails, since it was rewritten this pass from `entries[-1]` to a loop
- Actual: **NOT CAUGHT — `tests/suites/functional/test_f40_criteria.py`: 23 passed**
- Result: **FAIL**
- Evidence: instrumented probe printed `S3-PROBE rows=1` twice — the register the
  scenario reads holds **exactly one entry**. With one row, `entries[-1]` and
  `for entry in entries` assert precisely the same thing, so the rewrite cannot
  fail in any way the old form could not

**What this means.** The change is a real improvement to the *text* and an inert
one in *effect*: the criterion says "every Journal Import file this system
produced" and the scenario still verifies it of one file. This is the same shape
the sweep was opened to find, one level up — the fix moved the sampling from
`entries[-1]` to the fixture. Closing it needs a second produced file in the
scenario's world, which is a test-fixture change, not a product change.

Not a regression: nothing that passed before fails now. Reported because "every
entry" reads as held and is not.

---

## Finding B — `obligation_gap` lost four literal-value assertions and nothing replaced them

### Scenario: S1b — reword `scheduled_reversal`'s three labels, keeping all kinds distinct
- Status: EXECUTED
- Input: `KIND_VOCABULARY["scheduled_reversal"]` labels changed to
  `"thing"` / `"when"` / `"how much"` — generic words no close reviewer could
  act on, which is precisely what the criterion's "in its own words" forbids.
  All three kinds remain mutually distinct, so the distinctness scenario is
  untouched
- Expected: caught — at `1b1b56e` four of these values were asserted as literals
- Actual: **NOT CAUGHT. Whole tree: 2,987 passed in 218.37s, exit 0, zero failures**
- Result: **FAIL**
- Evidence:
  - `git show 1b1b56e:backend/tests/test_obligation_gap.py` lines 249-256 —
    `assert reversal["period_label"] == "expected reversal period"`,
    `assert reversal["amount_label"] == "unreversed amount"`,
    `assert feed["origin_label"] == "stopped feed"`,
    `assert feed["amount_label"] == "amount that did not post"`
  - head lines 259 and 267 — the only remaining reads are
    `assert found[field] == vocabulary[field]` and a distinctness loop, both over
    `obligation_gap.KIND_VOCABULARY` itself
  - `scratchpad/p19/s1b-fulltree.txt`

**Why it is a defect and not a style question.** `obligation_gap.evaluate()`
builds the finding's labels *from* `KIND_VOCABULARY` (line 122,
`vocabulary = KIND_VOCABULARY[obligation_kind]`). The rewritten scenario
compares the evaluator's output to the constant the evaluator read — the
projection against its own source. That is the exact defect class register 34
records for the old inventory scenario (`inventory == principals.DIRECTORY`,
"an equality that cannot fail for the reason the criterion is about"). It cannot
fail for the reason "in its own words" is about.

**And it contradicts a recorded claim.** `PROJECT_CONTEXT.md` §"After pass 19"
states: *"No scenario was deleted in this pass, and no scenario asserts less than
it did."* In the value dimension this scenario asserts less: four literal
expectations became zero. The node-id delta (+3, −1) shows growth and hides the
loss, which is exactly the invisibility the delta report exists to prevent.

**What was gained is real too** — `intercompany_counterparty` went from
unasserted to asserted, and S1 confirms a copied vocabulary is now caught. The
fix traded a sampling defect for a tautology defect; both halves belong in front
of a human.

---

## Candidates dismissed, with the reason

### Scenario: `.one()` hits are not sampling
- Status: EXECUTED · Expected: `one()` asserts cardinality
- Actual: `uihelpers.py:122-127` — `assert len(found) == 1, "expected exactly one
  {!r} on {}, found {}"`. 6 candidates dismissed on this
- Result: PASS (dismissal justified)

### Scenario: `test_UX12_the_three_failure_grammars_differ_in_words_with_styling_stripped`
- Status: EXECUTED · Expected: does it exercise all three grammars?
- Actual: **yes** — REFUSED, INVALID and UNAVAILABLE are each produced, the
  third by cutting the transport. Docstring records this as the pass-4d fix for
  the same defect class
- Result: PASS (dismissed)

### Scenario: `test_UX11_AC_F12_11_the_disclosure_is_visible_before_any_item_in_the_queue`
- Status: EXECUTED · Actual: `order[0]`/`order[1]` index a **two-element**
  `[indexOf(disclosure), indexOf(queue)]` tuple, not a population
- Result: PASS (dismissed)

### Scenario: `test_the_evidential_chain_walks_finding_to_run_to_agent_to_readiness`
- Status: EXECUTED · Actual: walks **one** chain, which is what `UX_KB` A2.1's
  sentence asserts. `all(edge)[0]` samples one E5 link on a page that renders one
- Result: PASS (dismissed) — noted as the weakest dismissal in the set

### Scenario: the 17 read in full
- Status: EXECUTED
- Actual: 15 are singular-subject scenarios (*"a leg"*, *"a batch"*, *"a member"*,
  *"a dataset"*, *"a capture"*) whose quantifier matched docstring prose, and
  read `findings[0]` of a run constructed to produce one finding. 2 are the two
  above
- Result: PASS (dismissed)
