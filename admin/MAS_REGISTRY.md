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

## How to read the two tool columns

`Tool grant` and `Scope constraint` are **different kinds of thing** and were
deliberately split apart on 2026-07-26. Conflating them is what let two real
drifts hide in plain sight.

- **`Tool grant`** is a **verbatim copy of the agent file's `tools:`
  frontmatter** — byte-comparable, nothing added, nothing paraphrased. This
  is the *only* column the contract-drift audit compares. If it doesn't match
  disk exactly, that is drift.
- **`Scope constraint`** is **advisory prose** summarising the narrowing an
  agent's own contract body imposes on that grant. It is documentation for a
  human reader. It is **never compared mechanically**, and a mismatch here is
  not drift — it is a doc-freshness question.

Two standing caveats:

- **`Bash(git)` parenthesised scoping is of unverified enforceability** in
  subagent frontmatter (that syntax belongs to the permissions system, and
  nobody has empirically tested whether it is honoured here). It appears on
  `enhance-agent` and `release-manager`. It is recorded below exactly as it
  appears on disk; until someone tests it, treat the *effective* grant as
  plain `Bash` plus the prose discipline in the Scope constraint column.
- **`DesignSync` is confirmed present** in the runtime (verified 2026-07-26).
  It is not a phantom tool; the drift audit records it `MATCH`. The
  "DesignSync unavailable" note in `admin/LESSONS.md` refers to one specific
  invocation context.

## Test-suite entry points (added 2026-07-26, Phase 2 / B2)

Every agent in the "Owns Test Suite" column below now holds a `Bash` grant
scoped **by convention in its own contract prose** — not by parenthesised
grant syntax — to invoking exactly one path plus read-only inspection of that
run's results:

```
dev/tests/suites/<suite>/run.sh
```

The slugs are fixed: `functional` (functional-agent), `industry`
(industry-expert), `ux` (ui-ux-designer), `architecture`
(solution-architect), `security` (security-architect), `red-team`
(responsible-ai-architect). `code-agent` authors these entry points at the
Code gate for every **active** suite (executable, non-zero exit on failure,
no installs required, short-lived, never starts its own server). Until an
entry point exists, its owner reports static-review-only — and a suite once
reported "could not execute" must actually be re-run once it exists, never
waved through on the earlier static pass. `test-agent` marks every suite
`EXECUTED` / `STATIC ONLY — NOT EXECUTED` / `PARTIAL` in its per-suite report,
because an unrun suite and a passing suite were previously indistinguishable.

`Version` mirrors each agent file's `version:` frontmatter. Semver for agent
contracts: MAJOR = gate placement / core-vs-optional / KB ownership /
test-suite ownership change; MINOR = tool-grant change or new required
behaviour; PATCH = clarification.

## Registry

