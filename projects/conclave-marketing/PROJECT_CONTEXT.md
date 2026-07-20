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
  rail every ~6s (frozen under prefers-reduced-motion; the only loop on the
  site). (3) Homepage comparison "Speed to demo isn't speed to production":
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
