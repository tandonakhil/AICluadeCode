# Orchestrator Lessons

Persistent, cross-session operational knowledge — distinct from
`admin/ROADMAP.md` (what to build) and `admin/CHANGELOG.md` (what shipped).
This file is what the orchestrator has *learned by doing*. Maintained
directly by the orchestrator (see `admin/ORCHESTRATOR.md`), no agent
indirection. Append-only within each section, dated.

Three sections: **pitfalls** so a known failure mode gets caught before it
repeats, **patterns** so what's already proven gets repeated deliberately,
**feedback** as a *queue* — not an applied change. Any actual agent-contract
edit still requires `mas-architect` review and human approval per
`mas-registrar`'s guardrail; this section just makes sure a real observation
doesn't get lost before that review happens.

## Common Pitfalls

- **2026-07-06 — Flask `debug=False` caches compiled templates in memory.**
  Editing `templates/index.html` and re-curling without restarting the
  server serves the *old* render. Symptom: an edit that should be visible
  isn't. Fix: restart the Flask process after any template change; don't
  assume static-file-style hot reload.
- **2026-07-06 — `.gitignore` patterns containing a slash are relative to
  the `.gitignore` file's own location, not "anywhere in the repo."**
  `data/chroma_db/` at repo root does not match `backend/data/chroma_db/`
  two levels down — it needs the full relative path
  (`backend/data/chroma_db/`) or `**/chroma_db/`. Caught twice in this build
  (Chroma binaries, then `.env.local`) before the pattern was internalized.
  Always `git check-ignore -v <path>` after writing a new ignore rule; don't
  assume it worked.
