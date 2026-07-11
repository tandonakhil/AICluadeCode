# ARCHITECTURE_KB — little-milestones

Maintained by: solution-architect. Architecture gate, 2026-07-10, jointly
presented with security-architect (`SECURITY_KB.md`) and
responsible-ai-architect (advisory, `RESPONSIBLE_AI_KB.md`). Resolves the six
open questions carried from PLAN.md §6, plus item 7 (output-side enforcement)
raised at this gate's kickoff. Designed against PLAN.md's proposed baselines,
DOMAIN_KB's R1–R8, INDUSTRY_KB's compliance flags, and UX_KB.md §1–6 in full.

**Status: pending human approval.** Nothing here authorizes code-agent to
start Increment 1 until the human signs off at this gate.

**Revision, 2026-07-10 (same day, human override):** §5 below was originally
a deferral ("ship opt-in machinery only, no real email"). The human overrode
that at this gate and requested real email delivery for F8's weekly digest.
§5 is fully replaced (not appended-to) with the real-delivery design below.
Everything else in this file is unchanged from the original Architecture
gate output.

---

## 0. Component map (unchanged template shape, extended)

```
dev/backend/app/
  main.py            — FastAPI app assembly only (routers mounted here)
  llm.py             — unchanged, provider switch
  db.py              — NEW: SQLite connection/session management (§3)
  ages.py            — NEW: pure age math (per PLAN §3.3)
  prompts.py         — NEW: system prompt assembly (per PLAN §3.4)
  milestones.py + data/milestones_cdc2022.json   — NEW: curated grounding (§1)
  profiles.py, memories.py, photos.py, digest.py, products.py, users.py — NEW: models + store classes, one per entity
  guardrails.py      — NEW: output-side enforcement layer (§7)
  crypto.py          — NEW: photo encryption helpers (paired with SECURITY_KB §photo)
  email_delivery.py  — NEW: Resend API client wrapper (§5.2)
  scheduler.py        — NEW: APScheduler setup + daily digest-send job (§5.3)
  routes/
    profiles.py, chat.py, memories.py, photos.py, digest.py, products.py, auth.py
dev/frontend/        — Next.js, per UX_KB.md; no architecture changes beyond
                        what ui-ux-designer's component/screen inventory implies
```

All stores implement a common `Store[T]` protocol (`create`, `get`,
`list_for_family`, `delete`) so the SQLite decision (§3) is testable in
isolation and swappable in principle, though no swap is planned.

---

## 1. R3 — milestone/activity grounding: **Option A, curated CDC-2022 table**

**Decision: adopt DOMAIN_KB's contested position.** `app/data/milestones_cdc2022.json`
is a hand-curated table (checklist buckets 2/4/6/9/12/15/18/24/30/36 months ×
domain: gross motor, fine motor, language/communication, social-emotional,
cognitive) sourced directly from the CDC/AAP February-2022 checklists, each
entry carrying `{bucket_months, domain, text, source: "CDC 2022"}`. A
parallel `activities` table (age-bucket-keyed, AAP-safety-vetted) backs F4/F9
via the same file or a sibling `activities_cdc2022.json`.

**Why A over B, concretely:**
- Model weights mix pre-2022 (50th-percentile) and post-2022
  (75th-percentile) framings indiscriminately — DOMAIN_KB R3 is not a
  theoretical risk, it's a training-data fact about every current frontier
  model. A milestone chat that occasionally cites "12 months for walking"
  and occasionally cites "18 months" in the same session is a correctness
  bug with anxiety consequences (R1), not a style inconsistency.
  Free generation cannot be prompted out of this reliably — the model doesn't
  know it's drawing from a stale source, so instruction-following cannot
  self-correct it.
  - Note the disagreement history: this is functional-agent's DOMAIN_KB
    position, and functional-agent is no longer on the active team (dropped
    after Intake per PROJECT_CONTEXT.md). solution-architect is *adopting*
    that recorded position at this gate on its technical merits, not
    rubber-stamping it — the reasoning above stands on its own.
- A curated table is cheap: ~10 buckets × ~5 domains × 1–2 line items is a
  few hundred rows, hand-checkable against the CDC source pages in an
  afternoon, versioned in git (it's data, not child data — it's fine in the
  repo, unlike `backend/data/`).
- It also directly satisfies F9's parallel need (products_catalog.json,
  cpsc_denylist.json already require curation) — same review discipline,
  same owner, addressed together (§1.1).

**What the LLM is still for, with A:** framing, warmth, answering the
parent's actual free-text question, weaving in the curated fact at the right
point, handling follow-ups, and all of R2's deflection logic. The LLM never
originates a milestone age or activity-safety claim; `prompts.py` injects the
current bucket's curated entries into the system prompt as the "Milestone/
activity grounding block" (PLAN §3.4 item 7), and instructs the model to draw
only from that block for factual milestone content. `guardrails.py` (§7)
backstops this at the output layer.

### 1.1 Curation ownership and update cadence

Three curated, safety-bearing data files exist after this gate:
`milestones_cdc2022.json` / `activities_cdc2022.json` (R3),
`products_catalog.json` (F9), `cpsc_denylist.json` (F9). All three share one
owner and one process, decided here rather than left dangling:

- **Owner: solution-architect**, as the role that already owns the grounding
  design; responsible-ai-architect co-reviews any change touching milestone
  *framing* (not just data — e.g. if CDC revises checklists again);
  functional-agent (re-engaged via `/consult` if needed, since it's dropped
  from the active roster) is the natural reviewer if a substantive medical/
  developmental content change is proposed, since that's domain-correctness
  territory outside solution-architect's lane.
- **Update trigger, not schedule:** these files are reviewed whenever (a) CDC/
  AAP revises the milestone checklist, (b) CPSC issues a new recall/ban
  relevant to the catalog's categories, or (c) a red-team/bias finding at
  Test flags stale or incorrect content — not on a calendar cadence, since a
  fixed schedule invites drift between reviews. This is recorded as a
  standing maintenance cost (PLAN §8 already flags it) rather than a one-time
  build cost.
- Each file carries a `_meta: {source, last_reviewed, reviewed_by}` block at
  the top for auditability.

