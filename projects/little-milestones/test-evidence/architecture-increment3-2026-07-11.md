# Architecture suite — Increment 3 (Test gate), little-milestones

Owner: solution-architect. Fourth attempt at this evidence file (attempts
1-3 crashed mid-response due to transient API connectivity errors, unrelated
to the task; `knowledge/ARCHITECTURE_KB.md` was confirmed untouched/intact
after every crash — zero git diff, still 941 lines — and is **not** touched
this pass either, per the task's instruction to minimize crash risk near
that file).

## Carried-forward conclusions (established in prior attempts, not re-verified this pass)

1. **Auth seam contract test** (`dev/backend/tests/test_route_signatures.py`)
   is meaningful and adequate: it locks in the shape of the auth dependency
   seam (`Depends(get_current_family)` / `Depends(require_owner)`) that every
   route handler relies on. Full suite: **168/168 passing**.
2. **CPSC serve-time filter** in `products.py` is genuinely re-evaluated
   per-request against `cpsc_denylist.json` — confirmed not cached/pre-filtered
   at write time, so a denylist update takes effect on the very next request
   without any data migration or reprocessing step.
3. **§0's component map matches the shipped file layout exactly**, including
   the plaintext `unsubscribe_token` column existing alongside
   `unsubscribe_token_hash` in the `users` table — the flagged deviation from
   ARCHITECTURE_KB's original hash-only design, addressed in item 3 below.

## New items checked this pass

### 1. `tests/test_email_delivery.py` — exists, meaningfully tests F8 email shape

**Confirmed adequate.** File read in full (108 lines, 8 test functions,
mocks `app.email_delivery.requests.post` throughout — no real network call
ever made, consistent with ARCHITECTURE_KB §5.1/§5.2/§5.7).

- **`List-Unsubscribe`/`List-Unsubscribe-Post` headers**:
  `test_send_digest_notification_calls_resend_with_correct_shape` asserts
  `payload["headers"]["List-Unsubscribe"] == "<http://api/digest/unsubscribe?token=abc>"`
  (correctly angle-bracket-wrapped per RFC 8058) and
  `payload["headers"]["List-Unsubscribe-Post"] == "List-Unsubscribe=One-Click"`
  — both asserted at the exact header-value level, not just presence.
- **No child-identifying content in body**:
  `test_email_body_has_no_child_identifying_content` asserts the rendered
  HTML never contains a name ("maya"), an age phrase ("months old",
  "corrected age", "months corrected"), or a specific milestone claim
  ("walking by") — this is the direct architectural answer to §5.7's privacy
  guarantee (digest emails are notification-only, no PHI/child data ever
  leaves the app boundary via email).
- **Fixed subject line**: `test_email_subject_is_fixed_and_content_free`
  asserts the exact string `"Your weekly little-milestones update is ready"`
  — a hardcoded, content-free subject, correctly excluding any
  personalization vector.
- Bonus coverage beyond the three requested items, also meaningful: no
  tracking pixel (`test_no_open_or_click_tracking_pixel_in_body`, checks for
  absence of `<img` tags), CAN-SPAM mailing-address placeholder flagged as
  still a placeholder (not silently shipped as real), and a non-2xx Resend
  response correctly raises rather than swallowing the failure.

**Verdict on this item: adequate, no gaps.**

### 2. `tests/test_scheduler.py` — exists, meaningfully tests due-check logic

**Confirmed adequate.** File read in full (153 lines). The due-check
predicate under test is `UserStore.list_due_for_digest()`, exercised via a
real `test_db` SQLite fixture (not mocked at the query level — only
`email_delivery.send_digest_notification` and the real APScheduler network
path are mocked).

Five tests directly cover the exact property specified — "a user is selected
iff `digest_opt_in=true` AND (`last_digest_sent_at` is null OR ≥7 days old)":

- `test_due_check_selects_opted_in_never_sent` — opted-in + null →
  selected.
