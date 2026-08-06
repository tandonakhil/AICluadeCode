# Test evidence - rendered UI (Playwright / Chromium, web backend), gate 11

**Project:** conclave-finance-studio
**Gate:** 11 - rendered-UI verification, web backend
**Date:** 2026-08-06
**Commit under test:** `dev` @ **`c68ad84`**, working tree clean
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**8 scenarios, 8 pass, 0 fail.** Executed in real Chromium, driven synchronously
inside one command invocation; the browser and the pilot both exited before the
turn ended. Two viewports, 1280 and 1440.

**Why this ran at all rather than being carried forward.** The last rendered-UI
run was 2026-08-04 at `7757e0d`. Pass 25's D1 has since added
`transport-topology-state` to **every screen this build serves**. A rendered
suite carried forward on a run that predates a new element on every screen is
the carried-forward static pass the contract forbids, so it was re-run.

**Native backends.** RNTL: **N/A** - no React Native surface in MVP1.
Maestro + simulator: **NOT BUILT** - no simulator or emulator on this machine
(2026-07-26 toolchain spike, unchanged).

## What R4 and R5 establish that no source grep could

`AC-F41-03` is *"the riskiest element at the largest computed font size"*. Only a
browser can answer that, because the size exists only as a CSS rule.

- **R4 (live shell-off exhibit):** `riskiest-figure` computes to **40px**, which
  is the strict maximum on the page, and it is the **only** element at that size.
  Six distinct sizes render. The criterion is satisfied and checkable.
- **R5 (the export artefact, opened as a local file exactly as an auditor
  would):** `riskiest-figure` is **absent**, and 133 measured elements render at
  just **two** computed sizes - 24px and 16px, the browser's own `<h*>` and body
  defaults. There is no typographic emphasis to evaluate.

## R6 - OBSERVED, not asserted: the artefact is worse than "missing an emphasis"

Reading the R5 screenshot rather than only its measurements
(`ui-export-artefact-unstyled-1280-2026-08-06.png`) shows the missing stylesheet
costs the artefact more than `AC-F41-03`. Every key/value pair renders with **no
separator between label and value**, because the separation was a CSS box and
nothing else:

```
Proposalno proposal for this finding
ItemITEM-21400-CP
Account21400 GR/IR Clearing
Amount312,480.00
Authoragent.crossperiod-surveillance
Dataset versiongl_balances vFIXTURE-2026.06.03-a
```

`Amount312,480.00` is what a reader with no application login actually receives
for a currency figure in an evidential record. This is **not** asserted as a
failing scenario here - no acceptance criterion in this product covers it, and
inventing one at gate 11 is not this agent's call - but it is recorded because
it is a rendering defect that only a rendering backend can see, it materially
affects the artefact `AC-F1-04` is about, and it strengthens register 35 /
`ARCHITECTURE_KB` §25.4 well beyond the single criterion that ruling names.
Referred to `functional-design-agent` and `solution-architect`.

**Evidence:** `/Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-export-artefact-unstyled-1280-2026-08-06.png`

---

