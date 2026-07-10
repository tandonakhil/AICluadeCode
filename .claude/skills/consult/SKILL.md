---
name: consult
description: Ad-hoc, on-demand call to any SME agent at any point during development, without waiting for or re-running a full gate. Args: "<project> <agent> <question>". Does not add the SME to the project's active roster — that's a separate, explicit re-engage action at the next gate.
---

# /consult

A thin router — no owning agent of its own, since its whole point is to
reach any of the standing SME agents on demand.

## Who can be consulted

Any of the project-pipeline SME agents: `functional-agent`, `industry-expert`,
`ui-ux-designer`, `solution-architect`, `security-architect`,
`responsible-ai-architect`. (Core pipeline agents — `plan-agent`,
`code-agent`, `test-agent`, `review-agent`, `deploy-agent` — aren't
"consulted," they're invoked through the normal gated pipeline; if the
request is really "run the Plan gate again," redirect to `/enhance-project`
or `/modify-feature` instead of treating it as a consult.)

## Procedure

1. Identify the target project and confirm it exists (`PROJECT_CONTEXT.md`
   present). The named SME does **not** need to be on the project's current
   Active Team roster — consulting doesn't require prior engagement.
2. Invoke the named agent with the question, giving it the same context it
   would normally read (`PROJECT_CONTEXT.md`, `PLAN.md`, its own
   `knowledge/*_KB.md` if one exists, and whatever else is relevant to
   answering — e.g. current source under `dev/` if the question is about
   existing code).
3. Append a dated entry to that agent's `knowledge/*_KB.md` (create the file
   if this project never engaged that SME before — same as an Intake-time or
   Architecture-gate KB, just triggered by a consult instead) **and** to
   `PROJECT_CONTEXT.md`'s Decisions Log, both tagged `[consult]` so they're
   distinguishable from gate-driven entries.
4. Report the answer back. That's it — no gate re-run, no approval loop.

## Guardrails

- A consult call **never** adds the SME to the project's Active Team roster
  for future gates — that's a separate, explicit decision made at the next
  Team Composition re-open (via `/enhance-project`'s re-engagement step),
  not an automatic side effect of asking one question.
- If the question is really asking for a full design pass (not a targeted
  question), say so and redirect to the appropriate gate instead of trying
  to cram a full Architecture-gate-sized deliverable into a consult.
- code-agent may also trigger a consult mid-Code if it flags genuine
  uncertainty — same procedure, same KB/Decisions-Log logging, just
  initiated by an agent instead of the human.
