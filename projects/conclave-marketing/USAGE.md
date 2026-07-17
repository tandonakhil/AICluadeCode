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
