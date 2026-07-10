# Architecture Knowledge Base: policy-lookup-assistant

Owner: solution-architect
Gate: Architecture (first pass — covers PLAN.md's first feature:
grounded-refusal + authority-labeled citations)

This document designs the *how* for PLAN.md's already-approved *what*. It
does not revisit scope decisions made at the Plan gate; it only adds the
technical shape needed to implement them, consistent with `UX_KB.md`'s
4-state design.

---

## 1. Component design

Three existing modules change; no new services or processes are introduced.

### 1.1 Manifest validation — lives in `ingest.py`, at ingestion time, not at query time

`load_documents()` becomes the single place that reads `manifest.json` and
joins it against the files on disk in `data/sample_docs/`. This is a
deliberate choice: **authority metadata is validated once, at ingestion,
and then travels with the data** (baked into each `Document`'s metadata,
persisted by Chroma alongside the vectors). `rag.py`'s `ask()` never touches
`manifest.json` directly — it only ever reads `metadata["authority"]`,
`metadata["label"]`, `metadata["as_of"]` off whatever `similarity_search`
returns. This keeps the query path (`ask()`, called on every request) free
of file I/O and free of a second copy of the validation logic, and it means
a manifest error surfaces at `python -m app.ingest` time — a human running a
CLI command who will see the traceback — rather than surfacing as a 500 on
some future `/ask` call to an end user who didn't touch the manifest.

