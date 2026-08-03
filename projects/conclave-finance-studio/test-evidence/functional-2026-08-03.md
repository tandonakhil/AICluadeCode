# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Suite owner:** `functional-agent`
**Executed by:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/functional/run.sh`
**Exit code:** 0
**Scenarios: 354 — PASS 354, FAIL 0, SKIP 0**

Test-count delta against `9d605b1`: **+5 added, −5 removed, 0 net.** All ten are
the `/exceptions` → `/evidence/run/<id>` re-point across `test_f26_criteria`,
`test_f28_criteria` and `test_f33_criteria`; each removed node ID has a
successor asserting the same thing on the screen the module moved to. Verified
scenario by scenario in `changed-scenario-audit-2026-08-03.md`.

---

### Scenario: the suite runs at its own entry point
- Status: EXECUTED
- Input: `dev/tests/suites/functional/run.sh`
- Expected: exit 0, "EXECUTED — suite passed"
- Actual: exit 0
- Result: PASS
- Evidence: `354 passed in 22.86s`

### Scenario: CONFLICT 1 (a) — `test_ui_dossier`'s "no links at all" vs edge E8
- Status: EXECUTED — **reported, not resolved**
- Input: `ARCHITECTURE_KB` §9.4, `AC-F41-04`, and the changed scenario
- Expected: confirm the fetch-nothing substance and `AC-F41-04`'s retained view
  are genuinely untouched
- Actual: **both confirmed untouched.**
  - **Fetch-nothing:** `test_there_is_no_external_reference_of_any_kind` does not
    appear in the diff. Independently re-proved in a real browser — the served
    dossier saved to disk and opened as `file://` issued zero non-`file://`
    requests and rendered still styled.
  - **`AC-F41-04`'s retained view:** `state._retained_view` builds a `<section>`
    with an `<h2>`, a `<table>` and a `<p>`. It contains **no anchor of any
    kind**, and it is assembled separately from the screen renderer precisely so
    a screen's chrome cannot leak into it. The exported artefact is unaffected
    by the dossier screen's new back-reference.
  - §9.4's three binding consequences are about the *evidential region* being a
    pure function of `(review_payload, template_version)`, byte-determinism, and
    inlined styles. **None of the three speaks to anchors on the dossier
    screen.** An `<a>` is inert until clicked.
- Result: PASS on substance; **the conflict stands open** — whether the dossier
  SCREEN (as opposed to the retained view) should carry zero anchors is a ruling
  for `functional-design-agent`, and is not decided here
- Evidence: `_retained_view` source at `app/ui/state.py:2437`; rendered-UI R1

### Scenario: CONFLICT 1 (b) — gold is narrower than `UX_KB` A2.8
- Status: EXECUTED — **reported, not resolved**
- Input: `UX_KB` A2.8 vs `chrome.STYLESHEET`
- Expected: state the departure
- Actual: the build paints gold on **five selectors only** —
  `.btn.approve`, `.seal`, `.card.approved`, `.pull`, `.pull-dot` — asserted by
  set **equality**. A2.8 additionally gives gold to `.goldline` (one
  gold-underlined phrase per page-opening) and to the six section icons.
  Neither is carried: `.goldline` is not in the stylesheet at all and the icons
  take `--ink-3`. `code-agent`'s stated reason is the brand's own rule — gold
  means *a human decided*, and a decorative headline underline is not a human
  decision.
- Result: the departure is **real, deliberate and disclosed**; not resolved here
- Evidence: **`UX_KB` A2.8's own version row reads "Human request, 2026-08-03;
  approval pending"** — the KB entry the build departs from is not yet approved,
  which is material to whoever rules on it. Confirmed in a real browser: 28
  gold-painted elements across 12 renders, all `.pull`/`.pull-dot`/`.btn.approve`.

### Scenario: FINDING — `AC-F5-02` is reported PASS and the build cannot support it
- Status: EXECUTED
- Input: `tests/suites/functional/test_unclaimed_criteria.py:344`,
  `test_AC_F5_02_every_agent_is_listed_with_identity_entitlements_and_version`
- Expected: `AC-F5-02` — *"Given an agent that has been **deployed and has
  performed at least one action**, When the Inventory is read, Then the agent
  appears with its identity, its entitlements and its current version"*
- Actual: the scenario asserts
  `{a["principal_id"] for a in inventory["agents"]} == set(principals.DIRECTORY)`
  — **the projection compared against its own source.** That equality is true by
  construction and cannot fail for the reason the criterion is about. The
  criterion's population is *agents that acted*, which the scenario never
  consults.
  **Five agents authored findings in the pilot run. Four of them do not appear
  on `/inventory` at all**: `agent.crossperiod-surveillance`,
  `agent.omission-detector`, `agent.anomaly-detect`, `agent.fidelity-check`.
- Result: **FAIL** — the criterion is not satisfied and the suite reports it green
- Evidence: authors `{crossperiod-surveillance: 3, omission-detector: 1,
  coding-detect: 1, anomaly-detect: 1, fidelity-check: 1}`; `/inventory` rows
  `{agent.anomaly_detector@1, agent.coding-detect, agent.omission_detector@1,
  agent.threshold_widening@1, …}`. Reproduced over HTTP against the served
  pilot — smoke **S12 FAIL**. This is the same id disagreement `code-agent`
  disclosed on the agent page; the disclosure was added to
  `/evidence/agent/<id>` and **not** to `/inventory`, whose own rendered prose
  still reads *"An agent that can act is an agent that is listed."*

### Scenario: FINDING — `AC-F5-03`/`-05` lineage completeness over the same gap
- Status: EXECUTED
- Input: `test_AC_F5_03_a_lineage_result_STATES_that_it_is_complete_rather_than_sampled`
- Expected: `AC-F5-05` — *"a lineage query that cannot be computed completely is
  labelled **incomplete** and names what could not be traversed; a partial list
  is never returned unlabelled"*
- Actual: the scenario asserts `lineage["complete"] is True` for **every** agent.
  Seven dossiers exist in the pilot close. **Zero of them appear in any
  lineage**; the union of artefacts across all eleven inventory rows is 9 and
  none is a dossier. Every row still reports `complete=True`.
- Result: **FAIL** — a partial list is being returned labelled complete
- Evidence: `agent.omission_detector@1` reports 8 artefacts; the four agents
  that authored the seven dossiers report 0 or are not listed. Downstream of the
  same id disagreement.

### Scenario: register 16's closure claim over `AC-F5-07`
- Status: EXECUTED
- Input: register entry 16, CLOSED at pass 4, claiming each of fifteen
  observable-UI criteria "is asserted on the screen it names, in the state it
  names"
- Expected: `AC-F5-07` — *"the agent inventory is visible listing **each
  agent**"*
- Actual: `test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements`
  checks `agents[0]` for the words "Version" and "Entitlements". It never checks
  the population either.
- Result: **advisory** — the assertion is present and passes; it does not cover
  the criterion's "each agent" clause on a build where four of five acting
  agents are absent from the screen
- Evidence: `test_ui_governance_screens.py:341`
