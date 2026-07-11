# Security suite — little-milestones, Increment 2 (F7: photo upload/storage/encryption)

Owner: security-architect. Gate: Test gate, Increment 2.
Reviewed against: `knowledge/SECURITY_KB.md` §2 (photo storage & encryption-at-rest design).

**Method note (stated explicitly, not glossed over):** this session's tool
grant did not include Bash/shell access — no live server start, no live
upload/decrypt/delete round-trip was possible from this agent directly. This
review is therefore static code-and-test review (full read of
`app/photos.py`, `app/photo_theme.py`, `app/routes/photos.py`, `app/main.py`,
`app/auth.py`, `app/db.py`, `.env`, `.env.example`, `.gitignore` at both repo
root and `backend/`, and `tests/test_photos.py`/`tests/conftest.py`), cross-
checked line-by-line against SECURITY_KB §2's design and against the actual
existing pytest suite's assertions (which do exercise the live FastAPI app
via `TestClient`, i.e. real request/response cycles against a real SQLite
file and real filesystem writes under `tmp_path`, even though I did not
independently execute `pytest` this run). Per the recorded pattern that
static-only review has missed real bugs live execution catches, this
limitation is flagged as a **process gap for this run specifically**, not
absorbed silently — see Finding S-7.

---

## Scenario: Fernet key sourced from `.env`, never hardcoded

- Input: `app/photos.py::_get_fernet()`
- Expected: key read from `os.environ["PHOTO_ENCRYPTION_KEY"]`, raises loudly
  if absent, never a literal/default key in source.
