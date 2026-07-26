# MAS Platform Changelog

Version history for the MAS platform itself (agent roster, pipeline shape,
templates) — distinct from any individual project's `RELEASES.md`. Maintained
by `mas-release-manager`.

## Unreleased

- **Phase 1 contract sweep (2026-07-26)** — one `mas-registrar` pass
  implementing `mas-architect`'s consolidated review
  (`admin/proposals/2026-07-26-mas-architect-review.md`), approved by the
  human on 2026-07-26. **Closes the 2026-07-20 proposal's P1 item 1 in full.**
  All 19 agent contracts touched; every one bumped to **v1.1.0**.

  - **B1 — the KB-destruction fix (shipped first, before anything else).**
    A `Write` on an append-target knowledge base destroyed
    `ARCHITECTURE_KB.md` (787 lines, 2026-07-11) and `UX_KB.md` (458 lines,
    2026-07-12), one day apart; both recoveries depended on session
    transcripts still existing, which is not a fix. Eleven agents' tool grants
    now include `Edit` — `ui-ux-designer`, `solution-architect`,
    `security-architect`, `responsible-ai-architect`, `functional-agent`,
    `industry-expert`, `synthetic-data-agent`, `plan-agent`, `enhance-agent`,
    `release-manager`, `usage-monitor` — each with the rule added verbatim to
    its Guardrails: **`Write` is permitted only when the target file does not
    exist; `Read` first, and if the `Read` succeeds, `Write` is off the table
    for that path.** `deliverables-agent` was **deliberately excluded** — its
    outputs are regenerated wholesale, so `Write` is semantically correct
    there; the exclusion is recorded in its own change history so it doesn't
    read as an oversight later.
  - **A1 — two drift corrections.** `code-agent`: the **registry** was wrong,
    not the agent — its broad `Bash` is correct (the Code gate needs
    npm/pip/pytest/tsc/build/linters, and `Bash(git)` would have broken it
    immediately), so the registry row was corrected to disk and shell
    discipline was added as contract prose instead (confined to `dev/`, never
    `prod/`, no destructive recursive deletes outside `dev/`, no `git push`,
    no `git reset --hard`, no unapproved dependency installs, no long-lived
    servers started in-turn). `review-agent`: **both sides were wrong** —
    disk had `Read, Bash`, the registry had `Read, Bash(git diff)`; both are
    now `Read, Grep, Glob, Bash` with hard read-only discipline. It needs
    `git log`/`show`/`status`, not just `diff`, and it had no `Grep`/`Glob`
    at all — likely why `Bash` got widened in the first place. The rejected
    alternative (drop `Bash`; orchestrator hands it a pre-computed diff) is
    recorded in its contract so it isn't re-litigated.
  - **A2 — registry column split.** `admin/MAS_REGISTRY.md`'s single `Tools`
    column mixed enforceable frontmatter grants with prose-only scoping
    annotations, which is how the two drifts hid in plain sight — 8 further
    rows had the same defect. Split into **`Tool grant`** (verbatim
    frontmatter, byte-comparable, the only column the audit compares) and
    **`Scope constraint`** (advisory prose from the contract body, never
    compared mechanically). Every one of the 19 `Tool grant` cells now
    reflects what is actually on disk.
  - **A3 — prevention machinery.** `mas-architect` gains a standing
    contract-drift audit duty (Glob agent files, extract `name`/`tools`,
    compare against the registry's `Tool grant` and `status`, emit one row per
    agent verdicted MATCH / DRIFT / MISSING ON DISK / ORPHAN / UNRESOLVABLE;
    report-only, never edits) run as pre-flight on every `propose-agent` and
    **mandatory + blocking before any platform version cut** — mirrored as a
    guardrail in `mas-release-manager`. `mas-registrar` gains a `verify`
    action running the same comparison (fixes require explicit per-item human
    approval; silent reconciliation is prohibited, since it destroys the
    evidence that something went wrong) and a **mandatory post-write
    self-check**: re-`Read` every agent file written, echo its frontmatter
    verbatim, confirm it equals the approved contract. Real contract
    versioning added throughout: `version:`/`updated:` frontmatter, a trailing
    `## Change history` table per agent, and a `Version` column in the
    registry, with semver defined for contracts (MAJOR = gate/core-optional/
    KB/test-suite ownership change; MINOR = tool grant or new required
    behaviour; PATCH = clarification). All 19 agents backfilled to `1.0.0`
    against their real build dates from `admin/ROADMAP.md`'s Shipped section,
    then bumped to `1.1.0` for this pass.
  - **A4 — 7th standard contract question.** `mas-architect` must now answer
    **interruption behaviour** for every agent it evaluates: what the agent
    does if cut off mid-task and how a resumed invocation recovers. The
    corresponding uniform clause was rolled into every write-capable agent —
    declare the intended write set up front; never leave a reference to a file
    that does not exist yet; checkpoint per coherent unit; on resume re-read
    actual on-disk state rather than assuming the prior turn's intended state.
    `code-agent`'s **phased commits** (a real commit per coherent unit on any
    multi-part build) landed as the Code-gate instance of the same rule, now
    an explicit obligation rather than a style preference.
  - **B3 — completeness-check rollout**, wider than originally queued: added
    to `plan-agent`, `code-agent`, `solution-architect`, `security-architect`,
    `responsible-ai-architect`, `test-agent`, `review-agent`, `deploy-agent`,
    `enhance-agent` (`ui-ux-designer` already carried it from 2026-07-10). The
    load-bearing part is that the agent must **state explicitly which binding
    decisions it checked against and how its output satisfies each** —
    otherwise the guardrail is aspirational.
  - **B5 — two standing human rules moved from orchestrator practice into
    contract text.** `plan-agent`: the per-feature checkbox backlog split is a
    **default pre-selection, never the decision** — the human approves every
    feature individually, and deferred/recommend-reject items are always
    shown, never filtered out before the human sees them. `ui-ux-designer`: a
    rendered mockup/preview is **required** before requesting approval at any
    Experience Design or similar visual gate; approval is never requested from
    spec text alone.
  - **Smaller selected items.** `deploy-agent` now records the served URL and
    a real health-check result (endpoint, status, timestamp) in
    `PROJECT_CONTEXT.md`, not just assigned ports. `test-agent` now reports the
    per-suite **test-count delta** (added / removed / changed) each run —
    a plausible-looking total can hide silently replaced coverage.
  - **Two findings resolved, one still open.** `DesignSync` was flagged as a
    possible phantom tool; it is **confirmed present** in the runtime and is
    recorded normally (the `admin/LESSONS.md` "DesignSync unavailable" note
    refers to one invocation context, not to the tool's absence). Still
    unverified: whether `Bash(git)` parenthesised scoping is honoured in
    subagent frontmatter — it affects `enhance-agent` and `release-manager`,
    is recorded exactly as it appears on disk, and must be treated as plain
    `Bash` plus prose discipline until tested empirically.
  - **Not in this pass, by design**: B2 (scoped `Bash` so suite-owning SMEs
    can execute their own suites) and B4 (review-agent cross-KB sweep with an
    `escalate` verdict) remain approved and scheduled for Phase 2/3; the
    PRD/plan-agent expansion, mobile, and cloud `target_env` are later phases.
    `admin/ROADMAP.md` was deliberately left untouched — that is
    `mas-release-manager`'s lane.

- **`synthetic-data-agent` scaffolded (2026-07-12)**: new optional
  cross-cutting agent, added via `/admin-panel add-agent` after
  `mas-architect`'s 2026-07-11 advisory review and human approval via
  checkbox backlog review on 2026-07-12. Generates realistic synthetic
  test/demo data (personas/records at a chosen high/medium/low volume),
  invoked just before the Test gate or on-demand for QA/demo prep — not a
  new pipeline gate. Optional/droppable at Team Composition, default-on for
  `genai-chatbot`/`rag-knowledge-base`, default-off for `agentic-workflow`.
  Owns `knowledge/TEST_DATA_KB.md` only (read-only sourced from
  `DOMAIN_KB.md`/`INDUSTRY_KB.md`); owns no test suite (test-agent retains
  sole verification ownership). Tools scoped tightly: Bash usage limited to
  invoking code-agent's own `scripts/seed-data.sh reset|reload` — no direct
  infra/DB access, code-agent keeps ownership of that script. Re-engages on
  `/enhance-project` only if flagged relevant (new data shape introduced).
  Added `.claude/agents/synthetic-data-agent.md`; registry row added at
  `built`; roadmap entry moved from Backlog to Shipped. Pure scaffolding —
  no project has adopted this agent yet.
- **Orchestrator role write-up + LESSONS.md (2026-07-10)**: formalized the
  previously-implicit orchestrator role (the main conversation, not a
  registered agent) as a documented contract at `admin/ORCHESTRATOR.md` —
  what it does, what it explicitly delegates rather than doing itself, and
  why it isn't and can't be a subagent (it's the caller, not a callee).
  Added `admin/LESSONS.md`: a persistent, cross-session log distinct from
  `ROADMAP.md`/`CHANGELOG.md` — pitfalls, proven patterns, and a
  sub-agent-contract-feedback queue (observations pending `mas-architect`
  review, not silently-applied changes). Seeded with real material from
  this build rather than placeholders: 7 pitfalls (Flask template caching,
  gitignore slash-anchoring, LangChain `content` shape, missing CORS,
  wrong-repo-boundary writes, subagent-shell process death, unverified
  assumptions), 5 proven patterns, and 4 contract-feedback entries (3
  applied, 1 still open). Cross-referenced from `CLAUDE.md` and
  `MAS_REGISTRY.md`.
- **KB site v3 — "The Signal Path" (2026-07-10)**: full visual redesign after
  the human rejected v2 as "vanilla," benchmarked against a premium
  reference site (heavn-one.webflow.io) the human supplied. Process:
  researched the reference (WebFetch), engaged `ui-ux-designer` for a
  concrete design spec (saved at `admin/kb-server/DESIGN_SPEC.md`), then
  `code-agent` implemented it — the platform's own agents doing the
  platform's own work, now invoked as first-class registered agent types.
  Design thesis: *the site IS a signal traveling through a machine* — a
  scroll-driven signal line threads the page, gates render as aperture
  slits, agents as conic-gradient irises. Dark-only (light theme
  deliberately deleted per spec), ember/arc dual accents, viewport-scale
  display type, hero particle-beam canvas (9 slits dev / 5 admin),
  scroll-ignited pipeline stations with a sticky mini-map, instrument-rack
  roster with a shared inspector panel, terminal-ledger console. Verified
  with real Playwright screenshots of both tabs; found and fixed one layout
  collision (ghost numeral vs. station tag) plus a Flask template-caching
  gotcha (debug=False caches compiled templates in memory — server restart
  required after template edits). Server: `admin/kb-server`, port 5050.
- **Post-Phase-9, visual pass (2026-07-09)**: added a signature hero
  visual — a canvas-drawn "orbit" diagram directly representing the
  pipeline (a pulsing core node with 9 satellite gate nodes on a ring,
  directional light-pulses traveling the ring), asymmetric hero layout
  (text left, orbit right, not centered). Added: count-up stat animation
  on scroll-into-view, scroll-reveal fade/rise for every section, a subtle
  SVG grain/noise texture overlay for tactile depth, distinct geometric
  glyph icons per agent-roster tier (square/diamond/hexagon/circle —
  reinforces hierarchy, not decoration), stronger accent-colored glow
  shadows on panel/gate hover, and flow-connector notches between pipeline
  gate boxes. All verified via real Playwright screenshots in both themes
  with console/page-error capture (none found) — not just visually
  eyeballed once.
- **Post-Phase-9 (2026-07-09)**: redesigned the knowledge-base page as a
  two-tab experience (Developers / Admins) and moved it from a static
  Artifact to a real local Flask server at `admin/kb-server/` (`app.py`,
  `templates/index.html`, `requirements.txt`; run with `python app.py`,
  serves on `127.0.0.1:5050`). New "web 4.0" visual identity: deep
  indigo-black ground, ambient canvas particle field (agents-as-nodes,
  respects `prefers-reduced-motion`), dual signal accents — amber for
  Developers, cyan for Admins — that switch with the active tab as a
  functional (not decorative) "which mode am I in" signal. Developers tab:
  what the harness is, pipeline overview, full lifecycle walkthrough,
  commands, how to use `/help`. Admins tab: Admin Panel governance flow,
  agent roster, a capabilities matrix (can-do/cannot-do per layer), and a
  new "how to report or fix an issue" section routing bugs/gaps/backlog
  items to their correct real path. **Verified for real**: ran the actual
  Flask server, confirmed clean logs and a 200 response, then used
  Playwright to screenshot both tabs in both themes and confirm the gate
  click-to-expand interaction actually works — not just described. Known
  follow-up, not yet done: wiring this page's regeneration into
  `deliverables-agent`'s trigger (content is still hand-embedded, same
  limitation the original standalone Artifact version had).
- **Phase 9, item 6/6 (2026-07-09)**: shipped `deliverables-agent` — the
  heaviest lift of the batch, first agent needing third-party libraries.
  Verified for real: confirmed python-pptx/python-docx/openpyxl actually
  install and work here, then generated genuine PPTX/DOCX/XLSX files for
  `policy-lookup-assistant` from its real markdown, each re-opened and
  validated with its own library after writing. Remaining: Excel rollups of
  the roadmap/FEATURES.md, and wiring the standalone HTML page's
  regeneration into this agent (currently manual refresh). **All 6 selected
  backlog items now shipped** (feature flags scoped-but-deferred per human
  agreement, the other 5 fully built and verified).
- **Phase 9, item 5/5 (2026-07-09)**: shipped `release-manager`'s automated
  conflict resolution — proximity vs. semantic classification, lightweight
  confirm for the former, full review unchanged for the latter, approval
  never automated. Verified for real: created two genuinely conflicting
  features on `load-alert-agent`, confirmed the conflict via an actual git
  merge probe, correctly classified and resolved it, real test pass, real
  promotion to a corrected `v1.0.0` baseline in `prod/` (this was actually
  the project's first release — an initial version-numbering assumption
  error was caught and fixed rather than left inconsistent). **All 5
  selected backlog items now shipped.**
- **Phase 9, item 4/5 (2026-07-09)**: shipped `usage-monitor`'s
  auto-pause/durable-resume capability — `CronCreate` added to its tool
  grant, honest design around the real constraint that no tool reports
  remaining usage budget proactively (the trigger is always a human signal
  or a rate-limit-shaped tool error, never proactive detection). On trigger:
  checkpoint written to whichever file is already the natural status
  record (`admin/CHANGELOG.md` for platform work, `PROJECT_CONTEXT.md` for
  project work), a one-shot `CronCreate` job scheduled for the known/
  estimated reset time, resume reads the checkpoint and continues exactly
  where it left off with normal approval gates still applying. **Verified
  for real, not simulated**: scheduled a genuine one-shot cron at 20:09 CDT
  for 20:12 CDT (3-minute real-time test), it fired exactly on schedule,
  and the resumed session read this checkpoint and continued autonomously.
  This formalizes what had already been done manually twice earlier in this
  platform's own build (informal checkpoints resumed on a human "continue"
  message) into an actual scheduled mechanism.
