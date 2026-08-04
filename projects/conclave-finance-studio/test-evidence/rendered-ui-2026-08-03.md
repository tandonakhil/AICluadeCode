# Test evidence — rendered-UI verification (Playwright / Chromium, web backend)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**13 scenarios, 13 pass, 0 fail, 0 inconclusive.** Chromium **148.0.7778.96**,
driven against the **served** pilot on 8021 at two viewports (1280 and 1440),
the invocation starting, driving and reaping its own pilot **inside one command
invocation**. The human's pilot (pid 59422, 8030) was alive before and after.

**16 screenshots** in this directory, all captured this pass.

## Backend

**Web backend only.** MVP1 ships one surface — desktop web — per this project's
header and `PLAN` §9.2 A2, so the **RNTL native backend does not apply** and
**Maestro + simulator** remains the future deeper backend, unavailable on this
machine (2026-07-26 toolchain spike, unchanged). Nothing is reported as passing
on a backend that was not run.

## Assertions are on what the browser computed, not on source strings

Computed styles resolved by Chromium, the rendered accessibility structure,
`getBoundingClientRect` geometry, effective opacity multiplied up the ancestor
chain, and real clicks — never a grep of served bytes. Where a claim is visual,
a screenshot backs it.

## One harness correction this pass

The "gold appears nowhere a human decision is not being made" predicate
excluded the brand lockup **by class name** (`lockup`, `pull-dot`), and then
flagged the brand mark's own `path.pull` — the same lockup — at both viewports.
Lockup membership is now read from the DOM (`el.closest('.lockup')`), which is
the structural fact the scenario means. The four "violations" were the brand
mark, not an action affordance on a non-decision screen.

---

### Scenario: the gold predicate can say YES (positive control)
- Status: EXECUTED
- Input: /approvals/PROP-2026-06-0031 at 1280 and 1440, computed styles over body *, body svg *
- Expected: gold on the Approve control and on the brand mark
- Actual: 1280: 5 gold-bearing declarations, 1440: 5. sample=[('BUTTON', 'btn approve', 'color', 'rgb(138, 90, 23)', 'Approve these 2 lines for export'), ('BUTTON', 'btn approve', 'backgroundColor', 'rgb(251, 241, 223)', 'Approve these 2 lines for export')]
- Result: PASS
- Evidence: ui-approval-gold-1280-2026-08-03.png, ui-approval-gold-1440-2026-08-03.png

### Scenario: gold appears NOWHERE a human decision is not being made
- Status: EXECUTED
- Input: /queue and /inventory at both viewports, same predicate
- Expected: no action-gold outside the brand lockup
- Actual: 0 violations
- Result: PASS
- Evidence: {"/queue": [], "/inventory": []}

### Scenario: no green anywhere on the served surface
- Status: EXECUTED
- Input: computed colour on 5 screens x 2 viewports; predicate g > r+25 and g > b+25
- Expected: zero green-dominant computed colours
- Actual: 0
- Result: PASS
- Evidence: []

### Scenario: no text is rendered at compounded opacity below 0.5
- Status: EXECUTED
- Input: every text-bearing element on 9 screens x 2 viewports, opacity multiplied up the ancestor chain
- Expected: no text below 0.5 effective opacity
- Actual: 0 offenders
- Result: PASS
- Evidence: []

### Scenario: the `.ctx` lockup defect stays fixed, measured not asserted
- Status: EXECUTED
- Input: getBoundingClientRect on .lockup-row and .ctx at both viewports
- Expected: .ctx is not a descendant of .lockup-row and sits below it
- Actual: {"1280": {"rowBottom": 48.875, "ctxTop": 55.875, "ctxIsChildOfRow": false, "ctxHeight": 48.5625, "rowHeight": 34.875}, "1440": {"rowBottom": 48.875, "ctxTop": 55.875, "ctxIsChildOfRow": false, "ctxHeight": 48.5625, "rowHeight": 34.875}}
- Result: PASS
- Evidence: {"1280": {"rowBottom": 48.875, "ctxTop": 55.875, "ctxIsChildOfRow": false, "ctxHeight": 48.5625, "rowHeight": 34.875}, "1440": {"rowBottom": 48.875, "ctxTop": 55.875, "ctxIsChildOfRow": false, "ctxHeight": 48.5625, "rowHeight": 34.875}}

### Scenario: no horizontal overflow at either viewport
- Status: EXECUTED
- Input: scrollWidth vs clientWidth on 9 screens x 2 viewports
- Expected: no overflow
- Actual: 0 overflowing
- Result: PASS
- Evidence: {}

