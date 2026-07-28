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

## [OPEN] Questions the human still owes

| # | Question | Why it matters |
|---|---|---|
| **O1** | **Process lifetime.** Manual `python app.py` when wanted, or a real always-on service (`launchd`)? | Determines whether "we can go to that link" is actually true. Nothing in this platform keeps a service alive across sessions today; this would be the first. `LESSONS.md` 2026-07-09: a server started inside a subagent's shell dies with that turn. |
| **O2** | **Does `admin/kb-server/` move and retire, or stay and get extended in place?** | Follows from the placement decision. `app.py` is 28 lines; the real assets are `index.html` and `DESIGN_SPEC.md`. Moving is a `git mv` plus a blueprint split. |
| **O3** | **Does the Artifact-publishing obligation survive** once a live page renders the same graphs? | Recommend keeping both this round — Artifacts are shareable and already work — but it should be a decision, not an accretion. |

## Recorded risks (answered "we don't know yet" or accepted)

- **Schema untested before the server commits to it.** The human chose to build
  in one run rather than `mas-architect`'s Phase 0 first. Accepted risk,
  recorded here so it is visible if the schema has to change at gate 7+.
- **First project ever to run all eleven gates.** Both new gates get their
  first real exercise on tooling that will itself become a source of truth.
