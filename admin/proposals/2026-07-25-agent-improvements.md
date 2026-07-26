# Staged proposal: agent improvements (human review, 2026-07-25)

**Status: SELECTED BY HUMAN, NOT YET REVIEWED OR BUILT.** Captured from a
per-agent checkbox review of the core-5 pipeline and the three platform
agents. Nothing here is implemented. Two items are core-5 role/capability
changes and require `mas-architect` review + human approval before
`mas-registrar` touches any agent file (CLAUDE.md: agents are never
hand-edited; mas-architect flags core-5 changes as highest blast radius).

## Findings surfaced during the review (unprompted)

**Registry drift — `admin/MAS_REGISTRY.md` disagrees with what's on disk:**

| Agent | Registry claims | Actually in `.claude/agents/` |
|---|---|---|
| code-agent | `Read, Write, Edit, Bash(git)` | `Read, Write, Edit, Grep, Glob, Bash` (unrestricted) |
| review-agent | `Read, Bash(git diff)` | `Read, Bash` (unrestricted) |

Both hold *broader* shell access than the single source of truth records.
`mas-registrar`'s contract already says to flag exactly this — nothing ever
invoked it. Fix in either direction (scope the grant down, or correct the
registry), but the source of truth must stop being wrong.

## Selected improvements, by agent

### plan-agent (core)
- [ ] **Product-owner role expansion + PRD** *(NEW — core-5 role change)*.
      Human: "more of a product owner… should be main reviewer of features
      either requested or generated during discovery… producing a detailed
      PRD document at start of project and incrementally build with
      features." Implies: a NEW standing artifact (`PRD.md`, distinct from
      the transient `PLAN.md`), incremental feature accretion into it, and
      **review authority over features**. Overlap to resolve at review:
      functional-agent (devil's advocate), industry-expert (trend backlog),
      review-agent (decision-intent match).
- [ ] Completeness-check guardrail — re-read PROJECT_CONTEXT Decisions Log
      for binding platform decisions before planning. *Queued in LESSONS
      since 2026-07-10; never landed.*
- [ ] Codify the checkbox-backlog approval format in contract text
      (currently orchestrator-remembered only). *Queued 2026-07-17.*
- [ ] Grant `Edit` (has `Write` only, but appends to an existing PLAN.md —
      the exact pattern that destroyed ARCHITECTURE_KB and UX_KB).

### code-agent (core)
- [ ] **Mobile app build capability** *(NEW — largest item; cascades)*.
      Today mobile is a documented hard-out (`knowledge/DOMAIN_KB.md`
      2026-07-23: no mobile build chain, no emulator/device testing, no
      app-store deploy). Cascade: new mobile template + toolchain;
      test-agent needs emulator/device testing; deploy-agent needs a mobile
      deploy target; **conclave-marketing's honest-scope copy and CITATIONS
      rows would need updating** (they were written around mobile being out
      of scope).
- [ ] Mandate phased/incremental commits on multi-part builds. *Three agent
      connection drops this session left half-finished state (a
      referenced-but-never-created `what.js`, stale tests) that the
      orchestrator repaired by hand.*

### test-agent (core)
- [ ] Report test-count delta (added/removed/changed), not just pass/fail —
      *tests were silently replaced this session while the count stayed
      plausible.*
- [ ] Golden-set behavioural regression evals (versioned prompt→expected
      suites re-run per enhancement/release; seeded from real red-team
      findings). Folded into test-agent per the overlap rule — NOT a new agent.
- [ ] Headless-browser capability — it currently cannot see rendered output;
      the compounding-opacity bug and layout defects were invisible to it and
      required the human to report them. Also a prerequisite for mobile testing.

### review-agent (core)
- [ ] Copy/claims drift check — *after the hero rewrite, `<title>` and meta
      description still carried the old headline and no gate caught it.*
      Make rendered-copy vs. approved-copy drift an explicit review dimension.

### deploy-agent (core)
- [ ] Mobile deploy target (device/simulator install, app-store/TestFlight path).
- [ ] Rollback + redeploy verification (confirm a redeploy replaced the running
      process; support rolling back to last good state).
- [ ] Record served URL + health-check result, not just ports.
- [ ] *NOT selected: cloud `target_env`.* **Flagged:** this remains P1 on
      ROADMAP and is what backs conclave-marketing's live FDE claim
      ("forward-deployed engineers run the pipeline inside your environment").
      Deploy is local-only until it ships.

### mas-architect (platform)
- [ ] Standing **contract-drift audit** duty — compare MAS_REGISTRY against
      `.claude/agents/` on disk. Would have caught both drifts above.
- [ ] Process the queued `LESSONS.md` backlog (4 open items; one — the
      Write-vs-Edit KB wipe — recurred destructively twice and was escalated,
      not just re-queued).
- [ ] Add a 7th standard-contract question: **interruption behaviour** (what
      an agent must do if cut off mid-task). *Three agents dropped connection
      this session.*

### mas-registrar (platform)
- [ ] Real contract versioning — its contract says treat agent definitions as
      versioned, not casually tweakable, yet no agent file carries a version
      or change history.
- [ ] Actively enforce its own drift guardrail (give it a verify/audit action;
      today nothing ever invokes the check it already promises).

### mas-release-manager (platform)
- [ ] Groom the 8 staged roadmap items from
      `admin/proposals/2026-07-20-roadmap-additions.md` (still unapproved),
      now absorbing the PRD and mobile items above.

## Recommended sequence

1. **mas-architect consolidated review** — one pass covering: the two drift
   findings, the 4 queued LESSONS items, the plan-agent PO/PRD expansion, and
   the mobile capability (incl. its cascade across templates/test/deploy and
   the marketing-site claim implications). Returns recommendations only.
2. **Human approves** the recommendations (per-item).
3. **mas-registrar** implements approved contract changes (with versioning).
4. **Build** the non-contract capabilities (mobile template/toolchain,
   headless browser, golden-set evals, deploy targets).
5. **mas-release-manager** grooms the roadmap and cuts a platform version.
