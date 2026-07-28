# Proposal — closing the pipeline's verification gap

**Raised**: 2026-07-28 by the human, after the little-milestones F18 mobile build.
**Status**: awaiting `mas-architect` review, then human approval, then `mas-registrar`.
**Origin**: six numbered feedback points from the human (verbatim below), plus an
orchestrator end-to-end analysis and 2026 external research.

---

## The human's feedback, verbatim

1. Any time a new feature or development is done, testing is not done properly.
   We are continuously seeing missed development or loose ends.
2. Need of strong unit testing for developers.
3. Do we need different technical and functional design agents, as we are seeing
   a lot of after-the-fact work being done?
4. No engagement from deliverables agent.
5. There is a need to establish a visual graph showing a typical workflow, how
   each project will get executed with agents, and the flow needs to be followed
   very strictly without exceptions — unless triggered by human for exception,
   ask for explicit approvals.
6. Any time a new feature gets added, solution architect needs to review the
   end-to-end impact, not a myopic view.

---

## Evidence base — the F18 mobile build defect ledger

Ten defects. **Eight were caught by the human on the running app**; two by tests
that were only written *after* the human reported the symptom. Zero were caught
by the nine gates or the six SME suites on their own.

| # | Defect | Class | Invisible to | Caught by |
|---|--------|-------|--------------|-----------|
| 1 | Avatar built, never rendered | built-not-wired | typecheck, bundle, API tests | human |
| 2 | Journey photos never rendered | built-not-wired | typecheck, bundle, API tests | human |
| 3 | Lightbox + gallery never mounted | built-not-wired | all six SME suites | human |
| 4 | ChatHistorySheet imported, state-managed, never mounted | built-not-wired | all six SME suites | RNTL test (written after) |
| 5 | Prompt chips rendered as stretched ovals | visual regression | every non-rendered check | human |
| 6 | Dead band above composer | visual regression | every non-rendered check | human |
| 7 | First prompt chip age-blind across all 10 buckets | logic shipped unverified | no unit tests existed | human |
| 8 | Logout over bearer never revoked server-side | security | security suite as written | new test (written after) |
| 9 | Desktop web had zero SME-suite coverage | structural blind spot | the Test gate itself | human |
| 10 | Deliverables 15 days stale, describe a web-only product | untriggered agent | no gate checks freshness | human |

**Root cause**: the pipeline verifies that *code was written*, never that *the
feature works*. Nothing binds a feature's acceptance criteria to executed
evidence, so "done" is asserted by the agent that did the work rather than
demonstrated to an independent checker.

Corroborating detail: four of ten defects (1–4) are literally the same failure —
a component built, imported, sometimes even state-managed, and never rendered.
That class is invisible to typecheck, bundle, and API tests by construction, and
no suite asserted on rendered output.

---

## Proposed new agents

### N1 — `functional-design-agent`
- **Gate**: new **Functional Design** gate, between Plan & Backlog and Experience Design.
- **Core/optional**: proposed core for all templates.
- **KB**: `FUNCTIONAL_SPEC.md` (per-feature observable behaviour in Given/When/Then
  form, edge cases, empty/error states — every line testable).
- **Owns test suite**: none (it defines what other suites verify against).
- **Addresses**: #3, #1.
- **Overlap risk to adjudicate**: borders `plan-agent` (scope/backlog) and
  `ui-ux-designer` (flow/layout). Proposed lane: *observable behaviour and
  acceptance criteria* — not what to build, not what it looks like.

### N2 — `verification-agent`
- **Gate**: new **Verification** gate, between Test and Review.
- **Core/optional**: proposed core.
- **KB**: none; writes a per-feature evidence matrix into `PROJECT_CONTEXT.md`.
- **Owns test suite**: none — it runs nothing, it audits the evidence trail.
- **Behaviour**: every acceptance criterion in `FUNCTIONAL_SPEC.md` must map to a
  named, executed, passing check. Unmapped criteria block and route back to Code.
- **Addresses**: #1.
- **Depends on**: N1 (nothing to verify against otherwise).
- **Overlap risk to adjudicate**: borders `test-agent` (which runs suites and
  aggregates) and `review-agent` (which checks intent match). Proposed lane:
  *coverage of criteria by evidence* — not correctness, not style.

