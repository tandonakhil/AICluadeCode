# SECURITY_KB — little-milestones

Maintained by: security-architect. Architecture gate, 2026-07-10, jointly
presented with solution-architect (`ARCHITECTURE_KB.md`) and advised by
responsible-ai-architect (`RESPONSIBLE_AI_KB.md`). Read alongside
`ARCHITECTURE_KB.md` (component shape) and `INDUSTRY_KB.md` (compliance
flags) — this file designs the security posture for what solution-architect
designed, it does not re-derive the component shape.

**Status: pending human approval.**

---

## 1. Authentication & Authorization Design

*(Dedicated, non-collapsible section per this role's contract — even where a
decision is "confirm the baseline," it is reasoned to here, not asserted.)*

### 1.1 Decision

**Real authentication is required, and is being built (Increment 3, behind
the Increment-1 seam) — this is not a "no auth needed" project.** Confirm
PLAN §4.6's baseline with the refinements below:

- Local email+password accounts (no OAuth/social login, no magic-link email).
- Password hashing: **argon2id** via `passlib[argon2]` (argon2id specifically,
  not bcrypt — argon2id is the current OWASP-recommended default and this is
  a greenfield project with no legacy-bcrypt constraint to honor).
- Server-side sessions: opaque random token (32 bytes,
  `secrets.token_urlsafe`), stored **hashed** (SHA-256 is sufficient for a
  session token — it's not a password, no need for a slow KDF) in the
  `sessions` table (ARCHITECTURE_KB §3), cookie carries the raw token.
- Cookie flags: `HttpOnly`, `SameSite=Lax`, `Secure` (conditional — see §1.4
  deployment note), 30-day sliding expiry re-issued on activity, absolute
  90-day cap.
- Roles: `owner` (created the family) / `caregiver` (joined via invite).
- Invites: single-use, expiring (7 days), random unguessable code
  (`secrets.token_urlsafe(9)` ≈ 12 chars, base64url — sufficient entropy
  against online guessing given rate-limiting, §1.5).
- Cross-family access returns **404, not 403** — do not confirm a resource's
  existence to a session that doesn't own it (PLAN's own instinct, confirmed
  correct here: this is a real information-disclosure control, not just
  tidiness — it prevents a caregiver in family B from learning that
  `profile_id=17` exists in family A at all).

### 1.2 Criteria evaluated to reach this decision

Per this role's contract, the reasoning must be checkable against the
project's actual attributes, not asserted:

| Criterion | This project's attribute | Weight toward auth |
|---|---|---|
| Multi-tenancy? | **Yes, by design** — F10 is explicitly multiple caregivers per family, and the product's whole premise (INDUSTRY_KB §1.4 point 3) depends on family sharing. | Strong → auth required |
| PII / sensitive data? | **Yes, and of an unusually sensitive class** — a minor child's birthdate, health-adjacent data (`weeks_early`, corrected-age status, a text log of developmental moments), and photographs. DOMAIN_KB R6 and INDUSTRY_KB §2.1–2.2 both independently flag this as sensitive-by-domain-norm even where COPPA's formal consent machinery doesn't strictly attach (INDUSTRY_KB §2.1: "very likely outside COPPA's formal scope — but should behave as if the spirit applies"). | Strong → auth required |
| Network exposure beyond localhost? | The platform decision (PROJECT_CONTEXT.md, human-confirmed) is a **responsive web app**, not a localhost-only tool — "any browser, no install" is meaningless if the server only binds to `127.0.0.1`. Even at MVP/local-target-environment, the intent is a real deployable web app, and target environment for this run is `local` per PROJECT_CONTEXT but that is a deployment-staging decision, not a permanent architecture constraint — cloud-dev/cloud-prod are explicitly on the roadmap (admin/ROADMAP.md), not ruled out. | Strong → auth required (see §1.4 for what changes if/when it deploys beyond local) |
| Deployment target? | `local` today (PROJECT_CONTEXT.md "Target environment: local"), but F10's entire feature (inviting a *second household member*, e.g. a grandparent) only makes sense if the app is reachable by more than one person's device — "local" here means "not yet cloud-hosted," not "single machine, single user," and the human's own request ("multi-caregiver access") is incompatible with skipping auth regardless of hosting target. | Strong → auth required |

**Conclusion from the criteria table, not asserted independently of it:**
every criterion in this project's actual shape points toward auth being
required, and F10 is the human-approved feature that makes it concrete. This
is the textbook case this role's guardrail describes ("no auth needed for
local MVP is a legitimate conclusion... but must be reasoned to") reasoning
to the *opposite* conclusion correctly, not a default assumption that more
features always need more security.

### 1.3 What is deliberately NOT being built, and why (right-sizing, not gold-plating)

- **No OAuth/social login.** Google/Facebook/Apple sign-in would route a
  child-adjacent account signal through a third-party identity provider —
  exactly the kind of third-party data flow INDUSTRY_KB §2.2's "no third-
  party disclosure without separate consent" flag warns about, for a feature
  (login convenience) that has no corresponding requirement in the approved
  scope. Local email+password avoids it entirely, at the acceptable cost of
  no "sign in with Google" convenience.
