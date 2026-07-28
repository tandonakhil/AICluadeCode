---
name: project-status
description: Show where a project is in its journey — a wrapped left-to-right progress graph across the 11 gates with human-approval checkpoints, what was skipped and why, open loop-backs, and what's next. Args "<project-name>" for one project, or no argument for the whole portfolio.
---

# /project-status

`/project-status <project-name>` — one project's position, in detail.
`/project-status` — the whole portfolio, one graph per project.

> **Naming.** The human asked for this as `/ProjectStatus`. It is registered as
> `project-status` because skill resolution follows the **directory name**, and
> every other skill in this platform is kebab-case (`new-project`,
> `enhance-project`, `cut-release`). A mixed-case outlier would be the one
> command that behaves differently from the other seven. If asked for by the
> original name, answer to it — it is the same command.

Read-only. This command **never** advances a gate, never approves anything, and
never edits a project's state. It reports.

## Procedure

### With a project name

1. **Resolve the project.** Match against `projects/*/`. If the name is
   ambiguous or absent, list what exists rather than guessing — a status report
   for the wrong project is worse than none.

2. **Read, in this order** (stop early if a file is missing; say which was
   missing rather than inferring around it):
   - `projects/<name>/PIPELINE_LOG.md` — the authoritative position. If it does
     not exist, say so plainly and reconstruct from the sources below, marking
     the report **reconstructed, not logged**.
   - `projects/<name>/PROJECT_CONTEXT.md` — Current Status, Active Team, and the
     tail of the Decisions Log.
   - `projects/<name>/FEATURES.md` — what is in development, ready, released.
   - `admin/PIPELINE.md` — canonical gate order and notation.

3. **Render the graph**, left-to-right, using the exact notation and `classDef`
   block from `admin/PIPELINE.md` §3. Every project's graph must look the same;
   that consistency is what makes the portfolio view scannable.

4. **Report, in this order:**
   - **Position** — which gate, and whether it is running, awaiting approval, or
     blocked.
   - **The graph.**
   - **What was skipped, and why.** Separate `⊘ not applicable to this template`
     from `⊘ gate did not exist yet` from `⊘ skipped without an exception`.
     These look identical in a graph and are completely different facts.
   - **Open loop-backs** — anything sent back and not yet resolved.
   - **What's next** — the next gate, its owner, and what the human will be
     asked to approve.
   - **Anything stale** — a KB, deliverable or record that no longer matches
     reality. Say it here rather than letting the human find it later.

### With no argument

Read `admin/PORTFOLIO_STATUS.md` and present it. If any project's
`PIPELINE_LOG.md` is newer than that file, regenerate the affected section
first — a portfolio view that lags its own sources is misinformation.

## Guardrails

- **Report the truth, including the unflattering parts.** A skipped gate, an
  unfired trigger, a stale KB, a gate marked `⚠` — these are the findings most
  worth surfacing. A status report that only shows green is not a status report.
- **Never mark a gate `✅` that a human did not approve.** If the log says
  otherwise, report the discrepancy.
- **Distinguish "not applicable" from "not done".** `agentic-workflow` has no
  Experience Design gate by design; that is not the same as a gate that was
  owed and skipped.
- **Do not advance anything.** If the human wants to proceed, that is
  `/enhance-project`, `/modify-feature`, or continuing the active run.
- **Say when the log is missing.** Reconstructing from the Decisions Log is
  acceptable; presenting a reconstruction as a log is not.

## Note on projects that predate the 11-gate pipeline

Functional Design and Verification were added 2026-07-28. Every project created
before then shows both as `⊘`. Report this as a real coverage gap — those
projects have no acceptance criteria with stable IDs and no audited evidence
trail — not as a cosmetic artefact. Any future enhancement to them runs the
full eleven.
