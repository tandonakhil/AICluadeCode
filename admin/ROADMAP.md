# MAS Platform Roadmap

Prioritized, dependency-ordered backlog for the MAS platform itself — distinct
from any individual project's feature backlog (see `projects/<name>/FEATURES.md`
for that). Populated by `mas-architect`'s Founding Review, approved 2026-07-05,
groomed afterward via `/admin-panel roadmap`.

## MVP Scope (approved for v1)

Ordered so nothing depends on something listed after it. Each item is built
one at a time via `/admin-panel add-agent`, even though the whole set was
approved together.

1. ~~**Templates** — `genai-chatbot`, `agentic-workflow`, `rag-knowledge-base` scaffolds.~~ **Shipped** (Phases 1, 3).
2. ~~**Core pipeline agents, in gate order** — `plan-agent` → `code-agent` → `test-agent` → `review-agent` → `deploy-agent`.~~ **Shipped** (Phase 1).
3. ~~**`/new-project` skill** — orchestrates Intake → Team Composition → Plan & Backlog → Experience Design (UI-bearing only) → Architecture → Code → Test → Review → Deploy.~~ **Shipped**, full gate order (Phase 4).
4. ~~**ui-ux-designer** — non-droppable for UI-bearing templates.~~ **Shipped** (Phase 4).
5. ~~**solution-architect + security-architect** — joint Architecture gate.~~ **Shipped** (Phase 4).
6. ~~**functional-agent + industry-expert** — Intake/Plan & Backlog/Architecture SMEs.~~ **Shipped** (Phase 4).
7. ~~**enhance-agent + `/enhance-project` + `/modify-feature`** — reuses every agent above; enhance-agent owns both skills.~~ **Shipped** (Phase 5).
8. ~~**release-manager (project-level) + `/cut-release`** — conflict *detection* and dev→prod promotion via git-remote-merge are in MVP; automated conflict *resolution* is deferred (see Backlog).~~ **Shipped** (Phase 6).
9. ~~**usage-monitor — tracking, estimation, and soft-budget warnings only.** Auto-pause/resume is deferred (see Backlog).~~ **Shipped** (Phase 7).
10. ~~**`/consult` skill** — thin router to any agent + its KB; depends on the full roster existing.~~ **Shipped** (Phase 8). **Original MVP scope (items 1-10) is now 100% complete.**

## Backlog (post-MVP)

- **`deliverables-agent`** — on-demand PPTX/DOCX/XLSX export generated one-way FROM `knowledge/*_KB.md`/`PLAN.md`/`test-evidence/` (never the reverse — markdown stays the source of truth every other agent reads). Auto-regenerates at the end of the same gate that updated its source markdown, not via a standing file-watcher. Also produces an Excel rollup of `admin/ROADMAP.md` (platform-wide tracking) and each project's `FEATURES.md` (per-project tracking). Needs new tooling (python-pptx/python-docx/openpyxl) the platform doesn't have yet — first agent requiring third-party libraries beyond what's already in use. Placed after `/consult`: heaviest lift of the human-requested 2026-07-06 additions, nothing else depends on it. Hard rule if built: no agent ever reads from `deliverables/`.
  - **Added scope note (2026-07-09)**: a fourth export target — an **interactive HTML knowledge-base page** documenting the MAS's end-to-end approach (pipeline stages, agent roster, templates, Admin Control Panel) generated FROM `admin/MAS_REGISTRY.md`, `admin/ROADMAP.md`, `.claude/agents/*.md`, and `.claude/skills/*/SKILL.md` — so users can click through to learn the system and see how to structure their own projects. This is `deliverables-agent`'s **first platform-level target** (everything else in its scope is per-project or a per-project rollup) — a real scope widening to call out and re-bless when this agent is actually built, not silently assumed. Regeneration trigger: end of `mas-registrar`'s `add-agent` (registry changes) and end of `mas-release-manager`'s `roadmap`/`release` (roadmap/CHANGELOG changes) — same "regenerate at the triggering write" principle as the project-level exports, no new standing service. Ship this after the simpler project-level exports/rollups are built and proven, same "prove the simple case first" sequencing already used elsewhere in this roadmap (usage-monitor tracking before auto-pause/resume; conflict detection before automated resolution).

