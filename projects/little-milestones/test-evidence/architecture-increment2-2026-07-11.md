# Test Evidence — architecture suite — little-milestones — Increment 2 (F6/F7/F8-content)

Run date: 2026-07-11. Suite owner: solution-architect (Architecture test-suite
ownership contract, `knowledge/ARCHITECTURE_KB.md` §7). Suite policy:
blocking (this project's Test Policy records no advisory exceptions).

This is a **conformance-verification pass**, not an architecture-design pass:
does the shipped code in `dev/backend/app/` (F6 memories/timeline, F7
photos/photo_theme, F8-content digest) actually match what
`ARCHITECTURE_KB.md` specifies, and does the suite that's supposed to prove
that actually exist and actually prove it. §9's two follow-up design
questions (HEIC, multi-photo theming) were resolved in a separate pass
earlier the same day and are not re-litigated here.

Method: read `ARCHITECTURE_KB.md` §0/§3/§4/§7 first, then read the shipped
code (`app/db.py`, `app/profiles.py`, `app/memories.py`, `app/photos.py`,
`app/photo_theme.py`, `app/digest.py`, `app/guardrails.py`,
`app/routes/*.py`, `app/main.py`) and every test file under
`dev/backend/tests/` that could plausibly cover the four items in scope. No
tests were executed by solution-architect in this pass (evidence is
inspection-based: does the required test exist and does it test what it
claims to); test-agent's suite already independently re-runs the full
`pytest` count.

---

## 1. Contract tests — `Store[T]` interface conformance

`ARCHITECTURE_KB.md` §0: "All stores implement a common `Store[T]` protocol
(`create`, `get`, `list_for_family`, `delete`)... so the SQLite decision is
testable in isolation." §7 lists this as an owned contract test.

### Scenario: does a `Store[T]` conformance test exist anywhere in the suite
- Searched `dev/backend/tests/` for any test asserting a common interface
  shape across `ProfileStore`/`MemoryStore`/`PhotoStore` (by name pattern
  and by content) — none found. No `test_stores.py`, no
  `test_architecture_contracts.py`, no inline contract assertion in any
  existing test file.
- Result: **FAIL — no coverage.** This is a suite item this role owns per
  §7 and it has never been built, for any store, in any increment.

### Scenario: manual conformance check — does the shipped interface actually match §0's stated shape, absent a test
- `ProfileStore` (`app/profiles.py`): `create(family_id, data)`,
  `get(family_id, profile_id)`, `list_for_family(family_id)`,
  `delete(family_id, profile_id)` — **exact match** to §0's stated protocol.
- `MemoryStore` (`app/memories.py`): `create(profile_id, data)`,
  `get(profile_id, memory_id)`, `list_for_profile(profile_id)` (not
  `list_for_family`), `delete(profile_id, memory_id)`, plus an extra
  `last_moment_date(profile_id)`. The module's own docstring explains why:
  memories have no `family_id` column (transitively scoped through
  `profiles.family_id` + cascade), so a literal `list_for_family` would be
  meaningless without an extra join the store doesn't need. **This is a
  reasoned, documented deviation from §0's literal method name, not an
  oversight** — but §0 as written doesn't say this, so a reader of the KB
  alone would expect `list_for_family` on every store.
- `PhotoStore` (`app/photos.py`): `create(profile_id, raw_bytes,
  content_type, memory_id=None)`, `get_meta(profile_id, photo_id)` (not
  `get`), `get_bytes(profile_id, photo_id)` (a second, decrypt-and-read
  accessor `get` alone couldn't unambiguously represent), `list_for_profile`
  (not `list_for_family`), `delete(profile_id, photo_id)`, plus
  `delete_all_files_for_profile(profile_id)`. Splitting `get_meta`/
  `get_bytes` is a defensible design choice (a plain `get` returning
  sometimes-metadata sometimes-plaintext-bytes would be a worse interface,
  and decrypting bytes on every metadata read would be wasteful) — but it
  is a real, un-flagged divergence from the "common protocol" framing in §0.
- Result: **FAIL / real gap, not blocking on its own merits, but blocking under this
  suite item's absence.** The three stores are *not* interchangeable behind
  a literal `Store[T]` shape — each has a domain-appropriate but distinct
  method set. That may well be the right call (transitively-scoped entities
  genuinely don't have a `family_id` to scope by), but §0's own wording
  promises more uniformity than the code delivers, and nothing tests either
  the promise or the actual, more nuanced shape. **Recommend**: either (a)
  a contract test asserting each store's *actual* documented shape (three
  separate, explicit interface assertions, not one generic `Store[T]`
  check), or (b) a KB edit to §0 replacing "common `Store[T]` protocol" with
  the real pattern ("family-scoped stores expose `list_for_family`;
  entities scoped transitively through a parent expose `list_for_<parent>`
  instead") — either closes the gap, but right now neither exists.

---

## 2. Contract tests — `photo_theme.extract_accent` clamped-band contract

`ARCHITECTURE_KB.md` §7: "`photo_theme.extract_accent` output always
satisfies the clamped-band contract (**property-based test: for N random
hues**, derived tokens fall within the specified S/L ranges) or returns
`None`."

### Scenario: is this actually property-based / multi-case, per the KB's own stated bar
- `tests/test_photo_theme.py` has 6 tests, each against a single fixed
  color: vivid blue (band-conformance + both contrast checks, 3 separate
  test functions all reusing the *same* blue input), solid mid-gray
  (near-gray filter → `None`), undecodable bytes (`None`), and one
  near-`--lm-danger`-hue red (hue-rotation check, single fixed color, with
  an explicit "if tokens is None, that's also acceptable" escape hatch that
  makes the assertion non-committal on some runs).
- **Only one hue (blue, ~228°) is ever checked against the clamped-band
  contract.** There is no loop over N random or even N fixed hues spanning
  the color wheel, no parametrized test, no `hypothesis`-style property
  test. §7's literal bar ("for N random hues") is not met — this is a
  single-example regression test wearing a property-test's stated
  justification.
- **No test exercises the skin-tone exclusion band directly.** The only
  cluster-filtering behavior actually tested is the near-gray path
  (saturation < 15%); UX_KB §6.3 rule 1 / ARCHITECTURE_KB §4.1 step 4's
  skin-tone HSL band (hue 5–35°, sat 20–60%, light 40–85%) has zero test
  coverage — no input constructed to fall inside that band and confirm it's
  correctly excluded (as opposed to being excluded only by coincidence
  because the surviving cluster in a given test photo happens to be outside
  it).
- Result: **FAIL against the KB's own stated test bar.** What exists is
  real and passing, but it is not the property-based/multi-hue test §7
  commits to, and it has a second, independent gap (skin-tone-band
  exclusion, the actual highest-stakes filter in this pipeline per
  RESPONSIBLE_AI_KB's no-face-processing framing) with zero direct coverage.

---

## 3. Design-conformance — SQLite cascade chain (profile → memories → photo_meta → files)

`ARCHITECTURE_KB.md` §7: "SQLite foreign-key cascade behavior (`PRAGMA
foreign_keys=ON` actually enforced...); delete-a-family cascades every
table." Task brief specifically calls out: profile delete → memories gone →
photo_meta gone → files gone.

### Scenario: `PRAGMA foreign_keys=ON` actually set, not left at SQLite's default-off
- `app/db.py::get_connection()` executes `PRAGMA foreign_keys = ON`
  unconditionally on every connection open (not just at `init_db()` time),
  which is the correct fix for the footgun §7 names (the pragma is
  per-connection, not persistent in the DB file). **PASS** by inspection.

### Scenario: profile delete → `memories` rows actually gone (DB-row-level, not just route-level)
- `tests/test_memories.py::test_profile_delete_cascades_memories` creates a
  memory, deletes the profile via the route, then queries
  `SELECT COUNT(*) FROM memories WHERE profile_id = ?` directly against the
  test DB connection and asserts 0. **PASS, real DB-level assertion, not
  just a 404 on the list route.**

### Scenario: profile delete → `photo_meta` rows actually gone (DB-row-level)
- `tests/test_photos.py::test_profile_delete_leaves_zero_photo_files`
  uploads two photos, deletes the profile, and asserts the on-disk photo
  *directory* no longer exists. **It never queries `photo_meta` directly.**
  No test anywhere asserts `SELECT COUNT(*) FROM photo_meta WHERE
  profile_id = ?` returns 0 after a profile delete. The DB-level half of
  this specific step in the chain the task asked to verify is untested —
  only the filesystem half is.
- Result: **FAIL — partial coverage.** Files-gone: verified. Metadata-row-
  gone: asserted nowhere, for either delete path (see next scenario).
  Given `ON DELETE CASCADE` is declared on `photo_meta.profile_id`, this is
  very likely true in practice — but "very likely true, unverified" is
  exactly the gap a Test-gate architecture suite exists to close, and this
  project's own Increment-1 precedent (unit-integration-2026-07-11.md)
  treats an identically-shaped "probably true but unasserted" gap as a
  reportable FAIL, not a pass-by-inspection.

### Scenario: memory delete → attached `photo_meta` rows cascade (the `memory_id` FK path, independent of the `profile_id` FK path)
- `photo_meta` has **two** cascade paths to a photo: `memory_id FK →
  memories(id) ON DELETE CASCADE` and `profile_id FK → profiles(id) ON
  DELETE CASCADE`. `tests/test_memories.py::test_delete_memory_hard_deletes`
  deletes a memory that was never given an attached photo — no test
  anywhere creates a memory, attaches a photo to it (`memory_id` set on
  upload — the route/param exists per `PhotoStore.create`'s signature), 
  deletes *the memory* (not the profile), and asserts the photo's
  `photo_meta` row and file are gone. This specific cascade edge is
  **completely untested**, in either direction (DB row or file — a memory
  delete doesn't call `delete_all_files_for_profile`, so this path relies
  entirely on the DB cascade to remove the metadata row, and would *orphan
  the file on disk* even if the DB row went away correctly, since nothing
  unlinks the file bytes on a memory-only delete).
- Result: **FAIL — no coverage, and a plausible real defect, not just a
  test gap.** Unlike the profile-delete path (which explicitly unlinks
  files before deleting the DB row, per `routes/profiles.py`), nothing in
  `routes/memories.py`'s delete handler unlinks photo files for photos
  attached to that memory before the DB cascade removes their `photo_meta`
  rows. If a photo is attached to a memory and that memory (not the whole
  profile) is deleted, the `photo_meta` row is removed by cascade but the
  encrypted file on disk is very likely orphaned — the same "row exists,
  file gone" vs. "row gone, file exists" crash-safety concern
  SECURITY_KB §2.4 addresses for profile/photo deletes was never extended
  to memory deletes. **This is a genuine architecture/security-adjacent gap
  in the shipped code, found by tracing the two FK paths against the actual
  delete-handler code, not merely a missing test.**

### Scenario: family delete → cascades every table (§7's other named case)
- No route exposes family delete yet (F10/auth not built until Increment
  3), so this specific cascade is currently unreachable from the API and
  untestable end-to-end. Reasonable to defer — not a gap in Increment 2's
  actual shipped surface, flagged here only for completeness against §7's
  literal wording.

---

## 4. Design-conformance — `guardrails.py` / `photos.py` import isolation

`ARCHITECTURE_KB.md` §7: "`guardrails.py` import isolation from `photos.py`
and vice versa (shared static-import-graph check with F7's isolation
requirement, §6.3)."

### Scenario: does a static check actually exist for this specific pair
- `tests/test_photos.py::test_photo_isolation_import_check` is a real,
  AST-based (not comment/docstring-substring) static import-graph check —
  but it checks `app.photos`/`app.photo_theme`/`app.routes.photos` against
  `app.llm`/`app.prompts` only. **`app.guardrails` is not one of the
  modules checked in either direction.** The literal pair §7 names
  (`guardrails.py` ↔ `photos.py`) has no dedicated automated check.
- Manual verification (read both files in full): `app/guardrails.py`
  imports only `app.milestones`; `app/photos.py` imports `app.photo_theme`
  and stdlib/`cryptography`/`pydantic` — **neither imports the other**, so
  isolation currently holds in fact. But this is solution-architect's own
  manual read this session, not a standing, re-run-every-commit check —
  exactly the "comment saying isolation is maintained" risk the task asked
  to distinguish from a real test.
- Result: **FAIL against the KB's literal ownership claim, PASS by manual
  inspection of current code.** Non-blocking on its own (isolation is true
  today, and there's no plausible reason `guardrails.py` — a text-pattern
  checker for LLM output — would ever need to import photo-handling code),
  but the suite item as specified doesn't exist, so a future regression
  (e.g. someone importing `app.photos` into `guardrails.py` to log a
  photo-count alongside a violation) would not be caught automatically.

---

## 5. `photo_meta.id`: TEXT/uuid4 vs. the rest of the schema's ID convention

Task brief: is code-agent's judgment call (autoincrement int → TEXT uuid4)
consistent with the rest of the schema, or a flagged inconsistency.

### Scenario: compare `photo_meta.id`'s type against every other primary key in `app/db.py`'s `SCHEMA`
- `families.id`, `users.id`, `profiles.id`, `memories.id`: `INTEGER PRIMARY
  KEY [AUTOINCREMENT]` — sequential, enumerable, never externally exposed
  as anything security-sensitive on their own.
- `sessions.token_hash`, `invites.code`: `TEXT PRIMARY KEY` — both are
  **already** non-sequential, non-enumerable, externally-exposed-adjacent
  identifiers (a session token and an invite code respectively) — the exact
  same category `photo_meta.id` now joins (an id that doubles as a
  filename an attacker might try to guess, per code-agent's stated
  reasoning and SECURITY_KB §2).
- Result: **Not an inconsistency — a correctly-recognized precedent.**
  `photo_meta.id`'s TEXT/uuid4 shape is consistent with this schema's
  existing (if implicit) two-tier ID convention: sequential integers for
  "internal, never independently guessable-sensitive" entities, opaque
  random tokens for entities whose id is exposed or security-relevant on
  its own. code-agent's judgment call correctly identified which tier
  `photo_meta.id` belongs in.
- **Documentation gap, non-blocking:** `ARCHITECTURE_KB.md` §3's own schema
  listing (`photo_meta(id, memory_id FK→memories ...)`) was never updated
  to show `id` as TEXT/uuid4 — it still reads as if every table's `id` is
  the same shape. The decision is recorded in `PROJECT_CONTEXT.md`'s
  Decisions Log (Increment 2 judgment call 1) but not folded back into the
  architecture document of record. Recommend a one-line edit to §3 to keep
  the KB itself accurate for a reader who doesn't also read
  PROJECT_CONTEXT.md.

---

## 6. Component map cross-check (§0) — F6/F7/F8-content file layout

### Scenario: does the shipped file layout match §0's component map exactly
- `app/memories.py`, `app/photos.py`, `app/photo_theme.py`, `app/digest.py`,
  `app/routes/memories.py`, `app/routes/photos.py`, `app/routes/digest.py`
  all exist exactly as named in §0. `app/main.py` remains assembly-only
  (`init_db()`, CORS, router mounts, the explicit "no static mount, ever"
  negative-space comment) — no route-handler logic leaked into it.
  `app/db.py` carries the full schema including F8's `users` column
  additions (`last_digest_sent_at`, `unsubscribe_token_hash`) even though
  F8 *delivery* isn't built until Increment 3, matching §3's "lay down the
  schema for later increments' entities too" instruction.
- Result: **PASS — no deviation found.**

---

## Summary

| Item | Status |
|---|---|
| `Store[T]` contract test (ProfileStore/MemoryStore/PhotoStore) | **FAIL — never built**; manual check shows each store's actual interface reasonably-but-undocumentedly diverges from §0's literal wording |
| `photo_theme.extract_accent` clamped-band property test | **FAIL against KB's own stated bar** — single-hue example test, not N-random-hues property test; skin-tone-band exclusion has zero direct test coverage |
| Cascade: profile delete → memories gone | PASS (real DB-row assertion) |
| Cascade: profile delete → photo_meta gone | **FAIL — untested** (files-gone verified; DB-row-gone never asserted) |
| Cascade: memory delete → attached photo_meta/file gone | **FAIL — untested, and a likely real orphaned-file defect** (`routes/memories.py`'s delete handler doesn't unlink photo files before the DB cascade, unlike the profile-delete path) |
| `guardrails.py` ↔ `photos.py` static isolation check | **FAIL as specified** (no dedicated check exists); PASS by manual inspection of current imports |
| `photo_meta.id` TEXT/uuid4 vs. schema ID convention | **Consistent, not an inconsistency** — matches the existing `sessions.token_hash`/`invites.code` opaque-token precedent; KB §3 documentation not updated to match (non-blocking) |
| §0 component-map file layout | **PASS — exact match** |

## Gate verdict: **Architecture suite does not pass — blocking.**

Per this project's Test Policy (all active suites blocking, no advisory
exceptions) and the precedent set at Increment 1's Test gate (an identically
-shaped "probably fine, unverified" gap on the disclaimer/red-team items was
recorded as a blocking FAIL, not waved through), this suite is reported as a
blocking finding, not a pass, for two reasons that are more than test-writing
debt:

1. **A likely real defect, not just a missing test**: memory-only delete
   (as opposed to profile delete) does not unlink attached photo files
   before the DB cascade removes their metadata rows — an orphaned
   encrypted file left on disk with no `photo_meta` row pointing at it. This
   directly touches SECURITY_KB §2.4's crash-safety/delete-completeness
   discipline, which this project treats as load-bearing, not incidental.
2. **Two suite items this role explicitly owns per §7 were never built at
   all** (`Store[T]` contract test, the property-based `extract_accent`
   test) rather than built-and-weaker-than-ideal — a materially different
   situation from "test exists but has a caveat," which this project's own
   precedent (Increment 1) already distinguishes and treats as blocking
   when coverage is genuinely absent.

**Recommended path to close, mirroring the Increment-1 pattern (code-agent
fixes, solution-architect/test-agent re-verifies):**
- code-agent: add a photo-file-unlink step to `routes/memories.py`'s delete
  handler (list `PhotoStore.list_for_profile`/attached-photo lookup by
  `memory_id`, unlink files, same files-first ordering as the profile-delete
  path) — this is the one item here that is a product fix, not a test-only
  gap.
- code-agent or solution-architect: add the missing `Store[T]` contract
  test (three explicit per-store interface assertions, given the KB's
  literal wording doesn't match the justified real shape), the N-random-hue
  property test + a dedicated skin-tone-band-exclusion test case for
  `extract_accent`, a direct `photo_meta` row-count assertion after profile
  delete, a memory-delete-with-attached-photo cascade test, and an extension
  of `test_photo_isolation_import_check` to include `app.guardrails` in both
  directions.
- solution-architect: fold the `photo_meta.id` TEXT/uuid4 decision back into
  `ARCHITECTURE_KB.md` §3's schema listing (documentation-only, no code
  change).

Non-blocking on their own, tracked for closure alongside the above: the KB
§3 documentation sync, and the general "each store's actual shape should be
named explicitly in §0" KB wording tightening.