### N3 — `pipeline-marshal`
- **Gate**: cross-cutting; guards every transition.
- **Core/optional**: core (infrastructure).
- **Owns**: `admin/PIPELINE.yaml` — gate order, per-gate required inputs/outputs
  and exit criteria; renders the workflow diagram from that same file so picture
  and rule cannot drift.
- **Behaviour**: refuses a transition whose prerequisites are unmet; records every
  human-granted exception with its reason in the Decisions Log.
- **Addresses**: #5.
- **Note**: this constrains the orchestrator itself. In the F18 build the
  orchestrator skipped gates and nothing detected it.

---

## Proposed contract changes to existing agents

| Ref | Agent | Bump | Change | Addresses |
|-----|-------|------|--------|-----------|
| C1 | `code-agent` | MAJOR | Unit tests become a Code-gate deliverable, authored by the implementer in the same commit. Every new module gets unit tests; every new UI component gets a rendering test proving it is reachable on screen. Gate does not close on untested new code. | #2 |
| C2 | `solution-architect` | MAJOR | Mandatory Impact Analysis artifact per enhancement: which surfaces (web/mobile/API/data/deliverables) the change reaches, which are unaffected **and why**, what must be re-tested. An unjustified omission blocks Architecture. | #6 |
| C3 | `test-agent` | MAJOR | Rendered-output evidence required per surface named by C2's Impact Analysis. A surface with no rendered evidence reports `NOT VERIFIED`, never folded into a pass. | #1 |
| C4 | `deliverables-agent` | MINOR | Freshness becomes a blocking Deploy-gate check: each deliverable's timestamp compared against its source markdown. | #4 |
| C5 | `review-agent` | MINOR | Add a wiring sweep to its existing lane — every component defined under this feature is rendered somewhere reachable. Cheap, static, would have caught defects 1–4. | #1 |
| C6 | platform | MINOR | Promote the cross-surface parity suite written during F18 into the templates, so multi-surface projects get it from day one. | #1, #6 |

---

## Explicitly rejected (do not re-litigate)

- **A separate technical-design agent.** The human asked whether functional and
  technical design should split. Functional — yes, it is missing. Technical — no:
  `solution-architect` owns it and does it well. The after-the-fact work traces to
  absent *functional* spec, not overloaded technical design.
- **LLM-as-judge quality scoring.** Well-supported externally, but substitutes a
  probabilistic opinion for the deterministic evidence trail that is the actual
  missing piece. Revisit after N2 exists.
- **More SME suites.** Six went green while the app was broken. The problem is
  what they assert on, not how many there are.

---

## Proposed sequencing

| Phase | Ships | Rationale |
|-------|-------|-----------|
| 1 | C1, C5 | Contract-only, no new agents, highest yield. Would have caught 5 of 10 defects. |
| 2 | N1 | Creates the acceptance criteria everything downstream verifies against. |
| 3 | N2, C3 | Closes the loop. Depends on Phase 2. |
| 4 | C2, C6 | Multi-surface correctness. |
| 5 | N3, C4 | Enforcement last — codifies a pipeline shape Phases 1–4 have already changed. |

---

## Cost caveat

External research is consistent that orchestrator decomposition calls compound at
volume. Two new gates add per-project cost. N2 in particular must audit an
evidence table, not re-reason about the code, or it becomes the most expensive
gate in the pipeline for the least new information.

---

# MAS-ARCHITECT REVIEW — 2026-07-28

Full advisory review returned. Headline: **fold all three proposed agents into
existing ones; zero new agents, zero new gates.** Its substantive findings, all
verified:

1. **The proposal's largest error — the missing mobile rendering backend.**
   `test-agent` v1.3.0 made rendered-UI verification contractual and shipped
   2026-07-26; F18 ran *under* that contract and still shipped six rendering
   defects. Cause: the capability has exactly one built backend (Playwright), and
   the native backend was deferred when the 2026-07-26 toolchain spike found no
   simulator. Defects 1–6 were **structurally uncatchable**. Defect #4 was caught —
   by an RNTL test, which needs no simulator. RNTL is the missing backend and was
   absent from this proposal entirely.
