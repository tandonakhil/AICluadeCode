# MAS Platform Changelog

Version history for the MAS platform itself (agent roster, pipeline shape,
templates) — distinct from any individual project's `RELEASES.md`. Maintained
by `mas-release-manager`.

## Unreleased

- **Phase 8 (2026-07-09)**: shipped `/consult` — thin router to any SME on
  demand, never touches the Active Team roster. **Original MVP scope
  (roadmap items 1-10) is now 100% shipped.** Verified with a real consult:
  `responsible-ai-architect` on `grid-assistant`'s pre-existing `/chat`
  feature, producing a genuine (not padded) finding — role-play/instruction-
  override/off-topic-drift guardrails are currently absent from the system
  prompt, logged as advisory, low-to-moderate severity, not blocking for the
  current local-only exposure. Logged correctly to `RESPONSIBLE_AI_KB.md`
  and `PROJECT_CONTEXT.md`, both tagged `[consult]`. Human chose to review
  the full backlog collectively before prioritizing further work (declined
  to pull the HTML-knowledge-base item forward ahead of schedule).
- **Phase 7 (2026-07-09)**: shipped `usage-monitor`, completing roadmap item
  9 — tracking/estimation/soft-budget only, auto-pause/resume correctly
  deferred to Backlog (needs `CronCreate`). Tracking works off real
  token-usage metadata every Agent-tool call already returns; orchestrator
  logs, `usage-monitor` analyzes. Fixed a real staleness gap found in the
  process: `/new-project` predated `responsible-ai-architect` and was
  missing it from Team Composition/Architecture/Test entirely — fixed.
  Verified with real backfilled data (`policy-lookup-assistant` ~646,833
  tokens full-team, `load-alert-agent` ~150,297 tokens core-only) rolled up
  into `memory/USAGE_INDEX.md`, then a real dry-run Team Composition
  estimate that correctly caveated its n=2 sample size and adjusted for a
  template-shape mismatch rather than extrapolating blindly. 17/18 registry
  agents `built`; only `deliverables-agent` remains (backlog). Only
  remaining MVP item: `/consult`.
- **Phase 6 (2026-07-09)**: shipped `release-manager` (project-level),
  completing roadmap item 8 — `/cut-release`: conflict detection + human-
  assisted resolution, semver classification, full-regression gate, local
  git-remote-merge promotion to `prod/`, two distinct required approvals.
  Verified with a real first release: `grid-assistant` `v1.0.0` — `prod/`
  created fresh, tagged, `pytest` green both on the release branch and
  independently inside `prod/`'s own venv, real `uvicorn` smoke test against
  the promoted tree. 16/18 registry agents `built`; remaining: `usage-monitor`
  (next), `deliverables-agent` (backlog).
- **Phase 5 (2026-07-09)**: shipped `enhance-agent` (`/enhance-project` +
  `/modify-feature`), completing roadmap item 7. Mini gated pipeline reuses
  the full stage lineup (Plan & Backlog → Experience Design → Architecture →
  Code → Test → Review → Deploy) scoped to one feature at a time.
  Re-engagement rule: solution-architect/security-architect/
  responsible-ai-architect always re-engage on enhancements; ui-ux-designer
  always re-engages for UI-bearing projects; functional-agent/industry-expert
  only if flagged relevant. 15/18 registry agents now `built`; remaining:
  `release-manager` (next), `usage-monitor`, `deliverables-agent` (backlog).
  Verified with a real `/enhance-project` run against `grid-assistant`
  (`GET /regions` endpoint, merged `84cffcc`) — a deliberately awkward edge
  case (project predates Team Composition, no recorded roster) that
  confirmed the re-engagement rule holds and that `ui-ux-designer`/
  `responsible-ai-architect` correctly decline to fabricate work when a
  feature has nothing in their lane, rather than padding the record.
- **Roadmap addition (2026-07-09)**: interactive HTML knowledge-base page
  (end-to-end pipeline/agent-roster/template documentation for users) added
  as a scope note under `deliverables-agent`'s existing backlog entry — its
  first platform-level export target, evaluated via `mas-architect` rather
  than added as a new agent. See `admin/ROADMAP.md` Backlog section.
