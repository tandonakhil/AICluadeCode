# Test evidence — changed-scenario audit (added / removed / changed, named)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Baseline:** `dev` @ `1b1b56e` (2,977) → **head `dev` @ `e00a214` (2,987)**
**Parent repo:** `8dcb490`
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

**Method.** Node ids collected at both commits with the same interpreter
(`--collect-only -q -o addopts=`), the baseline in a detached worktree, and
compared with `comm`. Not counted by hand, and not taken from the commit
messages.

**+12 added, −2 removed, 5 changed in place. Net +10.**

---

### Scenario: the two removals are parametrisations, not deletions
- Status: EXECUTED
- Input: `comm -23 base.ids head.ids`
- Expected: each removal accounted for
- Actual: **exactly two, both bare ids whose parametrised successors are in the
  added set** —
  `test_evaluator_primitives.py::test_every_anomaly_states_the_threshold_in_force`
  → `[1000] [1] [200.01] [49.99]`;
  `test_obligation_gap.py::test_each_kind_labels_its_own_fields_in_its_own_words`
  → `[scheduled_reversal] [interface_feed_entry] [intercompany_counterparty]`
- Result: PASS — **no scenario was deleted in this pass**

### Scenario: the twelve additions are each traceable to a stated purpose
- Status: EXECUTED
- Actual: 4 threshold parametrisations (both directions, both edges);
  3 obligation-kind parametrisations; 1 label-distinctness scenario;
  1 `AC-F38-01` every-card scenario; 1 whole-surface disclosure guard;
  2 `unregistered_actors` scenarios
- Result: PASS

### Scenario: the five changed-in-place scenarios — do they assert MORE?
- Status: EXECUTED
- Input: `git diff 1b1b56e..e00a214` on the five bodies, plus a mutation each
- Expected: strictly more, per the pass-19 claim *"no scenario asserts less than
  it did"*
- Actual: **four yes, one no.**

| Scenario | Verdict | Mutation |
|---|---|---|
| `test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements` | MORE — every row, labels **and** values, joined to the broker payload | F7-M caught; M6 caught |
| `test_AC_F5_07_a_lineage_view_is_reachable_for_each_listed_version` | MORE — counting became containment | M5 caught |
| `test_AC_F5_02_IS_NOT_MET_agents_that_acted_are_absent_from_the_inventory` | MORE — the four links are now followed and their landing asserted | M3 caught; M3b caught |
| `test_a_whole_export_carries_every_reconstruction_field` | MORE — two dossiers with different values, every field on both | S5 caught |
| `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts` | **NEITHER more nor less in effect** — the register holds one entry, so the loop and `entries[-1]` are the same assertion | S3 **NOT caught** |

- Result: **PARTIAL** — recorded as such, not rounded up. See
  `sampling-sweep-2026-08-03.md`, Finding A

### Scenario: does any scenario assert LESS than it did?
- Status: EXECUTED
- Input: the four removed literal-value assertions in `test_obligation_gap.py`
- Expected: none, per the recorded claim
- Actual: **one does.**
  `test_each_kind_labels_its_own_fields_in_its_own_words` lost
  `== "expected reversal period"`, `== "unreversed amount"`, `== "stopped feed"`,
  `== "amount that did not post"` and replaced them with a comparison against the
  constant the implementation itself reads
- Result: **FAIL** — the claim *"no scenario asserts less than it did"* is not
  true as written. Mutation-demonstrated: S1b reworded three labels to
  `"thing"/"when"/"how much"` and **2,987 stayed green**. Detail in
  `sampling-sweep-2026-08-03.md`, Finding B

### Scenario: no criterion claim was dropped
- Status: EXECUTED
- Actual: **256 `AC-…` identifiers referenced at both commits, 0 lost, 0 gained**
- Result: PASS

### Scenario: no test file was deleted
- Status: EXECUTED
- Input: `git diff --stat 1b1b56e..e00a214`
- Actual: **8 files touched, all modified, none deleted, none added**
- Result: PASS
