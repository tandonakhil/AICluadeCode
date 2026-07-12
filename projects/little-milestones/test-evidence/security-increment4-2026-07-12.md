# Security test-gate evidence — Increment 4 (F14/F15/F16)

**Scope:** verifying the *shipped* code for ARCHITECTURE_KB §9.3's avatar-replace
design satisfies all 3 security-architect conditions set earlier this session,
plus a fresh check that the new Settings upload entry point didn't introduce an
under-scoped/unauthenticated path.

**Method note:** no Bash/shell tool was available to this agent this session
(Read/Write only). Live curl verification (login, double profile-photo upload,
assert exactly one `memory_id IS NULL` row survives) was **not** performed
directly by security-architect, deviating from this session's established
live-check pattern. In its place: (a) direct static read of the shipped
`photos.py`/`routes/photos.py`/`SettingsScreen.tsx`/`lib/api.ts`, and (b) full
reading of the actual test *bodies* (not names) in `test_photos.py`, which
already exercise the equivalent flow end-to-end through `TestClient` — real
HTTP requests, real SQLite rows, real filesystem paths, no mocking of the
create/cleanup path. This is treated as strong evidence but not a substitute
for an independent live run; flagged for the orchestrator to run the curl
check directly if a stronger guarantee is wanted before ship.

---

## Condition 1 — explicit `profile_id` filter in cleanup query

**Status: SATISFIED.**

`dev/backend/app/photos.py`, `PhotoStore._replace_prior_profile_level_photos`:

```python
rows = self._conn.execute(
    "SELECT id FROM photo_meta WHERE profile_id = ? AND memory_id IS NULL AND id != ?",
    (profile_id, new_id),
).fetchall()
for row in rows:
    old_id = row["id"]
    path = _photo_path(profile_id, old_id)
    if path.exists():
        path.unlink()  # files first (SECURITY_KB §2.4)
    self._conn.execute(
        "DELETE FROM photo_meta WHERE id = ? AND profile_id = ? AND memory_id IS NULL",
        (old_id, profile_id),
    )
```

Both the `SELECT` and the `DELETE` filter on `profile_id = ?` explicitly, not
just implicitly via which `PhotoStore`/connection instance is in scope — the
`DELETE` is doubly defensive (filters again on `profile_id` and `memory_id IS
NULL` even though `old_id` came from an already-filtered `SELECT`). Matches
the condition exactly.

## Condition 2 — authz-bypass comment

**Status: SATISFIED.**

Docstring on the same method, `photos.py` lines 216–226:

```python
"""... This also means it bypasses `delete()`'s owner-only authz check
(security-architect's condition 2, ARCHITECTURE_KB §9.3) -- safe
here because it runs only inside `create()`'s own already-authorized
upload request, never as an independently reachable operation.
```

This is a docstring block rather than a strict "one-line" `#` comment, but it
is unambiguous, explicitly names the bypass, names the reason it's safe, and
cross-references the condition and the architecture section — satisfies the
intent (a future reader cannot mistake this for an oversight) more thoroughly
than a bare one-liner would. Not flagging the form difference as a gap.

## Condition 3 — regression tests exist and are real

**Status: SATISFIED.** Read actual test bodies in
`dev/backend/tests/test_photos.py`, not just names.

**(a) Repeat-upload replaces correctly** —
`test_repeated_profile_level_upload_replaces_not_accumulates` (lines 251–280):
uploads twice, then directly queries
`SELECT id FROM photo_meta WHERE profile_id = ? AND memory_id IS NULL` and
asserts the result list equals `[second_id]` exactly (not just "not empty" —
a real one-row assertion). Also asserts `first_path.exists()` is `False` and
`_photo_path(profile_id, second_id).exists()` is `True` — both DB and
filesystem checked, matching the condition's own wording.

A companion test, `test_memory_attached_photos_unaffected_by_avatar_replacement`
(lines 283–313), confirms the cleanup is correctly scoped to `memory_id IS
NULL` only — a memory-attached photo survives two avatar uploads untouched,
row and file both asserted present.

**(b) Cross-profile isolation** —
`test_avatar_replacement_is_cross_profile_isolated` (lines 316–348): creates
profile A and profile B, uploads once to A, then twice to B (same connection/
store instance, deliberately, per its own docstring), then asserts profile
A's row (`row_a`) still exists with `row_a["profile_id"] == profile_a`, its
file still exists on disk, and a direct
`SELECT id FROM photo_meta WHERE profile_id = ? AND memory_id IS NULL`
scoped to profile A returns exactly `[photo_a_id]` — i.e., B's repeated
uploads provably never touched A's row. This is a real assertion against DB
state, not a name-only smoke test.

