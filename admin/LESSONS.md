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
- **Open — not yet applied.** `review-agent`'s scope is narrow by design,
  but its guardrail text doesn't yet say what to do when a cross-cutting
  consistency issue spans two SME KBs written in different sessions (e.g.
  `ARCHITECTURE_KB.md` and `SECURITY_KB.md` disagreeing on a detail neither
  Architecture-gate participant caught). Flagged for a future
  `mas-architect` pass.
