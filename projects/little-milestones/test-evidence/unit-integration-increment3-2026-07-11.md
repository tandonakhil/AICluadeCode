# Test Evidence — unit/integration suite — little-milestones — Increment 3 (F9 buying recs, F10 auth, F8 email delivery)

Run date: 2026-07-11. Suite: `pytest` (dev/backend/tests/), test-agent
(blocking per default policy — no advisory suites recorded for this
project). Environment: `dev/backend/.venv` (Python 3.9.6). Verified with
both `python -m pytest -v` and plain `pytest -q` (the Increment-1 gate's
"stale installed package" finding stays fixed — both invocations agree).

## Suite count verification

- Code-agent's report: "165 backend tests pass." Independently re-run:
  `python -m pytest --collect-only -q` → 165 collected;
  `python -m pytest -v` → **165 passed, 0 failed, 0 skipped, 0 errors**;
  plain `pytest -q` → **165 passed**, identical count. Confirmed matching.
- Not a zero-test suite. This is a real increase from Increment 2's 137
  (101 pre-existing Inc-1/2 tests + auth/products/email suites added this
  increment).

---

## §7-I Buying recommendations (items 30–32) — `tests/test_products.py`

### Scenario: catalog-only items, non-empty safety_note, corrected-age keying (item 30)
- Input: `GET /profiles/{id}/products` for P1 (14mo full-term), P2 (preterm,
  corrected bucket), P3 (40mo, out-of-range), P4 (newborn)
- Expected: items only from `products_catalog.json`, each with non-empty
  `safety_note`; P2 keyed to corrected bucket; defined P3/P4 behavior
- Actual: all four fixtures pass; `test_products_items_only_from_catalog_no_llm_origination`
  asserts returned title set is a subset of the catalog's own title set
- Result: PASS
- Evidence: `test_products_p1_full_term_14_months`,
  `test_products_p2_preterm_keyed_to_corrected_bucket`,
  `test_products_p3_out_of_range_no_fabricated_items`,
  `test_products_p4_newborn_uses_defined_mode`,
  `test_products_items_only_from_catalog_no_llm_origination`

### Scenario: recall filter, tested by fixture injection (item 31 — critical, verified in depth)
- Input: `test_denylisted_category_injected_into_catalog_never_appears`
  deep-copies the real catalog into `tmp_path`, first asserts the *live*
  catalog starts clean of the denylisted category (fixture-validity
  assumption), then deliberately appends an item carrying a denylisted
  `category` (e.g. `drop_side_cribs`) into bucket_months=12 of the copy,
  writes it to a temp file, and calls `get_products_for_bucket(12,
  catalog_path=poisoned_path, denylist_path=DENYLIST_PATH)`
- Expected: the injected category/title MUST NOT appear in the filtered
  response
- Actual: neither the category nor the injected title appears
- Result: PASS — **this is a genuine injection test, not "the shipped
  catalog happens to be clean."** It reads a real file with an actually
  corrupted category, runs the real filter function against it, and
  asserts on the real output. `test_every_bucket_denylist_filter_applies_for_all_denied_categories`
  extends this to every denylisted category injected into every bucket
  (broader than the single-category case PLAN literally asks for)
- Evidence: `tests/test_products.py::test_denylisted_category_injected_into_catalog_never_appears`,
  `::test_every_bucket_denylist_filter_applies_for_all_denied_categories`

### Scenario: no small-part toys under 36mo; no tracking/affiliate/price; chat has no product path (item 32)
- Input: `get_products_for_bucket` for every bucket <36mo checked against
  the `small_part_toys_under_3` category; full JSON payload scanned for
  `$`, `price`, `utm_`, `affiliate`, `sponsored`, "only 3 left"; AST parse
  of `app/llm.py` and `app/prompts.py` for any import mentioning `products`
- Expected: none of the above ever present/importable
- Actual: confirmed absent / no import path exists
- Result: PASS. Note: the "chat defers to the feature" half of item 32 is
  verified structurally (no code path exists for chat to originate a
  product), the same pattern used for F7 photo isolation — a legitimate
  and arguably stronger proof than a prompt-level assertion, but it does
  not by itself prove the chat's *prose* framing is safety-consistent
  when a user asks "what should I buy?" (that prose behavior is live-LLM,
  non-deterministic territory — see the §7-J item 37 gap below for the
  same category of limitation)
- Evidence: `test_no_small_part_toy_categories_in_under_36_month_buckets`,
  `test_products_payload_has_no_price_brand_or_tracking`,
  `test_chat_asked_what_to_buy_has_no_products_import_path`

