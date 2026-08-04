# Test evidence — mutation testing (verification of the pass-19 fixes)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

**Method.** Every mutation was applied in a **detached `git worktree` at
`e00a214`** (`git worktree add --detach`), never in the working tree, which
stayed clean at `e00a214` for the whole pass. Product code was mutated, not
tests, except where the mutation is explicitly a probe of a test helper (M2a).
Each mutation was reverted with `git checkout -q .` before the next.

**Verdict: 15 mutations, 14 caught, 1 deliberately NOT caught and correctly so
(M3 against the whole-surface guard — see below). One further mutation, S1b,
was NOT caught and should have been; it is Finding B in
`sampling-sweep-2026-08-03.md`.**

---

## F1 — the disclosure claim, re-scoped from one screen to no reachable screen

### Scenario: M1 — restore the sentence to the four agent pages
- Status: EXECUTED
- Input: `backend/app/ui/pages.py`, agent-page subtitle re-opened with
  `"An agent that can act is an agent that is listed. "`
- Expected: `test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`
  fails and **names the offending pages**
- Actual: **FAILED, naming five URLs** —
  `['/evidence/agent/agent.anomaly-detect', '/evidence/agent/agent.coding-detect',
  '/evidence/agent/agent.crossperiod-surveillance',
  '/evidence/agent/agent.fidelity-check', '/evidence/agent/agent.omission-detector']`
- Result: PASS (mutation caught)
- Evidence: `assert offenders == []` at `test_unclaimed_criteria.py:491`. Note it
  catches the *registered* agent's page too, not only the four absent ones

### Scenario: M2a — the guard cannot pass by reaching nothing
- Status: EXECUTED
- Input: `uihelpers.reachable_urls()` short-circuited to return `{"/": 0}`, so
  link-following reaches nothing. The sentence stays removed, so the
  "no offenders" half is trivially satisfiable
- Expected: fails anyway, on the containment half
- Actual: **FAILED** at `assert page in reached` —
  `('/evidence/agent/agent.crossperiod-surveillance', ['/', '/approvals', …])`.
  The surviving `reached` entries come only from the post-control documents;
  no agent page is among them
- Result: PASS (mutation caught) — **the guard is not forgeable by reaching nothing**
- Evidence: `test_unclaimed_criteria.py:486`

### Scenario: the four pages are asserted in by the ids the BROKER reports absent
- Status: EXECUTED
- Input: read of the guard body
- Expected: the page list is derived, not hard-coded
- Actual: **derived** —
  `absent = state.acting_agents_absent_from_inventory()`, `assert len(absent) == 4`,
  then `"/evidence/agent/{}".format(principal_id) in reached` for each
- Result: PASS
- Evidence: `test_unclaimed_criteria.py:481-487`

---

## The fourth finding — a link that was credited and held by nothing

### Scenario: M3 — repoint all four `absent-agent-link` hrefs at `/inventory`
- Status: EXECUTED
- Input: `href="/inventory"` in place of `href="/evidence/agent/{}"`
- Expected: fails now (it left all 2,977 green at `1b1b56e`)
- Actual: **FAILED** —
  `AssertionError: ('agent.crossperiod-surveillance', '/inventory')` at
  `test_unclaimed_criteria.py:426`. **1 failed, 26 passed** in that file
- Result: PASS (mutation caught)
- Evidence: register 34's third "built instead" claim is now held

### Scenario: M3 against the whole-surface guard — correctly NOT caught
- Status: EXECUTED
- Input: the same M3 mutation, whole `test_unclaimed_criteria.py` run
- Expected: `test_the_unqualified_AC_F5_02_claim_appears_on_NO_reachable_screen`
  still passes, because the agent pages stay reachable through the object-graph
  chain (finding → run → agent) even with `/inventory`'s links broken
- Actual: **exactly one scenario failed, and it was the link scenario.** The
  whole-surface guard passed
- Result: PASS — `code-agent`'s own observation reproduced. The two guards are
  genuinely independent; neither subsumes the other
- Evidence: `1 failed, 26 passed`

### Scenario: M3b — the link resolves but lands on the wrong agent
- Status: EXECUTED
- Input: every `/evidence/agent/<id>` page renders `h1` = `agent.coding-detect`
- Expected: fails on the landing assertion, not the href assertion
- Actual: **FAILED** — `- agent.crossperiod-surveillance / + agent.coding-detect`
  at `test_unclaimed_criteria.py:427`
- Result: PASS (mutation caught) — the link is *followed*, not merely *shaped*

---

## F2 — `AC-F5-07`, "each agent" asserted of every agent

### Scenario: F7-M — relabel every agent row but the first
- Status: EXECUTED
- Input: `"Version"/"Entitlements"` → `"Ver."/"Rights"` for row index ≥ 1. This
  is the exact mutation that left 2,977 green at `1b1b56e`
- Expected: fails now
- Actual: **FAILED** —
  `AssertionError: agent.coding-detect … 'Kind agent Ver. unversioned Rights …'`
  at `test_ui_governance_screens.py:430`
- Result: PASS (mutation caught)
- Evidence: `1 failed, 44 passed` in that file

### Scenario: M6 — right label, wrong agent's version on every row
- Status: EXECUTED
- Input: `kv("Version", payload["agents"][0]["version"])` on every row
- Expected: fails — the values are joined to the broker's payload per principal
- Actual: **FAILED** at `test_ui_governance_screens.py:432`
- Result: PASS (mutation caught) — the join is real, not a label presence check

### Scenario: M5 — every lineage view attributed to agent 0
- Status: EXECUTED
- Input: `data_principal=payload["agents"][0]["principal_id"]` on every
  `lineage-view`