- **No magic-link email.** Correctly deferred alongside F8's email
  infrastructure (ARCHITECTURE_KB §5) — building magic-link auth would force
  the email-infrastructure decision this gate is deliberately deferring, for
  a login mechanism that isn't materially safer than password+argon2id for
  this threat model (a stolen device with an open email client is arguably
  *worse* for magic-link than a stored password on the same device, given
  no MFA either way this run).
- **No MFA this run.** Flagged as a revisit trigger (§1.6), not built now —
  MFA adds real friction to a product whose retention model depends on
  near-zero friction (UX_KB §1.6, UXR-7's "loggable in ≤3 taps" ethos extends
  to login, not just memory-logging) for a threat model (family photo/memory
  data, not financial or medical-record-regulated data) that argon2id +
  session hygiene + rate-limiting (§1.5) meaningfully mitigates already.
- **Password reset:** deferred to a documented gap, not silently dropped.
  **This run ships without a self-service password-reset flow** (it would
  require the email infrastructure this gate defers). Mitigation: the
  Settings/family panel documents this plainly ("no password reset yet —
  losing your password means losing access to this account; ask another
  caregiver to invite you again into a fresh account, or contact us" — exact
  copy is ui-ux-designer's, this is the functional requirement). This is an
  accepted MVP gap, explicitly stated rather than glossed over, and is the
  first thing that should ship when email infrastructure is added.

  **Note (2026-07-10, §5 addendum below):** email infrastructure has since
  shipped (real delivery, per human override) without password-reset being
  re-scoped alongside it — this remains an accepted, still-open gap; §1.7
  below does not change this, since the unsubscribe token mechanism
  (§1.7) is a narrower, single-purpose capability, not a reusable password-
  reset primitive, and must not be repurposed as one.

### 1.4 Deployment-target sensitivity, stated explicitly

The `Secure` cookie flag and the entire session-cookie transport model
assume HTTPS in any non-local deployment. **Local dev today likely runs
plain HTTP** (`localhost`), so: `Secure` is conditionally set based on an
environment flag (`ENV=production` → `Secure=True`; local dev → omitted,
since browsers reject `Secure` cookies over plain HTTP and would silently
break local login). This is called out explicitly as **the one line in this
design that must be revisited, not just re-verified, before any non-local
deployment** (§1.6).

### 1.5 Supporting controls (not the core decision, but part of "auth design")

- **Rate limiting on `/auth/login`:** fixed-window limiter (e.g. 10
  attempts / 15 min per IP+email pair) to blunt credential-stuffing/brute-
  force against argon2id-hashed passwords — argon2id is slow by design, but
  a limiter is still cheap insurance and standard practice; implementation
  is an in-process counter (no external dependency needed at this scale,
  consistent with ARCHITECTURE_KB's "no new operational surface" instinct
  for a local-first app).
- **Invite-code rate limiting:** `/auth/join` limited similarly, since a
  12-char code is guessable-in-bulk without a limiter even at reasonable
  entropy.
- **Generic auth error messages:** login failure returns a single generic
  "invalid email or password" for both wrong-password and unknown-email
  cases (no user enumeration via differential error messages).
- **Session invalidation on logout is a real server-side delete of the
  session row**, not just a client-side cookie clear (a stolen cookie
  post-logout must not remain valid).

### 1.6 Explicit revisit triggers

This design must be revisited — not merely re-confirmed — when any of the
following occurs:

1. **Before any non-local (cloud-dev/cloud-prod) deployment**: confirm
   `Secure`/HTTPS enforcement is actually active end-to-end (not just
   toggled in config), reconsider MFA, and reconsider whether a managed
   session store becomes warranted at higher concurrency.
2. **Before password-reset ships**: this is the moment email infrastructure
   (ARCHITECTURE_KB §5) gets built for real, and reset-token design (single-
   use, short-expiry, rate-limited) needs the same rigor as invite codes.
   **Note (2026-07-10):** email infrastructure now exists (§5 addendum
   below), but password-reset itself has not been re-scoped — this trigger
   remains open, not retired by §5's delivery mechanism existing.
3. **If the user base or threat model changes** — e.g. if little-milestones
   ever adds any monetization, third-party integration, or data export/
   sharing beyond the family unit, re-evaluate whether password+session is
   still sufficient or whether OAuth/MFA earns its complexity at that point.
4. **If COPPA's 2025-amended-Rule applicability is ever re-assessed** (e.g.
   if the product ever becomes child-directed, or if a state
   Age-Appropriate-Design-Code determination changes) — re-run the §1.2
   criteria table, since a formal-applicability change could add consent-
   flow requirements auth doesn't currently need to carry.

### 1.7 Addendum, 2026-07-10 — independent review of the F8 unauthenticated unsubscribe route

solution-architect's revised `ARCHITECTURE_KB.md` §5 (real email delivery,
human override) introduces the project's first deliberately-unauthenticated,
credential-bearing route: `GET /digest/unsubscribe?token={raw_token}`
(design at ARCHITECTURE_KB §5.4–5.5). Per this role's re-engagement
contract ("always re-consulted on any enhancement or key design decision"),
this is independently assessed here — **additive to §1.1's decision, not a
replacement of it.**

**Assessment: the core design is sound, with two concrete additions required
before this is signed off as jointly approved, plus one point confirmed as
correct without change.**

