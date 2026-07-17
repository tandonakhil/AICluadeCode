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
(to be decided at the Team Composition gate)

## Decisions Log
- 2026-07-17 — Project created by human direction as the governed home for the
  Conclave marketing website; template-less scaffold approved implicitly by
  the pivot instruction; FastAPI + multi-page chosen by human via
  AskUserQuestion. [orchestrator]

## Test Results
(none yet)

## Current Status
Scaffolded; Intake gate in progress (domain + industry research dispatched).
