# Conclave — Multi-Agent SDLC System

**Conclave** (repo: AICluadeCode) is a Multi-Agent System (MAS) that builds
and operates a portfolio of AI-centric applications for the energy industry
(GenAI chatbots, agentic workflows, RAG/knowledge-base apps). It runs on
Claude Code's own Agent SDK primitives — subagents, skills, and the Workflow
tool. The name reflects its shape: a roster of specialist agents (architects,
security, UX, industry experts) convened per project, deliberating under one
orchestrator, with the human always holding final say — a conclave, not a
single monolithic builder. Named 2026-07-13, human-approved.

## Two separate axes — do not mix them

1. **Project development** (`/new-project`, `/enhance-project`, `/modify-feature`,
   `/consult`) — builds and evolves individual applications under `projects/`.
2. **Platform governance** (`/admin-panel`) — evolves the MAS itself (its agent
   roster, pipeline shape, roadmap) under `admin/`. Never reachable from project
   commands; never writes to `projects/`.

**One deliberate carve-out to that rule — accelerator harvesting.** Promoting a
component from a shipped project into `accelerators/` **reads** `projects/` and
writes to a platform directory. It is the only sanctioned crossing of the two
axes, and it is stated here explicitly rather than left to be inferred, because
this platform's documented failure mode is rules that exist and aren't followed —
a silently reinterpreted rule is the same disease. The crossing is read-only on
the project side, always human-approved per item, and never runs from a project
command. See `admin/proposals/2026-08-08-accelerator-layer.md`.

`admin/MAS_REGISTRY.md` is the single source of truth for every agent in the
system — its pipeline gate, whether it's core or optional, its knowledge-base
file, and its test-suite ownership. Any new agent is added through
`/admin-panel add-agent`, never by hand-editing `.claude/agents/` directly.

The human's single point of contact across every command is the
orchestrator — the main conversation itself, not a registered agent. See
`admin/ORCHESTRATOR.md` for its contract and `admin/LESSONS.md` for the
persistent, cross-session log of pitfalls, proven patterns, and queued
agent-contract feedback it maintains.

## Directory map

- `admin/` — platform roadmap, changelog, agent registry, staged proposals,
  orchestrator role contract (`ORCHESTRATOR.md`), cross-session lessons
  (`LESSONS.md`), and the pipeline's shape (`PIPELINE.md` + `PIPELINE.yaml`,
  with `PIPELINE_LOG.md` recording per-project gate history).
- `.claude/agents/` — all subagent definitions (`mas-*` = admin/platform agents,
  everything else = project-pipeline agents).
- `.claude/skills/` — entry-point commands.
- `templates/` — starter templates for `/new-project` (`genai-chatbot`,
  `agentic-workflow`, `rag-knowledge-base`). **One per project, chosen before
  anything exists.**
- `accelerators/` — reusable components harvested from shipped project work,
  consulted by `solution-architect` at every Architecture gate. **Zero to many
  per project, chosen after the plan exists.** That cardinality-and-timing split
  is the whole boundary against `templates/`. `accelerators/CATALOGUE.md` is the
  SSOT index (deliberately compact — it is read at every Architecture gate
  forever). Distributed by **copy-in vendoring with a provenance stamp, never a
  shared dependency**: projects' `dev/` trees are independent git repos, so a
  submodule or cross-repo path would break `dev/`→`prod/` promotion and import
  the coupling this platform has never had.
- `memory/INDEX.md` — one row per project; load a project's own
  `PROJECT_CONTEXT.md` for detail rather than reading everything.
- `projects/<name>/` — one project: `PROJECT_CONTEXT.md`, `FEATURES.md`,
  `RELEASES.md`, `USAGE.md`, `knowledge/*_KB.md`, and independent `dev/`/`prod/`
  git repos.

See `admin/MAS_REGISTRY.md` for the full current agent roster and
`admin/ROADMAP.md` for what's built vs. planned.
