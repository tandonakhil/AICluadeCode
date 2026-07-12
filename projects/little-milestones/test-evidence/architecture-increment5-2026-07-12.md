# Architecture test-suite evidence — Increment 5 (F13, chat history + suggested prompts)

**Owner:** solution-architect
**Date:** 2026-07-12
**Scope:** Test-gate verification that shipped code matches ARCHITECTURE_KB.md §10
exactly (chat history schema, 4-hour session-boundary logic, snippet
immutability, `/chat` wire contract, `/suggested_prompts`, no-pagination
decision, route-signature contract).

Files read: `dev/backend/app/chat_sessions.py`,
`dev/backend/app/routes/chat.py`, `dev/backend/app/routes/chat_sessions.py`,
`dev/backend/app/db.py`, `dev/backend/app/routes/profiles.py`,
`dev/backend/app/suggested_prompts.py`, `dev/backend/app/ages.py`,
`dev/backend/tests/test_route_signatures.py`.

---

## Scenario 1 — Schema matches §10.1 exactly

**Checked:** `db.py` SCHEMA block, lines 131–150.

- `chat_sessions(id INTEGER PRIMARY KEY AUTOINCREMENT, profile_id INTEGER
  NOT NULL REFERENCES profiles(id) ON DELETE CASCADE, snippet TEXT NOT
  NULL, message_count INTEGER NOT NULL DEFAULT 0, created_at, last_message_at)`
  — matches §10.1 verbatim.
- `chat_messages(id INTEGER PRIMARY KEY AUTOINCREMENT, session_id INTEGER
  NOT NULL REFERENCES chat_sessions(id) ON DELETE CASCADE, role TEXT NOT
  NULL CHECK(role IN ('user','assistant')), content TEXT NOT NULL,
  created_at)` — matches §10.1 verbatim.
- Both indices present exactly as specified:
  `idx_chat_sessions_profile_recency ON chat_sessions (profile_id,
  last_message_at)` and `idx_chat_messages_session_created ON
  chat_messages (session_id, created_at)`.
- `ON DELETE CASCADE` present on both FKs (`chat_sessions.profile_id →
  profiles`, `chat_messages.session_id → chat_sessions`).
- **Id convention verified as the deliberate departure §10.1 specifies:**
  both tables use plain `INTEGER PRIMARY KEY AUTOINCREMENT` — confirmed
  this was *not* accidentally reverted to the `photo_meta.id` TEXT/uuid4
  pattern. `photo_meta`'s schema block (lines 90–106) is unchanged and
  still correctly TEXT/uuid4 for its own (unrelated, filename-doubling)
  reason — the two patterns coexist correctly, not conflated.
- `ChatSessionStore` in `chat_sessions.py` confirms the transitive-scoping
  shape (`list_for_profile(profile_id)`, `list_for_session(session_id)`,
  no `family_id` column/param anywhere in the store) matching
  `MemoryStore`/`PhotoStore`'s established pattern, not `ProfileStore`'s
  direct-scoping shape.

**Verdict: PASS.** No deviation.

---

## Scenario 2 — 4-hour boundary logic matches §10.2

**Checked:** `chat_sessions.py` lines 24–27, 133–164.

- `CHAT_SESSION_GAP_HOURS = 4` is a module-level config constant, not
  hardcoded inline in the comparison — confirmed (line 27, referenced by
  name at line 151, not a literal `4` re-typed at the call site).
- `resolve_or_create_session`'s actual logic (lines 133–164):
  - `needs_new = existing is None or force_new` — covers "no session
    exists" and the explicit forced-new case in one expression.
  - If a session exists and `force_new` is false: `gap = now -
    _parse_db_datetime(existing["last_message_at"]); needs_new = gap >
    timedelta(hours=CHAT_SESSION_GAP_HOURS)` — exactly the `now -
    last_message_at > 4h` comparison §10.2 specifies, computed against
    `last_message_at` (not `created_at`), which is the correct field for
    an *inactivity* gap (a session's clock resets on every turn, not just
    at creation).
  - Comparison is the boolean OR of exactly the three conditions §10.2
    lists: no session exists, gap exceeds threshold, or `force_new`. No
    additional undocumented condition found.
