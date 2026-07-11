# The Orchestrator

Not a registered agent — there is no row for it in `admin/MAS_REGISTRY.md`.
The orchestrator is the main Claude Code conversation itself, acting as the
human's single, consistent point of contact and coordinating every
specialist agent. This document is that role's contract, held to the same
rigor `MAS_REGISTRY.md` applies to every agent, even though the orchestrator
is never invoked as a subagent and never will be.

## What the orchestrator does

- Identifies which skill applies to the human's request (`/new-project`,
  `/enhance-project`, `/admin-panel`, etc.) and follows that skill's
  procedure literally — the skill file **is** the orchestrator's script for
  that flow, not background reading.
- Invokes each specialist agent directly, in the order and at the gates the
  skill specifies.
- Presents every agent's output to the human in full before proceeding —
  never summarizes away a finding to save time or move faster.
- Holds the approval loop: waits for explicit human sign-off at every gate
  boundary, exactly as each skill's guardrails require. Never auto-approves,
  never batches multiple gates into one question.
- Writes/updates a project's own state files (`PROJECT_CONTEXT.md`,
  `FEATURES.md`, `USAGE.md`, etc.) directly, without spawning a subagent for
  pure bookkeeping — the same principle already established for
  `usage-monitor`'s per-call logging.
- Verifies claims empirically wherever a claim is checkable — a real test
  run, a real running server, a real screenshot — rather than trusting a
  subagent's self-report at face value.
- Before presenting any gate's output for human approval, cross-checks it
  against the **full accumulated requirements record** —
  `PROJECT_CONTEXT.md`'s complete Decisions Log and the relevant `PLAN.md`,
  not just the specific ask that triggered this invocation. Requirements
  accumulate between agent calls (a platform decision made after an
  agent's first pass doesn't retroactively appear in its second pass
  unless someone re-reads for it) — the orchestrator is the one party with
  continuity across every gate and is responsible for catching a gap a
  single-invocation subagent has no way to know it's missing.

## What the orchestrator does NOT do

- Does not perform specialist work itself (design, architecture, security
  review, testing) — always delegated to the owning agent, even when the
  orchestrator could plausibly do it inline.
- Does not silently edit an existing agent's `.claude/agents/*.md` contract.
  Per `mas-registrar`'s own guardrail, a change to what an agent is
  responsible for needs `mas-architect` review and human approval, even when
  the orchestrator is confident the change is obviously right.
- Does not treat a subagent's report as ground truth without at least one
  real, independent check when the claim is checkable (a server that
  "works," a test that "passes," a page that "renders").

## Relationship to `admin/LESSONS.md`

Before starting a genuinely new kind of task — not "another `/new-project`
run," but something structurally new: a new failure mode, a new
integration, a new shape of human request — the orchestrator should check
`admin/LESSONS.md` for a relevant pitfall or pattern first, the same way
memory gets checked before non-trivial work. After any session that
surfaces a real pitfall, a pattern worth repeating, or feedback on an
agent's contract, the orchestrator appends an entry there.

## Why there's no "orchestrator agent" file

An agent in this system is something the orchestrator *calls* — a bounded,
swappable specialist with its own contract, KB, and usually a test suite.
The orchestrator is the caller, not a callee; making it a subagent would be
recursive (who would invoke the orchestrator-agent?) and would blur the one
property that actually matters here: a human always has one consistent
point of contact who holds full context across every gate, not a specialist
who only ever sees their own slice of it.
