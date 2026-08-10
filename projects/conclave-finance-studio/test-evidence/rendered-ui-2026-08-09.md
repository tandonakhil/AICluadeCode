# Test evidence — rendered UI (Playwright / Chromium, web backend), live comparison against approved mockups

**Project:** conclave-finance-studio
**Task:** live-rendered comparison of the running pilot (port 8030) against
`design-review/close-cockpit-2026-08-08/` and `design-review/redesign-2026-08-02/`
— routed here by `ui-ux-designer`, which correctly declined (no browser/HTTP
tool in its grant).
**Date:** 2026-08-09
**Owner:** `test-agent`
**Backend:** Playwright / Chromium (web). RNTL: N/A, no React Native surface.
Maestro + simulator: NOT BUILT (unchanged, 2026-07-26 spike).
**Blocking:** this is an ad hoc verification pass, not one of the project's
seven registered gate suites; findings below are reported for human triage,
not scored pass/fail against a gate.
**Status:** `EXECUTED`

## Process lifecycle

The live instance on **8030 was never stopped** and was not used for any
mutating action (persona switch was performed and then explicitly restored;
tier switch was performed and then explicitly restored). A **second instance
was started on port 8031** (`API_PORT=8031 GES_PORT=8032 .venv/bin/python
backend/pilot.py`) strictly for the two actions that mutate persistent state
(resolving an item, viewing the approval detail) so 8030 would not be touched
by anything not reversible. The 8031 process was killed at the end of this
pass (`kill`, confirmed by a failed `curl` afterward) — nothing was left
running past this turn. The Playwright driver itself ran synchronously inside
single Python invocations; no browser process was left running.

## Currency check — mid-run drift found and corrected

At the very start of this task, `curl http://localhost:8030/` showed
`data-testid="cockpit-h1"` = *"6 item(s) are yours tonight - 5 finding(s) and
1 the system could not settle."* — the expected staff-persona pattern, so the
build was judged current and the walk proceeded.

**However**, by the time the Playwright script's first navigation ran (several
minutes later, after code review), the live process's persona had already
drifted to **controller** (`h1` = *"One act is yours alone tonight."*). `Persona`
is process-wide session state (`state.py` `VIEWER_SESSION_ATTRS`), so this was
someone — plausibly the human — interacting with 8030 while this review was in
progress, not a stale build. It is reported here because it means the main
viewport sweep (drawer, nine destinations, four tracker states, dossier) was
captured under **controller** persona rather than staff, contrary to the
initial assumption. Those files are named accordingly
(`*-controller-persona-during-run.png`, `*-ACTUALLY-CONTROLLER-mislabeled.png`)
rather than silently reported as staff-persona evidence. A corrected,
**verified** staff-persona pass was taken afterward
(`cockpit-staff-VERIFIED-{1280,1440}.png`, `drawer-open-staff-VERIFIED-*.png`),
and the live instance was left exactly as found: staff persona, certified
tier, confirmed by a final `curl` matching the opening one byte-for-byte.

**Conclusion: the build was current throughout.** The drift was a live user
action on the shared singleton, not a stale artefact, and it is fully
reconciled in the evidence set.

## Findings — drift and defects

