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
