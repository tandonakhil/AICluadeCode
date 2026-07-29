# Intake — conclave-dashboard

**Path A · New project.** Form: `admin/templates/INTAKE_FORM.md`.
Completed 2026-07-28. Pre-filled from the request, the `mas-architect`
advisory review, and the human's gate-2 decisions; open questions marked
**[OPEN]**.

> First project to run under the mandatory intake process, and the process
> immediately earned itself: `mas-architect` independently found that
> "live project status" was ambiguous between pipeline status and runtime
> status — an A-series question that went unasked because the request arrived
> as a prompt. Resolved below as **both**.

---

## A1 · Identity

| # | Answer |
|---|---|
| A1.1 | `conclave-dashboard` |
| A1.2 | A served console showing, for every project, where it stands in the 11-gate pipeline **and** whether its deployed app is actually running. |
| A1.3 | Human (platform owner). Approval authority at every gate. |

## A2 · Problem

| # | Answer |
|---|---|
| A2.1 | Project status is spread across `PIPELINE_LOG.md` per project, `PORTFOLIO_STATUS.md`, and `PROJECT_CONTEXT.md` — all hand-maintained, and drift between them is this platform's most persistent failure. |
| A2.2 | The platform owner, checking on five projects between sessions. |
| A2.3 | Today: run `/project-status`, which requires an active Claude session. Or read markdown, where mermaid does not render. |
| A2.4 | Status stays session-bound and hand-maintained. The drift continues — `kb-server` is the worked example: 18 days stale, and wrong in three places at once. |

## A3 · Users and context

| # | Answer |
|---|---|
| A3.1 | Desktop browser, local machine. Checked between working sessions, and during a run to see where a gate stands. |
| A3.2 | Scanning, not reading. Wants position at a glance and to spot anything wrong. |
| A3.3 | One user. This is single-tenant local tooling — no auth, no multi-user, no external exposure. |

## A4 · Domain and industry

| # | Answer | Owner |
|---|---|---|
| A4.1 | Software delivery / pipeline observability. Internal developer tooling. | `functional-agent` |
| A4.2 | **N/A — internal tooling, no market-facing industry.** Recorded rather than skipped silently. `industry-expert` is expected to be dropped at Team Composition. | `industry-expert` |

## A5 · Surfaces — never skipped

| # | Answer |
|---|---|
| A5.1 | **Desktop web only.** Served locally. |
| A5.2 | None anticipated. No mobile, no API for third parties. |
| A5.3 | N/A — single surface. |

**Consequence**: single-surface, so `solution-architect` is **droppable by
rule**. `mas-architect` nonetheless recommends keeping it, because the state
schema is consumed by four things (orchestrator, `/project-status`, the
generated markdown, the server) and is the highest-leverage artifact in the
build. That is a human choice at gate 2, not a rule.

## A6 · Data

| # | Answer |
|---|---|
| A6.1 | Reads `admin/PIPELINE.yaml` (shape) and each `projects/<name>/pipeline-state.json` (state). For runtime status, reads each project's recorded served URL and performs a health check. |
| A6.2 | Nothing. The dashboard is a **reader**; the orchestrator owns all writes. |
| A6.3 | **No PII, no regulated data.** Project metadata only. |
| A6.4 | N/A — stores nothing. |

> **Novel boundary, flagged for gate 6**: this project reads `admin/` and
> **sibling projects'** state. No project has ever read another project.
> Read-only, path-scoped, and it must import nothing from any project.

## A7 · AI behaviour

| # | Answer |
|---|---|
| A7.1 | It generates nothing. No LLM call anywhere in this project. |
| A7.2 | **Worst plausible harm: the dashboard asserts a state that is false and is believed** — showing eleven green gates for a project whose Review was never approved, or "running" for a process that died. This platform's whole failure pattern is authoritative-looking assertions that are wrong. A status board is the highest-leverage place to repeat it. |
| A7.3 | Every figure must be read from state at request time. **No hardcoded counts, no hardcoded gate names, no hardcoded agent lists — including in copy.** `kb-server`'s `DESIGN_SPEC.md` hardcoded "Eighteen agents / Nine gates" into the *design*, so even a data-wired page would have shipped wrong. |
| A7.4 | The human. The dashboard reports; it never decides. |

## A8 · Success and scope

