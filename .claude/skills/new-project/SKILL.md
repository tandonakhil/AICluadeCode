---
name: new-project
description: Create a new project and run it through the full gated SDLC pipeline (Intake, Team Composition, Plan & Backlog, Experience Design, Architecture, Code, Test, Review, Deploy). All core and SME agents now exist per admin/MAS_REGISTRY.md.
---

# /new-project

Creates a new project under `projects/<name>/` and drives it through the
full gated pipeline, pausing for explicit human approval at every stage
boundary. Re-check `admin/MAS_REGISTRY.md` before relying on this file if
it's been a while — this skill should be updated whenever the registry's
agent roster or gate order changes, not left stale.

## Procedure

1. **Collect the request**: project name (slug it) and one-line description.
   **Do not ask the human to pick a template up front** — invoke `plan-agent`
   with the description to get a recommended template + reasoning (it reads
   every `TEMPLATE_MANIFEST.md` and matches the actual described need, not
   surface keywords). Present the recommendation for a single confirm/
   override, not a blind multiple-choice menu. Only ask the human to choose
   between options when `plan-agent` itself reports the request genuinely
   fits two templates equally well — that's the sole case for asking.
   If the request describes multiple capabilities that don't fit one
   template today (e.g. chat + document grounding + tool-using automation),
   say so plainly: recommend a template for the MVP's actual first slice
   and note the rest as likely `/enhance-project` work later — don't force
   a single template to pretend it covers everything at once.

2. **Scaffold the project**: `mkdir -p projects/<name>`, create
   `PROJECT_CONTEXT.md` / `FEATURES.md`, register in `memory/INDEX.md`, copy
   the template into `projects/<name>/dev/` with placeholders filled, `git
   init` + initial commit. `projects/<name>/prod/` stays uncreated until the
   first promotion.

3. **Intake gate** (unconditional, regardless of what Team Composition later
   decides): invoke `functional-agent` to ask "what functional/technical
   domain is this for?" and `industry-expert` to ask "which industry is this
   for?" Both research and write their initial `knowledge/DOMAIN_KB.md` /
   `knowledge/INDUSTRY_KB.md`. This always runs — it resolves the ordering
   circularity with Team Composition (see `admin/MAS_REGISTRY.md`'s
   governance rules).

4. **Team Composition gate**: propose a roster — **core, non-droppable**:
   `plan-agent`, `code-agent`, `test-agent`, `review-agent`, `deploy-agent`,
   plus `ui-ux-designer` if the template is UI-bearing (`genai-chatbot`,
   `rag-knowledge-base`; not applicable for `agentic-workflow`). **Optional,
   droppable**: `functional-agent`, `industry-expert`, `solution-architect`,
   `security-architect`, `responsible-ai-architect`, `synthetic-data-agent`
   (default-on for UI-bearing templates, default-off for `agentic-workflow`
   — invoked just before the Test gate, not a gate of its own). Present the proposal
   (informed by the Intake answers and template) and let the human trim the
   optional portion, along with `usage-monitor`'s rough token-cost estimate
   for the full pipeline broken out by which optional agents are included
   (see step 3.5). Also ask whether any active suite should be **advisory**
   rather than blocking at the Test gate (default: everything blocking —
   only mark a suite advisory if there's a real reason for this specific
   project, per `test-agent.md`'s policy; don't offer this as a way to make
   gates pass faster in general). Record the approved roster **and any Test
   Policy exceptions** in `PROJECT_CONTEXT.md` under "Active Team." Every
   downstream stage only invokes agents on the approved roster (functional-
   agent/industry-expert still keep their Intake-time KB even if dropped
   here — see step 3).

3.5. **Usage estimate**: invoke `usage-monitor` to read `memory/USAGE_INDEX.md`
   and any comparable prior projects' `USAGE.md` for historical per-stage
   averages, and produce a concrete pre-work estimate for this pipeline —
   broken out by whether each optional SME is included — to inform the
   human's Team Composition trim decision above. If no historical data
   exists yet (e.g. the very first project), say so plainly rather than
   inventing a number.

