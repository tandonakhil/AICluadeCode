# Test evidence — rendered-UI verification (Playwright / Chromium, web backend)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**19 scenarios, 19 pass, 0 fail, 0 inconclusive.** (Pass 20: 13. **+6**, all on
the pass-21/22 work.) Chromium **148.0.7778.96**, driven against the **served**
pilot on 8021 at two viewports (1280 and 1440), the invocation starting,
driving and reaping its own pilot **inside one command invocation**. The human's
pilot (**pid 78317**, re-read from `lsof`, port 8030) was alive before and
after; 8021/8022 were empty after teardown.

**20 screenshots** in this directory, all captured this pass.

## Backend

**Web backend only.** MVP1 ships one surface — desktop web — per this project's
header and `PLAN` §9.2 A2, so the **RNTL native backend does not apply** and
**Maestro + simulator** remains the future deeper backend, unavailable on this
machine (2026-07-26 toolchain spike, unchanged). Nothing is reported as passing
on a backend that was not run.

## Assertions are on what the browser computed, not on source strings

Computed styles resolved by Chromium, rendered accessibility structure,
`getBoundingClientRect` geometry, effective opacity multiplied up the ancestor
chain, and **real clicks** — never a grep of served bytes. Where a claim is
visual, a screenshot backs it.

**No harness correction was needed this pass.** The lockup-membership fix made
at pass 20 (`el.closest('.lockup')` rather than a class-name allowlist) carried
forward unchanged.

---

### Scenario: the gold predicate can say YES (positive control)
- Status: EXECUTED
- Input: /approvals/PROP-2026-06-0031 at 1280 and 1440, computed styles over `body *`, `body svg *`
- Expected: gold on the Approve control and on the brand mark
- Actual: 5 gold-bearing declarations at each viewport; sample `('BUTTON','btn approve','color','rgb(138, 90, 23)','Approve these 2 lines for export')`
- Result: PASS
- Evidence: ui-approval-gold-1280-2026-08-04.png, ui-approval-gold-1440-2026-08-04.png

### Scenario: gold appears NOWHERE a human decision is not being made
- Status: EXECUTED · Input: /queue and /inventory at both viewports · Expected: no action-gold outside the brand lockup · Actual: **0 violations** · Result: PASS
- Evidence: `{"/queue": [], "/inventory": []}`; ui-queue-*, ui-inventory-*

### Scenario: no green anywhere on the served surface
- Status: EXECUTED · Input: computed colour on 5 screens × 2 viewports, predicate `g > r+25 and g > b+25` · Actual: **0** · Result: PASS

### Scenario: no text is rendered at compounded opacity below 0.5
- Status: EXECUTED · Input: every text-bearing element on 9 screens × 2 viewports, opacity multiplied up the ancestor chain · Actual: **0 offenders** · Result: PASS

### Scenario: the `.ctx` lockup defect stays fixed, measured not asserted
- Status: EXECUTED · Actual: `rowBottom 48.875 / ctxTop 55.875 / ctxIsChildOfRow false` at both viewports · Result: PASS

### Scenario: no horizontal overflow at either viewport
- Status: EXECUTED · Input: scrollWidth vs clientWidth on 9 screens × 2 viewports · Actual: 0 overflowing · Result: PASS

### Scenario: every screen has exactly one `h1` and the landmark pair
- Status: EXECUTED · Input: 11 screens, accessibility structure from the rendered DOM · Actual: 0 offenders · Result: PASS

### Scenario: the four agent pages do NOT render the unqualified claim
- Status: EXECUTED · Input: rendered `innerText` of each agent page · Actual: four pages, none carrying the sentence · Result: PASS

### Scenario: the four `/inventory` links are CLICKED and land on that agent
- Status: EXECUTED · Actual: each real click lands on the agent page whose id the row names · Result: PASS

### Scenario: the `/inventory` disclosure renders with all four agents named
- Status: EXECUTED · Actual: non-zero box, four ids readable · Result: PASS · Evidence: ui-inventory-disclosure-1280-2026-08-04.png

### Scenario: the UNKNOWN population answer is actually visible, not merely present
- Status: EXECUTED · Actual: `w 1036, h 148.5, effOpacity 1, computable "false"`, UNKNOWN readable · Result: PASS

### Scenario: every lineage row renders INCOMPLETE with its scope
- Status: EXECUTED · Actual: `rows=11`, every row `data-complete=false`, `scope=decision_ledger`, INCOMPLETE readable, visible · Result: PASS

---

## New this pass — the structured reject, driven in a real browser

