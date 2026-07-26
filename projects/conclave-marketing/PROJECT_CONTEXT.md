# PROJECT_CONTEXT: conclave-marketing

## Overview
- **Project**: conclave-marketing
- **One-liner**: Multi-page marketing website for the Conclave platform itself —
  FastAPI-served, THRED-inspired design language in Conclave's copper identity.
- **Template**: none (custom, human-approved deviation — no existing template
  fits a marketing website; scaffolded template-less with its own dev/ repo,
  FastAPI backend chosen by the human for consistency with the portfolio stack)
- **Created**: 2026-07-17
- **Target env**: local (dev)
- **Current stage**: Intake

## Origin (pivot record)
The Conclave microsite began life as a deliverables-agent output
(`admin/deliverables/microsite.html`), hand-iterated through five design
generations (v1 roundtable → v5 THRED-essence branding) directly by the
orchestrator with human feedback each round. On 2026-07-17 the human directed:
"transform this into a new project under conclave as marketing — one of the
marketing features is the website. that way it goes through appropriate gates."
The v5 single-page microsite is preserved as the design seed at
`dev/design-reference/microsite-v5-seed.html`; all further evolution happens
through this project's gated pipeline.

Human decisions already made (2026-07-17, via AskUserQuestion):
- **Backend**: FastAPI (over Flask, which the human first floated; chose the
  recommended portfolio-consistent option).
- **Structure**: Multi-page like THRED — Home (numbered sections), a dedicated
  Solutions deep-dive page, a Contact page — served as real routes, replacing
  "everything vertically in same page."

Feature intent already voiced by the human (candidate backlog for Plan gate):
- Multi-page site served by FastAPI (Home / Solutions / Contact routes).
- Replicate remaining THRED components in Conclave's context: always-moving
  animations (looping hero council diagram, marquee), tabbed value-by-role
  (CxO-style) module, Solutions deep-dive components, platform/stack tab
  module with detail cells, giant typographic closing CTA with grow-on-hover
  underline links, THRED-style footer brand block.
- Bigger, more prominent Conclave branding (larger wordmark/headline type —
  partially applied in v5 seed already).
- Design reference: https://thred.dltoci.com/home (human-provided); its CSS/JS
  techniques already analyzed and documented in the v5 seed's header comment.
- Constraint carried from deliverables conventions: the site makes zero
  external network requests; all assets self-contained. Real Gartner citations
  only — never fabricate attributions.
- Placeholder `hello@conclave.example` must be replaced by a real address
  before external sharing (human-owned item).

## Architecture Summary
(to be produced at the Architecture gate)

## Active Team
Approved by human 2026-07-17 (option: "Core + targeted claims review"):
- **Core**: plan-agent, code-agent, test-agent, review-agent, deploy-agent,
  ui-ux-designer (non-droppable, UI-bearing).
- **Optional SMEs**: none on the roster. functional-agent and industry-expert
  contributed Intake KBs only (read downstream, not re-invoked at gates).
- **Targeted consult**: responsible-ai-architect performs ONE claims-accuracy
  review of final site copy before the Deploy gate (marketing-claims
  substantiation per FTC Operation AI Comply; not a roster member, owns no
  recurring suite here).
- **Test Policy**: all active suites blocking (default; no exceptions).

## Decisions Log
- 2026-07-17 — Project created by human direction as the governed home for the
  Conclave marketing website; template-less scaffold approved implicitly by
  the pivot instruction; FastAPI + multi-page chosen by human via
  AskUserQuestion. [orchestrator]

## Test Results
(none yet)

## Intake Gate (complete, 2026-07-17)
- Domain (functional-agent): B2B AI-platform marketing-site engineering →
  `knowledge/DOMAIN_KB.md`. Headlines: the site's strongest honest proof is
  "built by Conclave itself"; one primary CTA per page; WCAG 2.2 AA with
  reduced-motion parity for all always-moving components; hard anti-fabrication
  rules incl. a citations manifest checked at Test.
