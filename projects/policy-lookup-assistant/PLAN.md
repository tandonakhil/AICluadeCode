# PLAN.md — policy-lookup-assistant

## Feature

First real feature for this project: **grounded-refusal + authority-labeled
citations.** The `/ask` endpoint must (a) tag every retrieved chunk with the
document's authority level and an as-of date, surface that label alongside
every citation, and (b) explicitly refuse — rather than answer by
extrapolation — when the retrieved context doesn't actually contain the
answer to the question asked. This plan covers `FEATURES.md` items 1 and 2
together (they share the same metadata and prompt-construction changes) and
folds in item 4 (numeric-precision guardrail) as acceptance criteria rather
than separate code. The template (`rag-knowledge-base`) is already scaffolded
and confirmed correct at Intake; this plan does not revisit that choice.

## Why this feature first

Both `knowledge/DOMAIN_KB.md` and `knowledge/INDUSTRY_KB.md` converge on this
as the highest-leverage first build:
- DOMAIN_KB risk #1 (wrong-authority citations), #3 (numeric precision), #5
  (silent extrapolation), #6 (incentive-stacking trap) are all either
  directly fixed or directly tested by this feature.
- INDUSTRY_KB's proposed items #1 (authority/as-of badge) and #3
  (insufficient-evidence refusal) are its top two backlog items, both
  scoped to exactly this change.
- The template's current baseline (`backend/app/rag.py`) already does
  retrieval + generic citation-by-filename — this feature is the smallest
  concrete step that turns that baseline into something a regulated-utility
  deployment can trust, per the Moffatt v. Air Canada liability precedent in
  DOMAIN_KB.

## Baseline (confirmed by reading the existing template code)

- `backend/app/ingest.py` loads every `.txt` file in
  `data/sample_docs/` and tags each chunk's metadata with only
  `{"source": filename}`. No authority/type/date metadata exists today.
- `backend/app/rag.py`'s `ask()` does `similarity_search(question, k=3)`,
  concatenates the top-k chunks into a system prompt with a generic
  instruction ("use ONLY the context... if the context doesn't contain the
  answer, say so rather than guessing"), and returns `{"answer": ...,
  "sources": [...]}"` where `sources` is just a sorted set of filenames.
  The "say so" instruction already exists in prose but is unenforced,
  untested, and not surfaced in the response shape — there's no structured
  signal the frontend (or a test) can check to confirm a refusal actually
  happened rather than a hedge buried in prose.
- `backend/app/main.py`'s `POST /ask` passes `ask()`'s return value straight
  through as the response body — no new fields needed there beyond what
  `ask()` now returns.
- Sample docs: `grid_maintenance_policy.txt` (utility's own internal
  operating standard — no regulator letterhead, reads as internal policy)
  and `renewable_incentives_faq.txt` (explicitly an FAQ). Per DOMAIN_KB,
  neither is a binding regulation; both are lower-authority document types,
  which is itself useful for testing the badge (both should read as
  non-regulation).

## File / module changes

### New: `backend/data/sample_docs/manifest.json`
- A small JSON file, one entry per sample doc, keyed by filename:
  ```json
  {
    "grid_maintenance_policy.txt": {
      "authority": "internal_policy",
      "label": "Internal Policy",
      "as_of": "2026-01-01"
    },
    "renewable_incentives_faq.txt": {
      "authority": "faq",
      "label": "FAQ — Informal Guidance",
      "as_of": "2026-01-01"
    }
  }
  ```
- `authority` is a closed enum used for logic/sorting:
  `regulation | guidance | internal_policy | faq`. `label` is the
  human-readable string shown to the user (kept separate from `authority` so
  copy can change without touching logic). `as_of` is a placeholder date
  (today's project-creation date, since neither sample doc carries a real
  publication date) — this is explicitly a stand-in for real per-document
  effective dates, which item 6 (staleness alerting) will make load-bearing
  later; for this feature it only needs to round-trip into the response.
- A manifest file (not inline Python dict, not front-matter in the .txt
  files) is the ingestion-time source of truth so that adding a new document
  later is "add the file + add one manifest entry," not a code change —
  matches how code-agent will extend the real corpus post-MVP.
- If a `.txt` file has no manifest entry, ingestion must fail loudly (raise),
  not default silently to some authority level — an untagged document
  silently defaulting to, say, "internal_policy" is exactly the
  wrong-authority-citation risk this feature exists to prevent.

### Modify: `backend/app/ingest.py`
- `load_documents()` reads `manifest.json` once, and for each `.txt` file
  looks up its entry, raising `ValueError` with the filename if missing.
- Each `Document`'s metadata becomes
  `{"source": filename, "authority": ..., "label": ..., "as_of": ...}`
  (Chroma metadata values must be str/int/float/bool — all three added
  fields are strings, so no serialization change needed).
- No change to chunking (`RecursiveCharacterTextSplitter`, chunk_size=500,
  overlap=50) or to `Chroma.from_documents` call shape — LangChain persists
  arbitrary metadata dict keys through to `similarity_search` results
  automatically.