Concretely:
```python
def load_documents():
    manifest_path = os.path.join(DOCS_DIRECTORY, "manifest.json")
    with open(manifest_path) as f:
        manifest = json.load(f)

    documents = []
    for filename in sorted(os.listdir(DOCS_DIRECTORY)):
        if not filename.endswith(".txt"):
            continue
        if filename not in manifest:
            raise ValueError(f"No manifest entry for {filename!r} — add one to manifest.json before ingesting.")
        entry = manifest[filename]
        path = os.path.join(DOCS_DIRECTORY, filename)
        with open(path) as f:
            documents.append(Document(
                page_content=f.read(),
                metadata={"source": filename, **entry},
            ))
    return documents
```
`**entry` spreads `authority`/`label`/`as_of` directly — no per-field
plumbing to update if the manifest schema grows a field later (e.g., a
future `as_of` becoming a real date, or a `version` field for staleness
alerting in FEATURES.md item 6). Trade-off: this also means an
accidentally-malformed manifest entry (e.g., a typo'd key) silently becomes
extra Chroma metadata rather than failing loudly on the *unwanted* keys —
acceptable for a 2-entry hand-written manifest at MVP scale; if the corpus
grows enough that manifest entries are generated/edited by more people,
add a schema check (e.g., assert the entry has exactly `{authority, label,
as_of}` and `authority` is in the closed enum) at the same load point. Not
built now — flagged as a cheap follow-up, not a gap in this pass, per
PLAN.md's non-goal framing for speculative work.

**No separate "manifest validator" module.** A standalone validator adds a
layer of indirection for a ~20-line check that only ever runs from one call
site (`load_documents()`). If a second call site emerges (e.g., a future
admin/upload endpoint that adds documents at runtime), extract the
validation into a shared function then — YAGNI for a single caller.

### 1.2 Sentinel-token parsing — lives in `rag.py`'s `ask()`, string-based, not regex

Per PLAN.md decision #1, the sentinel is a fixed literal
(`INSUFFICIENT_EVIDENCE`) that the prompt instructs the model to emit **as
its own first line**, and only when refusing. Parsing this reliably means:

```python
content = response.content.strip()
sufficient_evidence = not content.startswith("INSUFFICIENT_EVIDENCE")
if not sufficient_evidence:
    answer = REFUSAL_MESSAGE  # fixed, product-controlled string
else:
    answer = content
```

Design choices here, made explicit because they're easy to get subtly
wrong:
- **`.startswith()` on the stripped content, not `in` / substring search
  anywhere in the response.** A substring check would false-positive if the
  model ever discusses the token itself (unlikely but not impossible given
  it appears in the system prompt) or echoes it mid-answer while still
  answering. Anchoring to "first line, after stripping leading
  whitespace" matches exactly what the prompt asks the model to do and
  nothing looser.
- **On refusal, the model's own content is discarded entirely** — not
  trimmed/stripped of the sentinel line and reused. PLAN.md decision #4 is
  explicit that the refusal string must be product-controlled, not
  model-phrased, specifically so a partially-hedging answer can't leak
  through after the sentinel. Implementation-wise this simplifies the
  parsing too: no need to find-and-remove a substring from arbitrary
  positions in the text, just a boolean branch.
- **Only `.strip()` is used for normalization** — no case-insensitive match,
  no fuzzy match on token variants. The prompt fully controls the token's
  exact casing and the model is instructed to emit it verbatim; loosening
  the match (e.g., `"insufficient_evidence" in content.lower()`) trades a
  small robustness gain for a much larger false-positive-refusal risk (a
  user question that happens to contain similar words). If Test-gate runs
  show the model emitting near-miss variants (extra punctuation, wrapped in
  markdown like `**INSUFFICIENT_EVIDENCE**`), the fix is prompt tightening
  first (e.g., "emit the token with no other characters on that line"), not
  looser parsing — a looser regex papers over a prompting problem and
  reintroduces exactly the brittleness PLAN.md decision #1 was trying to
  avoid by choosing a sentinel over prose-regexing in the first place.

### 1.3 `/ask` response schema — no route-layer change, but a `Pydantic` model is worth adding now

PLAN.md's plan explicitly flags the missing `AskResponse` Pydantic model as
an "accepted gap... deferred to avoid scope creep." Solution-architect's
recommendation, as the person who owns *how* things are wired: **add the
response model in this pass anyway**, because it's a ~10-line addition, not
new scope — it doesn't change `ask()`'s return shape or any behavior, it
only types what's already true:

```python
class SourceInfo(BaseModel):
    document: str
    label: str
    authority: str
    as_of: str

class AskResponse(BaseModel):
    answer: str
    sufficient_evidence: bool
    sources: list[SourceInfo]

@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest):
    return ask(request.question)
```
This is the one place this document deviates from "how, not what" — it's
not a scope change, it's a wiring detail that directly serves PLAN.md's own
stated goal ("a structured signal the frontend... can check"). Without a
declared response model, a future accidental shape drift in `ask()` (e.g.,
someone renames `document` to `filename`) would silently break the frontend
with no error until manual testing catches it; with the model, FastAPI
raises a `ResponseValidationError` at the point of the bug. If the human
reviewing this KB wants to keep it out of this pass strictly per PLAN.md's
text, that's a one-line revert — flagging it here rather than silently
adding it un-flagged.

This directly enables the four UX states in `UX_KB.md` section 1.3: the
frontend's state machine is `sufficient_evidence` (boolean) driving
Answered vs. Refused, `sources` (array) driving whether `SourceBadgeList`
renders anything, and the existing `AskRequest`/loading-transition pattern
already covering Empty/Asking. No additional response field is needed for
any of the 4 states — confirmed by walking each UX_KB row against the
schema above.

### 1.4 No new component/module boundaries

Everything above is a change to the *body* of three existing functions
(`load_documents`, `ask`, `ask_endpoint`), not a new architectural
boundary. `embeddings.py` and `llm.py` are untouched, matching PLAN.md's
"not changed in this pass" list — retrieval and model-selection concerns
are orthogonal to metadata plumbing and refusal signaling.

---

## 2. Data flow

```
manifest.json ──┐
                ├─► load_documents() ─► Document.metadata{source, authority, label, as_of}
sample_docs/*.txt ┘                          │
                                              ▼
                                RecursiveCharacterTextSplitter (unchanged)
                                              │
                                              ▼
                                  Chroma.from_documents() (persists metadata as-is)
                                              │
                                   ═══════ ingestion ends / query begins ═══════
                                              │
question ──► similarity_search(question, k=3) ─► docs[] (each carries authority/label/as_of)
                                              │
                                              ▼
                        context blocks: "[Source: f | Type: label | As of: date]\n{content}"
                                              │
                                              ▼
                              system_prompt (authority framing + numeric-precision +
                              insufficient-evidence + sentinel-emission instructions)
                                              │
                                              ▼
                                    model.invoke([system, human])
                                              │
                                              ▼
                        sentinel check on response.content.strip()
                          ├─ starts with INSUFFICIENT_EVIDENCE → answer = fixed refusal string, sufficient_evidence=False
                          └─ else → answer = response.content, sufficient_evidence=True
                                              │
                                              ▼
                sources = [{document, label, authority, as_of} for unique filename in docs]
                                              │
                                              ▼
                        {answer, sufficient_evidence, sources} ─► AskResponse (Pydantic) ─► JSON
                                              │
                                              ▼
                          frontend renders Answered/Refused per UX_KB.md 1.3
```

Two properties of this flow are worth calling out because they're
load-bearing for correctness, not just implementation detail:

1. **Metadata never round-trips through the LLM as structured data** — it's
   flattened into the prompt text (`[Source: ... | Type: ... | As of:
   ...]`) for the model to *read and reference in its answer*, but the
   `sources[]` field in the final response is built by the application
   directly from `docs[].metadata`, not parsed back out of the model's
   answer text. This means a citation badge is always accurate to what was
   actually retrieved, even if the model's prose citation is imperfect —
   the UI's authority badge is never dependent on the model correctly
   naming its source in free text.
2. **The sentinel decision and the `sources[]` list are independent
   pipelines that happen to share one LLM call.** `sources[]` is derived
   from `docs` (the retrieval result) unconditionally, before the model
   responds at all — even on a refusal, `docs` still exists (it's just that
   the model judged the *content* insufficient to answer from). PLAN.md's
   UX_KB section 1.2 state 4 says "No authority badges rendered in this
   state" — that's a **frontend** rendering decision (don't render
   `SourceBadgeList` when `sufficient_evidence` is false), not a backend
   one. The backend should still populate `sources[]` on a refusal exactly
   as it does on a success (same `docs`-derived list), since suppressing it
   server-side would remove information a future debugging/Test-gate pass
   might want (e.g., "which chunks did it see and still refuse on"). This
   is a place where architecture and UX intent could be read two ways —
   flagging the resolution explicitly: **backend always populates
   `sources[]`; frontend decides whether to render it.**