### Scenario: every screen has exactly one `h1` and the landmark pair
- Status: EXECUTED
- Input: 11 screens, accessibility-relevant structure from the rendered DOM
- Expected: exactly one h1, at least one nav and one main
- Actual: 0 offenders
- Result: PASS
- Evidence: {}

### Scenario: the four agent pages do NOT render the unqualified claim
- Status: EXECUTED
- Input: rendered innerText of each agent page named absent on /inventory
- Expected: four pages, none carrying the sentence
- Actual: agents=4 claims={'agent.crossperiod-surveillance': False, 'agent.omission-detector': False, 'agent.anomaly-detect': False, 'agent.fidelity-check': False}
- Result: PASS
- Evidence: {"agent.crossperiod-surveillance": false, "agent.omission-detector": false, "agent.anomaly-detect": false, "agent.fidelity-check": false}

### Scenario: the four `/inventory` links are CLICKED and land on that agent
- Status: EXECUTED
- Input: real click on each absent-agent link, then the rendered h1
- Expected: each lands on the agent page whose id the row names
- Actual: {"agent.crossperiod-surveillance": {"url": "http://127.0.0.1:8021/evidence/agent/agent.crossperiod-surveillance", "h1": "agent.crossperiod-surveillance"}, "agent.omission-detector": {"url": "http://127.0.0.1:8021/evidence/agent/agent.omission-detector", "h1": "agent.omission-detector"}, "agent.anomaly-detect": {"url": "http://127.0.0.1:8021/evidence/agent/agent.anomaly-detect", "h1": "agent.anomaly-detect"}, "agent.fidelity-check": {"url": "http://127.0.0.1:8021/evidence/agent/agent.fidelity-check", "h1": "agent.fidelity-check"}}
- Result: PASS
- Evidence: {"agent.crossperiod-surveillance": {"url": "http://127.0.0.1:8021/evidence/agent/agent.crossperiod-surveillance", "h1": "agent.crossperiod-surveillance"}, "agent.omission-detector": {"url": "http://127.0.0.1:8021/evidence/agent/agent.omission-detector", "h1": "agent.omission-detector"}, "agent.anomaly-detect": {"url": "http://127.0.0.1:8021/evidence/agent/agent.anomaly-detect", "h1": "agent.anomaly-detect"}, "agent.fidelity-check": {"url": "http://127.0.0.1:8021/evidence/agent/agent.fidelity-check", "h1": "agent.fidelity-check"}}

### Scenario: the `/inventory` disclosure renders with all four agents named
- Status: EXECUTED
- Input: rendered geometry + innerText of the disclosure block
- Expected: non-zero box, four ids readable
- Actual: vis={'w': 962, 'h': 23.25, 'display': 'list-item', 'visibility': 'visible', 'opacity': '1', 'text': 'agent.crossperiod-surveillance'} named=4
- Result: PASS
- Evidence: ui-inventory-disclosure-1280-2026-08-03.png

### Scenario: the UNKNOWN population answer is actually visible, not merely present
- Status: EXECUTED
- Input: geometry, effective opacity and text of the answer node
- Expected: non-zero box, effective opacity >= 0.5, data-computable=false, UNKNOWN readable
- Actual: {"w": 1036, "h": 148.484375, "effOpacity": 1, "computable": "false", "text": "Agents acting under an unpublished idUNKNOWN Which agents acted under an id this registry does not publish is UNKNOWN here; it is not none. This is computed as a difference over the decision_ledger al", "fontSize": "15px"}
- Result: PASS
- Evidence: {"w": 1036, "h": 148.484375, "effOpacity": 1, "computable": "false", "text": "Agents acting under an unpublished idUNKNOWN Which agents acted under an id this registry does not publish is UNKNOWN here; it is not none. This is computed as a difference over the decision_ledger al", "fontSize": "15px"}

### Scenario: every lineage row renders INCOMPLETE with its scope
- Status: EXECUTED
- Input: rendered lineage rows on /inventory
- Expected: every row data-complete=false, scope=decision_ledger, INCOMPLETE readable, visible
- Actual: rows=11 ok=True
- Result: PASS
- Evidence: [{"complete": "false", "scope": "decision_ledger", "visible": true, "incomplete": true}, {"complete": "false", "scope": "decision_ledger", "visible": true, "incomplete": true}, {"complete": "false", "scope": "decision_ledger", "visible": true, "incomplete": true}, {"complete": "false", "scope": "decision_ledger", "visible": true, "incomplete": true}]

### Scenario: both viewports were checked (responsive requirement)
- Status: EXECUTED
- Input: 1280 and 1440 contexts driven for every style/geometry scenario above
- Expected: both
- Actual: 1280 and 1440
- Result: PASS
- Evidence: chromium 148.0.7778.96; 16 screenshots written to test-evidence/