1. **Is a stable, non-expiring, hashed per-user token the right call?
   Confirmed yes, given the capability's actual blast radius.** Unlike a
   session token or a password-reset token, this token grants exactly one
   capability — flip `digest_opt_in` to `false` on one specific row — never
   a session, never read access to any other data, never any other field.
   Worst case on token compromise (URL forwarded, browser history, a shared
   inbox) is an unwanted opt-out of a weekly notification email, not an
   account or data compromise. That severity profile does not justify
   single-use/expiring-token complexity (which, per ARCHITECTURE_KB §5.4,
   would also break the legitimate re-click case). This reasoning is the
   same class of proportionality judgment as §1.3's "no MFA this run" —
   right-sized to the actual capability, not gold-plated to session-token
   standards it doesn't need.

2. **Token entropy: confirmed consistent with existing session-token design,
   no change needed.** `secrets.token_urlsafe(32)` (32 bytes / 256 bits raw
   entropy) matches §1.1's session-token generation exactly, hashed at rest
   with SHA-256 (also matching §1.1's session-token-hash reasoning — not a
   password, no slow KDF warranted). At this entropy, offline/online
   brute-force of a single token is not a credible attack regardless of
   rate-limiting; rate-limiting below is recommended for a different reason
   (abuse resistance, not brute-force resistance).

3. **Scoping — "flips digest_opt_in and nothing else": the design as
   *described* is scoped correctly, but this must be enforced by
   implementation shape, not merely documented intent. Change required:**
   `routes/digest.py`'s unsubscribe handler must issue a narrowly-scoped,
   single-purpose write (e.g. `UPDATE users SET digest_opt_in = 0 WHERE
   unsubscribe_token_hash = ?`, or the `Store[T]`-pattern equivalent of the
   same single-column mutation) — **it must not be implemented by calling
   through a generic user-update/profile-patch function that happens to be
   invoked with only one field populated this time**, since that shape would
   make the "only this field" guarantee a matter of caller discipline rather
   than a structural property of the code path, and a future edit to the
   generic updater (e.g. adding a new mutable field) could silently widen
   what an unauthenticated request can change. This is the same "structural
   absence of the capability" standard ARCHITECTURE_KB §6.3 already applies
   to F9's product-recommendation path — applied here to the unsubscribe
   route. **New security-suite test required at Test gate:** attempt to
   pass extra fields/params on the unsubscribe request (e.g. an
   `email`/`role`/`family_id` field alongside the token) and assert no field
   other than `digest_opt_in` changes on the target row.

4. **Rate limiting / abuse resistance — currently absent from the design,
   change required.** ARCHITECTURE_KB §5.5 does not specify any rate limit
   on this route, and §1.5 above's existing limiters cover `/auth/login`
   and `/auth/join` only. Recommend: apply the same in-process fixed-window
   limiter pattern (§1.5) to `/digest/unsubscribe`, keyed by IP (e.g. 20
   requests/min/IP) — not because token brute-force is credible (point 2
   above rules that out), but for ordinary abuse/DoS resistance on any
   unauthenticated, no-login-required endpoint that performs a database
   write per request, consistent with treating every unauthenticated
   write-capable route the same way as a matter of policy, not case-by-case
   judgment. Low implementation cost (same limiter primitive already
   planned), so this is a small, right-sized addition, not new operational
   surface.

5. **GET-based token transport — confirmed acceptable, with one explicit
   constraint on the confirmation page.** RFC 8058's `List-Unsubscribe-Post`
   mechanism requires a URL-addressable, no-login endpoint, so a token in
   the URL is the standard (not a design mistake) — but URLs land in server
   access logs, and potentially in a `Referer` header if the page the token
   lands on makes any outbound request. ARCHITECTURE_KB §5.9 already
   confirms no tracking pixel/analytics on this flow, which covers most of
   this risk; the one thing to state explicitly and hold code-agent to: the
   confirmation page (§5.5) must contain **no external resource loads or
   outbound links** that could leak the token via `Referer` (the existing
   "Settings" link back into the app is same-origin and fine; anything
   third-party — e.g. a font CDN, an analytics snippet, a social-share
   button — would leak the raw token to that third party). This is a new,
   explicit constraint on `routes/digest.py`'s unsubscribe confirmation
   response, verified at Test gate alongside item 3's scoping test.

**Net assessment on item 1 (the unsubscribe route): approved, conditional on
items 3 and 4 above being implemented as stated — not a rubber stamp.**
Items 1, 2, and 5 are confirmed correct as designed with no change requested.

---

## 2. Photo storage & encryption-at-rest design (F7)

Confirms and completes PLAN §4.3's baseline, decides the parts PLAN left to
this gate (key management, DB-file protection, backup posture cross-check).

### 2.1 Decision: application-level encryption, Fernet (AES-128-CBC +
HMAC), per-photo IV, key from environment

- **Mechanism:** `cryptography.fernet.Fernet` — authenticated encryption
  (confidentiality + integrity in one primitive), well-audited Python
  library already a near-certain transitive dependency of this stack's
  ecosystem, no exotic crypto choices for a project this size.
- **Key management:** a single symmetric key, generated once
  (`Fernet.generate_key()`), stored in `.env` as `PHOTO_ENCRYPTION_KEY`
  (never committed — confirmed against `.gitignore`, see §2.5) for local
  development. **Not** OS keychain this run: keychain integration
  (`keyring` library, platform-specific backends) adds real complexity and
  a new failure mode (key retrieval failing silently on an unsupported
  platform) for a local single-developer-run app where `.env` is already
  the established secret-handling pattern for `ANTHROPIC_API_KEY`/
  `OPENAI_API_KEY` in this same template. This is a right-sizing call,
  stated as a trade-off, not an oversight: **revisit before any non-local
  deployment** (§2.6) — a shared/cloud deployment cannot rely on a
  developer's local `.env` for the key that protects every family's
  child photos.
