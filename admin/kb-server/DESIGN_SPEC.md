# MAS Knowledge Base — Redesign Specification
**"THE SIGNAL PATH"** — v1.0 · ui-ux-designer · target file: `admin/kb-server/templates/index.html`

Reference bar set by human: https://heavn-one.webflow.io/ ("build something like this or even better").
Research findings on the reference: near-black canvas, warm amber gradient glows (light IS the brand),
massive bold display typography, full-width narrative scroll with alternating rhythm, generous whitespace,
smooth scroll-driven reveals, benefits-first copy.

---

## 1. Design Thesis

**heavn sells light, so light is the site. MAS sells orchestrated flow through gates — so the site IS a signal traveling through a machine.**

The one idea: **a single luminous thread of work moving through apertures.** Every project in MAS is a signal that enters the pipeline, passes through nine gates, gets touched by agents, and exits as a deployed system. The page dramatizes exactly that:

- A continuous glowing **signal line** runs the entire vertical length of the page. Scrolling *is* the journey through the pipeline. Your scroll position is the work item's position.
- Gates are rendered as **apertures** — vertical slits the light passes through. Light on one side is raw/diffuse; after the slit it is focused. That's what a gate does: it doesn't stop work, it disciplines it.
- Agents appear as **irises** — small conic-gradient discs that "open" when active. Eighteen instruments in one machine.

If a visual element can't be explained as signal, aperture, or iris, it doesn't ship.

**Commit to dark-only.** Delete the light theme and the theme toggle. A "signal on black" identity dies at #f6f4ef.

## 2. Color System

Two-hue world: **ember** (developers) and **arc** (admins). Tab switch = the whole room changes temperature.

```css
--void:    #030405;   /* page canvas */
--floor:   #0a0c10;   /* section alternation band */
--surface: #10131a;   /* raised panels */
--surface2:#161b26;   /* hover / inset wells */
--hair:    rgba(235,240,255,0.07);
--hair-hi: rgba(235,240,255,0.16);
--ink:      #f4f2ec;
--ink-dim:  #a8abb8;
--ink-faint:#5c6070;
/* Ember (Developers) */
--accent:      #f5a83c;  --accent-hot: #ffd9a0;  --accent-deep: #b4530f;
--glow: rgba(245,168,60,0.16);  --glow-core: rgba(255,217,160,0.55);
/* Arc (Admins) */
--accent:      #6fb4ff;  --accent-hot: #dcecff;  --accent-deep: #1d4d8f;
--glow: rgba(111,180,255,0.14); --glow-core: rgba(220,236,255,0.5);
/* Status */
--good:#3fd68f  --warn:#e8b93f  --crit:#f2645e  /* matrix + issue cards only */
```

Glow recipe (standardized, used everywhere):
```css
/* ambient wash — huge, behind sections */
background: radial-gradient(ellipse 60% 40% at var(--x) var(--y), var(--glow), transparent 70%);
/* focused element glow — 3 layers */
box-shadow: 0 0 2px var(--glow-core), 0 0 18px var(--glow), 0 0 80px -20px var(--glow);
```
Rule: glows are **large, few, asymmetric** — three big light sources per tab max, never a small glow on every card.

## 3. Typography

System stack. Premium through **violent size contrast + weight contrast + disciplined tracking**.

| Role | Spec |
|---|---|
| Display (hero h1) | clamp(3.6rem, 10vw, 8.2rem) · weight 800 · tracking -0.045em · line-height 0.92 · text-wrap: balance |
| Display accent word | one word per headline: linear-gradient(100deg, var(--accent-hot), var(--accent) 55%, var(--accent-deep)); background-clip: text; color transparent |
| Section h2 | clamp(2.2rem, 4.5vw, 3.4rem) · 750 · -0.03em · 1.02 |
| Ghost numerals | clamp(6rem, 14vw, 11rem) · 800 · color: transparent; -webkit-text-stroke: 1px var(--hair-hi) |
| Lede | 1.2rem · 400 · --ink-dim · 1.65 · max 56ch |
| Eyebrow/labels | mono · 0.72rem · uppercase · tracking 0.28em |
| Stats numerals | sans weight 200 ultralight · clamp(3.5rem, 6vw, 5rem) · tabular-nums |

Sections: `padding: clamp(96px, 14vh, 180px) 0`. Content ~1200px, headlines may break to ~1400px.

## 4. Hero (full viewport, single-column, theatrical)

Developers tab, in order:
1. **The beam**: full-width canvas band (~40vh, behind text, z-index 0). ~140 particles flowing left→right, colored --accent-deep→--accent-hot, additive blending (globalCompositeOperation:'lighter'). Nine thin vertical slits (gates) across the width: 2px --hair-hi lines with 1px --accent-hot core. Particles converge approaching each slit, re-fan after. Left of slit 1: wide/dim. After slit 9: tight bright line. ~20% opacity under text.
2. **Eyebrow** top-left: `MAS HARNESS — MULTI-AGENT DELIVERY PLATFORM`, wide-tracked mono + leading rule.
3. **Headline** enormous, left, three stacked lines: `Eighteen agents.` / `Nine gates.` / `One <lit>pipeline</lit>.` — "pipeline" gets gradient text.
4. **Lede** below, 56ch.
5. **Stats strip** pinned to hero bottom: full-width, top border --hair, 4 cells (18/9/3/7) ultralight giant numerals + wide mono labels, hairline-separated, count up 900ms on first view.
6. **Scroll cue** bottom-center: 1px vertical line 48px, accent dot slides down + fades, 2.4s loop. Visually becomes the signal line below.
7. **Ambient light**: one huge fixed radial ember wash from top-right (CSS), grain overlay kept.