### Scenario: R1-1280 - transport-topology-state renders visibly at 1280px, computed not asserted
- Status: EXECUTED
- Input: GET /queue in Chromium at 1280x900
- Expected: exactly one, opacity 1, visible, non-zero box, not occluded
- Actual: count=1 computed={"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1036, "h": 122.703125, "occluded": false}
- Result: PASS
- Evidence: 

```
{"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1036, "h": 122.703125, "occluded": false}
```


### Scenario: R2-1280 - pilot-strip renders visibly at 1280px, computed not asserted
- Status: EXECUTED
- Input: GET /queue in Chromium at 1280x900
- Expected: exactly one, opacity 1, visible, non-zero box, not occluded
- Actual: count=1 computed={"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1036, "h": 56.28125, "occluded": false}
- Result: PASS
- Evidence: {"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1036, "h": 56.28125, "occluded": false}

### Scenario: R3-1280 - screenshot of the served queue at 1280px
- Status: EXECUTED
- Input: full viewport capture
- Expected: file written
- Actual: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-topology-strip-1280-2026-08-06.png (279833 bytes)
- Result: PASS
- Evidence: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-topology-strip-1280-2026-08-06.png

### Scenario: R1-1440 - transport-topology-state renders visibly at 1440px, computed not asserted
- Status: EXECUTED
- Input: GET /queue in Chromium at 1440x900
- Expected: exactly one, opacity 1, visible, non-zero box, not occluded
- Actual: count=1 computed={"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1132, "h": 102.5625, "occluded": false}
- Result: PASS
- Evidence: {"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1132, "h": 102.5625, "occluded": false}

### Scenario: R2-1440 - pilot-strip renders visibly at 1440px, computed not asserted
- Status: EXECUTED
- Input: GET /queue in Chromium at 1440x900
- Expected: exactly one, opacity 1, visible, non-zero box, not occluded
- Actual: count=1 computed={"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1132, "h": 56.28125, "occluded": false}
- Result: PASS
- Evidence: {"opacity": "1", "visibility": "visible", "display": "block", "color": "rgb(74, 79, 88)", "background": "rgb(241, 241, 239)", "w": 1132, "h": 56.28125, "occluded": false}

### Scenario: R3-1440 - screenshot of the served queue at 1440px
- Status: EXECUTED
- Input: full viewport capture
- Expected: file written
- Actual: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-topology-strip-1440-2026-08-06.png (287280 bytes)
- Result: PASS
- Evidence: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-topology-strip-1440-2026-08-06.png

### Scenario: R4 - AC-F41-03 IN A REAL BROWSER: the riskiest element computes to the largest font size on the exhibit
- Status: EXECUTED
- Input: open /dossier/DOS-2026-06-0412-01 in Chromium and read getComputedStyle().fontSize on every visible element
- Expected: the riskiest-figure's computed size is the strict maximum on the page
- Actual: riskiest=40px page_max=40px elements_at_max=['riskiest-figure']
- Result: PASS
- Evidence: {"riskiest_figure_px": 40, "page_max_px": 40, "at_max": ["riskiest-figure"], "distinct_sizes": [40, 28, 21, 15, 13, 12]}

### Scenario: R5 - AC-F41-03 IS UNCHECKABLE IN THE ARTEFACT, proven in the browser an auditor would use
- Status: EXECUTED
- Input: open the export's rendered_view as a local file in Chromium
- Expected: the riskiest element is absent and the document renders at essentially one uniform computed size - nothing to compare
- Actual: riskiest_figure_elements=0 distinct_computed_sizes=[24, 16]
- Result: PASS
- Evidence: 

```
{"riskiest_figure_present": 0, "distinct_computed_font_sizes": [24, 16], "elements_measured": 133, "note": "the live exhibit renders 7 distinct sizes with a 40px maximum; the artefact renders 2"}
```


---

# RE-RUN 2 — rendered UI at `dev` @ `b447a11` (pass 26), Playwright / Chromium 148

**Commit under test:** `b447a11` · **Owner:** `test-agent` · **Blocking:** yes
**Status:** `EXECUTED` · **Result: 11 scenarios, 11 pass, 0 FAIL.**
**Backend:** Playwright / Chromium (web). RNTL (native) is **N/A** — this build
has no React Native surface. Maestro + simulator remains **NOT BUILT**.

**Re-run, not carried forward from the earlier run in this file.** Pass 26
changed what the exhibit renders, so a rendered-UI verdict recorded before it
describes a different tree.

**Why this suite matters for THIS fix specifically.** Pass 26's claim is about
what a reader **sees** on the shell-off exhibit. HTML containing the sentence is
not that claim: a strip can be in the DOM and be `display:none`, be occluded by
a later element, be scrolled out, or be invisible through **compounded** parent
opacity. Each scenario therefore reads the browser's own computed values,
including effective opacity walked up the whole ancestor chain, and asserts the
four phrases against `inner_text` — **the text the browser rendered**, not the
markup it was given. Two viewports, 1280 and 1440.

**Process lifecycle:** the pilot and the browser were both started and both torn
down inside the single command invocation, the pilot reaped by process group.
Nothing was left running. `CONCLAVE_VAR_DIR` pointed at a copy of `dev/var`.

## The scenarios

### Scenario: R6-1280 - THE FIX IN A REAL BROWSER: the shell-off exhibit's provenance strip is VISIBLE and READABLE at 1280px - computed, not asserted from source
- Status: EXECUTED
- Input: goto /dossier/DOS-2026-06-0412-01 at 1280px; read computed styles, effective (compounded) opacity, occlusion, viewport position and the rendered inner_text
- Expected: visible, effective opacity > 0.5, not occluded, in viewport, non-zero box, all four phrases in the TEXT THE BROWSER RENDERED
- Actual: visible=True eff_opacity=1.000 occluded=False in_viewport=True box_h=56.3 style={"display": "block", "visibility": "visible", "opacity": "1", "color": "rgb(74, 79, 88)", "backgroundColor": "rgb(241, 241, 239)", "fontSize": "13px"} phrases={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
rendered text: Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a posting or an assurance conclusion about a real ledger.
```

### Scenario: R7-1280 - the exhibit's provenance disclosure is reachable in the ARIA SNAPSHOT and by user-visible-text query at 1280px, not only in the DOM
- Status: EXECUTED
- Input: body.aria_snapshot() and get_by_text(phrase) on /dossier/DOS-2026-06-0412-01
- Expected: every required phrase in the aria snapshot AND visible to a text query
- Actual: aria={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true} visible_text={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
- main:
  - text: Entity Northwind Grid Holdings Period 2026-06 Close day Day 3 Data 1 close day(s) behind the close clock
  - group: What "1 close day(s) behind the close clock" means, and where these figures came from
  - text: Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a postin
```

### Scenario: R8-1280 - screenshot of the shell-off exhibit at 1280px
- Status: EXECUTED
- Input: page.screenshot on /dossier/DOS-2026-06-0412-01
- Expected: an image is written
- Actual: written: ui-dossier-provenance-strip-1280-2026-08-06.png (198842 bytes)
- Result: PASS
- Evidence: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-dossier-provenance-strip-1280-2026-08-06.png

### Scenario: R1-1280 - transport-topology-state renders visibly on /queue at 1280px, computed not asserted
- Status: EXECUTED
- Input: goto /queue at 1280px
- Expected: visible, effective opacity > 0.5
- Actual: visible=True eff_opacity=1.000
- Result: PASS
- Evidence:

```
Pilot topology - the guardrail broker is running inside this process. Every broker fact on this screen - each eligibility, decision, refusal and routing answer - was obtained over the in-process trans
```

### Scenario: R2-1280 - pilot-strip renders visibly on /queue at 1280px and the screen and the exhibit say the SAME sentence
- Status: EXECUTED
- Input: goto /queue at 1280px
- Expected: visible, effective opacity > 0.5, all four phrases
- Actual: visible=True eff_opacity=1.000 phrases={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a posting or an assurance conclusion about a real ledger.
```

### Scenario: R6-1440 - THE FIX IN A REAL BROWSER: the shell-off exhibit's provenance strip is VISIBLE and READABLE at 1440px - computed, not asserted from source
- Status: EXECUTED
- Input: goto /dossier/DOS-2026-06-0412-01 at 1440px; read computed styles, effective (compounded) opacity, occlusion, viewport position and the rendered inner_text
- Expected: visible, effective opacity > 0.5, not occluded, in viewport, non-zero box, all four phrases in the TEXT THE BROWSER RENDERED
- Actual: visible=True eff_opacity=1.000 occluded=False in_viewport=True box_h=56.3 style={"display": "block", "visibility": "visible", "opacity": "1", "color": "rgb(74, 79, 88)", "backgroundColor": "rgb(241, 241, 239)", "fontSize": "13px"} phrases={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
rendered text: Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a posting or an assurance conclusion about a real ledger.
```

### Scenario: R7-1440 - the exhibit's provenance disclosure is reachable in the ARIA SNAPSHOT and by user-visible-text query at 1440px, not only in the DOM
- Status: EXECUTED
- Input: body.aria_snapshot() and get_by_text(phrase) on /dossier/DOS-2026-06-0412-01
- Expected: every required phrase in the aria snapshot AND visible to a text query
- Actual: aria={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true} visible_text={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
- main:
  - text: Entity Northwind Grid Holdings Period 2026-06 Close day Day 3 Data 1 close day(s) behind the close clock
  - group: What "1 close day(s) behind the close clock" means, and where these figures came from
  - text: Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a postin
```

### Scenario: R8-1440 - screenshot of the shell-off exhibit at 1440px
- Status: EXECUTED
- Input: page.screenshot on /dossier/DOS-2026-06-0412-01
- Expected: an image is written
- Actual: written: ui-dossier-provenance-strip-1440-2026-08-06.png (202090 bytes)
- Result: PASS
- Evidence: /Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/conclave-finance-studio/test-evidence/ui-dossier-provenance-strip-1440-2026-08-06.png

### Scenario: R1-1440 - transport-topology-state renders visibly on /queue at 1440px, computed not asserted
- Status: EXECUTED
- Input: goto /queue at 1440px
- Expected: visible, effective opacity > 0.5
- Actual: visible=True eff_opacity=1.000
- Result: PASS
- Evidence:

```
Pilot topology - the guardrail broker is running inside this process. Every broker fact on this screen - each eligibility, decision, refusal and routing answer - was obtained over the in-process trans
```

### Scenario: R2-1440 - pilot-strip renders visibly on /queue at 1440px and the screen and the exhibit say the SAME sentence
- Status: EXECUTED
- Input: goto /queue at 1440px
- Expected: visible, effective opacity > 0.5, all four phrases
- Actual: visible=True eff_opacity=1.000 phrases={"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence:

```
Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a posting or an assurance conclusion about a real ledger.
```

### Scenario: R9 - no control inside the exhibit's provenance strip dismisses it - a disclosure the reader can turn off is not a disclosure
- Status: EXECUTED
- Input: count interactive descendants of pilot-strip on the exhibit
- Expected: zero
- Actual: interactive_descendants=0
- Result: PASS
- Evidence: 