- **Per-photo IV/nonce:** Fernet handles this internally (a fresh
  initialization vector per encryption call, embedded in its token format)
  — no manual IV management needed, which also avoids the classic
  IV-reuse mistake.
- **Encrypt-before-write, decrypt-on-serve:** upload path encrypts the
  validated, EXIF-stripped image bytes before the temp-then-rename write
  (ARCHITECTURE_KB §3); `GET /profiles/{id}/photos/{pid}` decrypts
  in-memory and streams the response, never writing decrypted bytes back to
  disk.

### 2.2 SQLite file: yes, equivalent protection is warranted, with one
caveat stated honestly

**Decision: the SQLite DB file itself is NOT separately encrypted this
run** (no SQLCipher, no filesystem-level encryption mandate from the app).
Reasoning, stated as a real trade-off rather than a silent gap:

- The highest-sensitivity content (photo bytes) is already protected at the
  application layer regardless of what happens to the DB file (§2.1) — the
  DB only ever holds `photo_meta`, never bytes (ARCHITECTURE_KB §3).
- What the DB *does* hold in plaintext under this decision: profile names/
  DOB/prematurity status, memory text, password **hashes** (not passwords),
  session token **hashes** (not tokens), email addresses. This is real PII
  and deserves acknowledgment, not dismissal — but it is qualitatively
  different from photo bytes or credential material, both of which already
  have their own protection (encryption, hashing) independent of the DB
  file's own state.
