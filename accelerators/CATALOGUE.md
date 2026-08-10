# Accelerator Catalogue

Single source of truth for what accelerators exist, at what version, and who
has vendored them. Written only by `mas-registrar` (rows, placement) and
`mas-release-manager` (version, deprecation, CHANGELOG), each only under
explicit human approval. `mas-architect` audits this file against disk.

## This file is deliberately SHORT — keep it that way

`solution-architect` reads this catalogue at **every Architecture gate on every
project, forever.** Its size is therefore a *recurring* token cost paid by every
future project, and a catalogue that grows long inverts the entire motivation
for having one.

**Rules for future editors:**

- One row per accelerator. One line of purpose. No prose sections per entry.
- Detail belongs in `<name>/ACCELERATOR.md`, which is read only for the
  shortlist an architect is actually considering.
- Rationale, provenance, config tables and adoption steps never appear here.
- If you are tempted to explain something in this file, that is the signal it
  belongs in the entry's own `ACCELERATOR.md`.

## Status values

`planned` (approved, nothing harvested yet) → `built` (directory exists, passes
admission H1–H10) → `deprecated` (superseded; **still runnable**, never deleted
— admission criterion H8).

## Entries

A1/A2/A3/A4/A5 are all harvested and `built`.

| # | Name | Version | Status | Gate relevance | Known consumers | Purpose |
|---|---|---|---|---|---|---|
| A1 | `auth-core` | 1.0.0 | **built** | Architecture (H9 security co-sign required) | `little-milestones` (origin — harvested *from*, not yet vendored *back into*; see `ACCELERATOR.md` H10) | Auth, session and mobile token-store core: argon2id, hashed session tokens, sliding+absolute expiry, TOTP, rate limiting, tenant-genericized via a `PrincipalResolver` seam. **H9 co-signed by security-architect 2026-08-09, conditional on ACCELERATOR.md items 1-8, all incorporated.** |
| A2 | `grounded-answer-kernel` | 1.0.0 | **built (not yet `admitted`** — H9 responsible-AI co-sign outstanding, see `ACCELERATOR.md`) | Architecture (H9 responsible-AI co-sign required) | rate-case-analyzer, policy-lookup-assistant, templates/rag-knowledge-base (origin/pattern-source, not vendored consumers) | Four-layer RAG grounding: L0 contract, L1 refusal/sources kernel, L2 retrieval protocol + offline hash-embed, L3 coverage-ledger + abstention assurance. |
| A3 | `design-system` | 1.0.0 | built | Experience Design, Architecture | CFS, RCA, marketing, dashboard | Conclave token schema, light/dark law, semantic-law checklist, and the journey-map timing rule (journeys at Experience Design, unwalkable journey blocks the gate). |
| A4 | `test-scaffold` | 1.0.0 | **built** | Code, Test | `templates/genai-chatbot`, `templates/agentic-workflow`, `templates/rag-knowledge-base`, `projects/conclave-marketing/dev`, `projects/little-milestones/dev` (origin — harvested *from*, not yet vendored *back into*; see `ACCELERATOR.md` H10) | Suite scaffold and harnesses (`browser.py`, `native.py`), and the platform 0/1/3/4 exit-code convention every other accelerator's suite must satisfy. |
| A5 | `conformance-kit` | 1.0.0 | **built** | Architecture, Test | rate-case-analyzer (origin), conclave-finance-studio (origin) | Structural conformance checks (import-boundary closure) plus a live-resource construction guard and a numeric-leak assertion, each with negative controls. |

**Build order was not rank order.** `A4` was built **first**: every other
entry ships a runnable suite in the platform exit-code convention (H4), and
A4 is what defines it. A1 shipped out of the originally-stated A5→A3→A2→A1
sequence, at the human's explicit approval, in parallel with A2-A5's own
harvests — see `A1/ACCELERATOR.md`'s H3 note on what that means for the
A5-closure-checker cross-check (not yet run against A1, since A5 had not
yet landed at the moment A1's harvest started).

## Known consumers

Every `built` entry names the projects that vendored it and at which version
(admission criterion H10). Without it, *"who is still holding the old copy?"* is
unanswerable — which is exactly how the `max_tokens=4096` fix stayed trapped in
one project while every other chatbot kept the broken default.

## Related

- `accelerators/ADMISSION.md` — H1–H10, the bar for entering this table.
- `accelerators/README.md` — what an accelerator is, and the vendoring rules.
- `admin/proposals/2026-08-08-accelerator-layer.md` — the approving proposal.
