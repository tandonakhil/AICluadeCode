# Test evidence — rendered-UI verification (Playwright / Chromium)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Backend:** Playwright / **Chromium 148.0.7778.96**, driven against the
**SERVED pilot on 8021** — a real HTTP origin, not `page.route()` interception
**Exit code:** 0
**Scenarios: 9 — PASS 8, FAIL 1**

RNTL is **not applicable**: MVP1 is desktop web only (`PROJECT_CONTEXT.md`
header, `PLAN` §9.2 A2). Maestro remains unbuilt and unavailable.

**Process lifecycle.** The pilot was started, driven and reaped inside **each
single command invocation** — four times across this pass. `start_new_session=True`
makes the launcher pid its own process-group id and teardown calls `os.killpg`
on **that group and only that group**. No name-based sweep of any kind was run.
The human's pilot (**pid 39289, port 8030**) was verified alive before and after
every invocation, and 8030/8031 were never probed. `lsof` on 8021 and 8022
returned empty after every teardown.

Coverage: **6 screens × 2 viewports (1280, 1440) = 12 renders**, plus the
dossier opened as a `file://` document. 13 screenshots written.

---

### Scenario: R1 — the dossier opens from a FILE, offline, and fetches nothing
- Status: EXECUTED
- Input: the served dossier bytes saved to disk, opened as `file://` in Chromium
  with every network request recorded
- Expected: no request leaves `file://`; the exhibit is still styled; exactly
  one inert anchor
- Actual: **one request, the document itself.** `risk-band` background resolved
  to `rgb(246, 228, 227)` — still styled with no server. Anchors:
  `["/review/ITEM-21400-CP"]`
- Result: PASS
- Evidence: `ux-dossier-offline-file-2026-08-03.png`. This is the independent
  witness for conflict 1(a) — `ARCHITECTURE_KB` §9.4's fetch-nothing property
  survives the eighth graph edge.

### Scenario: R2 — zero green elements under COMPUTED colour
- Status: EXECUTED
- Input: `getComputedStyle` over every visible element on 12 renders, checking
  `color`, `backgroundColor`, `borderTopColor`, `fill` and `stroke`
- Expected: no element resolves to a green colour anywhere
- Actual: **0 green elements across all 12 renders**
- Result: PASS
- Evidence: the check is on what the engine resolved, not on the token table

### Scenario: R3 — no text below 0.05 effective (compounded) opacity
- Status: EXECUTED
- Input: opacity multiplied up the full ancestor chain for every text-bearing
  element, 12 renders
- Expected: nothing readable-in-source but invisible-on-screen
- Actual: **0 faint text nodes**
- Result: PASS
- Evidence: the compounding-opacity class the rendered-UI contract exists for

### Scenario: R4 — minimum computed font size (advisory)
- Status: EXECUTED
- Input: min computed `fontSize` over every text-bearing element
- Expected: recorded, not asserted — UX-4/`AC-F41-03` is a *relative* check and
  no rule sets an absolute minimum
- Actual: **12.0px on all six screens at both viewports**
- Result: PASS (advisory)
- Evidence: **improved from 10.0px at the previous pass.** The carried advisory
  for `ui-ux-designer` is materially better and is recorded as such.

### Scenario: R5 — `AC-F41-03`: the riskiest figure is the largest computed text
- Status: EXECUTED
- Input: computed `fontSize` of `riskiest-figure` vs every other text element on
  `/review/ITEM-21400-CP`
- Expected: `riskiest-figure` is the maximum on the screen
- Actual: **riskiest 40.0px = largest on screen 40.0px**, against a 28.0px `h1`
- Result: PASS
- Evidence: `ux-finding-desktop-1280-2026-08-03.png`

### Scenario: R6 — every object page names its object in its rendered `<h1>`
- Status: EXECUTED
- Input: rendered `innerText` of the first `<h1>`, 12 renders
- Expected: the finding names the finding — **never its approval state** (the
  pass-17 commit `47735c9`); the run names the run; the agent names the agent
- Actual: finding `"21400 GR/IR Clearing"`; run `"Run RUN-2026-06-0412"`; agent
  `"agent.crossperiod-surveillance"`; approvals `"Approval - PROP-2026-06-0031"`;
  queue `"My queue - 2026-06 Northwind Grid Holdings"`. **No approval vocabulary
  in the finding's `<h1>` at either viewport.**