---

## 3. Technology choices

**No new dependencies.** Everything needed is already in
`backend/pyproject.toml`:
- Manifest parsing: stdlib `json` (already used implicitly via
  `pydantic`/FastAPI's JSON handling elsewhere; no new import needed beyond
  `import json` in `ingest.py`).
- Sentinel parsing: plain Python string methods (`.strip()`,
  `.startswith()`) — no regex library needed, deliberately (see 1.2).
- Response schema: `pydantic>=2.8` is already a direct dependency (FastAPI
  requires it); `SourceInfo`/`AskResponse` are new model *classes*, not a
  new package.
- Chroma metadata: `langchain-chroma>=0.1` already persists arbitrary
  str/int/float/bool metadata keys per document — confirmed by reading
  `ingest.py`'s existing `Chroma.from_documents()` call, which already
  passes through `{"source": filename}` today with no serialization step;
  adding three more string keys is the same code path.

This confirms PLAN.md's own claim ("No new dependencies... manifest
parsing uses stdlib json, already available") — solution-architect finds
no reason to add anything beyond what PLAN.md scoped.

---

## 4. Trade-offs (architecture-level, beyond what PLAN.md's Design Decisions already cover)

1. **Ingestion-time validation vs. query-time validation.** Chosen:
   ingestion-time (see 1.1). Trade-off: if `manifest.json` is edited (e.g.,
   an authority level corrected) without re-running `python -m app.ingest`,
   the Chroma store keeps serving stale metadata until the next ingestion —
   there's no live reconciliation. Acceptable at this scale (a manual,
   infrequent, single-operator re-ingestion step) but should be
   re-evaluated if authority corrections become frequent enough to need a
   faster feedback loop than "re-run ingestion."
2. **Adding the `AskResponse` Pydantic model now, contrary to PLAN.md's
   explicit deferral.** See 1.3. Low-risk, additive, and directly serves
   PLAN.md's own goal, but noted as a deviation from what was written, not
   silently slipped in.
3. **`sources[]` always populated, even on refusal**, deferring "hide
   badges" purely to the frontend. See section 2, point 2. Alternative
   considered: backend returns `sources: []` on refusal to make the API
   contract self-describing without relying on frontend logic — rejected
   because it destroys information (which chunks were retrieved-but-judged-
   insufficient) that's useful for debugging retrieval quality
   (FEATURES.md item 5, explicitly a future item that will want this data).
4. **No relevance-score threshold gate before the LLM call** — PLAN.md
   decision #1 already flags this as a possible future iteration if the
   sentinel proves unreliable in Test-gate runs; solution-architect concurs
   this is correctly deferred rather than built preemptively, since Chroma
   similarity scores would need empirical threshold-tuning against this
   specific corpus before they could be trusted as a gate, and that tuning
   work doesn't exist yet.

---

## 5. Open items for security-architect (raised here so both KBs cross-reference)

- Confirming `.env`/`.gitignore` handling is security-architect's domain,
  but solution-architect notes for the record: `ingest.py`'s new
  `manifest.json` read introduces one more file-path join
  (`os.path.join(DOCS_DIRECTORY, "manifest.json")`) using the same
  `DOCS_DIRECTORY` constant already in the file — no new path-traversal
  surface, since `DOCS_DIRECTORY` is a fixed constant, not derived from any
  request input, and `manifest.json`'s filename is a literal, not
  user-supplied.
- The `/ask` endpoint's only external input is `request.question: str`
  (already validated as a string by the existing `AskRequest` Pydantic
  model) — solution-architect did not identify a need for additional
  input-shape validation beyond what security-architect independently
  assesses in `SECURITY_KB.md` (e.g., length limits, injection framing for
  the system-prompt-construction step in `ask()`).
