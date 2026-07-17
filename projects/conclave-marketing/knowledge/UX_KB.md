# UX_KB: conclave-marketing

**Author**: ui-ux-designer (Experience Design gate, 2026-07-17; content returned to orchestrator, file written by orchestrator per KB-write policy)
**Seed**: `dev/design-reference/microsite-v5-seed.html` — this spec **extends** the approved v5 identity (Copper+Dark, constellation, pill nav, copper thread, wordmark-with-copper-period, split hero + council SVG, ghost numbers, thread-rules, flush grids). No new visual language introduced; every component reuses existing v5 tokens/classes or composes them.

## Summary

The v5 single page splits into three routes. **Home** keeps the split hero (now with a *looping* council animation + a marquee under the stat strip), 01-Why, a compressed 02-How (pipeline diagram + 3-beat teaser linking to Solutions), the persona module upgraded from a 4-card grid to THRED-style **tabs**, a compressed Proof section, and a new **giant closing CTA**. **Solutions** inherits the deep content: full gate-by-gate walkthrough, three use-case modules, governance-on-the-record artifact renderings, platform/stack tab module, RFP-ready resource block. **Contact** is one mailto action. Every page ends with the same giant "Convene the Conclave." CTA. Two contrast bugs found in the seed are fixed in F8 (muted-gray small text ~4.1:1; white-on-copper buttons 2.7:1 in dark theme — buttons switch to dark-ink text on copper). One THRED component recommended for porting in F12 (scroll-triggered word-by-word statement reveal); the rest skip.

## 1. Multi-page IA & shared chrome (F1/F2/F5/F6)

**Content split** (all content is existing v5 content unless marked *new*):

| Home (`/`) | Solutions (`/solutions`) | Contact (`/contact`) |
|---|---|---|
| Hero (wordmark row, thesis h1, lede, CTA row, looping council SVG, stat strip, *new* marquee) | Page hero: short h1 + lede (no council SVG — reuse `.section-head` scale) | Short h1 "Start the conversation." |
| 01 Why: Gartner stat-hero-row + stat-flush + problem/solution `ps-grid` | 01 Three use cases (chatbot / agentic / RAG modules) | One `btn-primary` mailto + plain-text address fallback |
| 02 How (compressed): pipeline diagram + first 3 journey entries + "Read the full walkthrough →" link to `/solutions#walkthrough` | 02 Gate-by-gate walkthrough (full 9-entry `.log`) | Response expectation line (verify truthfulness at copy review) |
| 03 Value by role: **tabbed** module (F4) replacing persona-grid | 03 Governance, on the record (artifact renderings) | Dev-only placeholder-address warning banner (amber) |
| 04 Proof (compressed): "Built by Conclave" log, 3 entries (F10 strengthens) | 04 Platform & stack tab module (F5) | Giant closing CTA rendered as static statement + button (self-referencing avoided) |
| Giant closing CTA → `/contact` | 05 Evaluation-ready resource block (F11) | |
| | Giant closing CTA → `/contact` | |

Newsroom/team section (v5 §03) moves to **Solutions**, folded into "Governance, on the record" (team-grid + `tech-disclosure`) — Home stays light; evaluators get depth.

**Header (base.html)**: floating pill nav, unchanged visually, with real routes: `HOME` / `SOLUTIONS` / `CONTACT` (drop `tn` section numbers from nav — those belong to in-page sections). Active page: server-rendered `class="active" aria-current="page"` (replaces scroll-spy at the page level; scroll-spy may still drive a secondary mobile label on Home only, never mixed with route-active state on desktop). Brand mark → `/`. "Talk to us" pill CTA → `/contact` (not raw mailto), preserving one-mailto-total (on Contact) and the one-primary-CTA rule. Mobile menu behavior unchanged from seed.

