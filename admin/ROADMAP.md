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

- ~~**`deliverables-agent`**~~ **Shipped (2026-07-09).** On-demand PPTX/DOCX/XLSX export generated one-way FROM `knowledge/*_KB.md`/`PLAN.md`/`test-evidence/` — markdown stays the source of truth every other agent reads, hard rule enforced: no agent ever reads from `deliverables/`. **Verified for real**: confirmed `python-pptx`/`python-docx`/`openpyxl` actually install and work in this environment, then generated genuine `architecture.pptx` (6 slides), `design.docx` (252 paragraphs, 13 headings mirroring PLAN.md's real structure), and `test-results.xlsx` (10 rows across all 3 real test-evidence files) for `policy-lookup-assistant` — each file re-opened and validated with its own library after writing, not just written-and-assumed-correct. **Remaining, not yet built**: the Excel rollups of `admin/ROADMAP.md` and each project's `FEATURES.md`, and wiring the already-shipped standalone HTML knowledge-base page's regeneration into this agent's trigger mechanism (it currently requires a manual refresh).
  - ~~**Added scope note (2026-07-09)**: a fourth export target — an **interactive HTML knowledge-base page**~~ **Shipped standalone (2026-07-09)**, decoupled from `deliverables-agent` per human decision (needed none of its Office-export tooling) — see Shipped section below. Original note preserved: documenting the MAS's end-to-end approach (pipeline stages, agent roster, templates, Admin Control Panel) generated FROM `admin/MAS_REGISTRY.md`, `admin/ROADMAP.md`, `.claude/agents/*.md`, and `.claude/skills/*/SKILL.md` — so users can click through to learn the system and see how to structure their own projects. This is `deliverables-agent`'s **first platform-level target** (everything else in its scope is per-project or a per-project rollup) — a real scope widening to call out and re-bless when this agent is actually built, not silently assumed. Regeneration trigger: end of `mas-registrar`'s `add-agent` (registry changes) and end of `mas-release-manager`'s `roadmap`/`release` (roadmap/CHANGELOG changes) — same "regenerate at the triggering write" principle as the project-level exports, no new standing service. Ship this after the simpler project-level exports/rollups are built and proven, same "prove the simple case first" sequencing already used elsewhere in this roadmap (usage-monitor tracking before auto-pause/resume; conflict detection before automated resolution).

- **Cloud `target_env` for deploy-agent** — local-only deploy proves the pipeline first; cloud auth/infra-as-code is meaningfully more work and premature before the core loop is validated.
- ~~**usage-monitor auto-pause/resume**~~ **Shipped (2026-07-09)**. Honest design constraint: no tool proactively reports remaining usage budget, so the trigger is always a human signal or a rate-limit-shaped tool error, never automatic detection. On trigger: checkpoint to the natural status file (`admin/CHANGELOG.md` or `PROJECT_CONTEXT.md`), a real one-shot `CronCreate` job for the reset time, resume reads the checkpoint and continues with normal approval gates still applying. **Verified for real**: a genuine 3-minute cron test (scheduled 20:09 CDT for 20:12 CDT) fired exactly on schedule and the resumed session continued autonomously — not simulated. Formalizes what had already been done manually twice earlier in this platform's own build.
- ~~**release-manager automated conflict resolution**~~ **Shipped (2026-07-09).** Design: automated *triage*, never automated *approval* — conflicts are classified as **proximity** (textually conflicting but no actual logical overlap; code-agent proposes a resolution and applies it, but still gets a lightweight single yes/no human confirm on the concrete diff) or **semantic** (genuine overlapping logic; unchanged full deliberative review, same as original MVP). When in doubt, treat as semantic. **Verified for real, not simulated**: deliberately created two genuinely conflicting feature branches on `load-alert-agent` (both append an independent function near the end of the same file), confirmed the real git conflict via an actual merge probe, correctly classified it as proximity, resolved it (kept both functions), ran the real test suite (1/1 pass) plus a manual functional check, and promoted to a real `prod/` (this was actually the project's first release — corrected to a `v1.0.0` baseline, matching `grid-assistant`'s own precedent, after an initial version-numbering assumption error was caught and fixed).
- **Feature flags** — **now designed (2026-07-09, via mas-architect), deliberately still deferred.** Real problem identified: today's only rollback is `git reset --hard` on an entire release train, so a bad feature can only be killed by taking down every feature bundled with it — there's no surgical per-feature kill switch. Rollout-percentage/user-targeting flags don't apply (no traffic-splitting layer for a local single-process deploy) — building those would be pure ceremony. **Recommended mechanism**: extend `release-manager` (not a new agent — no distinct gate/KB/test-suite needed), a `prod/flags.json` store, opt-in per feature (not blanket instrumentation), a toggle action that edits+commits+logs, `code-agent` wiring a guard around a flaggable feature's entry point, `deploy-agent` handling the required restart. `FEATURES.md`'s Released section gets an optional flag-state annotation sourced from `flags.json`, never a second source of truth. **Deferred deliberately**: no release has ever actually needed partial rollback — building this now would be guessing at the design's edges rather than learning them from a real failure, following the same "prove the simple case insufficient first" discipline applied to auto-pause/resume and automated conflict resolution. Build the first time a real release needs it.
- ~~**Multi-suite Test-gate override policy**~~ **Shipped (2026-07-09)**, despite no suite ever actually having blocked something the human wanted to ship — human chose to build it now rather than wait for a trigger. Design: every suite defaults to blocking (formalizing what was already implicit — the human could always approve past a failure). A project can mark specific suites **advisory** via a recorded `Test Policy` line in `PROJECT_CONTEXT.md`'s Active Team section, human decision only, reversible anytime. Advisory failures are still fully reported, just don't force a gate stop; blocking failures still stop the gate and require either a fix or an explicit `[override]`-tagged reason in the Decisions Log. Wired into `test-agent.md`, `/new-project`'s Team Composition and Test steps, and `/enhance-project`'s Test step (respects the project's existing policy unless amended). **Verified for real**: applied retroactively to `policy-lookup-assistant` (marked UX/accessibility advisory, reasoned from its own internal-tool-first framing), re-ran its real blocking suites (5/5 pass), and confirmed the report format correctly separates Blocking from Advisory without conflating them.

- ~~**`synthetic-data-agent`**~~ **Shipped (2026-07-12).** Proposed
  2026-07-11 (human request, during little-milestones' manual tester-account
  setup — a real, concrete need: a populated profile with
  memories/photos/timeline/digest content was needed to exercise every
  feature, and no agent generated that at the time). `mas-architect`
  advisory review recommended it as a good future-roadmap candidate; human
  approved it for build via checkbox backlog review on 2026-07-12. Built
  exactly per the advisory design: cross-cutting, invoked just before the
  Test gate (and on-demand for QA/demo prep) — not a new pipeline gate;
  optional/droppable at Team Composition, default-on for `genai-chatbot`/
  `rag-knowledge-base`, default-off for `agentic-workflow`; owns
  `knowledge/TEST_DATA_KB.md` (data model/personas/volume presets, read-only
  sourced from `DOMAIN_KB.md`/`INDUSTRY_KB.md`); owns no test suite
  (test-agent retains sole verification ownership); high/medium/low volume
  control recorded per generation run; Bash scoped strictly to invoking
  code-agent's `scripts/seed-data.sh reset|reload` — no direct infra/DB
  access, code-agent retains ownership of that script, this agent owns
  content generation only; re-engagement on `/enhance-project` only if
  flagged relevant (new data shape introduced), not unconditional. See
  `.claude/agents/synthetic-data-agent.md` and `admin/MAS_REGISTRY.md`.

- **Deferred from the 2026-07-28 verification-gap round** (see
  `admin/proposals/2026-07-28-pipeline-verification-gap.md`; the human's
  decision table selected N1, N2, RNTL, C1, C5, and C2 for immediate build —
  everything below was explicitly *not* selected this round, and none of it is
  rejected):
  - **C3 — rendered-output evidence required per surface named by C2's Impact
    Analysis.** A surface with no rendered evidence would report `NOT VERIFIED`
    and never be folded into a pass. Now genuinely buildable in a way it wasn't
    before: `solution-architect` v2.0.0 produces the surface list, and
    `test-agent` v1.4.0 finally has a native rendering backend to produce
    mobile evidence with. Deferred only for sequencing.
  - **C6 — promote the cross-surface parity suite into the templates**, so
    multi-surface projects get it from day one rather than having it
    hand-written per project (it was written during F18 and exists only there).
    Naturally pairs with C3 and with the multi-surface question below.
  - **`admin/PIPELINE.yaml` + `admin/PIPELINE_LOG.md`.** The human's feedback
    #5 asked for a strictly-followed workflow with a visual graph.
    `pipeline-marshal` (N3) was correctly rejected for **circularity** — the
    only way it runs is if the orchestrator invokes it, and an orchestrator
    that skips gates skips the marshal too. What survives that objection is the
    *artifacts*, not the enforcing agent: a single `PIPELINE.yaml` declaring
    gate order plus per-gate required inputs/outputs and exit criteria, with
    the workflow diagram **rendered from that same file** so picture and rule
    cannot drift; and `PIPELINE_LOG.md`, a per-project record of which gates
    actually ran, when, and with what human approval or recorded exception.
    `mas-architect`'s reasoning for why the log is the load-bearing half:
    every gate-skip in F18 violated rules that **already existed**, so the
    problem was never a missing rule — it was that non-compliance was visible
    only to the non-complier. A log makes it visible to someone else. Note the
    gate count is now **11**, not 9, so anything built here must be authored
    against the current order in `admin/MAS_REGISTRY.md`.
  - **Open structural question — "multi-surface project" as a first-class
    concept.** Raised by `mas-architect` and deliberately left open rather than
    silently resolved. This platform has no first-class notion of a project
    having multiple surfaces (web + mobile, app + public API, app + a
    data/deliverables pipeline). Defects 9 and 10 of the F18 ledger are both
    symptoms: desktop web had **zero** SME-suite coverage, and the deliverables
    sat fifteen days stale describing a web-only product. The 2026-07-28 round
    patched the *consequence* — `solution-architect` is now non-droppable for
    multi-surface projects and must produce a per-surface Impact Analysis — but
    the underlying gap is structural: templates are single-surface by
    construction, `PROJECT_CONTEXT.md` has no surface inventory, no gate
    enumerates surfaces, and "which surfaces exist" currently lives only in an
    architect's prose. Candidate directions (none chosen, none evaluated):
    a declared surface inventory in `PROJECT_CONTEXT.md` that gates read;
    multi-surface templates; per-surface test-suite instantiation. **Route
    through `mas-architect` before building anything here** — this is a
    platform-shape question, not a contract tweak.

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
  **Human decision**: reviewed the full backlog collectively afterward and
  selected 5 of 6 items to build next (all but cloud `target_env`), in a
  proposed order — see Phase 9 below.
- **Phase 9, item 1 of 5 (2026-07-09)**: shipped the **interactive HTML
  knowledge-base page** standalone, decoupled from `deliverables-agent`
  (confirmed it needed none of that agent's Office-export tooling — pure
  markdown-to-HTML, no new dependencies). Generated from
  `admin/MAS_REGISTRY.md` (18 agents, grouped core/SME/infra/platform,
  click-to-expand), the 9-gate pipeline (click-to-expand per gate, showing
  which agents act there and which are optional), the 3 templates, and every
  command from `.claude/skills/*/SKILL.md`. Published as an Artifact for
  human review; source file at `admin/deliverables/knowledge-base.html`.
  Design: schematic/blueprint-inspired palette (ink-navy ground, amber for
  gates, teal for agents, semantic status colors kept separate), monospace
  for identifiers (agent/command names read as code because they are code),
  humanist sans for prose. Both light/dark themes designed, not inverted
  naively. Regeneration note recorded in the page's own footer: regenerate
  after any registry or roadmap change (this is currently a manual step —
  the automated "regenerate at the triggering write" trigger described in
  the original scope note is `deliverables-agent`'s job once that agent
  exists; until then, treat this as a snapshot to refresh by hand).
- **`synthetic-data-agent` (2026-07-12)**: scaffolded per `mas-architect`'s
  2026-07-11 advisory review, approved via checkbox backlog review
  2026-07-12. Cross-cutting, invoked just before the Test gate or on-demand
  for QA/demo prep — not a new pipeline gate. Optional/droppable, default-on
  for `genai-chatbot`/`rag-knowledge-base`, default-off for
  `agentic-workflow`. Owns `knowledge/TEST_DATA_KB.md` only (read-only
  sourced from `DOMAIN_KB.md`/`INDUSTRY_KB.md`), owns no test suite. Bash
  scoped to invoking code-agent's `scripts/seed-data.sh reset|reload` only —
  no direct infra/DB access. See Backlog section above for the full design
  and `.claude/agents/synthetic-data-agent.md` for the built contract. Pure
  scaffolding — no project has adopted this agent yet.
- **Verification-gap round (2026-07-28)**: shipped the six items the human's
  decision table marked BUILD in
  `admin/proposals/2026-07-28-pipeline-verification-gap.md`. **Roster 19 → 21
  agents; pipeline 9 → 11 gates.** Evidence base: the little-milestones F18
  mobile build shipped ten defects, eight caught by the human on the running
  app and **zero** caught by the nine gates or six SME suites — the pipeline
  verified that code was written, never that the feature worked.
  - **`functional-design-agent` (new, v1.0.0)** — new **Functional Design**
    gate between Plan & Backlog and Experience Design; core, all templates;
    owns `knowledge/FUNCTIONAL_SPEC.md`; owns no test suite. Per-feature
    Given/When/Then acceptance criteria with **stable unique IDs**
    (`AC-F18-03`), mandatory edge/empty/error coverage, and mandatory
    **observable-UI criteria** for UI-bearing features. Lane discipline against
    `plan-agent` and `ui-ux-designer` defended in contract prose, per
    `mas-architect`'s flagged overlap risk. Human overrode the recommended
    fold.
  - **`verification-agent` (new, v1.0.0)** — new **Verification** gate between
    Test and Review; core, **blocking**, sole gate owner. Owns no KB and no
    test suite; produces a per-feature evidence matrix in
    `PROJECT_CONTEXT.md`. Unmapped acceptance criteria are `NOT VERIFIED`,
    never folded into a pass, and block back to Code. Hard read-only
    (`Read, Grep, Glob`) and contractually barred from re-reasoning about the
    code, per `mas-architect`'s cost caveat. Human overrode the recommended
    fold; blocking-not-advisory was the orchestrator determination.
  - **RNTL native rendering backend (`test-agent` v1.4.0)** —
    `mas-architect`'s strongest recommendation and absent from the original
    proposal entirely. Rendered-UI verification had exactly one built backend
    (Playwright, web-only), so F18's rendering defects were **structurally
    uncatchable** even though it ran under the v1.3.0 rendered-UI contract.
    RNTL renders in-process with **no simulator required**, so the 2026-07-26
    toolchain spike's blocker doesn't apply. Maestro + simulator retained as
    the deeper future native backend, not deleted.
  - **`code-agent` v1.3.0 (C1)** — unit tests are a Code-gate deliverable in
    the implementer's own commit; every new UI component gets a reachability
    test **rendered from the real entry point**, never in isolation.
  - **`review-agent` v1.3.0 (C5)** — wiring sweep tracing from the app entry
    point through the render tree; an import is explicitly not sufficient
    evidence of reachability.
  - **`solution-architect` v2.0.0 (C2, MAJOR)** — non-droppable for any
    multi-surface project, plus a mandatory per-enhancement Impact Analysis
    whose unjustified surface omissions block the Architecture gate.
  - **Not built by decision**: `pipeline-marshal` (circularity accepted) and
    the `deliverables-agent` freshness check (an optional agent may not block a
    core gate). C3, C6, the `PIPELINE.yaml`/`PIPELINE_LOG.md` artifacts, and the
    open multi-surface structural question moved to Backlog above.
    Pure platform scaffolding — no project has run the 11-gate pipeline yet.