- **Phase 9, item 3/5 (2026-07-09)**: shipped the multi-suite Test-gate
  override policy — suites default blocking, a project can mark specific
  ones advisory (human decision, recorded, reversible), blocking failures
  still require a fix or an explicit `[override]`-tagged reason. Wired into
  `test-agent.md`, `/new-project`, `/enhance-project`. Verified for real:
  applied to `policy-lookup-assistant` (UX/accessibility marked advisory),
  re-ran its real blocking suites (5/5 pass), confirmed correct report
  separation.
- **Phase 9, item 2/5 (2026-07-09)**: scoped feature flags via `mas-architect`
  — real problem identified (surgical per-feature rollback inside a bundled
  release, not rollout %/targeting, which doesn't apply to local deploys),
  mechanism designed (extend `release-manager`, `prod/flags.json`, opt-in
  per feature), deliberately **not built**: no release has ever needed
  partial rollback yet, and building ahead of a real trigger risks getting
  the design's edges wrong. Human agreed to defer after hearing the
  reasoning. See `admin/ROADMAP.md` Backlog section for the full design,
  ready to build the first time it's actually needed.
- **Phase 9, item 1/5 (2026-07-09)**: shipped the interactive HTML
  knowledge-base page, decoupled from `deliverables-agent` (needed none of
  its Office-export tooling). Source at `admin/deliverables/knowledge-base.html`,
  published as an Artifact. Click-to-expand pipeline gates and agent cards,
  generated from real registry/skill data. Human selected 5 of 6 backlog
  items to build next; this is item 1 of 5.
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
