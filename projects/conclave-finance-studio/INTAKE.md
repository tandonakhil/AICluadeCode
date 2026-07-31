# Intake — conclave-finance-studio

**Path A · New project.** Form: `admin/templates/INTAKE_FORM.md`.
Gathered conversationally, one question per turn, 2026-07-30.

---

## A1 · Identity

| # | Answer |
|---|---|
| A1.1 | `conclave-finance-studio` — "Conclave Finance Agentic Studio" |
| A1.2 | A multi-agent AI system for finance accountants: create standalone agents, or assemble agentic teams, to run month-end close activities. |
| A1.3 | Human (platform owner). Approval authority at every gate. |

## A2 · Problem

| # | Answer |
|---|---|
| A2.1 | Month-end close is manual, repetitive and time-boxed. Reconciliations, accruals, variance explanation and journal prep consume the close window. |
| A2.2 | **Three personas, all primary** — staff accountant (does the work), controller / close manager (supervises and signs off), FP&A analyst (explains the result). |
| A2.3 | Today: Oracle ERP Cloud plus a financial data warehouse. This system sources from those rather than replacing them. |

## A3 · Users and context

| # | Answer |
|---|---|
| A3.1 | Month-end close window — time-boxed, high pressure, day-N deadlines. |
| A3.2 | Under deadline pressure. **Design consequence**: an approval requested at 11pm on day 3 of close is an approval given with low scrutiny; the system must not rely on careful reading at the moment of approval. |

## A4 · Domain and industry

| # | Answer | Owner |
|---|---|---|
| A4.1 | Financial close operations / record-to-report. Multi-agent orchestration for accounting workflows. | `functional-agent` |
| A4.2 | Finance & accounting — corporate controllership. | `industry-expert` |

## A5 · Surfaces — **three, so multi-surface**

| # | Answer |
|---|---|
| A5.1 | **Desktop web · mobile web · native mobile** |
| A5.3 | Yes — one shared backend over the warehouse. |

**Consequence, binding**: three surfaces makes `solution-architect`
**non-droppable** at Team Composition, with a mandatory Impact Analysis on every
enhancement. Recorded here so the roster proposal can be checked against the
surface count, not just accepted.

## A6 · Data

| # | Answer |
|---|---|
| A6.1 | A financial data warehouse, sourced from **Oracle ERP Cloud** as the base application. |
| A6.2 | *(open — Architecture)* Agent definitions, team compositions, run history, approval records. |
| A6.3 | **Financial / regulated.** Ledger data, journals, reconciliations. Pulls `security-architect` onto the roster; audit-trail obligations are architectural, not optional. |

## A7 · AI behaviour

| # | Answer |
|---|---|
| A7.1 | *(open — routed to SMEs)* |
| **A7.2** | **DELEGATED, not skipped.** Human: *"you will ask this question to SME agents when pipeline is being designed."* Owed by `functional-agent` + `industry-expert` at Intake, and `responsible-ai-architect` at Architecture. **Consequence: `responsible-ai-architect` is effectively non-droppable** — the harm analysis is owed and no one else on the roster produces it. |
| A7.4 | Accountability sits with the named human approver per write (see A-write below). |

## A-write · Write-back — the defining decision

**Agents write back to the ledger, gated by explicit per-action human approval.**

Not read-only, and not autonomous. Every posting — journal, reconciliation
close-out — requires a named human to approve *that specific action*.

Architectural obligations this creates, carried to gate 6 rather than
rediscovered there:
- an **audit trail per write** — who approved what, when, on what evidence
- **rollback** for any posted action
- **segregation of duties** — the approver cannot be the requester
- the approval UI must stay legible under deadline pressure (see A3.2)

## A8 · Success and scope

| # | Answer |
|---|---|
| A8.1 | *(open — follows from MVP)* |
| A8.2 | *(open)* |
| **A8.3** | **DELEGATED, not skipped.** Human: *"let SMEs propose it."* `plan-agent` proposes the MVP slice, `industry-expert` informs it from close practice, `functional-agent` challenges it as devil's advocate. The human still approves the split feature-by-feature at gate 3. |

## Product shape

**Both** — pre-built close agents that ship working, *and* a builder letting
accountants clone, tweak and combine them into teams. Widest of the three
options considered; the others were a builder-only studio and a closed system
with agents hidden inside. Recorded because "which half ships first" is now the
central MVP question.

---

## Recorded risks

- **Scope is very wide**: both product shapes × three personas × three surfaces
  × write-back. The MVP slice is the mitigation and it is delegated; if the SME
  proposal comes back broad, that is the moment to push back, not later.
- **Two mandatory questions delegated to SMEs** (A7.2, A8.3). Legitimate — the
  form permits an answer of "route it" — but it means gate 1 and gate 3 carry
  work that would normally arrive already answered. If the SMEs do not produce
  a concrete harm scenario, Architecture proceeds without one, which is the
  failure this form exists to prevent.
- **Approval-under-pressure** (A3.2): a per-write approval model whose approvals
  are given at 11pm on day 3 is a control in name. Flagged for
  `responsible-ai-architect` and `ui-ux-designer`.