**§7-I verdict: genuinely covered.** All three items have real, specific
tests, and item 31 in particular is exactly the fixture-injection test
PLAN specifies, independently confirmed by reading the test body (not
just its name).

---

## §7-J Auth + multi-caregiver (items 33–37) — `tests/test_auth.py`, `tests/conftest.py`

### Scenario: 401 without session, 401 wrong password, argon2 hash storage, HTTP-only cookie (item 33)
- Input: `GET /profiles` and `POST /profiles` with no session cookie;
  login with wrong password; direct sqlite inspection of
  `users.password_hash`; `Set-Cookie` header inspection
- Expected: 401 / 401 / hash starts with `$argon2`, not plaintext / cookie
  carries `HttpOnly`
- Actual: `test_data_route_without_session_is_401` → 401 on both routes;
  `test_login_wrong_password_generic_401` → 401, generic message (also
  `test_login_unknown_email_same_generic_401` for no-enumeration);
  `test_password_stored_only_as_argon2_hash` → direct DB read shows
  `row["password_hash"] != "correct horse battery staple"` and
  `.startswith("$argon2")`; `test_session_cookie_is_httponly_and_samesite_lax`
  → `"HttpOnly" in set_cookie` and `samesite=lax`
- Result: PASS — all four sub-claims are real, store-level or
  response-level assertions, not comments
- **Coverage gap (minor, not blocking):** the no-session-401 check is
  exercised directly against only `/profiles` (GET+POST). Every other
  data route (`memories`, `photos`, `digest`, `timeline`, `products`,
  `chat`, `invites`) shares the same single `Depends(get_current_family)`
  dependency (confirmed by code inspection — `grep Depends(get_current_family)`
  across `app/routes/*.py` shows one shared function, not per-route
  copies), so the guarantee is structurally sound, but there is no direct
  test asserting 401 on those other routes with no session. Recommend
  code-agent add one parametrized test hitting each data route
  unauthenticated, to catch a future route that's added without the
  dependency rather than relying solely on the architectural argument.
- Evidence: `test_data_route_without_session_is_401`,
  `test_login_wrong_password_generic_401`,
  `test_password_stored_only_as_argon2_hash`,
  `test_session_cookie_is_httponly_and_samesite_lax`

### Scenario: family isolation, 404 not 403, all six resource types (item 34 — checked per-resource)
- Input: `test_cross_family_profile_access_is_404_not_403` — family A
  creates a profile; family B (a second, separately signed-up user) then
  requests: `GET /profiles/{id}`, `/profiles/{id}/memories`,
  `/profiles/{id}/timeline`, `/profiles/{id}/digest`,
  `/profiles/{id}/products`, `/profiles/{id}/photos/does-not-matter`
- Expected: 404 for **each** of the six, never 403
- Actual: all six assert `== 404` individually (resp/resp2/resp3/resp4/resp5/resp6),
  confirmed by reading the test body line-by-line — profiles, memories,
  timeline, digest, products, and photos are each present and each
  checked. This is exactly the "commonly missed one resource type" risk
  called out in the task, and it is NOT missed here — all six are covered
- Result: PASS
- Evidence: `tests/test_auth.py::test_cross_family_profile_access_is_404_not_403`
  (lines covering profiles/memories/timeline/digest/products/photos)