- Industry (industry-expert): energy-sector AI-software buyers →
  `knowledge/INDUSTRY_KB.md`. Headlines: utility buying is committee/RFP-driven —
  the site must survive being forwarded to skeptics; auditability + human
  oversight language is the differentiator ("decision support, not autonomous
  control"); FTC Operation AI Comply puts AI marketing claims squarely in
  scope; both Gartner stats on the seed verified real; several seed claims
  need sync/hedging (test-suite counts, "0 lines" as design guarantee).
- Usage estimate (usage-monitor): core-only ~270–440k tokens; full team
  ~800–950k; recommends core-only + one targeted responsible-ai-architect
  claims review (~40–50k). Biggest cost risk: design revisions — mitigated by
  treating the v5 seed as approved direction (extend, don't reimagine).

## Current Status
Deployed (dev, local) — 2026-07-17. All 9 gates complete: Intake, Team
Composition, Plan & Backlog, Experience Design, Architecture, Code, Test,
Review, Deploy. MVP F1-F12 live at http://127.0.0.1:8100/ (run via
`cd dev && source .venv/bin/activate && uvicorn app.main:app --port 8100`).
F13 (real contact address) remains deferred, human-owned, blocking any
external sharing.

Additional Decisions Log entries:
- 2026-07-19 — Human, with a screenshot, asked for all menus consolidated
  at the top ("this menu needs to be embedded in the top"), plus internet
  research on how large menus work on product sites, plus a thorough
  ui-ux-designer test with logged defects. Researched SaaS mega-menu +
  combined-nav best practice (task-based grouping; the "layered
  navigation" pattern — one persistent nav element, not independently-
  appearing bars — is the standard fix for exactly this complaint).
  Dispatched ui-ux-designer with that research; returned 11 defects (1
  Critical: two genuinely separate nav bars, the in-page section nav only
  entering the layout after scrolling past the hero) and a concrete
  consolidation spec, saved at dev/test-evidence/ux-nav-audit-2026-07-19.md.
  Implemented directly: single <nav class="topnav"> with two rows (global
  links always visible; that page's in-page sections in row 2, present
  on Home/Solutions, correctly absent on Contact) — both rows render
  together from initial page load, no scroll-triggered appearance.
  Fixed 5 of the 6 High/Critical defects as part of the same pass
  (label mismatches across mega-panel/row2/jump-palette, a scroll-margin
  single-source-of-truth bug, a mobile menu/row2 overlap risk, a
  double-smooth-scroll animation conflict). dev/ commit c9bbe62. 36/36
  tests re-confirmed, live-verified. [orchestrator]
- 2026-07-17 — Human reported menu still confusing, disliked the center
  thread line, said pages didn't match the approved color mockup, and
  asked for wider responsiveness — with an explicit request for
  ui-ux-designer to do a thorough audit and log defects (not orchestrator
  guessing). Dispatched; returned 19 logged defects (1 Critical, 8 High,
  6 Medium, 4 Low) saved verbatim at dev/test-evidence/ux-reaudit-
  2026-07-17.md. Root causes confirmed, not just preferences: the
  Solutions mega-trigger was a non-navigating button (Critical — direct
  cause of "confusing"); main::before mathematically collided with the
  v8 pass's new wide/asymmetric grids; the live site had 3 animating
  decorative layers (constellation, blobs, marquee) never shown in the
  flat mockup the human approved; main's 1060px cap left 300-1500px of
  dead space on wide viewports; the Moss palette swap introduced an
  unchecked AA contrast regression (~4.25:1, needed 4.5:1). All
  Critical/High items fixed same session (dev/ commit e2570ee); Medium/
  Low items queued as follow-up polish, not blocking. 36/36 tests
  re-confirmed, live-verified. [orchestrator]
- 2026-07-17 — Human requested: redo the top menu, consolidate/deepen the
  Solutions page ("seems very light"), reorganize content, and generate
  5 additional color-scheme options. Clarified scope via AskUserQuestion:
  mega-menu with dropdowns (not a flat restyle), consolidate AND add
  substance to Solutions, swatch-picker format for palettes. Delivered:
  design-review/color-palette-picker.html (5 original palettes: Slate &
  Signal, Ember, Moss, Ink & Gold, Cobalt — own hex values, not sampled
  from any reference). Human selected Moss + light theme as new default.
  Mega-menu built (Solutions dropdown, hover+click+keyboard, 3 sub-links).
  Solutions page's 5 sections consolidated to 3 (Governance/Platform-
  Stack/Evaluation merged into one dense "Governed & ready to evaluate"
  section with a new 3-column artifact row and a genuinely new
  evaluation cell, not just repacked). dev/ commit cc4b78a. 36/36 tests
  re-confirmed, live-verified. [orchestrator]
- 2026-07-17 — Human requested "an exact replica of THRED for Conclave" —
  declined: reproducing a real commercial product's (Deloitte-branded)
  visual identity crosses from design inspiration into copying another
  company's actual work. Clarified with human via AskUserQuestion; human
  confirmed "inspiration is what I want but for conclave" (density,
  typography, interaction feel) plus a follow-up request for THRED-like
  responsive behavior. Delivered a v6 design pass (dev/ commit cf64b3f):
  denser editorial spacing, tighter letter-spacing/smaller type scale,
  grow-underline link utility, faster tab transitions, and a new <480px
  responsive density tier — original Conclave colors/copy throughout
  (own warm paper-toned neutrals and copper accent, not Deloitte's actual
  brand palette). 36/36 tests re-confirmed, live-verified. [orchestrator]
