# Security Test Evidence — Increment 5 (F13: chat history, shared per-profile)

Date: 2026-07-12
Owner: security-architect
Scope: verify shipped code in `dev/backend/app/routes/chat_sessions.py`,
`dev/backend/app/chat_sessions.py`, and `dev/backend/app/routes/chat.py`
against the design confirmed at the Architecture gate
(`knowledge/ARCHITECTURE_KB.md` §10.8, "security-architect confirmed"
block, 2026-07-12).

**Method note:** no Bash/shell tool was available in this session (only
Read/Write). Verification below is static code review of the shipped
route/store implementations, cross-checked against the existing automated
test suite (`dev/backend/tests/test_chat_sessions.py`), rather than a live
curl/browser session against the running :8000 backend as originally
requested. This is flagged as a methodology deviation, not silently
substituted — see gate verdict note at the end.

---

## Scenario 1 — Family-scoping on all three new routes

**Route:** `GET /profiles/{profile_id}/chat_sessions`
- Code: `_get_profile_or_404(profile_store, family, profile_id)` called
  before `session_store.list_for_profile(profile_id)`
  (`chat_sessions.py:61-62`). `ProfileStore.get(family.id, profile_id)`
  is family-scoped at the query level (per `MemoryStore`/`PhotoStore`
  precedent) — an out-of-family profile id resolves to `None` →
  404 "Profile not found," never a filtered/empty 200.
- Test corroboration: `test_chat_sessions_list_route_cross_family_404`
  (signup family A, create profile+session, logout, signup family B,
  GET as family B → asserts 404). **PASS.**