### Scenario: invite flow — single-use, expiry, code format (item 35)
- Input: `test_join_reused_code_rejected` (same code used twice),
  `test_join_expired_code_rejected` (DB row's `expires_at` back-dated),
  `test_join_unknown_code_rejected`, `test_join_valid_invite_becomes_caregiver_and_sees_family_profiles`
  (positive path: second caregiver sees profiles, can create a memory)
- Expected: reused code → 4xx; expired code → 4xx; valid code → 201,
  caregiver role, visible family data
- Actual: reused → 400; expired → 400; unknown → 400; valid → 201 +
  `role == "caregiver"` + profile visible + memory creation succeeds (201)
- Result: PASS on single-use and expiry enforcement.
- **Coverage gap (minor):** "code format" is not independently asserted.
  `test_owner_can_create_invite` only checks `body["code"]` is truthy —
  no assertion on length/charset/entropy of the generated code. By code
  inspection (`app/auth.py::generate_opaque_token` → `secrets.token_urlsafe(32)`,
  the same primitive used for session tokens and the unsubscribe token),
  the implementation is sound, but there's no regression test that would
  catch a future change to a weaker/predictable code generator. Recommend
  a one-line test asserting invite code length/character set.
- Evidence: `test_join_reused_code_rejected`, `test_join_expired_code_rejected`,
  `test_join_unknown_code_rejected`, `test_owner_can_create_invite`,
  `test_join_valid_invite_becomes_caregiver_and_sees_family_profiles`

### Scenario: role enforcement — caregiver 403 on delete/invite, owner succeeds; pre-auth data ownership (item 36)
- Input: `test_caregiver_cannot_delete_profile_owner_can`,
  `test_caregiver_cannot_delete_photo_owner_can`,
  `test_caregiver_cannot_create_invite`,
  `test_pre_auth_data_invisible_to_second_family`
- Expected: caregiver → 403 on profile delete, photo delete, invite
  creation; owner → success on the same actions; Increment 1/2 pre-auth
  data owned by family 1 (first signup), invisible to any later family
- Actual: all three caregiver actions return 403; owner's profile delete
  returns 200; `test_signup_first_user_becomes_owner_of_default_family`
  confirms `family_id == 1` for the first-ever signup; a second signup's
  attempt to read the first profile returns 404 and its own `/profiles`
  list is empty
- Result: PASS — all sub-claims real and independently checked
- Evidence: `test_caregiver_cannot_delete_profile_owner_can`,
  `test_caregiver_cannot_delete_photo_owner_can`,
  `test_caregiver_cannot_create_invite`,
  `test_pre_auth_data_invisible_to_second_family`,
  `test_signup_first_user_becomes_owner_of_default_family`

### Scenario: §7-A adversarial suite re-passes under authenticated session (item 37 — critical; this suite's own evidence, see cross-suite resolution below)
- Input: verified code-agent's specific claim — that `tests/conftest.py`'s
  `client` fixture now signs up a user before yielding, and that this
  satisfies item 37 for "every existing test"
- Expected (per code-agent's report): the mechanism is real, and it
  constitutes "the full §7-A adversarial suite re-passes under a real
  authenticated session"
- Actual, checked directly against `conftest.py`:
  - The mechanism claim IS TRUE: `client` fixture (lines 38–58) calls
    `POST /auth/signup` and asserts 201 before yielding
    `unauthenticated_client`; `TestClient` persists cookies across calls
    within one instance, so every test using the `client` fixture
    genuinely runs its requests through a real session, not a bypass.
    Re-confirmed independently by reading the fixture body, not taking
    the claim at face value.
  - **However, this does NOT fully satisfy item 37 as literally stated.**
    The actual §7-A content — the 8 live-LLM adversarial scenarios
    (anxiety/R1, medical dosing/R2, diagnosis/R2, regression red
    flag/R2, premature infant/R4, out-of-range old/R4, out-of-range
    newborn/R4, unsafe activity/R5) — were previously verified only via
    a **manual, non-pytest live rerun against a running server**
    (`test-evidence/red-team-bias-2026-07-11-LIVE-RERUN.md`, run by the
    orchestrator directly, real Anthropic API calls, real model
    responses graded against the R1-R8 pass/fail criteria). That live
    rerun predates auth entirely (Increment 1) and has **not** been
    re-run for Increment 3.
  - Grepped the pytest suite directly for any test containing the actual
    adversarial prompt text (`"freaking out"`, `Tylenol`, `autism`, safe
    sleep, etc.) — none exist. `test_guardrails.py`'s 18 tests exercise
    `check_framing`/`check_medical`/`enforce` as pure Python functions,
    with no `client` fixture and no HTTP call at all — they cannot be
    "authenticated" or "unauthenticated," auth is not in their path.
    `test_chat_content_normalization.py`'s 3 tests exercise `_as_text()`
    directly, same story. `test_smoke.py` does call the real `/chat`
    endpoint through the authenticated `client` fixture, but only with
    benign smoke prompts ("hello"), not the R1-R8 adversarial content.
  - Code-agent's own PROJECT_CONTEXT.md entry (lines 1034–1051) already
    discloses this precisely and accurately — it explicitly says "Not
    re-covered in this pass: a live-LLM red-team re-run... equivalent to
    the one the orchestrator ran live for Increment 1... is recommended
    but not performed," and flags it for the Test gate to decide. This
    independent re-check confirms that disclosure is accurate and the
    gap is real, not overstated or hedged unnecessarily.
- Result: **PARTIAL, on this suite's evidence alone** (see cross-suite
  note below, which resolves item 37 to PASS once read together with the
  red-team-bias suite's own explicit decision). The deterministic guardrail-function
  regression (101 pre-existing tests, all now genuinely running through
  a real authenticated session for their own HTTP-level assertions) is
  real and passes. But the specific, literal claim of item 37 — "the
  full Increment-1 red-team/adversarial guardrail suite re-passes under
  a real authenticated session" — has not actually been exercised for
  Increment 3, because that suite was never pytest-native to begin with;
  it is a live-LLM manual exercise that has not been re-run post-auth.
- Evidence: `dev/backend/tests/conftest.py` lines 38–58 (mechanism, real);
  absence of R1-R8 prompt text anywhere in `dev/backend/tests/*.py`
  (confirmed via grep); `PROJECT_CONTEXT.md` lines 1034–1051 (code-agent's
  own accurate disclosure); `test-evidence/red-team-bias-2026-07-11-LIVE-RERUN.md`
  (the last time this suite actually ran, Increment 1, pre-auth)

### Cross-suite note: red-team-bias suite's independent resolution of item 37

After this evidence was drafted, `test-evidence/red-team-bias-increment3-2026-07-11.md`
(owner: responsible-ai-architect, that suite's own scope) was checked and
found to address this exact question directly, not incidentally. Their
verdict: **PASS — no live-LLM re-run of the §7-A/RESPONSIBLE_AI_KB §5
scenarios is warranted this increment**, reasoned explicitly (not
defaulted) from a direct read of `chat.py`/`auth.py`: `get_current_family`'s
signature and return shape are unchanged from Increment 1, only its body
now resolves from a real session instead of a hardcoded default; the
`enforce(raw_text, profile_id=profile.id)` call and everything upstream of
it in `chat.py` (prompt construction, `model.invoke()`, `_as_text()`) is
byte-for-byte unchanged; the auth dependency sits strictly upstream of
profile resolution, not wrapped around request/response body construction
that guardrail logic reads or writes. Their explicit fallback condition —
re-assess if a future increment touches `chat.py`'s response-construction
path, `prompts.py`, or `guardrails.py` itself — is a sound, narrowly-scoped
decision boundary, not a blanket exemption.

**This test-agent's own finding above stands on its own facts** (the
pytest suite alone does not contain or re-exercise the 8 R1-R8 adversarial
prompts, and code-agent's "conftest fixture satisfies item 37" framing
conflates deterministic-function regression with live-model-behavior
regression) — but combined with the red-team-bias suite's suite-scoped,
reasoned, code-level analysis of *why* a live re-run isn't needed this
specific increment, item 37 is **no longer treated as an open,
undecided gap**. It is a **decided, documented, cross-suite-consistent
PASS**, not a silent pass-through. Revising this suite's own item 37
line item from "PARTIAL / GAP" to **PASS, decided-not-to-re-run** on
that basis — see the Gate Verdict section below for the combined
statement.

---

## Judgment call: plaintext `users.unsubscribe_token` column (beyond ARCHITECTURE_KB §5.4)

- Claim to verify: is there a test asserting the plaintext column is
  never used for verification/lookup — only the hash?
- Code inspection: `app/users.py::unsubscribe_by_token_hash` is the
  *only* write path reachable from the unauthenticated unsubscribe route
  (`app/routes/digest.py` line 106: `user_store.unsubscribe_by_token_hash(hash_token(token))`),
  and its SQL is `UPDATE users SET digest_opt_in = 0 WHERE
  unsubscribe_token_hash = ?` — the plaintext `unsubscribe_token` column
  is never referenced in any WHERE clause anywhere in the codebase
  (grepped `app/*.py` for `unsubscribe_token FROM`/`unsubscribe_token =`
  outside of the scheduler's outbound-URL-building read, which is a
  legitimate, different use). So the implementation is correct today.
- **Test coverage gap: no test proves this negatively.** Every existing
  unsubscribe test (`test_digest_unsubscribe.py`) passes the *correct*
  raw token, whose hash also matches — so these tests cannot distinguish
  "verified via hash" from "verified via plaintext equality," because
  both would pass identically today. There is no test that, e.g.,
  corrupts the plaintext `unsubscribe_token` column while leaving
  `unsubscribe_token_hash` correct (or vice versa) and asserts the
  hash-only path still governs. Without such a test, a future
  regression that accidentally adds a `WHERE unsubscribe_token = ?`
  fallback path would not be caught by this suite.
- Result: **Judgment call itself is sound (confirmed by code, not test)
  — but the testing-coverage question asked is a genuine gap.** Recommend
  code-agent add one differential test: set `unsubscribe_token_hash` to a
  wrong value while `unsubscribe_token` matches the request, confirm the
  route does NOT unsubscribe (or the reverse), to structurally lock in
  "hash is the sole verification mechanism" the same rigor item 31's
  fixture-injection test locks in the recall filter.
- Evidence: `app/users.py` line 150–162 (`unsubscribe_by_token_hash`),
  `app/routes/digest.py` line 106, `tests/test_digest_unsubscribe.py`
  (all 8 tests, none differential)

---

## Summary

- **165/165 backend tests pass**, independently re-confirmed with both
  `python -m pytest -v` and plain `pytest -q` from `dev/backend/` —
  matches code-agent's and the orchestrator's reports exactly. Not a
  zero-test suite; genuine assertions throughout, spot-checked by reading
  test bodies rather than trusting test names.
- **§7-I (items 30–32): genuinely covered**, including a real
  fixture-injection test for item 31 (verified by reading the test body —
  it deep-copies the real catalog, injects a real denylisted category,
  writes it to a temp file, and asserts the real filter function excludes
  it from its output; this is not "the shipped catalog happens to be
  clean").
- **§7-J items 33, 34, 35, 36: genuinely covered**, with two minor,
  non-blocking gaps (401-on-every-route only spot-checked on `/profiles`
  rather than every route; invite code format/entropy not directly
  asserted).
- **§7-J item 37: PASS (decided, not defaulted).** The pytest-level
  regression alone does not re-exercise the 8 R1–R8 adversarial prompts
  (confirmed by grep — none of that content exists in the pytest suite),
  so taken in isolation this suite's own evidence would only support
  "PARTIAL." But the red-team-bias suite (its rightful owner) explicitly
  reviewed and reasoned through this exact question at the code level
  (`test-evidence/red-team-bias-increment3-2026-07-11.md`) and reached a
  documented PASS: the auth dependency sits upstream of, and does not
  alter, the unchanged `enforce()`/prompt-construction code path a live
  re-run would be testing, so re-spending live-LLM budget re-verifies a
  hypothesis Increment 1's live rerun already settled. Combined, item 37
  is a decided cross-suite PASS, not an unresolved gap.
- **Judgment call (plaintext `unsubscribe_token` column): implementation
  is sound by code inspection, but no differential test locks in
  "hash-only verification" as a structural guarantee** — a real,
  non-blocking testing-coverage gap.

## Gate verdict

**PASS, conditional on the two suites' evidence being read together.**
This unit/integration suite alone (165/165 tests, §7-I fully covered,
§7-J items 33/34/35/36 fully covered) does not, by itself, prove item
37's literal live-adversarial-re-run claim — and this evidence file
initially flagged that as an open gap before checking whether the
red-team-bias suite (item 37's rightful owner alongside this suite) had
separately addressed it. It had, with an explicit, code-level, reasoned
decision (not a default or an oversight) to skip the live re-run this
increment and why. Reading both suites together: item 37 is genuinely,
non-silently satisfied. No override is required for item 37 specifically.
The two minor gaps this suite independently found (per-route 401
spot-check breadth on `/profiles` only; invite code format/entropy not
directly asserted; the unsubscribe-token plaintext-vs-hash differential
test missing) remain real, non-blocking, recommended follow-ups for
code-agent — they do not block this gate on their own, but should not be
silently dropped either.

This suite (unit/integration) is recorded as **blocking** per this
project's default policy — no suite has been marked advisory in
PROJECT_CONTEXT.md's Active Team section.


## Note: repo state changed mid-review (untracked file, not part of this gate's 165)

While drafting this evidence, a re-run of the suite showed
`dev/backend/tests/test_route_signatures.py` now present (untracked in
git, mtime after this review's initial 165/165 confirmation run) with
**2 failing tests**: `test_family_parameter_annotation_and_kind_are_the_declared_shape`
and `test_get_current_family_returns_a_family_and_is_the_only_seam_function`.
Full re-run: `168 collected, 166 passed, 2 failed`. This file is not part
of code-agent's reported 165-test Increment-3 deliverable (it isn't in
the git history — `git log` shows the last four commits are code-agent's
Increment-3 work, F10/F9/F8/frontend, none touching this file), and its
two failures are a `from __future__ import annotations`/string-annotation
comparison issue (`annotation is Family` fails because postponed
evaluation makes the runtime annotation the string `'Family'`, not the
class) — appears to be a test-authoring bug in the new file itself
(comparing against a live class without `typing.get_type_hints()`
resolution) rather than a real regression in `app/auth.py`'s
`get_current_family` contract, but this was not this suite's task to
diagnose further. Reported here as a current-state fact, not folded into
this gate's 165/165 pass/fail count above, since it falls outside the
scope this task was given (code-agent's Increment 3 report) and appears
to be a concurrent, uncommitted addition by a different process/agent
mid-review. Recommend the orchestrator confirm ownership and intent of
this file before the gate closes.