- Actual: `key = os.environ.get("PHOTO_ENCRYPTION_KEY")`; raises
  `RuntimeError` with a non-secret message if unset; no hardcoded fallback
  key anywhere in `photos.py`. `.env.example` documents the variable
  (empty value, with a generation command in a comment) and `.env` (dev
  machine's actual file, not committed — see secrets-leak scenario below)
  holds a real generated Fernet key.
- Result: PASS

## Scenario: per-photo IV/nonce handling

- Input: `fernet.encrypt(stripped)` call site in `PhotoStore.create()`.
- Expected: no manual IV management (Fernet's internal per-call IV is
  relied on, per SECURITY_KB §2.1), so no IV-reuse risk from custom code.
- Actual: confirmed — no manual IV/nonce code exists anywhere in
  `photos.py`; a single `Fernet(key).encrypt(...)` call per upload, which is
  exactly the primitive's intended per-call-fresh-IV usage. The `enc_iv`
  DB column is present but unused (schema comment in `db.py` explicitly
  documents this as intentional dead column, not a mistake).
- Result: PASS

## Scenario: delete ordering — file unlink before metadata row delete

- Input: `PhotoStore.delete()` (single-photo path) and
  `PhotoStore.delete_all_files_for_profile()` (profile-cascade path).
- Expected: `path.unlink()` executes before the `DELETE FROM photo_meta`
  statement, both in the single-photo and profile-cascade code paths
  (SECURITY_KB §2.4's crash-safety ordering).
- Actual: **single-photo path**, `photos.py:249-263` — `path.unlink()` at
  line 256, `DELETE FROM photo_meta` at line 259-262: correct order,
  confirmed by direct code reading (not merely "tests pass," which per the
  task brief could coincidentally hold even with the wrong order — the
  actual statement sequence in source was inspected). **Profile-cascade
  path**, `delete_all_files_for_profile()` (`photos.py:272-287`) iterates
  and unlinks every file, called from `routes/profiles.py`'s delete handler
  *before* the DB's `ON DELETE CASCADE` fires (per module docstring and
  `db.py`'s cascade-constraint design) — file-unlink code path is
  self-contained and has no DB-delete call inside it, consistent with
  "files first, then the caller triggers DB cascade separately."
- Result: PASS (source-order verified, not just outcome-tested)

## Scenario: no static file mount serving `data/photos/` directly

- Input: full read of `app/main.py` (the only place a `StaticFiles`/`.mount(...)`
  call could plausibly appear) and a grep-equivalent manual scan for
  `app.mount(` or `StaticFiles` anywhere in `app/main.py`, `app/routes/photos.py`.
- Expected: zero static mount of `backend/data/` anywhere; `GET /data/photos/...`
  or any raw-path bypass is unroutable (404).
- Actual: `app/main.py` contains no `app.mount(...)` call at all, and an
  explicit negative-space comment (lines 56-60) documents the invariant.
  `routes/photos.py`'s docstring makes the same claim. The existing test
  `test_no_static_mount_serves_photo_bytes` (tests/test_photos.py:123-129)
  asserts `GET /data/photos/` → 404 against the live `TestClient` app (a
  real FastAPI routing pass, not a mock) — this is a real execution-backed
  check even though I did not personally re-run pytest this session.
- Result: PASS, with the caveat that I did not independently execute this
  test this run — see Finding S-7.

## Scenario: `GET /profiles/{id}/photos/{pid}` enforces family scope

- Input: `routes/photos.py::get_photo()` → `_get_profile_or_404()` →
  `ProfileStore.get(family.id, profile_id)` (`app/profiles.py:118-123`,
  `WHERE id = ? AND family_id = ?`).
- Expected: cross-family photo request returns 404 (not 403, per SECURITY_KB
  §1.1's information-disclosure rule).
- Actual: the SQL is structurally family-scoped (a query with no matching
  `family_id` returns no row → `_get_profile_or_404` raises 404). This is
  the same "structurally impossible, not just checked" pattern
  `ProfileStore`'s own docstring claims (profiles.py:95-96) and it holds up
  on inspection. **However — no true cross-family test exists yet**, and
  cannot meaningfully exist yet: the Increment-1 auth seam
  (`app/auth.py::get_current_family`) always resolves to
  `DEFAULT_FAMILY_ID`, so every profile created in this run's test suite
  belongs to the same single family. This is the correct, expected state
  per SECURITY_KB §2.3 ("verified by PLAN §7-J34's post-Increment-3
  fixture... re-run as a regression at Increment 3's gate") — **not a
  Increment-2 gap**, since a second family literally cannot exist until
  Increment 3 activates real accounts. Flagged as a non-blocking carry-
  forward, not a finding against this increment.
- Result: PASS (structural review); cross-family behavior is
  untestable-in-practice until Increment 3, tracked, not a defect.

## Scenario: authorization on photo read/write given current auth seam

- Input: `routes/photos.py` — all three routes (`upload_photo`, `get_photo`,
  `delete_photo`) depend on `family: Family = Depends(get_current_family)`
  and pass `family.id` into every store call.
- Expected: `family_id` check on every route (present); `role=caregiver`
  restriction on delete (SECURITY_KB §2.3's "owner-only delete") — but only
  to the extent realistically enforceable given Increment-1's auth seam has
  no session/role concept exposed to any route yet.
- Actual: `family_id` scoping present on all three routes — PASS. **Role-
  based delete restriction (owner vs. caregiver) is genuinely absent from
  `delete_photo()`** — there is no role check at all. This is correctly
  **not a defect at this gate**: `get_current_family` (auth.py:54-67)
  returns only a bare `Family(id=...)`, with no user/role/session
  attached — there is no caregiver-vs-owner distinction anywhere in the
  request pipeline yet, by design (F10 activates in Increment 3). Building
  a role check now would have nothing real to check against (every request
  this run is, structurally, "the owner" — there is exactly one seeded
  family and no second user). Confirmed against SECURITY_KB §2.3's own text
  and the task brief's framing ("full multi-caregiver auth (F10) isn't
  activated until Increment 3 — check what's realistically enforceable
  now").
- Result: PASS as scoped to Increment 2; role-based 403 is a tracked
  Increment-3 requirement (SECURITY_KB §2.3, PLAN §7-J36), not a gap in
  this increment's shipped code.

## Scenario: EXIF/GPS stripping — JPEG/PNG/WEBP

- Input: `app/photos.py::_strip_exif()`; test
  `test_exif_gps_stripped_on_upload` (tests/test_photos.py:154-173) attaches
  a real EXIF `Make` tag to a JPEG, uploads, re-fetches, asserts
  `len(stored_exif) == 0`.
- Expected: EXIF (all of it, GPS included — SECURITY_KB/PLAN's "floor, not
  ceiling" framing) stripped on upload, before encryption.
- Actual: `_strip_exif()` re-opens the image via Pillow, does not pass
  `exif=` on save, and the function runs unconditionally in
  `PhotoStore.create()` before `fernet.encrypt(stripped)` — order is
  correct (strip, then encrypt, matching the docstring's stated pipeline
  order). The existing test exercises this via a real upload→fetch round
  trip against the live `TestClient`/real Pillow decode, which is a
  meaningfully strong check (it re-decodes the served bytes and inspects
  actual EXIF tag count, not just "file size changed" or similar weak
  proxy).
- Result: PASS (source + existing test logic both confirm), not
  independently re-executed this session (Finding S-7).

## Scenario: EXIF/GPS stripping — HEIC (new this increment)

- Input: `_strip_exif()`'s HEIC branch (`save_format = "HEIF"`), plus the
  explicit `image.info.pop("exif", None)` line and its accompanying comment
  explaining *why* this line exists specifically for HEIC (pillow-heif's
  HEIF plugin auto-propagates already-decoded EXIF into `image.info["exif"]`
  on re-save unless removed, unlike JPEG/PNG/WEBP's save path which only
  embeds EXIF if explicitly passed via `exif=`). Test
  `test_heic_exif_gps_stripped_on_upload` (tests/test_photos.py:189-210)
  synthesizes a real HEIC image with a real embedded EXIF `Make` tag via
  `pillow_heif`, uploads it, re-fetches, and asserts zero EXIF tags on the
  served bytes.
- Expected: HEIC's EXIF-carrying re-save behavior (flagged by code-agent as
  a subtle judgment call) is genuinely handled, not just claimed.
- Actual: **code correctly identifies and handles the exact subtlety
  flagged.** The `image.info.pop("exif", None)` call is the load-bearing
  line — without it, `image.save(out, format="HEIF")` would silently
  re-embed the EXIF block Pillow already decoded into `image.info`, even
  with no `exif=` kwarg passed (this is a genuine HEIF-plugin-specific
  behavior difference from JPEG/PNG/WEBP's save path, and the code comment
  at photos.py:99-103 states this accurately, referencing the specific test
  that verifies it). This is exactly the "subtle judgment call" the task
  brief warned about, and on inspection it is handled correctly, not just
  asserted to be.
- Result: PASS (source-level confirmation of the specific mechanism, plus
  an existing test that would fail if the `.pop("exif", None)` line were
  ever removed — a real regression guard, not a decorative comment).

## Scenario: `PHOTO_ENCRYPTION_KEY` present in `.env`/`.env.example`, same pattern as `ANTHROPIC_API_KEY`

- Input: `backend/.env.example`, `backend/.env` (dev machine's actual file).
- Expected: `.env.example` documents the variable (empty/placeholder);
  `.env` holds a real value; same file, same pattern as the existing
  `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` convention.
- Actual: `.env.example` (repo-tracked) has
  `PHOTO_ENCRYPTION_KEY=` (empty) with a generation-command comment, in the
  same file and same style as the existing LLM keys. `.env` (not repo-
  tracked, see next scenario) has a real generated Fernet key
  (`vNDAKrow2Z...`, truncated here deliberately — full value read during
  this review is not reproduced in this evidence file, consistent with
  "never logged/echoed" discipline extending to this report too).
- Result: PASS

## Scenario: secrets-leak check — `.env`/`data/` gitignored, no key/plaintext logging

- Input: repo-root `.gitignore` (`dev/.gitignore`), `backend/.gitignore`,
  `app/photos.py`'s logging call sites.
- Expected: `.env` (all variants) and `backend/data/` excluded from git;
  `photos.py` never logs key material or raw/plaintext photo bytes.
- Actual:
  - `dev/.gitignore` (repo root): `.env*` with `!.env.example` and
    `!backend/.env.example` exceptions — covers `backend/.env` (gitignore
    patterns apply repo-wide unless anchored, and this one is unanchored).
  - `backend/.gitignore`: `/data/` — covers `backend/data/` (photo bytes +
    SQLite file), anchored correctly to that directory per its own comment.
  - `photos.py` logging call sites (3 total, all `logger.warning`):
    `photo_orphaned_metadata profile_id=%s` (get_bytes, missing-file case),
    `photo_decrypt_failed profile_id=%s` (get_bytes, `InvalidToken` case),
    `photo_exif_strip_failed content_type=%s` (_strip_exif, decode-failure
    case). None of the three interpolates the encryption key, the raw
    photo bytes, or the on-disk file path — only `profile_id` (an integer,
    already exposed in the URL) and `content_type` (a MIME string) appear.
  - **Not independently verified this run**: actual `git ls-files`/`git
    status` output confirming `backend/.env` and `backend/data/` are not
    presently tracked in the repo's git index (no Bash access this
    session — see Finding S-7). Pattern-level review of the `.gitignore`
    files is complete and correct; the live git-index check itself is the
    part not independently executed.
- Result: PASS (pattern-level/code-level review); **the live git-tracking
  confirmation is an explicit follow-up item, not assumed** — see
  Finding S-7/S-8.

## Scenario: content-sniffing / size cap (cross-referenced, PLAN §7-G20)

- Input: `tests/test_photos.py::test_upload_disguised_exe_content_sniffed_415`,
  `test_upload_over_size_cap_413`.
- Expected: extension/claimed-content-type is never trusted; magic bytes
  gate acceptance; 10MB cap enforced.
- Actual: `sniff_content_type()` (photos.py:51-62) checks raw byte
  signatures only, ignoring the `filename`/claimed `content_type` form
  fields entirely (route layer never reads `file.content_type` for
  validation, only `file.read()`'s bytes) — the `.exe`-renamed-`.jpg` test
  case sends a fake `image/jpeg` claimed type with real MZ-header bytes and
  the route correctly 415s. Size cap checked before content-sniffing
  (`len(raw_bytes) > MAX_PHOTO_BYTES` at line 60, ahead of the sniff call)
  — correct order (cheap check first).
- Result: PASS

## Scenario: verified purge (`os.path.exists` post-delete)

- Input: `tests/test_photos.py::test_delete_purges_metadata_and_file_bytes`,
  `test_profile_delete_leaves_zero_photo_files`.
- Expected: single-photo delete and profile-cascade delete both leave zero
  file bytes on disk, not just zero metadata rows.
- Actual: both tests assert `os.path.exists(...)` / `profile_dir.exists()`
  is False post-delete, in addition to the metadata-row assertion. This
  matches SECURITY_KB §2.4's "verified purge, not just metadata pointer"
  standard.
- Result: PASS (existing test logic confirmed correct on inspection; not
  independently re-executed this session).

---

## Findings

### S-1 through S-6 (embedded above): no blocking defects found in the shipped F7 implementation

Fernet key sourcing, IV handling, delete ordering, no-static-mount,
family-scoped read, EXIF/GPS stripping (JPEG/PNG/WEBP and the new HEIC
path), `.env` pattern consistency, and logging hygiene all match
SECURITY_KB §2's design on direct source inspection. **Non-blocking.**

### S-7 (process finding, non-blocking but should be closed before sign-off): no live execution performed this session

This session's tool grant was Read/Write only — no Bash. Per the task
brief's own stated pattern ("static-only review has repeatedly missed real
bugs live execution catches"), this review could not independently: start
the backend, upload a live test image, confirm the on-disk file is not a
valid/openable image via an external tool invocation, or confirm a live
delete actually removes bytes from a running process's perspective. What
*was* done: full source read of every file in scope, plus reading (not
running) the existing `tests/test_photos.py` suite, which does perform
real `TestClient`-driven HTTP round trips against a real SQLite file and
real filesystem writes (`tmp_path`-scoped) when it *is* run — the suite
itself is well-constructed for exactly this kind of check (e.g.
`test_stored_file_is_not_plaintext_readable_image` directly reads the
on-disk bytes and asserts they don't start with the JPEG magic bytes).
**Recommendation: before this gate is signed off, test-agent (who does
have Bash) or a rerun of this suite with Bash access should confirm
`pytest tests/test_photos.py -v` actually passes end-to-end in this
environment** — this evidence file documents what static review found,
not a substitute for that live confirmation. Flagging this explicitly
rather than silently presenting static review as equivalent to live
verification.

### S-8 (non-blocking, tracked): git-index tracking status of `.env`/`data/` not independently confirmed this session

`.gitignore` pattern review (both `dev/.gitignore` and
`backend/.gitignore`) is correct and complete — the patterns *should*
exclude `backend/.env` and `backend/data/`. What was not independently run
this session is the live check (`git ls-files | grep -E '\.env$|^backend/data/'`
returning empty) that would confirm these files are not *currently*
tracked in the git index regardless of what `.gitignore` says (a file
already tracked before a `.gitignore` rule was added stays tracked until
explicitly `git rm --cached`). Recommend this specific check be run with
Bash access before final sign-off; it is a five-second check once available
and is called out here rather than assumed to be fine.

### S-9 (non-blocking, informational): role-based (owner vs. caregiver) delete restriction is correctly absent, not a defect

See "authorization on photo read/write" scenario above — confirmed
consistent with SECURITY_KB §2.3's own phasing and the task brief's
framing. Tracked forward to Increment 3 (PLAN §7-J36), not raised as a
gap against this increment.

### S-10 (non-blocking, informational): cross-family 404 behavior structurally correct but untestable-in-practice until Increment 3

See "family scope" scenario above. The SQL/query shape is correct and
matches `ProfileStore`'s existing family-scoping pattern exactly; a live
two-family fixture cannot exist until Increment 3's auth activates. Tracked
forward per SECURITY_KB §2.3 and PLAN §7-J34, not a gap in this increment.

### S-11 (non-blocking, informational): test fixtures rely on the developer's real `.env` for `PHOTO_ENCRYPTION_KEY`

`tests/conftest.py` sets no `PHOTO_ENCRYPTION_KEY` override — the test
suite relies on `app.main`'s `load_dotenv()` picking up the real
`backend/.env` file's key at import time. This works on this developer's
machine but is a portability/CI gap (a fresh clone/CI runner without a
populated `.env` would fail every photo test with the `_get_fernet()`
`RuntimeError`, not a security defect but worth flagging as a test-
infrastructure robustness item for test-agent/code-agent, not this role's
suite to fix).

---

## Gate verdict

**Security suite: PASS, conditional on S-7 and S-8 being closed with a live
run before final human sign-off of the Test gate.**

No blocking security defect was found in the shipped F7 implementation
against SECURITY_KB §2's design — encryption, key sourcing, delete
ordering, private-by-default access, family scoping (to the extent
enforceable pre-Increment-3), and EXIF/GPS stripping (including the new
HEIC path) all check out on direct source and existing-test inspection.
The two open items (S-7, S-8) are process/verification gaps in *this
review*, not defects found *in the code* — they should be closed by
re-running this suite (or at minimum `pytest tests/test_photos.py -v` plus
a `git ls-files` check for `.env`/`data/`) with Bash access before treating
this gate as fully closed, per this session's own recorded pattern that
live execution catches things static review does not. Recommend: hand this
evidence file to test-agent (or re-invoke this role with Bash access) to
perform that final live confirmation pass; do not block Increment 2 on
re-review of the *design*, only on the *live-execution confirmation* being
completed.
