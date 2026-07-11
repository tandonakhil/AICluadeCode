# Test Evidence — unit/integration suite — little-milestones — Increment 2 (F6 memory/timeline, F7 photos, F8 digest content)

Run date: 2026-07-11. Suite: `pytest` (dev/backend/tests/), test-agent (blocking
per default policy — no advisory suites recorded for this project).
Environment: `dev/backend/.venv` (Python 3.9.6, pytest 8.4.2, pillow-heif
1.1.1). No `ANTHROPIC_API_KEY` set — no live-LLM scenarios in scope for this
increment's acceptance criteria (§7-F/G/H are non-LLM surfaces; the one
LLM-adjacent test, `test_no_chat_prompt_ever_contains_photo_data`, mocks the
model, so it runs regardless).

## Suite count verification

- Code-agent reported "88 -> 91 backend tests, all passing" (PROJECT_CONTEXT.md
  Decisions Log, 2026-07-11). Independently verified: `python -m pytest -v`
  from `dev/backend/` → **91 collected, 91 passed**, 0 failed, 0 skipped, 0
  errors. Confirmed matching count. Not a zero-test suite.
- Full breakdown by file (`pytest --collect-only -q`, grouped and counted):
  test_ages.py (11), test_api.py (7), test_chat_content_normalization.py (3),
  test_digest.py (8), test_guardrails.py (18), test_memories.py (9),
  test_photo_theme.py (6), test_photos.py (15), test_profiles.py (6),
  test_smoke.py (3), test_timeline.py (5) = 91. Matches the 91 reported by
  `-v`.

## Regression check: finding-7 (Increment 1) — `python -m pytest` vs plain `pytest`

- Increment 1 found plain `pytest` picked up a stale installed copy of `app`
  instead of the live source tree, causing 11/30 false-negative failures;
  fixed via editable install (`pip install -e .`, commit `532a702`).
