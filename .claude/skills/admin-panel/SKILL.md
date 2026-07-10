---
name: admin-panel
description: Entry point for evolving the MAS platform itself (agent roster, pipeline shape, roadmap) — never for building or changing an individual project. Sub-commands via args: "propose-agent <idea>", "add-agent", "roadmap", "release". If no sub-command is given, ask which one is wanted.
---

# Admin Control Panel

This skill is the **only** entry point for changing the MAS platform itself. It
is never invoked from `/new-project`, `/enhance-project`, `/modify-feature`, or
`/consult`, and it never reads or writes anything under `projects/`. All its
state lives under `admin/`.

Parse the sub-command from the skill args and follow the matching flow. If args
are empty or ambiguous, ask the user which sub-command they want.

## `propose-agent <idea>`

1. If `admin/MAS_REGISTRY.md` still has an empty table (no agents registered
   yet), this is the **Founding Review**, not a routine proposal — invoke the
   `mas-architect` subagent and ask it to review the entire proposed MAS
   design and produce a complete registry + roadmap (see mas-architect's own
   instructions for what that entails), rather than evaluating one idea.
2. Otherwise, invoke the `mas-architect` subagent with the proposed idea. It
   will check for overlap against the existing registry, answer the standard
   agent contract questions, and return a recommendation.
3. Present the recommendation to the user in full (including any overlap/risk
   flags) and ask for explicit approval, rejection, or revision — never treat
   silence or a vague "ok" as approval for anything touching the core 5 agents
   or pipeline gate order.
4. Write the approved (or revised-and-approved) recommendation to
   `admin/proposals/<slug>.md` so there's a record, regardless of outcome.

## `add-agent`

Only proceed if there is an approved recommendation (from `propose-agent`,
found in `admin/proposals/`, or freshly approved in this conversation).

1. Invoke the `mas-registrar` subagent with the approved recommendation.
2. For the Founding Review case specifically: registrar writes the full
   registry + roadmap first (status `planned` for everything), then this
   sub-command is run again, once per agent, in the roadmap's priority order,
   to actually scaffold each one — never scaffold everything in one shot, even
   though they were all approved together, so each addition is independently
   verifiable.
3. Report exactly what was created/changed.

## `roadmap`

Invoke the `mas-release-manager` subagent to show current MVP scope / backlog
from `admin/ROADMAP.md` and groom it per the user's input (reprioritize, defer,
add a new backlog idea — note that a genuinely new *agent* idea should still go
through `propose-agent` for mas-architect's review before landing on the
roadmap as more than a placeholder line).

## `release`

Invoke the `mas-release-manager` subagent to bundle shipped-but-unreleased
platform changes into a named version, update `admin/CHANGELOG.md`, and decide
+ record rollout scope (future projects only vs. also offered to in-flight
projects via `/enhance-project`).
