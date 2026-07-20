# Usage Log: conclave-marketing

| Timestamp | Stage | Agent | Tokens | Running total | Notes |
|---|---|---|---|---|---|
| 2026-07-17 | Team Composition (pre-work estimate) | usage-monitor | 11,926 | 11,926 | Pipeline estimate: core-only ~270–440k; recommends dropping all optional SMEs except a targeted responsible-ai-architect claims review (~40–50k); biggest risk = design revisions, mitigated by v5 seed |
| 2026-07-17 | Intake | functional-agent | 11,663 | 23,589 | Domain research: B2B AI-platform marketing sites — DOMAIN_KB.md written by orchestrator from returned content |
| 2026-07-17 | Intake | industry-expert | 37,025 | 60,614 | Industry research: marketing AI software to energy-sector buyers — INDUSTRY_KB.md written by orchestrator from returned content |
| 2026-07-17 | Plan & Backlog | plan-agent | 26,055 | 86,669 | PLAN.md: F1–F8 MVP (multi-page FastAPI + THRED components + claims manifest), F9–F13 deferred |
| 2026-07-17 | Experience Design | ui-ux-designer | 55,266 | 141,935 | UX_KB.md spec for F1–F12; orchestrator built required rendered preview (design-review/experience-design-preview.html) per gate contract |
| 2026-07-17 | Code | code-agent | 164,094 | 306,029 | Built real FastAPI multi-page app (F1–F12), 26/26 pytest passing, committed to dev/ (8e89a6c) |
| 2026-07-17 | Test (unit/integration) | test-agent | 30,300 | 336,329 | 26/26 pytest confirmed; found 2 defects: missing tests/test_content.py (F7 automated enforcement), unhedged 100% stat in home.html:88-90 |
| 2026-07-17 | Test (UX/accessibility) | ui-ux-designer | 56,709 | 393,038 | Found 4 a11y/spec defects: sr-only trapped in aria-hidden, missing header landmark, h4-under-h2 skip, missing Contact closing-CTA |
| 2026-07-17 | Test defect fixes (direct) | orchestrator | ~4,000 (est.) | ~397,038 | All 6 Test-gate defects fixed directly; 36/36 tests passing after fix |
| 2026-07-17 | Review | review-agent | 46,091 | 443,129 | Approved with 1 finding (stale "eight" agent count); diff hygiene, decision-intent match, consistency all clean |
| 2026-07-17 | Targeted claims review | responsible-ai-architect | 36,317 | 479,446 | Clear to ship after 1 fix; no overclaiming, no fabricated traction, hedging consistent, stats faithful to source |
| 2026-07-17 | Review fix (direct) | orchestrator | ~500 (est.) | ~479,946 | Corrected sr-only agent count eight→six; 36/36 tests re-confirmed |
| 2026-07-17 | Post-Deploy gap fix (direct) | orchestrator | ~9,000 (est.) | ~488,946 | Added sticky sub-nav, dual-CTA, restyled platform panels, functional jump palette; 36/36 tests re-confirmed |
| 2026-07-17 | v6 design pass (direct) | orchestrator | ~11,000 (est.) | ~499,946 | Denser editorial layout, tighter typography, grow-underline links, <480px responsive tier; declined literal "exact replica" of THRED, clarified scope to inspiration |
| 2026-07-17 | Palette picker + mega-menu + IA consolidation (direct) | orchestrator | ~16,000 (est.) | ~515,946 | 5-palette swatch picker built; mega-menu shipped; Solutions consolidated 5→3 sections; Moss+light applied as new default per human choice |
| 2026-07-17 | Thorough UX re-audit | ui-ux-designer | 71,256 | 587,202 | 19 defects logged (1 Critical, 8 High) against live site — mega-menu non-navigable trigger, thread-line grid collision, decorative-layer/mockup mismatch, width cap, Moss contrast regression |
| 2026-07-17 | Audit fix pass (direct) | orchestrator | ~13,000 (est.) | ~600,202 | Fixed all Critical/High defects: split mega-trigger, removed main::before, widened layout, dialed back decorative layers, fixed contrast; 36/36 tests re-confirmed |
| 2026-07-19 | Nav consolidation research + audit | orchestrator + ui-ux-designer | ~68,015 | ~668,217 | WebSearch on SaaS mega-menu/combined-nav patterns; dispatched designer for full nav audit — 11 defects logged (1 Critical: two separate nav bars) + consolidation spec |
| 2026-07-19 | Nav consolidation fix pass (direct) | orchestrator | ~15,000 (est.) | ~683,217 | Merged floating pill nav + separate in-page subnav into one two-row .topnav; fixed 5 additional High/Medium defects (label mismatches, scroll-margin bug, mobile overlap risk, double-scroll conflict); 36/36 tests re-confirmed |
| 2026-07-19 | From-scratch redesign — Experience Design round 2 | ui-ux-designer | 27,411 | ~710,628 | Human rejected current site (unclear one-liner, single-scroll fatigue); designer delivered 5 fresh multi-page experience concepts, clean-slate brief (no reference to existing site) |
| 2026-07-19 | Redesign concept mockups (direct) | orchestrator | ~10,000 (est.) | ~720,628 | Built design-review/redesign-concepts-v2.html — rendered homepage mockups of all 5 concepts + page maps for human selection |
| 2026-07-19 | Merged concept design (1+5) | ui-ux-designer | 24,763 | ~745,391 | Human picked combination of Plain Answer + Watch One Get Built; designer delivered "Show Your Work" — Q&A chain spine with the build replay as /how; industry-agnostic per positioning change |
| 2026-07-19 | Merged concept mockup (direct) | orchestrator | ~12,000 (est.) | ~757,391 | Built design-review/show-your-work-mockup.html — all 5 pages clickable, working replay stepper (5 sample steps), light/dark toggle |
| 2026-07-20 | Plan & Backlog v2 | plan-agent | 42,234 | ~799,625 | Rebuild plan appended to PLAN.md; 11 features F2.1–F2.11; all approved via checkbox list |
| 2026-07-20 | Code gate v2 | code-agent | 139,714 | ~939,339 | Full "Show Your Work" rebuild, commit beda5d3, 90/90 tests; orchestrator re-verified + redeployed :8100 |
| 2026-07-20 | Market positioning deep research | industry-expert | 27,595 | ~966,934 | Competitive map (vibe-coding/agentic/FDE clusters), STRONG/MEDIUM/WEAK claims evidence tiers, recommended positioning + 3 pillars, FDE hedge rules; INDUSTRY_KB.md updated by orchestrator |
| 2026-07-20 | Admin-panel roadmap proposals | mas-architect | 42,256 | ~1,009,190 | 8 platform roadmap items proposed (P1: contract sweep, cloud target_env re-prioritized, packaging; P2: golden evals, compliance pack, observability; P3: multi-tenant, guardrails module); advisory only, pending human approval |
| 2026-07-20 | Positioning copy approval + apply (direct) | orchestrator | ~8,000 (est.) | ~1,017,190 | "Defend" short form applied to home (8a39fe3), 91/91 tests; roadmap staged to admin/proposals pending approval |
| 2026-07-21 | Harness + jazzed /who build | code-agent | ~132,758 | ~1,141,948 | Homepage 9-gate rail, /who team-color+icon+shimmer redesign; commit d90c6c1, 138/138 tests |
| 2026-07-21 | Comparison + FDE rollout build | code-agent | ~83,365 | ~1,225,313 | Homepage vibe-coding comparison (cited), /why FDE 3-week section; commit 54632ac, 141/141 tests; F2.3 one-viewport relaxed per human |
| 2026-07-21 | /what rework build | code-agent | ~181,096 | ~1,406,409 | New replayable chat/workflow/retrieval demos on /what; commit 8ae09ec, 147/147 tests (2 interrupted attempts + 1 completed resume) |