- **2026-07-06 — LangChain's `AIMessage.content` is typed `str | list[str |
  dict]`, not always `str`.** A degenerate/repetitive prompt can make
  Anthropic return a list of content blocks; code that does
  `response.content.strip()` unconditionally will crash on exactly the kind
  of input a real user might send by accident, not just an adversarial
  case. Always normalize before calling string methods on model output.
- **2026-07-06 — CORS is not on by default and curl will never catch its
  absence.** A backend that works perfectly under `TestClient`/curl can
  still be completely broken from an actual browser if `CORSMiddleware`
  isn't configured — invisible to every non-browser verification method.
  Browser-based verification (Playwright) is not optional once a frontend
  exists.
- **2026-07-05 — A subagent given an ambiguous path reference can write to
  the wrong repo boundary.** `knowledge/*_KB.md` files were written inside
  `dev/` (the nested git repo) instead of the project root twice before the
  instruction was made explicit every time: "at PROJECT ROOT, not inside
  dev/."
- **2026-07-09 — A background process started inside a subagent's shell
  dies when that subagent's turn ends.** A Flask/uvicorn server a subagent
  starts is not still running when the orchestrator checks back later —
  always restart it from the orchestrator's own shell before relying on it.
- **2026-07-09 — An assumed fact can be wrong and cascade into wrong
  output.** Assuming "this is the project's second release" produced a
  `v1.1.0` tag for what was actually a first release, until checked against
  the real repo state. Verify background details too, not just the main
  task's own facts.

- **2026-07-11 — `responsible-ai-architect`, `security-architect`, and
  `ui-ux-designer` all lack a shell/execution tool in their `.claude/agents/`
  tool grants (`Read, Write, WebSearch` / `Read, Write` / `Read, Write,
  DesignSync`), forcing static-only review whenever their gate actually
  needs to run something live.** Hit three separate times this session
  (argon2id hash roundtrip, a `git log` secrets check, and now the full
  red-team/bias suite, which could only produce a `STATIC ONLY — NOT
  EXECUTED` verdict on 6 of 7 scenarios until the orchestrator ran them
  directly). The orchestrator closing the gap itself is a reasonable
  one-off workaround, but it means the agent that *owns* the suite never
  actually validated its own report — the orchestrator did, using tools
  outside that agent's contract. **Open — queued for `mas-architect`**:
  evaluate whether `responsible-ai-architect` (and possibly
  `security-architect`) should get a scoped `Bash` grant (or a narrower
  "run this specific test command" tool) so the owning agent can execute
  its own suite rather than only ever producing a static-review report
  that a human or the orchestrator has to separately verify.
  - **APPLIED 2026-07-26 (Phase 2).** "B2" shipped. All six suite-owning
    SMEs — `functional-agent`, `industry-expert`, `ui-ux-designer`,
    `solution-architect`, `security-architect`, `responsible-ai-architect` —
    now hold `Bash`, scoped **by convention in contract prose** (not by
    parenthesised syntax, whose enforceability here is still unverified) to
    invoking their own suite's entry point at
    `dev/tests/suites/<suite>/run.sh` plus read-only result inspection,
    following the proven `synthetic-data-agent` precedent. `code-agent` now
    carries the obligation to author those entry points at the Code gate
    (executable, non-zero exit on failure, no installs required, short-lived,
    never starts its own server), and `test-agent` must mark every suite
    `EXECUTED` / `STATIC ONLY — NOT EXECUTED` / `PARTIAL`, since an
    unexecuted suite and a passing suite were previously indistinguishable.
    Hard prohibitions on all six: no installs, no long-lived processes,
    never `prod/`, no git mutation, and **never edit the code under test**.
    Where an entry point doesn't exist yet the owner reports
    static-review-only; a suite once reported "could not execute" **must
    actually be re-run** once it exists, never waved through on the earlier
    static pass. The agent that could only return `STATIC ONLY — NOT
    EXECUTED` on 6 of 7 red-team scenarios can now run its own suite.

- **2026-07-11 — An agent with `Write` (not `Edit`) access to a large,
  append-only KB file is one misused tool call away from destroying it.**
  A `responsible-ai-architect` subagent meant to append a short
  implementation-status note to `knowledge/ARCHITECTURE_KB.md` (787 lines)
  instead called `Write` with placeholder content, wiping the whole file.
  Recoverable this time only because the file's full content happened to
  still exist in this session's own transcript/subagent logs — `knowledge/
  *_KB.md` files live at the project root, which is a git repo, but they
  are not committed after every edit the way `dev/`/`prod/` are, so there
  was no git history to fall back on. **Open — queued for `mas-architect`**:
  any agent contract granting `Write` access to a `knowledge/*_KB.md` file
  it's expected to *append to* (not create fresh) should grant `Edit`
  instead, or the orchestrator should commit `projects/<name>/` root files
  to git after every gate the same way `dev/`/`prod/` commits happen, so a
  destructive `Write` is a one-command `git checkout` away from reversible
  instead of a transcript-archaeology recovery.
  - **Recurred 2026-07-12, same project, `knowledge/UX_KB.md` this time**:
    a `ui-ux-designer` pass meant to append §7 instead called `Write` with
    content that started mid-sentence, destroying §1-§6 (458 lines of
    approved, human-reviewed design rationale). This is the SAME open
    item above, still not applied — the recommended fix (grant `Edit`,
    not `Write`, for append-to KB files) was queued 2026-07-11 and never
    landed before this recurred one day later. Recovered again via
    transcript archaeology (the pre-corruption `Write` call was still in
    this session's own subagent logs, and happened to end in the exact
    sentence the corrupted file picked up mid-word, making a byte-exact
    splice possible) — but a fix that only works "if this session's logs
    still exist" is not a fix. **Escalating, not just re-queuing**: this
    should be treated as confirmed-recurring, not hypothetical, the next
    time `mas-architect`/`mas-registrar` touch any agent's KB-file tool
    grants — `ui-ux-designer`, `solution-architect`, and any other agent
    with `Write` (not `Edit`) on a `knowledge/*_KB.md` file all carry this
    exact risk today, not just the one agent that happened to trigger it
    twice.
  - **RESOLVED 2026-07-26 — the tool-grant half is applied.** Phase 1 of
    `mas-architect`'s consolidated review shipped `Edit` to all 11
    append-target agents, each carrying the explicit rule that `Write` is
    only permitted when the target file does not exist. `deliverables-agent`
    is the one deliberate exclusion (it regenerates its outputs wholesale).
    **The git-backstop half is not yet applied**: the orchestrator does not
    yet commit `projects/<name>/` root artifacts at every gate close, and
    `mas-architect` flagged that doing so requires a real
    `git check-ignore -v` pass first (`dev/.venv/` has hundreds of files on
    disk). Also still open and recorded as a genuine policy conflict:
    `DOMAIN_KB.md` records an orchestrator-proxy KB-write policy that
    contradicts the registry's KB ownership — the recommendation is
    agent-writes-with-`Edit` and retire the proxy, but that needs to be an
    explicit recorded decision, because two contradictory policies are
    running today.

- **2026-07-11 — Never run `next build` while the same project's `next dev`
  server is running.** Both write to the same `.next/` directory; the build
  overwrites the dev server's compiled chunks, after which the dev server
  keeps serving HTML (200) whose referenced JS/CSS chunks are stale or
  missing — the page renders an unstyled shell ("Loading…" in a serif
  font, no hydration, zero API calls fired) with no error anywhere in the
  server logs. Symptom is easy to misread as a backend/auth bug. Fix:
  stop the dev server, `rm -rf .next`, restart. Prevention: verify a
  frontend change with `tsc --noEmit` while dev is running, and only run
  the full `next build` with the dev server stopped.

- **2026-07-28 — A contract can be live while the capability behind it is
  empty, and nothing reports the difference.** `test-agent` v1.3.0 made
  rendered-UI verification contractual on 2026-07-26. The F18 mobile build ran
  *under* that contract and still shipped six rendering defects, because the
  capability had exactly one built backend (Playwright) and Playwright cannot
  load a React Native tree; the native backend had been deferred when a
  toolchain spike found no simulator. The gate was satisfied, the suites were
  green, and the class of defect was **structurally uncatchable**. Fix applied:
  RNTL added as the native backend (no simulator needed, ~1s). **Prevention: when
  a contract asserts a capability, check that a backend exists for the specific
  surface in play — "the contract requires it" is not evidence the check can
  actually run.** Found by `mas-architect`, missed entirely by the orchestrator's
  own end-to-end analysis.
- **2026-07-28 — A component-rendering test proves compilation, not
  reachability.** `render(<Avatar />)` passes brilliantly while `Avatar` is
  mounted nowhere — which is exactly the defect it was written to prevent. Four
  separate defects in F18 were this shape (`Avatar`, `RemoteImage`/`Lightbox`,
  `ChatHistorySheet` — the last imported *and* state-managed *and* never
  mounted). **A reachability test must render from the screen's or app's real
  entry point and assert the component appears in the resulting tree.** This
  distinction is the difference between a guard that works and one that is
  decorative.
- **2026-07-28 — Always run a negative control before trusting a new guard.**
  A test verified only against correct code proves nothing about whether it
  detects the bug. Before committing the new reachability guards, the original
  defect was deliberately reintroduced (Avatar imported, not rendered); the guard
  failed with the correct message, and passed again on restore. Cheap, and the
  only thing that distinguishes a real guard from a passing no-op.
- **2026-07-28 — A shadow copy of the test tree silently reports every suite as
  EMPTY.** `dev/tests/<suite>/run.sh` delegated to a runner that scanned
  `dev/tests/<suite>/test_*.py`, while every real test lived under
  `dev/tests/suites/`. Result: exit 3 (`NO SCENARIOS DEFINED`) for suites that
  had passing tests. Nothing referenced the outer tree and all 24 contract and
  registry references named the inner one, so the outer was removed. **Check
  that the path an agent's tool grant is scoped to is the path the tests actually
  live at.**
- **2026-07-28 — A registry-vs-disk slug mismatch can make an agent unable to
  run its own suite.** `responsible-ai-architect`'s `Bash` grant is scoped to
  `dev/tests/suites/red-team/run.sh`; the directory on disk was `redteam`. The
  agent that owns the red-team suite could not invoke it, and nothing surfaced
  that as anything other than a missing suite. Contract, registry and
  `code-agent` all agreed on `red-team` — the disk was the outlier and was
  renamed.
- **2026-07-28 — The orchestrator's own analysis is biased toward machinery.**
  The pipeline gap analysis written by the orchestrator proposed three new agents
  and two new gates; `mas-architect` folded all three into existing agents and
  rejected the third outright for a circularity the orchestrator had not seen (an
  agent that guards the orchestrator only runs if the orchestrator invokes it).
  Its sharper point: **every gate-skip in F18 violated rules that already
  existed.** Adding rules to a system that is not executing the rules it has does
  not fix it. Prefer making non-compliance *visible to someone other than the
  non-complier* over adding another rule.

## Successful Patterns

- **Verify empirically, every time a claim is checkable.** Real `pytest`
  runs, real running servers smoke-tested with curl, real Playwright
  screenshots for anything visual — not because subagents are untrustworthy,
  but because environment-specific failures (a missing CORS header, a
  caching layer, a Python-version syntax issue) are invisible to code
  review alone and only surface under real execution.
- **When blocked by a missing tool, install the real thing rather than
  working around it.** Node.js and the `gh` CLI were both installed
  directly (via `nvm` / the official release binary) rather than substituted
  with a lesser alternative, because the actual ask ("run this for real,"
  "push to GitHub") required the real tool.
- **Route any change to the platform's own shape — new agent, changed
  contract, new cross-cutting capability — through `mas-architect` before
  building it, even when the idea seems small.** Caught real, non-obvious
  overlap and gate-placement questions every time it was actually used
  (the interactive HTML page's ownership, the Responsible AI agent's lane
  vs. `security-architect`/`functional-agent`).
- **When a subagent honestly reports a caveat or a gap ("DesignSync
  unavailable," "no OpenAI quota," "this suite is not yet applicable"),
  preserve it rather than smoothing it over.** These turned out to be some
  of the most valuable signals in the whole build, not noise to clean up.
- **Backfilling real historical data (e.g. `usage-monitor`'s token counts)
  from actual prior tool results, rather than fabricating plausible-looking
  numbers, made a "verification" step genuinely load-bearing** instead of
  theatrical.
- **2026-07-11 — A red-team/bias suite that was "STATIC ONLY — NOT EXECUTED"
  on its first pass, once actually run live, surfaced three real defects a
  thorough static code review had completely missed**: a content-type crash
  on every real call, an intermittent false-positive refusal from a broken
  regex grouping, and mid-sentence response truncation. None of these were
  guessable from reading `guardrails.py`/`prompts.py`/`llm.py` alone — they
  only existed at the intersection of the real model's actual output shape
  and the code, which is exactly the gap "verify empirically, every time a
  claim is checkable" (above) already names. Concretely reinforces: a
  suite blocked on "no API key" or "no execution tool" is not equivalent to
  a passing suite once unblocked — it should be actually re-run, not
  waved through because the static pass looked thorough.

## Sub-Agent Contract Feedback

Queue, most recent first. "Applied" = already reviewed via `mas-architect`
and edited; "Open" = observed, not yet reviewed.

- **2026-07-26 — Applied (Phase 1 contract sweep).** `mas-architect`'s
  consolidated review (`admin/proposals/2026-07-26-mas-architect-review.md`)
  was approved by the human and implemented by `mas-registrar` in one pass.
  Three long-queued items from this section landed:
  - **B1 `Write`→`Edit` — APPLIED.** The item queued 2026-07-11 and escalated
    2026-07-12 after it recurred is now actually fixed: 11 agents gained
    `Edit`, each with the rule "`Write` is permitted only when the target file
    does not exist — `Read` first; if the `Read` succeeds, `Write` is off the
    table for that path" in its Guardrails. `deliverables-agent` deliberately
    excluded (regenerates wholesale). *This is the entry that proves the
    queue's own failure mode: a correct fix sat here for one day and a KB was
    destroyed again before it landed. Queued is not applied.*
  - **B3 completeness-check — APPLIED**, and wider than queued: `plan-agent`,
    `code-agent`, `solution-architect`, `security-architect`,
    `responsible-ai-architect`, `test-agent`, `review-agent`, `deploy-agent`,
    `enhance-agent`. The wording requires the agent to **state explicitly
    which binding decisions it checked and how the output satisfies each** —
    without that, the guardrail is aspirational.
  - **B5 checkbox backlog + rendered mockup — APPLIED to contract text.** Both
    were orchestrator practice only; they are now in `plan-agent`'s and
    `ui-ux-designer`'s own contracts, so they survive a session that doesn't
    happen to remember them.

  Not landed in *this* pass but **both APPLIED later the same day** in the
  Phases 2 and 3 pass (see the `2026-07-26 — Applied (Phases 2 and 3)` entry
  further down this queue): **B2**
  scoped `Bash` for the suite-owning SMEs, and **B4** `review-agent`'s
  cross-KB sweep + `escalate` verdict.

- **2026-07-10 — Applied to orchestrator + ui-ux-designer; queued for
  broader rollout.** `ui-ux-designer`'s second revision pass (colors +
  wireframes) ran *after* the "responsive web app" platform decision was
  already recorded in `PROJECT_CONTEXT.md`'s Decisions Log, but still only
  produced mobile screens — the desktop requirement was missed a second
  time, and the human had to ask a third time before desktop layouts
  existed. Root cause: an agent's own contract only tells it to respond to
  what it's handed in the current invocation, not to re-check the full
  accumulated requirements record for anything that changed since its last
  pass. Applied directly: `admin/ORCHESTRATOR.md` (cross-check every gate
  output against the full Decisions Log before presenting for approval —
  the orchestrator has cross-gate continuity a single-invocation subagent
  doesn't) and `ui-ux-designer.md` (same self-check, agent-side). **Open —
  queued for `mas-architect`**: the same completeness-check guardrail
  likely belongs in every other gate-owning agent's contract
  (`plan-agent`, `solution-architect`, `security-architect`,
  `responsible-ai-architect`, `code-agent`) — applying it to all six at
  once is a real contract-shape change and deserves the standard review,
  not a unilateral edit under time pressure mid-pipeline.
  **Applied 2026-07-26** via the Phase 1 contract sweep, and wider than
  queued here — also added to `test-agent`, `review-agent`, `deploy-agent`,
  and `enhance-agent`, since each equally reads only its current brief.
- **2026-07-10 — Applied directly (human feedback, real-time).** At the
  Experience Design gate, the orchestrator asked for design approval from a
  text summary. Human feedback: there must be a process to review the
  design visually (wireframe page or similar) before approving. Fixed in
  `ui-ux-designer.md` (contract now requires rendered preview HTML per key
  screen assembled into `projects/<name>/design-review/index.html`) and
  `new-project/SKILL.md` step 6 (orchestrator serves that page locally and
  hands the human a URL before asking for approval — never text-only).
  Immediate remediation for little-milestones: assembled the 8 preview
  cards ui-ux-designer had already produced for DesignSync into a review
  page served at localhost:5051.
- **2026-07-10 — Applied directly (human feedback, real-time).** At the
  Plan & Backlog gate, the orchestrator presented the proposed backlog as a
  prose summary with a single approve/strike/reject question. Human
  feedback: show the *entire* feature list as a popup so each item can be
  reviewed and approved for build-now or later individually. Fixed in
  `new-project/SKILL.md` step 5: the backlog is always presented as the
  full itemized list with per-item multi-select now/later control;
  plan-agent's proposed split is the default pre-selection, never the
  decision itself.
- **2026-07-10 — Applied directly (human feedback, real-time).** The
  orchestrator asked the human to pick a template from a menu at
  `/new-project`'s very first step, before ever asking what they wanted to
  build. Human feedback: this decision belongs to an agent's judgment, not
  a cold multiple-choice question. Fixed: `plan-agent`'s contract now
  explicitly recommends a template from the request's actual description
  (reads every `TEMPLATE_MANIFEST.md`, matches described need not
  keywords); `new-project/SKILL.md` step 1 collects name + description
  only and asks the human to confirm/override a recommendation, never to
  pick blind. Note: also caught that the orchestrator had skipped a step
  the skill already documented ("if genuinely ambiguous, ask" implies
  *try to determine it first*) — a self-inflicted miss, not just a design
  gap. This one was small/mechanical enough to apply directly rather than
  queue for a separate `mas-architect` pass; larger contract changes still
  go through that review.
- **2026-07-09 — Applied.** `security-architect`: tightened to require a
  dedicated, non-collapsible "Authentication & Authorization Design"
  subsection (decision + criteria + revisit triggers) in every
  `SECURITY_KB.md`, instead of allowing a one-line "no auth needed" waiver.
- **2026-07-09 — Applied.** `test-agent` + all SME agents: added structured
  per-scenario test evidence (`test-evidence/<suite>-<date>.md`) as the
  source of record, distinct from `PROJECT_CONTEXT.md`'s narrative Test
  Results summary — feeds `deliverables-agent`'s Excel export.
- **2026-07-09 — Applied.** `functional-agent`: added an explicit
  lane-discipline note distinguishing its domain-correctness devil's-advocate
  pass from `responsible-ai-architect`'s AI-behavior-risk pass, so the two
  don't duplicate each other's work at a shared gate.
- **2026-07-26 — Applied (Phases 2 and 3).** The two items left Open after the
  Phase 1 sweep both landed in a second `mas-registrar` pass, against the same
  approved proposal (`admin/proposals/2026-07-26-mas-architect-review.md`).
  Nine contracts bumped to **v1.2.0**.
  - **B2 scoped `Bash` for the suite-owning SMEs — APPLIED.** Detailed above,
    against the 2026-07-11 pitfall it closes. *Note the same pattern the B1
    entry called out: this item was queued 2026-07-11, re-confirmed by a
    three-defect incident the same day, and only shipped on 2026-07-26. It
    stayed queued through two full contract passes.*
  - **B4 `review-agent` cross-KB sweep + `escalate` verdict — APPLIED.**
    Detailed below.
  - Also landed in the same pass (not previously in this queue): `test-agent`
    gains **rendered-UI verification** — one capability, two backends, with
    Playwright built now for web and Maestro + simulator recorded as the
    future native backend; and `review-agent` gains a **copy-drift check**
    against an optional `COPY_MANIFEST.md`, degrading to a Decisions-Log
    comparison where none exists.
  - **New pitfall recorded from the rendered-UI work**: a page can return
    `200`, contain every expected string in its source, and still render as
    something a user cannot use. A compounding-opacity bug and a set of
    layout defects reached the human because no gate rendered anything —
    HTTP responses and source greps are structurally blind to this class.
    Playwright asserting on computed styles and the accessibility tree is the
    only mechanism that sees it, which is why it is now contractual rather
    than optional.

- **Applied 2026-07-26 (Phase 3) — was Open, approved, scheduled for Phase 3.**
  `review-agent`'s scope is
  narrow by design, but its guardrail text didn't say what to do when a
  cross-cutting consistency issue spans two SME KBs written in different
  sessions (e.g. `ARCHITECTURE_KB.md` and `SECURITY_KB.md` disagreeing on a
  detail neither Architecture-gate participant caught). This is "B4" in
  `mas-architect`'s 2026-07-26 consolidated review, which reviewed and
  approved a concrete design: add a **third verdict, `escalate`** (a
  contradiction between two SME KBs is not `code-agent`'s to fix), naming
  both KBs and their owners and quoting the conflict; lane discipline holds —
  `review-agent` reports *that* they disagree, never adjudicates which is
  right; scope is changed KBs by default with a full sweep at
  `/cut-release`. **All of that is now in `review-agent`'s contract text
  (v1.2.0, 2026-07-26)** — the sweep reads every active `knowledge/*_KB.md`
  plus the Decisions Log and `PRD.md`, `escalate` must name both KBs, both
  owning agents and quote both statements verbatim before stopping, and the
  lane-discipline sentence is stated explicitly so the check doesn't grow
  into adjudication. A live instance already
  exists in the wild and is cited in the contract as the motivating example:
  `DOMAIN_KB.md` still lists native mobile under HARD
  OUT while the site's boundary lines were removed on 2026-07-25, so KB and
  site currently describe different worlds.
- **2026-07-17 — Applied (process).** Backlog approvals: the human directed
  that every backlog/MVP approval be presented as a **per-feature checkbox
  list** (AskUserQuestion with multiSelect, one checkbox per feature incl.
  deferred items so any can be pulled forward) — never a single
  approve-the-bundle question or a small set of pre-cut scope options.
  First applied at conclave-marketing's Plan & Backlog gate. Orchestrator
  practice at every Plan & Backlog gate and enhancement-scope approval;
  also queued for plan-agent's contract text at the next mas-architect pass.
  **Applied to `plan-agent`'s contract text 2026-07-26** (Phase 1 sweep):
  its proposed split is recorded as a default pre-selection and never the
  decision, with deferred and recommend-reject items always shown rather
  than filtered out before the human sees them.
- **2026-07-17 — Applied (process).** Design/mockup approvals: the human
  wants to **always review a rendered mockup/preview before approving**
  any Experience Design (or similar visual) gate — never approve from
  spec text alone. Already ui-ux-designer's own gate contract in principle
  (conclave-marketing's spec explicitly flagged "final human sign-off
  requires visual artifacts, not text alone"), but the human made it
  explicit and general: standard practice going forward for every project,
  not just when the designer happens to ask for it. Orchestrator practice:
  build/present a rendered HTML preview (design-review/ or equivalent)
  at every Experience Design gate before requesting approval; queued for
  ui-ux-designer's contract text at the next mas-architect pass so the
  requirement isn't just orchestrator-remembered.
  **Applied to `ui-ux-designer`'s contract text 2026-07-26** (Phase 1
  sweep): a rendered mockup/preview is now a hard precondition of requesting
  approval at any visual gate, and an unrenderable design must be reported
  as not ready rather than approved from text.

- **2026-07-26 — Applied (human decision, security-flagged).** Phase 2 granted
  unrestricted `Bash` to the six suite-owning SMEs (functional-agent,
  industry-expert, ui-ux-designer, solution-architect, security-architect,
  responsible-ai-architect) so they can execute the suites they own. The
  platform's automated security review **flagged this as a permission
  escalation**, correctly: the scope limit ("invoke only your own suite's
  `run.sh`") is **contract prose, not technically enforced**, because the
  parenthesised `Bash(...)` scoping syntax has unverified enforceability here
  (see the Phase 1 open finding). **Root cause of the flag was an orchestrator
  disclosure failure, not the registrar**: the human approved "Phase 2 — SME
  suite execution" from a summary that never said "six agents gain
  unrestricted shell access." The detail existed only in the proposal file.
  **Resolution**: surfaced in full to the human with the diff, the enforcement
  gap, and three options (keep / revert / orchestrator-proxy). The human
  **knowingly accepted the prose-scoped grant** on 2026-07-26, on the
  precedent that `synthetic-data-agent` and `deliverables-agent` already hold
  unrestricted `Bash` under prose scoping, and against the measured cost of
  the alternative — responsible-ai-architect's static-only pass missed three
  defects that executing the suite found.
  **Standing rule going forward**: any change that widens an agent's tool
  grant must be stated to the human *in the approval prompt itself*, naming
  the agents and the tool, not merely referenced in a proposal document. An
  approval given against a paraphrase is not an approval of the permission.
  **Still open**: `Bash(...)` enforceability remains unverified; until it is
  tested, every "scoped" Bash grant on this platform is honour-system, and the
  registry's `Scope constraint` column should be read as documentation, not
  as a control.