---

## 2. Auth design (F10): baseline confirmed, refined in three places

**Decision: confirm PLAN §4.6's baseline** — local email+password accounts,
argon2 hashing via `passlib`, server-side sessions, HTTP-only SameSite=Lax
cookies, owner/caregiver roles, single-use expiring invite codes, cross-family
access returns 404. See SECURITY_KB.md's dedicated Authentication &
Authorization Design section for the full reasoning, criteria, and revisit
triggers — that is security-architect's call to document, not
solution-architect's to duplicate. This section covers the parts that are
architecture (component/data-flow), not security posture:

- **The Increment-1 seam holds exactly as PLAN §4.1 describes:**
  `get_current_family: Family = Depends(get_current_family)` is present on
  every route from Increment 1. Its Increment-1 body returns a single
  hardcoded default `Family` row (created by a startup migration, id fixed,
  e.g. `family_id=1`). Increment 3 replaces the function body only — no route
  signature changes. This is verified as an architecture-suite contract test
  at Test gate (§8 below): route handler signatures identical pre/post
  Increment 3.
- **Session storage: a `sessions` table in the same SQLite DB** (§3), not an
  external store (Redis, etc.) — this is a local, single-process app; adding
  an external session store would be complexity with no corresponding
  benefit at this scale. Session row: `{token_hash, user_id, created_at,
  expires_at}`. The cookie carries an opaque token; only its hash is stored
  (mirrors password-hash discipline for a second class of secret-bearing
  value).
