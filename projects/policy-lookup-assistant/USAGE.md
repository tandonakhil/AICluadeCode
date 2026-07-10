# Usage: policy-lookup-assistant

**Note on this file's origin**: `usage-monitor` didn't exist yet when this
project was built (Phase 4, 2026-07-05/06), so this is a **retroactive
backfill** from real per-agent token totals recorded in each Agent-tool
call's result during that work — not live-logged at the time. Timestamps are
approximate (date-accurate, not necessarily minute-accurate). Going forward,
every project's `USAGE.md` is logged live per the orchestrator's per-call
bookkeeping described in `usage-monitor.md`.

| Timestamp (approx) | Stage | Agent | Tokens | Running Total |
|---|---|---|---|---|
| 2026-07-05 | Intake | functional-agent (DOMAIN_KB) | 31,625 | 31,625 |
| 2026-07-05 | Intake | industry-expert (INDUSTRY_KB) | 40,194 | 71,819 |
| 2026-07-05 | Plan & Backlog | plan-agent | 52,199 | 124,018 |
| 2026-07-05 | Experience Design | ui-ux-designer | 52,460 | 176,478 |
| 2026-07-05 | Architecture | solution-architect + security-architect (joint) | 65,293 | 241,771 |
| 2026-07-05 | Code | code-agent (first feature) | 51,983 | 293,754 |
| 2026-07-06 | Test (multi-suite) | functional-agent suite | 40,408 | 334,162 |
| 2026-07-06 | Test (multi-suite) | industry-expert suite | 40,682 | 374,844 |
| 2026-07-06 | Test (multi-suite) | ui-ux-designer suite | 27,599 | 402,443 |
| 2026-07-06 | Test (multi-suite) | solution-architect suite | 46,357 | 448,800 |
| 2026-07-06 | Test (multi-suite) | security-architect suite | 47,739 | 496,539 |
| 2026-07-06 | Review | review-agent (first pass) | 46,099 | 542,638 |
| 2026-07-06 | Code (frontend) | code-agent (UX implementation) | 53,313 | 595,951 |
| 2026-07-06 | Review (frontend) | review-agent (second pass) | 50,882 | 646,833 |

**Project total (agent-call tokens only, excludes orchestrator-side Bash/Read/Edit work): ~646,833.**

This project ran the **full team** (all 5 optional SMEs + ui-ux-designer)
through the complete 9-gate pipeline plus a full multi-suite Test-gate
verification pass and a frontend implementation cycle — it is close to a
worst-case/upper-bound sample, not a typical-feature sample. See
`load-alert-agent`'s (core-only) comparable numbers once backfilled for
contrast.