**Route:** `GET /chat_sessions/{session_id}/messages`
- Code: `_get_family_session_or_404(session_store, profile_store, family,
  session_id)` (`chat_sessions.py:72`), which:
  1. `session_store.get(session_id)` — **unscoped** lookup by id only
     (`chat_sessions.py:107-114`, docstring explicitly notes this is
     intentional: "callers use this to discover a session's profile_id
     before confirming family scope").
  2. If `None` → 404 "Conversation not found."
  3. Otherwise `_get_profile_or_404(profile_store, family,
     session.profile_id)` — family-scoped check on the *resolved*
     profile_id, same 404 path as scenario above if it fails.
  This is exactly the "resolve session first, then check owning
  family" order the task asked me to confirm, and it is implemented
  in a single shared helper (`_get_family_session_or_404`) used by both
  session-id-only routes, not duplicated/drifted logic.
- **Indistinguishability check:** an unknown session_id (step 2 fails)
  and a real session belonging to another family (step 3 fails) both
  raise `HTTPException(404, ...)` — same status code. Detail strings
  differ ("Conversation not found" vs. "Profile not found"), which is a
  very minor residual signal (a determined attacker could in principle
  distinguish "session doesn't exist" from "session exists but isn't
  mine" by response body, not status code). **Non-blocking finding** —
  flagged below.
- Test corroboration: `test_chat_session_messages_route_cross_family_404`
  and `test_list_messages_for_unknown_session_404` both assert plain
  `404` status. **PASS** on status-code indistinguishability (the
  contract the architecture doc actually specifies — "cross-family is a
  404, never a 403" — is satisfied); body-text distinguishability is the
  separate non-blocking note above.

**Route:** `DELETE /chat_sessions/{session_id}`
- Same `_get_family_session_or_404` call before `session_store.delete(...)`
  (`chat_sessions.py:86-87`). Same resolve-then-check order, same 404
  behavior.
- Test corroboration: `test_chat_session_delete_route_cross_family_404`
  — asserts 404 on cross-family delete attempt, **and** explicitly
  re-authenticates as the owning family afterward to confirm the row was
  **not actually deleted** despite the attempt (`still_there` assertion,
  lines 253-258 of the test file). This is exactly the check I would
  have designed myself (a 404 that still silently deleted the row would
  be a worse bug than a 403). **PASS.**
- `test_delete_unknown_session_404` confirms unknown-id delete is also a
  plain 404. **PASS.**

**Verdict, scenario 1: PASS**, with one non-blocking cosmetic finding
(detail-string difference between "not found" and "not yours," see
Findings below).

---

## Scenario 2 — Delete permission is any-caregiver, not owner-only

- Route decorator: `@router.delete("/chat_sessions/{session_id}")` on
  `delete_chat_session` (`chat_sessions.py:76-90`). Its dependency list
  is `family: Family = Depends(get_current_family)`,
  `profile_store: ProfileStore = Depends(_profile_store)`,
  `session_store: ChatSessionStore = Depends(_session_store)` — **no**
  `require_owner` dependency anywhere, unlike e.g. profile/invite-create
  routes which explicitly add `Depends(require_owner)`
  (`routes/auth.py:221`, `SessionUser = Depends(require_owner)`).
- An inline comment at the route confirms this is deliberate, not an
  omission: "ARCHITECTURE_KB §10.8: any caregiver on the family may
  delete a conversation — deliberately no `require_owner` dependency
  here, unlike profile/photo delete" (`chat_sessions.py:83-85`).
- `ChatSessionStore.delete()` itself performs no role check either
  (`chat_sessions.py:193-200`, plain `DELETE FROM chat_sessions WHERE id
  = ?` after the route-layer family-scope check already ran) — consistent
  with the architecture's stated split (authz is a route-layer concern,
  store layer trusts the caller).
- Test corroboration:
  `test_caregiver_can_delete_chat_session_not_owner_only` — creates an
  owner, an invited (non-owner) caregiver via `/auth/join`, logs in as
  the caregiver, and asserts `DELETE /chat_sessions/{id}` returns `200`
  (not `403`) for that non-owner role. **PASS**, matches the confirmed
  design exactly (severity tier = memory-delete, not profile/photo-delete).

**Verdict, scenario 2: PASS.**

---

## Scenario 3 — `/chat`'s persistence side-effect doesn't leak data

- `routes/chat.py:81-83`: `profile = store.get(family.id,
  request.profile_id)`; `if profile is None: raise HTTPException(404,
  ...)`. This is the same family-scoped `ProfileStore.get` used
  everywhere else — `request.profile_id` is validated against the
  authenticated caller's `family.id` before any other logic in the
  handler runs.
- Every downstream use of a profile id in this handler uses `profile.id`
  (the object returned by the validated `store.get(...)` call), never
  `request.profile_id` directly again:
  - `ages = compute_age(profile.date_of_birth, ...)` — uses `profile.*`.
  - `system_prompt = build_system_prompt(profile, ages, bucket)` — uses
    `profile`.
  - `safe_text = enforce(raw_text, profile_id=profile.id)` — uses
    `profile.id`.
  - `log_stale_age(raw_text, profile_id=profile.id)` — uses `profile.id`.
  - `session_id, _created = session_store.resolve_or_create_session(
    profile.id, first_message_if_new=request.message,
    force_new=request.new_session)` — the new Increment-5 call, uses
    `profile.id`, **not** `request.profile_id`.
  - `session_store.record_turn(session_id, request.message, safe_text)`
    — `session_id` was just derived from `profile.id` above.
- There is no code path in this handler where a session could be
  created/written against a `profile_id` that bypassed the initial
  `store.get(family.id, request.profile_id)` check — the variable
  `request.profile_id` (unvalidated, caller-supplied) is read exactly
  once, only as an argument to that validating lookup, and never reused
  afterward. **PASS**, confirms the design note in `ARCHITECTURE_KB`
  §10.3 was checked "against the actual code, not just the spec" (same
  discipline applied here for the family-scoping angle).

**Verdict, scenario 3: PASS.**

---

## Scenario 4 — No new secrets/logging concerns

- `chat_sessions.py` (route file and store module) contains **zero**
  `logger`/`print`/`logging` calls of any kind — no message content, no
  profile ids, nothing. Confirmed by full read of both files.
- `guardrails.py`'s two logging call sites (`enforce()` and
  `log_stale_age()`, pre-existing from Increment 1/2, not new this
  increment) log only `category`/`matched` (a short regex-match
  fragment, e.g. "percentile" or "12 months") plus `profile_id` — never
  the full `text`/`raw_text`/`safe_text`. This matches the module's own
  documented discipline ("no PII beyond a profile id and violation
  category," `guardrails.py:13-14`) and was not altered by Increment 5's
  changes to `chat.py` (the two guardrail call sites in `chat.py` are
  unchanged calls into the same pre-existing functions).
- No new secret/API-key surface is introduced by this increment (no new
  third-party service, no new `.env` variable). `dev/.gitignore` (root of
  the dev repo) excludes `.env*` while allowing `.env.example`/
  `backend/.env.example` — confirmed by direct read, consistent with the
  pattern already verified for `RESEND_API_KEY`/`PHOTO_ENCRYPTION_KEY` at
  prior gates (SECURITY_KB §2.5).
- `chat_messages.content` (the actual chat text) is written to SQLite via
  parameterized queries only (`?` placeholders in both `INSERT`
  statements, `chat_sessions.py:179-184`) — no string interpolation into
  SQL, no injection surface.

**Verdict, scenario 4: PASS.**

---

## Findings

**Non-blocking:**
1. `_get_family_session_or_404`'s two failure branches return different
   `detail` strings ("Conversation not found" for unknown id vs. "Profile
   not found" for cross-family, inherited from `_get_profile_or_404`).
   Both are `404` status codes (the load-bearing contract per
   ARCHITECTURE_KB §10.8 and PLAN §7-J36's owner/cross-family distinction
   is satisfied), so this is not a status-code oracle. It is a
   very-low-value response-*body* oracle (an attacker who already knows a
   valid-looking session id format could distinguish "doesn't exist" from
   "exists, not yours" by reading the detail string). Recommend
   normalizing both branches to a single generic detail string (e.g.
   "Conversation not found") for defense-in-depth, but this does not rise
   to a gate-blocking issue given: (a) session ids are plain sequential
   integers already acknowledged as non-enumerable-sensitive in
   ARCHITECTURE_KB §10.1 ("neither chat_sessions.id nor chat_messages.id
   is ever exposed as a filename or otherwise reachable outside an
   authenticated, family-scoped route"), and (b) the caller must already
   be authenticated to reach either branch at all, so this is at most an
   information-disclosure refinement within an already-authenticated
   session, not a pre-auth enumeration vector.

**Blocking:** none found.

---

## Methodology deviation note

The task requested a live check (login, create a session via `/chat`,
attempt cross-family access, confirm 404) using the orchestrator's
running backend on :8000. This session had no Bash/shell tool available
(only Read/Write), so no live HTTP requests were made. In its place, this
review relies on (a) full static read of every code path in scope, and
(b) the pre-existing automated test suite
(`dev/backend/tests/test_chat_sessions.py`), which already implements
the exact live-check scenarios requested (signup family A → create
session → logout → signup family B → attempt access → assert 404, for
all three routes, plus a "confirm not actually deleted" check on the
delete route) as executable pytest cases. I read those tests in full and
they exercise the real FastAPI app via `TestClient` against a real SQLite
test DB — this is a materially strong substitute for a manual curl
session (same code paths, same DB engine, actually executed rather than
hypothesized), but it is not the same as an independent live run I
personally triggered and observed this session. If the orchestrator can
supply Bash access, I recommend re-running `pytest
tests/test_chat_sessions.py -v` live and pasting the pass/fail output
into this file as a follow-up; I have not been able to execute pytest
myself this session either.

---

## Gate verdict

**PASS — no blocking findings.** All four scenarios (family-scoping with
resolve-then-check ordering, any-caregiver delete permission, `/chat`
persistence-side-effect isolation, no new secrets/logging concerns) are
satisfied by the shipped code and corroborated by an existing, relevant
automated test suite. One non-blocking, low-severity finding (detail-
string distinguishability between "unknown session" and "not your
session") is recorded above for optional future hardening, not a gate
blocker. The implementation matches the design confirmed at the
Architecture gate (§10.8) exactly, including the specific ordering
requirement (resolve session by unscoped id first, then check family)
that was the main point of this verification pass.

Recommend: re-run the live-check portion with actual shell access when
available, purely as an additional independent confirmation layer — not
a condition for this gate to pass, given the strength of the existing
static+test-suite evidence.

## Orchestrator follow-up: live cross-family + delete-permission check (closes this evidence file's methodology caveat)

Executed directly against the running backend (localhost:8000), real sessions:
1. Family A (tester) created a chat session via `/chat` (session_id=1).
2. Family B (fresh signup) attempted `GET /chat_sessions/1/messages` → 404.
3. Family B attempted `DELETE /chat_sessions/1` → 404, and Family A confirmed
   the session (2 messages) still existed afterward -- the failed cross-family
   delete attempt had zero effect.
4. A second caregiver invited into Family A (role: "caregiver", not owner)
   successfully deleted session_id=1 → 200. Confirmed gone (404 on subsequent
   fetch) -- the any-caregiver-can-delete design works exactly as specified,
   live, not just in the test suite.

**Live-confirmed: PASS.** Closes this evidence file's one methodology caveat
(no Bash access in that session).
