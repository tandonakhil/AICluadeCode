# Test evidence — rendered-UI verification (Playwright / Chromium, web backend)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**13 scenarios, 13 pass, 0 fail, 0 inconclusive.** Chromium **148.0.7778.96**,
driven against the **served** pilot on 8021 at two viewports (1280 and 1440),
each of the two invocations starting, driving and reaping its own pilot **inside
one command invocation**. The human's pilot (pid 59422, 8030) was alive before
and after both.

**16 screenshots** in this directory, all captured this pass.

## The pass-18 gold sweep was INCONCLUSIVE. It is now conclusive.

Last pass's gold predicate was `r > 150`, which matches neither the light token
`#8A5A17` (138, 90, 23) nor its ground `#FBF1DF`. It matched nothing and proved
nothing, and was recorded as inconclusive rather than as "0 violations". The
predicate is now the **four exact shipped token values** — `#8A5A17`, `#FBF1DF`,
`#E0A94E`, `#2A2317` — read from `backend/app/ui/tokens.py`, and the sweep now
also reads `stroke` and `fill`, not only `color` and `backgroundColor`.

**It fires.** A positive control run proves the predicate can say YES before its
silence is read as evidence.

---

### Scenario: the gold predicate can say YES (positive control)
- Status: EXECUTED
- Input: `/approvals/PROP-2026-06-0031` at 1280 and 1440, computed styles over
  `body *, body svg *`
- Expected: gold on the Approve control — the brand law's "a human decision" —
  and on the brand mark
- Actual: **`BUTTON.btn approve` → `color=rgb(138,90,23)`,
  `backgroundColor=rgb(251,241,223)`, `borderTopColor=rgb(138,90,23)`, text
  "Approve these 2 lines for export"; `circle.pull-dot` → `fill=rgb(138,90,23)`**
- Result: PASS
- Evidence: `ui-approval-gold-1280-2026-08-03.png`,
  `ui-approval-gold-1440-2026-08-03.png`

### Scenario: gold appears NOWHERE a human decision is not being made
- Status: EXECUTED
- Input: `/queue` and `/inventory` at both viewports, same predicate
- Expected: only the brand mark
- Actual: **`circle.pull-dot` only, on every screen. No `.btn.approve`, no
  `.seal`, no `.card.approved` outside the approval screen**
- Result: PASS

### Scenario: no green anywhere on the served surface
- Status: EXECUTED
- Input: computed-style sweep over six screens × two viewports
- Expected: zero elements
- Actual: **0**
- Result: PASS
- Evidence: corroborated by smoke S17 over the served bytes

### Scenario: no text is rendered at compounded opacity below 0.5
- Status: EXECUTED
- Input: for every leaf element with text, the product of `opacity` up the whole
  ancestor chain — the compounding-opacity defect class
- Expected: zero
- Actual: **0 elements below 0.5**
- Result: PASS

### Scenario: the `.ctx` lockup defect stays fixed, measured not asserted
- Status: EXECUTED
- Input: `getBoundingClientRect` + computed styles on `.lockup .ctx`, six
  screens × two viewports
- Expected: identical geometry everywhere, `display:block`, parent `.lockup`
- Actual: **167.00 × 48.56 px at x=14.00, y=55.88, `lineCount=3`,
  `display=block`, parent `.lockup` with `display:block` — identical on all
  twelve measurements.** `.lockup` children exactly `['lockup-row', 'ctx']`;
  `.lockup-row` children exactly `['glyph mark', 'wm']`. Text
  "Northwind Grid Holdings - 2026-06 - Day 3"
- Result: PASS
- Evidence: pass 17's defect measured 67.53 × 116.25

### Scenario: no horizontal overflow at either viewport
- Status: EXECUTED
- Expected: `scrollWidth - clientWidth == 0`
- Actual: **`[0]`** — one distinct value across all twelve measurements
- Result: PASS

