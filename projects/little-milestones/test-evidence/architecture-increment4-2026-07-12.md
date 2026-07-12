# Architecture test-suite evidence — Increment 4 (F14/F15/F16)

Owner: solution-architect. Test gate, 2026-07-12. Scope: verify the shipped
Increment-4 code matches `knowledge/ARCHITECTURE_KB.md` §9.3's
`avatar_photo_id` / replace-not-accumulate design exactly — a design this
role authored and is now independently re-verifying against the shipped
code (not re-reading the Code-gate summary as sufficient evidence).

Reviewed directly, by reading source: `dev/backend/app/{db.py, profiles.py,
photos.py, routes/profiles.py, routes/photos.py, main.py}`,
`dev/backend/tests/{test_photos.py, test_profiles.py,
test_route_signatures.py}`.

---

## Scenario 1 — `avatar_photo_id` is a derived field, not a stored column

**Check:** `db.py`'s `profiles` table schema must not carry a new
`avatar_photo_id` column.

**Evidence:** `db.py` SCHEMA block, `profiles` table (lines 67–78): columns
are `id, family_id, display_name, dob, born_early, weeks_early,
photo_accent_mid, photo_accent_deep, photo_accent_tint, created_at`. No
`avatar_photo_id` column. `profiles.py`'s `Profile` model carries
`avatar_photo_id: Optional[str] = None` as a Pydantic field with an explicit
comment ("derived, not a stored column ... populated by the route layer,
same pattern as `age_summary`"), and `_row_to_profile()` never sets it from
a row — it's left at the Pydantic default and only overwritten by
`routes/profiles.py::_with_avatar_photo_id()`, which runs a live `SELECT id
FROM photo_meta WHERE profile_id = ? AND memory_id IS NULL ORDER BY
created_at DESC LIMIT 1` query and `model_copy(update=...)`s it in, applied
on create/list/get (lines 76, 86, 100 of `routes/profiles.py`).

**Verdict: PASS** — matches §9.3 exactly, same pattern as `age_summary`.

---

## Scenario 2 — `photo_meta(profile_id, memory_id, created_at)` index exists

**Check:** `schema.sql`/`db.py` must define the index §9.3 calls for, to
back both the `avatar_photo_id` lookup and the replace-cleanup query.

**Evidence:** `db.py` lines 116–122:
```sql
CREATE INDEX IF NOT EXISTS idx_photo_meta_profile_memory_created
    ON photo_meta (profile_id, memory_id, created_at);
```
Idempotent (`IF NOT EXISTS`), applied on every `init_db()` call including
against pre-existing DBs (no separate migration step needed, consistent
with §3's "create tables/indexes if absent" posture). Comment explicitly
ties it to both consuming queries.

**Verdict: PASS**

---

## Scenario 3 — `PhotoStore.create()` replace-not-accumulate: scope, order, isolation

**Check 3a — scoped only to `memory_id IS NULL`, memory-attached photos
unaffected (verified by reading code, not assuming from test names).**

**Evidence:** `photos.py::create()` line 192: `if memory_id is None:
self._replace_prior_profile_level_photos(...)` — the cleanup helper is
called conditionally, only when the *new* upload itself has no
`memory_id`. Inside `_replace_prior_profile_level_photos()` (lines 208–245),
the `SELECT` that finds rows to delete is itself filtered
`WHERE profile_id = ? AND memory_id IS NULL AND id != ?` — so even among a
profile's own photos, only other `memory_id IS NULL` rows are candidates;
a memory-attached row for the same profile can never be selected regardless
of upload order. Confirmed independently via
`test_photos.py::test_memory_attached_photos_unaffected_by_avatar_replacement`,
which asserts (not just names) that the memory-attached row/file survive
two subsequent avatar uploads — read the assertions directly (lines
308–313), not just the test's pass/fail status.

**Check 3b — exact sequence: create new → cleanup old (bypassing
`delete()`) → `_set_profile_accent` from new tokens.**

**Evidence, read in execution order from `photos.py::create()`:**
1. Lines 169–190: strip EXIF, encrypt, write file, `INSERT` the new
   `photo_meta` row, commit.
2. Lines 192–193: **only if `memory_id is None`**, call
   `_replace_prior_profile_level_photos(profile_id, photo_id)` — this
   unlinks old files and `DELETE`s old rows directly via raw SQL
   (`self._conn.execute("DELETE FROM photo_meta WHERE id = ? AND
   profile_id = ? AND memory_id IS NULL", ...)`, lines 241–244), **not**
   via the public `delete()` method. Confirmed `delete()` (lines 293–314)
   is never called from this path — no `self.delete(...)` call anywhere
   in `create()` or its helper.
3. Lines 195–202: **after** step 2 completes, `extract_accent(stripped)`
   runs and `self._set_profile_accent(profile_id, tokens)` is called with
   the **new** photo's tokens — this is the last accent-touching call in
   the method.

This is exactly the order §9.3 specifies, and exactly avoids the bug it
was designed around: `delete()`'s own body unconditionally calls
`_set_profile_accent(profile_id, None)` (line 312) — had cleanup gone
through `delete()` and run *after* the new accent was set, or had the
accent-set line been ahead of cleanup instead of after it, the new photo's
accent would have been silently wiped. The shipped order (new accent-set
is the last write) makes that impossible.

**Check 3c — cross-profile isolation (security-architect condition 1).**

**Evidence:** the cleanup `SELECT`/`DELETE` both explicitly filter
`profile_id = ?` (lines 232–234, 241–244), not merely implied by which
`PhotoStore` instance/connection is in scope. Confirmed by
`test_photos.py::test_avatar_replacement_is_cross_profile_isolated`
(lines 316–348), which reads back both the DB row and the on-disk file for
profile A after two avatar uploads to profile B, and asserts both are
untouched.

**Check 3d — authz-bypass comment (security-architect condition 2).**

**Evidence:** `_replace_prior_profile_level_photos()`'s docstring (lines
208–231) explicitly states the method bypasses `delete()`'s owner-only
authz check and explains why that's safe (runs only inside `create()`'s
already-authorized upload request, never independently reachable). Present
and substantive, not a one-liner stub.