### Modify: `backend/app/rag.py`
- `ask()` changes in three ways:
  1. **Structured per-source metadata in the response.** Replace the
     `sources: list[str]` field with `sources: list[dict]`, one entry per
     unique filename among the retrieved chunks:
     `{"document": filename, "label": label, "authority": authority,
     "as_of": as_of}`. This is the authority badge data the frontend (or a
     test) reads directly, instead of parsing prose.
  2. **Refusal is a structured field, not prose-only.** Add a boolean
     `sufficient_evidence` field to the return dict. The system prompt is
     rewritten to require the model to open its response with a fixed
     sentinel token on its own first line — `INSUFFICIENT_EVIDENCE` — if and
     only if the retrieved context does not contain enough information to
     answer the question; otherwise it omits the token entirely.
     `ask()` checks for that sentinel in `response.content`, sets
     `sufficient_evidence = False` and strips the sentinel line from the
     user-facing `answer` text if present (replacing it with a fixed,
     product-controlled refusal sentence — not the model's own phrasing —
     so the refusal message is consistent and testable), else
     `sufficient_evidence = True`. This keeps the enforcement point in
     application code rather than trusting the model's prose to always be
     parseable, while still relying on the model to make the underlying
     judgment call (no separate classifier model in this pass — see
     Design Decisions).
  3. **System prompt rewrite** to fold in authority framing and the
     numeric-precision guardrail (FEATURES.md item 4), e.g.:
     - Each context block is now
       `[Source: {filename} | Type: {label} | As of: {as_of}]\n{content}`
       instead of just `[Source: {filename}]`.
     - Explicit instruction: quote numeric figures (percentages, dollar
       amounts, time windows, counts) exactly as they appear in the source
       text — do not paraphrase, round, or average across chunks.
     - Explicit instruction: if the question asks about something adjacent
       to but not directly stated in the context (e.g., a program/type/
       jurisdiction not mentioned), treat that as insufficient evidence
       rather than answering by analogy — this directly targets DOMAIN_KB
       risk #6 (incentive-stacking trap) and risk #5 (silent
       extrapolation).
     - Explicit instruction to emit `INSUFFICIENT_EVIDENCE` per the rule
       above.
- Response shape after this change:
  ```json
  {
    "answer": "...",
    "sufficient_evidence": true,
    "sources": [
      {"document": "grid_maintenance_policy.txt",
       "label": "Internal Policy", "authority": "internal_policy",
       "as_of": "2026-01-01"}
    ]
  }
  ```
- The `k=3` retrieval parameter and `similarity_search` call are unchanged —
  this feature is about what's done with retrieved chunks and how failure is
  reported, not retrieval tuning (chunking/retrieval-quality work is
  FEATURES.md item 5, explicitly deferred).

### Modify: `backend/app/main.py`
- No structural change needed — `ask_endpoint` already returns whatever
  `ask()` returns, so the richer response shape flows through automatically.
  (Confirmed by reading the existing 20-line file — there is no
  response-model/schema declared on the FastAPI route today, so no Pydantic
  response model needs updating either. Flagging this as an accepted gap:
  a `AskResponse` Pydantic model would give FastAPI-generated docs and
  validation for free, but adding it is not required for this feature to
  work and is deferred to avoid scope creep in this pass.)

### Modify: `backend/tests/test_smoke.py`
- Existing `test_health` stays unchanged.
- Add a comment block (no new automated test requiring a live API key, same
  pattern as today) noting that the new `sufficient_evidence` / `sources[*]`
  shape is exercised at the Test gate's behavioral checks below, consistent
  with how `/ask`'s original behavior was already deferred to that gate.

### Not changed in this pass
- `backend/app/embeddings.py`, `backend/app/llm.py` — provider/embedding
  selection is unaffected; this is a prompt-construction and metadata
  concern.
- `frontend/` — still the template placeholder. Rendering the authority
  badge and refusal state in the UI is the Experience Design gate's job
  once the backend contract above is stable; this plan only guarantees the
  new response fields exist for that gate to consume.
