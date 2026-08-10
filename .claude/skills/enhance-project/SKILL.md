---
name: enhance-project
description: Propose and build a new feature on an already-deployed project. Owned by enhance-agent — creates a feature branch, runs a re-engagement decision for dropped SMEs, and drives a mini gated pipeline (Plan & Backlog, Functional Design, Experience Design, Architecture, Code, Test, Verification, Review, Deploy) scoped to the one feature.
---

# /enhance-project

Delegates to `enhance-agent` (see `.claude/agents/enhance-agent.md` for the
full procedure — this skill is the thin entry point).

1. Identify the target project (ask if ambiguous) and confirm its
   `PROJECT_CONTEXT.md` shows status `deployed` — if not, this is a
   `/new-project` situation, not an enhancement.
1a. **Run intake — Path B of `admin/templates/INTAKE_FORM.md`.** A free-form
   prompt is a request, not an intake. Read `PROJECT_CONTEXT.md` FIRST and
   **do not re-ask what it already answers** — Path B is deliberately short
   for that reason. Pre-fill what the prompt answered; ask only what's open,
   as checkboxes, never bundled.

   Non-negotiable on this path: **B4 (which surfaces it touches, and which it
   does NOT and why)** — that answer seeds `solution-architect`'s mandatory
   Impact Analysis, and it is the exact question whose absence let a shared
   backend change ship to desktop web with zero web-side test coverage. Also
   **B9 (what's out of scope)**, because mid-flight scope growth is what
   forces a route redraw.

   If research or an SME surfaced options rather than an answer, each option
   is its own candidate with its own checkbox — never bundled, never
   implicitly chosen. Append the completed form to the `FEATURES.md` entry.

2. Collect the feature request and hand off to `enhance-agent`, which:
   - Asks for a feature name.
   - Runs the re-engagement decision (ask about dropped SMEs; always
     re-engage solution-architect/security-architect/responsible-ai-architect,
     and ui-ux-designer for UI-bearing projects). `functional-design-agent`
     and `verification-agent` are core and always engage — they are not part
     of the re-engagement question.
   - Creates `feature/<YYYY-MM-DD>-<slug>`, registers it in `FEATURES.md`.
   - Runs the mini gated pipeline (Plan & Backlog → **Functional Design** →
     Experience Design if applicable → Architecture → Code → Test →
     **Verification** → Review → Deploy), pausing for human approval at every
     boundary exactly like `/new-project`.
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
- **Impact Analysis is mandatory at the mini pipeline's Architecture stage**
  (2026-07-28): `solution-architect` must record, in `ARCHITECTURE_KB.md`,
  which surfaces (web / mobile / API / data / deliverables) this enhancement
  reaches, which are unaffected **and why**, and what must be re-tested. A
  surface omitted without justification blocks Architecture. On any
  multi-surface project `solution-architect` is non-droppable, so this is not
  waivable by trimming the roster.
- **Accelerator consultation is mandatory at the mini pipeline's Architecture
  stage too** (2026-08-08): `solution-architect` reads
  `accelerators/CATALOGUE.md` and records a **Reuse Decision Table** in
  `ARCHITECTURE_KB.md` — one row per catalogue entry, decision exactly
  `reuse` / `adapt` / `build-new`, never "not considered"; a `build-new` with no
  reason blocks Architecture. Consultation is mandatory, reuse is not, and reuse
  never lowers the evidence bar. The Impact Analysis must also state which
  accelerator-derived code this enhancement touches, by slug and version, and
  whether it creates, widens or closes a local divergence from upstream.
- **Verification is blocking**: an acceptance criterion from
  `FUNCTIONAL_SPEC.md` with no mapped, executed, passing check is
  `NOT VERIFIED` and routes back to Code, exactly as in `/new-project`.
- **Test Policy**: the mini pipeline's Test stage respects the project's
  existing blocking/advisory suite policy from `PROJECT_CONTEXT.md` (see
  `test-agent.md`) unless the human explicitly amends it as part of the
  re-engagement decision for this feature.