2. **C1 as written would not prevent the defect class it targets.** A test that
   renders `<Avatar/>` in isolation passes while `Avatar` is mounted nowhere —
   exactly defects 1–4. The contract must require rendering from the screen's or
   app's real entry point.
3. **Semver corrections**: C1 MINOR (not MAJOR), C2 MINOR (not MAJOR), C4
   MAJOR-if-blocking (not MINOR).
4. **C4 as written violates standing governance** — an optional agent may not
   block a core gate; `deploy-agent` owns Deploy and SME input is never
   independently blocking.
5. **N3's fatal circularity** — the only way `pipeline-marshal` runs is if the
   orchestrator invokes it; an orchestrator that skips gates skips the marshal.
6. **Machinery vs. discipline** — every gate-skip in F18 violated rules that
   already existed. `PIPELINE_LOG.md` is the load-bearing artifact because it makes
   non-compliance visible to someone other than the non-complier.
7. **Two live bugs, both verified on disk**: the `dev/tests/<suite>/run.sh` entry
   points that the six SME `Bash` grants point at are shadowed by a duplicate tree
   and report `NO SCENARIOS DEFINED` (exit 3) for suites that have passing tests;
   and the registry slug `red-team` does not match the on-disk `redteam`.
8. **Unexamined structural question** — this platform has no first-class notion of
   a **multi-surface project**. Defects 9 and 10 are both symptoms.

---

# HUMAN DECISIONS — 2026-07-28

| Item | Decision | Notes |
|------|----------|-------|
| N1 `functional-design-agent` | **BUILD as a real agent** | Human overrode the fold. New gate between Plan & Backlog and Experience Design; owns `FUNCTIONAL_SPEC.md`. |
| N2 `verification-agent` | **BUILD as a real agent** | Human overrode the fold. New gate between Test and Review. |
| N3 `pipeline-marshal` | **NOT BUILT** | Circularity accepted. |
| RNTL native rendering backend | **BUILD NOW** | `mas-architect`'s strongest recommendation; absent from the original proposal. |
| C1 `code-agent` unit + reachability tests | **BUILD NOW**, MINOR | With `mas-architect`'s correction: render from the app's real entry point, never the component in isolation. |
| C5 `review-agent` wiring sweep | **BUILD NOW**, MINOR | Trace from entry point through the render tree; verdict `request-changes`. |
| Broken entry points + slug mismatch | **FIX NOW** | Project-level fix in little-milestones `dev/`. |
| C2 `solution-architect` | **NON-DROPPABLE for multi-surface projects** — **MAJOR** | Human chose the higher-blast-radius option over the gate-level artifact. Touches the core-vs-optional roster boundary. |
| C4 `deliverables-agent` | **NO new check** | Treated as orchestrator trigger discipline plus `PIPELINE_LOG` visibility, per `mas-architect`'s own diagnosis. |
| C3, C6 | Deferred to a later phase | Not selected in this round. |

**Orchestrator determinations on points the human did not specify**, applying
`mas-architect`'s guardrails:

- **N2 is BLOCKING, not advisory.** An advisory verification gate is ignorable,
  which reproduces feedback #1 exactly. To honour the cost caveat it is
  contractually barred from re-reasoning about the code: it audits the evidence
  table only.
- **N1 owns `FUNCTIONAL_SPEC.md`** as a new KB, which is the standard contract for
  a new agent and avoids the `PLAN.md`-is-transient durability problem.
- **Acceptance criteria carry stable IDs** (`AC-F18-03`). `mas-architect` is right
  that the IDs are the load-bearing part — without them N2's audit is
  interpretive rather than mechanical.

## External research consulted

- Orchestrator-worker is ~70% of production multi-agent deployments — Conclave's
  topology is not the problem.
- Maker–checker (independent critic, different prompts from the generating agent)
  is the cited pattern for quality control. N2 is this.
- Evidence-driven release gates (PROMOTE/HOLD/ROLLBACK against operationalised
  dimensions) closely match N2's per-criterion evidence audit.
- Reviewer agents evaluating outputs in isolation rather than end-to-end is a
  documented failure mode — the argument for C2.
- Sonar (Jan 2026): 96% of 1,100+ developers do not fully trust AI-generated code
  is functionally correct. Verification, not generation, is the bottleneck.
