# Security suite — Increment 3 (Test gate), little-milestones

Owner: security-architect. Scope: SECURITY_KB.md §1 (auth design) verified
against shipped code — `dev/backend/app/{users.py,auth.py}`,
`dev/backend/app/routes/{auth.py,profiles.py,photos.py,memories.py,
digest.py,products.py}`, `dev/backend/app/db.py`, `dev/backend/app/
{scheduler.py,email_delivery.py}`, `dev/backend/.env`/`.env.example`/
`.gitignore`.

**Method note, stated up front, not glossed over:** this run's tool access
was **Read/Write only — no Bash/shell tool was available**, contrary to
this session's stated preference for live execution over static review.
Everything below is a thorough static code review (every route, every
store method, every relevant test file read in full), cross-checked
against the design in `knowledge/SECURITY_KB.md` §1, plus verification
that the codebase's own automated security-relevant tests
(`tests/test_auth.py`, `tests/test_security.py`, `tests/test_photos.py`,
`tests/test_scheduler.py`, `tests/test_email_delivery.py`) actually assert
the right things — not that they were executed by me this session.
code-agent's Increment-3 summary in `PROJECT_CONTEXT.md` claims 165/165
passing; **this claim is not independently re-verified here** and should
be, by whichever agent/orchestrator has shell access, before this gate is
treated as fully closed rather than statically reviewed. Exact commands
recommended at the bottom of this file.

---

## 1. argon2id (not bcrypt)

