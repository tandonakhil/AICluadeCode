# `grounded-answer-kernel` (A2) -- grounded-answer / RAG kernel, four layers

**Version**: 1.0.0 · **Status**: `built`, **NOT YET `admitted`** (see H9
below) · **Slug fixed**: `grounded-answer-kernel`

Source: `admin/proposals/2026-08-08-accelerator-layer.md`, Seed 3 ("Reusable
RAG frameworks"), approved by the human 2026-08-08. Written by
`mas-registrar` under that approval.

---

## What this is, in one paragraph

Four independently-adoptable layers for a RAG product that must be able to
**refuse honestly** rather than hallucinate: `L0` a one-page contract
(prose only), `L1` a near-zero-dependency kernel (refusal detection, typed
refusal kinds, source-building), `L2` a retrieval protocol plus a
credential-free deterministic embedder, and `L3` an assurance layer
(coverage ledger, abstention vocabulary, deterministic citation
verification). The prior review's key finding, restated here because it
governs every design choice below: **merge the contract, not the
implementation** -- `rate-case-analyzer` and `policy-lookup-assistant` are
architecturally incompatible (hand-rolled protocol-over-SQLite vs.
LangChain/Chroma `similarity_search`), so `L2` is deliberately the seam
where they diverge, not a place this accelerator tries to unify them.

## The do-not-build finding (explicit, per the prior review)

**This accelerator does NOT attempt to make `policy-lookup-assistant`'s
LangChain/Chroma approach and `rate-case-analyzer`'s hand-rolled approach
into one implementation.** They are architecturally incompatible retrieval
strategies. Forcing them together behind one interface would produce an
interface satisfying neither -- worse than the two independent
re-derivations that motivated this harvest in the first place. `L2`'s
`EvidenceSource` Protocol is therefore intentionally thin: it names the
SHAPE both approaches can satisfy (`retrieve`, `candidate_ids`,
`claims_for_chunks`, `read_case`, ...), and an adopter chooses ONE backing
implementation -- a Chroma-backed adapter, a hand-rolled store, or
`hash_embed`'s deterministic offline ranking -- never a framework spanning
both.

---

## H1 -- Declared contract

Public surface, by file. Anything not listed here is private and may change
in a MINOR release without notice.

| File | Public surface |
|---|---|
| `l1_kernel/sentinel.py` | `INSUFFICIENT_EVIDENCE` (constant), `is_refusal(content: str) -> bool` |
| `l1_kernel/refusal.py` | `RefusalKind`, `QueryOutcome`, `OUTCOME_FOR_KIND`, `STATEMENT_TEMPLATES`, `statement_for()`, `gap_rows()`, `examined_lines()`, `relaxes_exactly_one_dimension()`, `filter_alternatives()` |
| `l1_kernel/sources.py` | `Source` (dataclass), `SourceContextMissing`, `build_sources(verified) -> tuple[Source, ...]`, `build_sources_arity()` |
| `l2_retrieval/protocol.py` | `EvidenceSource` (Protocol), `ChunkPredicate` |
| `l2_retrieval/hash_embed.py` | `EMBEDDING_DIM`, `hash_embed(text, dim=...) -> tuple[float, ...]`, `rank_within(candidate_ids, query_vector, embeddings, k) -> tuple[str, ...]` |
| `l3_assurance/coverage_ledger.py` | `Coverage`, `CoverageLedger`, `CoverageNotBalanced`, `BlankReasonError`, `Included`, `Excluded`, `Unassessable` |
| `l3_assurance/abstention.py` | `AbstentionType`, `TYPES`, `CODES`, `abstention_type()`, `Abstention`, `RAG_STATES`, `NEGATIVE_STATES`, `RAG_FOR`, `AssuranceItem`, `item_for_abstention()`, `item_for_conclusion()`, `negative_findings()`, `unknowns()`, `quality_denominator()`, `rates()`, `evaluate_band()`, `assert_no_abstention_control()`, `routing_cost()` |
| `l3_assurance/verify.py` | `normalise()`, `contains_span()`, `spans_equal()`, `AssertionType`, `Chunk`, `Claim`, `Assertion`, `Composition`, `EvidenceBundle`, `ClaimLookup`, `VerifiedCitation`, `VerifiedCitations`, `VerificationFailure`, `verify()` |

`Coverage` has **no public constructor** -- calling `Coverage(...)` directly
raises `TypeError`; `CoverageLedger.seal()` is the only producer. This is
part of the declared contract, not an implementation detail: a checker (or a
reviewer) can rely on "if a `Coverage` object exists, it balances."

## H2 -- Config-vs-code boundary

| Layer | What's config | What requires a fork |
|---|---|---|
| **L0** | Nothing -- it's a doc. Adopt the four laws as-is or don't adopt this accelerator at all. | The doc's wording itself, if a project needs different framing. |
| **L1** | The refusal literal's *value* is a constant you can rename in your own copy (not parameterise -- see the sentinel's own harvest note on why a configurable literal is a substring test away). `STATEMENT_TEMPLATES` in `refusal.py` is **meant** to be rewritten per project -- every string is neutral placeholder language. `RefusalKind`'s six members are the closed vocabulary; adding a seventh is a fork, not a config change. | The check structure in `is_refusal()` (must stay zero-import) and the all-or-nothing discard shape in `build_sources()`'s caller contract. |
| **L2** | **This is the layer's central config decision, and it is a real one, not decoration**: credentialed retrieval (Chroma, OpenAI embeddings, a hosted vector store -- PLA's shape) vs. `hash_embed`'s offline/deterministic ranking (RCA's shape, zero API key, what makes CI runnable without credentials). Which `EvidenceSource` implementation backs the Protocol is a per-project architecture decision, made once, not a runtime toggle. | The `EvidenceSource` Protocol's method shapes themselves; adding a method to the protocol is a contract change requiring every implementation to follow. |
| **L3** | `known_exclusions`, `corpus` label strings, and the `AbstentionType` taxonomy's six triggers are all adopter-supplied text/values. | **The genuinely hard adapt-not-reuse boundary is here.** RCA's `Corpus`/`ClaimStatus`/`Basis`/`Unit`/`Scope`/`Parameter`/`DocumentType` enums do NOT travel with this file (see H3). `verify.py`'s `Chunk`/`Claim`/`Assertion` are now plain dataclasses with `str` fields where RCA had closed enums -- an adopter is expected to either use these generic dataclasses as-is (accepting untyped strings) or fork them into their own typed enums before wiring in real domain logic. This is a fork either way; there is no config knob that avoids it. |