**Check 3e — regression test: two uploads leave exactly one row/file
(security-architect condition 3).**

**Evidence:**
`test_photos.py::test_repeated_profile_level_upload_replaces_not_accumulates`
(lines 251–280) asserts both the DB row set (`[second_id]` exactly) and the
filesystem state (`first_path` gone, `second_path` exists) after two
sequential avatar uploads.

**Verdict: PASS on all five sub-checks (3a–3e).**

---

## Scenario 4 — no incidental contract change elsewhere; route-signature test scope

**Check:** every other route/store method touching `Profile` keeps its
existing signature; does `test_route_signatures.py` need a new case for
`avatar_photo_id`?

**Evidence:** `routes/profiles.py`'s four route handlers
(`create_profile`, `list_profiles`, `get_profile`, `delete_profile`) were
read in full — parameter lists, types, and `Depends(...)` wiring are
unchanged from the pre-Increment-4 shape already covered by
`test_route_signatures.py`'s `EXPECTED_FAMILY_SEAM_ROUTES` set (all four
routes' paths/methods already appear in that set: `POST /profiles`, `GET
/profiles`, `GET /profiles/{profile_id}`, `DELETE /profiles/{profile_id}`).
The only change made was adding a helper function
(`_with_avatar_photo_id`) and threading `conn` through two more route
bodies as a local call, not a new/changed route parameter — `family:
Family = Depends(get_current_family)` is untouched on every route.
`ProfileStore`'s public methods (`create/get/list_for_family/delete`) are
also unchanged (read `profiles.py` in full — no method signature edited
this increment).

`test_route_signatures.py` is scoped explicitly (per its own docstring) to
the family-seam parameter shape (`family: Family = Depends
(get_current_family)`), not to response-model field sets — `Profile`
gaining a field is a response-shape change, outside this test's stated
contract. **Out of scope for `test_route_signatures.py` as currently
designed; no new case needed there.** The correct place for
`avatar_photo_id`'s contract *is* covered — by
`test_profiles.py::test_avatar_photo_id_null_until_profile_level_upload`
and `test_avatar_photo_id_ignores_memory_attached_photos`, both read in
full and confirmed to assert the field's presence/value across
create/get/list, which is the field-level contract that matters here.

**Verdict: PASS** — no incidental signature drift found; the
route-signature contract test's scope is correctly unchanged (a genuine
scope boundary, not a gap).

---

## Scenario 5 — F15/F16 zero new backend surface

**Check:** F15 (lightbox) and F16 (gallery) are frontend-only; no new
routes/endpoints, no new route file.

**Evidence:** `main.py`'s router mount list (lines 77–83) is unchanged:
`profiles, chat, memories, photos, digest, products, auth` — the same
seven routers as end of Increment 3, no eighth added. `routes/photos.py`
(read in full, 108 lines) has exactly the same three endpoints as before
Increment 4 (`POST /profiles/{id}/photos`, `GET
/profiles/{id}/photos/{photo_id}`, `DELETE
/profiles/{id}/photos/{photo_id}`) — no new route added to this file
either. F16's gallery view reuses the already-existing `getTimeline()`
response client-side (per the Increment-4 implementation summary in
`PROJECT_CONTEXT.md`, cross-checked against the fact that no new
`GET`-returning route exists anywhere in the backend for gallery data) —
consistent with "no new API call" as designed. No new backend file
(`routes/lightbox.py`, `routes/gallery.py`, or similar) exists.

**Verdict: PASS** — F15/F16 shipped as designed, zero new backend surface.

---

## Overall gate verdict

**PASS — no blocking findings.**

All five scenarios verified directly against shipped source (not inferred
from the Code-gate summary or test pass/fail status alone). The
`avatar_photo_id` derived-field design, the `photo_meta` index, and the
replace-not-accumulate sequence in `PhotoStore.create()` all match
ARCHITECTURE_KB §9.3 exactly, including all three security-architect
conditions (explicit `profile_id` filter, documented authz-bypass comment,
and the three regression tests). No incidental contract drift found on any
other route/store method. F15/F16 confirmed as designed: zero new backend
surface, frontend-only.

**Non-blocking notes (not findings against this design, informational
only):**
- `test_route_signatures.py`'s scope (family-seam shape only, not
  response-field contracts) means a future field addition to `Profile`
  would similarly not be caught by it — this is a correct, narrow scope
  for that test, not a gap this increment introduced, but worth naming so
  a future reviewer doesn't assume that test is a general response-schema
  guard.
- PROJECT_CONTEXT.md's Increment-4 judgment call 4 notes the live `:8000`
  dev process was not restarted this session — a Deploy-gate concern, not
  an architecture-conformance one; noted here only so it isn't lost between
  gates.