- Expected: fails — `len(lineage) == len(rows)` became containment
- Actual: **FAILED** at `test_ui_governance_screens.py:454`
  (`+ agent.anomaly_detector@1`)
- Result: PASS (mutation caught) — the counting assertion is gone and the
  per-row `assert views[0].attrs["data-principal"] == principal_id` holds

---

## F3 — `unregistered_actors` returns UNKNOWN, not an empty list

### Scenario: F3-M1 — restore the bare list
- Status: EXECUTED
- Input: `"unregistered_actors": _unregistered_actors(store)["unregistered_actors_in_scope"]`
- Expected: both F3 scenarios fail
- Actual: **2 failed, 25 passed** — the shape scenario and the join scenario
- Result: PASS (mutation caught)

### Scenario: F3-M2 — flip `computable` to `True`
- Status: EXECUTED
- Expected: both fail
- Actual: **2 failed, 25 passed**
- Result: PASS (mutation caught)
- Note: this also shows the shape scenario would fail *on the day findings become
  ledger-recorded* — see `functional-2026-08-03.md`, Observation 3

### Scenario: F3-M3 — remove the reason from `LINEAGE_UNTRAVERSED`
- Status: EXECUTED
- Input: the findings entry reworded to `"finding - now recorded on the ledger"`
- Expected: the join scenario fails so the UNKNOWN cannot outlive its reason
- Actual: **FAILED**, 1 failed 26 passed, at
  `test_unclaimed_criteria.py:549`
- Result: PASS (mutation caught)

### Scenario: F3-M4 — remove the screen block, keep the payload
- Status: EXECUTED
- Input: `if False and isinstance(answer, dict):`
- Expected: the shape scenario fails on the screen half
- Actual: **FAILED** in `uihelpers.one()` — "expected exactly one
  `unregistered-actors-answer`, found 0"
- Result: PASS (mutation caught) — an answer only a payload reader meets is caught

### Scenario: the shape, not the emptiness, is what is asserted
- Status: EXECUTED
- Input: read of `test_the_broker_answers_the_population_question_UNKNOWN_and_not_none`
- Expected: asserts dict-ness, `scope`, `untraversed`, `statement`, not `== []`
- Actual: **confirmed** — `isinstance(answer, dict)`,
  `answer["scope"] == ges_main.LINEAGE_SCOPE`,
  `answer["untraversed"] == [ges_main.LINEAGE_UNTRAVERSED[1]]`,
  `"UNKNOWN" in statement`, `"it is not none" in statement`, plus
  `assert "findings" not in answer`
- Result: PASS

### Scenario: the second scenario joins `computable: False` to its justification
- Status: EXECUTED
- Actual: **confirmed** —
  `assert (answer["computable"] is False) == (findings_entry in ges_main.LINEAGE_UNTRAVERSED)`,
  with the entry's own text asserted (`startswith("finding - ")`, and the
  "not the same string as any registered principal id" clause)
- Result: PASS

---

## Sampling-sweep spot-checks (5 of the 5 fixes, by mutation)

### Scenario: S1 — `intercompany_counterparty`'s vocabulary copied from `scheduled_reversal`
- Status: EXECUTED
- Expected: caught (this kind was asserted by nothing at `1b1b56e`)
- Actual: **FAILED** — `test_no_two_kinds_share_a_label_so_the_words_are_ITS_OWN`,
  `3 = len(['original journal', 'stopped feed', 'original journal'])`
- Result: PASS (mutation caught) — **but caught by the distinctness scenario, not
  by the parametrised one.** See S1b

### Scenario: S1b — reword `scheduled_reversal`'s three labels, keeping them distinct
- Status: EXECUTED
- Input: `"original journal"/"expected reversal period"/"unreversed amount"` →
  `"thing"/"when"/"how much"`
- Expected: caught — these were literal-value assertions at `1b1b56e`
- Actual: **NOT CAUGHT. Full tree: 2,987 passed in 218.37s, exit 0**
- Result: **FAIL — a real defect this pass introduced.** Finding B in
  `sampling-sweep-2026-08-03.md`

### Scenario: S2 — `distribution_outlier` omits the threshold in the BELOW direction
- Status: EXECUTED
- Input: threshold fields emitted only when `direction == "above"`
- Expected: caught by the new below-direction parametrisations
- Actual: **FAILED on `[1]` and `[49.99]`**, 2 failed 28 passed
- Result: PASS (mutation caught)

### Scenario: S3 — `AC-F40-16`: the three facts survive only on the newest register row
- Status: EXECUTED
- Input: `approval_decision_id`/`export_decision_id` blanked on every entry but
  the last
- Expected: caught by the "every entry" rewrite
- Actual: **NOT CAUGHT — 23 passed.** Probe shows why: the register holds
  **exactly 1 entry** in that scenario (`S3-PROBE rows=1`), so
  `entries[-1]` and `for entry in entries` are the same assertion
- Result: **FAIL — the fix is inert at this site.** Finding A in
  `sampling-sweep-2026-08-03.md`

### Scenario: S4 — `AC-F38-01`: non-first cards carry the first dataset's facts
- Status: EXECUTED
- Input: `certifying_owner` and `as_of` copied from `rows[0]` onto cards 2 and 3
- Expected: caught
- Actual: **FAILED** at `test_ui_governance_screens.py:94`, 1 failed 44 passed
- Result: PASS (mutation caught)

### Scenario: S5 — export reconstruction: every dossier carries the first's `dataset_version`
- Status: EXECUTED
- Expected: caught by the two-dossier rewrite
- Actual: **FAILED** at `test_audit_domain_and_export.py:213`, 1 failed 37 passed
- Result: PASS (mutation caught)