*"It's configurable" without this table fails admission (H2) -- this table
is the answer, not a substitute for reading it.*

## H3 -- Host decoupling, confirmed per file

Checked as this accelerator was written, not asserted after the fact.

| File | Host-domain imports found in the RCA/CFS source | Resolution |
|---|---|---|
| `sentinel.py` | None -- zero imports in the source already. | Copied verbatim, no change needed. |
| `refusal.py` | `app.comparability.dimensions.Dimension`, `app.coverage.ledger.Coverage`, `app.enums.quarantine.{QueryOutcome,RefusalKind}` | Removed. `RefusalKind`/`QueryOutcome` redefined generically in this file; `Coverage` replaced with a structural Protocol (`_CoverageLike`) so L1 does not import L3. **Fully genericised.** |
| `sources.py` | `app.enums.claim.ClaimStatus`, `app.enums.corpus.Corpus`, `app.grounding.verify.VerifiedCitations`, `app.model.source.{PublicSource,Source,WorkProductSource}` | Removed. Replaced with one generic `Source` dataclass (open `extra: dict`) and structural Protocols (`_VerifiedBundleLike`, `_VerifiedCitationLike`) instead of importing L3's concrete types. **Fully genericised**, and L1 now correctly does not depend on L3 at all. |
| `l2_retrieval/protocol.py` | `app.enums.case.JurisdictionCode`, `app.enums.corpus.Corpus`, `app.model.records.{Case,Chunk,Claim,Document,Jurisdiction}`, `app.retrieval.filters.ChunkPredicate` | Removed. Method signatures now typed against `object`/`str`/a generic `ChunkPredicate` callable. **One method dropped rather than genericised**: `read_jurisdiction(code: JurisdictionCode)` had no domain-neutral equivalent worth inventing, so it is simply absent from the generic Protocol -- an adopter needing it adds it back in their own fork. Flagged here rather than silently omitted. |
| `l2_retrieval/hash_embed.py` | None -- only `hashlib`, `numpy`. | Copied with unmodified logic, per the harvest brief. |
| `l3_assurance/coverage_ledger.py` | `app.coverage.standing.STANDING_EXCLUSIONS`, `app.enums.corpus.Corpus` | Removed. `corpus` fields are now plain `str` (default `"default"`); `known_exclusions` defaults to `()`, adopter-supplied via the existing constructor parameter. **Fully genericised**, invariant logic byte-for-byte otherwise. |
| `l3_assurance/abstention.py` | None in code (already zero-import beyond stdlib in the CFS source). | Docstring provenance kept; taxonomy trigger text lightly reworded to remove one CFS-internal term (`G-RESTYPE`) from a comment, no code change. |
| `l3_assurance/verify.py` | `app.enums.claim.{Basis,ClaimStatus,Scope,Unit}`, `app.enums.corpus.Corpus`, `app.grounding.compose.*` (Pydantic-schema types), `app.model.records.{Chunk,Claim}` | Removed. Replaced with plain dataclasses (`Chunk`, `Claim`, `Assertion`, `Composition`) with `str` fields in place of closed enums, and the Pydantic `BaseModel`/`ConfigDict`/schema-validation machinery is **not carried over** -- this file no longer has a Pydantic dependency. **This is the file where "adapt, not reuse" is least optional**: the six-member `AssertionType` vocabulary is kept as a plausibly-general RAG taxonomy, but nothing here enforces it stays exhaustive for a new domain, and the numeric-tuple comparison (`value, unit, scope, basis`) assumes a project has *some* four-part comparison key even though the parts are now untyped strings. |