### Scenario: the six reject radios render as CODES, none pre-selected, none disclosed away
- Status: EXECUTED
- Input: computed properties of every `[data-testid=rejection-reason]` on `/review/ITEM-11500-PA`
- Expected: six distinct non-numeric values, each equal to its `data-reason-code`, none `checked`, all laid out, none inside `<details>`
- Actual: **six**, values `evidence_insufficient`, `population_not_covered`, `resolution_wrong`, `already_handled`, `data_stale_or_wrong`, `judgement_disagreement`; `checked=[false ×6]`; every `visible: true`, `inDetails: false`; each `value === data-reason-code`
- Result: PASS
- Evidence: ui-reject-form-1280-2026-08-04.png; labels read off the DOM — "Evidence insufficient for the conclusion drawn", "Population scanned does not cover this account", "Detection is correct, proposed resolution is wrong", "Known and already handled outside this system", "Data is stale or wrong at source", "Judgement call - I disagree, reasoning below"

### Scenario: negative control — submitting the rendered form with NO reason does not complete
- Status: EXECUTED
- Input: click `reject-submit` with no radio selected
- Expected: the rejection does not complete and the form is re-rendered
- Actual: **`h1` is not "Rejection recorded"**; all six radios still rendered
- Result: PASS
- Evidence: this is what makes the six positive results below able to fail

### Scenario: all six rejection reasons COMPLETE when driven from the rendered form
- Status: EXECUTED
- Input: **click** each of the six rendered radios, each on its own finding screen, then click `reject-submit`. **No code was posted by hand at any point** — this is the defect pass 21 found, re-tested from the browser
- Expected: six completions, each recorded, none answering `rejection_reason_unknown`
- Actual: **six for six**, every one `clicked: true`, `h1: "Rejection recorded"`, `completed: true`, the chosen reason's label visible on the resulting page

| Reason code | Finding driven | `h1` after submit |
|---|---|---|
| `evidence_insufficient` | /review/ITEM-11500-PA | Rejection recorded |
| `population_not_covered` | /review/ITEM-13800-CP-1 | Rejection recorded |
| `resolution_wrong` | /review/ITEM-18300-OM | Rejection recorded |
| `already_handled` | /review/ITEM-19900-FD | Rejection recorded |
| `data_stale_or_wrong` | /review/ITEM-21400-CP | Rejection recorded |
| `judgement_disagreement` | /review/ITEM-54100-CD | Rejection recorded |

- Result: PASS
- Evidence: ui-reject-recorded-1280-2026-08-04.png; six separate findings used so that six distinct reasons are each driven to completion rather than one item rejected six times

### Scenario: every element the artefact retains is actually VISIBLE on the approval screen
- Status: EXECUTED
- Input: computed geometry, effective opacity and disclosure membership of the eight retained elements
- Expected: all eight rendered, none behind a disclosure, none faint, none empty
- Actual: **eight for eight**, `effOpacity 1`, `visibility visible`, `inDetails false`, heights 93.75–295.7px, text 156–586 chars
- Result: PASS
- Evidence: ui-approval-evidential-region-1280-2026-08-04.png — this is what makes "the approver was shown it" a rendered fact rather than a presence check

### Scenario: AC-F41-24 in the browser — approve is not the only visible terminal action
- Status: EXECUTED
- Input: computed geometry and ancestry of both terminal controls
- Expected: both laid out and visible; the alternative not disclosed, not in a dialog, not behind a link, posting elsewhere
- Actual: approve at `top 1889.70, h 71.25, opacity 1`, action `/proposal/PROP-2026-06-0031/approve`; alternative at `top 1968.95, h 420.47, opacity 1`, action `/review/ITEM-54100-CD/reject`, method `post`; **neither** `inDetails`, `inDialog` or `inAnchor`
- Result: PASS

### Scenario: AC-F41-22 in the browser — three elements co-visible, nothing approves, both levels
- Status: EXECUTED
- Input: `/review/ITEM-54100-CD` rendered as `staff` and as `controller`
- Expected: all three laid out and undisclosed; zero approving forms at either level
- Actual: both personas — `evidence-set h 186.83`, `resolution-row h 218.45`, `rejection-reasons h 368.19`, none `inDetails`; `approving: []`; no `approve-lines` / `approval-control` element at either level
- Result: PASS
- Evidence: ui-finding-no-approve-1280-2026-08-04.png

### Scenario: both viewports were checked (responsive requirement)
- Status: EXECUTED
- Expected: both, since the project records a desktop-web responsive requirement
- Actual: 1280 and 1440 driven for every style/geometry scenario above
- Result: PASS
- Evidence: chromium 148.0.7778.96; 20 screenshots written to `test-evidence/`
