---
name: help
description: Lists every command/skill currently available in the MAS, read dynamically from .claude/agents/ and .claude/skills/ — never a hardcoded list, so it can't go stale as new agents/skills ship.
tools: Read, Glob
---

# /help

Do not hardcode a command list in this file — it will go stale the moment a
new skill ships. Instead, on every invocation:

1. `Glob` `.claude/skills/*/SKILL.md` and read each one's frontmatter
   (`name`, `description`) to build the current command list live.
2. `Glob` `.claude/agents/*.md` and read `admin/MAS_REGISTRY.md` to know
   which agents are platform-level (`mas-*`) vs. project-pipeline agents —
   only surface commands, not individual agents, to the user (agents are
   invoked indirectly through commands/gates, not called directly).
3. Present the result grouped into two sections, matching the platform's own
   two-axis split:
   - **Project development** — `/new-project` and any other skill whose
     `SKILL.md` lives outside `admin-panel/`, `help/`, or an `mas-`-prefixed
     concern. Include a one-line description pulled from each skill's
     frontmatter `description`.
   - **Platform governance** — `/admin-panel` and its sub-commands
     (`propose-agent`, `add-agent`, `roadmap`, `release`), read from
     `.claude/skills/admin-panel/SKILL.md`'s own documented sub-commands
     rather than hardcoded here too.
4. If `admin/ROADMAP.md` lists MVP-scope items not yet shipped (status
   `planned` in `MAS_REGISTRY.md`), do NOT list their commands as available
   — only show what's actually usable today. Optionally note "N more
   commands planned, see admin/ROADMAP.md" as a single line, not an itemized
   list (avoid /help doubling as a roadmap dump).

Keep the output short — a scannable list, not a tutorial. If the user asks
a follow-up about a specific command, answer conversationally; don't try to
cram full usage docs into every /help response.