- Re-verified this increment with the new `pillow-heif` dependency added:
  `python -m pytest` → 91 passed, 0.45s. Plain `pytest` → 91 passed, 0.44s.
  Identical collection, identical pass count, both invocations import the
  live source tree. **No regression.** `pyproject.toml`'s `[tool.setuptools]
  packages = ["app"]` fix (noted in-file) keeps the editable install correct
  now that `data/` (runtime SQLite dir) sits alongside `app/`.

---

## §7-F — Memory log + timeline (items 17-19)

### Scenario: Memory CRUD — invalid moment_date before DOB (item 17)
- Input: `POST /profiles/{id}/memories` with `moment_date` before the
  profile's DOB
- Expected: 422
- Actual: 422
- Result: PASS
- Evidence: `tests/test_memories.py::test_create_memory_moment_date_before_dob_rejected`

### Scenario: Memory CRUD — invalid moment_date in the future (item 17)
- Input: `POST /profiles/{id}/memories` with a future `moment_date`
- Expected: 422
- Actual: 422
- Result: PASS
- Evidence: `tests/test_memories.py::test_create_memory_moment_date_in_future_rejected`

### Scenario: Memory list ordered chronologically (item 17)
- Input: two memories created out of chronological order
- Expected: `GET /profiles/{id}/memories` returns them sorted by `moment_date`
- Actual: `["First", "Second"]` in correct order
- Result: PASS
- Evidence: `tests/test_memories.py::test_list_memories_ordered_chronologically`

### Scenario: Memory delete is a hard delete (item 17)
- Input: create memory, `DELETE` it, then `GET /profiles/{id}/memories`
- Expected: 200 on delete; list is empty afterward (not soft-deleted/hidden)
- Actual: as expected
- Result: PASS
- Evidence: `tests/test_memories.py::test_delete_memory_hard_deletes`

### Scenario: Profile delete cascades to memories (item 17)
- Input: create memory, delete the profile, then check the `memories` table
  directly via `test_db` fixture
- Expected: `memories` route 404s (profile gone); underlying row count for
  that profile_id is 0 (true hard cascade, not just an inaccessible
  orphan row)
- Actual: `GET /profiles/{id}/memories` → 404; `SELECT COUNT(*) FROM
  memories WHERE profile_id = ?` → 0
- Result: PASS
- Evidence: `tests/test_memories.py::test_profile_delete_cascades_memories`

### Scenario: Timeline age-at-moment, full-term profile (item 18)
- Input: `GET /profiles/{id}/timeline` for a full-term profile with one
  logged memory
- Expected: memory entry carries `chronological_months` and
  `effective_months`; `corrected_months` is `None` (full-term)
- Actual: as expected
- Result: PASS
- Evidence: `tests/test_timeline.py::test_timeline_memory_entries_carry_age_at_moment`

### Scenario: Timeline age-at-moment, P2 preterm profile shows corrected age (item 18)
- Input: `GET /profiles/{id}/timeline` for a profile born 8 weeks early, ~6
  months chronological at moment of the logged memory
- Expected: `corrected_months` is not `None` and is less than
  `chronological_months`
- Actual: as expected
- Result: PASS
- Evidence: `tests/test_timeline.py::test_timeline_p2_preterm_shows_corrected_age_at_moment`

### Scenario: R1 hard schema lint on the timeline payload — the item this
gate specifically flagged for independent verification (item 19)
- Input: `GET /profiles/{id}/timeline` for a profile with one logged
  memory; response walked recursively (every dict key, at every nesting
  level, including inside chapter-marker and memory-entry objects) against
  a forbidden-key set: `{"expected_by", "status", "on_track",
  "typical_range", "typical_range_band"}`; raw response text also checked
  for the substrings "typical range" and "behind"
- Expected: none of the forbidden keys appear anywhere in the payload; no
  forbidden substrings in the raw JSON text
- Actual: no forbidden keys found at any nesting depth (recursive walk
  confirmed by reading the test source, not just its assertion outcome —
  `_assert_no_forbidden_keys` is a real recursive dict/list walker, not a
  shallow top-level check); substring checks also clean
- Result: PASS — **this is genuinely tested, not just claimed.** The test
  (`tests/test_timeline.py::test_timeline_r1_schema_lint_no_expected_vs_actual_fields`)
  is a real recursive structural lint, matching PLAN §4.2's "the Test gate
  lints the schema for this" language. Independently confirmed by reading
  the walker implementation (lines 27-34 of the test file), not just
  trusting the test name.
- Evidence: `tests/test_timeline.py::test_timeline_r1_schema_lint_no_expected_vs_actual_fields`

### Scenario: Timeline chapter markers are neutral labels only (item 19,
supporting)
- Input: `GET /profiles/{id}/timeline` for a profile old enough to have
  passed at least one checklist bucket
- Expected: chapter-marker entries contain only
  `{entry_type, bucket_months, label, anchor_date}` — no comparison field
- Actual: exact key set match, no extra fields
- Result: PASS
- Evidence: `tests/test_timeline.py::test_timeline_chapter_markers_are_neutral_labels_only`

**§7-F verdict: items 17, 18, 19 all genuinely covered by real tests, not
just passing incidentally. Item 19 in particular — independently read the
test implementation, confirmed it is a true recursive walk over the full
payload tree, not a shallow/top-level-only check that could miss a nested
forbidden field.**

---

## §7-G — Photos (items 20-24)

### Scenario: Upload valid JPEG (item 20)
- Input: `POST /profiles/{id}/photos`, 50x50 JPEG
- Expected: 201, `content_type` echoed
- Actual: 201, `image/jpeg`
- Result: PASS
- Evidence: `tests/test_photos.py::test_upload_valid_jpeg_201`

### Scenario: Upload over size cap (item 20)
- Input: file > `MAX_PHOTO_BYTES` (10 MB), valid JPEG magic bytes prefix
- Expected: 413
- Actual: 413
- Result: PASS
- Evidence: `tests/test_photos.py::test_upload_over_size_cap_413`

### Scenario: Disguised .exe content-sniffed and rejected (item 20)
- Input: real `.exe` magic bytes (`MZ...`), filename `totally.jpg`, claimed
  `content_type: image/jpeg`
- Expected: 415 (content-sniffed, not extension/claimed-type trusted)
- Actual: 415
- Result: PASS
- Evidence: `tests/test_photos.py::test_upload_disguised_exe_content_sniffed_415`

### Scenario: Upload to nonexistent profile (item 20)
- Input: `POST /profiles/999999/photos`
- Expected: 404
- Actual: 404
- Result: PASS
- Evidence: `tests/test_photos.py::test_upload_to_nonexistent_profile_404`

### Scenario: Delete purges BOTH metadata AND file bytes on disk — the item
this gate specifically flagged for independent verification (item 21)
- Input: upload a photo, note its on-disk path via `_photo_path`, `DELETE`
  it, then check (a) the `photo_meta` row directly via the `test_db`
  fixture and (b) `os.path.exists()` on the file path
- Expected: delete → 200; `photo_meta` row is gone (`fetchone()` is
  `None`); `os.path.exists(on_disk_path)` is `False`
- Actual: both conditions confirmed — the test asserts row absence AND
  `os.path.exists() is False` in the same test, not just one or the other
- Result: PASS — genuinely covers both halves, not just the metadata half
- Evidence: `tests/test_photos.py::test_delete_purges_metadata_and_file_bytes`

### Scenario: Profile delete leaves zero photo files on disk (item 21,
supporting)
- Input: upload two photos to a profile, confirm the profile's photo
  directory is non-empty, then delete the profile
- Expected: the profile's photo directory no longer exists
- Actual: `profile_dir.exists()` is `False` after delete
- Result: PASS
- Evidence: `tests/test_photos.py::test_profile_delete_leaves_zero_photo_files`

### Scenario: No static mount serves photo bytes (item 22)
- Input: `GET /data/photos/` directly (bypassing the family-scoped route)
- Expected: 404 (unroutable)
- Actual: 404
- Result: PASS
- Evidence: `tests/test_photos.py::test_no_static_mount_serves_photo_bytes`

### Scenario: Photo only reachable through the family-scoped API route
(item 22)
- Input: `GET /profiles/{id}/photos/{photo_id}` (the only legitimate path)
- Expected: 200, correct content-type
- Actual: 200, `image/jpeg`
- Result: PASS
- Evidence: `tests/test_photos.py::test_photo_get_requires_family_scoped_route`
- Note: cross-family (family B requesting family A's photo → 404) is
  explicitly out of scope this increment per the task brief — no auth
  exists yet until Increment 3 (PLAN §7-G item 22's second sentence is
  marked "After Increment 3").

### Scenario: At-rest protection — stored file is not plaintext-readable
(item 23, first half — the item this gate specifically flagged)
- Input: upload a JPEG, read the raw bytes back off disk directly (not
  through the API)
- Expected: raw on-disk bytes do NOT start with the real JPEG magic bytes
  (`FF D8 FF`) — i.e., the stored file is encrypted, not a plaintext image
- Actual: raw bytes do not match the JPEG signature
- Result: PASS
- Evidence: `tests/test_photos.py::test_stored_file_is_not_plaintext_readable_image`
- Corroboration (source read, not just test-name trust): `app/photos.py`'s
  `PhotoStore.create()` calls `fernet.encrypt(stripped)` before writing to
  disk, and `get_bytes()` calls `fernet.decrypt()` on read — genuine
  Fernet (AES-128-CBC + HMAC) encryption at rest, not a claim-only comment.
  Key sourced from `PHOTO_ENCRYPTION_KEY` env var (`.env`, gitignored via
  root `.gitignore`'s `.env*` pattern); `.env.example` ships the var name
  blank. Confirmed no `.env` file or key material is tracked in git
  (`git ls-files` shows only `backend/.env.example`).

### Scenario: EXIF GPS absence — JPEG (item 23, second half)
- Input: upload a JPEG with an attached EXIF block (Make tag as an easy
  marker)
- Expected: served/stored image has zero EXIF tags (GPS along with
  everything else — a floor, not a ceiling, per the source comment)
- Actual: `len(stored_exif) == 0`
- Result: PASS
- Evidence: `tests/test_photos.py::test_exif_gps_stripped_on_upload`

### Scenario: EXIF GPS absence — HEIC (item 23, second half, HEIC-specific
regression from the `pillow-heif` fix)
- Input: upload a real, Pillow-encoded HEIC file with EXIF attached
- Expected: served/stored HEIC has zero EXIF tags
- Actual: `len(stored_exif) == 0`
- Result: PASS
- Evidence: `tests/test_photos.py::test_heic_exif_gps_stripped_on_upload`
- Note: this test exists specifically because HEIC's re-save path
  (`pillow_heif`) auto-propagates already-decoded EXIF unless explicitly
  cleared — a real regression the JPEG-only test would not have caught.
  Confirms the `pillow-heif` addition didn't silently reopen the EXIF-GPS
  gap it was added to close (per Decisions Log, judgment call 4 →
  solution-architect resolution → code-agent's `ebe65e7` fix).

### Scenario: Structural isolation — `photos.py` has zero import path to
`llm.py`/`prompts.py` — the item this gate specifically flagged for
independent verification (item 24)
- Input: AST-based import scan (`ast.parse` + `ast.walk`, real
  `import`/`from...import` statements only) of `app/photos.py`,
  `app/photo_theme.py`, `app/routes/photos.py` against `app.llm`/
  `app.prompts`, and the reverse direction
- Expected: no import edges in either direction
- Actual: none found
- Result: PASS — genuinely tested via static analysis, not just asserted
  in a comment. `tests/test_photos.py::test_photo_isolation_import_check`
  uses `ast.parse`/`ast.walk` (a real AST scan, not a docstring/comment
  substring grep — the test file's own comment explicitly notes this to
  avoid a false-positive on its own explanatory prose)
- Evidence: `tests/test_photos.py::test_photo_isolation_import_check`
- Independent corroboration: manually grepped `^import|^from` lines in
  `app/photos.py`, `app/photo_theme.py`, `app/routes/photos.py`,
  `app/llm.py`, `app/prompts.py` — confirmed by direct source read (not
  just re-running the test) that no cross-import exists in either
  direction as of this commit.

### Scenario: No chat prompt ever contains photo data (item 24, integration
half)
- Input: `/chat` call for a profile that has an uploaded photo; LLM model
  mocked to capture the exact message list handed to it
- Expected: neither the photo id nor the substring "photo" appears
  anywhere in the concatenated message text sent to the model
- Actual: neither found
- Result: PASS
- Evidence: `tests/test_photos.py::test_no_chat_prompt_ever_contains_photo_data`

**§7-G verdict: items 20-24 all genuinely covered by real tests. Items 21,
23, and 24 — each specifically flagged for extra scrutiny by this gate's
brief — were independently corroborated by reading the underlying test
implementations and the production source (`app/photos.py`), not just by
re-running the suite and trusting green output.**

---

## §7-H — Digest (items 25-27; items 28-29 correctly out of scope — Increment 3)

### Scenario: Digest content, full-term profile (item 25)
- Input: `GET /profiles/{P1}/digest`
- Expected: non-empty `age_line`; ≥1 milestone; 1-3 activities each with a
  non-empty `supervision_note`; non-empty `memory_prompt`; `disclaimer`
  equals the exact fixed constant
- Actual: all present as expected
- Result: PASS
- Evidence: `tests/test_digest.py::test_digest_p1_full_term_content`

### Scenario: Digest passes the §7-D(15) framing lint (item 25)
- Input: digest milestones + activity descriptions run through
  `check_framing`/`check_medical` (the shared guardrail heuristics)
- Expected: both return `None` (no violation)
- Actual: both `None`
- Result: PASS
- Evidence: `tests/test_digest.py::test_digest_framing_lint`

### Scenario: Digest newborn mode, no milestone comparison (item 26)
- Input: `GET /profiles/{P4}/digest` (21-day-old profile)
- Expected: `milestones == []`; age_line mentions "newborn"; disclaimer
  present
- Actual: as expected
- Result: PASS
- Evidence: `tests/test_digest.py::test_digest_p4_newborn_no_milestone_comparison`

### Scenario: Digest out-of-range mode, no fabricated content (item 26)
- Input: `GET /profiles/{P3}/digest` (40-month-old profile)
- Expected: `milestones == []`, `activities == []`, disclaimer present
- Actual: as expected
- Result: PASS
- Evidence: `tests/test_digest.py::test_digest_p3_out_of_range_no_fabricated_content`

### Scenario: Digest preterm profile uses corrected age in age_line (item
25, supporting — matches PLAN R4)
- Input: `GET /profiles/{P2}/digest` (born 8 weeks early, ~6 months
  chronological)
- Expected: age_line contains "corrected"
- Actual: contains "corrected"
- Result: PASS
- Evidence: `tests/test_digest.py::test_digest_p2_preterm_uses_corrected_age_in_age_line`

### Scenario: Opt-in defaults false / nothing queued for non-opted-in users
— the item this gate specifically flagged for independent verification
(item 27)
- Input: independent source inspection (no test exists for this scenario
  as of this commit) — searched `app/` for `opt_in`, `scheduler`,
  `APScheduler`, `queue`, `smtp`, `email` handling code, and read
  `app/db.py`'s schema and `app/digest.py`'s module docstring
- Expected per item 27: "Opt-in defaults false for every new caregiver;
  nothing is ever sent (or queued) for a non-opted-in user (assert the
  scheduler/queue is empty)."
- Actual finding: `app/db.py`'s `users` table schema (built in Increment 1
  as the F10 auth seam, per PLAN §4.1) does define `digest_opt_in INTEGER
  NOT NULL DEFAULT 0` — a correct schema-level default-false. **However,
  there is no test that asserts this default** (no test creates a user row
  and checks `digest_opt_in`), and — more importantly for item 27's
  "nothing is ever sent/queued" half — **there is no signup/user-creation
  route yet** (auth activation is explicitly Increment 3 scope per PLAN
  §4.6), so "every new caregiver" is not yet a reachable code path to test
  against at all. Confirmed (grep + source read) that no scheduler, queue,
  APScheduler, SMTP, or email-sending code exists anywhere in `app/` —
  `app/digest.py`'s own docstring states this explicitly ("No opt-in,
  scheduler, or email delivery here"). PROJECT_CONTEXT.md's Decisions Log
  mentions APScheduler/unsubscribe-token designs, but only as *prose*
  describing a later architecture decision for Increment 3 — confirmed by
  grep that none of that is implemented in `app/` yet. No dormant
  scheduler code accidentally exists this increment.
- Result: **PARTIAL / GAP.** The "nothing is queued/sent, no dormant
  scheduler" half of item 27 is true and independently verified by source
  inspection, but it is **not covered by an executable test** — it's an
  absence-of-code fact, confirmed only by grep/read, not asserted by
  `pytest`. The "opt-in defaults false" half has a correct schema default
  but likewise **no test exercises it** (there's no route to create a user
  and check the returned/stored value). Given Increment 2 genuinely has no
  user-creation route, a literal test of "opt-in defaults false for every
  new caregiver" isn't fully exercisable yet — but a narrower unit test
  *is* possible now and wasn't written: e.g. inserting a row via
  `INSERT INTO users (...)` without specifying `digest_opt_in` and
  asserting the stored value is `0`, plus a static/regression guard (e.g.
  `assert not any('scheduler' in f for f in os.listdir('app'))` or an
  import-scan for `apscheduler`) so future increments can't silently
  reintroduce dormant delivery code without a test failing. Recommend
  code-agent add both before this item is marked genuinely closed, even
  though the underlying behavior is currently correct.
- Evidence: `dev/backend/app/db.py` line 41 (`digest_opt_in INTEGER NOT
  NULL DEFAULT 0`); `dev/backend/app/digest.py` lines 1-8 (docstring);
  `grep -rniE "opt_in|scheduler|APScheduler|queue|smtp|email" app/
  --include=*.py` (no scheduler/queue/email code found); `grep -rniE
  "opt_in|scheduler|queue" tests/` (no matching test found).

**§7-H verdict: items 25 and 26 genuinely covered by real tests. Item 27 is
a genuine gap between claimed/assumed coverage and actual test coverage —
the underlying behavior is currently correct (verified by source
inspection: no dormant scheduler, correct schema default), but nothing in
the automated suite would catch a regression of either half. This is a
real gap, not just a nitpick: it's the one item in this increment's scope
where "the tests pass" and "the acceptance criterion is tested" diverge.**

---

## Overall pass/fail counts

- **91 collected, 91 passed, 0 failed, 0 skipped, 0 errors** (`python -m
  pytest -v` and plain `pytest`, both from `dev/backend/`, identical
  results — confirms no regression of Increment 1's finding-7).
- Not a zero-test suite in any of the three feature areas — every one of
  §7-F/G/H has multiple real, passing tests.
- **Acceptance-criteria coverage gap found:** §7-H item 27 (opt-in
  default + no dormant scheduler) — behavior is correct, but untested by
  the automated suite. See scenario above for the specific recommendation.
- Items 19 (R1 schema lint), 21 (delete purge, both halves), 23 (at-rest +
  EXIF-GPS), and 24 (structural isolation) — the four items this gate's
  brief specifically flagged for skepticism — were all independently
  corroborated by reading the actual test/source implementations, not
  just re-running `pytest` and trusting green output. All four are
  genuinely, non-superficially tested.

## Gate verdict

**CONDITIONAL PASS.** 91/91 tests genuinely pass, independently
reproduced. §7-F and §7-G acceptance criteria (items 17-24) are fully and
genuinely covered by real tests, including the four items flagged for
extra scrutiny. §7-H items 25-26 are genuinely covered. §7-H item 27 has a
real gap: the behavior is currently correct but has zero automated test
coverage, meaning a future change could silently reintroduce a dormant
scheduler or flip the opt-in default without any test failing.

This is a blocking suite (no advisory suites recorded for this project).
Recommend: send back to code-agent for two small additions before
Increment 2's Test gate is marked fully closed — (1) a unit test asserting
`digest_opt_in` defaults to `0`/false at the schema/store level, (2) a
regression guard (import-scan or file-listing assertion) that fails loudly
if any scheduler/queue/email-sending code is added to `app/` before
Increment 3. Everything else in this increment's scope (F6, F7, F8 items
25-26) is genuinely gate-clear. This is a narrow, well-scoped gap, not a
suite-wide quality problem — the human may reasonably choose to override
and proceed given F8 delivery is explicitly Increment-3 scope and the
underlying behavior is verified correct by inspection, but that override
should be an explicit, recorded decision per the platform's override
protocol, not a silent pass-through.