- Timezone handling (`_parse_db_datetime`/`_format_db_datetime`) is
  consistent — SQLite's naive UTC strings are tagged UTC-aware on read, so
  the `now - last_message_at` subtraction is never comparing a naive and
  aware datetime (which would raise, not silently misbehave — verified
  this isn't a latent bug, not just documented-as-fine).

**Verdict: PASS.** No deviation.

---

## Scenario 3 — Snippet handling matches §10.3

**Checked:** `chat_sessions.py` lines 70–76, 133–191; `routes/chat.py`
lines 96–120.

- `make_snippet` truncates `request.message` (the parent's own text) at
  `SNIPPET_MAX_LENGTH = 80`, called only from
  `resolve_or_create_session`'s insert path (line 161) — i.e. only at
  session-creation time, never elsewhere.
- `record_turn` (lines 166–191) inserts both `chat_messages` rows and
  updates `message_count`/`last_message_at` only — confirmed by reading
  its full body that it contains **no** reference to `snippet` at all
  (its docstring even states this explicitly: "Snippet is never touched
  here").
- **Call-order check in `chat.py` (the specific concern flagged):**
  `safe_text = enforce(raw_text, ...)` runs at line 101, *before* session
  resolution. `resolve_or_create_session(profile.id,
  first_message_if_new=request.message, force_new=request.new_session)`
  runs at line 117–119, using `request.message` — the parent's raw input
  — not `safe_text`. `record_turn(session_id, request.message, safe_text)`
  at line 120 stores both sides, but by that point the snippet (if this
  call created a new session) was already fixed from `request.message` at
  line 117–119, three lines earlier, and is never revisited. Confirmed:
  `enforce()`'s output (`safe_text`) never reaches the snippet at any
  point in the call graph — it's structurally impossible given
  `make_snippet`'s single call site, not merely conventionally avoided.

**Verdict: PASS.** No deviation. Snippet is immutable post-creation and
guardrail-output-isolated, exactly as designed.

---

## Scenario 4 — `/chat` contract matches §10.4

**Checked:** `routes/chat.py` lines 38–46, 74–131.

- `ChatRequest.new_session: bool = False` (line 45) — genuinely optional
  with a default; a client that never sends this field is unaffected
  (Pydantic fills the default, existing implicit-resume behavior holds).
  Verified it's the *only* new request field — `profile_id`, `message`,
  `history` are unchanged.
- Response body (lines 128–131): `{"text": safe_text, "disclaimer":
  DISCLAIMER, "session_id": session_id}` — `text` and `disclaimer` fields
  and their values are unchanged from the pre-Increment-5 shape (same
  `DISCLAIMER` constant, same `safe_text` variable). `session_id` is the
  only addition. `X-LM-Disclaimer` header unchanged (`DISCLAIMER_HEADER_SAFE`,
  same as before).

**Verdict: PASS.** No deviation. Wire contract is additive-only as
designed.

---

## Scenario 5 — `/suggested_prompts` matches §10.5

**Checked:** `routes/profiles.py` lines 197–218; `suggested_prompts.py`
(full file).

- Genuinely server-side: `build_suggested_prompts` runs entirely in
  `app/suggested_prompts.py`, called from the route handler
  (`routes/profiles.py` line 215) — no delegation back to the client, no
  client-side bucket computation implied anywhere in this surface.
- `suggested_prompts.py`'s own docstring and imports confirm the
  never-raw-LLM-origination discipline: "Nothing here ever calls
  `app.llm`" — confirmed, no `llm`/`get_chat_model` import anywhere in the
  file.
- T1/T2/T3/T4 template logic reuses existing bucket logic rather than
  duplicating age→bucket assignment:
  - T1 (`_bucket_domain`) calls `app.milestones.get_bucket_content` —
    reuses the curated-table lookup, does not re-derive bucket boundaries.
  - T2 calls `app.ages.next_bucket(ages.bucket_months)` directly —
    the exact same function `routes/profiles.py`'s `/activities` route
    already uses for its "coming next" preview (confirmed by reading
    `ages.py`: `next_bucket` walks the single `CHECKLIST_BUCKETS` list,
    the same list `checklist_bucket`/`compute_age` use — one source of
    truth for bucket boundaries, not a second copy).
  - The age→bucket assignment itself (`compute_age`, `checklist_bucket`)
    is never re-implemented in `suggested_prompts.py` — the route handler
    computes `ages = compute_age(...)` once (line 214) and passes the
    resulting `AgeResult` in; `suggested_prompts.py` only reads
    `ages.bucket_months`/`ages.mode`, never recomputes age from `dob`.
  - T3 calls `memory_store.most_recent_tagged(profile.id)` — reuses
    `MemoryStore`, no duplicated query logic.

**Verdict: PASS.** No deviation. Server-side, reuses existing bucket/age
logic, no duplication found.

---

## Scenario 6 — No pagination, correctly not built (§10.6)

**Checked:** `routes/chat_sessions.py` (full file).

- `GET /profiles/{profile_id}/chat_sessions` — `session_store
  .list_for_profile(profile_id)`, no query params beyond the path param
  and the `family`/store dependencies. `chat_sessions.py`'s
  `list_for_profile` SQL: `SELECT * FROM chat_sessions WHERE profile_id =
  ? ORDER BY last_message_at DESC` — no `LIMIT`/`OFFSET`.
- `GET /chat_sessions/{session_id}/messages` — `session_store
  .list_for_session(session_id)`, same shape, no pagination params.
  `list_for_session` SQL: `SELECT * FROM chat_messages WHERE session_id =
  ? ORDER BY created_at ASC` — no `LIMIT`/`OFFSET`.
- No cursor param, no `page`/`limit`/`offset` query param anywhere on
  either route signature.

**Verdict: PASS — confirmed as a deliberate, correctly-not-built scope
decision** (§10.6's own right-sizing call), not an accidental gap. Both
supporting indices (§10.1) are present, so the decision's own "cheap at
realistic single-family scale" premise holds structurally.

---

## Scenario 7 — Route-signature contract (`test_route_signatures.py`)

**Checked:** `dev/backend/tests/test_route_signatures.py` (full file).

- `EXPECTED_FAMILY_SEAM_ROUTES` (lines 47–70) includes all four
  Increment-5 routes, each with an inline comment attributing them to
  §10.8:
  - `("GET", "/profiles/{profile_id}/suggested_prompts")`
  - `("GET", "/profiles/{profile_id}/chat_sessions")`
  - `("GET", "/chat_sessions/{session_id}/messages")`
  - `("DELETE", "/chat_sessions/{session_id}")`
- Cross-checked each route's actual handler signature
  (`routes/profiles.py` line 201, `routes/chat_sessions.py` lines 57, 68,
  79) — all four declare `family: Family = Depends(get_current_family)`,
  matching the exact shape `test_family_parameter_annotation_and_kind_are
  _the_declared_shape` and `test_every_expected_route_carries_the_family
  _seam_with_the_exact_shape` assert.
- `("POST", "/chat")` was already present in the expected set from a
  prior increment and remains correct — `routes/chat.py`'s `chat()`
  handler still declares the same `family` parameter shape (line 77).
- Test logic itself (read in full): builds the actual seam-route set from
  live `app.routes` (not a hand-maintained mirror), asserts the missing
  set is empty, asserts the extra set is empty (symmetric check — catches
  both an under-declared and an over-declared route), and separately
  asserts parameter name/annotation/kind. This is exactly the kind of
  reflection-based check that would have caught a missed route on this
  increment; it did not need to catch one, because the diff correctly
  added all four.

**Verdict: PASS.** All four new routes are present in
`EXPECTED_FAMILY_SEAM_ROUTES` with the correct family-seam shape; the
test's own construction (live-route reflection, not a static mirror)
makes this a durable regression guard, not a one-time snapshot.

*(Note: this file confirms the test's construction and target-set
correctness by static reading, matching the mandate above. Whether the
current test process/CI run reports this test green is test-agent's
execution to log; nothing read here suggests it would fail — the shipped
route signatures match the expected set exactly.)*

---

## Overall verdict

**PASS — no blocking findings, no non-blocking findings.**

Every one of the seven checks in this mandate matches ARCHITECTURE_KB.md
§10 exactly:

1. Schema (§10.1) — exact match, including the deliberate plain-INTEGER-id
   departure from `photo_meta`'s uuid4 pattern (not an accidental
   reversion).
2. 4-hour boundary logic (§10.2) — config constant used correctly, exact
   three-condition OR comparison against `last_message_at`.
3. Snippet handling (§10.3) — write-once at session creation from
   `request.message`, structurally isolated from `enforce()`'s output by
   call order and by `make_snippet`'s single call site.
4. `/chat` contract (§10.4) — `new_session` genuinely optional/additive;
   response gains only `session_id`.
5. `/suggested_prompts` (§10.5) — genuinely server-side, reuses
   `ages.py`/`milestones.py`'s existing bucket logic, no duplicated
   age→bucket assignment.
6. No pagination (§10.6) — correctly absent on both new list routes, a
   right-sized decision, not a gap.
7. Route-signature contract (§10.9/test file) — all four new routes
   correctly added to `EXPECTED_FAMILY_SEAM_ROUTES` with the exact
   required shape.

**Gate verdict: solution-architect signs off on the architecture-suite
portion of the Test gate for Increment 5.** No items require code-agent
rework before this gate closes on architecture grounds.