**Footer (base.html)** — THRED-style brand block, evolved from `.bookend`:
1. Giant closing CTA component (§5) — the conversion moment on every page.
2. Brand block: oversized wordmark "Conclave·" at `clamp(2.4rem, 8vw, 6rem)`, `--ink` at 12% opacity (decorative, `aria-hidden`), copper dot at full opacity.
3. Sitemap links (three routes + in-page anchors) + `.meta` line adding the no-external-requests trust statement (INDUSTRY_KB §5): "This site makes zero external network requests and sets no trackers."

Copper thread `main::before` terminates in the footer dot exactly as in seed — carries to all three pages.

**Per-page narrative** (DOMAIN_KB §2): Home = problem → thesis → how → proof → personas → closing CTA. One primary CTA per page: Home/Solutions = closing CTA to `/contact`; Contact = the mailto button. All other links are visually subordinate.

**Bigger branding (F2)**: hero wordmark scale increases to `clamp(3.8rem, 8vw, 7rem)`; tagline/vrule scale proportionally; h1 unchanged. 404 page: wordmark + "This gate doesn't exist." + link home.

## 2. F3 — Looping council animation + marquee

**Council SVG loop**: master cycle **T = 14s** on the existing rAF clock (`t % 14`):
- 0–3.5s draw-in (threads draw core-ward, staggered 0.3s, 1.1s each — existing easing).
- 3.5–10.5s hold (rings orbit, core pulse breathes, verdict `pullLine` pulses — existing speeds; add a node highlight sweep, each specialist's stroke-width easing 1.2→2→1.2 in sequence, ~0.8s each).
- 10.5–12s retract (threads reverse in reverse stagger order; pullLine opacity → 0).
- 12–14s rest (rings + core pulse only), then redraw. The human node and core wordmark never disappear — only threads cycle.
- **Reduced motion**: freeze at the hold state (threads fully drawn, pullLine static at 0.55, rings static, core pulse at 0.10) — never a blank diagram.
- Pause when `document.hidden` (existing) and when the hero scrolls out of viewport (new IntersectionObserver guard).

**Marquee**: single-row strip below the stat strip, full-bleed, 1px `--hairline` rules top+bottom. Content = the honest-vocabulary litany (INDUSTRY_KB §4 "resonates" list): mono 12.5px uppercase, copper-dot separators — `DECISION RECORD · HUMAN FINAL SAY · TEST EVIDENCE — INCLUDING FAILURES · INDEPENDENT REVIEW · DEFINED SCOPE · PORTABLE STACK · NINE GATES · …`. Duplicated track, CSS `translateX` keyframe, 45s linear infinite.
- **Pause affordance** (WCAG 2.2.2): pause/play toggle (`aria-pressed`, 44px hit area) pinned at the strip's right edge; hover also pauses via `animation-play-state`, but the button is the accessible control.
- **Reduced motion**: animation off, track static left-aligned with a fade-out gradient at the right edge; toggle hidden.

## 3. F4 — Tabbed value-by-role module (Home §03)

`.section-head` (ghost 03, "Value, by seat at the table") → horizontal tablist (styled like nav pills) → one tabpanel styled as a wide `.card`, two-column ≥800px: left = pain quote (italic) + distinct value story; right = role-specific proof artifact:

| Tab | Proof artifact |
|---|---|
| Product owner | Mini backlog excerpt (3 checkbox rows: approved/reordered/cut) |
| Operations | Industry-advisor KB excerpt card (2-line pressure-test note) |
| Compliance & security | Decision-record excerpt (3 append-only log lines incl. one override) |
| IT | Stack strip + one portability-statement line |

**ARIA/keyboard**: `role="tablist"` (aria-label "Value by role"), `role="tab"` with `aria-selected`/`aria-controls`, `role="tabpanel"` with `aria-labelledby`, `tabindex="0"`. Roving tabindex; Left/Right/Home/End. Panel switch: 0.25s fade+8px rise; instant under reduced motion.
**Mobile (<640px)**: tablist scroll-snaps horizontally with edge-fade; panel stacks single column (story then artifact). No accordion conversion.

## 4. F5 — Solutions page

Ghost-number sections 01–05: use cases → walkthrough → governance → platform/stack → evaluation-ready → closing CTA.

**Three use-case modules (01)**: `stat-hero-row` split, alternating left/right. Left: `stat-featured`-style panel with the pain, sourced (chatbot → outage communication; agentic → workload relief, Deloitte 2026 26%-by-2035 peak-demand strain; RAG → EPRI data-readiness gap). Right: what Conclave builds — 3 capability bullets + one governance-application line. Sources render in `.src` (contrast-fixed per §7).

**Walkthrough (02)**: full 9-entry `.log` from the seed verbatim, `#walkthrough` anchor target from Home.

**Governance, on the record (03)**: credibility centerpiece. Artifact excerpts as document chrome (`.card` with mono header bar `filename · date`, hairline, 4–6 mono excerpt lines, copper left-border on human-decision lines) — not screenshots. Two artifacts: a decision-record excerpt (incl. a "send back") and a test-evidence excerpt (incl. a real failure row, amber). Content must be faithful renderings of real artifacts (hard rules 1/2 — sourced at build, verified at Test). Framework-language card: "aligned with the expectations of NIST AI RMF / ISO 42001; decision support, not autonomous control" — never "certified." Team/newsroom subsection + `tech-disclosure` roster table land here.

**Platform & stack tab module (04)**: shares the F4 tab component. Tabs: Templates / Stack / Portability / Isolation, each a flush-editorial detail-cell grid (`stat-flush` pattern). Portability panel ships its config-switch claim **only if verified**; otherwise the cell becomes the isolation/no-tracking statement.

## 5. F6 — Giant closing CTA + Contact

`.closing-cta`, on every page above the footer brand block:
- Kicker: mono uppercase 12px "THE FIRST GATE IS A CONVERSATION."
- Statement (Home/Solutions): `<a href="/contact">Convene the Conclave<span class="dot">.</span></a>` at `clamp(2.6rem, 7vw, 5.5rem)`, weight 700, letter-spacing −0.03em.
- **Grow-on-hover underline**: `background-size: 0% 0.06em → 100% 0.06em` on hover/focus, transition `.45s cubic-bezier(.16,.8,.3,1)`; dot scales 1→1.15. Instant under reduced motion.
- **Focus-visible**: underline at 100% *plus* `outline: 2px solid var(--primary); outline-offset: 6px; border-radius: 4px` — never underline-only.
- Sub-line: 15px, "Describe what you want to build in plain language — that's genuinely all gate one needs."
- Contact page variant: statement is a static heading-adjacent display line; the interactive element is the `btn-primary` mailto below it.

## 6. F9 / F10 / F11

**F9 stats strip**: reuse `stat-flush`. Cells: Gartner 2024 30%, Gartner 2025 40%+, Itron 2025 81% (+43% expertise-gap in the `d2` line). Source line is structural — a stat cell without a populated source is a template error, not an optional field. No count-up when the strip appears on Solutions (count-up stays a Home-hero moment only).

**F10 strengthened**: keep the 3-entry log; add a document-chrome artifact rendering of a `admin/MAS_REGISTRY.md` excerpt (counts pulled from the registry at build, verified at Test). Add trust line: "Zero external requests, zero trackers — verifiable in this page's source." Hedged phrasing throughout: "by design, nothing advances without approval" replaces bare 0/100% framings ("Lines shipped unapproved — by design" / "Gates ending in an explicit human decision").

**F11 evaluation-ready block** (Solutions §05): flush 3-cell grid — (a) "For your RFP scoring matrix" bullets mapping Conclave properties to standard RFP criteria; (b) compact reference-architecture SVG (seed's `arch-diagram` restyled, same tokens); (c) stack-portability statement **only if it verifies** — otherwise the isolation/no-tracking statement. Framed as "shaped to be pasted into an evaluation," no download pretense.

## 7. F8 — Accessibility annotations (build-time requirements)

**Contrast (dark theme, default) — computed:**
- `--primary` #E08849 on `--bg` #0E0F13 ≈ 7.1:1 (passes); on `--surface` #16181E ≈ 6.6:1 (passes).
- `--body` #B7BAC3 on `--bg` ≈ 9.9:1 (passes).
- **FAIL** — `--muted` #767A85 on `--surface` ≈ 4.1:1 (labels, `.src`, `.s2`, marquee at 11–12.5px). Fix: dark-theme muted → ~`#8B90A0` (≈5.1:1). Light-theme muted #8A8D96 on #FFFFFF ≈ 3.4:1 also fails; darken to ~`#6E7280`.
- **FAIL** — `.btn-primary`/nav `.cta` white-on-copper ≈ 2.7:1 at 13–14.5px bold. Fix: dark-theme buttons use `color: #0E0F13` on copper (7.1:1); light-theme copper #B15A2B with white text ≈ 4.6:1 passes, keep.
- Amber failure rows / green checks: verify ≥3:1 as non-text indicators + never color-only (pair with ✓/✕ glyphs).

**Landmarks per page**: `header` (pill nav, `nav aria-label="Site"`), single `main`, `footer` (`nav aria-label="Footer"`). One `h1` per page. Skip link "Skip to content" as first focusable (new). Heading order strictly h1→h2(sections)→h3.

**Focus order**: skip link → brand → nav links → theme toggle → nav CTA → main content in DOM order (marquee pause after stat strip; tablist before panel) → closing CTA → footer nav. Decorative layers (`#net`, blobs, council SVG, ghost wordmark) `aria-hidden` and non-focusable. Council SVG gets a visually-hidden text alternative: "Diagram: eight specialist agents thread into one council; a human above holds final say at every gate."

**Reduced-motion parity** (freeze, not remove): council → hold state; marquee → static strip; constellation → single static frame (seed behavior, keep); count-ups → final values instantly; reveals/shimmer/blobs/spotlight → off, content fully visible.

**Mobile**: tabs scroll-snap; marquee toggle retained; giant CTA min 2.6rem with wrap; pill-nav menu pattern from seed; pipeline horizontal scroll gets a right-edge fade + "scroll →" hint below 760px; `tech-disclosure` tables scroll within the card.

## 8. F12 — Remaining THRED components, ranked

| Component | Messaging value | Recommendation |
|---|---|---|
| Scroll-triggered word-by-word statement reveal | High — vehicle for the one-sentence thesis on Solutions ("Decision support, not autonomous control."); cheap, easy reduced-motion parity (render complete) | **Port** (one instance, Solutions, between §02 and §03) |
| Image/photo parallax panels | Low — no photography; stock imagery dilutes artifact-first credibility | Skip |
| Multi-column mega-footer nav | Low — 3-route site; brand block + single-row sitemap already covers it | Skip (satisfied by F1 footer) |
| Case-study card carousel | Negative — no customers; implies traction (hard rule 2) | Skip |
| Cursor-following custom pointer | Negative — decoration over substance, a11y/perf cost | Skip |
| Number-ticker KPI band | Already exists (stat strip/count-up) | Skip (done) |

## Guardrail flags

- Covers all recorded decisions to date: FastAPI multi-page routes, all-MVP F1–F12 per checkbox approval, seed-as-approved-direction/extend-don't-reimagine, one-primary-CTA, reduced-motion parity, hedged claims, placeholder-address flagging, zero external requests.
- Not covered here (by design): F7 citations-manifest content (plan-agent/code-agent scope), F13 (human-owned, deferred), uvicorn port selection (Architecture gate).
- Two seed contrast failures found (§7) — new findings, not silently absorbed; both AA-mandated fixes.
- Advisory note for Architecture/Code (core owners have final say): the tab component in F4 and F5 should be one shared JS module; the council loop refactor replaces the seed's open-ended clock with `t % 14` — the smallest change to the approved animation code.