- **Pre-auth data migration (F1–F9 built before F10 activates):** a
  `Family(id=1)` row and all pre-existing profiles/memories/photos already
  carry `family_id=1` from Increment 1 onward (they were never actually
  family-less — the seam means there is no "migration" in the schema sense,
  just an ownership assignment when the first real signup occurs: that
  signup's resulting `User.family_id` is forced to `1` rather than a new
  family being created, so "first user becomes owner of the existing family"
  replaces "first user creates a family." This removes the data-migration
  step PLAN §4.6 anticipated — it's a one-line special case in the signup
  handler, not a migration script.

---

## 3. Storage backend: **confirm SQLite**

**Decision: SQLite**, single file at `backend/data/little_milestones.db`
(gitignored), accessed via SQLAlchemy Core or a thin query layer — code-agent's
choice between SQLAlchemy and raw `sqlite3` + hand-written SQL is an
implementation detail, not an architecture decision, but either must go
through the `Store[T]` interfaces (§0) so route code never touches SQL
directly.

**Why, beyond PLAN §3.2's own reasoning:** five entity types
(`families`, `users`, `profiles`, `memories`, `photo_meta`, `invites`,
`digest_subscriptions` — seven, actually, once auth and digest are counted)
with real foreign-key cascade requirements (family delete → cascades
everything; profile delete → cascades memories → cascades photo_meta) is
exactly SQLite's sweet spot: `PRAGMA foreign_keys = ON` plus `ON DELETE
CASCADE` constraints turn "five hand-rolled JSON stores with manual cascade
logic" (PLAN's own words, correctly) into database-enforced invariants that
can't drift out of sync across store implementations. Concretely:

- `families(id)`
- `users(id, email UNIQUE, password_hash, family_id FK→families, role, digest_opt_in)`
- `sessions(token_hash, user_id FK→users, expires_at)`
- `profiles(id, family_id FK→families ON DELETE CASCADE, display_name, dob, born_early, weeks_early)`
- `memories(id, profile_id FK→profiles ON DELETE CASCADE, moment_date, title, note, milestone_tag)`
- `photo_meta(id, memory_id FK→memories ON DELETE CASCADE, profile_id, content_type, size, created_at, enc_iv)` —
  note: `enc_iv` (or equivalent) lives here, never the key (SECURITY_KB owns
  key handling)
- `invites(code, family_id FK→families, expires_at, single_use, used_at)`

**Note (added by §5's revision, does not alter anything above):** §5.4 below
adds three columns to `users` (`unsubscribe_token_hash`,
`last_digest_sent_at`) and documents them there rather than duplicating this
table here, to keep this section's diff-free from the original gate.

**Photo bytes stay on the filesystem, not in SQLite** (confirms PLAN §4.3):
`photo_meta` rows point to `backend/data/photos/{profile_id}/{photo_id}.enc`
by convention (id-derived path, not a stored path string, to avoid path-
injection surface). This keeps the DB file small, keeps hard-delete
literal (unlink the file, then delete the row — or vice versa, see §photo
delete-ordering note in SECURITY_KB), and avoids ever loading a photo blob
into a query result the app doesn't need.

**Migration:** a single `schema.sql` (or Alembic if code-agent prefers —
implementation choice) applied idempotently at startup. No production data
exists yet, so no data-migration tooling is warranted beyond "create tables
if absent."

**Backups:** confirms PLAN §4.6's proposal — no automatic backups of the
DB file or photo directory. A backup is a second copy of child data, which
is a liability under the retention/delete promise (INDUSTRY_KB §2.1: a photo
"deleted" from the app but sitting in a backup contradicts the "immediately
and permanently" UI copy in UX_KB §1.10). Revisit only if/when the human
requests an explicit export feature — which would be a deliberate,
user-initiated copy, not an automatic background one.

---

## 4. Photo color-extraction algorithm (UX_KB §6 contract)

UX_KB §6.3 specifies the *visual outcome and safety contract* and explicitly
delegates the extraction algorithm to Architecture. This is that design.
**Runs server-side, at upload time, once, synchronously as part of the
upload request** — never client-side (photo bytes must never leave the
server per F7's structural isolation, and "extract color client-side" would
require sending the decrypted image to the browser on every load, defeating
the point).

### 4.1 Pipeline

1. On `POST /profiles/{id}/photos`, after content-sniffing/validation and
   before encryption-at-rest, the raw image bytes pass through
   `app/photo_theme.py::extract_accent(image_bytes) -> AccentTokens`.
2. **Downsample first** (e.g. to a 64×64 or 100×100 thumbnail in memory,
   Pillow `Image.thumbnail`) — extraction never needs full resolution, and
   downsampling is also a cheap, incidental privacy improvement (less detail
   in the working buffer, though this is not a substitute for the encryption/
   isolation controls, which remain the real guarantee).
3. **Quantize to a reduced palette** using median-cut or k-means (k=5) over
   the downsampled pixels in RGB space (Pillow's built-in
   `Image.quantize(colors=5, method=Image.MEDIANCUT)` is sufficient — no new
   heavy dependency needed; Pillow is already implied by any image-handling
   in F7).
4. **Filter candidate clusters** before ranking, per UX_KB §6.3 rule 1
   ("most prominent non-skin-tone, non-neutral color"):
   - Convert each cluster's centroid to HSL.
   - Drop clusters with saturation < 15% (near-gray/near-white/near-black —
     "no color," matches UX_KB's rejection of whole-image averaging).
   - Drop clusters whose HSL falls inside a fixed **skin-tone exclusion
     band** (hue 5°–35°, saturation 20–60%, lightness 40–85% — a generous
     band covering the common range of photographed skin tones across
     lighting conditions; approximate by design, erring toward
     over-excluding rather than risking a face-adjacent hue becoming "the
     theme," which would be an odd personalization outcome even though it
     is not itself a face-detection operation — no facial geometry,
     landmarks, or identity data is computed, only a pixel-color-cluster
     heuristic, so this stays clear of INDUSTRY_KB's face-processing ban;
     see RESPONSIBLE_AI_KB / SECURITY_KB cross-check note below).
   - Rank remaining clusters by pixel-count (dominance) and pick the
     top one as the extraction target hue. If every cluster is filtered out
     (e.g. a genuinely monochrome or all-skin-tone photo), extraction
     returns `None` and the caller falls back to the default theme (§6.4's
     "complete theme, not placeholder" — this is the code path that
     realizes it).
5. **Clamp to the three safe bands** exactly as UX_KB §6.3.2 specifies, in
   HSL, deriving all three from the single extracted hue:
   - `--lm-photo-mid`: S 30–55%, L 45–60%
   - `--lm-photo-deep`: S 35–60%, L 22–32%
   - `--lm-photo-tint`: S 18–28%, L 90–94%
6. **Hue-exclusion rotation:** if the extracted hue is within ±20° of
   `--lm-danger`'s hue (compute once at build time from the fixed hex, store
   as a constant), rotate all three derived tokens' hue by +40° before
   returning.
7. **Automated contrast pre-check** (UX_KB §6.3 rule 4): render the two
   contract cases — white text over `--lm-photo-deep` with the fixed scrim
   gradient composited, and `--lm-ink` over `--lm-photo-tint` — compute WCAG
   contrast ratio (standard relative-luminance formula) for each. If either
   falls below its threshold (4.5:1 body / 3:1 large text, matching UX_KB),
   `extract_accent` returns `None` for that child rather than the computed
   tokens, and the frontend renders the default theme for that surface. This
   check is deterministic and re-run at upload time only (not per page
   load) — the result (`AccentTokens | None`) is stored as three hex values
   (or null) on the profile row, computed once, read many times.
8. Store the three resulting hex values (or nulls) in `profiles` (new
   columns `photo_accent_mid`, `photo_accent_deep`, `photo_accent_tint`) —
   **not** the photo-derived intermediate data, and definitely not raw pixel
   data beyond the transient in-memory processing of step 2–4. Nothing from
   this pipeline ever reaches `prompts.py`/`llm.py` (same structural
   isolation as the rest of F7 — `photo_theme.py` has no import path into
   the LLM layer, verified by the same static check as §photo isolation).

### 4.2 Why this satisfies "runs server-side... not client-side"

The only network trip is the original upload; the three derived hex strings
(a handful of bytes) are the only photo-derived data that ever reaches the
frontend for theming purposes — the browser never receives pixel data for
extraction. This also means re-computation on photo replace/delete is
trivial: delete clears the three columns (falls back to default theme
immediately, satisfying UX_KB §6.4), replace re-runs the pipeline.

**Note on multi-photo theme-source tracking (added 2026-07-11 — see §9.2):**
this section, as originally written, describes a single-photo mental model
("delete clears the three columns... replace re-runs the pipeline") and does
not specify how a profile with *multiple* photos should track which one is
currently powering the theme. §9.2 records the Increment-2 resolution of
that gap.

### 4.3 Library choice

**Pillow** (already a near-certain dependency for content-sniffing/EXIF-strip
in F7) is sufficient for steps 2–4 — no new heavy dependency (no OpenCV, no
ML model) is justified for a decorative accent-color feature. This keeps the
"why clamping alone is not sufficient" honesty from UX_KB (a simple k-means/
median-cut extraction is not claimed to be perceptually perfect) matched by
an equally simple, auditable implementation — no black-box color-science
library where a bug would be hard to reason about.

**Update, 2026-07-11 — HEIC support (see §9.1):** this section's "Pillow
alone is sufficient" claim is qualified by §9.1 — it is sufficient for the
JPEG/PNG/WebP formats Pillow decodes natively, but not for HEIC without the
`pillow-heif` plugin. §9.1 records the decision to add that plugin.

---

## 5. Email/notification infrastructure (F8 delivery) — **REVISED, real delivery**

**This section supersedes the original Architecture-gate deferral in full.**
The human overrode the deferral at this gate: F8's weekly digest ships with
real email delivery this run, not opt-in machinery alone. The original
deferral's stated privacy concern — a child's name/developmental stage
leaving the machine to a third-party mail provider on an unattended,
recurring basis — was valid and is not dropped by the override; it is
addressed by design below (§5.1's content minimization is the load-bearing
answer to it), not by reversing the concern.

### 5.0 What ships

- `GET /profiles/{id}/digest` (in-app content, unchanged from the original
  design — still the source of truth for digest *content*).
- Real outbound email, sent on a recurring schedule, to caregivers with
  `digest_opt_in=true`, via a transactional email provider (§5.1) triggered
  by an in-process scheduler (§5.3).
- A working, real, one-click unsubscribe path independent of the in-app
  opt-in toggle (§5.5) — required both because a toggle buried in Settings
  is not a functioning opt-out once mail is actually landing in someone's
  inbox, and because it is close to a legal expectation for any recurring
  commercial-adjacent email in the US (§5.6).

### 5.1 Provider choice: **Resend**

**Decision: Resend**, over Postmark, SES, or raw SMTP.

- **Free tier fits this project's actual scale.** Resend's free tier (3,000
  emails/month, 100/day) comfortably covers a small number of families each
  receiving at most one email per week — this is not a bulk-sending product,
  and no paid tier is warranted at this scale.
- **API surface is minimal** — a single authenticated POST with
  `{from, to, subject, html, headers}` — matching this project's "no new
  operational surface" instinct (same reasoning §3 already applies to
  SQLite-over-Postgres, applied here to email-over-SMTP). Raw SMTP is
  rejected for the same reason PLAN's original fallback rejected it:
  credential handling and deliverability (SPF/DKIM setup, IP reputation) are
  materially harder to get right by hand than via a transactional API.
- **Deliverability-relevant headers are first-class**, not bolted on: Resend
  supports arbitrary custom headers, which §5.5 depends on for
  `List-Unsubscribe`/`List-Unsubscribe-Post` (RFC 8058 one-click headers,
  now effectively required by Gmail/Yahoo's 2024+ bulk-sender rules for any
  sender doing recurring automated mail — directly relevant here even at
  small volume, because the *behavior* (a scheduled, automated, recurring
  send) is what those rules key off, not sender size).
- **Postmark** was the documented fallback's other option; Resend is chosen
  over it on convenience (simpler onboarding, no separate "transactional
  stream" concept to configure) with no meaningful capability gap for this
  project's needs — this is a close call between two reasonable options, not
  a strong technical differentiator either way.
- **Operational precondition, stated explicitly:** sending from a shared
  testing domain (e.g. `onboarding@resend.dev`) restricts delivery to
  verified addresses only during development; a real send to arbitrary
  caregiver inboxes requires verifying a domain (SPF/DKIM records) with
  Resend before Increment-3-equivalent production use. This is a deployment
  step, not a code-agent task, and is flagged for deploy-agent/human action
  before the digest scheduler is enabled against real user data.

### 5.2 Sending mechanism: `app/email_delivery.py`

A thin wrapper, not a general email framework:

```
def send_digest_notification(to_email: str, unsubscribe_url: str) -> None
```

- Calls Resend's REST API with `RESEND_API_KEY` (§5.4).
- Builds the fixed notification template (§5.1's content design) — no
  per-recipient templating beyond the unsubscribe URL and (optionally) a
  neutral family-nickname if the family has set one, never the child's real
  name (§5.1... see §5.1 content rule below, this function only assembles
  what §5.1-content already decided).
- Sets `List-Unsubscribe: <{unsubscribe_url}>` and
  `List-Unsubscribe-Post: List-Unsubscribe=One-Click` headers.
- Raises on non-2xx; caller (§5.3) catches per-recipient so one failure
  doesn't block the batch.
- No retry logic in this function — retry policy lives in the scheduler
  job (§5.3), kept out of the delivery wrapper so the wrapper stays a pure
  "send one email" primitive, testable in isolation (contract test at Test
  gate: mock the Resend HTTP call, assert headers/body shape).

### 5.3 Scheduling mechanism: **in-process APScheduler — confirms the documented fallback**

**Confirmed as designed** (the original deferral's fallback is adopted as-is,
not revised): `app/scheduler.py` initializes an APScheduler
`BackgroundScheduler` at FastAPI startup (via the app's lifespan/startup
hook), registering **one daily job** (not per-user, not a separate cron
process) that:

1. Runs once per day at a fixed local time (e.g. 08:00 server time — a
   config constant, not user-configurable this run; per-user send-time
   preference is out of scope).
2. Queries `users` where `digest_opt_in=true` and
   (`last_digest_sent_at IS NULL OR last_digest_sent_at <= now - 7 days`).
3. For each due user, in a per-user `try/except`: calls
   `email_delivery.send_digest_notification(...)`, and on success updates
   `last_digest_sent_at = now()`. On failure, logs `{user_id, error}` (no
   email address — same no-PII-in-logs discipline as `guardrails.py`'s
   incident logging, §6.1) and leaves `last_digest_sent_at` unchanged so the
   user is naturally retried on the next day's run rather than needing
   explicit retry logic.
4. Runs **in-process, sharing the FastAPI process** — rejected the
   separate-cron-process alternative for the same reason the original
   fallback gave: fewer moving parts for a local, single-process app. This
   does mean the digest job only fires while the app process is running; for
   a `local` target environment (PROJECT_CONTEXT.md) where the app isn't
   expected to run 24/7 unattended yet, this is an accepted, named
   limitation — **revisit trigger: before any non-local/always-on
   deployment**, confirm the scheduler actually fires reliably at that
   uptime profile, or move to a proper cron/managed-scheduler trigger at
   that point (same class of revisit as SECURITY_KB's deployment-sensitivity
   triggers, kept in this file since it's a scheduling architecture
   decision, not a security one).

### 5.4 Data model additions (extends §3, not a new backend)

Two new columns on `users` (SQLite, per §3's schema):

- `last_digest_sent_at TIMESTAMP NULL` — drives the due-check in §5.3.
- `unsubscribe_token_hash TEXT NOT NULL` — generated once, at account
  creation (or at `digest_opt_in` first being set true, whichever comes
  first), using the same pattern as session tokens (SECURITY_KB §1.1):
  `secrets.token_urlsafe(32)`, only the **hash** stored (SHA-256, same
  reasoning as session tokens — not a password, no slow KDF needed), raw
  token embedded in the unsubscribe URL. This means the unsubscribe link is
  stable for a given user (doesn't rotate on every send), so a caregiver
  who saved or bookmarked it, or is re-clicking an older email, still gets a
  working link — deliberately not single-use, since single-use would make a
  second click on the same email (a very plausible real-world action) fail
  or need special-cased idempotent handling; a stable per-user token
  achieves the same idempotency more simply.

### 5.5 Unsubscribe: real, one-click, independent of the in-app toggle

**The in-app `digest_opt_in` Settings toggle remains** (governs whether the
scheduler considers the user "due" at all — §5.3 step 2), but it is not
treated as a sufficient opt-out mechanism once real mail is being sent,
because it requires the caregiver to log in to turn email off, which is
exactly backwards for someone who wants unwanted mail to stop.

- **New unauthenticated route:** `GET /digest/unsubscribe?token={raw_token}`.
  Deliberately unauthenticated — an unsubscribe link that requires login
  defeats the point (a caregiver who lost access, or is on a different
  device, must still be able to opt out with one click) and is also the RFC
  8058 / mailbox-provider expectation (§5.6) for a one-click header to work
  automatically without a login prompt.
- Looks up `unsubscribe_token_hash` by hashing the incoming raw token
  (constant-time compare, mirroring session-token lookup discipline), sets
  `digest_opt_in = false` on the matching user, and returns a plain
  confirmation page ("You've been unsubscribed from the weekly digest. You
  can re-enable it anytime from Settings.") — **idempotent**: re-visiting an
  already-unsubscribed link re-confirms rather than erroring, since bulk-mail
  norms (and simple UX correctness) expect a repeated unsubscribe click to be
  a harmless no-op, not a 404/error page.
- **This exact URL is also what the `List-Unsubscribe-Post` one-click header
  (§5.2) points at** — this is the same mechanism serving both the
  in-email visible link (footer) and the mailbox-provider automated
  one-click action, not two separate implementations to keep in sync.
- No separate "confirm unsubscribe" step (no "are you sure?" page) — a
  one-click unsubscribe that isn't actually one click fails both the
  usability goal and, for the `List-Unsubscribe-Post` header specifically,
  the RFC 8058 contract (providers expect the action to complete on the
  single POST, no intermediate page).

### 5.6 Compliance check: CAN-SPAM, stated explicitly (a gap INDUSTRY_KB did not name)

INDUSTRY_KB's compliance flags (§2 of that file) cover COPPA, state
children's-privacy codes, and targeted-advertising restrictions, but do not
name CAN-SPAM — worth stating explicitly here since this revision is the
first time this project actually sends commercial-jurisdiction email:

- **Applicability, reasoned rather than assumed:** CAN-SPAM applies to
  "commercial electronic mail messages." The weekly digest is arguably
  borderline — its primary purpose is informational/relationship
  (an update notification), but F9's buying-recommendation content
  (INDUSTRY_KB §1.5) is reachable from the same digest surface in the
  in-app content, and CAN-SPAM's own guidance treats messages with *any*
  commercial content conservatively. **Decision: comply with CAN-SPAM's
  requirements regardless of the borderline classification** — the
  compliance cost of doing so is low and the downside of guessing wrong is
  not.
- **What CAN-SPAM requires, and how this design satisfies each:**
  - *Accurate header/subject information* — the fixed subject line and
    `from` address (§5.1) are non-deceptive by construction (no fake sender
    name, no misleading subject).
  - *Clear identification as an ad, if applicable* — not applicable if the
    notification-only content design (§5.1) is followed exactly (no product
    content in the email body itself — see below); this is in fact another
    reason the neutral, content-free notification design is the right
    choice, not just a privacy-minimization one.
  - *A valid physical postal address* — **new requirement this design must
    carry**: the email footer must include a real mailing address or
    registered PO box. This is a business/operational detail outside
    solution-architect's authority to invent (it requires an actual address
    to exist) — **flagged for the human/deploy-agent to supply before the
    scheduler is enabled against real users**; `email_delivery.py`'s
    template has a placeholder constant (`MAILING_ADDRESS`) that must be
    filled before production sending, and this is a Review-gate assertion
    (template renders with a non-placeholder address), not just a design
    note.
  - *A working opt-out mechanism, honored within 10 business days* — §5.5's
    unsubscribe is honored immediately (same request, not batched), which
    exceeds the statutory floor.
  - *No opt-out fee, no additional info required beyond email address* —
    satisfied structurally: §5.5's endpoint takes only the token, no login,
    no form.
- **Not a CAN-SPAM point but adjacent and worth stating:** AADC-direction
  states (INDUSTRY_KB §2.3) favor privacy-protective defaults generally —
  `digest_opt_in` defaulting to `false` (unchanged from the original design)
  already aligns with that direction; this revision does not change the
  default.

### 5.7 Privacy design: what actually goes in the email body

This is the direct answer to the original deferral's stated concern, not a
side note:

- **The email body never contains the child's real name, DOB, age, or any
  milestone/developmental content.** It is a pure notification:
  - Subject: `"Your weekly little-milestones update is ready"` — fixed,
    identical for every send, no per-family interpolation.
  - Body: a short, fixed sentence ("There's something new for your little
    one this week — activities, milestones, and a memory prompt are waiting
    for you.") plus a login-required CTA button/link to the in-app
    `/digest` panel (§5.0), plus the footer (unsubscribe link + mailing
    address, §5.5–5.6).
  - **No child name substitution, even as a personalization touch.** The
    original deferral's concern was specifically "a child's name and
    developmental stage leaving the machine... on a recurring, unattended
    basis" — the design answer is that neither ever does. What leaves the
    machine, per send, is: the caregiver's own email address (already known
    to the mail provider by virtue of being the recipient — this is
    unavoidable for any email delivery mechanism) and a fixed, content-free
    notification string. No profile data, no memory text, no milestone
    content, no photo-derived data (already excluded per §4.1 step 8's
    isolation) ever appears in an outbound email.
  - **All specifics require login.** The actual "Maya is 14 months this
    week" content (INDUSTRY_KB §1.4 point 5's example digest copy) is
    rendered only by the authenticated `/digest` in-app panel — the email's
    role is purely "come look," never "here is the content." This is a
    stronger privacy posture than a typical transactional-email design
    (most competitors in this category, per INDUSTRY_KB §1.4, do put the
    child's name/age directly in the email) and is a deliberate,
    stated trade-off: slightly less engaging email copy, in exchange for
    child-identifying data never leaving the local system via the email
    channel at all. This is architecture's call to make explicitly, the
    same way §6.1's streaming trade-off is stated explicitly rather than
    left implicit.

### 5.8 API key handling

`RESEND_API_KEY` in `.env`, following the exact pattern already established
for `PHOTO_ENCRYPTION_KEY`/`ANTHROPIC_API_KEY`/`OPENAI_API_KEY`
(SECURITY_KB §2.5): never committed, `.env` already gitignored per the
inherited template pattern, verified (not assumed) at Review gate. No new
secret-handling mechanism is introduced — this key is not more sensitive
than the LLM provider keys already handled this way, and does not warrant a
different pattern (e.g. keychain) for the same right-sizing reasoning
SECURITY_KB §2.1 already applied to `PHOTO_ENCRYPTION_KEY`. **Revisit
trigger, inherited from SECURITY_KB §2.6:** before any non-local deployment,
move to a proper secret manager rather than `.env`.

### 5.9 What is explicitly NOT built this run

- **No per-user send-time preference** (fixed 08:00 server time for
  everyone) — right-sized; a preference UI is a real feature with no
  corresponding requirement in F8's approved scope.
- **No email open/click tracking** — no tracking pixel, no click-through
  analytics on the CTA link. Adding either would mean Resend (or an
  analytics layer) recording *when a caregiver opens an email about their
  child* — exactly the kind of incidental, unnecessary third-party
  data-flow expansion the original privacy concern was about, and nothing
  in F8's requirement needs it. Stated explicitly as a deliberate omission,
  not an oversight.
- **No digest-frequency options** (weekly only, matching F8's approved
  scope) — a configurable cadence is a real feature, not built this run.
- **No re-engagement/win-back email sequence** — F8 is a standing opt-in
  weekly notification, not a marketing sequence; building the latter would
  be scope creep beyond the approved backlog item.

### 5.10 Seam preserved from the original design

`digest.py`'s `build_digest` (in-app content assembly) remains
delivery-agnostic, exactly as the original deferral noted — this revision
adds a delivery channel (`email_delivery.py` + `scheduler.py`) without
touching `build_digest` itself, confirming the original seam design was
correct even though the deferral decision built on top of it was overridden.

---

## 6. Output-side enforcement (beyond system-prompt instructions)

System-prompt rules (PLAN §3.4) are necessary but, per DOMAIN_KB R1/R2 and
the general behavior of LLMs under adversarial or merely unlucky phrasing,
not sufficient on their own — especially once F8's digest generation runs
unattended (no parent in the loop to notice a bad response the way a chat
turn is at least read before the parent acts on it). `app/guardrails.py` is
a **post-generation, code-level check layered on every LLM-touching
response path** (`/chat` streaming completion, `/digest` generation), plus
**serve-time filters that are not LLM-adjacent at all** for F9.

### 6.1 R1 anxiety-framing check (`guardrails.check_framing(text) -> Violation | None`)

Runs after the full response is assembled (streaming responses are checked
on the complete buffered text before being released to the client for
non-streaming paths like `/digest`; for `/chat`'s streaming response,
see the trade-off note below) against:
- A denylist regex/phrase set: "behind," "delayed" (in a child-comparison
  context — a simple substring check is intentionally over-inclusive here;
  false positives are cheap, a missed violation is not), "ahead of,"
  "percentile," "don't worry," "plenty of kids," any percentile-number
  pattern (`\d{1,2}(st|nd|rd|th)\s*percentile`).
- Pre-2022 milestone age patterns are structurally impossible if grounding
  (§1) is followed correctly (the model is never asked to originate an age),
  but as a backstop, `guardrails.py` also flags any numeric age pattern
  ("X months") that does not match one of the curated table's own bucket
  values when the response is discussing a milestone — this is a heuristic,
  not a hard block (free-text answers legitimately mention ages in other
  contexts, e.g. "many toddlers start around age 2 for potty training" is
  outside the CDC checklist's scope), logged for the red-team suite's
  review rather than auto-blocked.
- **On violation:** the response is not silently passed through. Behavior:
  the offending response is discarded and replaced with a fixed, safe
  fallback message ("Let's take that differently — [restated CDC-2022
  framing pulled directly from the curated table] — it's worth mentioning
  to your pediatrician if you're not seeing this yet.") plus the incident is
  logged (no PII beyond profile id, to a local log file, for
  responsible-ai-architect's red-team suite to review, not sent anywhere).

**Streaming trade-off, stated explicitly:** `/chat` is specified as a
streaming response (PLAN §4.1, template default). A true per-token
guardrail check that can swap out an in-flight stream requires either (a)
buffering the full response server-side before streaming to the client
(loses perceived latency, the one thing a streaming UI is for), or (b)
streaming optimistically and only being able to *append* a correction
after the fact, not retract already-rendered tokens. **Decision: buffer and
check server-side before streaming to the client for `/chat`.** The latency
cost (typically sub-second to low-seconds for a short parenting-chat
response) is an acceptable trade for a child-data product where R1/R2
violations are the highest-severity failure mode in this project — this is
architecture's call to make explicitly rather than let "streaming was the
template default" silently decide it. `/digest` was never streaming
(PLAN §4.4 describes it as a content-assembly function), so no trade-off
exists there.

### 6.2 R2 medical-deflection check (`guardrails.check_medical(text) -> Violation | None`)

Pattern-matches for dosage-shaped output (`\d+\s?(mg|ml|mcg)`, drug-name
list from a small fixed denylist: acetaminophen/Tylenol, ibuprofen/Motrin,
etc.) and diagnostic-assertion phrasing ("this is/sounds like/is likely
[condition]"). Same discard-and-replace behavior as §6.1, replacement text
is the fixed pediatrician-redirect template from PLAN §3.4(4). This is a
narrower, higher-precision check than §6.1's framing check because dosage
and diagnosis-assertion patterns are much less prone to false positives than
general anxiety-framing language.

### 6.3 F9 CPSC recall filter — not LLM-adjacent, but stated here for completeness

Confirms PLAN §4.5's design exactly: `products.py` applies
`cpsc_denylist.json` as a **serve-time filter over the already-curated
catalog**, i.e. `response_items = [i for i in catalog_items if i.category
not in denylist]`, evaluated on every request, not cached pre-filtered at
catalog-load time — this is deliberate: it means even if a denylisted
category is accidentally re-added to the catalog file later (a curation
mistake, §1.1), the filter still catches it at serve time without requiring
someone to remember to re-run a build step. The LLM has no code path into
`products.py`'s response construction at all (confirms PLAN's "never raw
LLM product output" — this isn't a guardrail *check*, it's a structural
absence of the capability, same category of control as F7's photo/LLM
isolation).

### 6.4 Test-gate ownership

`guardrails.py`'s unit tests (does the denylist/pattern logic work in
isolation) belong to test-agent's suite. Whether it actually *fires
correctly against the full R1/R2 adversarial transcripts* (PLAN §7-A,
§7-D15) is responsible-ai-architect's red-team suite — this is an
architecture-designed mechanism that responsible-ai-architect's suite
verifies in integration, a clean division matching each role's charter.

---

## 7. Architecture test-suite ownership (Test gate, this project)

Per the Test suite ownership contract, solution-architect owns:
- **Contract tests:** route-handler signature stability across the
  Increment-1→3 auth-seam swap (§2); `Store[T]` interface conformance for
  every entity store; `photo_theme.extract_accent` output always satisfies
  the clamped-band contract (property-based test: for N random hues,
  derived tokens fall within the specified S/L ranges) or returns `None`;
  **new (§5 revision): `email_delivery.send_digest_notification` contract
  test (mocked Resend call — correct headers, no child-identifying content
  in body, subject fixed) and `scheduler`'s due-check logic (property test:
  a user is selected iff `digest_opt_in=true` and `last_digest_sent_at` is
  null or ≥7 days old).**
- **Design-conformance checks:** SQLite foreign-key cascade behavior
  (`PRAGMA foreign_keys=ON` actually enforced — a common SQLite footgun if
  left at its default-off state; delete-a-family cascades every table);
  `guardrails.py` import isolation from `photos.py` and vice versa (shared
  static-import-graph check with F7's isolation requirement, §6.3);
  `milestones.py`/`products.py` never called from a route without the
  serve-time filter/grounding-block step present (i.e. no route bypasses
  the curated-data path); **new (§5 revision): static check that no
  profile/memory/child-name field is ever passed into
  `email_delivery.send_digest_notification`'s call site (the function's own
  signature — `to_email, unsubscribe_url` only — already makes this
  structurally hard to violate, verified rather than assumed).**
- Evidence recorded per-scenario in `projects/little-milestones/test-evidence/`,
  per test-agent's documented convention.

---

## 8. Completeness check against this gate's mandate

1. R3 grounding — resolved (§1): Option A, curated CDC-2022 table, owner +
   cadence assigned (§1.1).
2. Auth design — confirmed with architecture-level refinements (§2); full
   authn/authz reasoning is SECURITY_KB.md's dedicated section.
3. Photo storage/encryption — storage layout decided here (§3); encryption
   mechanism, key management, and compliance mapping is SECURITY_KB.md's;
   isolation-from-LLM structural design confirmed (§6.3, §4.1 step 8).
4. Photo color-extraction algorithm — fully specified (§4): server-side,
   upload-time, Pillow-based median-cut extraction, skin-tone exclusion,
   clamped HSL bands, hue-exclusion rotation, automated contrast pre-check
   with default-theme fallback, feeding the three `--lm-photo-*` tokens.
5. **Email/notification infrastructure — REVISED, real delivery designed
   (§5): Resend (transactional API, generous free tier), in-process
   APScheduler daily job (confirms the original fallback), content-free
   notification-only email body (no child name/age/milestone content —
   direct answer to the original privacy concern), real one-click
   unsubscribe independent of the in-app toggle (RFC 8058 headers + stable
   per-user token), CAN-SPAM addressed explicitly (mailing-address
   requirement flagged for human/deploy-agent, opt-out honored immediately),
   `RESEND_API_KEY` in `.env` per the existing secrets pattern.**
6. Storage backend — confirmed SQLite, schema sketched, cascade rules,
   backup posture (none) confirmed (§3).
7. Output-side enforcement — `guardrails.py` designed for R1/R2 (§6.1–6.2),
   F9's structural (non-LLM) filter confirmed (§6.3), streaming trade-off
   for `/chat` stated explicitly (buffer-then-check) rather than left
   implicit.

Cross-checked against DOMAIN_KB R1–R8: R1 (§6.1, plus UX_KB's payload/DOM
rules this KB does not re-litigate), R2 (§6.2), R3 (§1), R4 (unchanged from
PLAN §3.3, no architecture objection), R5 (unchanged, activity filtering is
`milestones.py`/`activities` data + system prompt, no new architecture
surface), R6 (§2 hard-delete via cascade, §3 no backups), R7 (§6.1's framing
check is the code-level backstop for the same tone requirement UX_KB
enforces visually), R8 (§6.3's structural CPSC filter; F11 RAG stays
out-of-scope, no architecture impact this run).

Cross-checked against INDUSTRY_KB compliance flags: no AI training on child
data/photos (§4.1 step 8 — nothing photo-derived reaches the LLM layer, and
no training pipeline exists in this project at all), no face processing
(§4.1 step 4's clarifying note — color-cluster heuristic, not facial
geometry), retention/delete (§3's cascade design + SECURITY_KB's delete
semantics), private-by-default (§3's filesystem-path-by-id design + routes
per PLAN §4.3, SECURITY_KB owns the authz check), contextual-only product
recs (§6.3, unchanged from PLAN). **§5's revision additionally cross-checks
CAN-SPAM (§5.6, not originally named by INDUSTRY_KB — flagged here as a gap
in that file worth noting for future intake reviews of any project adding
recurring email) and the state Age-Appropriate-Design-Code direction-of-
travel (§5.6, privacy-protective default unchanged).**

Cross-checked against UX_KB design contracts: §5's responsive strategy
requires no backend changes (it's a frontend/CSS concern; the API shapes
already support it) — noted here as confirmation, not a gap. §6's
photo-personalization contract is fully addressed by §4. UX_KB's R1
structural payload rules (no `expected_by`/`status`/`on_track` fields) are
PLAN's responsibility (§4.2) and this KB does not alter them.

**No disagreement between solution-architect and security-architect at this
gate** — see SECURITY_KB.md for security-architect's independent sign-off on
the auth and photo-encryption portions of this design. Any disagreement
would be flagged explicitly in both files; there is none to record. **This
applies to the original gate; §5's revision is solution-architect's design
alone per the human's direct override request — security-architect should
be (re-)consulted on §5's API-key handling (§5.8) and any new data-flow
implications before this revision is treated as jointly approved,
consistent with the joint-presentation requirement for the Architecture
gate.**

---

## 9. Increment 2 architecture follow-ups (solution-architect, 2026-07-11)

code-agent flagged two open design questions in the Increment-2 implementation
summary (`PROJECT_CONTEXT.md`) before the Test gate runs. Both resolved here.
Neither required security-architect co-review (no auth/encryption/data-flow
surface touched) or a human gate re-approval (both are within solution-
architect's "how, not what" authority over an already-approved F6/F7/F8
design) — recorded per the re-engagement requirement regardless, since both
are exactly the kind of "key design decision" that must not be silently
resolved by code-agent alone.

### 9.1 HEIC uploads — decision: close the gap, add `pillow-heif`

**Decision: (a), add `pillow-heif` as an approved dependency.** Not (b)
document-only.

**Reasoning:** SECURITY_KB §2's EXIF-GPS-stripped-on-upload commitment
(PLAN §4.3) is not a soft preference — it is the stated privacy guarantee
for a product whose entire premise is storing photos of children. HEIC is
not an edge-case format for this product's actual user base: it is Apple's
default capture format on every iOS device since iOS 11, and this product's
"parent uploads a phone photo of their kid" core flow means a large fraction
of real uploads will be HEIC. A silent, format-dependent gap in a stated
privacy commitment — where the code path exists and looks like it works
(upload succeeds, photo displays) but quietly skips the privacy-bearing step
for exactly the files most likely to carry embedded GPS data (phone camera
EXIF) — is a materially different risk than "a feature is incomplete." It is
the kind of gap that should not be closed by documentation alone when a
well-scoped fix exists.

`pillow-heif` is a mature, actively-maintained plugin (not a heavy or novel
dependency — it registers a Pillow-compatible codec, `pillow_heif.
register_heif_opener()`, after which `photos.py`'s existing Pillow-based
EXIF-strip and `photo_theme.py`'s existing extraction pipeline both handle
HEIC with zero pipeline-logic changes). This is a one-line dependency
addition plus one registration call, not a new architecture surface —
right-sized to close a real gap, not scope creep.

**What code-agent's next pass must do** (not implemented by
solution-architect — this is implementation work):
1. Add `pillow-heif` to the backend's dependency list (`pyproject.toml`/
   `requirements.txt`), alongside Pillow.
2. Call `pillow_heif.register_heif_opener()` once at app startup (e.g. in
   `main.py` or `db.py`'s init path, wherever other one-time startup
   registration lives).
3. Remove the current HEIC special-case (the `photo_exif_strip_failed`
   fallback-to-raw-bytes path in `photos.py`) for the format itself — HEIC
   should flow through the same EXIF-strip and `photo_theme.extract_accent`
   pipeline as JPEG/PNG once the plugin is registered, no separate code path.
4. Add regression tests: a real (or synthetically-constructed) HEIC fixture
   upload asserts EXIF-GPS is stripped and a theme accent is extracted, same
   assertions as the existing JPEG/PNG upload tests.
5. Verify `pillow_heif` doesn't reintroduce any dependency the plan's
   approved list was deliberately keeping out (it has no ML/network
   dependencies of its own — a pure C-library-backed codec binding — so no
   conflict expected, but this is code-agent's install-and-verify step, not
   an assumption to carry forward unchecked).

**Not a revisit-trigger deferral** — this is closed now, at the next
code-agent pass, before Test gate re-runs, since it is a real privacy-
commitment gap rather than a scoped-out feature.

### 9.2 Multi-photo theme-source tracking — decision: accept as a documented Increment-2 limitation

**Decision: (a), acceptable simplification for Increment 2.** No schema
addition (`theme_source_photo_id` FK or equivalent) this run.

**Reasoning:** unlike §9.1, this gap sits entirely in decorative UI
territory — UX_KB §6's photo-personalization theme is explicitly a
"decorative accent layer only" (per the Architecture-gate summary,
PROJECT_CONTEXT.md), structurally excluded from anything safety- or
privacy-bearing (no LLM reachability, no PII implication either way). The
worst-case user-facing outcome of the current behavior — deleting any one
photo resets the accent to the default theme even if other photos remain,
rather than recomputing from a remaining photo — is a mildly surprising
visual reset, not a data-loss, privacy, or correctness problem in any of the
senses this project's Architecture/Security/Responsible-AI gates actually
care about. It is also self-healing: uploading any new photo (or the parent
noticing and re-uploading) immediately recomputes a theme, and the "last-
upload-wins" model code-agent implemented is a coherent, simple mental model
in its own right, not an obviously-broken one.

Adding `theme_source_photo_id` now would be real, non-trivial scope: a
schema migration, delete-time "find the next-most-recent remaining photo
and recompute" logic, and a UX_KB decision (not solution-architect's alone)
about whether "falls back to next-most-recent" is even the experience
design wants, versus e.g. "always resets, re-upload to re-theme" being fine
by design. Building the schema/logic side of that before UX_KB has actually
specified the desired multi-photo behavior would risk building the wrong
thing.

**Documented as a known Increment-2 limitation, with an explicit revisit
trigger:** revisit if either (a) a future increment's UX_KB revision
specifies multi-photo theme-fallback behavior explicitly (at which point
this becomes a scoped, spec'd feature rather than a speculative one), or
(b) red-team/UX testing at a future Test gate finds the reset-to-default
behavior is confusing or objectionable enough in practice to warrant fixing
ahead of a UX_KB revision. Until then, code-agent's existing implementation
(§Increment 2 judgment call 2 in PROJECT_CONTEXT.md) stands as designed.
`ARCHITECTURE_KB.md` §4.2 has been annotated to point here.