### Scenario: every screen has exactly one `h1` and the landmark pair
- Status: EXECUTED
- Actual: one `h1` per screen, distinct per screen (`My queue…`, `Approvals`,
  `What should the agent do?`, `Audit - 2026-06 Northwind Grid Holdings`,
  `Certified dataset catalogue`, `Agent and principal inventory`); landmarks
  `('nav', 'main')` on all twelve
- Result: PASS

### Scenario: the four agent pages do NOT render the unqualified claim
- Status: EXECUTED
- Input: `document.body.innerText` on each `/evidence/agent/<id>`, in the browser
- Expected: `unqualified: false`, `discloses: true` on all four
- Actual: **all four `unqualified=false`, `discloses=true`, `h1` = its own
  principal id**
- Result: PASS
- Evidence: `ui-agent-page-absent-agent-1280-2026-08-03.png`

### Scenario: the four `/inventory` links are CLICKED and land on that agent
- Status: EXECUTED
- Input: for each of the four, reload `/inventory`, read the row's
  `data-principal`, **click the anchor**, read the rendered `h1`
- Expected: four clicks, four correct landings
- Actual: **4/4 `lands_on_that_agent: true`** —
  `agent.crossperiod-surveillance`, `agent.omission-detector`,
  `agent.anomaly-detect`, `agent.fidelity-check`, each URL and `h1` matching its
  row
- Result: PASS
- Evidence: this is the rendered-backend form of the fourth finding; the
  mutation form is in `mutation-tests-2026-08-03.md` M3/M3b

### Scenario: the `/inventory` disclosure renders with all four agents named
- Status: EXECUTED
- Actual: `absent` = the four ids; the notice reads *"This inventory is
  INCOMPLETE … 4 agent(s) authored findings in this run and appear in no row
  above"* and ends *"AC-F5-02 … is NOT met by this build and is recorded as
  unmet rather than reported as satisfied"*
- Result: PASS
- Evidence: `ui-inventory-disclosure-1280-2026-08-03.png` (full page)

### Scenario: the UNKNOWN population answer is actually visible, not merely present
- Status: EXECUTED
- Input: computed styles and box of `[data-testid=unregistered-actors-answer]`
- Expected: rendered, visible, not faded, not zero-sized
- Actual: **`data-computable="false"`, `display:block`, `visibility:visible`,
  **compounded opacity 1.0**, 1036 × 148.48 px.** Text begins
  "AGENTS ACTING UNDER AN UNPUBLISHED ID / UNKNOWN Which agents acted under an
  id this registry does not publish is UNKNOWN here; it is not none…"
- Result: PASS
- Advisory, not a failure: it sits at **y = 7601.7 px**, near the foot of a very
  long page. A reader must scroll ~7,600 px to meet the build's own answer to the
  population question. For `ui-ux-designer`

### Scenario: every lineage row renders INCOMPLETE with its scope
- Status: EXECUTED
- Actual: **11 rows, every one `data-complete="false"` and
  `data-scope="decision_ledger"`**
- Result: PASS

### Scenario: both viewports were checked (responsive requirement)
- Status: EXECUTED
- Expected: not a desktop-only pass
- Actual: **1280 and 1440 on all six screens plus the gold control.** Every
  measurement identical between the two
- Result: PASS
- Note: 1280 and 1440 are both desktop widths. This project's Decisions Log
  records a **desktop reviewer surface**, not a responsive web app, so two
  desktop widths is the requirement rather than a partial pass. Recorded
  explicitly so a later reader does not have to infer it

---

## Native backend (RNTL)

**NOT APPLICABLE — not `STATIC ONLY`.** This project has no React Native
surface; the product is a server-rendered web application (`backend/app/ui`,
`ARCHITECTURE_KB` §9.4). There is no native component for RNTL to render, so
there is nothing here that RNTL would catch and that Playwright cannot.

## Deeper native backend (Maestro + simulator)

Still not built, and still not needed here for the same reason.