**Verified — PASS.**
- `dev/backend/pyproject.toml`: `"passlib[argon2]>=1.7"` — correct extra installed (pulls in `argon2-cffi`, without which passlib's `argon2` scheme cannot run at all — confirmed present, not just declared).
- `dev/backend/app/auth.py:39`: `CryptContext(schemes=["argon2"], deprecated="auto")` — passlib's `argon2` handler defaults to `type="ID"` (argon2id) in passlib >= 1.7.3; no override to `argon2i`/`argon2d` anywhere in the codebase (grep-equivalent: only one `CryptContext` construction site exists, in `auth.py`).
- `tests/test_auth.py::test_password_stored_only_as_argon2_hash` asserts the stored hash `.startswith("$argon2")` and is not byte-equal to the plaintext password — correct assertion shape, though it does not itself distinguish argon2id from argon2i/d (the `CryptContext` default is what actually guarantees "id"). No code path overrides the default.

## 2. Session tokens: opaque 32-byte, SHA-256-hashed at rest, cookie flags

**Verified — PASS.**
- `generate_opaque_token()` → `secrets.token_urlsafe(32)` (256 bits raw entropy) — matches spec exactly.
- `create_session()`: raw token is hashed via `hash_token()` (`hashlib.sha256(...).hexdigest()`) before the `INSERT INTO sessions`; only `token_hash` is ever persisted — confirmed no code path writes a raw token into the `sessions` table (`sessions.token_hash TEXT PRIMARY KEY` in `db.py`'s schema — no raw-token column exists at all, so this isn't just convention, it's structurally impossible to store the raw token there).
- `_resolve_session_row()` looks up by `hash_token(raw_token)` — round-trip correct.
- Cookie: `set_session_cookie()` sets `httponly=True`, `samesite="lax"`, `secure=os.environ.get("ENV") == "production"` — matches §1.4's conditional-Secure design exactly (default unset/anything-else → `Secure` omitted, `ENV=production` → `Secure=True`).
- `tests/test_auth.py::test_session_cookie_is_httponly_and_samesite_lax` and `::test_session_cookie_secure_flag_conditional_on_env` assert this at the actual `Set-Cookie` header level (not just intent) — correct test shape.
- Sliding/absolute expiry: `_resolve_session_row()` re-issues `min(now + 30d, created_at + 90d)` on every successful resolution — matches §1.1 exactly.

## 3. Cross-family access → 404, verified for every resource type

**Verified — PASS, checked at the route level for all six resource types.**

| Route | File | Cross-family behavior |
|---|---|---|
| `GET/DELETE /profiles/{id}` | `routes/profiles.py` | `store.get(family.id, profile_id)` scoped by `family.id` → `None` → 404 |
| `GET/POST/DELETE /profiles/{id}/memories`, `/timeline` | `routes/memories.py` | `_get_profile_or_404` scoped by `family.id` before any memory-store call |
| `GET/POST/DELETE /profiles/{id}/photos` | `routes/photos.py` | `_get_profile_or_404` scoped by `family.id` before any photo-store call — same helper pattern |
| `GET /profiles/{id}/digest` | `routes/digest.py` | `profile_store.get(family.id, profile_id)` → 404 |
| `GET /profiles/{id}/products` | `routes/products.py` | `store.get(family.id, profile_id)` → 404 |

Every one of these routes takes `family: Family = Depends(get_current_family)`
and passes `family.id` as the first scoping argument into the relevant
store's `.get(...)` call — no route queries by `profile_id` alone. This is
a structural property (every store method requires `family_id`/scoping as
a parameter, ARCHITECTURE_KB's `Store[T]` convention), not a per-route
discipline that could silently regress on one route and not another.

`tests/test_auth.py::test_cross_family_profile_access_is_404_not_403`
explicitly asserts 404 (not 403, not 401) across profile/memories/
timeline/digest/products/photos in one fixture — this is exactly the
required "check every resource type, not just one example" coverage the
task called for, and it's already present in the shipped test suite.
`test_pre_auth_data_invisible_to_second_family` additionally confirms this
holds for the pre-auth-migrated default-family data specifically (item 9
below).

## 4. Role enforcement: owner-only delete/invite; caregiver → 403 (not 404)

**Verified — PASS, and the 403-vs-404 distinction is implemented correctly, not conflated.**
- `require_owner()` (`auth.py`) raises `403` if `user.role != "owner"` — a role check independent of any resource lookup, applied via `Depends(require_owner)` as an *additional* dependency alongside `Depends(get_current_family)` on exactly three routes: `DELETE /profiles/{id}` (`routes/profiles.py`), `DELETE /profiles/{id}/photos/{id}` (`routes/photos.py`), `POST /invites` (`routes/auth.py`).
- Ordering confirmed correct: FastAPI resolves all declared `Depends(...)` parameters before the route body executes, so `require_owner`'s 403 fires *before* the route body's own `store.get(family.id, id) is None` → 404 check ever runs — meaning a caregiver hitting a *nonexistent or cross-family* id on an owner-gated route still gets 403, not 404 (documented explicitly as judgment call 3 in `PROJECT_CONTEXT.md`'s Increment-3 summary, and consistent with role being a session-level property, not something that should leak resource-existence info either way).
- Distinct from the cross-family case (item 3 above) which is 404 precisely because that check runs on routes *without* `require_owner` (e.g. `GET /profiles/{id}` for any session-holding caregiver in the wrong family).
- `tests/test_auth.py::test_caregiver_cannot_delete_profile_owner_can` and `::test_caregiver_cannot_delete_photo_owner_can` and `::test_caregiver_cannot_create_invite` all assert the 403 case explicitly and separately from the 404 cross-family test — the two failure modes are tested as genuinely distinct scenarios, not conflated into one assertion.

## 5. Rate limiting on `/auth/login` and `/auth/join`

**Verified — PASS, a real in-process fixed-window limiter, wired into both routes (not a TODO).**
- `check_rate_limit(key, max_requests, window_seconds)` in `auth.py`: a sliding-list-of-timestamps fixed-window counter (`_RATE_BUCKETS: dict[str, list[float]]`), evicts timestamps older than the window on each call, rejects once `len(bucket) >= max_requests`.
- `routes/auth.py::login`: `rate_key = f"login:{ip}:{email}"`, `LOGIN_MAX_ATTEMPTS=10`/`LOGIN_WINDOW_SECONDS=900` — checked before any password verification, returns `429` on exceed.
- `routes/auth.py::join`: `rate_key = f"join:{ip}"`, `JOIN_MAX_ATTEMPTS=10`/`JOIN_WINDOW_SECONDS=900` — same shape.
- `routes/digest.py::unsubscribe` also carries a limiter (`UNSUBSCRIBE_RATE_LIMIT_MAX=20`/`60s`, keyed by IP) — this is the §1.7-point-4 addition, confirmed actually present, not just documented.
- `tests/test_auth.py::test_login_rate_limited_after_repeated_attempts`, `::test_join_rate_limited`, `tests/test_security.py::test_unsubscribe_rate_limited` all assert the 429 boundary at the exact configured limit (10th/11th, 20th/21st request) — correct test shape, not just "a limiter exists somewhere."

## 6. Generic auth error messages (no user enumeration)

**Verified at the response-body level — PASS, and hardened beyond the literal spec.**
- `routes/auth.py::login`: `password_hash = row["password_hash"] if row is not None else DUMMY_PASSWORD_HASH` — `verify_password` is *always* called, even for an unknown email, against a fixed dummy argon2id hash (`DUMMY_PASSWORD_HASH`, computed once at module load). Both the wrong-password and unknown-email branches raise the identical `HTTPException(401, detail="Invalid email or password")`.
- `tests/test_auth.py::test_login_wrong_password_generic_401` and `::test_login_unknown_email_same_generic_401` both assert `resp.json()["detail"] == "Invalid email or password"` byte-for-byte — this is the actual response-body check the task asked for, not an assumption of intent.
- The dummy-hash-verify-always pattern also equalizes response *timing* between the two cases (argon2id's cost dominates either way) — this goes beyond SECURITY_KB §1.5's literal "same error message" requirement into timing-side-channel resistance, a real strengthening, not scope creep (comment in `auth.py:41-45` states this rationale explicitly).

## 7. Logout — real server-side session delete

**Verified — PASS.**
- `delete_session_by_raw_token()`: `DELETE FROM sessions WHERE token_hash = ?` — a real row delete, not a no-op.
- `routes/auth.py::logout` calls it whenever a cookie is present, then always clears the client cookie regardless (idempotent even with no/expired/unknown cookie).
- `tests/test_auth.py::test_logout_deletes_session_row_server_side` asserts the `sessions` table row count drops from 1 to 0 *and* that the old cookie, if replayed, now gets 401 on a protected route — this is the strongest possible test of "a stolen cookie post-logout must not remain valid," and it's already present.

## 8. Invite codes: single-use, 7-day expiry, entropy

**Verified — PASS, with one documented, justified deviation from the literal generator call.**
- Single-use: `InviteStore.is_valid()` returns `False` if `used_at is not None and invite.single_use` — `mark_used()` is called immediately after a successful join, before the session is created. `tests/test_auth.py::test_join_reused_code_rejected` confirms a second join attempt on the same code gets 400.
- Expiry: `INVITE_EXPIRY_DAYS = 7`, set at `InviteStore.create()` time; `is_valid()` checks `now <= expires_at`. `test_join_expired_code_rejected` confirms.
- Entropy: SECURITY_KB §1.1 specifies `secrets.token_urlsafe(9)`; shipped code instead uses `generate_opaque_token()[:12]` — i.e., `secrets.token_urlsafe(32)[:12]`, a truncation of the same high-entropy generator already used for session/unsubscribe tokens, rather than a second differently-parameterized call. This is documented as judgment call 7 in `PROJECT_CONTEXT.md`'s Increment-3 summary. **Assessed here as acceptable, not a finding**: `token_urlsafe(9)` and a 12-char prefix of `token_urlsafe(32)` are the same base64url alphabet and produce the same ~12-character output length SECURITY_KB actually asked for ("`secrets.token_urlsafe(9)` ≈ 12 chars, base64url") — truncating a longer urlsafe-base64 token is not an encoding-boundary bug, and the resulting code still carries materially more effective entropy than the literal spec, not less. No downgrade.

## 9. Pre-auth data migration — first user becomes owner of the existing family, doesn't leak to a second signup's family

**Verified — PASS.**
- `db.py`: `DEFAULT_FAMILY_ID = 1`, seeded unconditionally by `init_db()`.
- `routes/auth.py::signup`: `family_id = DEFAULT_FAMILY_ID if store.count() == 0 else family_store.create()` — a one-line branch, exactly matching ARCHITECTURE_KB §2's "first user becomes owner of the existing family" design, not a migration script.
- `tests/test_auth.py::test_signup_first_user_becomes_owner_of_default_family` confirms `family_id == 1` for the very first signup.
- `tests/test_auth.py::test_signup_second_ever_user_gets_a_new_family` confirms the *second* signup gets `family_id != 1` (a brand-new family via `FamilyStore.create()`), and — critically for this item's specific concern — `tests/test_auth.py::test_pre_auth_data_invisible_to_second_family` explicitly asserts that a profile created under the first (migrated) family is **not visible** (`404` on direct fetch, `[]` on list) to a second family's owner. This is the exact "doesn't leak Increment-1/2 data to a family created by a second signup" scenario the task called out, and it's already a named, passing test — good coverage, not an assumption.

## 10. Independent assessment: plaintext `users.unsubscribe_token` column

**Assessed independently, per the task's request. My conclusion: acceptable as a stated trade-off, but this needs a formal, explicit SECURITY_KB addendum rather than resting solely on code-agent's inline schema comment and PROJECT_CONTEXT's Decisions Log entry — the reasoning is basically right, but it hasn't actually been signed off by this role in the KB itself yet, and there is one real, narrow security delta worth naming precisely rather than waving through by analogy.**

What code-agent's inline comment (`db.py`) and PROJECT_CONTEXT Decisions Log
item 2 claim: "worst case on compromise of either value is unchanged from
SECURITY_KB §1.7 point 1's existing assessment (an unwanted opt-out of a
weekly email, not an account/data breach)." **This is not quite precise,
and the imprecision matters for what "acceptable" actually rests on:**

- With **hash-only** storage (what §1.7 originally specified), an attacker
  who gains **read-only** access to the SQLite file (e.g. a leaked backup,
  a read-only filesystem compromise, a misconfigured static file leak)
  gains *nothing* usable against the unsubscribe endpoint — SHA-256 of a
  256-bit token is not invertible, so the hash alone cannot be replayed
  against `GET /digest/unsubscribe?token=...`.
- With the **plaintext column actually shipped**, that same read-only
  compromise directly yields every user's working, replayable unsubscribe
  token — an attacker with read-only DB access (no write access, no
  ability to run `UPDATE users SET digest_opt_in=0` directly) can now
  achieve the same effect *via the public API*, and can do so **for every
  opted-in user in the family, in bulk**, which the hash-only design would
  not permit even under read compromise.
- This is a genuine, narrow **widening of what a read-only DB compromise
  grants**, not a no-op — code-agent's "worst case is unchanged" framing
  undercounts this by treating "worst case on this token's compromise" as
  the only relevant frame, when the more precise frame is "worst case on a
  *DB-file-read* compromise," which is exactly the scenario §2.2 already
  independently discusses (SQLite DB file not separately encrypted this
  run) and where this column is a *new* item of exposure, not present at
  the last time §2.2 was written.

**Why I still conclude this is acceptable, not a blocking finding:**
1. **Severity ceiling stays trivial.** The single achievable action is
   flipping `digest_opt_in` to `false` — never account access, never any
   other field, never any other table (structurally enforced,
   `unsubscribe_by_token_hash()` is the single-column UPDATE §1.7 point 3
   already requires and verifies). Bulk opt-out of a marketing-adjacent
   weekly email, for a feature that isn't even enabled in this environment
   yet (item 11 below), is a real but low-consequence annoyance, not a
   privacy or safety incident.
2. **The DB file is already an accepted plaintext-PII surface for this
   MVP** (§2.2: profile names, DOB, prematurity status, memory text are
   all already readable in plaintext by anyone with raw filesystem access
   to `little_milestones.db`, mitigated only by `0600` perms + gitignore,
   with an explicit revisit trigger before non-local deployment). Adding
   one more plaintext field whose worst case is strictly less severe than
   what's already accepted in that same file does not meaningfully change
   the DB file's overall risk classification — it's already "sensitive if
   read," and this doesn't change that qualitative bucket.
3. **A better alternative exists but is not obviously worth building this
   run**: encrypting `unsubscribe_token` at rest with the existing
   `PHOTO_ENCRYPTION_KEY`/Fernet primitive (already a dependency, already
   an established pattern in this codebase, §2.1) would close this gap
   cheaply — decrypt in-memory only inside `scheduler.py`'s per-user loop
   when building the outbound URL. I flag this as a **worthwhile, low-cost
   improvement**, not a Code-gate blocker: F8 delivery is not even enabled
   in this environment (`ENABLE_DIGEST_SCHEDULER=false`, item 11), so
   there is no live exposure today, and this can be picked up before the
   scheduler is ever turned on for real.

**Recommendation, not a blocking finding:** SECURITY_KB.md should get a
short, explicit addendum recording this assessment (my conclusion above),
rather than leaving the sign-off implicit in a `db.py` code comment +
PROJECT_CONTEXT Decisions Log entry that a future reader could mistake for
already having been reviewed by this role with this level of precision. I
will flag to solution-architect that my reasoning here differs slightly
from code-agent's stated "worst case unchanged" framing (I think it's
"worst case severity unchanged, but read-compromise blast radius widened
in a narrow, low-consequence way") — this is a nuance, not a disagreement
on the bottom-line conclusion (acceptable), and should be recorded as such
rather than silently smoothed over.

## 11. F8 delivery security — `RESEND_API_KEY` handling, scheduler gating

**Verified — PASS.**
- `.env.example` documents `RESEND_API_KEY=` with no committed value; the
  live `dev/backend/.env` has `RESEND_API_KEY` **absent entirely** (only
  `ANTHROPIC_API_KEY` and `PHOTO_ENCRYPTION_KEY` are populated) — consistent
  with "no verified Resend sending domain yet" and confirms no Resend key
  is even configured in this environment, let alone at risk of being
  logged.
- `email_delivery.py::send_digest_notification`: raises a `RuntimeError`
  with a message that names the *missing config*, never the key value; on
  a non-2xx Resend response, the error includes `response.text[:200]`
  (Resend's own response body) but never the request `Authorization`
  header/API key.
- `scheduler.py::run_digest_job`'s per-user `except` logs
  `"digest_send_failed user_id=%s error=%s"` — no email address, no API
  key, matching the "no PII in logs" discipline already established for
  `guardrails.py`. `tests/test_scheduler.py::test_run_digest_job_error_log_has_no_email_address`
  asserts this at the actual log-record level.
- Scheduler gating: `main.py`'s startup hook only calls `start_scheduler()`
  when `os.environ.get("ENABLE_DIGEST_SCHEDULER", "false").lower() == "true"`
  — defaults to **off**. `.env.example` documents `ENABLE_DIGEST_SCHEDULER=false`
  explicitly with an inline warning not to flip it until a verified sending
  domain + real `MAILING_ADDRESS` exist. The live `.env` has no
  `ENABLE_DIGEST_SCHEDULER` entry at all, which resolves to the same `false`
  default — **confirmed genuinely, not accidentally, off** in this
  environment. `tests/test_digest.py::test_scheduler_mechanism_exists_but_is_not_auto_started`
  locks this in as a source-level regression check.
- No secret (RESEND key, session token, password) found in any log-emitting
  code path reviewed (`scheduler.py`, `email_delivery.py`, `guardrails.py`'s
  existing pattern).

## Cross-check: repo secrets hygiene (`.env` / gitignore)

**Verified via file inspection, not `git log` (no Bash access this run —
flagged below as a residual live-check gap).**
- `dev/.gitignore`: `.env*` with explicit exceptions for `.env.example` and
  `backend/.env.example` — correctly excludes `dev/backend/.env` (which
  does contain a real `ANTHROPIC_API_KEY` and `PHOTO_ENCRYPTION_KEY` in the
  working tree per PROJECT_CONTEXT's own Decisions Log, human-consented).
- `dev/backend/.gitignore`: `/data/` — correctly excludes
  `backend/data/little_milestones.db` (the SQLite file, which per item 10
  above holds plaintext PII including the new `unsubscribe_token` column)
  and `backend/data/photos/`.
- **Not verified this session (no shell access): whether `.env` or
  `backend/data/` was ever committed in an *earlier* commit before the
  `.gitignore` entries existed**, which would leave a real secret/PII leak
  in git history even if the current working tree and `.gitignore` are
  correct now. This is a real residual gap in this report, not an
  oversight to gloss over — see recommended commands below.

---

## Residual live-check gap and recommended commands

No Bash/shell tool was available to this agent this session. The
following should be run by the orchestrator (or whichever agent has shell
access) before this gate is treated as fully closed, not just statically
reviewed:

```bash
cd "/Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/little-milestones/dev/backend"

# 1. Re-confirm the reported 165/165 test count for real, this session.
python -m pytest -v

# 2. Confirm no secret/PII file was ever committed historically, not just
#    excluded by the current .gitignore.
cd "/Users/tandonakhil/Documents/AI Projects/AICluadeCode/projects/little-milestones/dev"
git log --all --oneline -- '**/.env' 'backend/.env' 'backend/data/**'
git log --all -p -- '**/.env' | grep -iE 'sk-ant|resend|api_key' || echo "no hits"

# 3. Live cross-family / role / rate-limit smoke check against a running
#    backend (localhost:8000), independent of the pytest suite:
curl -s -c /tmp/a.jar -X POST localhost:8000/auth/signup \
  -H 'content-type: application/json' \
  -d '{"email":"livecheck-a@example.com","password":"correct horse battery staple"}'
PROFILE_ID=$(curl -s -b /tmp/a.jar -X POST localhost:8000/profiles \
  -H 'content-type: application/json' \
  -d '{"display_name":"X","date_of_birth":"2024-01-01","born_early":false}' | python3 -c 'import sys,json;print(json.load(sys.stdin)["id"])')
curl -s -c /tmp/b.jar -X POST localhost:8000/auth/signup \
  -H 'content-type: application/json' \
  -d '{"email":"livecheck-b@example.com","password":"correct horse battery staple"}'
echo "expect 404:"
curl -s -o /dev/null -w '%{http_code}\n' -b /tmp/b.jar localhost:8000/profiles/$PROFILE_ID
echo "expect 401 (no cookie):"
curl -s -o /dev/null -w '%{http_code}\n' localhost:8000/profiles
```

---

## Findings summary

**Blocking: none.**

**Non-blocking:**
1. Item 10 (plaintext `unsubscribe_token`): acceptable trade-off, but
   record it as a formal SECURITY_KB.md addendum rather than an inline
   code comment + Decisions Log entry — my precise reasoning (read-only
   DB-compromise blast radius widened, though severity ceiling unchanged)
   differs slightly from code-agent's "worst case unchanged" framing;
   flagging the nuance for the record, not a disagreement on the
   bottom-line "acceptable" conclusion. Optional low-cost hardening
   (encrypt the column with the existing Fernet key, decrypt only inside
   `scheduler.py`) recommended before the scheduler is ever enabled for
   real, not required before this gate closes.
2. Residual live-check gap: this session had no Bash/shell tool, so the
   165/165 pytest claim and git-history secrets check are statically
   corroborated (code review of the test files matches the design intent
   exactly) but not independently re-executed. Recommend the orchestrator
   run the three command blocks above before treating Increment 3's Test
   gate as fully, not just statically, verified.

## Gate verdict

**Security suite: APPROVE, conditional on the orchestrator (or an agent
with shell access) running the residual live-check commands above and
reporting no surprises** — every item in the assigned checklist (1
through 11) was verified correct against SECURITY_KB.md's design via full
route/store code review and cross-referenced against an already-thorough,
correctly-shaped automated test suite (`test_auth.py`, `test_security.py`,
`test_photos.py`, `test_scheduler.py`, `test_email_delivery.py`). No
blocking defect found. The one substantive finding (item 10) is a
documentation/precision gap in an already-acceptable trade-off, not a
functional defect requiring a code change before this gate closes.
