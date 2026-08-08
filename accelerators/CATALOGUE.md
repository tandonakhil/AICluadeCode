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

Nothing is harvested yet. All five entries below were approved by the human on
2026-08-08 (`admin/proposals/2026-08-08-accelerator-layer.md`) and are `planned`
at `0.0.0` until their directory, contract and suite actually exist.

| # | Name | Version | Status | Gate relevance | Known consumers | Purpose |
|---|---|---|---|---|---|---|
| A1 | `auth-core` | 0.0.0 | planned | Architecture (H9 security co-sign required) | — | Auth, session and mobile token-store core: argon2id, hashed session tokens, sliding+absolute expiry, TOTP, rate limiting. |
| A2 | `grounded-answer-kernel` | 0.0.0 | planned | Architecture (H9 responsible-AI co-sign required) | — | Four-layer RAG grounding: refusal contract, refusal/sources kernel, retrieval protocol, coverage-ledger assurance. |
| A3 | `design-system` | 0.0.0 | planned | Experience Design, Architecture | — | Conclave token schema, light/dark law, semantic-law checklist, and the journey-map timing rule (journeys at Experience Design, unwalkable journey blocks the gate). |
| A4 | `test-scaffold` | 0.0.0 | planned | Code, Test | — | Suite scaffold and harnesses, and the platform 0/1/3/4 exit-code convention every other accelerator's suite must satisfy. |
| A5 | `conformance-kit` | 0.0.0 | planned | Architecture, Test | — | Structural conformance checks (import-boundary closure) plus their negative-control fixture trees. |

**Build order is not rank order.** `A4` is built **first**: every other entry
must ship a runnable suite in the platform exit-code convention (H4), and A4 is
what defines it. Then A5 → A3 → A2 → A1 (A1 last: largest, and gated on
`security-architect`'s H9 rulings).

Slugs other than `auth-core` (which the approved proposal fixes via its
provenance-stamp example) are **provisional** and are fixed at the moment each
entry is actually built.

## Known consumers

Every `built` entry names the projects that vendored it and at which version
(admission criterion H10). Without it, *"who is still holding the old copy?"* is
unanswerable — which is exactly how the `max_tokens=4096` fix stayed trapped in
one project while every other chatbot kept the broken default.

## Related

- `accelerators/ADMISSION.md` — H1–H10, the bar for entering this table.
- `accelerators/README.md` — what an accelerator is, and the vendoring rules.
- `admin/proposals/2026-08-08-accelerator-layer.md` — the approving proposal.