- **Human-requested platform additions (2026-07-06)**, routed through
  `mas-architect` via `propose-agent`/roadmap grooming, not added ad hoc.
  Paused mid-application on a usage-limit checkpoint and resumed cleanly —
  first real (informal) exercise of the pause/resume discipline
  `usage-monitor` is designed to formalize later. Shipped:
  - `/help` skill — dynamically enumerates `.claude/skills/`/`.claude/agents/`
    and `admin/ROADMAP.md`'s shipped-vs-planned status; never a hardcoded
    command list, so it can't go stale.
  - `responsible-ai-architect` — new optional SME, Architecture gate
    (advisory, alongside solution-architect + security-architect) + Review;
    owns `knowledge/RESPONSIBLE_AI_KB.md` and a red-team/bias test suite;
    always re-consulted on enhancements. Explicit lane boundaries added to
    both this agent's file and `functional-agent.md` so their two
    devil's-advocate passes at Architecture don't duplicate (domain-
    correctness risk vs. AI-behavior risk).
  - `security-architect` auth/authz scope tightened: Authentication &
    Authorization Design is now a mandatory `SECURITY_KB.md` subsection
    (decision + criteria + revisit triggers) — never a one-line waiver, even
    when the answer is "none needed." Not retrofitted to existing projects
    (`grid-assistant`, `policy-lookup-assistant`) per human decision — new
    projects only.
  - Structured per-scenario test evidence capture added to `test-agent` and
    all 5 SME agents' contracts (`projects/<name>/test-evidence/`, one file
    per suite per run) — the underlying data a future Excel export will read
    from, captured now so nothing needs reconstructing retroactively.
  - `deliverables-agent` (PPTX/DOCX/XLSX export generated one-way FROM
    markdown, auto-regenerated at each gate that updates its source, plus
    Excel rollups of `admin/ROADMAP.md` and each project's `FEATURES.md`)
    **registered as `planned`, placed in Backlog (post-MVP)** — needs new
    tooling (python-pptx/python-docx/openpyxl) the platform doesn't have yet;
    not built this round.

- Bootstrapped the Admin Control Panel (`mas-architect`, `mas-registrar`,
  `mas-release-manager`, `admin/` state, `/admin-panel` skill).
- Completed the Founding Review (2026-07-05): populated `MAS_REGISTRY.md` with
  all 16 agents (13 project-level, 3 platform-level) and `ROADMAP.md` with an
  approved MVP scope + backlog. Resolved four design gaps surfaced during
  review:
  - `/modify-feature` is owned by `enhance-agent` (lighter-weight mode of the
    same agent), not a separate agent.
  - Intake's domain/industry questions are asked unconditionally, resolving a
    circular dependency with Team Composition.
  - Core-pipeline gate owners always have final approval authority over
    advisory SME input at shared gates.
  - `review-agent`'s scope narrowed to code style/diff hygiene/decision-intent
    matching/cross-cutting consistency, to avoid re-checking what the 6
    Test-gate suites already cover.
  - Deferred to backlog: cloud `target_env`, usage-monitor's auto-pause/resume,
    release-manager's automated conflict *resolution*, feature flags.
- Shipped roadmap items 1-3 (2026-07-05): `genai-chatbot` template; core 5
  agents (`plan-agent`, `code-agent`, `test-agent`, `review-agent`,
  `deploy-agent`); `/new-project` skill running the reduced 5-stage pipeline
  (Plan & Backlog → Code → Test → Review → Deploy). Full gate order (Intake,
  Team Composition, Experience Design, Architecture) waits on roadmap items
  4-6.
- Phase 2 validation (2026-07-05): built `projects/grid-assistant/` as a real
  sample project and drove it through all 5 gates for real, with human
  approval at each boundary. Found and fixed a genuine bug along the way
  (`main.py` never called `load_dotenv()`) in both the project and the
  `genai-chatbot` template source; also corrected an overstated
  `requires-python` floor (`>=3.11` → `>=3.9`, verified working). Confirmed
  behavioral acceptance criteria against a live Anthropic API call. Pipeline
  pattern confirmed sound before Phase 3 (remaining templates).
- Phase 3 (2026-07-05): shipped `agentic-workflow` and `rag-knowledge-base`
  templates, completing roadmap item 1 (all 3 templates now exist). Both
  smoke-tested; `rag-knowledge-base`'s full ingest/embed/retrieve flow is a
  known, documented gap pending a real `OPENAI_API_KEY` — flagged in its own
  `TEMPLATE_MANIFEST.md`, not silently assumed working. Verified
  `plan-agent`'s template-selection logic against 5 sample requests spanning
  all 3 templates, including correctly flagging one as genuinely ambiguous.
- Phase 4 (2026-07-05 to 2026-07-06): shipped `ui-ux-designer`,
  `solution-architect`, `security-architect`, `functional-agent`,
  `industry-expert` — all 5 remaining SME agents, completing roadmap items
  4-6. Rewrote `/new-project` with the full 9-gate pipeline. All 16 registry
  agents are now `built`. Fully verified with two complete 9-gate sample
  projects (full-team and core-only), including retroactively invoking all
  5 SME test suites for real — which found and fixed 2 genuine bugs
  (blank-input crash, LangChain content-shape crash) plus a `.gitignore`
  pattern bug that let Chroma binary data get committed. Remaining MVP scope
  is enhance-agent, release-manager, and usage-monitor (tracking-only).
