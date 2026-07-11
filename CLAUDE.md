# AICluadeCode — Multi-Agent SDLC System

This repo is a Multi-Agent System (MAS) that builds and operates a portfolio of
AI-centric applications for the energy industry (GenAI chatbots, agentic
workflows, RAG/knowledge-base apps). It runs on Claude Code's own Agent SDK
primitives — subagents, skills, and the Workflow tool.

## Two separate axes — do not mix them

1. **Project development** (`/new-project`, `/enhance-project`, `/modify-feature`,
   `/consult`) — builds and evolves individual applications under `projects/`.
2. **Platform governance** (`/admin-panel`) — evolves the MAS itself (its agent
   roster, pipeline shape, roadmap) under `admin/`. Never reachable from project
   commands; never touches `projects/`.

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
  (`LESSONS.md`).
- `.claude/agents/` — all subagent definitions (`mas-*` = admin/platform agents,
  everything else = project-pipeline agents).
- `.claude/skills/` — entry-point commands.
- `templates/` — starter templates for `/new-project` (`genai-chatbot`,
  `agentic-workflow`, `rag-knowledge-base`).
- `memory/INDEX.md` — one row per project; load a project's own
  `PROJECT_CONTEXT.md` for detail rather than reading everything.
- `projects/<name>/` — one project: `PROJECT_CONTEXT.md`, `FEATURES.md`,
  `RELEASES.md`, `USAGE.md`, `knowledge/*_KB.md`, and independent `dev/`/`prod/`
  git repos.

See `admin/MAS_REGISTRY.md` for the full current agent roster and
`admin/ROADMAP.md` for what's built vs. planned.
