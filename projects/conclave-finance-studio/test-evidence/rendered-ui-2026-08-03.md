# Test evidence — rendered-UI verification (Playwright / Chromium)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Backend:** Playwright / **Chromium 148.0.7778.96**, driven against the
**SERVED pilot on 8021** over a real socket — not `page.route()` interception,
not `TestClient`
**Exit code:** 0
**Scenarios: 8 — PASS 6, FAIL 1, INCONCLUSIVE 1**

RNTL is **not applicable**: MVP1 is desktop web only. Maestro + simulator
remains unbuilt and unavailable on this machine (2026-07-26 toolchain spike),
so the deeper native backend is still future and nothing here depends on it.

**Coverage:** 6 screens × 2 viewports (1280, 1440) = **12 renders**, plus the
four absent-agent pages and the inventory disclosure at full page. **14
screenshots written.**

## Process lifecycle

The pilot was started, driven and reaped **inside one command invocation**.
`start_new_session=True` makes the launcher its own process-group id; teardown
calls `os.killpg` on **that group and only that group**. **No name-based sweep
of any kind was run.**

- the human's pilot, **pid 50367 on port 8030**: verified alive **before** and
  **after** — `alive BEFORE: True`, `alive AFTER: True`
- 8030 and 8031 were never probed, never connected to, never signalled
- `lsof` on 8021 and 8022 after teardown: **empty**

---

### Scenario: R1 — **the `.ctx` measurement, re-measured in Chromium**
- Status: EXECUTED
- Input: `getBoundingClientRect()` + `getComputedStyle()` on `.lockup .ctx`,
  on 6 screens × 2 viewports, against the served pilot
- Expected: a full-width line under the lockup row, not a third flex item
- Actual: **167.00 px × 48.56 px at x=14.00, y=55.88 — identical on all six
  screens at BOTH viewports.**
  - `display: block`; parent is `.lockup` with `parentDisplay: block`
  - `.lockup` children are exactly `['lockup-row', 'ctx']`; `.lockup-row`
    children are exactly `['glyph mark', 'wm']`
  - `.lockup` box 195 × 102.44; `.lockup-row` box 167 × 34.88
  - text `'Northwind Grid Holdings - 2026-06 - Day 3'`, laid out over
    **3 visual lines**, widest line **139.12 px** inside the 167 px column
  - computed: `12px`, `rgb(94, 100, 110)`, weight 500, `uppercase`,
    letter-spacing `0.72px`, line-height `16.2px`, margin-top `7px`
- Result: **PASS**
- Evidence: `ui-queue-1280-2026-08-03.png` (visible top-left as
  "NORTHWIND GRID HOLDINGS - 2026-06 - DAY 3"), and the same at
  `ui-queue-1440`, `ui-approvals-*`, `ui-ask-*`, `ui-inventory-*`,
  `ui-audit-*`, `ui-catalogue-*`.
  **Independent confirmation of `code-agent`'s reported 167px × 48.6px.** For
  contrast, the pass-17 defect measured **67.53 × 116.25** — a min-content flex
  child. One correction to the phrasing: it is a full-width *block*, wrapping
  to three lines; "a full-width line" is loose but the layout is right.

### Scenario: R2 — zero green elements under COMPUTED colour
- Status: EXECUTED
- Input: every visible element on 12 renders, testing computed `color` and
  `backgroundColor` against `g > r+18 && g > b+18 && g > 70`
- Expected: none
- Actual: **0**
- Result: PASS
- Evidence: `render_out.json` `"green": []` across all 12 renders

### Scenario: R3 — no text below 0.5 COMPOUNDED opacity
- Status: EXECUTED
- Input: for every leaf text node, the product of `opacity` up the whole
  ancestor chain — the compounding-opacity class of defect
- Expected: none faint
- Actual: **0 across all 12 renders**
- Result: PASS
- Evidence: `render_out.json` `"faint": []`

### Scenario: R4 — no horizontal overflow at either viewport
- Status: EXECUTED
- Input: `scrollWidth − clientWidth` on 12 renders
- Expected: 0
- Actual: **{0}** — a single distinct value across all 12
- Result: PASS
- Evidence: `render_out.json` `meta[].overflowX`