- Chunk size/overlap/retrieval `k` — left at template defaults; tuning these
  against the emergency-clause retrieval risk (DOMAIN_KB risk #7) is
  FEATURES.md item 5, deliberately deferred until this feature's
  evidence-sufficiency behavior is in place and can be used to detect
  retrieval gaps.
- No new dependencies — manifest parsing uses stdlib `json`, already
  available.

## Key design decisions and trade-offs

1. **Sentinel-token refusal signal, not a second classifier call or a
   regex-only prose check.** Asking the same model call to self-report via a
   fixed token is cheap (no extra LLM round-trip) and more reliable than
   regexing for phrases like "the context doesn't contain" in free-form
   prose, which the numeric-precision and citation instructions in the same
   prompt would otherwise make brittle to match. Trade-off: this still
   trusts the model to correctly judge sufficiency — it is a prompting
   discipline, not a formal guarantee. If Test-gate runs show the model
   frequently answers instead of emitting the token when it should refuse,
   the next iteration should consider a stricter approach (e.g., a
   relevance-score threshold on retrieved chunks as an additional, code-side
   gate before the LLM call). That's flagged, not built preemptively.

2. **Manifest file for authority metadata, not per-document front-matter or
   a hardcoded dict in `ingest.py`.** A separate `manifest.json` keeps
   metadata edits independent of both document content and ingestion code,
   and mirrors how a real deployment would receive authority tags from
   whoever manages the corpus (likely not the same person editing Python).
   Trade-off: introduces a manual sync requirement (new doc without a
   manifest entry fails ingestion) — treated as a feature, not a bug, since
   DOMAIN_KB risk #1 specifically warns against defaulting untagged content
   to a plausible-looking authority level.

3. **Closed `authority` enum with 4 values matching DOMAIN_KB's taxonomy**
   (`regulation | guidance | internal_policy | faq`), even though neither
   current sample doc is tagged `regulation` or `guidance`. Modeling the
   full taxonomy now — rather than just the two levels the current corpus
   happens to use — means the next real document (e.g., an actual FERC/PUC
   citation) doesn't require a schema change, only a manifest entry.

4. **Refusal replaces the model's own phrasing with a fixed product string**
   (e.g., "The available documents don't contain enough information to
   answer this question."), rather than passing the model's own refusal
   prose through. This keeps refusal messaging consistent and testable
   (Test gate can assert exact/substring match) and avoids the model
   inventing hedged-but-still-partially-answering text after the sentinel,
   which would undercut the point of a hard refusal signal.

5. **No jurisdictional-layer disambiguation logic in this pass** (DOMAIN_KB
   risk #4). The current sample corpus doesn't contain multiple
   jurisdictional layers describing the same rule, so there's nothing to
   disambiguate yet — building that logic now would be speculative. Carried
   forward in `FEATURES.md` as an explicit non-goal until the corpus grows.

## Acceptance criteria (Test gate)

Functional / wiring:
- `GET /health` still returns `200 {"status": "ok"}` (unchanged).
- After running `python -m app.ingest`, every chunk in the Chroma store
  carries non-empty `authority`, `label`, and `as_of` metadata fields.
- Ingesting with a `.txt` file present in `data/sample_docs/` that has no
  corresponding `manifest.json` entry raises an error and aborts ingestion
  (does not silently proceed).
- `POST /ask` response body contains `answer` (string), `sufficient_evidence`
  (bool), and `sources` (list of objects each with `document`, `label`,
  `authority`, `as_of` keys) — for every query, not just refusals.

Behavioral (qualitative, checked via example prompts against `/ask` with the
two sample docs ingested):
- Q: "How long after a substation exceeds 90% capacity for two hours must it
  be flagged for inspection?" → `sufficient_evidence: true`; answer states
  "48 hours" exactly (not "about two days" or similar paraphrase); at least
  one source entry has `document: "grid_maintenance_policy.txt"` and
  `label: "Internal Policy"`.
- Q: "What's the residential solar rebate cap?" → `sufficient_evidence:
  true`; answer states "$4,000" and "20%" exactly; source entry shows
  `document: "renewable_incentives_faq.txt"`, `label: "FAQ — Informal
  Guidance"`.
- Q: "What's the commercial solar rebate cap?" (the corpus only defines a
  *residential* solar rebate and a *commercial wind* incentive — no
  commercial solar figure exists) → `sufficient_evidence: false`; answer is
  the fixed refusal string; answer must NOT contain a dollar figure or
  percentage (i.e., must not extrapolate the residential solar cap onto
  commercial solar). This is the direct DOMAIN_KB risk #5/#6 regression
  test.
- Q: "Can I stack the residential solar rebate with a municipal program?" →
  the FAQ says yes "unless explicitly stated otherwise in the municipal
  program's terms" — a municipal program's terms are not in this corpus.
  Acceptable per this pass: `sufficient_evidence: true` with an answer that
  states stacking is generally allowed *and* explicitly notes the
  municipal-program-terms caveat is not covered by the ingested documents.
  (Full disambiguation of this case is a judgment call the Test gate should
  flag as pass/fail based on whether the caveat is present, not require a
  refusal — this is documented here so the human tester isn't surprised by
  either qualifying outcome.)
- Q: "What's the maintenance policy in Germany?" (jurisdiction not
  represented anywhere in the corpus) → `sufficient_evidence: false`;
  answer does not fabricate a policy.
- Q: "What is the capital of France?" (fully out-of-domain) →
  `sufficient_evidence: false` (or an answer that plainly states the corpus
  doesn't cover this) — must not have the model reach outside the corpus to
  answer general knowledge, since that would undercut the entire
  grounding guarantee this feature exists to provide.

Out of scope for this Test gate (do not fail the build on these):
- Frontend UI rendering of the authority badge or refusal state (no UI
  changes in this pass).
- Retrieval-quality tuning for the emergency-maintenance carve-out
  (FEATURES.md item 5).
- Real per-document `as_of` dates beyond the placeholder in the manifest
  (FEATURES.md item 6, staleness alerting).
- A `regulation`/`guidance`-labeled document existing in the corpus (neither
  sample doc is one; the enum is modeled for future use, not exercised by
  today's sample docs).
