# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Suite owner:** `functional-design-agent` / `functional-agent` —
**`test-agent` did not author these scenarios**; it executed them, mutated them
and reports the result
**Blocking:** yes — `PROJECT_CONTEXT.md` Active Team: *"Test Policy: all suites
blocking. No advisory exceptions."*
**Status:** `EXECUTED`
**Entry point:** `tests/suites/functional/run.sh` → shared `_runner.sh`
**Exit code:** 0
**Scenarios: 355 — PASS 355, FAIL 0**

## Test-count delta since `6bf8ed9` (354)

| | |
|---|---|
| **added** | **+3** |
| **removed** | **−2** |
| changed | 1 (`test_AC_F5_06...` — its `lineage["complete"] is True` assertion replaced) |
| current | **355** |

**Removed — a coverage decision, named here rather than left in a diff:**

1. `test_AC_F5_02_every_agent_is_listed_with_identity_entitlements_and_version`
2. `test_AC_F5_03_a_lineage_result_STATES_that_it_is_complete_rather_than_sampled`

Both were the green scenarios gate 8 blocked on: the first asserted
`inventory == principals.DIRECTORY`, a projection against its own source; the
second asserted `lineage["complete"] is True` over rows that omit seven
dossiers. **Their removal is the right call**, but it is a reduction in claimed
coverage and the human should see it as one.

**Added (+3):** `test_the_inventory_needs_no_manual_registration_step` (the
narrowed registration clause only),
`test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory`,
`test_AC_F5_03_and_05_ARE_NOT_MET_no_dossier_appears_in_any_lineage`.

---

### Scenario: the functional suite runs to completion through its own entry point
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0
- Actual: **`EXECUTED — suite passed`**, 355 passed in 23.14s
- Result: PASS

### Scenario: the three replacement checks are falsifiable in BOTH directions
- Status: EXECUTED
- Input: nine mutations — ids reconciled, gap widened, disclosure removed,
  sentence restored, `LINEAGE_UNTRAVERSED` emptied, `complete` hard-coded,
  scope dropped, `data-complete` hard-coded, dossier index emptied