| Agent | Gate(s) | Core / Optional | Knowledge Base | Owns Test Suite | Tool grant | Scope constraint | Version | Re-engagement (on enhancement) | Notes | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| mas-architect | Platform-level (advisory; `/admin-panel propose-agent`) | Core (platform) | None | None | Read, Grep, Glob, WebSearch | Holds no write tool at all — advisory only. Standing contract-drift audit is report-only; never edits to fix what it finds. | 1.1.0 | N/A — platform agent | Never writes files; recommendation only. Owns the contract-drift audit: pre-flight on every `propose-agent`, and mandatory + **blocking** before any platform version cut | built |
| mas-registrar | Platform-level (`/admin-panel add-agent`) | Core (platform) | None | None | Read, Write, Edit, Glob | Writes only `admin/MAS_REGISTRY.md`, `admin/ROADMAP.md`, and platform `.claude/agents/*.md`. Fixes drift only with explicit per-item human approval — never silently reconciles. Mandatory post-write self-check on every agent file. | 1.1.0 | N/A — platform agent | Only agent that writes to this registry | built |
| mas-release-manager | Platform-level (`/admin-panel roadmap`/`release`) | Core (platform) | None | None | Read, Write, Edit | Writes `admin/ROADMAP.md`/`admin/CHANGELOG.md` only. May not cut a platform version while `mas-architect`'s drift audit has an unresolved finding. | 1.1.0 | N/A — platform agent | Distinct from project-level release-manager below | built |
| plan-agent | Plan & Backlog | Core | None | None | Read, Write, Edit, Grep, Glob | `Write` only if the target file does not exist; existing files are modified with `Edit`. Writes `PLAN.md`, appends to `PROJECT_CONTEXT.md`. Writes no source code. | 1.1.0 | Always | Drafts PLAN.md + project feature backlog/MVP. Its backlog split is a **default pre-selection, never the decision** — every feature is approved individually by the human, and deferred/recommend-reject items are always shown | built |
| code-agent | Code | Core | None | None | Read, Write, Edit, Grep, Glob, Bash | Shell confined to `projects/<name>/dev/` and its toolchain. Never `prod/`. No destructive recursive deletes outside `dev/`. No `git push` to any remote. No `git reset --hard` (release-manager's lane). No dependency installs beyond the approved PLAN/PRD or TEMPLATE_MANIFEST without flagging. Never starts a long-lived server in-turn (the process dies with the turn). Authors `dev/tests/suites/<suite>/run.sh` per active suite at the Code gate; no always-passing stubs for inactive suites. | 1.2.0 | Always | Broad `Bash` is **correct and deliberate** — the Code gate needs npm/pip/pytest/tsc/build/linters; the pre-2026-07-26 registry row (`Bash(git)`) was the wrong side of that drift and was corrected to disk, not the reverse. A real commit per coherent unit is a contract obligation on multi-part builds | built |
| test-agent | Test | Core | None | Unit/integration + post-deploy smoke | Read, Write, Edit, Bash | `Write` only if the target file does not exist — `test-evidence/` files accumulate per-scenario entries across runs and are modified with `Edit`. Runs suites; never fixes failing tests (that's feedback for code-agent). Drives Playwright **synchronously within one command invocation** — never starts the browser, simulator, or app server as a long-lived process in-turn; that lifecycle is deploy-agent's/the orchestrator's. | 1.3.0 | Always | Reports the per-suite **test-count delta** (added/removed/changed) every run, not just pass/fail — a stable-looking total can hide silently replaced coverage. Marks every suite `EXECUTED` / `STATIC ONLY — NOT EXECUTED` / `PARTIAL` (2026-07-26): an unexecuted suite and a passing suite were previously indistinguishable, which silently defeated the blocking-vs-advisory policy. Owns **rendered-UI verification** as one capability with two backends — Playwright for web (computed styles, accessibility tree, visible state, screenshots into `test-evidence/`) built now; Maestro + simulator recorded as the future native backend, not built | built |
| review-agent | Review | Core | None | None | Read, Grep, Glob, Bash | **Hard read-only.** Read-only commands only; never mutates the working tree, index, or any file; never installs; never runs servers; never runs the test suites. Permitted shell limited to git inspection (`diff`, `log`, `show`, `status`, `blame`) and read-only file inspection. Never writes or updates a project's copy manifest — checks against it only. | 1.2.0 | Always | Scope is narrow by design: code style/diff hygiene, decision-intent match, copy drift, cross-cutting consistency — does NOT re-check what the 6 test suites already cover. **Three verdicts since 2026-07-26: `approve` / `request-changes` / `escalate`.** `escalate` is for a contradiction that is not code-agent's to fix (two SME KBs disagreeing) — names both KBs, both owning agents, quotes both conflicting statements verbatim, then stops; the orchestrator re-opens Architecture or routes `/consult` to the owning SMEs. Owns the **cross-KB consistency sweep** (changed KBs by default, FULL sweep at `/cut-release`) and the **copy-drift check** against an optional `COPY_MANIFEST.md`, degrading to a Decisions-Log/`PRD.md` comparison where no manifest exists. Lane discipline is contractual: it checks consistency of the *record*, never correctness within a lane, and never adjudicates which KB is right. Corrected 2026-07-26: **both** sides were wrong (disk `Read, Bash`, registry `Read, Bash(git diff)`) — it needs `git log`/`show`/`status`, and had no `Grep`/`Glob` at all, which is the likeliest reason `Bash` got widened. Rejected alternative (drop `Bash`, orchestrator supplies a pre-computed diff) recorded in its contract so it isn't re-litigated | built |
| deploy-agent | Deploy | Core | None | None (hands smoke test to test-agent) | Read, Bash | Owns process lifecycle. Never deploys to `prod/`. Any `target_env` other than `local` must fail loudly, not silently no-op. | 1.1.0 | Always | `target_env` stubbed; only `local` implemented in MVP. Records the served **URL and a real health-check result** (endpoint, status, timestamp) in `PROJECT_CONTEXT.md`, not just ports | built |
| functional-agent | Intake (domain question, unconditional) + Plan & Backlog (devil's advocate) + Architecture (advisory review) | Optional / droppable | `knowledge/DOMAIN_KB.md` | Functional | Read, WebSearch, Write, Edit, Bash | Writes only `knowledge/DOMAIN_KB.md` and `test-evidence/`. `Write` only if the target file does not exist; existing files are modified with `Edit`. `Bash` scoped by contract prose to invoking `dev/tests/suites/functional/run.sh` + read-only result inspection: no installs, no long-lived processes, never `prod/`, no git mutation, never edits the code under test. | 1.2.0 | Only if flagged relevant | | built |
| industry-expert | Intake (industry question, unconditional) + Plan & Backlog (trend backlog) + Architecture + Review + Deploy (advisory stakeholder) | Optional / droppable | `knowledge/INDUSTRY_KB.md` | Industry/compliance | Read, WebSearch, Write, Edit, Bash | Writes only `knowledge/INDUSTRY_KB.md` and `test-evidence/`. `Write` only if the target file does not exist; existing files are modified with `Edit`. `Bash` scoped by contract prose to invoking `dev/tests/suites/industry/run.sh` + read-only result inspection: no installs, no long-lived processes, never `prod/`, no git mutation, never edits the code under test. | 1.2.0 | Only if flagged relevant | | built |
| ui-ux-designer | Experience Design (own gate, UI-bearing templates only, between Plan & Backlog and Architecture) | Core for `genai-chatbot`/`rag-knowledge-base`; not applicable for `agentic-workflow` | `knowledge/UX_KB.md` | UX/usability + accessibility | Read, Write, Edit, DesignSync, Bash | Writes `knowledge/UX_KB.md`, `design-review/`, `test-evidence/`. Never touches backend logic. `Write` only if the target file does not exist; existing files are modified with `Edit`. `DesignSync` confirmed present in the runtime (2026-07-26). `Bash` scoped by contract prose to invoking `dev/tests/suites/ux/run.sh` + read-only result inspection: no installs, no long-lived processes, never `prod/`, no git mutation, never edits the code under test — `Bash` is not a licence to build, serve, or modify the app. | 1.2.0 | Always, for UI-bearing projects | Design intent + observed post-deploy behavior logged in same KB. **A rendered mockup/preview is required before requesting approval at any visual gate** — never spec text alone | built |
| solution-architect | Architecture (joint owner with security-architect) | Optional / droppable | `knowledge/ARCHITECTURE_KB.md` | Architecture | Read, Write, Edit, Bash | Writes only `knowledge/ARCHITECTURE_KB.md` and `test-evidence/`. `Write` only if the target file does not exist; existing files are modified with `Edit`. `Bash` scoped by contract prose to invoking `dev/tests/suites/architecture/run.sh` + read-only result inspection: no installs, no long-lived processes, never `prod/`, no git mutation, never edits the code under test. | 1.2.0 | Always, on enhancement/key design decision | | built |
| security-architect | Architecture (joint owner with solution-architect) | Optional / droppable | `knowledge/SECURITY_KB.md` | Security | Read, Write, Edit, Bash | Writes only `knowledge/SECURITY_KB.md` and `test-evidence/`. `Write` only if the target file does not exist; existing files are modified with `Edit`. `Bash` scoped by contract prose to invoking `dev/tests/suites/security/run.sh` + read-only result and git-history inspection (`log`/`show`/`status`, for secrets-leak checks): no installs, no long-lived processes, never `prod/`, no git mutation — explicitly including no history rewriting to scrub a leaked secret — never edits the code under test. **B2 closed 2026-07-26: it can now execute the suite it owns.** | 1.2.0 | Always, on enhancement/key design decision | Tightened 2026-07-06: Authentication & Authorization Design is a mandatory `SECURITY_KB.md` subsection (decision + criteria + revisit triggers) — never a one-line waiver, even when the answer is "none needed" | built |
| responsible-ai-architect | Architecture (advisory, alongside solution-architect + security-architect) + Review | Optional / droppable | `knowledge/RESPONSIBLE_AI_KB.md` | Red-team/bias | Read, Write, Edit, WebSearch, Bash | Writes only `knowledge/RESPONSIBLE_AI_KB.md` and `test-evidence/`. `Write` only if the target file does not exist; existing files are modified with `Edit`. `Bash` scoped by contract prose to invoking `dev/tests/suites/red-team/run.sh` + read-only result inspection: no installs, no long-lived processes, never `prod/` (an adversarial suite is never pointed at a promoted build), no git mutation, never edits the code under test — explicitly including never patching `guardrails.py` to make its own suite pass. **B2 closed 2026-07-26**: this is the agent whose `STATIC ONLY — NOT EXECUTED` verdict, once actually run, surfaced 3 defects static review had missed. | 1.2.0 | Always, on enhancement | Content/behavior guardrails — distinct from security-architect (authn/authz/secrets) and functional-agent (domain-correctness); must not duplicate either's devil's-advocate pass | built |
| enhance-agent | Cross-cutting — drives `/enhance-project` (mini Plan→Experience Design→Architecture→Code→Test→Review→Deploy) and `/modify-feature` (correction mode) | Core (infra) | None (writes `FEATURES.md`) | None | Read, Write, Edit, Bash(git) | `Bash(git)` scoping enforceability **unverified** — treat as plain `Bash` + prose until tested. `Write` only if the target file does not exist; `FEATURES.md`/`PROJECT_CONTEXT.md` are append-targets modified with `Edit`. Never promotes to `prod/`. | 1.1.0 | N/A — this agent is the re-engagement mechanism | Owns both `/enhance-project` and `/modify-feature`; solution-architect/security-architect/responsible-ai-architect/ui-ux-designer (UI-bearing) always re-engage, functional-agent/industry-expert only if flagged | built |
| release-manager | Cross-cutting — `/cut-release` command, after Deploy | Core (infra) | None (writes `RELEASES.md`/`CHANGELOG.md`) | None | Read, Write, Edit, Bash(git) | `Bash(git)` scoping enforceability **unverified** — treat as plain `Bash` + prose until tested. `Write` only if the target file does not exist (legitimate on a project's first release); appends thereafter via `Edit`. Sole owner of `prod/` promotion and of `git reset --hard` rollback, both behind explicit human confirmation. | 1.1.0 | Always, when a release train is cut | Project-level; distinct from mas-release-manager above. Automated conflict *triage* (2026-07-09, verified for real): proximity conflicts get a lightweight confirm, semantic conflicts get full review — approval is never automated, only classification is. Two distinct approvals required before prod promotion (test results, then promotion itself). | built |
| usage-monitor | Cross-cutting — observes all gates | Core (infra) | None (writes `USAGE.md`/`USAGE_INDEX.md`) | None | Read, Write, Edit, CronCreate | `Write` only if the target file does not exist — `USAGE.md` and `memory/USAGE_INDEX.md` are cumulative ledgers a `Write` would erase; append via `Edit`. `CronCreate` used only for a one-shot durable resume at a known/estimated reset time, never speculatively. | 1.1.0 | Always | Tracking/estimation/soft-budget, plus auto-pause/durable-resume (2026-07-09, verified with a real 3-minute cron test). Trigger is always a human signal or rate-limit-shaped error, never proactive detection. Logging is orchestrator bookkeeping per agent call, not a separate agent invocation. | built |
| deliverables-agent | Cross-cutting — on-demand export, never a blocking gate | Optional | None (reads others' KBs; writes one-way to `projects/<name>/deliverables/` and, for the platform-level HTML page, `admin/deliverables/`) | None | Read, Write, Bash | `Bash` used only for python-pptx/python-docx/openpyxl work (install check + generation/validation). Writes one-way to `deliverables/` only. **Deliberately retains unrestricted `Write`** — the sole agent excluded from the 2026-07-26 `Write`→`Edit` change, because its outputs are regenerated wholesale, making overwrite correct rather than destructive. | 1.1.0 | On-demand, triggered at the end of the same gate/action that updated the source markdown — not a standing file-watcher | Exports FROM markdown (architecture→PPTX, plan/design docs→DOCX, test scripts + per-scenario evidence→XLSX), one-way only — hard rule: no agent ever reads from `deliverables/`. **Verified for real (2026-07-09)**: generated actual `architecture.pptx`/`design.docx`/`test-results.xlsx` for `policy-lookup-assistant` from its real KB/PLAN/test-evidence content, re-opened and validated each with its own library (not just written-and-hoped). Roadmap/FEATURES.md Excel rollups and the platform-level HTML knowledge-base page (already shipped standalone, regeneration-wiring into this agent still pending) remain to be built. | built |
| synthetic-data-agent | Cross-cutting — invoked just before the Test gate, or on-demand for QA/demo prep; never a new pipeline gate | Optional / droppable | `knowledge/TEST_DATA_KB.md` (data model/personas/volume presets, read-only sourced from `DOMAIN_KB.md`/`INDUSTRY_KB.md`) | None (test-agent retains sole verification ownership) | Read, Write, Edit, Bash | `Write` only if the target file does not exist — `TEST_DATA_KB.md` is append-per-run and is modified with `Edit`. `Bash` scoped strictly to invoking code-agent's `scripts/seed-data.sh reset\|reload` — no direct database or infrastructure access, and never an alternate seeding mechanism. Reads `DOMAIN_KB.md`/`INDUSTRY_KB.md` read-only. | 1.1.0 | Only if flagged relevant (new feature introduces a new data shape) | Team Composition roster option — default-on for `genai-chatbot`/`rag-knowledge-base`, default-off for `agentic-workflow`, droppable either way. Volume control: high/medium/low, recorded per generation run in `TEST_DATA_KB.md`. code-agent owns the reset/reload script mechanism; this agent owns content generation only and invokes that script, never seeds data by any other path. Approved from `mas-architect`'s 2026-07-11 advisory review; human sign-off 2026-07-12. | built |