**Overall H3 verdict: genericised, with one honest exception.** Every file
above passes a "no `from app.`, `from backend.`" grep (the same check
`test-scaffold`'s own H4 suite runs on itself). The one place this
accelerator did not invent a domain-neutral replacement is
`read_jurisdiction` in the L2 protocol, which was dropped rather than
faked into a false generality.

## H4 -- Own executable suite

`tests/run.sh` + `tests/test_kernel.py`. **Executed for real** (orchestrator
pass, 2026-08-09): `13 passed`, exit code 0. `mas-registrar` held no `Bash`
grant at harvest time and had marked this STATIC ONLY; the first real run
found and fixed two genuine bugs -- one in `src/` (a Python-version
portability defect), one in the test file itself -- see `CHANGELOG.md`
[1.0.1]. The suite exercises the sentinel closure property (by reading the
module's own source via AST, not a raw text scan), the coverage ledger's
seal/balance invariant (both directions -- fires and does not fire),
`build_sources`'s one-parameter arity, `verify()`'s all-or-nothing discard,
and the abstention module's UNKNOWN-never-negative invariant, all as
pure-Python unit tests with no live service, no network, and no
credentials.

## H5 -- Negative controls

Two guards in this accelerator have an explicit fire/not-fire pair in
`test_kernel.py`:

- `CoverageLedger.seal()`: `test_seal_succeeds_when_fully_dispositioned`
  (does not fire) vs. `test_seal_raises_when_undispositioned` and
  `test_double_disposition_raises` (fires).
- `verify()`'s all-or-nothing discard:
  `test_verify_succeeds_when_all_assertions_pass` (does not fire) vs.
  `test_verify_all_or_nothing_on_bad_citation` (fires on a bad quoted
  span).

Both pairs are, like the rest of H4, **executed for real** -- see above.

## H6 -- Provenance and rationale

| Source file | Exact path | Project gate status at harvest time |
|---|---|---|
| `sentinel.py` | `projects/rate-case-analyzer/dev/app/grounding/sentinel.py` | RCA: all 11 gates done; Code/Test gates record 899 tests, 8 blocking suites (Deploy gate independently re-derived 932 tests from a clean shell). |
| `refuse.py` -> `refusal.py` | `projects/rate-case-analyzer/dev/app/grounding/refuse.py` | Same. |
| `app/answer/sources.py` -> `sources.py` | `projects/rate-case-analyzer/dev/app/answer/sources.py` | Same. |
| `app/retrieval/protocol.py` -> `l2_retrieval/protocol.py` | `projects/rate-case-analyzer/dev/app/retrieval/protocol.py` | Same. |
| `app/retrieval/rank.py` -> `l2_retrieval/hash_embed.py` | `projects/rate-case-analyzer/dev/app/retrieval/rank.py` | Same. |
| `app/coverage/ledger.py` -> `coverage_ledger.py` | `projects/rate-case-analyzer/dev/app/coverage/ledger.py` | Same. |
| `app/grounding/verify.py` + `app/grounding/normalise.py` -> `verify.py` | `projects/rate-case-analyzer/dev/app/grounding/verify.py`, `.../normalise.py` | Same. |
| `backend/common/abstention.py` -> `abstention.py` | `projects/conclave-finance-studio/dev/backend/common/abstention.py` | CFS: all 11 gates done; 3,158 scenarios / 12 suites at Deploy (2026-08-06). **No module-scoped test count exists for `abstention.py` specifically** -- unlike RCA's L1/L3 files, this figure covers the whole product, not this module in isolation. Stated as a maturity gap, not glossed over. |

**Maturity claim, stated precisely per the harvest brief**: `L1` (sentinel)
and the `Coverage`/`CoverageLedger` half of `L3` are gate-10, 899-test
proven **in their source project**. `L2`'s `hash_embed`/`rank_within` are
likewise from the 899-test suite. `abstention.py` is from a separately
gate-10-complete product but without a module-specific test count. **None
of this maturity transfers to an adopting project** -- per
`solution-architect`'s standing rule, "reuse never lowers the evidence bar."

**What was deliberately left behind**: the worked reference implementation
(`kb-seed/reference_impl_note.md`); RCA's Pydantic-schema validation layer in
`compose.py` (not carried into `verify.py`, which now uses plain
dataclasses); RCA's `vintage.py` (staleness/freshness caveats) and
`prompts.py` (system-prompt text) -- both read during this harvest but
judged too RCA-specific in wording to genericise usefully in this pass, and
not included; `l2_retrieval`'s Chroma-backed adapter named in the approving
proposal's Seed-3 write-up ("a Chroma-backed adapter so PLA-shaped projects
satisfy the same protocol") -- **not built in this pass**, named here as a
gap alongside the reference implementation.

## H7 -- Semver + CHANGELOG

`VERSION` = `1.0.0`. `CHANGELOG.md` in this directory. A MAJOR bump requires
a migration note naming every known consumer (H10) -- there are none yet.

## H8 -- Deprecation

Not applicable at 1.0.0; no prior version exists to deprecate.

## H9 -- Co-signs (OPEN -- this is why status is `built`, not `admitted`)

**This accelerator sits on a grounding/refusal/guardrail path.** Per
`ADMISSION.md`'s H9, it therefore requires a **responsible-AI co-sign**
from `responsible-ai-architect` before it can move from `built` to
`admitted`. `mas-registrar` is not the agent who can give that co-sign and
has not attempted to.

**The specific open question flagged for that review**: does the L1
sentinel's zero-import closure guarantee hold once L3's enum types are
genericised, or does genericising risk reintroducing an import that breaks
the closure property? Concretely -- `sentinel.py` itself imports nothing and
this harvest changed none of its code, so the closure holds as shipped
today. But an adopter following this accelerator's own H2 guidance will, by
design, fork `verify.py`'s generic `Chunk`/`Claim`/`Assertion` dataclasses
back into typed domain enums, and `refusal.py`'s `_CoverageLike` Protocol is
structurally satisfied by whatever `Coverage` implementation an adopter
wires in. **Neither of those forks touches `sentinel.py`'s own import list**
-- the closure is scoped to exactly that one file plus its literal, by
design, and nothing else in L1/L3 is on the sentinel's own import path.
But `responsible-ai-architect` should confirm that reasoning independently
rather than accept it from the agent that did the harvest: the whole point
of AC-F31-12-style closure guarantees is that they are checked
mechanically, not argued for in prose, and no mechanical check of this
property has been run against the generalised files in this accelerator
(only against the original RCA source, at RCA's own gate 10).

## H10 -- Known consumers

None yet. This accelerator was harvested from `rate-case-analyzer` and
`conclave-finance-studio` (sources, not consumers of this accelerator
package) and its patterns already independently reached
`templates/rag-knowledge-base/` in a separate, already-completed increment
(the manifest requirement, `_extract_text` normalisation, scoped CORS, input
validation -- see that template's `backend/app/{ingest,rag,main}.py` for the
already-generalised form of a *different* subset of hardening deltas,
distinct from the four layers harvested here). No project has vendored
`accelerators/grounded-answer-kernel/` itself at any version.

## Adoption steps (for a future `solution-architect` / `code-agent`)

1. Read `src/l0_contract.md` first, regardless of which other layers you
   adopt.
2. Decide L2's central config question (H2): credentialed retrieval or
   `hash_embed`'s offline determinism. This is an Architecture-gate
   decision, not a default.
3. If adopting L3, budget real fork time for `verify.py`'s dataclasses --
   read the H3 table above before assuming they drop in.
4. Copy the files, stamp them with the provenance header
   (`accelerators/README.md`'s vendoring convention), and record the
   adoption in your project's `PROJECT_CONTEXT.md` `## Accelerators`
   section per H10.
5. Write your own acceptance criteria against your own use of this kernel.
   "Covered upstream by the accelerator" is never an answer to
   `NOT VERIFIED` at your project's Verification gate.