- Adding SQLCipher (or requiring the host OS's full-disk encryption as a
  documented precondition) is the correct next step, but doing it *this
  run* for a `local` target-environment app (where "at rest" substantially
  means "on the developer's own machine, which they are also responsible
  for physically securing") is disproportionate complexity for the
  marginal protection gained, given photo bytes and credentials are already
  covered by their own mechanisms.
- **This is a genuine gap, named explicitly rather than glossed over**:
  profile display names, DOB, and memory text are readable by anyone with
  raw filesystem access to `backend/data/little_milestones.db`. Mitigated
  operationally by: `backend/data/` is gitignored (confirmed, §2.5) and the
  DB file's OS-level permissions should be `0600` (owner-read-write only) —
  code-agent should set this on file creation. **Revisit trigger: before
  any non-local deployment, or if the human's threat model includes
  "someone else with access to this machine" even locally** (§2.6).

### 2.3 Private-by-default access — confirms PLAN, states the authz check explicitly

- **No static file mount, ever** — confirmed as an architectural invariant,
  not just a route convention: `photos.py`'s router is the *only* code path
  that can produce photo bytes in an HTTP response. This is checked at
  Review gate (ARCHITECTURE_KB §6.3/§7's static-import-graph check covers
  the LLM-isolation half; this role's Test-gate security suite separately
  asserts the raw filesystem path — `GET /data/photos/...` or any bypass of
  the API — returns 404/is unroutable, per PLAN §7-G22).
- **Authorization check on every photo read/write**: `family_id` on the
  owning profile must match `get_current_family(session)`'s result —
  cross-family photo access is 404 (§1.1's rule applied here specifically),
  verified by PLAN §7-G22's post-Increment-3 fixture (family B requesting
  family A's photo → 404) and re-run as a regression at Increment 3's gate
  (PLAN §4.7 item 3).
- **Owner-only delete** (F10's rule, PLAN §4.6): a caregiver session with
  valid family-scope but `role=caregiver` attempting photo delete gets 403
  (not 404 — this is a legitimate-access-but-insufficient-role case,
  correctly distinguished from the cross-family 404 case per PLAN §7-J36).

### 2.4 Retention/delete — verified purge semantics

Confirms PLAN §4.3's design exactly, with the delete-ordering detail made
explicit (this is a security-relevant sequencing question ARCHITECTURE_KB's
§3 flagged but didn't resolve):

- **Delete order: unlink the file bytes first, then delete the `photo_meta`
  row**, not the reverse. Reasoning: if the process crashes between the two
  steps, "row exists, file gone" is a safe failure (the app can detect and
  clean up an orphaned row on next access, returning 404 for a photo whose
  file is missing) — whereas "row gone, file still on disk" is an unsafe
  failure (an orphaned encrypted file with no record of its existence,
  never cleaned up, technically still "deleted" from the user's perspective
  but not actually purged, which directly contradicts the "immediately and
  permanently... we keep no copies" UI promise, UX_KB §1.10).
- **Verified purge**: PLAN §7-G21's `os.path.exists` post-delete assertion
  is confirmed as the correct test-level guarantee and is this role's suite
  to own at Test gate (security suite: does delete *actually* remove bytes,
  not just the metadata pointer).
- **Cascading delete** (profile delete → memories → photo bytes + metadata)
  is enforced by the SQLite `ON DELETE CASCADE` constraints
  (ARCHITECTURE_KB §3) for the *metadata* side; the *file-bytes* side
  cannot be a DB constraint (SQLite doesn't delete filesystem files), so
  `photos.py`'s profile-delete handler must explicitly iterate and unlink
  all photo files for that profile **before** issuing the DB cascade delete
  — this ordering (files first, then DB cascade) is the same crash-safety
  reasoning as the single-photo case above, applied to the batch case, and
  should be a named test case at Test gate (PLAN §7-G21's "profile delete
  leaves zero files" assertion already covers the outcome; this note
  covers *why* the ordering must be files-then-DB specifically).

### 2.5 Secrets handling — confirmed against actual repo state

- `.env` holds `PHOTO_ENCRYPTION_KEY`, `ANTHROPIC_API_KEY`/`OPENAI_API_KEY`
  (existing template pattern), and (if email infra is ever added)
  transactional-email API keys. **Confirmed**: this role's standard check —
  `backend/.gitignore` must exclude `.env` and `backend/data/` — is a
  Review-gate assertion (does the actual committed `.gitignore` list both),
  not just a design intention; PLAN §4.1/§4.3 already specify adding
  `data/` to `.gitignore`, and `.env` exclusion is inherited from the
  `genai-chatbot` template (verify at Review, don't assume).
- No secret (key, password, session token) is ever logged. §output-side
  enforcement's incident logging (ARCHITECTURE_KB §6.1) logs profile id and
  violation category only — explicitly audited for this at Test gate
  (security suite: trigger a guardrail violation, inspect the log line,
  assert no session token/password/photo path appears in it).

### 2.6 Explicit revisit triggers (photo/DB encryption)

1. **Before any non-local deployment**: move `PHOTO_ENCRYPTION_KEY` to a
   proper secret manager or OS keychain-backed store rather than `.env`;
   reconsider SQLCipher for the DB file now that "at rest" means a shared
   or cloud host, not a developer's own machine.
2. **If a backup/export feature is ever added** (ARCHITECTURE_KB §3 notes
   this is deferred): any export path must decrypt only into a user-
   initiated, user-controlled artifact — never an automatic background
   backup — and should re-encrypt or at minimum warn the user explicitly
   that an exported copy is no longer covered by the app's retention/delete
   guarantees.
3. **If multi-server/horizontal scaling is ever needed**: a single
   env-var key stops working across processes/machines without a shared
   secret-distribution mechanism — revisit key management then, not before
   (premature to design for a scale this project isn't at).

---

## 3. Input validation boundaries (cross-cutting, brief — most of this is
already specified in PLAN and ARCHITECTURE_KB; this section states the
security framing on top)

- Every Pydantic model boundary (profiles, memories, users) is the
  validation boundary — confirmed sufficient for this app's shape (no raw
  SQL string interpolation anywhere per ARCHITECTURE_KB §3's `Store[T]`
  interface discipline, so SQL injection is structurally avoided rather
  than defended against per-query).
- Photo upload: content-sniffed (magic bytes), not extension-trusted
  (PLAN §4.3, confirmed as the correct control against a renamed
  executable — PLAN §7-G20's `.exe`-renamed-`.jpg` test case is this role's
  to co-own with test-agent as a security-suite scenario, not just a
  functional one).
- Size caps (10MB photo) prevent trivial resource-exhaustion via upload.
- Rate limiting (§1.5) covers the auth surface; the F8 addendum (§1.7)
  extends this to the unsubscribe route as well — no other endpoint in this
  MVP carries a comparable brute-force-able secret or unauthenticated
  write, so no additional rate-limiting is designed this run — stated as a
  scoped decision, not an oversight.

---

## 4. Test-suite ownership (Test gate, this project)

Per this role's contract, security-architect owns at Test gate:
- **Authz boundary tests**: cross-family 404s (PLAN §7-J34), owner-vs-
  caregiver 403s (§7-J36), unauthenticated-route 401s (§7-J33).
- **Input validation/injection checks**: photo content-sniff bypass
  attempts (§7-G20), Pydantic boundary fuzzing on profile/memory fields.
- **Secrets-leak check**: `.env`/`backend/data/` actually gitignored (not
  just intended to be); no secret appears in logs (§2.5); password/session
  tokens are never stored or transmitted in plaintext (store inspection,
  §7-J33); **new (§5 addendum): `RESEND_API_KEY` also actually gitignored
  via `.env`, never appears in logs (including Resend HTTP-call error
  logging in `email_delivery.py`/`scheduler.py`).**
- **Photo purge verification**: §2.4's file-then-DB ordering and
  `os.path.exists` assertions (co-owned with the architecture suite's
  broader photo tests, ARCHITECTURE_KB §7, since the two overlap by
  design — cascade correctness is architecture's frame, purge-as-a-security-
  guarantee is this role's frame, same test fixtures serve both).
- **New (§1.7 addendum): unsubscribe-route scoping test** — extra
  fields/params on `GET /digest/unsubscribe` change no row field besides
  `digest_opt_in`; confirmation-page response contains no third-party
  resource loads/links (Referer-leak check); rate limiter fires on repeated
  requests from one IP.
- Evidence recorded per-scenario in `projects/little-milestones/test-evidence/`.

---

## 5. Third-party data processors (F8 addendum, 2026-07-10)

*(New section — the original gate had no third-party data-processor
consideration to record because no external service received any user data;
F8's revised, real-delivery design changes that, and this role's contract
requires flagging any new data-flow consideration the design introduces,
not just the API-key mechanics.)*

### 5.1 What Resend actually receives, stated precisely

Per ARCHITECTURE_KB §5.7's content design (confirmed correct and load-
bearing, not re-litigated here): **no child data** — no name, DOB, age,
milestone content, memory text, or photo-derived data — ever reaches
Resend. What Resend *does* receive, once per send:

- The caregiver's own email address (the recipient) — this is unavoidable
  for any email-delivery mechanism, by definition of "delivery."
- Standard email transport metadata: send timestamp, subject line (fixed,
  content-free), the fixed HTML body, `List-Unsubscribe`/
  `List-Unsubscribe-Post` header values (which contain the per-user
  unsubscribe token, §1.7 point 5).
- Incidentally, by virtue of being the sending platform: delivery-status
  metadata (bounced/delivered/failed) tied to that email address.

### 5.2 Is this a new disclosure requiring flagging? Yes — assessed and scoped, not dismissed

This is genuinely new: prior to this revision, no user data of any kind left
the local system to a third party at all (LLM provider calls carry
milestone-context prompt text, which is a separate, already-accepted
disclosure surface predating this addendum, not equivalent to this one).
Sending a caregiver's email address to Resend is a **third-party disclosure
of adult-caregiver PII** (not child PII — that distinction matters and is
why this is not a COPPA-triggering event, but it is still PII disclosure
under general privacy-by-design practice and INDUSTRY_KB §2.2's "no
third-party disclosure without separate consent" flag, which this project
has otherwise held to strictly).

**Assessment: this specific disclosure is low-risk and consented-to
structurally (the caregiver opted into the digest, which by definition
requires their email address reaching whatever delivery mechanism sends
it) — but it still requires a disclosure, not silent acceptance, because
"the user gave us their email to receive email" is not the same as "the
user was told a third-party vendor processes that email address."**

### 5.3 Required additions (change requested, not optional documentation)

1. **Privacy-policy disclosure required before production sending.** If/when
   this project has a privacy policy (not yet confirmed to exist in this
   project's current scope — flagged here rather than assumed), it must name
   Resend (or "a third-party transactional email provider") as a
   sub-processor of the caregiver's email address, alongside the existing
   LLM-provider disclosure this project presumably already needs for
   `/chat`. **This is the same class of flag as ARCHITECTURE_KB §5.6's
   mailing-address requirement — a human/deploy-agent action item, not
   something solution-architect or code-agent can invent unilaterally, and
   should be tracked alongside it as a pre-production go-live checklist
   item.**
2. **Vendor posture, light-touch check recommended (not a blocker for MVP
   given the low sensitivity of what's disclosed):** confirm Resend's own
   security/compliance posture (published SOC 2 report, standard DPA
   available on request) before the domain-verification step
   (ARCHITECTURE_KB §5.1's operational precondition) is carried out for
   production use — a five-minute vendor check, proportionate to what's
   actually at stake (an email address, not child data), not a full vendor-
   security-review process.
3. **No change to the Authentication & Authorization Design conclusion
   (§1.1)** — Resend does not gate access to anything in this app and
   introduces no new authn/authz surface of its own; this section exists
   because the role's contract requires flagging new data-flow/compliance
   considerations, not because this changes §1's reasoning.

### 5.4 Revisit trigger

Before any non-local deployment, or before a second third-party service is
ever added (analytics, error-tracking/Sentry-style tooling, etc.), re-run
this section's assessment as a standing "third-party processors" inventory
rather than a one-off note — this section is the seed of that inventory,
not assumed to be its final form.

---

## 6. Sign-off note

**No disagreement with solution-architect's design at this gate.** The
photo-encryption mechanism (§2.1), key-management right-sizing (§2.1, §2.2),
and auth baseline (§1) were reviewed against `ARCHITECTURE_KB.md`'s
component shape and found consistent — the SQLite decision, the
Increment-1 auth seam, and the filesystem-path-by-id photo storage design
all fit this security design without modification. Where this file names a
genuine gap (§1.3's no-password-reset, §2.2's unencrypted-DB-file), those
are stated as accepted, revisit-triggered trade-offs for a `local`-target
MVP, not silent omissions — consistent with this role's guardrail against
both over- and under-building for what's actually being shipped.

### 6.1 Addendum, 2026-07-10 — F8 real-delivery revision (§5 of ARCHITECTURE_KB)

**Independently reviewed as requested by solution-architect. Not a rubber
stamp — findings below.**

- **API key handling (`RESEND_API_KEY` in `.env`, ARCHITECTURE_KB §5.8):
  confirmed consistent with §2.5's existing secrets pattern, no change
  needed.** Same file, same gitignore coverage, same right-sizing rationale
  already applied to `PHOTO_ENCRYPTION_KEY`; the "no new secret-handling
  mechanism" claim in §5.8 is accurate.
- **Unauthenticated unsubscribe route: approved conditional on two concrete
  additions** — see §1.7 above for full reasoning. In short: (a) the route
  handler must perform a structurally single-purpose write (not a generic
  user-update call), verified by a new scoping test; (b) a rate limiter
  (reusing §1.5's pattern) must be added to the route for abuse resistance.
  Token design itself (stable, hashed, 256-bit entropy, GET-transported per
  RFC 8058) is confirmed correct as designed, no change requested there.
- **New data-flow implication identified and addressed: third-party
  processor disclosure (§5 above).** This was not covered by
  ARCHITECTURE_KB §5.8 (which addressed only the API-key mechanics, not the
  fact that a caregiver's email address now reaches a third-party vendor) —
  flagged as a required privacy-policy addition and light-touch vendor
  check before production sending, not a blocker for continuing to Code
  gate at `local`-target scope.

**This revision (§5's F8 real-delivery design) is treated as jointly
approved by security-architect as of this addendum, conditional on items 3
and 4 of §1.7 and the privacy-policy/vendor-check items of §5.3 being
tracked and completed before production sending is enabled** — consistent
with the joint-presentation requirement ARCHITECTURE_KB §8 calls out.

---

## 7. F12 — Hardened auth suite (Increment 6 design, security-architect, 2026-07-12)

Design pass for the human-approved F12 build (checkbox review 2026-07-12).
Scopes F12's four sub-items against their own recorded triggers (§1.6,
FEATURES.md F12), then designs what's in scope precisely enough for
code-agent. This section extends §1; it does not replace §1.1's baseline.

### 7.1 Scope decisions, reasoned against the triggers

1. **Self-service password reset — IN SCOPE.** §1.6 trigger 2 has fired:
   email infrastructure exists (ARCHITECTURE_KB §5, Increment 3). §1.3
   already named this the first post-email-infra build. Constraint carried
   from §1.3's note: the unsubscribe-token mechanism is NOT repurposed —
   reset tokens are a separate, single-use, short-expiry mechanism (§7.2).
2. **TOTP MFA — IN SCOPE, strictly per-user opt-in.** §1.6 trigger 3
   (threat-model change via third-party integration) fires next increment:
   F17 links caregiver Google accounts and grants Photos-API access, so an
   account takeover post-F17 reaches a third-party grant, not just local
   data. Building MFA in the dedicated security increment, before F17,
   closes that window instead of opening it. The human's recorded intent
   ("top of the line auth mechanism") independently supports it. §1.3's
   friction objection is answered by opt-in-only: no user — including the
   family owner on caregivers' behalf — can force MFA on another account;
   the zero-friction default is preserved.
3. **OAuth/social login — REMAINS DEFERRED.** §1.3's privacy reasoning is
   unchanged and no concrete user-facing need has emerged. Explicitly: F17's
   Google OAuth is a resource grant for the Photos API, not a login
   identity — it creates no precedent for "sign in with Google" and does
   not weaken this rejection.
4. **Managed session store / HTTPS enforcement — REMAINS DEFERRED**
   (trigger 1, non-local deployment, has not fired). Folded in instead, as
   cheap hardening on the existing sessions table: session listing,
   per-session revocation, "log out everywhere," an authenticated
   change-password endpoint, and invalidate-all-sessions on any password
   change or reset (§7.4). No external store, no new operational surface.

### 7.2 Password reset design

- **Schema:** new table
  `password_reset_tokens(id INTEGER PK, user_id FK→users ON DELETE CASCADE,
  token_hash TEXT UNIQUE NOT NULL, created_at, expires_at, used_at NULL)`.
- **Token:** `secrets.token_urlsafe(32)` (matches §1.1 session tokens),
  SHA-256 hash at rest (not a password, no slow KDF), **30-minute expiry,
  single-use** (`used_at` set on redemption), **one active token per user**
  (a new request invalidates any outstanding token for that user first).
- **`POST /auth/password-reset/request` `{email}`** — always returns the
  same generic 202 ("if an account exists for that address, we've sent a
  link") for known email, unknown email, AND send failure (no enumeration
  via status, body, or timing-visible branching; the Resend call happens
  after the response path is fixed, failure logged per §2.5's no-PII rule
  — user_id only, never the email address). Rate limits (§1.5 primitive):
  3/hour per email + 10/hour per IP.
- **Email:** new `email_delivery.send_password_reset_email(to_email,
  reset_url)` — same content-free discipline as ARCHITECTURE_KB §5.7:
  fixed subject/body, no child data, no personalization; footer per §5.6.
  **Same delivery gating as the digest:** built and contract-tested against
  mocked Resend; real sending contingent on the unmet domain-verification
  precondition (ARCHITECTURE_KB §5.1). Stated posture, not a gap.
- **`POST /auth/password-reset/confirm` `{token, new_password}`** — lookup
  by hash (constant-time compare, mirroring session lookup), enforce
  expiry + single-use, validate password, write new argon2id hash, mark
  token used, and **delete ALL sessions for the user** (a reset is a
  possible-compromise event; every existing session dies, including any
  attacker's). Generic error for invalid/expired/used token (no
  distinguishing which). Rate limit: 10/15min per IP. **Reset does not
  bypass or disable TOTP** — an attacker with email access alone must not
  be able to strip MFA; a user locked out of both email-recovery and TOTP
  uses a recovery code (§7.3), which is what recovery codes are for.
- **Frontend token-leak constraints** (for ui-ux-designer/code-agent, same
  reasoning as §1.7 point 5): the reset page carries the raw token in its
  URL — it must load no third-party resources and should strip the token
  from the address bar (`history.replaceState`) once read.
- **§1.3 status change:** the "no password reset" accepted gap is retired
  by this build; the Settings copy documenting it must be removed
  (flagged to ui-ux-designer).

### 7.3 TOTP MFA design (opt-in)

- **Library/parameters:** `pyotp`, RFC 6238 defaults — SHA-1, 6 digits,
  30s step, ±1 step verification window (standard authenticator-app
  compatibility; not a weakness at this token lifetime).
- **Schema:** on `users`: `totp_secret_enc TEXT NULL` (secret encrypted
  with the existing Fernet key from §2.1 — unlike a password it must be
  recoverable to verify codes, so hashing is impossible; encryption keeps
  it out of the §2.2 plaintext-DB surface), `totp_verified_at TIMESTAMP
  NULL` (NULL = not enrolled or enrollment pending). New table
  `recovery_codes(id, user_id FK→users ON DELETE CASCADE,
  code_hash TEXT NOT NULL, used_at NULL)`.
- **Enrollment (authenticated, Settings):** `POST /auth/totp/setup`
  (requires current-password re-entry — a hijacked session must not be
  able to enroll its own MFA) → generates secret, stores it encrypted with
  `totp_verified_at=NULL`, returns the `otpauth://` provisioning URI (QR
  rendered client-side; the server never generates a QR image). Pending
  secrets have no effect at login. `POST /auth/totp/verify {code}` with a
  valid code completes enrollment: sets `totp_verified_at`, generates
  **8 recovery codes** (`secrets`-sourced, ~16 base32 chars, grouped for
  readability), returns them **exactly once**, stores argon2id hashes
  (short enough to be password-class, unlike 256-bit tokens — slow KDF is
  warranted here). Re-running setup replaces any pending secret.
- **Login flow for enrolled users:** `POST /auth/login` with a correct
  password creates a session row with a new `sessions.mfa_pending`
  flag set — the auth dependency (`get_current_family`) rejects pending
  sessions for every route except `POST /auth/totp/login {code}`, which on
  a valid TOTP or unused recovery code clears the flag (recovery code:
  `used_at` set; response warns how many remain). **5 failed attempts
  destroy the pending session** (fresh password login required) — this,
  not the limiter, is the primary 6-digit brute-force control. Pending
  sessions expire after 5 minutes regardless. Non-enrolled users' login is
  byte-for-byte unchanged.
- **Disable:** `POST /auth/totp/disable` requires current password AND a
  valid TOTP or recovery code; clears secret and deletes remaining
  recovery codes.
- **Never forced:** no owner-mandates-MFA capability is built; per-user
  opt-in only.

### 7.4 Session hardening (folded into F12, in lieu of sub-item 4)

- **Schema:** `sessions` gains `id TEXT` (uuid4 — non-enumerable, same
  reasoning as `photo_meta.id`), `mfa_pending BOOLEAN DEFAULT 0`,
  `last_seen_at TIMESTAMP` (updated on the existing sliding-expiry touch).
- **Routes (all authenticated, self-scoped — a user manages only their own
  sessions, never another caregiver's):** `GET /auth/sessions` (list:
  created, last-seen, current-session marker; never the token or its
  hash), `DELETE /auth/sessions/{id}` (revoke one),
  `POST /auth/sessions/revoke-others` ("log out everywhere else").
- **`POST /auth/password` (change, authenticated):** requires current
  password; new argon2id hash; deletes all OTHER sessions (current
  survives — deliberate difference from reset's delete-all, since a
  logged-in, password-knowing change is not a compromise signal).

### 7.5 Test-suite additions (extends §4, this role's suite at Test gate)

- Reset token: single-use enforced; expired token rejected; second request
  invalidates the first token; identical response body/status for
  known-vs-unknown email on request (enumeration check).
- Reset confirm: all sessions for the user are dead afterward (a
  pre-reset session cookie gets 401); TOTP enrollment survives reset.
- Reset email contract (mocked Resend): no child data in body, fixed
  subject, reset URL present — same fixture pattern as the digest test.
- TOTP: pending (`mfa_pending`) session gets 401 on every non-TOTP route;
  5th failed code destroys the pending session; recovery code is
  single-use; setup without current password is rejected; secret at rest
  in the DB file is Fernet ciphertext, not a plaintext base32 seed.
- Session hardening: user A cannot list or revoke user B's sessions
  (404 per §1.1's cross-scope rule); revoke-others leaves exactly the
  current session valid.
- Secrets-leak sweep extended: no reset token, TOTP secret, or recovery
  code ever appears in a log line (trigger each flow, inspect logs).
- Rate limiters fire on reset-request (per-email and per-IP) and
  reset-confirm.

### 7.6 Revisit triggers (additive to §1.6)

1. Before F17 ships: confirm MFA is live and re-assess whether the Google
   token grant warrants recommending (not forcing) MFA enrollment in the
   linking flow's UI copy.
2. Before real email sending is enabled (domain verification): re-verify
   the reset flow end-to-end with live delivery, not just mocked Resend.
3. §1.6 triggers 1, 3, 4 remain in force unchanged; sub-items 3 and 4 of
   F12 (OAuth, managed session store) stay parked on their own triggers.

### 7.7 Joint-presentation note

Schema additions (`password_reset_tokens`, `recovery_codes`, three
`users`/`sessions` column sets) and the new `email_delivery` function
touch ARCHITECTURE_KB §3/§5's surface — solution-architect should confirm
they fit the store/schema conventions before code-agent starts. No
disagreement anticipated (all patterns reuse §1.1/§2.1/§5.4 precedents),
but per this role's contract that confirmation is theirs to record, not
mine to assume.