### 1. Cockpit body content is materially thinner than the approved mockup (drift)
Comparing `cockpit-staff-VERIFIED-1440.png` against
`design-review/close-cockpit-2026-08-08/home-staff.html`:
- The mockup's four/five "What needs you tonight" tiles carry a paragraph of
  supporting detail each (e.g. *"214 detected this run, 6 routed to you. 2
  blast-radius, 1 omission (elevated)... 6 against a routing cap of 12 for
  tonight; the cap is set and enforced at the broker and this page only
  reports it."*). The live build's tiles carry one short sentence each.
- **The mockup has a fifth tile — "A boundary check that could not run" (A9,
  FX/CTA arithmetic)** — the live cockpit renders only **four** tiles; there is
  no boundary-check tile anywhere on the live page (confirmed via
  `document.body.innerText`, not just a screenshot read).
- The mockup's close-tracker checkpoint labels are descriptive ("Subledger
  feeds complete", "Warehouse refresh complete", "Reconciliations complete"…);
  the live build renders generic labels ("day-1 cut-off", "day-2 cut-off"…).
- **The mockup's entire lower half is absent from the live render**: the
  two-column "Coverage achieved so far" / "What we refuse to do" panel and the
  "How tonight's list was reduced from 214 to 6, in the system's own words"
  expandable footer do not exist on the live page at all (confirmed by reading
  full page text — the live page ends after "…does not certify.").
- Not asserted as a defect against any specific AC (that's `functional-design-agent`'s
  or `ui-ux-designer`'s call), but this is a real, material difference between
  what was approved and what ships, not a styling nuance.

### 2. Drawer is a compact `<details>` dropdown, not the approved full-height slide-out panel (drift)
`drawer-open-staff-VERIFIED-1440.png` vs
`design-review/close-cockpit-2026-08-08/menu.html`: the mockup is a full-height
left-edge slide-out with a page scrim and a description under every item
("What you are working. Findings and abstentions routed to you.", etc.). The
live build is a small native `<details>` dropdown anchored under the hamburger
button, bare link labels only, no descriptions, no scrim. This is plausibly
the disclosed consequence of the "no script tag" architecture decision recorded
in `state.py` (native `<details>` is the no-JS mechanism used everywhere else
on this build too), but the mockup was not adapted to reflect it, so the two
disagree on IA presentation, not just polish.

### 3. Genuine functional defect found while walking the approval flow — superseded proposal remains approvable through normal navigation
`state.py` builds `ITEM-54100-CD` / `PROP-2026-06-0031` with `superseded_by`
set, and the code comment at `state.py` (`ReviewItem`, item 3) states this is
carried on the item specifically *"so the proposal screen can REMOVE the
approval path rather than decorate it with a dismissible warning"* (`AC-F41-12`).
In practice:
- `pages.approvals()` builds the row link as plain `href="/approvals/{proposal_id}"`
  with no `?superseded=1`.
- `routes.py`'s `proposal_screen`/`approval_screen` both take `superseded: int = 0`
  as a **query parameter only** — neither route ever reads `item.superseded_by`
  to set that default.
- `pages.proposal()` / `pages.approval_detail()` only render the "This run has
  been superseded — approval is blocked" block when `superseded=True` is
  explicitly passed in.
- **Result, confirmed live**: navigating `/approvals` → click PROP-2026-06-0031
  → `/approvals/PROP-2026-06-0031` renders a fully live, clickable **"Approve
  these 2 lines for export"** button (`approval-detail-1440.png`), and
  `/proposal/PROP-2026-06-0031` (`proposal-detail-1440.png`) actively links
  "Open the approval for PROP-2026-06-0031" — exactly the path the code
  comment says must not exist for this item.
- This is a functional/business-logic gap, not a purely visual one — surfaced
  here because it was directly observable while walking the requested
  "approval flow" screen, but ownership of triage belongs to
  `functional-design-agent` / `code-agent`. Flagging rather than filing a fix.

### 4. Dark theme is not reachable in the served product at all (drift/gap)
No route in `routes.py`/`pages.py` ever calls `chrome.page(..., theme="dark")`
— `theme` defaults to `"light"` everywhere and nothing overrides it. Dark mode
exists only as CSS custom properties (`[data-theme=dark]` in `chrome.py`) and
in the static `design-review` mockups (`theme.js`). **There is no live toggle,
route, or affordance to reach it as a user.** To still validate the dark
tokens compute sanely, I forced `document.documentElement.setAttribute('data-theme','dark')`
via `page.evaluate()` on the live cockpit (`cockpit-forced-dark-1440.png`) —
this is a **synthetic, not a reachable**, check: it proves the CSS variables
resolve to legible values (body background `rgb(14, 16, 19)`, good contrast
throughout) but does not prove a real user can ever see it, because they
cannot. Reported as a gap against "both light and dark theme" rather than a
pass.

### 5. Three-banner distinguishability and footprint — confirmed, with a numeric correction
Measured live via `getComputedStyle` at both 1280 and 1440 (identical at both,
content-width-constrained rather than viewport-constrained):

- **`pilot_strip()`** (`data-testid="pilot-strip"`) — class `pilotstrip` only
  (no `.hatch`). Renders a **fainter** hatch texture:
  `repeating-linear-gradient(..., rgba(120,128,140,.16) 7px 8px)` — this comes
  from `.pilotstrip`'s own `background-image` rule.
- **`transport_topology_strip()`** (`data-testid="transport-topology-state"`)
  — class `pilotstrip hatch`. The `.hatch` rule (declared later in the
  stylesheet, same specificity) overrides `.pilotstrip`'s background-image
  with a **denser** one: `rgba(120,128,140,.28) 6px 7px`.
- **`uncertified_derivation_strip()`** (`data-testid="uncertified-dataset-state"`)
  — also class `pilotstrip hatch`, **pixel-identical styling to banner #2**:
  same border colour, same background colour, same hatch density, same box
  chrome. Confirmed by switching to `?tier=exploration` and capturing all
  three stacked (`cockpit-exploration-three-banners-1440.png`), then restoring
  to certified tier.

**Distinguishability answer:** banners #2 and #3 (topology and uncertified-derivation)
are visually indistinguishable from each other by colour, texture, or chrome —
identical CSS classes produce identical computed styles. Banner #1 differs
from both by a subtler hatch density that is unlikely to register at a glance.
**The only thing that distinguishes any of the three today is reading the bold
lead sentence** ("Pilot build…" / "Pilot topology…" / "Not certified…"). This
satisfies `UX_KB` §3.2's letter (hatch plus a sentence, not colour alone) but
means a reader who skims rather than reads cannot tell banner #3 apart from
#1/#2 — directly relevant to the risk `ui-ux-designer` flagged: once #1 and #2
are removed, #3 alone will look and feel identical to how #2 looked, with
nothing but text to signal the topology disclosure is gone.

**Footprint — does NOT match the ~110px/~12% reported figure.** Measured on
the certified-tier cockpit (the two banners actually in scope for removal,
#1 + #2):
- `pilot-strip`: y=200.59, height=**56.28**
- `transport-topology-state`: y=270.88 (gap of 14.3px below strip 1), height=**102.56**
- **Combined vertical footprint, top of strip 1 to bottom of strip 2: 172.8px**
  (373.44 − 200.59), i.e. **≈173px, ≈19.2% of a 900px viewport** — not ≈110px/≈12%.

The ~110px/12% figure appears to describe an older/different pairing (the
code comment at `chrome.py`'s `provenance()` cites *"The provenance strip plus
the pilot strip occupied ~110px… 12% of a 900px viewport"* — that is
**provenance + pilot_strip**, not pilot_strip + transport_topology_strip). The
two banners actually proposed for removal occupy meaningfully more space than
reported. This should be corrected before the removal decision is finalized on
the smaller figure.

## Screens walked — all reachable, all 200, no console errors

Cockpit (staff, controller), drawer + all nine destinations (`/queue`,
`/approvals`, `/ask`, `/catalogue`, `/monitors`, `/audit`, `/inventory`,
`/refusals`, `/my-probe-history`), close tracker's four states (`?tracker=on_calendar|after_last|no_refresh|absent`),
`/dossier/DOS-2026-06-0412-01` (chrome off, standalone exhibit, renders
cleanly), an approval flow (`/approvals` → `/approvals/{id}`, on 8031),
`/proposal/{id}` (on 8031), and a post-resolution landing (resolving
`ITEM-18300-OM` as R2 on 8031, landing on the `AC-COCKPIT-13..15` continuation
that surfaces the next item inline). All returned HTTP 200. Zero browser
console errors recorded across the sweep. No overlap, no broken layout, no
unstyled flash observed in any screenshot at either viewport.

**No evidence export was triggered** — reaching it required a completed
approval, which I judged out of proportion to attempt on top of the resolution
already recorded on 8031 for this pass; flagging as not attempted rather than
claiming coverage.

---

### Scenario: currency-check - live 8030 is the current build at task start
- Status: EXECUTED
- Input: `curl http://localhost:8030/`, then Playwright `goto('/')`
- Expected: `cockpit-h1` matches "N item(s) are yours tonight" pattern
- Actual: matched at task start; live persona drifted to controller mid-task (see narrative above), fully reconciled and restored
- Result: PASS (with the drift explicitly disclosed, not silently absorbed)
- Evidence: `00-cockpit-1440-ACTUALLY-CONTROLLER-mislabeled.png`, `cockpit-staff-VERIFIED-1440.png`

### Scenario: cockpit-staff vs mockup home-staff.html
- Status: EXECUTED
- Input: `/` at 1280 & 1440, staff persona, vs `design-review/close-cockpit-2026-08-08/home-staff.html`
- Expected: content parity (tiles, checkpoints, coverage/refusal panel, footer)
- Actual: drift found — see Finding 1 (missing 5th tile, missing lower half, generic checkpoint labels)
- Result: FAIL (content drift, not a rendering crash)
- Evidence: `cockpit-staff-VERIFIED-1440.png`, `cockpit-staff-VERIFIED-1280.png`

### Scenario: cockpit-controller renders and differs correctly from staff
- Status: EXECUTED
- Input: switch persona via drawer, `/`
- Expected: distinct h1 for controller ("One act is yours alone tonight.")
- Actual: matched
- Result: PASS
- Evidence: `cockpit-controller-1440.png`

### Scenario: drawer vs mockup menu.html
- Status: EXECUTED
- Input: open `.drawer-wrap > summary` at 1280 & 1440 vs `design-review/close-cockpit-2026-08-08/menu.html`
- Expected: content/IA parity
- Actual: drift found — see Finding 2 (compact dropdown vs full-height slide-out with descriptions)
- Result: FAIL (IA drift)
- Evidence: `drawer-open-staff-VERIFIED-1440.png`, `drawer-open-staff-VERIFIED-1280.png`, `mockup-menu.png` (scratchpad)

### Scenario: nine drawer destinations all reachable, 200, clean
- Status: EXECUTED
- Input: GET each of `/queue`, `/approvals`, `/ask`, `/catalogue`, `/monitors`, `/audit`, `/inventory`, `/refusals`, `/my-probe-history` at 1280 & 1440
- Expected: 200, no console errors, no broken layout
- Actual: all 18 (9 × 2 viewports) returned 200, zero console errors
- Result: PASS
- Evidence: `dest-*-{1280,1440}.png` (18 files)

### Scenario: close tracker's four demo states
- Status: EXECUTED
- Input: `/?tracker=on_calendar|after_last|no_refresh|absent` at 1280 & 1440
- Expected: four distinct, honest states, all 200
- Actual: all 8 returned 200; `after_last` correctly shows all five checkpoints filled with a red "4 close day(s) behind" statement; states render distinctly
- Result: PASS
- Evidence: `tracker-{state}-{1280,1440}.png` (8 files)

### Scenario: dossier exhibit renders standalone and clean
- Status: EXECUTED
- Input: `/dossier/DOS-2026-06-0412-01` at 1280 & 1440, chrome off
- Expected: 200, no navigation chrome, complete evidential sections, no broken layout
- Actual: 200 both viewports; renders as a dense, well-formatted standalone exhibit with all sections (riskiest element, evidence set, in-force panel, precision, reversal, point-of-action revalidation)
- Result: PASS
- Evidence: `dossier-1440.png`, `dossier-1280.png`

### Scenario: approval flow (8031, not 8030) — superseded proposal remains approvable
- Status: EXECUTED
- Input: `/approvals` → `/approvals/PROP-2026-06-0031` → `/proposal/PROP-2026-06-0031`, on the second instance
- Expected (per code comment on `item.superseded_by`): approval path removed
- Actual: live "Approve these 2 lines for export" button present and clickable; proposal screen links "Open the approval" — see Finding 3
- Result: FAIL (functional gap, flagged for `functional-design-agent`/`code-agent`)
- Evidence: `approval-detail-1440.png`, `proposal-detail-1440.png`

### Scenario: post-resolution landing (8031, not 8030)
- Status: EXECUTED
- Input: POST `/review/ITEM-18300-OM/resolve` with `resolution_type=R2`, `explanation`, `clears_by=2026-08`
- Expected: `AC-COCKPIT-13..15` continuation — resolution confirmation plus the next open item inline
- Actual: "Resolution recorded" panel followed immediately by "Continuing your night" and the full next-item review form (21400 GR/IR Clearing), no broken layout
- Result: PASS
- Evidence: `post-resolution-landing-1440.png`, `review-before-resolve-1440.png`

### Scenario: three disclosure banners — distinguishability and combined footprint
- Status: EXECUTED
- Input: computed styles + bounding boxes on `pilot-strip`, `transport-topology-state` (certified tier) and all three (exploration tier, `?tier=exploration` then restored)
- Expected: confirm distinguishability; confirm ~110px/~12% footprint
- Actual: banners #2 and #3 pixel-identical in style (distinguishable only by reading text); combined footprint of the two in-scope banners measured at ≈173px/≈19.2% of a 900px viewport, not ≈110px/≈12% — see Finding 5
- Result: PARTIAL (distinguishability claim holds by text only; footprint claim does not match measurement)
- Evidence: `cockpit-staff-VERIFIED-1440.png`, `cockpit-exploration-three-banners-1440.png`, `results.json` (`banners_certified`, `banners_exploration`)

### Scenario: dark theme reachability and computed-style sanity
- Status: EXECUTED (forced/synthetic — see Finding 4 for why)
- Input: `page.evaluate()` forcing `data-theme=dark` on the live cockpit
- Expected: legible computed colours if it were reachable
- Actual: no live route/toggle reaches dark theme at all (gap); forced check shows CSS tokens resolve to legible values (body bg `rgb(14,16,19)`)
- Result: PARTIAL (visual tokens are sound; reachability is absent)
- Evidence: `cockpit-forced-dark-1440.png`

### Scenario: evidence export
- Status: STATIC ONLY — NOT ATTEMPTED
- Reason: reaching it required a completed approval on top of the resolution already recorded on 8031; judged disproportionate for this pass rather than attempted and left ambiguous
- What would make it EXECUTED: a follow-up pass on a fresh second instance, approving PROP-2026-06-0031 (a non-superseded proposal, since #3 above shows this one shouldn't be approvable) and triggering `/proposal/{id}/export`
