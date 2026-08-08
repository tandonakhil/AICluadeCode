# Features: conclave-finance-studio

## Backlog

_Not yet proposed. MVP slice is delegated to the SMEs at gate 3 —
`plan-agent` proposes, `industry-expert` informs from close practice,
`functional-agent` challenges. The human approves feature-by-feature._

## In Development

### `feature/2026-08-08-close-cockpit-home` — persona home page + hamburger nav

**Path B enhancement.** Requested by the human 2026-08-08, on the shipped MVP1 pilot.

| # | Question | Answer |
|---|---|---|
| B1 | Project | conclave-finance-studio |
| B2 | Feature | `close-cockpit-home` |
| B3 | What changes observably | A signed-in user lands on a home page scoped to **them**: a close tracker, and KPIs framed as *their* action items. All navigation moves into a hamburger. |
| B4 | Surfaces | Desktop web only — unchanged. No mobile claim. |
| B5 | Touches data/auth/state? | Reads existing state only. **No new store, no new write path, no new guardrail.** Persona already exists (`state.persona`). |
| B6 | Changes what the AI says or decides? | **No.** A home page composes facts already computed. Guardrails stay at the broker. |
| B7 | Dropped SME to re-engage? | None dropped. `ui-ux-designer` owns the design; `functional-design-agent` issues criteria. |
| B8 | How we know it worked | The human lands on it and can see what the close needs from them tonight without navigating. J3 becomes walkable. |
| B9 | Out of scope | The Period record (A2.6's other A-severity gap). FP&A Inquire mode. Any change to what the detectors compute. |

**This is not new design work.** `UX_KB` A2.2 already specifies a **Close cockpit** as
the default landing — *"Where is this close and what does it need from me tonight?",
per-persona call-list* — and A2.3 records **J3 as Unstartable** without it. A2.6 lists it
under **"A — blocks a whole journey."** The human arrived at it independently.

**Human decision, 2026-08-08:** asked whether the hamburger should hide everything
given their earlier "I just cannot follow anything", they chose **everything in the
hamburger** — no persistent work items in the chrome. Recorded as theirs; the home
page therefore has to carry the work, which raises the bar on it rather than lowering it.

**Status:** Experience Design.


_(none — gate 1)_

## Ready for Release

_None._

## Released

_None._
