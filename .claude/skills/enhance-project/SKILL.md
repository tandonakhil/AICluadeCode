---
name: enhance-project
description: Propose and build a new feature on an already-deployed project. Owned by enhance-agent — creates a feature branch, runs a re-engagement decision for dropped SMEs, and drives a mini gated pipeline scoped to the one feature.
---

# /enhance-project

Delegates to `enhance-agent` (see `.claude/agents/enhance-agent.md` for the
full procedure — this skill is the thin entry point).

1. Identify the target project (ask if ambiguous) and confirm its
   `PROJECT_CONTEXT.md` shows status `deployed` — if not, this is a
   `/new-project` situation, not an enhancement.
2. Collect the feature request and hand off to `enhance-agent`, which:
   - Asks for a feature name.
   - Runs the re-engagement decision (ask about dropped SMEs; always
     re-engage solution-architect/security-architect/responsible-ai-architect,
     and ui-ux-designer for UI-bearing projects).
   - Creates `feature/<YYYY-MM-DD>-<slug>`, registers it in `FEATURES.md`.
   - Runs the mini gated pipeline (Plan & Backlog → Experience Design if
     applicable → Architecture → Code → Test → Review → Deploy), pausing for
     human approval at every boundary exactly like `/new-project`.
3. On completion, the feature is "Ready for Release" — not yet in `prod/`.
   Mention `/cut-release` as the next step if the human wants to ship it.

## Guardrails

- Never batch this with `/new-project` — enhancements require an
  already-deployed project as their starting state.
- Same approval discipline as every other gated pipeline in this system:
  never skip a stage boundary's human sign-off.
- **Usage logging**: same as `/new-project` — append one line to
  `projects/<name>/USAGE.md` per agent invocation (see `usage-monitor.md`
  for the format), orchestrator bookkeeping, not a separate agent call.
- Before the mini pipeline's Code stage, invoke `usage-monitor` for a
  pre-work estimate the same way `/new-project`'s Team Composition gate
  does, scaled to a single-feature scope rather than a whole project.
