# Features: policy-lookup-assistant

## In Development

Proposed backlog for the first release (MVP). Informed by
`knowledge/DOMAIN_KB.md` (functional-agent's risk list) and
`knowledge/INDUSTRY_KB.md` (industry-expert's trend-informed 6-item
proposal). Not yet coded — this list is the candidate scope for PLAN.md
passes, taken one feature at a time. Ordered by build priority (highest
risk/value ratio first).

1. **"Insufficient evidence in corpus" explicit refusal path.** When a
   question isn't actually answered by the retrieved chunks (wrong
   jurisdiction, a program/detail the corpus doesn't cover, a question that
   invites extrapolation-by-analogy), the assistant states that plainly
   instead of answering anyway. Addresses DOMAIN_KB risk #5 (silent
   extrapolation) and risk #6 (incentive-stacking trap), and is
   INDUSTRY_KB's #3 proposed item — the single highest-leverage feature for
   the credibility this tool needs. **First feature to build — see PLAN.md.**

2. **Document authority/type badge shown with every answer** (e.g.
   "Internal Policy" vs. "FAQ — informal guidance"), derived from
   per-document metadata tagged at ingestion time. Addresses DOMAIN_KB risk
   #1 (citation to the wrong authority level) and is INDUSTRY_KB's #1
   proposed item. Bundled into the same first pass as item 1 below (see
   PLAN.md) because the refusal/citation behavior and the authority label
   share the same metadata and prompt-construction changes.

3. **Persistent AI-disclosure notice + verify-against-source prompt** on
   every answer (UI-level, not a backend behavior change): "This is an
   AI-generated answer — verify against the linked source document."
   Addresses INDUSTRY_KB compliance consideration #2 (proliferating
   state AI-disclosure laws) and the Moffatt v. Air Canada liability
   precedent from DOMAIN_KB. Deferred to the second build pass (after item
   1/2) because it's primarily a frontend/UI-copy change with no retrieval
   logic behind it — low risk to build later, and the UI template
   (frontend/app placeholder) isn't customized yet.

4. **Numeric-precision guardrail for exact thresholds.** A lightweight check
   (prompt instruction + spot-check test cases) that numeric answers quote
   the source figure verbatim rather than paraphrasing ("about a day"
   instead of "24 hours") or blending adjacent numbers. Addresses DOMAIN_KB
   risk #3. Deferred as a standalone feature for now — folded as an
   acceptance-criteria concern into item 1's plan (numeric questions are
   part of that feature's test set) rather than built as separate
   application logic, since there's no obvious code change beyond prompt
   wording and retrieval k-value tuning.

5. **Emergency/exception-clause retrieval check.** Verify chunking/retrieval
   surfaces the grid policy's emergency-maintenance carve-out alongside the
   base rule it modifies, rather than answering with only the general rule.
   Addresses DOMAIN_KB risk #7. Deferred to a follow-up pass once real
   retrieval behavior can be observed against the ingested corpus — this is
   more a tuning/evaluation task (chunk size, overlap, retrieval k) than a
   new feature, and is best done after item 1 establishes the
   evidence-sufficiency behavior it depends on.

6. **Staleness / "last verified" alerting for time-sensitive incentive
   content.** A visible per-document "last verified" date plus a lightweight
   (manual-at-MVP) re-check process against source-of-truth sites. Addresses
   DOMAIN_KB risk #2 and is INDUSTRY_KB's #5 proposed item. Deferred past
   MVP: valuable but not required to prove the core trust mechanism, and a
   manual re-check process has no code dependency on items 1-3 — can be
   scheduled independently once the app is live.

**Scoping decisions carried forward (not features, but backlog-adjacent):**
- **Audience: internal staff tool first, not public-facing**, per
  INDUSTRY_KB's #6 proposal and its lower compliance bar (state
  AI-disclosure laws and PUC scrutiny bear most heavily on customer-facing
  deployments). Revisit audience scoping before any public launch.
- **Corpus scope: public-facing policy/incentive content only, not
  operational/BES data**, per INDUSTRY_KB compliance consideration #1. Keeps
  NERC CIP BCSI controls out of MVP scope. Flagged as a re-scoping trigger
  if a later phase ingests internal grid-operation procedures.
- **Jurisdictional-layering disclosure** (DOMAIN_KB risk #4 — federal vs.
  state PUC vs. internal-policy answers can all be simultaneously "correct")
  is explicitly **not** a planned MVP feature: the current sample corpus
  doesn't contain multiple jurisdictional layers for the same rule, so there
  is nothing to disambiguate yet. Revisit if/when the real corpus grows to
  include documents from more than one regulatory layer on the same topic.

## Ready for Release

## Released