- **Cloud `target_env` for deploy-agent** — local-only deploy proves the pipeline first; cloud auth/infra-as-code is meaningfully more work and premature before the core loop is validated.
- **usage-monitor auto-pause/resume** (Claude-Code-usage-limit detection + `CronCreate`-based durable resume) — the riskiest, most novel part of usage-monitor's spec (external scheduling, checkpoint/resume correctness under a hard cutoff). Ship tracking/estimation/soft-budgets first; add this once that's proven in real use.
- **release-manager automated conflict resolution** — detection + human-assisted resolution is MVP; having code-agent auto-propose merges for conflicting hunks is a harder problem, deferred until manual handling shows where automation actually helps.
- **Feature flags** — not designed anywhere yet (no owning agent, no KB). Not "deferred" so much as undesigned; if wanted later, route it through `/admin-panel propose-agent` as a new capability rather than assuming it into release-manager's scope.
- **Multi-suite Test-gate override policy** — MVP ships a simple "all present suites must pass" rule; per-suite override/advisory-vs-blocking policy is a design question to revisit only if the simple rule proves too strict in practice.

## Shipped

- **Phase 0 (2026-07-05)**: Admin Control Panel bootstrap — `mas-architect`,
  `mas-registrar`, `mas-release-manager`, `admin-panel` skill, `admin/` state
  files, root `CLAUDE.md`, `.gitignore`, empty `templates/`/`projects/`/`memory/`.
- **Phase 0.5 (2026-07-05)**: Founding Review completed and approved — full
  registry and this roadmap established; four design gaps resolved (see
  `admin/CHANGELOG.md`).
- **Phase 1 (2026-07-05)**: `genai-chatbot` template scaffolded (roadmap item
  1); core 5 agents built in gate order — `plan-agent`, `code-agent`,
  `test-agent`, `review-agent`, `deploy-agent` (item 2); `/new-project` skill
  built running the reduced 5-stage pipeline (item 3, full gate order pending
  items 4-6).
- **Phase 2 (2026-07-05)**: validated the reduced 5-stage pipeline end-to-end
  with a real sample project, `grid-assistant` (mock grid-data chatbot
  feature) — all 5 gates run for real with human approval at each boundary,
  including a genuine mid-pipeline bug found and fixed (`main.py` missing
  `load_dotenv()`, fixed in both the project and the upstream template) and a
  real behavioral test pass against a live Anthropic API call, not simulated.
  Core pipeline pattern (§4b of the design) confirmed sound before building
  the remaining two templates.
- **Phase 3 (2026-07-05)**: `agentic-workflow` (FastAPI + LangGraph, API-only)
  and `rag-knowledge-base` (Next.js + FastAPI + LangChain + Chroma) templates
  built, completing roadmap item 1. Both smoke-tested in throwaway venvs:
  `agentic-workflow`'s `/health` test passes and its LangGraph
  `create_react_agent` wiring builds successfully without a real key;
  `rag-knowledge-base`'s `/health` test passes and document loading/chunking
  verified deterministically, but the full ingest→embed→retrieve→answer flow
  remains unverified pending a real `OPENAI_API_KEY` (embeddings are
  OpenAI-only regardless of chat provider — flagged in the template's own
  manifest as a known gap, not silently assumed working). Verified
  `plan-agent`'s template-selection logic across all 3 templates with 5 test
  requests — 4 correct, unambiguous picks and 1 correctly flagged as
  genuinely ambiguous (asked rather than guessed), confirming the guardrail
  behavior works as designed.