## Route/frontend fresh check — no new unauthenticated/under-scoped path

**Status: SATISFIED, no new surface introduced.**

- `dev/backend/app/routes/photos.py`'s `upload_photo` route is unchanged by
  this increment: `family: Family = Depends(get_current_family)` (session-
  authenticated, same seam as every other route) plus
  `_get_profile_or_404(profile_store, family, profile_id)` (family-scoped
  existence check, 404 on cross-family access) both still gate every upload,
  regardless of whether `memory_id` is supplied. `memory_id` is an optional
  form field on the *same* route/handler — there is no second route or
  branch for profile-level vs. memory-attached uploads.
- `dev/frontend/components/SettingsScreen.tsx`'s `handlePhotoSelected` calls
  `uploadPhoto(profile.id, file)` — the *same* `uploadPhoto()` function in
  `dev/frontend/lib/api.ts` already used by `AddMemoryForm.tsx` for
  memory-attached uploads, just omitting the optional `memoryId` argument.
  `uploadPhoto()` itself is a single implementation: `credentials: "include"`
  (sends the session cookie), `POST {API_BASE}/profiles/{profileId}/photos`
  — identical origin/auth handling as every other authenticated fetch in
  this app (`request()`'s own `credentials: "include"` pattern, applied
  manually here since this is a `FormData` call, not JSON).
- No new route, no new fetch wrapper, no bypass of `get_current_family` was
  introduced for this UI entry point. The Settings "Add/Change photo"
  affordance is a new *caller* of an existing, already-scoped code path, not
  a new path.

---

## Findings

**Blocking: none.**

**Non-blocking:**
1. Condition 2's comment ships as a multi-line docstring block rather than
   literally "a one-line code comment" as the condition's wording specified.
   The content fully satisfies the intent (explicit, unambiguous, cross-
   referenced) — recorded as a form deviation, not a defect.
2. Live curl-based verification (this session's established pattern) was not
   performed directly by security-architect due to no Bash/shell tool being
   available in this invocation. Static review + full reading of real,
   passing `TestClient`-based test bodies (real HTTP requests, real DB rows,
   real filesystem paths) is treated as strong substitute evidence, but is
   not equivalent to an independent live run. Recommend the orchestrator (or
   a tool-enabled follow-up pass) run: login → `POST
   /profiles/{id}/photos` twice with the tester account on the live `:8000`
   backend → confirm exactly one `memory_id IS NULL` row/file remains — before
   treating this increment as fully closed at Test gate, even though nothing
   in the static/test-body review suggests it would fail.

## Verdict

**PASS — gate condition satisfied, no blocking findings.**

All three security-architect conditions from ARCHITECTURE_KB §9.3 are
verified in the shipped code, not merely in the design: explicit
`profile_id` filtering, an explicit authz-bypass rationale comment, and real
(not name-only) regression tests covering both repeat-upload replacement and
cross-profile isolation, checking both DB and filesystem state. The new
Settings-triggered upload path is confirmed to reuse the existing family-
scoped, session-authenticated route and shared frontend upload function —
no new unauthenticated or under-scoped surface was introduced for F14.

Recommend closing this increment's security suite conditional only on the
non-blocking live-verification follow-up above, which is a confidence-
raising nice-to-have, not a gate blocker given the strength of the existing
static + real-test-body evidence.

## Orchestrator follow-up: live double-upload check (closes this evidence file's methodology caveat)

Executed directly against the running backend (localhost:8000, real
session, real profile id=6):
1. Uploaded a real JPEG with no `memory_id` → photo id `58610b9c...` created.
2. Uploaded a second real JPEG with no `memory_id` → photo id `60e811b0...` created.
3. `SELECT id FROM photo_meta WHERE profile_id=6 AND memory_id IS NULL` →
   returns exactly one row: `60e811b0...` (the new one). `58610b9c...` is gone.
4. Filesystem check on `data/photos/6/`: `58610b9c...` — 0 matches (file
   genuinely unlinked); `60e811b0...` — 1 match (file present).

**Live-confirmed: PASS.** The replace-not-accumulate fix works exactly as
designed under a real double-upload, closing this evidence file's one
methodology caveat (no Bash access in that session).