- Result: PASS
- Evidence: full `h1` map across 12 renders in `scratchpad/rendered17_results.json`

### Scenario: R7 — gold is painted only where the colour law allows
- Status: EXECUTED
- Input: every element the browser painted in **exactly** the resolved `--gold`
  token (`#8A5A17` → `rgb(138, 90, 23)`), read from the document itself
- Expected: gold appears (non-vacuous), on the approval screen, and nowhere
  outside `.btn.approve` / `.seal` / `.card.approved` / `.pull` / `.pull-dot`
- Actual: **28 gold-painted elements across 12 renders. Every one is `.pull`
  (stroke), `.pull-dot` (fill) or `.btn approve` (color + border). Zero
  offenders.** The approve control is gold on `/approvals` at both viewports and
  on no other screen.
- Result: PASS
- Evidence: this is the independent witness for the gold conflict — the unit
  suite asserts the law by parsing `chrome.STYLESHEET` as **text**; this asserts
  it on what Chromium actually painted. The scenario carries a **non-vacuity
  guard** after its first form passed on an empty set (see
  `mutation-tests-2026-08-03.md` M6).

### Scenario: R8 — screenshots captured as evidence
- Status: EXECUTED
- Input: full-page screenshots, 6 screens × 2 viewports + the offline dossier
- Expected: 13 files under `test-evidence/`
- Actual: 13 written, all present on disk
- Result: PASS
- Evidence: `ux-{queue,approvals,run-report,finding,agent,readiness}-desktop-{1280,1440}-2026-08-03.png`
  and `ux-dossier-offline-file-2026-08-03.png`

### Scenario: R9 — FINDING: the sidebar context line is unstyled and lays out one word per line
- Status: EXECUTED
- Input: bounding-box measurement of every text-bearing element, 8 renders
  across 4 screens × 2 viewports
- Expected: the sidebar identity block lays out as a lockup
- Actual: **the entity/period/close-day context line renders in a 67.5px-wide,
  116.25px-tall box at x=140 — roughly one word per line — on EVERY screen at
  BOTH viewports.**
  Root cause, found by reading the stylesheet after the measurement: the rule is
  scoped **`.brand .ctx`**. Pass 17's A2.8 identity layer replaced the `.brand`
  block with `.lockup` — `chrome.lockup()`'s own docstring says *"Replaces the
  plain `.brand` text block"* — but the `.ctx` selector was not re-scoped.
  **`.lockup .ctx` has no rule**, so the span is an unstyled min-content flex
  child of a `display:flex; align-items:center` row inside a ~160px sidebar.
- Result: **FAIL**
- Evidence: visible top-left in `ux-queue-desktop-1280-2026-08-03.png` and
  `ux-approvals-desktop-1440-2026-08-03.png` as "Northwind / Grid / Holdings - /
  2026-06 - / Day 3" stacked beside the Conclave wordmark. Measured:
  `{"text": "Northwind Grid Holdings - 2026-06 - Day ", "cls": "ctx",
  "w": 67.53, "h": 116.25, "x": 140.31, "y": 14}`, identical at 1280 and 1440.
  **Invisible to every non-rendering check**: the class is emitted, the string
  `.ctx` *does* exist in the stylesheet so a grep passes, the page returns 200
  and contains the right text. `test_ui_brand.py`'s 32 new scenarios do not
  catch it, and neither does the 194-scenario `ux` suite.

### Scenario: R10 — the "clipped pill" was this agent's misreading, not a defect
- Status: EXECUTED
- Input: the `PRESENT ANOMAL` pill in the queue screenshot looked truncated;
  measured with a `Range` rect against the pill box rather than eyeballed
- Expected: confirm or refute before reporting
- Actual: **refuted.** `'Present anomaly'` paints **136.4px inside a 152.4px
  box**, overflow −1.0px; every kind- and risk-pill on the queue has negative
  overflow at both viewports. Nothing is clipped.
- Result: PASS (no defect)
- Evidence: recorded because a visual impression that measurement refutes is
  worth recording — the same discipline that made R9 reportable