5. **Plan & Backlog gate**: invoke `plan-agent` (plus `industry-expert` for
   trend-informed backlog suggestions and `functional-agent` as devil's
   advocate, if either is on the roster). Produces `PLAN.md` and a proposed
   feature backlog. **Present the backlog as the full itemized feature
   list** — every proposed feature shown individually with a build-now vs.
   later selection per item (multi-select), never as a summary with a
   single approve/reject button. The human decides the now/later split
   feature-by-feature; plan-agent's proposed split is the default
   pre-selection, not the decision. **Stop and wait for approval** — the
   approved subset becomes this project's MVP scope, recorded in
   `FEATURES.md`.

6. **Experience Design gate** (UI-bearing templates only, skip entirely for
   `agentic-workflow`): invoke `ui-ux-designer` to propose flows, layout, and
   visual language for the approved backlog, pushing components via
   `DesignSync`. Writes `knowledge/UX_KB.md` **and a reviewable visual
   artifact** — rendered preview pages assembled at
   `projects/<name>/design-review/index.html`, which the orchestrator
   serves locally (e.g. `python3 -m http.server`) and hands the human as a
   URL before asking for approval. Never ask for design approval from a
   text summary alone. Stop and wait for approval before Architecture.

7. **Architecture gate**: invoke `solution-architect` and `security-architect`
   jointly (if either is on the roster — if both were dropped, skip this
   gate's SME work but still note in `PROJECT_CONTEXT.md` that architecture
   was not formally reviewed, so that's visible later, not silently absent),
   plus `responsible-ai-architect` as a third advisory voice if on the
   roster (content/behavior guardrails — distinct lane from the other two,
   don't let it duplicate their passes). They design around the approved
   plan and experience design, writing `knowledge/ARCHITECTURE_KB.md` /
   `knowledge/SECURITY_KB.md` / `knowledge/RESPONSIBLE_AI_KB.md`. Stop and
   wait for approval before Code.

8. **Code gate**: invoke `code-agent` with the approved plan, experience
   design, and architecture. Present a summary of what was
   implemented/committed. Stop and wait for approval.

9. **Test gate**: invoke `test-agent` for unit/integration, plus each active
   SME's owned suite (functional, industry/compliance, UX/accessibility,
   architecture, security, red-team/bias — only for agents actually on the
   roster). Present the report broken out per suite, not merged into one
   pass/fail number, and clearly marked per `PROJECT_CONTEXT.md`'s Test
   Policy which suites are blocking vs. advisory (default: all blocking).
   A blocking suite's failure stops the gate — the human either sends it
   back or explicitly overrides with a recorded `[override]` reason in the
   Decisions Log. An advisory suite's failure is still fully reported but
   doesn't force a stop. Stop and wait for approval.

10. **Review gate**: invoke `review-agent` (narrow scope — see its own
    definition; does not re-check what the Test gate's suites already
    covered). Present its verdict. Stop and wait for approval; "request
    changes" loops back to Code with human confirmation.

11. **Deploy gate**: invoke `deploy-agent`, then `test-agent` for the
    post-deploy smoke test. Present both results. On approval, update
    `PROJECT_CONTEXT.md`'s Current Status to `deployed (dev, local)` and
    `memory/INDEX.md`.

## Guardrails

- Never skip a gate or batch multiple gates' approvals into one question.
- A gate whose only active participants were dropped by Team Composition
  still "runs" in the sense that its absence is recorded, not silently
  skipped without a trace.
- Every stage's output is written to `PROJECT_CONTEXT.md` (and relevant
  `knowledge/*_KB.md`) before asking for approval, so progress survives an
  interrupted session.
- **Usage logging**: after every agent invocation in this pipeline, append
  one line to `projects/<name>/USAGE.md` (timestamp, stage, agent, tokens
  from the call's real usage metadata, running total) — see
  `usage-monitor.md` for the format. This is orchestrator bookkeeping, not a
  reason to spawn a separate agent call per log line.