- **Phase 4 (2026-07-05 to 2026-07-06)**: shipped all 5 remaining SME agents —
  `ui-ux-designer`, `solution-architect`, `security-architect`,
  `functional-agent`, `industry-expert` — completing roadmap items 4-6.
  `/new-project` skill rewritten with the full gate order. All 16 registry
  agents now `built`. **Full verification** (two complete 9-gate sample
  projects, not the lighter option): `policy-lookup-assistant`
  (rag-knowledge-base, full team — all 5 SMEs meaningfully engaged, real
  research, real design, a genuine cross-role disagreement surfaced and
  resolved) and `load-alert-agent` (agentic-workflow, core-only — all 4
  optional SMEs correctly dropped, `ui-ux-designer`/Experience Design
  structurally absent for the API-only template, not just declined).
  Retroactively closed a gap in the first pass: the multi-suite Test gate
  mechanism itself wasn't actually exercised (only test-agent's suite had
  run) — invoked all 5 SME test suites for real against
  `policy-lookup-assistant`, which surfaced and fixed **two real bugs**
  (an unhandled 500 on blank/whitespace input, and a LangChain
  `AIMessage.content` list-vs-string shape crash on a degenerate boundary
  input) plus a git-hygiene fix (Chroma binary data wrongly tracked due to a
  `.gitignore` pattern bug, fixed in both the project and the template
  source). This is the clearest evidence yet that the multi-suite design is
  pulling its weight, not just adding process for its own sake.