- 2026-07-17 — Post-Deploy gap fix: human flagged that several THRED-
  reference component patterns identified during Intake/research were
  never actually built (F12's ranking judged most as low-value/skip,
  which undershot the original instruction to replicate every component).
  Added directly, original content throughout: sticky in-page numbered
  sub-nav (Home + Solutions, active-tracked), dual-CTA closing layout
  (small text link + giant statement, was single-CTA), platform/stack
  tab panels restyled with header band + colored-border detail cells,
  and a functional (not decorative) footer quick-jump palette with
  Cmd/Ctrl+K, live filter, and arrow-key navigation over real sections.
  Deliberately did not build a fake video/media player component — no
  real product footage exists, and fake play controls would violate the
  project's own anti-overclaiming hard rules. 36/36 tests re-confirmed,
  live-verified on port 8100. dev/ commit 3cb36f4. [orchestrator]
- 2026-07-17 — Deploy gate: app launched via uvicorn (0.0.0.0:8100), all
  3 routes return 200, unknown paths return 404, confirmed live via curl
  smoke test and opened in browser. Status: deployed (dev, local). [orchestrator]
- 2026-07-17 — Review gate approved (review-agent) + targeted responsible-ai
  claims review clear to ship — both run in parallel, both independently
  found the same single issue (council-diagram sr-only text said "eight
  specialist agents," SVG renders six) and cleared everything else: no
  autonomy overclaiming, no fabricated customers/traction, "by design"
  hedging applied consistently everywhere the 0/100% claims appear (not
  just the Test-gate-fixed spot), NIST/ISO framework language correctly
  hedged, cited stats (Gartner/Deloitte/EPRI/Itron/NERC) faithful to
  source scope (RAI spot-verified the Gartner 30% claim via live web
  search against the actual 2024 press release). Fixed directly (eight->
  six); 36/36 tests re-confirmed. [orchestrator]
- 2026-07-17 — Test gate: test-agent (26/26 pytest, found missing
  tests/test_content.py + one unhedged 100% stat) and ui-ux-designer (found
  4 defects: sr-only text trapped inside aria-hidden ancestor — invisible to
  screen readers; missing <header> landmark; h4-under-h2 heading-order skip
  in ps-grid/eval-grid; missing Contact-page closing-CTA variant, dead
  .statement-static CSS). All 6 defects fixed directly by orchestrator
  (dev/ commit 1648c9e) per human direction to drive all gates to a final
  outcome without further pauses. 36/36 tests passing after fixes,
  independently re-verified live (header landmark present, sr-only text
  reachable, zero stray h4, contact closing-cta renders, 100% stat now
  reads "by design"). [orchestrator]
- 2026-07-17 — Code gate complete: code-agent built the real FastAPI app
  (F1–F12) under dev/, committed 8e89a6c. Independently re-verified by
  orchestrator: 26/26 pytest passing, live server on port 8100 returns 200
  on all 3 routes + 404 on unknown paths, zero external URLs in rendered
  HTML, titles/canonicals correct. content/CITATIONS.md is disciplined —
  explicitly records claims deliberately NOT made (unverified portability
  claim omitted per instruction) alongside every sourced stat. code-agent
  judgment calls to review: replaced seed's unsynced "eight platform
  capabilities" with six enumerated items from admin/ROADMAP.md, and
  "19 agents" counted from admin/MAS_REGISTRY.md row count. [orchestrator]
- 2026-07-17 — Experience Design (UX_KB.md + design-review/experience-
  design-preview.html) approved as-is after human reviewed the rendered
  mockup (published as Artifact for convenience). [human]
- 2026-07-17 — Architecture gate: no solution-architect/security-architect
  on roster (Team Composition decision). Per PLAN.md §3/§6, architecture is
  intentionally simple (static Jinja2 templates + FastAPI, no DB/auth/forms)
  and orchestrator records it as not formally SME-reviewed, per transparency
  rule. Two technical decisions made directly: (1) port 8100 for uvicorn
  (8000/3000 occupied by little-milestones); (2) app layout per PLAN.md §3
  (app/main.py, templates/, static/, content/CITATIONS.md, tests/). [orchestrator]

Additional Decisions Log entries:
- 2026-07-17 — Plan & Backlog gate approved via per-feature checkbox list
  (new standing approval format per human direction, recorded in
  admin/LESSONS.md): F1–F12 all in MVP 0.1.0; F13 deferred. [human]
- 2026-07-19 — FROM-SCRATCH REDESIGN INITIATED [human]: current site rejected
  ("very confusing for a visitor, does not tell me what it does in one line";
  dislikes single-scroll layout — wants unique pages with continuation).
  ui-ux-designer dispatched clean-slate (no reference to existing site);
  delivered 5 distinct multi-page experience concepts (Plain Answer /
  Convening / Control Room / Dossier / Watch One Get Built). Rendered
  mockups: design-review/redesign-concepts-v2.html. Awaiting human pick.
- 2026-07-19 — POSITIONING CHANGE [human]: website is now INDUSTRY-AGNOSTIC.
  Human: "this has nothing to do with utilities" → chose "Industry-agnostic"
  via AskUserQuestion. All energy/utility framing stripped from concepts;
  examples are generic (customer-support chatbot, knowledge apps). NOTE:
  CLAUDE.md and INDUSTRY_KB.md still describe the platform's portfolio as
  energy-focused — the marketing site no longer reflects that; INDUSTRY_KB's
  energy-buyer research is demoted to background for this project. Any
  rebuilt copy must not reintroduce industry framing.
- 2026-07-19 — EXPERIENCE DESIGN v2 APPROVED [human]: merged concept
  "Show Your Work" (Q&A-chain spine + build-replay as /how), industry-
  agnostic, "Paper & Seal" palette (Paper/Ink/Deep Teal/Human Gold/
  Artifact Cream/Rework Rust), gold-seal signature motion. Approved from
  rendered interactive mockup (design-review/show-your-work-mockup.html,
  also published as private artifact) after a motion-layer revision.
  Human additions at approval: (1) more content per page, (2) more
  intuitive animation on /how, (3) /who must show the team as a connected
  hierarchy visualization, not word-heavy cards. Full rebuild of the site
  proceeds through Plan & Backlog → Code → Test → Review → Deploy.
- 2026-07-20 — PLAN & BACKLOG v2 APPROVED [human]: all 11 rebuild features
  (F2.1–F2.11) approved via per-feature checkbox list, none trimmed.
  v2 ships as 0.2.0. Build order per PLAN.md. Code gate begins.
- 2026-07-20 — CODE GATE v2 COMPLETE: code-agent implemented all 11 features
  (F2.1–F2.11) in dev/ commit beda5d3. 90/90 tests passing (up from 36),
  orchestrator independently re-ran suite and live-smoke-tested (5 routes
  200, /solutions & /contact 308 redirects, zero external requests).
  Deployed locally on :8100. Code-agent judgment calls logged for Review:
  (1) /who diagrams 16 project-level agents, mas-* platform agents covered
  in prose; (2) Test send-back is one step containing fail→rework→re-run;
  (3) banned-terms list stricter than plan (adds substation, "certified");
  (4) contact placeholder centralized as CONTACT_EMAIL constant. Deferred
  to designer audit: no-below-fold rule, live motion/contrast behavior.
- 2026-07-20 — POSITIONING COPY APPROVED [human]: homepage sub-copy replaced
  with '"Defend" short form' variant, chosen from 3 research-backed previews
  ("AI-built software you can defend…" anti-vibe-coding differentiator +
  FDE delivery paragraph). Headline unchanged. dev/ commit 8a39fe3, 91/91
  tests (new copy-drift test). Backed by industry-expert market research
  (INDUSTRY_KB.md 2026-07-20 entry: competitive map, claims evidence tiers,
  FDE hedge rules). No stats on home — STRONG-tier stats reserved for /why.
  NEW STANDING RULE [human]: no website changes of any kind without prior
  human approval of exact wording/design (recorded in personal memory).
  Platform roadmap proposals STAGED, NOT APPROVED (human: "build website
  first") — see admin/proposals/2026-07-20-roadmap-additions.md.
- 2026-07-21 — POST-v2 CONTENT ADDITIONS APPROVED & BUILT [human]: from two
  rounds of mockup review (design-review/who-hierarchy-v2-mockup.html,
  design-review/comparison-and-fde-mockup.html). (1) Homepage "The Harness"
  strip: 9-gate rail beneath the CTA row, caption Option A verbatim
  ("industry best practices, wired into nine gates — end-to-end automation
  with you in command"), gold/rust ticks, deep-links to /how's real gate
  anchors. (2) /who hierarchy visual pass: rail-and-columns layout keeps
  the graph structure the human liked; every node gets a team-color accent
  + drawn icon (research/design/architecture/build/quality/ship/
  cross-cutting), staged entrance animation, hover glow, color legend, and
  one explicitly-approved looping exception — a slow gold shimmer on the
  rail every ~6s (frozen under prefers-reduced-motion). [CORRECTED
  2026-07-22 per coherence audit C2: this entry originally called the
  shimmer "the only loop on the site" — that was false. Other continuous
  loops exist: the site-wide ambient network canvas (added later same day)
  and /what's dotBounce/cursorBlink demo micro-animations. The shimmer is
  one of several motion exceptions, not the only one.] (3) Homepage
  comparison "Speed to demo isn't speed to production":
  vibe-coding vs Conclave, citing Veracode 2025 (45% security-vuln rate),
  GitClear 2025 (8x duplication, -70% refactoring), MIT NANDA 2025 (95%
  pilot-stall) — sourced from industry-expert's 2026-07-20 market research,
  added to content/CITATIONS.md. HUMAN RELAXED F2.3: homepage no longer
  strictly one-viewport — headline still opens the page, but it now scrolls
  to accommodate real content. (4) FDE 3-week rollout moved to /why (not a
  new 6th chain page, not the homepage) as its new opening section, titled
  "We bring the platform to you — in three weeks," framed explicitly as
  "the standard rollout... our defined process, not a promise on a specific
  engagement" (no named customers exist; hedge enforced per industry-expert
  research). dev/ commits d90c6c1 (harness+hierarchy) and 54632ac
  (comparison+FDE), 141/141 tests, orchestrator independently re-verified
  and redeployed :8100 both times.
- 2026-07-21 — /WHAT REWORK APPROVED & BUILT [human]: from reviewed mockup
  (design-review/what-fancy-mockup.html, "build as shown", auto-run once on
  load + replay button). Each of the three app types now opens with a
  small, replayable, scripted demo instead of only description: support
  chatbots (a Q&A exchange incl. one honest refusal), automated workflows
  (5-step pipeline pausing visibly at its human checkpoint), knowledge
  assistants (question types out, matching doc highlights, cited answer
  resolves). Explicit, one-time, human-approved exception to the site's
  general no-autoplay rule (demos auto-run once on page load; flagged in
  code as page-scoped, not a new pattern). All existing "what it is not"
  boundary copy preserved verbatim. dev/ commit 8ae09ec, 147/147 tests,
  orchestrator independently re-verified (pytest, JS syntax, zero external
  requests) and redeployed :8100.
- 2026-07-21 — AMBIENT BACKGROUND RESTORED [human]: from reviewed mockup
  (drifting-nodes canvas, ported from the pre-v2 design but recolored to
  the "Paper & Seal" palette — teal nodes/lines, one gold node standing in
  for the orchestrator). Human chose site-wide (all 5 pages) over
  homepage-only, and kept the differentiated gold node over uniform teal.
  Quieter than the original (opacity .22 vs .28-.5, 26 vs 38-60 nodes),
  fixed behind all content (z-index 0), freezes to a static frame under
  prefers-reduced-motion, zero external requests (pure canvas API). dev/
  commit 0e20e0d, 154/154 tests, orchestrator independently re-verified
  (pytest, JS syntax, canvas present on all 5 routes, zero external URLs)
  and redeployed :8100.
- 2026-07-21 — AMBIENT BACKGROUND FIX (real defect, found by dispatched
  UI/UX audit) [human]: after two blind visibility tweaks failed ("i dont
  see it on the side", then "still no animation"), human directed a proper
  audit ("test it properly before release to me, engage UI UX designer")
  instead of further guessing. Root cause found: #conclaveNet's CSS
  opacity (.38) and each shape's own rgba(...) alpha in site.js MULTIPLY,
  not add — true effective on-screen strength was only ~18% for dots and
  ~3-5% for connecting lines regardless of how high either number was
  pushed independently; secondary issue, canvas wasn't scaled for
  devicePixelRatio (blurred on Retina). Human approved the exact fix
  parameters via a live side-by-side comparison artifact (real code, both
  panels animating) rather than a static mockup — "go for right". Fix:
  CSS opacity removed entirely; target alpha baked directly into JS (dot
  .48->.55, core .7->.85, line coefficients .14/.22->.16/.24, radii
  1.8/3->2.2/3.6); DPR scaling added via ctx.setTransform, correctly
  reapplied on resize. Independently re-verified by the SAME
  ui-ux-designer instance that found the bug (not a fresh rubber-stamp) —
  recomputed effective contrast ~36%/49%/8-12%, confirmed DPR transform
  ordering correct, confirmed no new throw/stacking regressions. Verdict:
  PASS. dev/ commit b00f1bf, 154/154 tests, redeployed :8100.
- 2026-07-22 — FULL-SITE COHERENCE AUDIT + fixes [human flagged "make sure
  entire design is coherent"]. Dispatched ui-ux-designer for a real
  cross-page audit (not per-page): verdict NOT coherent as shipped but
  close/fixable, drift concentrated at the seams between separately-approved
  rounds. 2 Critical (C1 home missing its forward link; C2 code+this-log
  falsely claimed "/who shimmer is the only loop" while ambient canvas +
  /what micro-animations also loop), 1 High fixed (H1 Harness was a styled
  <span>, now a real <h2>). Fixed directly (dev/ commit 4789723, 159/159
  tests) + this log's false claim corrected above. STILL OPEN (need human
  decisions, NOT yet actioned): H2 (home comparison + /why both argue "why
  gates matter" with different stats — dedupe or make overlap deliberate);
  H3 (--c-quality ~= --gold, two meanings, near-identical hue); M1 (gold
  used decoratively on /why FDE week labels); M2 (rust drifted to generic
  negative — vibe column, /what not-boxes); M3/M4/L1/L2 (motion-weight
  inconsistency, Harness eyebrow style, latent class drift).
- 2026-07-22 — COUNCIL AS CORE CROSS-PAGE COMPONENT [human: "core component
  moving across pages, starting with main page, design philosophy should
  coexist"]. ui-ux-designer produced a design concept (pre-mockup): "The
  Council Mark" at 3 tiers sharing one draw-once-then-hold choreography —
  Tier 1 full labeled diagram stays EXCLUSIVELY on /who (resolves audit C2,
  no second full diagram); Tier 2 unlabeled teal-threads-into-neutral-core
  glyph with one gold pull-line travels (hero-scale woven into home hero via
  the existing ambient-canvas layer, icon-scale on /why); Tier 3 gold
  pull-line signature marks existing human-decision beats (Harness ticks,
  /how gate seals, /what workflow pause). NOT a 4th homepage section — woven
  into hero + Harness, zero new sections. Motion rule: draws in once per load
  (scroll-triggered below fold), then holds, never loops; supersedes the
  inaccurate "nothing loops" line for this component family. Palette: gold
  reserved strictly for pull-line/terminus, teal threads, neutral core never
  gold; no other gold element may share a viewport with the Mark (fixes H3
  within its footprint). Concept APPROVED-IN-PRINCIPLE by human; rendered
  mockup is the next step before any build.
- 2026-07-23 — POSITIONING + COUNCIL MARK APPROVED FOR BUILD [human]. After
  extended positioning work: the site's lead shifts from a governance/"brake"
  story to the AHA — "Conclave is a new way to build software — 16 expert AI
  agents that take an idea all the way to a production-grade platform." The
  differentiator (vibe coding = one prompt, one model, a demo; Conclave = 16
  agents running the full SDLC → production-grade) leads, with governance as
  the trust mechanism beneath. Approved hero copy (verbatim, from mockup
  design-review/council-mark-mockup.html): headline as above (gold underline
  on "production-grade platform"); lede "Imagine handing an idea to a full
  engineering team — planners, architects, security, testers, reviewers — and
  getting back software that's ready for the real world. That's Conclave: 16
  specialist AI agents running every stage of the software lifecycle, with you
  in command, so what you launch is production-grade from day one."; stat
  strip 16 (specialist agents, not one model) · 9 (SDLC gates, every one
  covered) · 0 (lines shipped unreviewed). New hero LAYOUT: full-width
  headline band, then a two-column body (copy left, council diagram right).
  THE COUNCIL MARK (cross-page component, 3 tiers, one draw-once-then-hold
  motion, never loops): Tier 1 = full labeled diagram, /who only (glyph draws
  in then unfolds into the existing team-colored pipeline-rail); Tier 2 =
  hero council glyph (6 SDLC-discipline nodes → neutral Conclave core → "→ a
  production-grade platform", gold "You / YOUR CALL · EVERY GATE" pull-line);
  Tier 3 = gold pull-line signature marking human-decision beats on /how gate
  seals and /what's workflow checkpoint. Palette: gold ONLY on pull-line/
  terminus, teal threads, neutral core never gold. Numbers grounded in real
  registry (16 project agents, 9 gates); "0 lines" = design guarantee, not an
  audited metric. FLAGGED as separate follow-up (NOT in this build, needs its
  own copy approval): propagating the new voice to /why and the comparison
  section, which still read in the old governance-first tone.
- 2026-07-23 — COUNCIL MARK + NEW HERO BUILT: code-agent implemented all 4
  phases. P1 shared component + draw-once motion (df69caa); P2 new homepage
  hero — full-width headline "a new way to build software", lede, 16/9/0 stat
  strip, Tier-2 council diagram, IntersectionObserver draw-once trigger
  (0d1b8cf); P3 /who Tier-1 glyph draws in then rail entrance follows via 700ms
  one-shot delay (d2f149f); P4 Tier-3 gold pull-line signatures on /how's 9
  seals (rust on Test send-back) + /what checkpoint (4ac845a). 161/161 tests;
  4 CITATIONS rows added (16 agents = real registry count; 9 gates; "0 lines"
  = design guarantee not metric; production-grade = capability claim, no
  customer implied). WCAG AA verified both themes. Orchestrator independently
  re-verified + redeployed :8100. KNOWN LOOSE END: page <title> and <meta
  description> still carry the OLD headline copy — flagged to human for a copy
  decision (needs new wording matching the "new way to build software"
  positioning). Old on-page headline fully removed.
- 2026-07-23 — EXPERIENCE REVIEW + fixes [human asked ui-ux-designer for a
  detailed review of experience loose ends]. Verdict: no Critical, new hero
  strongest yet, title/meta fix confirmed. Fixes applied (dev/ commit acadb37,
  161/161): H1 /who TRUE unfold — rail-entrance delay 700ms→1900ms so the
  glyph leads, glyph de-emphasized (max-width 520→340px, role labels removed
  so the labeled roster lives only in the rail, no more double "You"/roster);
  M3 hero lede/stat-strip/CTA staged entrance restored (orphaned selectors
  repointed to .home-body); M2 Tier-3 .sig3 signatures given their own short
  timeline (draw by ~0.8s, no more ~1s blank); M1 hero gold underline now
  wraps under both lines on mobile via box-decoration-break:clone + period
  folded into the goldline unit. H2 bridging edit [human-approved wording]:
  homepage comparison heading "Speed to demo isn't speed to production" →
  "Anyone can be fast to a demo. Conclave gets you to production." (dev/
  commit 34bdb8a) — puts Conclave on the winning side of the speed argument,
  resolving the same-page collision with the "production-grade from day one"
  hero. STILL DEFERRED (own copy-approval round): full /why + comparison-body
  voice rewrite into the new "new way to build software" register.
- 2026-07-23 — /why + COMPARISON VOICE REWRITE [human: "rewrite and fix that
  too"]. ui-ux-designer drafted the full rewrite into the new "new way to
  build software" partner voice; human approved via mockup (design-review/
  why-comparison-rewrite-mockup.html) incl. Conclave-first column order.
  Applied directly by orchestrator (build agent kept dropping on connection
  errors): (1) comparison — Conclave column now LEADS (left), divider moved
  to it, reframed as two paths from the same idea, subcaptions "9 gates →
  production" / "1 step: prompt → a demo"; all 3 cited stats (Veracode 45% /
  GitClear 8x&70% / MIT NANDA 95%) kept verbatim on the vibe side. (2) /why —
  partner-voice reframe of leads, FDE section ("We build it with you — and in
  three weeks, it's yours"), gates intro (design-bet-first), decision-log +
  claims-table intros, contact ("You're in command from the first line"),
  with EVERY substantiated claim kept verbatim: both Gartner stats, the two
  decision-log quotes, the unsanitized test-gate send-back, both seal lines,
  the 7-row claims table, the FDE hedge, the F13 placeholder note. No citation
  dropped/reworded — CITATIONS.md unchanged. dev/ commit 8db58c6, 161/161
  tests, redeployed :8100. Tests updated: comparison bullet substrings +
  column-order assertion, FDE-heading references (2 tests).
- 2026-07-23 — /what REDO INITIATED [human: "'what it builds' is wrong — we
  can use Conclave to build ANY software, need strong examples, conduct
  detailed research, all right agents involved"]. Current /what wrongly caps
  Conclave at 3 template types; truth is it's a general-purpose governed SDLC
  system, templates are accelerators not the ceiling. Dispatched industry-
  expert (deep research: software categories enterprises build/buy in 2026 +
  6-10 concrete illustrative example applications + honest breadth framing)
  and functional-agent (functional-breadth taxonomy + devil's-advocate on
  where "any software" overclaims + the honest scope/hedge — noting cloud
  target_env still local-only, mobile/embedded out of scope, etc.). Next:
  synthesize → ui-ux-designer /what redesign concept → mockup → human approval
  → build. Honesty constraint: illustrative capabilities only, no invented
  customers, must survive the claims manifest.
- 2026-07-24 — /what REDESIGN APPROVED FOR BUILD [human]. Research synthesized
  (industry-expert + functional-agent, recorded in INDUSTRY_KB/DOMAIN_KB).
  Human chose: breadth = "broadest defensible" ("a general-purpose way to build
  the software your business runs on"), boundary = present-but-understated (one
  quiet line: web/API/data/agentic · your environment · cloud roadmapped · not
  mobile/embedded). Page structure/copy approved from mockup (design-review/
  what-builds-redesign-mockup.html): lead + boundary line, 3 templates demoted
  to fast-starts, 7 concrete custom example categories + an 8th "unscoped" card,
  capability-spine, forward link. Human ADDITIONALLY directed: "actual previews
  to be built when the build begins, I am okay with UI design" — i.e. upgrade
  each example's schematic sketch to a REAL designed UI preview (fuller
  fidelity). HONESTY GUARDRAIL (kept): previews are generic ILLUSTRATIVE sample
  UIs — real design quality, placeholder/sample content, NO invented company
  name/logo, labeled as a sample — never a screenshot implying a delivered
  product; needs a claims-manifest row. Claims rows also needed: delivery=your-
  environment (cloud roadmapped), web-not-native-mobile, templates=accelerators.
  All examples illustrative ("Conclave can build…"), no market-ROI stat as
  Conclave's own, no compliance-guarantee language, domain-neutral.
- 2026-07-24/25 — /what REDESIGN BUILT: new page leads on breadth ("a
  general-purpose way to build the software your business runs on"), 3
  templates demoted to fast-starts, 8 example categories each with a REAL
  designed illustrative-sample UI preview (contract view / portal dashboard /
  ops table with status pills / audit log / analytics chart+recommendation /
  process flow with gold human-checkpoint / integration hub / idea canvas),
  capability spine, understated honest boundary (your environment; cloud
  roadmapped; not native-mobile/embedded). Previews are generic labeled
  "Illustrative sample" (no invented customer/logo) — honesty guardrail
  enforced. Cards rise-in once on scroll via new what.js (no loop; reduced-
  motion static). Build spanned agent connection drops; orchestrator finished
  the loose ends directly: created what.js, added .reveal motion CSS, added 6
  honest-scope CITATIONS rows, fixed banned-term false positive (ex-grid ->
  ex-cards class rename), removed orphaned what-demos.js + old animated-demo
  tests, wrote new-structure tests. dev/ commit 3031cf8, 163/163 tests,
  redeployed :8100, zero external requests.
- 2026-07-25 — /what RE-LANGUAGED + REALISTIC PREVIEWS [human] built. After
  the human rejected "not three templates" (insider framing) and the abstract
  sketches: (1) designer redid language positive/idea-first — page now opens
  "Have an idea for software? Conclave builds it." with the idea→built theme
  threaded end to end; (2) industry-expert researched example ORDER (serial-
  position effect) → Contract → Internal ops → Portals → Analytics →
  Integration → Agentic → Compliance → open-ended closer; (3) copy tightened;
  (4) boundary "One honest note on scope" line REMOVED (scope now implied by
  examples + spine's "Delivered into your environment"; CITATIONS mobile/
  embedded/cloud rows retired); (5) templates reframed "Three quick-start
  templates" (compact fast-lane), custom section made the prominent main event
  "Pure custom — your idea, built end to end" with 8 ENLARGED cards; (6) the 8
  previews upgraded from line-art to REALISTIC app-window sample UIs (window
  chrome, drop-shadows, filled buttons/pills, sample data, real chart + audit
  log) — still generic + labeled "Sample" (no company/logo), honesty held.
  dev/ commits c3cf47d + 3339280, 163/163 tests, redeployed :8100, zero
  external requests. Code-agent judgment calls: added --surface token (AA-
  verified), SVG filter regions as objectBoundingBox fractions (avoids stat-
  gate false positive on "140%"), breadth-lead test repointed to new lead.
- 2026-07-25 — VISUAL-ENGAGEMENT LAYER [human: "add imagery... very text heavy",
  then "research leading way to engage users, if not human it's fine"]. Research
  (industry-expert, INDUSTRY_KB 2026-07-25): for trust-led technical products the
  leading engagement move is NOT stock/AI photos (banner-blindness + credibility
  damage — worst move for a trust brand) but rationed restraint + editorial
  text-breaking + activating existing visuals + a locally-generated abstract
  texture. Human chose the research-backed plan, all pages one pass. Designer
  produced a build-ready per-page placement spec (caught real class collisions:
  .pull→.pullquote, .split→.split-card, .stat→.stat-callout). Built (dev/ commits
  c67d0c6/eaac20d/e2eaef4/739f608/66fcbae, 190/190 tests): P1 editorial kit
  (stat-callouts, pull-quotes, split-card) LIFTING existing copy only — no new
  marketing copy; P2 promoted the .reveal scroll observer site-wide + tightened
  to .24s; P3 the honest "imagery" = a locally-generated "council network"
  canvas texture (texture.js, multi-instance, IO-gated, reduced-motion static,
  theme-aware) as exactly 3 sparse section dividers (/why closing, /what custom-
  head, /who bottom; NONE on home [ambient canvas] or /how [replay]); P4 six thin
  gold seal/line section icons in base.html defs. /why got the heavy treatment
  (2 pull-quotes, 2-up Gartner stat-callouts, test-evidence as a split-card, a
  texture band), other pages light. Zero external requests (pure canvas), both
  themes, AA, reduced-motion parity all preserved. Deliberately AVOIDED: stock/AI
  photos, human imagery, fake screenshots, scroll-jacking. NOTE: I (orchestrator)
  cannot call the OpenAI image API — the generative-from-code texture sidesteps
  that entirely and keeps the site self-contained.