- `test_due_check_excludes_opted_out` — opted-out + null → not selected
  (isolates the `digest_opt_in` conjunct).
- `test_due_check_excludes_recently_sent` — opted-in + 2 days ago → not
  selected (isolates the recency conjunct below threshold).
- `test_due_check_includes_sent_over_seven_days_ago` — opted-in + 8 days ago
  → selected.
- `test_due_check_boundary_exactly_seven_days_is_due` — opted-in + exactly 7
  days ago → selected, confirming the boundary is inclusive (`>=`, not `>`)
  as specified.

This is a proper truth-table decomposition of the two-conjunct predicate,
including the boundary case explicitly — not just a couple of happy-path
examples. Additional tests beyond the strict ask, also architecturally
relevant: `run_digest_job` end-to-end (sends only to due users, updates
`last_digest_sent_at` only on success), per-user isolation on failure (one
user's send exception doesn't block others', matches §5.3 step 3's "no
explicit retry logic needed, naturally retried next day" design), a user
with no unsubscribe token fails gracefully rather than crashing the whole
job, no email address leaks into error logs, and a real (not mocked)
APScheduler start/shutdown lifecycle test with idempotent double-start
protection.

**Verdict on this item: adequate, no gaps.**

### 3. Architectural agreement on plaintext `unsubscribe_token` column

security-architect's `test-evidence/security-increment3-2026-07-11.md`
item 10 concludes: **acceptable as a trade-off**, with the precise framing
that severity ceiling is unchanged (worst case is still "flip
`digest_opt_in` to false," never account/data access) but that read-only
DB-file-compromise blast radius is narrowly widened (a hash-only column
would have been useless to a read-only attacker; the plaintext column is
directly replayable against the public unsubscribe endpoint, in bulk).
They recommend a formal SECURITY_KB.md addendum recording this, and flag
Fernet-encrypting the column (using the already-established
`PHOTO_ENCRYPTION_KEY` pattern) as a worthwhile future hardening, not a
Code-gate blocker, given F8 is not even enabled in this environment
(`ENABLE_DIGEST_SCHEDULER=false`).

**Architectural agreement: YES.** From a component-boundary/design-conformance
standpoint, this reasoning is sound: the plaintext column is a targeted,
single-purpose exception to §0's original hash-only design, its blast radius
is structurally bounded to a single boolean column via
`unsubscribe_by_token_hash()`'s single-column UPDATE (no broader query
surface was introduced), and the DB file is already an accepted
plaintext-PII surface for this MVP per §2.2 — so this doesn't change the
file's overall risk classification, only marginally extends what's already
inside it. I don't see a design-integrity reason to block on it.

**Flagged follow-up for a future pass (not done this pass, per instruction):**
`ARCHITECTURE_KB.md` §0's component map (or a new short subsection near it)
should get an explicit note recording that the `unsubscribe_token` /
`unsubscribe_token_hash` pair is a deliberate, reviewed deviation from the
original hash-only design — both to avoid a future reader mistaking the
current inline `db.py` comment + Decisions Log entry as the last word, and
to co-locate with whatever addendum security-architect adds to
SECURITY_KB.md so the two documents don't drift apart on the same fact.

## Overall gate verdict

**Architecture suite: APPROVE.**

- Blocking findings: **none.**
- Non-blocking findings:
  1. `ARCHITECTURE_KB.md` should get a short addendum near §0 recording the
     `unsubscribe_token` plaintext-column deviation and this role's
     agreement with security-architect's trade-off assessment — deferred to
     a future pass, not required before this gate closes (§0's component map
     already matches the shipped layout exactly, including this column per
     carried-forward conclusion 3, so nothing is currently *inconsistent* —
     this is a documentation completeness gap, not a design defect).
  2. No disagreement with security-architect to surface at this gate — both
     roles independently reach "acceptable trade-off," with
     security-architect's write-up carrying the more precise blast-radius
     reasoning; nothing here contradicts it.

Full suite count (carried forward from conclusion 1): **168/168 passing.**
