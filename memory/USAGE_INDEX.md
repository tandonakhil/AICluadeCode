# Cross-Project Usage Index

Rollup of each project's `USAGE.md`, maintained by `usage-monitor`. Cheap to
read at session start alongside `memory/INDEX.md` for a cross-project view
without opening every project's detail file.

| Project | Team | Gates covered | Agent-call tokens | Last updated |
|---|---|---|---|---|
| grid-assistant | core-only (predates Team Composition) | Plan/Code/Test/Review/Deploy x2 (original + 1 enhancement) | not yet backfilled | — |
| policy-lookup-assistant | full team (all 5 optional SMEs) | Full 9-gate pipeline + multi-suite Test verification + frontend cycle | ~646,833 | 2026-07-09 |
| load-alert-agent | core-only, API-only template | Intake/Plan/Code/Review (Test/Deploy via direct Bash, no agent-call cost) | ~150,297 | 2026-07-09 |

**Early signal (2 data points, not yet a reliable average)**: a full-team,
UI-bearing project with complete multi-suite verification runs roughly
**4x** the token cost of a core-only, API-only project. Use this as a rough
Team Composition planning input, not a firm prediction — `usage-monitor`
should always say how many samples an estimate is based on.