- Expected: each mutation fails at least one scenario
- Actual: **all nine caught.** In particular D1 — *ids reconciled, disclosure
  left behind* — fails, which is the direction `code-agent` claimed and the one
  that would otherwise let a fixed build keep a false "NOT MET" banner
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` Part C

### Scenario: `/inventory` no longer carries the unqualified claim
- Status: EXECUTED
- Input: the served `/inventory` markup — in-process, over real HTTP, and in
  Chromium
- Expected: *"An agent that can act is an agent that is listed"* absent
- Actual: **absent** in all three witnesses
- Result: PASS

### Scenario: every lineage row states scope and INCOMPLETE
- Status: EXECUTED
- Input: the 11 rendered `lineage-view` rows
- Expected: every row `data-complete="false"`, `data-scope="decision_ledger"`,
  naming its untraversed classes
- Actual: **11 of 11**, and `untraversed` names both classes —
  *"evidence dossier - produced by the close and not written to the decision
  ledger…"* and *"finding - authored under a run author id, which in this build
  is not the same string as any registered principal id"*
- Result: PASS

### Scenario: the broker returns `unregistered_actors`
- Status: EXECUTED
- Input: the inventory payload, measured in-process under the real fixtures
- Expected: the field exists
- Actual: **the field exists and its value is `[]`** — see Finding 3
- Result: PASS on existence; the value is a finding, not a pass

---

## Finding 1 — **BLOCKING**: the disclosure was removed from one screen and left standing on the four screens that screen links to

- Status: EXECUTED (three independent witnesses: in-process, real HTTP,
  Chromium)
- Input: `/evidence/agent/<id>` for each of the four agents `/inventory` names
  as absent and links to
- Expected: no surface repeats a claim the build records as NOT MET
- Actual: **all four agent pages carry, in the subtitle directly under the
  `<h1>`:** *"An agent that can act is an agent that is listed."* — and then,
  four lines later on the same page: *"This agent authored findings in this run
  and has no entry in the principal registry under this id."*
- Result: **FAIL**
- Evidence: `ui-agent-page-absent-agent-1280-2026-08-03.png`; smoke S12b;
  rendered R7; `backend/app/ui/pages.py:4096`

Why this matters, and what is and is not wrong:

- Register 34's own words are *"the unqualified sentence … is gone **from that
  screen**"* — literally true. **The register is not contradicted.**
- The same entry records that `/inventory` *"names all four absent agents,
  **links each to its agent page**"*. That link is the reader's path, and it
  leads from a screen saying `AC-F5-02` is NOT met to four screens that each
  assert the criterion's claim as a general truth.
- The guarding scenario is `test_unclaimed_criteria.py:421` —
  `assert "An agent that can act is an agent that is listed" not in document.markup`
  — where `document` is `/inventory` **and only `/inventory`**. A `grep` across
  both trees returns **exactly one hit**: no scenario asserts it anywhere else.
- This is the *same shape* as the defect pass 18 fixed: a claim that is true of
  the population a check happens to look at, and false of the population the
  claim is about.

Not fixed — reported, per this agent's guardrails.

## Finding 2 — **BLOCKING**: `AC-F5-07` has the same defect, and I agree with `code-agent`

`code-agent` raised this and declined to act, calling the narrowing of a
criterion's claim a Plan-gate decision. **I agree it has the same defect.** I
did not touch it. Measured rather than argued:

- The criterion (`FUNCTIONAL_SPEC` §AC-F5-07) reads: *"the agent inventory is
  visible listing **each** agent, its version and its entitlements"*.
- `test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements`
  (`backend/tests/test_ui_governance_screens.py:341`) reads `agents[0]` and
  checks for the two strings `"Version"` and `"Entitlements"`.
- **Mutation F7-M:** relabel the fields to `"Ver."`/`"Rights"` for every agent
  row **except the first**, so three of the four agent rows no longer carry
  what the criterion names. **Result: 2,977 scenarios green** — 2,302 unit +
  675 across all six SME suites. **Nothing anywhere notices.**

Two honest distinctions from the `AC-F5-02` case, so the human weighs it right:

1. It is **weaker, not false today**. All four agent rows currently do carry
   both fields, measured. The green is *unheld*, not *untrue*.
2. It is a **sampling** fault (`[0]` standing for "each"), not the tautology
   fault (`projection == its own source`). The `AC-F5-02` scenario could not
   fail for the reason the criterion was about; this one can — it just does not
   look.

The sibling scenario (`a_lineage_view_is_reachable_for_each_listed_version`)
asserts `len(lineage) == len(inventory-row)`, 11 = 11, which counts rows and
does not establish "reachable from that list" as the criterion words it.

## Finding 3 — **ADVISORY (recorded; not blocking on its own)**: `unregistered_actors` returns `[]` and is asserted by nothing

Register 34 lists three things "built instead". Two are real and
mutation-held. The third is not held at all.

- Measured: the inventory payload returns **`"unregistered_actors": []`** while
  `run_agent_ids()` = 5 and four of those five are absent from the inventory.
- Cause: it is computed as
  `{d["principal_id"] for d in store.decisions()} - set(principals.DIRECTORY)`
  — a set difference over the **decision ledger**. Findings are *not*
  ledger-recorded; that is literally the second entry in
  `LINEAGE_UNTRAVERSED`. **The field therefore cannot become non-empty in this
  build, by construction.**
- **`grep -rn "unregistered_actors" backend/tests tests/suites` returns
  nothing.** No scenario asserts its value in either direction. It would stay
  `[]` forever and no gate would notice.
- Register 33 records this product's own convention for exactly this shape:
  where the answer cannot be computed, the answer is **UNKNOWN, not none** —
  *"the most dangerous rounding in the product if it is ever softened"*. A bare
  `[]` from a source that structurally cannot hold the answer is that rounding.

Register 34's sentence — *"the broker's own answer to the population question
computed from its ledger"* — is accurate about the method, and on this build
returns the wrong answer to the question it names.
