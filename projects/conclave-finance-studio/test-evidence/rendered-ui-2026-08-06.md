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