Admin hero: same stage, arc-blue, beam has FIVE slits (propose→architect→approve→registrar→available), thinner stream. Headline: `Govern the` / `<lit>machine</lit> itself.`

Reduced motion: static frame, final counter values, static cue.

## 5. Sections

Global: alternate --void/--floor backgrounds; content alignment alternates against signal line; every section opens ghost numeral + eyebrow + h2 + one-line sub. Benefit-first h2s ("Nine gates between an idea and production," not "Overview").

### Developers
**D1 Pipeline (centerpiece)**: gates stop being a widget, become page structure. Signal line (§6.1) runs down center-left (~120px from left; left gutter mobile). Each gate = full-width station: aperture-ring node (28px hairline circle + accent core dot) on the line, ghost numeral, gate name at h2 scale, one-line purpose, agent irises to the side (odd gates right, even left). No cards/borders — type, nodes, hairlines, ~120px between stations. Scroll: line fills with accent gradient to viewport center (SVG stroke-dashoffset); node ignites (dot scales 0→1, ring gets glow, irises open 60ms stagger) when fill reaches it. Sticky mini-map at right edge: nine tiny slits, current lit, click scrolls to station.
**D2 Lifecycle**: five steps editorial rows, huge ghost numerals 01-05 alternating sides, title 1.6rem/700, mono command chips. Signal line branch connects numerals. Ends with slit divider (§6.2).
**D3 Commands → "the console"**: terminal ledger panel in --surface, mono, no vertical rules; /command in --accent-hot + description --ink-dim; row hover sweeps 1px accent underline (scaleX 0→1 from left) + command warms to full accent. Fake prompt `mas ▸ _` with blinking block cursor above (static under reduced-motion).
**D4 Help**: prose + keycap chips (--surface2 inset, mono, inset 0 1px 0 --hair-hi highlight). Tab ends with closing beam: signal line runs off bottom into fading glow.

### Admins
**A1 Governance flow**: horizontal signal segment, five aperture nodes on a hairline, wide-mono labels beneath, no arrows (the line IS the connection). A pulse (bright dot + trailing gradient) travels propose→available, 6s loop, 400ms pause in each node (static under reduced motion). The `approve` node: double ring + --accent-hot — the one gate a human holds.
**A2 Roster → "instrument rack"**: four tiers as horizontal rails (hairlines spanning width, tier name wide-mono at left). Agents sit on rails as irises with names beneath. Click iris → single shared inspector panel pinned below rack (not 18 expanding cards): enlarged iris left, name at h2, role/description, tier tag, owned gates as slit icons. Crossfade 120/180ms between agents; active iris opens + glows, others dim 40%. Irises are buttons; arrow keys move within rail; panel aria-live=polite.
**A3 Capabilities matrix → aperture grid**: keep table semantics; present = 8px disc accent core + tight glow; absent = hollow hairline ring. Row hover raises glow. Legend: `● capable ○ not in scope`. overflow-x auto.
**A4 Report an issue**: three severity lanes (full-width rows), status-colored aperture dot, type 1.3rem/650, action body, mono command chip, hairlines between.

## 6. Signature Elements

1. **Signal Line**: absolute full-height SVG per tab: 2px path, base --hair, accent-gradient overlay stroke, dashoffset tracks scroll. Nodes = circle pairs. Appears in hero cue, pipeline, lifecycle, page exit.
2. **Aperture slits**: divider motif — centered 1px vertical slit 24px --hair-hi with tight --accent-hot mid-glow, flanked by long horizontal hairlines stopping 16px short. Pure CSS. Brand dot in top bar becomes a tiny slit.
3. **Irises**: 44px discs, conic-gradient(from var(--a,0deg), --accent-deep, --accent, --accent-hot, --accent-deep) masked to ring with dark center. Opening = @property --a rotation 90deg→0 + center dot scale-in. Closed: grayscale 40%. Deterministic per-agent rotation offset (name hash → degrees).

Grain overlay (feTurbulence) kept at ~0.05.

## 7. Motion

All honors prefers-reduced-motion (static frames, drawn lines, final values, opacity-only 200ms reveals).
- Reveals: opacity 0→1, translateY 28px→0, **filter blur(6px)→0**, 850ms cubic-bezier(.16,1,.3,1), children staggered 70ms.
- Signal fill: one rAF-throttled scroll listener sets --progress; dashoffset + ignition classes derive. Ignition: glow 400ms; dot scale 500ms cubic-bezier(.34,1.56,.64,1) (only bounce on page).
- Hero beam: rAF ~30fps, 140 particles desktop / 60 <640px, paused on visibilitychange + hero exit (IO).
- Tab switch: 500ms transition on colors at root; panels crossfade 250ms; keep pill mechanics.
- Hover grammar: NO translateY/scale. Light responds: border --hair→--hair-hi + tight glow fade-in 150ms + text warms one step. Links: underline sweep.
- Counters: rAF 900ms ease-out, once, via IO.

## 8. Keep / Drop

KEEP: single-var accent swap (body[data-tab]), tab panel structure, sticky blur top bar, pill switcher, IO reveal plumbing, JS data arrays, grain, mono eyebrow + rule (widen to 0.28em), tabular-nums, text-wrap balance, ::selection tint. All content/IA verbatim.
DROP: light theme + toggle, orbit canvas, per-panel corner glows/hover sprinkle, rounded-card grid language (radius 12px only where a surface is truly needed: console, inspector, matrix).

**Testable definition of not-vanilla**: any viewport: ≤1 bordered box, ≥1 element over 3rem type or one lit graphic, visible blackness around content. If a screenful looks like cards on a background, it fails.
