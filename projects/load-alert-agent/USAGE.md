# Usage: load-alert-agent

**Note on this file's origin**: retroactive backfill, same caveat as
`policy-lookup-assistant/USAGE.md` — real per-agent token totals from this
project's actual Agent-tool calls, reconstructed after the fact since
`usage-monitor` didn't exist yet when this project was built (Phase 4,
2026-07-05/06). Test/Deploy stages here were run via direct Bash (pytest,
uvicorn) rather than a subagent call, so they have no token cost to log —
itself a data point: core-only projects lean more on direct orchestrator
execution and less on agent calls for the stages with no active SME suite.

| Timestamp (approx) | Stage | Agent | Tokens | Running Total |
|---|---|---|---|---|
| 2026-07-06 | Intake | functional-agent + industry-expert (combined, brief per Team Composition scope) | 32,823 | 32,823 |
| 2026-07-06 | Plan & Backlog | plan-agent | 40,892 | 73,715 |
| 2026-07-06 | Code | code-agent | 45,078 | 118,793 |
| 2026-07-06 | Review | review-agent | 31,504 | 150,297 |

**Project total (agent-call tokens only): ~150,297.**

**Contrast with `policy-lookup-assistant` (~646,833 total, full team, all
gates + multi-suite verification + a frontend cycle)**: this core-only,
API-only project cost **~23% of the full-team project's tokens** — the
single clearest real evidence usage-monitor will have, once more samples
exist, for the pre-work estimate it gives at Team Composition ("dropping all
optional SMEs and using an API-only template costs roughly a quarter of a
full-team UI-bearing project").