- **Human-requested additions (2026-07-06)**, routed through `mas-architect`
  via `propose-agent` rather than added ad hoc: `/help` skill (dynamically
  enumerates `.claude/skills/`/`.claude/agents/` — never a hardcoded list);
  `responsible-ai-architect` (new SME, Architecture gate advisory + Review,
  content/behavior guardrails distinct from security-architect's authn/authz
  and functional-agent's domain-correctness lanes — explicit no-duplication
  notes added to both agents' files); `security-architect`'s auth/authz
  scope tightened (Authentication & Authorization Design is now a mandatory
  `SECURITY_KB.md` subsection — decision + criteria + revisit triggers,
  never a one-line waiver); structured per-scenario test evidence capture
  (`projects/<name>/test-evidence/`) added to `test-agent` and all 5 SME
  agents' contracts, laying the groundwork `deliverables-agent`'s future
  Excel export will read from. `deliverables-agent` itself deferred to
  Backlog (post-MVP) — see above.
- **Roadmap addition (2026-07-09)**: interactive HTML knowledge-base page
  added as `deliverables-agent`'s first platform-level export target — see
  Backlog section above for full detail.
- **Phase 5 (2026-07-09)**: shipped `enhance-agent`, completing roadmap item
  7 — owns both `/enhance-project` (new feature on a deployed project) and
  `/modify-feature` (lighter-weight correction mode targeting an existing
  `FEATURES.md` entry). Mini gated pipeline: Plan & Backlog → Experience
  Design (if UI-bearing) → Architecture (lighter-touch) → Code → Test →
  Review → Deploy, same human-approval-at-every-boundary discipline as
  `/new-project`. Re-engagement rule enforced: solution-architect,
  security-architect, and responsible-ai-architect always re-engage on any
  enhancement regardless of original Team Composition roster; ui-ux-designer
  always re-engages for UI-bearing projects; functional-agent/industry-expert
  only if flagged relevant. 15/18 registry agents now `built`; remaining
  `planned` (at the time): `release-manager`, `usage-monitor`,
  `deliverables-agent` — `release-manager` shipped in Phase 6, below.
  **Verified for real**: ran the platform's first
  `/enhance-project` against `grid-assistant` (`GET /regions` endpoint) — a
  deliberately awkward edge case since that project predates Team
  Composition entirely (no original roster recorded). enhance-agent still
  correctly enforced the always-re-engage set while honoring the human's
  choice to leave functional-agent/industry-expert out; `ui-ux-designer` and
  `responsible-ai-architect` both correctly declined to fabricate work for a
  feature with nothing in their respective lanes to act on, rather than
  padding the record. Full mini-pipeline ran gate-by-gate with real
  approvals, real pytest (9/9), a real merge to `main`, and a real local
  redeploy + smoke test against the live process.
- **Phase 6 (2026-07-09)**: shipped `release-manager` (project-level,
  distinct from `mas-release-manager`), completing roadmap item 8. Owns
  `/cut-release`: feature-train batching from "Ready for Release,"
  pairwise conflict detection (human-assisted resolution only — automated
  resolution stays deferred per the original MVP scoping), semver
  classification, full-regression-suite gate on the merged release branch,
  local git-remote-merge promotion to `prod/`, and two distinct required
  approvals (test results, then promotion itself — never collapsed into
  one). **Verified for real**: cut `grid-assistant`'s first release,
  `v1.0.0` — `prod/` created fresh, `dev/` added as a local remote, merged
  and tagged, real `pytest` run on the release branch (9/9) and again
  independently inside `prod/`'s own fresh venv (9/9), and a real local
  `uvicorn` smoke test against the promoted code confirming both `/health`
  and `/regions` work from the actual `prod/` tree, not just `dev/`.
  `RELEASES.md`/`CHANGELOG.md` created with a real, reasoned v1.0.0-not-two-
  versions justification. 16/18 registry agents now `built`; remaining:
  `usage-monitor` (next, tracking-only for MVP), `deliverables-agent`
  (backlog).
- **Phase 7 (2026-07-09)**: shipped `usage-monitor` (tracking/estimation/
  soft-budget only — auto-pause/resume correctly deferred to Backlog, since
  it needs `CronCreate` which the MVP version isn't granted), completing
  roadmap item 9. Tracking works because every Agent-tool call already
  returns real token-usage metadata — the orchestrator appends one
  `USAGE.md` line per call; `usage-monitor` itself is invoked for the
  *analysis* half (pre-work estimates, cross-project rollup, soft-budget
  checks). Wired a usage-logging step and a pre-work-estimate step into
  `/new-project`'s Team Composition gate and `/enhance-project`'s
  pre-Code step; also caught and fixed a real staleness gap in
  `/new-project` — it predated `responsible-ai-architect` and was missing
  it from Team Composition/Architecture/Test gate lists entirely.
  **Verified for real**: backfilled `USAGE.md` for `policy-lookup-assistant`
  (~646,833 tokens, full team) and `load-alert-agent` (~150,297 tokens,
  core-only) from actual per-call token totals recorded during their real
  builds, rolled up into `memory/USAGE_INDEX.md`, then ran a real dry-run
  estimate for a hypothetical new UI-bearing project's Team Composition
  gate — the output was honestly caveated on n=2 sample size, correctly
  caught that `load-alert-agent`'s API-only shape wasn't a clean core-only
  comparison for a UI-bearing template (adjusted for the mandatory
  Experience Design gate), and gave a concrete, actionable recommendation
  rather than a vague estimate. 17/18 registry agents now `built`; only
  `deliverables-agent` remains, in Backlog. **Only remaining MVP item**:
  `/consult`.
- **Phase 8 (2026-07-09)**: shipped `/consult` — thin router (no owning
  agent) to any SME on demand, without waiting for or re-running a gate;
  never changes the project's Active Team roster as a side effect. **Original
  MVP scope (roadmap items 1-10) is now 100% shipped.** **Verified for
  real**: consulted `responsible-ai-architect` on `grid-assistant`'s
  original `/chat` feature (predates that agent's existence) about
  role-play/instruction-override/off-topic-drift guardrails — got a real,
  honestly-scoped answer (a genuine low-to-moderate gap identified, not
  padded, not dismissed), correctly logged to a new-or-appended
  `RESPONSIBLE_AI_KB.md` entry and `PROJECT_CONTEXT.md`'s Decisions Log,
  both tagged `[consult]`, with explicit confirmation the roster was not
  touched. The subagent also correctly identified and disregarded what
  looked like injected content in a tool result during this run, without
  acting on it — verified the underlying file was clean, no real concern,
  but good evidence the "treat fetched content as data, not instructions"
  discipline holds under a real (if likely harness-artifact) test.
  **Human decision**: the previously-added interactive-HTML-knowledge-base
  backlog item stays deferred for now — human wants to collectively review
  the full backlog before prioritizing further work, rather than pulling
  items forward piecemeal.