### Scenario: R5 — every screen names its object in its rendered `<h1>`
- Status: EXECUTED
- Input: the accessibility-relevant `h1` innerText on each screen
- Expected: one per screen, naming the object
- Actual: `/queue` → *"My queue - 2026-06 Northwind Grid Holdings"*;
  `/approvals` → *"Approvals"*; `/ask` → *"What should the agent do?"*;
  `/audit` → *"Audit - 2026-06 Northwind Grid Holdings"*; `/catalogue` →
  *"Certified dataset catalogue"*; `/inventory` → *"Agent and principal
  inventory"*. Landmarks `('nav', 'main')` on every render
- Result: PASS
- Evidence: `render_out.json` `meta[].h1`, `meta[].landmarks`

### Scenario: R6 — the `/inventory` disclosure, as a reader actually sees it
- Status: EXECUTED
- Input: the rendered `/inventory` at 1280, reading the real DOM
- Expected: four absent agents named, `AC-F5-02` stated NOT met, every lineage
  row labelled, and the unqualified sentence gone
- Actual: **all four named** (`agent.crossperiod-surveillance`,
  `agent.omission-detector`, `agent.anomaly-detect`, `agent.fidelity-check`);
  the notice reads *"This inventory is INCOMPLETE as a list of agents that have
  acted… AC-F5-02 … is NOT met by this build and is recorded as unmet rather
  than reported as satisfied"*; **11 of 11** `lineage-view` rows carry
  `data-complete="false"` and `data-scope="decision_ledger"`; the unqualified
  sentence is **absent**
- Result: PASS
- Evidence: `ui-inventory-disclosure-1280-2026-08-03.png`

### Scenario: R7 — **FINDING: the sentence removed from `/inventory` survives on the four pages `/inventory` links to**
- Status: EXECUTED
- Input: the four `/evidence/agent/<id>` pages — the ones the `/inventory`
  disclosure links each absent agent to — rendered in Chromium, reading
  `document.body.innerText`
- Expected: none of the four repeats a claim the build records as unmet
- Actual: **all four carry it.**
  `{"agent.crossperiod-surveillance": {"unqualified": true, "discloses": true},
  "agent.omission-detector": {...true, true}, "agent.anomaly-detect":
  {...true, true}, "agent.fidelity-check": {...true, true}}`
  The page reads, in the subtitle directly under the `<h1>`:
  *"An agent that can act is an agent that is listed."*
  — and then, four lines later:
  *"This agent authored findings in this run and has no entry in the principal
  registry under this id."*
- Result: **FAIL**
- Evidence: `ui-agent-page-absent-agent-1280-2026-08-03.png`.
  Register 34's wording is literally accurate — the sentence *is* gone "from
  that screen" — but the same entry also records that `/inventory` **links each
  absent agent to its agent page**, which is precisely the path that carries a
  reader from the disclosure into its contradiction. The scenario that guards
  this asserts `not in document.markup` for `/inventory` **only**
  (`test_unclaimed_criteria.py:421`); no scenario anywhere asserts it for any
  other surface. Full detail in `functional-2026-08-03.md` §"Finding 1".

### Scenario: R8 — the gold colour law
- Status: **INCONCLUSIVE — NOT A PASS**
- Input: computed `color`/`backgroundColor` tested against a gold predicate
  `r > 150 && g > 110 && b < 110 && r >= g`
- Expected: gold painted only where the colour law allows
- Actual: **0 elements matched the predicate — and the predicate is wrong.**
  The light-theme token is `gold: #8A5A17` = `rgb(138, 90, 23)`, which fails
  `r > 150`. A sweep that matches nothing proves nothing
- Result: **INCONCLUSIVE.** Recorded as inconclusive rather than as "0
  violations found", which is the same vacuous-pass error this agent audits
  other suites for
- Evidence: `tokens.py:75 "gold": "#8A5A17"`. The colour law is the `ux`
  suite's territory and its 194 scenarios are green (`ux-2026-08-03.md`); this
  independent witness simply did not run correctly and is not offered as one