| # | Answer |
|---|---|
| A8.1 | Open the link, see all five projects' gate position and whether each app is up, with no hand-maintained copy anywhere behind it. `PIPELINE_LOG.md` and `PORTFOLIO_STATUS.md` are generated from the same state the server reads. |
| A8.2 | **Out of scope**: editing anything from the UI; advancing a gate; approving anything; auth/multi-user; remote/public exposure; historical trend charts; notifications. |
| A8.3 | Smallest useful: state schema + backfill of five projects + one page listing them with gate position. |

## A9 · Constraints

| # | Answer |
|---|---|
| A9.1 | No deadline. |
| A9.2 | No explicit token budget; `usage-monitor` estimates at gate 2. |
| A9.3 | None — internal tooling, no compliance surface. |
| A9.4 | **Must reuse**: `admin/kb-server/`'s existing Flask app, `templates/index.html` and `DESIGN_SPEC.md` (migrating in); `admin/PIPELINE.md` §3's fixed `classDef` block and row structure, which the renderer must emit verbatim so every graph stays identical. |

## A10 · Template

| # | Answer |
|---|---|
| A10.1 | **custom (Flask)** — precedent `conclave-marketing`. Not `genai-chatbot` (no LLM), not `rag-knowledge-base`, not `agentic-workflow`. |
| A10.2 | Not ambiguous. |

---

## RESOLVED — human decisions, 2026-07-28

| # | Question | Why it matters |
|---|---|---|
| **O1** | **Manual start.** `python app.py` when wanted. No daemon, no launchd, no new operational surface. Consistent with every other project here. |
| **O2** | **Move and retire.** `admin/kb-server/` migrates into `dev/`. One app, one port, two routes — `/` knowledge base, `/status` dashboard. Its 18-day staleness is fixed structurally by reading from state rather than by a content edit. |
| **O3** | **Dashboard replaces Artifacts at gate report-outs** — *with the reachability caveat below.* |

### Conflict between O1 and O3, and how it is resolved

O1 (manual start) and O3 (dashboard replaces Artifacts) are in direct tension:
if the server is usually not running, and gate report-outs link to it instead
of publishing, then most report-outs hand the human a **dead link**. That is
strictly worse than today, and it is exactly the failure mode this project
exists to prevent — an authoritative-looking pointer to nothing.

**Resolution, orchestrator judgement, pending human correction:** the gate
report-out links to the dashboard **when it is reachable**, and falls back to
publishing an Artifact when it is not. The obligation is "the human can see the
graph," not "an Artifact exists." Revisit if O1 changes to always-on, at which
point O3 applies unconditionally.

This is recorded as a decision rather than absorbed silently, because it
changes what `admin/PIPELINE.md` §3a requires and that file is binding.

## Recorded risks (answered "we don't know yet" or accepted)

- **Schema untested before the server commits to it.** The human chose to build
  in one run rather than `mas-architect`'s Phase 0 first. Accepted risk,
  recorded here so it is visible if the schema has to change at gate 7+.
- **First project ever to run all eleven gates.** Both new gates get their
  first real exercise on tooling that will itself become a source of truth.

---

## Requirement addendum — 2026-07-28, human, arriving at gate 2

Experience-Design-shaped requirements arrived before gates 3 and 4. Recorded
here as intake input rather than acted on out of order; they feed Plan &
Backlog (3), become acceptance criteria at Functional Design (4), and are
designed at Experience Design (5).

| Ref | Requirement |
|---|---|
| R1 | **Project selector** — a dropdown to switch between projects, not five stacked graphs on one page. |
| R2 | **Analytical status-reporting layout**, not a document. Read the way a status dashboard is read: summary first, detail on demand. |
| R3 | **Key callouts on status** — the things that need attention surfaced before the detail, encoded in form as well as number. |
| R4 | **Follow an established project-status-report template** rather than inventing a layout. Researched, not improvised. |
| R5 | **Show how it looks before approval** — a rendered mockup, per `ui-ux-designer`'s standing contract obligation. |
| R6 | `ui-ux-designer` engaged for the design. |

**Consequence for A8.2 (out of scope).** R2/R3 pull toward analytics —
historical trend charts and notifications were explicitly out of scope at
intake and **remain so** unless the human reopens them. "Analytical" here means
the *layout and information design* of a status report, not time-series
analysis.

**Consequence for A7.2 (worst plausible harm).** R3 raises the stakes on the
callouts specifically: a callout is the most authoritative element on a status
page. A callout that is wrong, or that stays green while something is broken,
is the precise harm this project was chartered to avoid.
