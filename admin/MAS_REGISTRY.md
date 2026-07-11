# MAS Agent Registry

Every row below is something the orchestrator *calls* — see
`admin/ORCHESTRATOR.md` for the (unregistered, non-agent) role that calls
them, and `admin/LESSONS.md` for the cross-session log of pitfalls, proven
patterns, and queued contract feedback the orchestrator maintains.

Single source of truth for every agent in the system. Populated by
`mas-architect`'s Founding Review (Phase 0.5, approved 2026-07-05), then
updated by `mas-registrar` every time `/admin-panel add-agent` ships a new
agent. Status values: `planned` (approved, not yet built) → `built` (scaffolded
and in use).

## Governance rules (apply across every row below)

- **Gate approval authority**: where a droppable SME sits alongside a
  core-pipeline gate owner, the core-pipeline owner always has final say
  (solution-architect + security-architect jointly own Architecture;
  deploy-agent owns Deploy). SME input is always surfaced to the human, always
  advisory, never independently blocking.
- **Intake questions are unconditional**: functional-agent's domain question
  and industry-expert's industry question are always asked at Intake,
  regardless of what Team Composition (which runs after Intake) later decides
  about their ongoing engagement — this avoids a circular dependency between
  the two gates.

## Registry

| Agent | Gate(s) | Core / Optional | Knowledge Base | Owns Test Suite | Tools | Re-engagement (on enhancement) | Notes | Status |
|---|---|---|---|---|---|---|---|---|
| mas-architect | Platform-level (advisory; `/admin-panel propose-agent`) | Core (platform) | None | None | Read, Grep, Glob, WebSearch | N/A — platform agent | Never writes files; recommendation only | built |
| mas-registrar | Platform-level (`/admin-panel add-agent`) | Core (platform) | None | None | Read, Write, Edit, Glob | N/A — platform agent | Only agent that writes to this registry | built |
| mas-release-manager | Platform-level (`/admin-panel roadmap`/`release`) | Core (platform) | None | None | Read, Write, Edit | N/A — platform agent | Distinct from project-level release-manager below | built |
| plan-agent | Plan & Backlog | Core | None | None | Read, Write, Grep, Glob | Always | Drafts PLAN.md + project feature backlog/MVP | built |
| code-agent | Code | Core | None | None | Read, Write, Edit, Bash(git) | Always | | built |
| test-agent | Test | Core | None | Unit/integration + post-deploy smoke | Read, Bash | Always | | built |
| review-agent | Review | Core | None | None | Read, Bash(git diff) | Always | Scope is narrow by design: code style/diff hygiene, decision-intent match, cross-cutting consistency — does NOT re-check what the 6 test suites already cover | built |
| deploy-agent | Deploy | Core | None | None (hands smoke test to test-agent) | Read, Bash | Always | `target_env` stubbed; only `local` implemented in MVP | built |
| functional-agent | Intake (domain question, unconditional) + Plan & Backlog (devil's advocate) + Architecture (advisory review) | Optional / droppable | `knowledge/DOMAIN_KB.md` | Functional | Read, WebSearch, Write (KB only) | Only if flagged relevant | | built |
| industry-expert | Intake (industry question, unconditional) + Plan & Backlog (trend backlog) + Architecture + Review + Deploy (advisory stakeholder) | Optional / droppable | `knowledge/INDUSTRY_KB.md` | Industry/compliance | Read, WebSearch, Write (KB only) | Only if flagged relevant | | built |
| ui-ux-designer | Experience Design (own gate, UI-bearing templates only, between Plan & Backlog and Architecture) | Core for `genai-chatbot`/`rag-knowledge-base`; not applicable for `agentic-workflow` | `knowledge/UX_KB.md` | UX/usability + accessibility | Read, Write (KB), DesignSync | Always, for UI-bearing projects | Design intent + observed post-deploy behavior logged in same KB | built |
| solution-architect | Architecture (joint owner with security-architect) | Optional / droppable | `knowledge/ARCHITECTURE_KB.md` | Architecture | Read, Write (KB) | Always, on enhancement/key design decision | | built |
| security-architect | Architecture (joint owner with solution-architect) | Optional / droppable | `knowledge/SECURITY_KB.md` | Security | Read, Write (KB) | Always, on enhancement/key design decision | Tightened 2026-07-06: Authentication & Authorization Design is a mandatory `SECURITY_KB.md` subsection (decision + criteria + revisit triggers) — never a one-line waiver, even when the answer is "none needed" | built |
| responsible-ai-architect | Architecture (advisory, alongside solution-architect + security-architect) + Review | Optional / droppable | `knowledge/RESPONSIBLE_AI_KB.md` | Red-team/bias | Read, Write (KB), WebSearch | Always, on enhancement | Content/behavior guardrails — distinct from security-architect (authn/authz/secrets) and functional-agent (domain-correctness); must not duplicate either's devil's-advocate pass | built |
| enhance-agent | Cross-cutting — drives `/enhance-project` (mini Plan→Experience Design→Architecture→Code→Test→Review→Deploy) and `/modify-feature` (correction mode) | Core (infra) | None (writes `FEATURES.md`) | None | Read, Write, Bash(git) | N/A — this agent is the re-engagement mechanism | Owns both `/enhance-project` and `/modify-feature`; solution-architect/security-architect/responsible-ai-architect/ui-ux-designer (UI-bearing) always re-engage, functional-agent/industry-expert only if flagged | built |
| release-manager | Cross-cutting — `/cut-release` command, after Deploy | Core (infra) | None (writes `RELEASES.md`/`CHANGELOG.md`) | None | Read, Write, Bash(git) | Always, when a release train is cut | Project-level; distinct from mas-release-manager above. Automated conflict *triage* (2026-07-09, verified for real): proximity conflicts get a lightweight confirm, semantic conflicts get full review — approval is never automated, only classification is. Two distinct approvals required before prod promotion (test results, then promotion itself). | built |
| usage-monitor | Cross-cutting — observes all gates | Core (infra) | None (writes `USAGE.md`/`USAGE_INDEX.md`) | None | Read, Write, CronCreate | Always | Tracking/estimation/soft-budget, plus auto-pause/durable-resume (2026-07-09, verified with a real 3-minute cron test). Trigger is always a human signal or rate-limit-shaped error, never proactive detection. Logging is orchestrator bookkeeping per agent call, not a separate agent invocation. | built |
| deliverables-agent | Cross-cutting — on-demand export, never a blocking gate | Optional | None (reads others' KBs; writes one-way to `projects/<name>/deliverables/` and, for the platform-level HTML page, `admin/deliverables/`) | None | Read, Write, Bash (python-pptx/python-docx/openpyxl) | On-demand, triggered at the end of the same gate/action that updated the source markdown — not a standing file-watcher | Exports FROM markdown (architecture→PPTX, plan/design docs→DOCX, test scripts + per-scenario evidence→XLSX), one-way only — hard rule: no agent ever reads from `deliverables/`. **Verified for real (2026-07-09)**: generated actual `architecture.pptx`/`design.docx`/`test-results.xlsx` for `policy-lookup-assistant` from its real KB/PLAN/test-evidence content, re-opened and validated each with its own library (not just written-and-hoped). Roadmap/FEATURES.md Excel rollups and the platform-level HTML knowledge-base page (already shipped standalone, regeneration-wiring into this agent still pending) remain to be built. | built |
