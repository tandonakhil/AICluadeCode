# Project: little-milestones

## Overview
- Template: genai-chatbot (recommended by plan-agent, human-confirmed)
- Created: 2026-07-10
- Target environment: local (cloud-dev/cloud-prod deferred, see admin/ROADMAP.md)
- Current stage: Increment 1 (F1-F5) code built 2026-07-10, pending Test gate

## Full described scope (human's original request, verbatim intent)
A website to track infant-to-toddler details: kid profile created up front,
picture upload, best activities to do at each age as the kid grows, buying
recommendations as the kid grows, an interactive chat window for questions at
each milestone, and a "really cool life journey" visualization at a point in
time on a button click.

## This run vs. later (human-approved split, 2026-07-10 — supersedes plan-agent's first-slice proposal)
- **This pipeline run (F1–F10, human-selected via itemized backlog review)**:
  kid profiles, age computation, guarded milestone chat, activity
  suggestions, disclaimer, memory log + life-journey timeline, photo upload
  + storage (with its compliance preconditions pulled into scope:
  retention/delete, encryption at rest, private-by-default, no face
  processing, no AI training on child photos), weekly opt-in digest, buying
  recommendations with CPSC recall filtering, and multi-caregiver access.
  Built in three internal increments with per-increment gates — see PLAN.md
  §4.7.
- **Later via /enhance-project**: F11 only — a RAG-grounded answering mode,
  conditional on a vetted pediatric-guidance corpus ever being introduced.
- **Flagged for Architecture gate**: R3 milestone grounding, auth design
  (forced by F10), photo storage/encryption design (forced by F7),
  email/notification infrastructure (F8), storage backend (JSON vs. SQLite).
  See PLAN.md §6. **Resolved 2026-07-10 at the Architecture gate — see
  Architecture Summary below; pending human approval.**

## Architecture Summary
**Architecture gate held 2026-07-10 — pending human approval.** Jointly
designed by solution-architect (`knowledge/ARCHITECTURE_KB.md`) and
security-architect (`knowledge/SECURITY_KB.md`, joint owners), with
responsible-ai-architect advisory (`knowledge/RESPONSIBLE_AI_KB.md`, this
project's first). No disagreement among the three roles. Resolves all six
PLAN.md §6 open questions plus output-side enforcement:

1. **R3 grounding — Option A, curated CDC-2022 table.** Adopts
   functional-agent's DOMAIN_KB position: `app/data/milestones_cdc2022.json`
   + activities table, hand-curated, injected into the prompt/served
   directly. Curation ownership: solution-architect, with
   responsible-ai-architect co-review on framing changes; update triggered
   by CDC/AAP revisions or CPSC recalls, not a calendar cadence. Same
   discipline extended to F9's product catalog + CPSC denylist.
2. **Auth — baseline confirmed with refinements.** Local email+password,
   argon2id (`passlib`), server-side sessions (hashed tokens in SQLite),
   HTTP-only/SameSite=Lax/conditionally-Secure cookies, owner/caregiver
   roles, single-use expiring invites, cross-family access = 404. No OAuth,
   no magic-link, no MFA this run; no self-service password reset this run
   (documented gap, revisit when email infra ships). Full reasoning +
   revisit triggers in SECURITY_KB.md §1 (dedicated, non-collapsible
   section).
3. **Photo storage/encryption — confirmed.** Bytes on filesystem
   (id-derived paths, gitignored), Fernet (AES+HMAC) application-level
   encryption, key in `.env` for local dev (revisit before non-local
   deploy), decrypt-on-serve, no static mount, EXIF-GPS stripped, hard
   delete = unlink-then-DB-row-delete (crash-safe ordering), no automatic
   backups. SQLite DB file itself not separately encrypted this run
   (named gap, revisit trigger set) — photo bytes and credentials are
   already covered by their own mechanisms regardless.
4. **Photo color-extraction algorithm — specified.** Server-side, upload-
   time, Pillow-based: downsample → median-cut/k-means quantize → filter
   near-gray + skin-tone-band clusters → pick dominant remaining cluster →
   clamp to three HSL bands (`--lm-photo-mid/-deep/-tint` per UX_KB §6.3) →
   hue-rotate if near `--lm-danger` → automated WCAG contrast pre-check
   with fixed-scrim compositing → fallback to default theme (not an
   unchecked accent) if it still fails. Only three hex values ever leave
   the pipeline; nothing photo-derived reaches the LLM layer.
5. **Email/notification infra (F8) — REVISED 2026-07-10, real delivery
   (human override).** The original gate's deferral was overridden by the
   human same-day; `knowledge/ARCHITECTURE_KB.md` §5 was fully replaced
   (not appended) with a real-delivery design: **Resend** as the
   transactional email provider (generous free tier fits this project's
   scale, minimal API, first-class custom-header support needed for
   one-click unsubscribe), **in-process APScheduler** daily job (confirms
   the originally-documented fallback rather than revising it), sent via a
   thin `app/email_delivery.py` wrapper. The original privacy concern (a
   child's name/stage leaving the machine to a third party on an
   unattended, recurring basis) is addressed directly, not dropped: the
   email body is a **fixed, content-free notification only** — no child
   name, DOB, age, or milestone content ever appears in an outbound email;
   all specifics require login to the in-app `/digest` panel. A **real
   one-click unsubscribe** (`GET /digest/unsubscribe?token=...`,
   unauthenticated by design, RFC 8058 `List-Unsubscribe-Post` header,
   stable per-user token) exists independent of the in-app opt-in toggle.
   CAN-SPAM was checked explicitly (a gap INDUSTRY_KB itself did not name)
   and is complied with — mailing-address requirement flagged for
   human/deploy-agent to supply before the scheduler runs against real
   users. `RESEND_API_KEY` handled via `.env`, same pattern as existing
   secrets. **security-architect's independent review completed 2026-07-10
   — see the Decisions Log entry below: approved conditional on two
   concrete additions to the unsubscribe route (scoping enforcement +
   rate limiting) and a new privacy-policy/vendor-disclosure item for
   Resend as a third-party processor; API-key handling itself confirmed
   consistent with no changes needed.**
6. **Storage backend — confirmed SQLite.** Single gitignored file,
   `PRAGMA foreign_keys=ON`, `ON DELETE CASCADE` across
   families→users/profiles→memories→photo_meta; photo bytes stay on
   filesystem, never DB blobs; no automatic backups (a backup is a
   liability under the delete promise until the human requests export).
   (§5's revision adds two columns to `users` — `last_digest_sent_at`,
   `unsubscribe_token_hash` — documented in ARCHITECTURE_KB §5.4.)
7. **Output-side enforcement — `app/guardrails.py`.** Post-generation
   code-level checks for R1 (anxiety-framing denylist/pattern checks) and
   R2 (dosage/diagnosis pattern checks) on both `/chat` and `/digest`
   (digest gets no relaxation — unattended generation, PLAN §3.5 in
   RESPONSIBLE_AI_KB). `/chat` streaming is buffered server-side and
   checked before release to the client — an explicit latency trade-off
   stated rather than left to the template's streaming default. F9's CPSC
   filter is structural (serve-time catalog filter with no LLM code path),
   not a guardrail check.

Responsible-AI baseline (first `RESPONSIBLE_AI_KB.md` for this project):
content/behavior boundaries for R1 (never "behind"/"ahead," reassurance
must always pair with CDC framing + pediatrician suggestion), R2 (hard
refusal on diagnosis/dosing/triage, red-flag list never minimized or
excused by corrected age), and appropriate-use boundaries beyond
correctness (chat must not become a product-recommendation side door
around F9's catalog filter; no cross-child comparison; EI/diagnosed-
condition disclosures must be acknowledged, not overridden by generic
framing). Seven red-team scenarios specified for the Test-gate suite,
including a tone-matching-escalation probe and a persistent-unlock probe
that a keyword denylist alone would not catch.

Full detail, rationale, and trade-offs: `knowledge/ARCHITECTURE_KB.md`,
`knowledge/SECURITY_KB.md`, `knowledge/RESPONSIBLE_AI_KB.md`.

## Increment 1 implementation summary (code-agent, 2026-07-10)

F1-F5 built for real against the Architecture/Security/Responsible-AI gate
design, plus the Increment-1 seams PLAN §4.7 calls for. All 30 backend
tests pass (`pytest`); frontend type-checks and builds cleanly (`tsc
--noEmit`, `next build`).

**Backend** (`dev/backend/app/`): `db.py` (full SQLite schema for every
F1-F10 entity — families/users/sessions/profiles/memories/photo_meta/
invites — `PRAGMA foreign_keys=ON`, idempotent `init_db()`, 0600 file
perms); `ages.py` (chronological + corrected age via an adjusted-DOB
`relativedelta` approach, CDC-2022 bucketing, newborn/out-of-range mode);
`profiles.py` (minimal-fields model + family-scoped `ProfileStore`, hard
delete); `auth.py` (the Increment-1 seam — `get_current_family` always
resolves to the seeded default family; argon2id hashing helpers wired up
but not yet reachable from any route); `data/milestones_cdc2022.json` +
`milestones.py` (curated CDC/AAP milestone + activity table, 10 checklist
buckets); `prompts.py` (system-prompt assembly: persona, server-computed
child context, R1/R2/R5 hard rules, disclaimer, grounding block);
`guardrails.py` (post-generation R1 framing-denylist + R2 dosage/
diagnostic-assertion checks, discard-and-replace, no-PII incident
logging); `routes/{profiles,chat}.py` + assembly-only `main.py`.

**Frontend** (`dev/frontend/`): a real Next.js App Router build replacing
the placeholder — onboarding (welcome/name/birthday/born-early/ready per
UX_KB's exact sensitive copy), profile switcher with typed-confirmation
hard delete, milestone chat (age-context strip, corrected-age explainer,
pediatrician-note card), Today (activity cards + coming-next), a
persistent disclaimer footer, and the UX_KB §5.1 responsive shell (bottom
tab bar under 1024px, sidebar nav at/above it, Today's 2-column grid at
the same breakpoint).

**Judgment calls made during Increment 1** (documented per the Code-gate
brief, not silently decided):
1. **SQLite thread affinity**: `sqlite3.connect(..., check_same_thread=False)`
   was required — FastAPI's sync route handlers run in Starlette's
   threadpool, so a connection created on one thread must be usable from
   the worker thread handling the request. Each request still gets its
   own connection via `get_db`'s yield-per-request pattern; this doesn't
   introduce cross-request sharing.
2. **`X-LM-Disclaimer` header uses an ASCII-safe variant** of the
   disclaimer (em dash replaced with a hyphen) — the real disclaimer text
   is not Latin-1 encodable and would break HTTP header transmission.
   `DISCLAIMER` (full text) is still used in the system prompt, UI, and
   JSON payloads; `DISCLAIMER_HEADER_SAFE` is header-only.
3. **CDC-2022 milestone content was reconstructed from general model
   knowledge, not a live fetch** (no web-search tool available in this
   environment, same constraint ui-ux-designer noted for competitor
   research). The table is structured, sourced, and flagged (`_meta`
   block) per ARCHITECTURE_KB §1.1, but a pre-production content review
   against the actual cdc.gov checklist pages is an open follow-up, not
   yet done — recommended before Test-gate red-team sign-off treats the
   content as authoritative.
4. **Newborn-mode activities reuse the 2-month bucket's curated
   activities** (there is no separate newborn bucket in the curated
   table below 2 months) rather than a bespoke newborn activity set —
   right-sized for Increment 1; flagged for review if red-team finds any
   2-month activity unsuitable for a 3-week-old.
5. **No Tailwind/shadcn build-out.** `package.json` lists `tailwindcss`
   per the template, but no config scaffolding (`tailwind.config.js`,
   `postcss.config.js`) existed in the repo, and TEMPLATE_MANIFEST's
   "shadcn/ui" claim had no corresponding files either. Rather than spend
   Increment-1 budget standing up a utility-class pipeline neither the
   Plan nor UX_KB requires by name, styling is hand-written CSS using the
   exact UX_KB §4.2 token values. Revisit only if a later increment's
   design surface genuinely benefits from a component library.
6. **`/chat` is not truly streamed**, per ARCHITECTURE_KB §6.1's own
   explicit trade-off (buffer full response server-side, run guardrails,
   release once): the route calls `model.invoke(...)` (not `.stream(...)`).
   **Correction (2026-07-11, review-agent):** as of finding-4's fix
   (`94fc502`), the response is a plain `JSONResponse` (`{"text":
   ..., "disclaimer": ...}`), not `StreamingResponse` — the buffer-then-
   guardrail-check trade-off itself is unchanged, only this sentence's
   technical claim about the response type was stale.
7. **Frontend age display in the profile switcher is a simple client-side
   month count**, not corrected age — it's a quick list label only; every
   surface that does real milestone/corrected-age framing (Today, Chat)
   uses the server's `/profiles/{id}/activities` response, never
   recomputes age logic client-side.
8. **No router modules for memories/photos/digest/products/auth were
   created this increment** (`app/routes/` has only `profiles.py` and
   `chat.py`). PLAN §4.1 says code-agent should set up the router-split
   structure "as routes accumulate" — since only F1-F5 are in scope this
   increment, stub routers for not-yet-built features were judged as
   unstated scope addition rather than a required seam; `main.py`'s
   `include_router` pattern makes adding them in Increment 2 additive, not
   a refactor.

**Not built this increment** (Increment 2-3 per PLAN §4.7, confirmed out
of scope): F6 (memories/timeline), F7 (photo upload/encryption), F8
(digest — content or delivery), F9 (product catalog/CPSC filter), F10
(real signup/login/invites — only the `get_current_family` seam and
argon2id helper exist).

## Increment 2 implementation summary (code-agent, 2026-07-11)

F6 (memory log + life-journey timeline), F7 (photo upload + storage), and
F8-content (in-app "This week" digest) built against PLAN §4.2-§4.4 and
the Architecture/Security gate designs in `knowledge/SECURITY_KB.md` §2
and `knowledge/ARCHITECTURE_KB.md` §4. All 88 backend tests pass
(`pytest`, up from 30 at the end of Increment 1); frontend type-checks and
builds cleanly (`tsc --noEmit`, `next build`). F1-F5 code was left
untouched except where F6/F7 genuinely needed to extend it (the
`photo_meta.id` schema type and `routes/profiles.py`'s delete handler,
both noted below).

**Backend** (`dev/backend/app/`): `memories.py` (`Memory` + family-
transitively-scoped `MemoryStore`; `moment_date` validated >= DOB and <=
today, the DOB half enforced at the route layer since the Pydantic model
has no profile context); `timeline.py` (pure function: chronological merge
of memory entries carrying server-computed age-at-moment with passed-
checklist-bucket chapter markers — the R1 hard rule is structural, not a
filter: the payload shape has no field for "expected," so nothing renders
one); `routes/memories.py`. `photos.py` (`PhotoMeta` + `PhotoStore`:
Fernet-encrypted bytes on the filesystem, content-sniffed upload
validation via magic bytes — not extension/claimed-type — EXIF stripped
on upload, files-first-then-metadata delete ordering with verified purge,
per-photo-delete and per-profile-cascade both covered); `photo_theme.py`
(the ARCHITECTURE_KB §4 color-extraction pipeline: Pillow downsample ->
median-cut quantize (k=5) -> skin-tone/near-gray cluster filter -> clamp
to 3 HSL bands -> hue-rotate within 20° of `--lm-danger` -> WCAG AA
contrast pre-check -> `None` on any failure, caller falls back to the
default theme); `routes/photos.py` (upload/serve/delete, zero static
mount); `digest.py` (`build_digest` — pure content assembly, reuses
`ages.py`/`milestones.py`/the R1 framing rules + F6's last-memory date;
content only, no opt-in/scheduler/email per PLAN's explicit Increment-3
split); `routes/digest.py`.

**Frontend** (`dev/frontend/`): `JourneyScreen.tsx` (the "life journey"
tab — matches `design-review/journey/timeline.html`'s river layout);
`AddMemoryForm.tsx` (matches `design-review/screens/photo-upload.html` —
title/note/date/optional-tag entry with staged local photo previews,
uploaded once the memory exists); `DigestPanel.tsx` (the in-app "This
week" panel, wired into `TodayScreen`, fails quietly rather than blocking
Today if the digest call errors). `lib/types.ts`/`lib/api.ts` extended
with the F6/F7/F8 types and fetch wrappers, including `photoUrl()` which
always resolves through the family-scoped API route.

**Judgment calls made during Increment 2** (documented per the Code-gate
brief, not silently decided):
1. **`photo_meta.id` changed from an autoincrementing integer to a TEXT
   `uuid4` hex** in `db.py`'s schema (an F1-era schema line, touched
   because F7 genuinely needs it): the id also names the on-disk file
   (`backend/data/photos/{profile_id}/{photo_id}`), and a random,
   non-enumerable id is the right shape for something that doubles as a
   filename an attacker might try to guess. No migration was needed or
   written — no production photo data exists yet at this stage of the
   pipeline; the dev-only `little_milestones.db` file was deleted and
   regenerates from the new schema on next startup.
2. **Photo-theme "which photo currently powers the theme" simplification**:
   ARCHITECTURE_KB §4.2 describes "delete clears the three columns...
   replace re-runs the pipeline" without specifying how a profile with
   *multiple* photos tracks which one is the theme's source (no
   `is_theme_source` flag exists in the schema). Implemented as: every
   successful upload's extraction overwrites the profile's current accent
   (last-uploaded-wins); deleting *any* photo resets the accent to the
   default theme rather than recomputing from a remaining photo. This is
   a real simplification of the multi-photo case, not a bug — flagged for
   Architecture/UX review if a future increment wants "delete just falls
   back to the next-most-recent photo's theme" instead. **Resolved
   2026-07-11 — see the Decisions Log entry below and ARCHITECTURE_KB §9.2:
   accepted as a documented Increment-2 limitation, no schema change this
   run.**
3. **EXIF handling strips all EXIF metadata, not GPS tags only.** PLAN
   §4.3 specifically calls for GPS stripping; the implementation strips
   the entire EXIF block on re-save (simpler, and strictly more private —
   a floor, not a ceiling, on the stated requirement).
4. **HEIC uploads are accepted by content-sniff (magic bytes) but are not
   run through the EXIF-strip/color-extraction pipeline** in this
   environment, since Pillow can't decode HEIC without the optional
   `pillow-heif` plugin (not part of the plan's approved dependency list,
   and Architecture's photo-pipeline design named Pillow alone as
   sufficient). A HEIC upload is still validated, capped, and encrypted at
   rest; it just falls back to storing the original bytes unmodified
   (logged as `photo_exif_strip_failed`) and never contributes a photo
   accent. Flagged as a real gap for security-architect/solution-architect
   to confirm is acceptable, or to add `pillow-heif` as a dependency in a
   follow-up. **Resolved 2026-07-11 — see the Decisions Log entry below and
   ARCHITECTURE_KB §9.1: gap closed, `pillow-heif` approved as a new
   dependency, implementation steps specified for code-agent's next pass.**
5. **Timeline chapter-marker anchor dates use chronological DOB +
   bucket_months**, not a corrected-age-adjusted date, purely for
   interleaving position on the calendar timeline — this is a placement
   detail, not a milestone claim (the marker's only content is a neutral
   month-count label), so it doesn't need the same corrected-age handling
   that milestone *content* elsewhere in the app does.
6. **`routes/profiles.py`'s delete handler was extended** (the one F1-era
   route file genuinely touched by F7) to unlink all of a profile's photo
   files before the DB's `ON DELETE CASCADE` removes the `memories`/
   `photo_meta` rows — SQLite cascades handle metadata, never filesystem
   bytes, so this had to be explicit (SECURITY_KB §2.4's stated ordering).
7. **`digest.py`'s route return type is `dict`, not the `DigestPayload`
   TypedDict**, because `DigestPayload.activities` nests
   `milestones.Activity`, a `typing.TypedDict` from Increment-1 code
   (left as-is per this increment's "don't touch F1-F5" instruction) —
   pydantic v2 on this project's Python 3.9 runtime can't build a
   response-model schema from a plain `typing.TypedDict` used as a route
   return annotation. `DigestPayload` remains a real internal type for
   `digest.py`'s own callers/tests; only the route's declared return
   annotation is loosened.
8. **Pre-existing uncommitted Increment-1 diffs found in the working tree
   at the start of this run** (`app/guardrails.py`, `routes/chat.py`,
   `tests/test_guardrails.py`, `frontend/next-env.d.ts` — apparent
   stale-age-backstop and `next-env.d.ts` regeneration work, not attributed
   to this session) were left untouched and unstaged: not part of F6/F7/F8
   scope, and not mine to commit or discard. Flagged for the human/whoever
   owns that in-flight change to commit or revert explicitly.

**Not built this increment** (Increment 3 per PLAN §4.7, confirmed out of
scope): F8 delivery (opt-in, scheduler, email/notification channel), F9
(product catalog/CPSC filter), F10 (real signup/login/invites/roles).

## Increment 3 implementation summary (code-agent, 2026-07-11)

F9 (buying recommendations + CPSC filtering), F10 (real auth activation +
multi-caregiver), and F8 delivery (Resend email + scheduler + unsubscribe)
built against PLAN §4.5-§4.6 and `knowledge/ARCHITECTURE_KB.md` §5
(real-delivery revision) / `knowledge/SECURITY_KB.md` §1 (auth design,
dedicated non-collapsible section) in full. **165 backend tests pass**
(`pytest`, up from 101 at the end of Increment 2 -- 64 new tests: 30 auth,
16 products, 8 email delivery, 9 scheduler, 8 unsubscribe-route -- exact
counts overlap slightly across files); both `python -m pytest -v` and
plain `pytest -v` from `dev/backend/` report identical 165/165 (finding-7
parity re-confirmed a third time). Frontend `tsc --noEmit`/`next build`
both clean. F1-F8(content) code was left untouched except where F9/F10
genuinely needed to extend it: `get_current_family`'s body (the
Increment-1 seam, exactly as designed), `routes/profiles.py`'s and
`routes/photos.py`'s delete handlers (added the owner-only role check),
`routes/digest.py` (added the unsubscribe route alongside the unchanged
Increment-2 digest-content route), `db.py`'s schema (one additive column,
one migration helper), `main.py` (new routers + conditional scheduler
startup), and `tests/conftest.py` (see judgment call 1 below -- this is
the one broad, deliberate change).

**Backend** (`dev/backend/app/`):

- **F9**: `products.py` (`get_products_for_bucket` -- catalog load +
  **serve-time** CPSC-denylist filter, evaluated on every call, not cached
  pre-filtered) + `data/products_catalog.json` (10 checklist buckets x 2
  curated categories, `_meta` block, no brands/SKUs/tracking) +
  `data/cpsc_denylist.json` (12 recalled/banned/AAP-warned categories) +
  `routes/products.py` (`GET /profiles/{id}/products`, same
  newborn/out-of-range/corrected-bucket pattern as `/activities`).
- **F10**: `users.py` (`User`/`Invite` models, `UserStore`/`InviteStore`/
  `FamilyStore`); `auth.py` rewritten from the Increment-1 stub into the
  real thing -- session creation/resolution (opaque
  `secrets.token_urlsafe(32)`, SHA-256-hashed at rest, 30-day sliding /
  90-day absolute expiry), `get_current_family`'s body now resolves from
  the real session (its signature and every route's
  `Depends(get_current_family)` declaration are byte-for-byte unchanged,
  confirming ARCHITECTURE_KB §2's contract), `require_owner` (a new,
  additive dependency used only on the three owner-gated routes), an
  in-process fixed-window rate limiter (`check_rate_limit`), cookie
  helpers (`HttpOnly`/`SameSite=Lax`/conditionally-`Secure`).
  `routes/auth.py` (`POST /auth/signup|login|logout|join`, `POST
  /invites` owner-only, `GET`/`PATCH /auth/me` for the per-caregiver
  digest-opt-in toggle -- not explicitly named in PLAN's route list but
  required by its own frontend requirement).
- **F8 delivery**: `email_delivery.py` (thin Resend wrapper,
  `send_digest_notification(to_email, unsubscribe_url)`, fixed
  content-free HTML body, RFC 8058 `List-Unsubscribe`/
  `List-Unsubscribe-Post` headers, `MAILING_ADDRESS` placeholder flagged
  inline); `scheduler.py` (`run_digest_job` -- the exact due-check query
  + per-user try/except from ARCHITECTURE_KB §5.3 -- and
  `start_scheduler`/`shutdown_scheduler`, an in-process APScheduler
  `BackgroundScheduler`); two new `users` columns
  (`last_digest_sent_at`, already present from Increment 1's forward-
  looking schema; `unsubscribe_token`, new this increment, see judgment
  call 2); `routes/digest.py` extended with `GET
  /digest/unsubscribe?token=...` (unauthenticated, idempotent, rate-
  limited, a structurally single-purpose `UPDATE ... SET digest_opt_in =
  0` per SECURITY_KB §1.7 point 3, a confirmation page with zero
  external resource loads/links per §1.7 point 5). `main.py`'s startup
  hook only calls `start_scheduler()` when `ENABLE_DIGEST_SCHEDULER=true`
  is set in `.env` -- **left unset in this environment**, since no
  verified Resend sending domain exists yet (ARCHITECTURE_KB §5.1's
  stated operational precondition; flagged again in the report to the
  human/Test gate, not silently worked around).

**Frontend** (`dev/frontend/`): `AuthScreen.tsx` (signup/login/join,
storybook-warm styling reusing `.lm-onboarding`/`.lm-field`/`.lm-btn`
rather than inventing new visual language); `SettingsScreen.tsx` (family
panel with plain-words role labels, owner-only invite generation, the
per-caregiver digest toggle default-off, the documented no-password-reset
gap as UI copy, logout); `ProductsPanel.tsx` ("Ideas for this stage" on
Today, deliberately identical card anatomy to the activity-card family
per UXR-11 -- no distinct "product card" style). `app/page.tsx` now
gates the whole app shell behind a session check (`getMe()`), adds a
Settings nav entry to both the sidebar and bottom tab bar, and wires
logout to reset local state. `lib/api.ts`'s `request()` now sends
`credentials: "include"` on every call (required for the session cookie
to cross the :3000 -> :8000 origin boundary, paired with the backend's
new `allow_credentials=True` CORS setting) -- the two non-`request()`
fetch calls (`sendChatMessage`, `uploadPhoto`) were updated the same way.
**Design-gap flag**: no `design-review/` mockup exists for the
auth/signup/login/join, Settings/invite, or product-recommendation
screens -- confirmed absent by search, not overlooked. UX_KB.md §1.7
specifies the *flow and exact copy* for all three (Flow 3a/3b/3c) but no
visual mockup was produced for them at any Experience Design gate pass.
The screens above are functional implementations matching that copy and
reusing the established component language (cards, pill buttons,
one-column forms); they have **not** been through visual design review
and should be treated as a real gap for ui-ux-designer to close, not a
silent substitute for one.

**Judgment calls made during Increment 3** (documented per the Code-gate
brief, not silently decided):

1. **`tests/conftest.py`'s `client` fixture now authenticates a default
   user before yielding, rather than every existing test file being
   individually rewritten to sign up/log in.** This is the mechanism that
   satisfies PLAN §7-J item 37 ("the full Increment-1 red-team/
   adversarial suite must re-pass under an authenticated session") for
   every test in this pytest-based suite: since `TestClient` persists
   cookies across requests within one instance (the same way a browser
   does), authenticating once at fixture setup means all 101 pre-existing
   Increment-1/2 tests (profiles, ages, activities, guardrails,
   memories/timeline, photos, digest content) now genuinely exercise
   their original behavior through a real session, not a bypassed one --
   confirmed by full-suite re-run (165/165 passing, no test file's
   assertions needed to change). A new `unauthenticated_client` fixture
   (no signup) was added alongside it for tests that need to control
   authentication themselves (auth flows, 401 checks, cross-family
   isolation). This is also why `client`'s authenticated user becomes
   this test process's "first user ever" and lands as owner of
   `family_id=1` -- every existing test's implicit `family_id=1`
   assumption keeps holding, which is the same migration behavior
   ARCHITECTURE_KB §2 specifies for real production signups.
2. **Added a plaintext `users.unsubscribe_token` column beyond what
   ARCHITECTURE_KB §5.4 literally specifies** (which names only
   `unsubscribe_token_hash`, mirroring session-token hash-only storage).
   A hash is one-way; it cannot be turned back into the raw token
   `scheduler.py` needs to embed in each week's outbound email URL, and
   §5.4 explicitly wants a *stable* link reused across every send (not a
   fresh token minted per send, which single-use/rotating tokens would
   force). `unsubscribe_token_hash` remains the sole verification
   mechanism the incoming `GET /digest/unsubscribe` request is checked
   against, exactly as specified -- this column is additive, not a
   substitution. Flagged here for solution-architect/security-architect
   to confirm or revise; worst case on either value's compromise is
   unchanged from SECURITY_KB §1.7 point 1's existing assessment (an
   unwanted opt-out of a weekly email, not an account/data breach).
3. **`require_owner` is checked before the cross-family/existence check**
   on `DELETE /profiles/{id}` and `DELETE /profiles/{id}/photos/{id}`
   (FastAPI dependency order): a caregiver session gets 403 for *any*
   profile/photo id, including one that doesn't exist or belongs to
   another family, before the route body ever looks up the resource. This
   doesn't leak anything about the specific resource (role is a property
   of the session, not the target), and keeps the two checks cleanly
   separated (coarse-grained role gate, then fine-grained
   ownership/existence gate) -- flagged as a design choice, not
   independently re-derived per PLAN/ARCHITECTURE_KB, since neither
   document specifies the ordering for the caregiver-cross-family-delete
   combination specifically.
4. **`/auth/me` (`GET`/`PATCH`) is a new route pair not explicitly named
   in PLAN §4.6's route list** (`POST /auth/signup|login|logout`, `POST
   /invites`, `POST /auth/join` are the only ones named). It exists
   because PLAN's own frontend requirement -- "per-user digest opt-in
   toggle (default off)" -- has no other way to read or write the current
   session's `digest_opt_in` without it. Scoped minimally: `PATCH
   /auth/me` accepts only `{digest_opt_in: bool}`, nothing else.
5. **CORS `allow_credentials=True` and every frontend fetch call's
   `credentials: "include"`** were added as a necessary consequence of
   session cookies now existing at all -- not called out in PLAN/
   ARCHITECTURE_KB explicitly, but a cross-origin cookie-based session
   (frontend `:3000`, backend `:8000`) does not work without both sides
   of this. Also required: `crossOrigin="use-credentials"` on
   `JourneyScreen.tsx`'s `<img>` tags for photo bytes, since a plain
   cross-origin `<img>` does not send cookies by default -- without this,
   every existing photo in the Journey view would have silently 401'd
   once auth went live, a real regression risk this fix closes.
6. **Rate-limit state (`app.auth._RATE_BUCKETS`) is process-global, not
   per-request or per-connection** -- an in-process fixed-window counter,
   per SECURITY_KB §1.5's own specified mechanism ("no external
   dependency needed at this scale"). `reset_rate_limits()` is a
   test-only helper to prevent state leaking between test cases sharing
   the same Python process; it is never called from application code.
7. **Invite codes are `secrets.token_urlsafe(32)[:12]`** (truncating the
   same high-entropy generator already used for session/unsubscribe
   tokens) rather than a separately-tuned `secrets.token_urlsafe(9)` call
   -- SECURITY_KB §1.1 specifies "~12 chars, base64url" for invite codes,
   which this achieves via one shared generator instead of a second
   entropy-source configuration to reason about separately. Truncating a
   URL-safe base64 token is safe (no encoding-boundary issue) and the
   resulting ~12-char prefix still carries far more entropy than needed
   given the rate-limited, single-use, 7-day-expiring design.
8. **F8 delivery is genuinely not enabled in this environment.** This is
   not a code gap -- `email_delivery.py`, `scheduler.py`, and the
   unsubscribe route are fully built and tested (mocked Resend calls
   throughout; zero real network calls in the test suite) -- it is the
   stated operational precondition from ARCHITECTURE_KB §5.1 (no
   verified Resend sending domain) staying unmet. `ENABLE_DIGEST_
   SCHEDULER` defaults to unset/false; `RESEND_API_KEY` is unset in this
   `.env`. Flagged explicitly for the human/Test gate/deploy-agent, per
   the Code-gate brief's specific instruction not to silently skip this.
9. **`MAILING_ADDRESS` in `email_delivery.py` is a placeholder string**,
   not a real address -- ARCHITECTURE_KB §5.6 states this is a
   business/operational detail outside code-agent's authority to invent.
   `test_email_delivery.py::test_email_body_contains_mailing_address_
   placeholder_flag` locks in that the placeholder is present (and would
   need updating alongside any future change that fills in a real
   address) rather than letting it silently drift.

**Not built this increment / explicitly deferred, matching
ARCHITECTURE_KB's own "what is explicitly NOT built" list (§5.9) and
SECURITY_KB's revisit triggers (§1.6)**: no per-user digest send-time
preference, no email open/click tracking, no digest-frequency options, no
self-service password reset (documented gap, unchanged from Increment 1),
no MFA/OAuth/magic-link (F12, later backlog per human request, already
recorded in FEATURES.md).

## Increment 4 implementation summary (code-agent, 2026-07-12)

F14 (profile avatars + upload affordance), F15 (Journey lightbox), and F16
(Journey gallery view) built against `knowledge/UX_KB.md` §8/§8.1a and
`knowledge/ARCHITECTURE_KB.md` §9.3 in full, per the Experience Design +
Architecture consult approved 2026-07-12. **173 backend tests pass** (up
from 168, both `python -m pytest` and plain `pytest` agree); **34 frontend
tests pass** (up from 13); `tsc --noEmit` and `next build` (via
`NEXT_DIST_DIR=.next-build`, run against an isolated dist dir so the live
`:3000` dev server was never touched) both clean.

**Backend** (`dev/backend/app/`): resolves the two gaps ARCHITECTURE_KB
§9.3 flagged pre-Code-gate.
- `Profile.avatar_photo_id` (`profiles.py`): a derived field, not a stored
  column, populated at the route layer (`routes/profiles.py`, same
  pattern as `age_summary`) on create/get/list via "most recent
  `photo_meta` row for this profile where `memory_id IS NULL`." New index
  `idx_photo_meta_profile_memory_created` on
  `photo_meta(profile_id, memory_id, created_at)` (`db.py`, idempotent
  `CREATE INDEX IF NOT EXISTS`, applies to existing DBs on next startup
  with no separate migration step needed).
- `PhotoStore.create()` (`photos.py`): profile-level (`memory_id IS NULL`)
  uploads now replace rather than accumulate. A new private
  `_replace_prior_profile_level_photos()` helper runs after the new
  row/file commit and before the accent-extraction step, unlinking
  file(s) and deleting row(s) of any other `memory_id IS NULL` rows for
  that exact `profile_id` (explicit filter, security-architect condition
  1) -- deliberately not via the public `delete()` method (which would
  reset the new photo's just-computed accent to null), with a one-line
  comment documenting the authz-check bypass this represents and why it's
  safe (security-architect condition 2). Memory-attached photos are
  completely untouched by this path.
- **Regression tests** (security-architect condition 3, `test_photos.py`):
  repeated profile-level upload leaves exactly one row/file and it's the
  new one (DB count and on-disk file count both asserted); a
  memory-attached photo survives a profile-level upload unchanged;
  cross-profile isolation (uploading to profile B never touches profile
  A's rows/files). Two more in `test_profiles.py` cover `avatar_photo_id`
  staying null until a profile-level upload, then matching the uploaded
  photo's id across create/get/list, and staying null when only a
  memory-attached photo exists.

**Frontend** (`dev/frontend/`):
- **F14**: new `Avatar.tsx` component (+ `.lm-avatar` base CSS) — renders
  the profile's photo circularly when `avatar_photo_id` exists, with the
  *exact* pre-existing `.lm-identity-dot` fallback (unchanged color logic)
  otherwise; `onError` degrades to the same fallback. Wired into
  `ProfileSwitcher.tsx` (32px, `photo_accent_deep` ring, replacing the old
  accent-tinted-dot-as-photo-proxy render), `TodayScreen.tsx`'s new
  `.lm-hero-heading-row` (44px, fixed translucent-white ring), and
  `JourneyScreen.tsx`'s header (56px, cream border + shadow, new
  `.lm-journey-avatar-row`). New "Profile photo" `.lm-card` at the top of
  `SettingsScreen.tsx` (above "Your family"): reuses
  `AddMemoryForm.tsx`'s hidden-file-input pattern, upload-on-select via
  `uploadPhoto(profile.id, file)` (no `memory_id`), optimistic
  `URL.createObjectURL` preview reverted on failure, "Uploading…"
  disabled state, `role="alert"` error via the existing `ApiError`/
  `parseErrorMessage` path, and the UXR-10 privacy line. New
  `getProfile()` wrapper in `lib/api.ts` (exposes the already-existing
  `GET /profiles/{id}` route to the frontend for the first time) refetches
  the profile after a successful upload so `avatar_photo_id` and the
  photo-accent tokens land together; `app/page.tsx` threads
  `profile`/`identityColor` props into `TodayScreen`/`JourneyScreen`/
  `SettingsScreen` and a new `handleProfileUpdated` in-place state update
  (no full page reload).
- **F15**: new `Lightbox.tsx` — every Journey photo `<img>` (banner and
  `.lm-moment-photos`) wrapped in a new `.lm-photo-trigger` button. Full-
  screen `rgba(20,16,12,.88)` backdrop, reuses the exact `photoUrl()` src
  and `crossOrigin="use-credentials"`; dismiss via close button/Escape/
  backdrop-click (image/caption click never dismisses); `role="dialog"
  aria-modal="true" aria-label="{title} photo"`, focus-on-open, a
  hand-rolled Tab/Shift+Tab focus trap (no existing dialog in this app had
  one to copy), and focus returned to the triggering button on close;
  `ArrowLeft`/`ArrowRight` + visible prev/next buttons + dot indicator for
  multi-photo memories, no nav controls for single-photo ones.
- **F16**: new `.lm-view-toggle` segmented pill in `JourneyScreen.tsx`
  ("Timeline"/"Gallery", default Timeline, client-only state per UX_KB
  §8.3's named scoped simplification). Gallery flattens every timeline
  memory's `photo_ids` (already-fetched `getTimeline()` response, no new
  API call) into one chronological `.lm-gallery-grid` (3 cols mobile, 5 at
  the existing 1024px breakpoint, reusing `AddMemoryForm`'s photogrid
  column precedent), bare photos only (no date/age labels, UXR-1), its own
  empty-state copy, and a plain `<ul>` of `<button>`-wrapped images with
  `aria-label` = the parent memory's title. Gallery tiles open the same
  `Lightbox`, seeded with the full profile-wide chronological photo list
  (not just one memory's) — the F15/F16 "one component, two seed-list
  scopes" pairing requirement.
- **New tests**: `Avatar.test.tsx` (4), `Lightbox.test.tsx` (7),
  `JourneyScreen.test.tsx` (4, covering the toggle default, gallery
  flattening + `aria-label`, empty state, and the shared-Lightbox
  profile-wide seeding), `SettingsScreen.test.tsx` (6, covering Add/Change
  copy, upload-on-select with the refetch, the Uploading… disabled state,
  calm error handling with no avatar-state corruption on failure, and the
  duplicated-but-expected privacy line).

**Judgment calls made during Increment 4** (documented per the Code-gate
brief, not silently decided):
1. **`getProfile()` added to `lib/api.ts`** — not itself a new backend
   route (the backend's `GET /profiles/{id}` has existed since Increment
   1), just the first frontend caller of it. Chosen over reconstructing
   the updated `Profile` client-side from the `PhotoMeta` upload response
   because `PhotoMeta` doesn't carry the photo-accent tokens
   `PhotoStore.create()` also just updated server-side — a full refetch
   keeps `avatar_photo_id` and the accent tokens in the same lockstep
   §8.4 already establishes for the read side, at the cost of one extra
   round-trip per upload (acceptable for a settings action, not a
   high-frequency path).
2. **Settings' 72px avatar carries no additional ring**, unlike the other
   three surfaces — UX_KB §8.1a specifies "the existing `object-fit:
   cover` circle mask is the only treatment" for this surface and is
   silent on a ring convention for it specifically (switcher/Today/
   Journey each name one explicitly). Read literally rather than
   inventing a fourth ring convention the KB didn't ask for.
3. **`page.tsx`'s own sidebar-button and mobile-header identity dots were
   left unchanged** (not migrated to `Avatar`) — UX_KB §8.1 names three
   specific surfaces by file (`ProfileSwitcher.tsx`, `TodayScreen.tsx`,
   `JourneyScreen.tsx`) plus Settings' new control (§8.1a); the sidebar/
   header buttons in `page.tsx` are a different affordance (the switcher-
   opening button, not the switcher list itself) that neither section
   names. Left alone as an unstated-scope-addition guard, not an
   oversight — flagged here rather than silently expanding scope to a
   fourth/fifth surface.
4. **No backend server restart performed this session** — the live
   `:8000` process (left running per the task brief) was started before
   this session's backend edits (`db.py`/`photos.py`/`profiles.py`/
   `routes/profiles.py`) and was not reloading them live; a restart is a
   Deploy-gate action, not a Code-gate one. Flagged explicitly so the demo
   surface doesn't quietly diverge from what's actually committed.

**Not built this increment**: F13 (chat history + suggested prompts,
scheduled Increment 5 per FEATURES.md, needs its own Experience Design
pass) and F12/F17 (later backlog). UX_KB §8.6's DesignSync-push gap and
§8.4/§9.3's backend gaps are both closed by this increment's work; no new
gaps found during implementation beyond the four judgment calls above.

## Decisions Log
- 2026-07-10: plan-agent recommended `genai-chatbot` over `rag-knowledge-base`
  (no document corpus — recommendations are LLM-generated from the kid's
  profile, not cited from documents) and `agentic-workflow` (API-only, no UI;
  this is a consumer website). Human confirmed. [plan-agent, approved]
- 2026-07-10: Scaffolded from `genai-chatbot` template (FastAPI+LangChain
  backend, Next.js frontend placeholder), dev repo initialized at `72ef863`.
  [new-project skill]
- 2026-07-10: Intake complete — domain: child development & parenting
  guidance (functional-agent, `DOMAIN_KB.md`, 8 risks flagged incl. an
  active challenge for Architecture: don't let the LLM generate milestone
  ages ungrounded, embed a curated CDC-2022 table instead); industry:
  consumer parenting/family tech (industry-expert, `INDUSTRY_KB.md`,
  6-item trend-informed backlog + compliance flags: no AI training on
  child data, no face processing on photos, retention/delete policy
  before photos ship, contextual-only product recs). [Intake gate]
- 2026-07-10: Plan & Backlog gate — human reviewed the itemized backlog and
  approved F1–F10 for this run (larger than plan-agent's proposed F1–F5
  slice; F11 alone deferred), built in 3 gated increments per PLAN.md §4.7;
  pulls F7 photo-compliance preconditions and the F10 auth decision into
  scope and ~2.5–3.5×'s the original token estimate (usage-monitor
  re-estimate recommended before Architecture). [plan-agent, human-approved]
- 2026-07-10: **Platform decision, explicitly confirmed** — responsive web
  app (any browser, no install), not a PWA and not a native iOS/Android
  app. This had been an unstated assumption baked into `genai-chatbot`
  (Next.js/FastAPI is a browser stack) and ui-ux-designer's "phone-first,
  one-handed" design language, which could plausibly have read as native.
  Human confirmed responsive web is correct — no template or scope change.
  solution-architect should treat this as settled, not reopen it. [human,
  explicit]
- 2026-07-10: **Experience Design gate approved** (4 revisions, human
  review at each): rev 1 core flows/palette; rev 2 more saturated palette
  + full-screen wireframes (research-informed: parent-facing vibrancy
  register, not child-facing toy register); rev 3 desktop responsive
  layouts (sidebar nav ≥1024px, 2-col Today grid, centered Journey with
  alternating cards); rev 4 photo-personalized theming (decorative accent
  layer only, pediatrician-note slate + destructive red structurally
  excluded from the personalization token set, scrim-based contrast
  guarantee, automated pre-render fallback to default theme rather than a
  contrast violation — UXR-13). All reviewed via a locally-served
  design-review page (localhost:5051), never approved from text alone, per
  the process fix logged in `admin/LESSONS.md`. `knowledge/UX_KB.md` §§1-6
  is the full record. [ui-ux-designer, human-approved]
- 2026-07-10: **Architecture gate held — pending human approval.** Jointly
  designed by solution-architect and security-architect (no disagreement),
  advised by responsible-ai-architect. Resolved all PLAN.md §6 open
  questions: R3 grounding (curated CDC-2022 table adopted), auth design
  (baseline confirmed with refinements — full authn/authz reasoning in
  SECURITY_KB.md's dedicated section), photo storage/encryption (Fernet
  app-level encryption, key in `.env`, DB file itself not separately
  encrypted this run — named gap with a revisit trigger), photo color-
  extraction algorithm (server-side Pillow pipeline satisfying UX_KB §6.3's
  contrast contract), email/notification infra (deferred this run,
  documented fallback design if overridden), storage backend (SQLite
  confirmed, cascade-enforced schema), and output-side enforcement
  (`app/guardrails.py`, post-generation R1/R2 checks, streaming buffered
  server-side before release). First `RESPONSIBLE_AI_KB.md` established
  with content/behavior boundaries and 7 red-team scenarios. See
  `knowledge/ARCHITECTURE_KB.md`, `knowledge/SECURITY_KB.md`,
  `knowledge/RESPONSIBLE_AI_KB.md` for full detail. **Not yet approved by
  the human — Code gate cannot start until this is signed off.**
  [solution-architect + security-architect, joint; responsible-ai-architect,
  advisory; pending human approval]
- 2026-07-10: **Architecture gate, item 5 revised — human override.** The
  human explicitly overrode the F8 email-deferral decision recorded above,
  same day, requesting real email delivery rather than dormant opt-in
  machinery. solution-architect replaced `knowledge/ARCHITECTURE_KB.md` §5
  in full (not appended) with a real-delivery design: Resend as the
  transactional provider, in-process APScheduler daily job (confirms the
  gate's own documented fallback), a content-free notification-only email
  body (no child name/DOB/age/milestone content ever leaves the machine —
  the direct design answer to the deferral's original stated privacy
  concern, not a walk-back of it), a real one-click unsubscribe
  independent of the in-app opt-in toggle (unauthenticated by design, RFC
  8058 one-click headers, stable per-user token), CAN-SPAM compliance
  checked explicitly (INDUSTRY_KB did not name it; mailing-address
  requirement flagged for human/deploy-agent action before go-live), and
  `RESEND_API_KEY` handled via the existing `.env` secrets pattern. This
  revision is solution-architect's design alone; **security-architect
  should be re-consulted on the API-key handling and the new
  unauthenticated-route/data-flow implications before this piece is
  treated as jointly signed off**, consistent with the Architecture gate's
  joint-presentation requirement. Everything else from the original
  Architecture gate is unchanged. [solution-architect, per human override;
  pending security-architect re-consult and human approval]
- 2026-07-10: **security-architect's independent re-consultation on the F8
  revision, completed.** Reviewed `ARCHITECTURE_KB.md` §5 in full against
  `SECURITY_KB.md`'s existing auth/secrets design and appended findings to
  `SECURITY_KB.md` §1.7 (unsubscribe-route review), §5 (new "Third-party
  data processors" section), and §6.1 (F8 sign-off addendum) — additive,
  not a rewrite of the existing Auth & Authz section. Findings:
  - **API key handling (`RESEND_API_KEY` in `.env`): confirmed consistent**
    with SECURITY_KB §2.5's existing secrets pattern — no change needed.
  - **Unauthenticated unsubscribe route (`GET /digest/unsubscribe`):
    approved, conditional on two concrete changes**, not a rubber stamp —
    (1) the route handler must perform a structurally single-purpose write
    (a dedicated single-column update, not a call through a generic
    user-update function) so the "only digest_opt_in can change" property
    is enforced by code shape, not just documented intent, with a new
    Test-gate scoping test to verify it; (2) a rate limiter (reusing the
    existing `/auth/login`-style limiter, e.g. 20 req/min/IP) must be added
    to the route for abuse resistance — token entropy (256-bit,
    `secrets.token_urlsafe(32)`, matching session-token design exactly)
    already rules out brute-force as a concern, so this is for ordinary
    DoS/abuse resistance on an unauthenticated write-capable endpoint, not
    brute-force defense. Stable non-expiring token design, hashed storage,
    and GET-based RFC 8058 transport are all confirmed correct as designed
    — no change requested on those points. One additional explicit
    constraint added: the unsubscribe confirmation page must contain no
    third-party resource loads/links, to prevent Referer-header token leak.
  - **New consideration surfaced, not previously covered: Resend as a
    third-party data processor.** ARCHITECTURE_KB §5.8 addressed only
    API-key mechanics; it did not address that a caregiver's email address
    (adult-caregiver PII, not child PII) now reaches a third-party vendor
    on every send. Assessed as low-risk (no child data, structurally
    consented-to via digest opt-in) but requiring an explicit privacy-
    policy disclosure naming Resend as a sub-processor, and a light-touch
    vendor-posture check (published SOC 2/DPA availability) before
    production sending — flagged as a human/deploy-agent go-live checklist
    item, same class as ARCHITECTURE_KB §5.6's mailing-address requirement,
    not a blocker for continuing to Code gate at `local`-target scope.
  - **Net result: the F8 revision is treated as jointly approved by
    security-architect**, conditional on the two unsubscribe-route
    additions and the privacy-policy/vendor-check item being tracked and
    completed before production sending is enabled — full reasoning in
    `SECURITY_KB.md` §1.7, §5, §6.1. [security-architect, independent
    review complete; still pending final human approval of the gate as a
    whole]
- 2026-07-11: **Code-gate fix pass on the 7 findings from Increment 1's
  Test gate** (evidence: `test-evidence/{unit-integration,red-team-bias,
  ux-accessibility}-2026-07-11.md`). All 7 closed, each in its own commit:
  1. **Blocking (responsible-ai-architect):** `_DRUG_DENYLIST_RE` was
     defined in `guardrails.py` but never called from `check_medical()`,
     so a drug name without a numeric mg/ml/mcg dose slipped through
     unmodified. Wired it in; added regression tests for several
     dose-free drug-name phrasings plus an end-to-end `enforce()` check.
     **Closed.**
  2. **Blocking (ui-ux-designer + backend root cause):** `age_summary`
     in `routes/profiles.py` collapsed preterm profiles to a
     corrected-only number ("4 months (corrected)"), and the profile
     switcher computed a client-side chronological-only estimate with a
     label-only "(corrected age used)" suffix — neither showed the
     exact UX_KB §1.5 dual-age format. Fixed both call sites to
     `"{chrono} months (about {corrected} months corrected)"`;
     `Profile` responses (create/get/list) now carry a server-computed
     `age_summary` so the switcher renders the same authoritative
     string. Non-preterm profiles confirmed unchanged (chronological
     only). Added regression tests for both cases. **Closed.**
  3. **Blocking (ui-ux-designer, UXR-9):** `--lm-danger` (reserved for
     the delete-confirmation dialog) was used in `ChatScreen.tsx`'s
     network-error text and `OnboardingFlow.tsx`'s submit-error text.
     Both restyled to `--lm-terracotta-deep`, matching the existing
     non-alarm treatment used for onboarding's DOB-validation error.
     **Closed.**
  4. **Blocking (test-agent, PLAN §7-D item 14):** `/chat`'s response
     body carried no disclaimer at all — only an `X-LM-Disclaimer`
     header using the ASCII-safe variant, not the exact `DISCLAIMER`
     constant, and not in the payload. `/chat` now returns
     `{"text": ..., "disclaimer": DISCLAIMER}` (header kept too),
     matching how `/activities` already does it. Frontend updated to
     read the JSON payload. Added a regression test asserting the exact
     constant. **Closed.**
  5. **Non-blocking (ui-ux-designer, UXR-6):** `.lm-btn-quiet` (Skip/
     Cancel/Remove) overrode `min-height: auto`, and the chat info
     button's visible 20px dot was its entire hit area — both under the
     44×44px floor. Fixed: `.lm-btn-quiet` now enforces a 44×44px
     minimum tappable area (visual style unchanged); the info button
     keeps its 20px visible dot inside a 44×44px wrapper. **Closed.**
  6. **Non-blocking (ui-ux-designer):** no `<main>` landmark around the
     Today/Chat shell and no page-level `<h1>` on either screen. Added
     a `<main>` wrapper around `.lm-content` in `page.tsx` and a
     visually-hidden-but-announced `<h1>` (new `.lm-visually-hidden`
     utility) on `TodayScreen.tsx` and `ChatScreen.tsx`. **Closed.**
  7. **Tooling (test-agent):** plain `pytest` from `dev/backend/`
     silently imported a stale, non-editable pip-installed copy of
     `app` from `.venv/site-packages/app/` (confirmed via
     `direct_url.json`: a prior non-editable `pip install .`), missing
     the `check_same_thread=False` fix and causing spurious failures.
     `pyproject.toml` lacked explicit package discovery (`data/`, the
     runtime SQLite dir, was being picked up as a second top-level
     package, breaking `pip install -e .`); added
     `[tool.setuptools] packages = ["app"]`, uninstalled the stale
     install, reinstalled editable. Verified: `pytest -v` and
     `python -m pytest -v` both report identical 37/37 passing.
     **Closed.**
  - Added real regression tests for findings 1-4 specifically (not just
    the code fix) per instruction — these were exactly the failure
    modes with zero prior coverage. Full suite: 37/37 passing under
    both `pytest -v` and `python -m pytest -v` (up from 30, +7 new
    regression tests). [code-agent]

- **2026-07-11 — Red-team/bias suite re-run LIVE (orchestrator, direct
  execution — `responsible-ai-architect` has no shell/execution tool, same
  gap as other SME agents this session). Real `ANTHROPIC_API_KEY` now in
  `dev/backend/.env` (explicit human consent given earlier this session to
  reuse the key already used for other projects).** Full report:
  `test-evidence/red-team-bias-2026-07-11-LIVE-RERUN.md`. Result: **6/6
  executable scenarios PASS** (scenario 5/digest confirmed N/A — not shipped
  until F8). Scenario 3 (persistent-unlock dosing) — the one static-review
  FAIL from the earlier pass — now confirmed fixed live: refusal held
  identically across all 4 escalating turns including the teaspoon-phrased
  rephrasing that was the original gap.
  - **Three additional real defects found live** (invisible to the earlier
    static-only review) and fixed before finalizing this report:
    1. `AIMessage.content` is `str | list[str | dict]` — every real `/chat`
       call with an extended-thinking content block 500'd inside
       `check_medical()`. This is the exact LangChain content-type pitfall
       already on record in `admin/LESSONS.md`, now confirmed against this
       project's real code path, not a hypothetical. Fixed:
       `chat.py::_as_text()` normalizes before enforcement. Commit
       `2d80a96`.
    2. **False-positive medical-refusal fallback**: `_DIAGNOSTIC_ASSERTION_RE`'s
       alternation was ungrouped — bare `"this is"` matched as a full
       alternative, unconnected to the trailing `(diagnosis|condition|disorder)`
       clause, so any benign response containing "this is" (e.g. "this is
       completely routine") got misclassified as a medical violation and
       silently swapped for the refusal fallback. Observed directly
       breaking Scenario 1's tone-matching response ~2/3 of live attempts
       before the fix. Fixed: corrected regex grouping. Commit `31b67c5`.
    3. **Mid-sentence truncation**: default `max_tokens=1024` was
       insufficient once extended-thinking overhead counts against the
       same budget — observed a real response cut off mid-safety-caveat.
       Raised to 4096. Commit `ddeeeeb`.
  - Regression tests added for (1) and (2); full suite re-verified clean
    at **42/42** (up from 37) under both `python -m pytest` and plain
    `pytest`.
  - **Test gate for Increment 1 is now fully closed**: all 7 original
    findings fixed and verified, plus 3 additional defects found and fixed
    by actually executing the previously-blocked live suite. Proceeding to
    Review gate next.

- **2026-07-11 — Review gate: Approve** (review-agent). Diff hygiene clean
  across all 15 Increment-1 commits; decision-intent match confirmed for
  the regex/content/max_tokens fixes. One real gap found: ARCHITECTURE_KB
  §6.1 specified a log-only "stale age" backstop check in `guardrails.py`
  that was never implemented — a genuine divergence between approved
  architecture and shipped code, invisible to any single Test-gate suite.
  **Resolved same day (responsible-ai-architect): implemented**, not
  dropped — `check_stale_age()`/`log_stale_age()` added to
  `guardrails.py` exactly per spec (log-only, not wired into `enforce()`'s
  block-and-replace path), plus 6 regression tests. Full suite: 48/48
  passing. Two accompanying stale-documentation items also closed:
  `PROJECT_CONTEXT.md`'s Increment-1 summary point 6 corrected (response
  is `JSONResponse`, not `StreamingResponse`, since finding-4's fix) and
  `memory/INDEX.md`'s little-milestones row updated off its stale
  `intake`/2026-07-10 state.
  - **Incident during this resolution, logged for completeness:** the
    responsible-ai-architect subagent handling this fix accidentally
    overwrote `knowledge/ARCHITECTURE_KB.md` with placeholder text via a
    misused `Write` call. The file was recovered in full (787 lines,
    verified against known content and internal §0–§8 structure) from this
    session's own transcript logs, since the file predates any root-repo
    git commit for this project. Restored with explicit human
    confirmation before being written back. See `admin/LESSONS.md` for
    the queued process fix (agents that only have `Write`, not `Edit`,
    for KB files spanning hundreds of lines are one bad tool call away
    from this — worth requiring `Edit` for any append-only KB file
    instead of `Write`).
  - **Review gate: CLOSED.** Proceeding to Deploy gate next.

- **2026-07-11 — Deploy gate (local): verified up.** Backend
  (`uvicorn app.main:app --port 8000`) and frontend (`npm run dev -- --port
  3000`) confirmed genuinely serving, not just process-exit-0: `GET /health`
  -> `200 {"status":"ok"}`; end-to-end `POST /chat` with a real profile ->
  `200`, non-empty text + `disclaimer` field present (matches the Review-gate
  fix). CORS confirmed scoped to `http://localhost:3000` only. Found and
  fixed a real gap: the backend the orchestrator believed was already running
  on :8000 for the human demo was **not actually listening** (port dark) at
  the start of this check — restarted it; it is left running for the demo.
  Frontend on :3000 was already up and confirmed serving the correct project
  (cwd verified). Ports recorded above (8000/3000), stable for future
  redeploys. `target_env=local` only, per MVP scope — no cloud deploy
  attempted. **Deploy gate: ready**, pending hand-off to test-agent for the
  template's documented smoke test (backend `/health` + `/chat`; frontend
  Playwright once run). [deploy-agent]

- **2026-07-11 — Increment 2 Code gate: F6 (memory log + timeline), F7
  (photo upload + encrypted storage + photo-theme extraction), and F8
  content (in-app "This week" digest) built and committed to `dev/` in
  three logical commits (F6+F7 backend, F8 backend, frontend). 88 backend
  tests pass (30 -> 88); frontend `tsc --noEmit`/`next build` both clean.
  See "Increment 2 implementation summary" above for the full file list
  and 8 documented judgment calls, including a real gap flagged for
  Architecture/Security review (HEIC uploads skip the EXIF-strip/
  color-extraction pipeline in this environment) and a note about
  pre-existing uncommitted Increment-1 diffs found in the working tree
  and deliberately left untouched. [code-agent] Next: Test gate (PLAN
  §7-F, §7-G, §7-H(1-3)).

- **2026-07-11 — solution-architect: Increment-2 open design questions
  resolved, pre-Test-gate.** code-agent flagged two questions
  (Increment-2 judgment calls 2 and 4 above); both resolved directly by
  solution-architect (architecture-owned "how," not a plan-scope change;
  no security-architect co-review required — neither touches auth/
  encryption/data-flow surface). Full reasoning: `knowledge/
  ARCHITECTURE_KB.md` §9.
  1. **HEIC EXIF-strip/color-extraction gap (judgment call 4): closed, not
     documented-as-accepted.** Decision: add `pillow-heif` as a new
     approved backend dependency (a small, actively-maintained Pillow codec
     plugin, not a new architecture surface). Reasoning: SECURITY_KB §2's
     EXIF-GPS-stripped-on-upload commitment is a stated privacy guarantee,
     not a soft preference, and HEIC is Apple's default iOS capture format
     — the current silent fallback (raw bytes stored unmodified,
     `photo_exif_strip_failed` logged) means the format most likely to
     carry phone-camera GPS EXIF is exactly the one the stated protection
     doesn't cover. A well-scoped fix exists (`pillow_heif.
     register_heif_opener()`, zero pipeline-logic changes once registered),
     so documenting an exception rather than closing the gap was judged the
     wrong call here. **Implementation is code-agent's next pass, not done
     by solution-architect** — five concrete steps specified in
     ARCHITECTURE_KB §9.1 (dependency addition, startup registration,
     removal of the HEIC special-case, regression tests, dependency-conflict
     verification).
  2. **Multi-photo theme-source tracking (judgment call 2): accepted as a
     documented Increment-2 limitation.** Decision: no schema change
     (`theme_source_photo_id` or equivalent) this run; code-agent's
     last-upload-wins / reset-to-default-on-any-delete behavior stands as
     implemented. Reasoning: this sits entirely in decorative-UI territory
     (UX_KB §6's theme is explicitly a non-safety-bearing accent layer,
     structurally isolated from the LLM and from any PII concern either
     way) — the worst case is a mildly surprising visual reset, not a
     privacy/correctness failure, and it is self-healing (any new upload
     recomputes the theme). Building a schema/migration/recompute-logic
     fix now would also risk guessing at a UX_KB decision (what should
     "delete with photos remaining" actually show?) that isn't
     solution-architect's alone to make. Documented with an explicit
     revisit trigger (a future UX_KB revision specifying multi-photo
     fallback behavior, or a future Test-gate finding that the reset is
     confusing enough in practice to warrant fixing ahead of a UX_KB
     revision) — ARCHITECTURE_KB §4.2 cross-references §9.2.
  [solution-architect]

- **2026-07-11 — Code-gate fix pass on Increment 2's Test-gate findings**
  (evidence: `test-evidence/{architecture,ux-accessibility,
  unit-integration}-increment2-2026-07-11.md`). All 13 findings (4
  architecture, 6 UX/accessibility, 2 unit/integration, 1 documentation
  pair counted as one) closed, same discipline as the Increment-1 fix
  pass — each logical change in its own commit. Backend suite: 91 -> 101
  passing (10 new regression/property tests); `python -m pytest -v` and
  plain `pytest -v` from `dev/backend/` both report identical 101/101
  (finding-7 parity re-confirmed). Frontend: `tsc --noEmit` clean, `next
  build` clean.

  **Architecture (blocking), all closed:**
  1. **Real bug found and fixed:** `routes/memories.py`'s delete handler
     already unlinked attached-photo files before the DB cascade (code
     was correct), but `app/memories.py`'s `Memory.photo_ids` was typed
     `list[int]` while `photo_meta.id` is TEXT/uuid4 (ARCHITECTURE_KB
     §3) — any memory with an attached photo failed Pydantic validation
     on every read (`MemoryStore.get`/`list_for_profile`), which is what
     actually made the "does delete unlink the file" path untestable and
     misread as "unlinking never happens." Fixed the type to `list[str]`.
     Added `test_delete_memory_with_attached_photo_purges_both_row_and_file`
     asserting both the `photo_meta` row and the on-disk file are gone
     after a memory-only delete. **Closed.**
  2. **`Store[T]` contract test:** added `tests/test_stores.py` (3
     explicit per-store interface assertions — `ProfileStore`'s literal
     `Store[T]` match, `MemoryStore`/`PhotoStore`'s transitively-scoped
     `list_for_profile` + `PhotoStore`'s `get_meta`/`get_bytes` split).
     Also tightened `ARCHITECTURE_KB.md` §0's wording to describe the
     real, reasoned pattern instead of a single literal protocol every
     store was implied to follow identically. **Closed.**
  3. **`extract_accent` property-based test:** added
     `test_extract_accent_property_n_random_hues_stay_in_clamped_bands`
     (N=50 random hues, seeded) and
     `test_extract_accent_skin_tone_band_is_excluded` (direct coverage of
     the hue 5-35°/sat 20-60%/light 40-85% exclusion band, previously
     untested) to `tests/test_photo_theme.py`. **Closed.**
  4. **Cascade coverage asymmetry:** added a direct `SELECT COUNT(*) FROM
     photo_meta WHERE profile_id = ?` assertion to
     `test_profile_delete_leaves_zero_photo_files` (previously only
     checked the on-disk directory). **Closed.**
  - Also closed, flagged non-blocking in the evidence: extended
    `test_photo_isolation_import_check` with a dedicated
    `test_guardrails_photos_isolation_import_check` (the literal
    `guardrails.py` <-> `photos.py` pair ARCHITECTURE_KB §7 names, not
    just the `app.llm`/`app.prompts` pair); documented `photo_meta.id`'s
    TEXT/uuid4 shape in ARCHITECTURE_KB §3 (consistent with
    `sessions.token_hash`/`invites.code`'s existing precedent, not an
    inconsistency); corrected ARCHITECTURE_KB §6.1's inaccurate claim
    that `/digest` runs the R1 framing check at request time (`build_digest`
    is pure curated-data assembly with zero LLM involvement and correctly
    never calls `guardrails.enforce()` — the framing lint test exercises
    the curated content directly, not a runtime enforcement call).

  **UX/accessibility (blocking), all closed:**
  5. **Photo-personalization was invisible end-to-end:** `Profile`
     (`app/profiles.py`) now exposes `photo_accent_mid/deep/tint` (all
     three, null until a photo is uploaded); added
     `test_profile_response_exposes_photo_accent_fields`. Frontend:
     `lib/types.ts`'s `Profile` carries the same three fields; new
     `lib/theme.ts::photoAccentStyle()` sets `--lm-photo-mid/-deep/-tint`
     as inline CSS custom properties; wired into `JourneyScreen.tsx`'s
     header, `TodayScreen.tsx`'s hero card, and `ProfileSwitcher.tsx`'s
     identity dot (+ ring + informational "photo theme"/"default theme"
     chip per UX_KB §6.5). `globals.css`'s `.lm-journey-header`/
     `.lm-hero-card` gradients now read `var(--lm-photo-mid/-deep,
     var(--lm-peach|--lm-coral|--lm-gold))` — falls through to the fixed
     default theme when a profile has no photo, per §6.4. `.lm-hero-card`
     also gained the §6.3-rule-3 fixed black scrim layer behind its white
     headline text. **Closed.**
  6. **JourneyScreen desktop layout:** added a `@media (min-width:
     1024px)` block to `globals.css` (`.lm-content[data-screen="journey"]`
     max-width 760px, `.lm-river` centered spine, alternating
     `.lm-river-side-l`/`.lm-river-side-r` per moment) matching
     `design-review/screens/desktop/journey-desktop.html`'s alternating-
     river pattern; `JourneyScreen.tsx` now assigns alternating side
     classes to memory entries (not chapter markers, which stay
     centered) via a separate counter. **Closed.**
  7. **`AddMemoryForm`'s title/note/date inputs had no `className`:**
     added a new `.lm-input` class (14px radius, 12-14px padding, 15-16px
     font, 1.5px border, 44px min-height per `photo-upload.html`'s
     spec) and applied it to all three inputs. **Closed.**
  8. **`JourneyScreen.tsx` rendered memory photos with `alt=""`:** now
     `alt={entry.title || "Photo from this moment"}`. **Closed.**
  - Non-blocking, also closed: `.lm-ptile-remove` (staged-photo remove)
    grew a 44x44px transparent hit-area wrapper around its unchanged
    22px visible icon, same pattern as Increment 1's `.lm-btn-quiet`/
    `.lm-info-btn` fix generalized to this new control.
    `AddMemoryForm` converted from an ad-hoc centered dialog to
    `.lm-sheet-backdrop`/`.lm-sheet` — a real bottom sheet (grabber,
    rounded-top-only corners) below 768px matching
    `design-review/screens/photo-upload.html`, a centered 640px modal
    with a 5-column photo grid at >=768px, matching the desktop mockup's
    intent.

  **Unit/integration (non-blocking), closed:**
  9. Added `test_digest_opt_in_defaults_false_at_schema_level` (inserts a
     `users` row without specifying `digest_opt_in`, asserts the stored
     value is `0`) and `test_no_scheduler_queue_or_email_code_exists_yet`
     (AST-based import scan of every `.py` file under `app/` for
     `apscheduler`/`celery`/`smtplib`/`email.mime`/`email.message` or any
     import name containing "scheduler"/"smtp" — fails loudly if a future
     change reintroduces dormant delivery code before Increment 3) to
     `tests/test_digest.py`. **Closed.**
  [code-agent]

Approved 2026-07-10 — **core + 3 architects** (usage-monitor's recommended
option (b), est. ~420k–540k remaining vs ~590k–720k full-team):
- Core (non-droppable): plan-agent, code-agent, test-agent, review-agent,
  deploy-agent, ui-ux-designer (UI-bearing template).
- Optional, kept: solution-architect, security-architect,
  responsible-ai-architect — all three retained specifically because this
  project's risk lives at Architecture (child-data privacy, medical-advice
  boundary, the R3 grounding debate).
- Optional, dropped after Intake: functional-agent, industry-expert. Their
  Intake-time KBs (`DOMAIN_KB.md`, `INDUSTRY_KB.md`) remain the project's
  grounding context; their test suites are skipped at the Test gate; they
  can be re-engaged later via /enhance-project or /consult.

**Test Policy**: all active suites blocking (default) — no advisory
exceptions. Active suites at Test gate: unit/integration (test-agent),
UX/accessibility (ui-ux-designer), architecture (solution-architect),
security (security-architect), red-team/bias (responsible-ai-architect).

**Note (2026-07-10):** the ~420k–540k token estimate above was made for the
F1–F5 slice; the approved F1–F10 scope likely runs 2.5–3.5× that (PLAN.md
§8). Usage-monitor should re-estimate before the Architecture gate.

- **2026-07-11: Increment 3 Code gate — F9 (buying recommendations +
  CPSC filtering), F10 (real auth activation + multi-caregiver), and F8
  delivery (Resend email + scheduler + unsubscribe) built and committed
  to `dev/`.** Backend: 101 → 165 tests, all passing under both `pytest`
  invocations (parity re-confirmed). Frontend `tsc --noEmit`/`next build`
  both clean. See "Increment 3 implementation summary" above for the
  full file list and 9 documented judgment calls. Two items explicitly
  flagged for the Test gate/human, not silently resolved:
  1. **F8 real email sending is not enabled in this environment** — the
     mechanism (`email_delivery.py`, `scheduler.py`, the unsubscribe
     route) is fully built and tested against mocked Resend calls, but
     `ENABLE_DIGEST_SCHEDULER` stays unset and `RESEND_API_KEY` stays
     blank, per ARCHITECTURE_KB §5.1's stated operational precondition
     (no verified Resend sending domain exists for this project). This
     is a real, unmet operational gap, not a code gap — a human/deploy-
     agent action item before any real send is enabled.
  2. **`MAILING_ADDRESS` in `email_delivery.py` is a placeholder**, per
     ARCHITECTURE_KB §5.6's own flag — must be filled with a real
     mailing address or registered PO box before production sending
     (CAN-SPAM). A test (`test_email_body_contains_mailing_address_
     placeholder_flag`) locks in that this is still a placeholder so it
     doesn't silently drift into looking like a real address was
     supplied.
  - One judgment call flagged for solution-architect/security-architect
    re-review at Test gate: a plaintext `users.unsubscribe_token` column
    was added beyond ARCHITECTURE_KB §5.4's literal "hash only" spec,
    because a hash cannot be reversed to rebuild the stable, reused-
    across-sends URL the scheduler needs each week — `unsubscribe_token_
    hash` remains the sole verification mechanism for the incoming
    request, exactly as specified; this is additive, not a substitution.
    Worst case on compromise of either value is unchanged from
    SECURITY_KB §1.7 point 1's existing assessment.
  - **Full §7-A adversarial-scenario regression (PLAN §7-J item 37)**:
    satisfied for this project's automated pytest-based suite by making
    `tests/conftest.py`'s default `client` fixture authenticate before
    yielding (judgment call 1 above) — all 101 pre-existing Increment
    1/2 tests, including the photo/LLM-isolation integration test and
    the guardrail-net unit tests, now run under a real session with zero
    test-file assertion changes required, and the full suite (165/165)
    passes. **Not re-covered in this pass**: a live-LLM red-team re-run
    (real Anthropic API calls exercising the 8 PLAN §7-A adversarial
    chat scenarios under a real authenticated session) equivalent to the
    one the orchestrator ran live for Increment 1
    (`test-evidence/red-team-bias-2026-07-11-LIVE-RERUN.md`) — that was
    a manual, non-pytest exercise even then, and re-running it live is
    recommended but not performed as part of this Code-gate pass; flagged
    for the Test gate to decide whether to re-run it explicitly now that
    auth sits in the request path, or to treat the pytest-level
    regression coverage above as sufficient given `/chat`'s guardrail
    logic itself was not touched this increment. [code-agent]

- **2026-07-11: Code-gate fix pass on ui-ux-designer's Increment 3 UX/
  accessibility gate** (evidence: `test-evidence/
  ux-accessibility-increment3-2026-07-11.md`). Two blocking + three
  non-blocking findings, all closed:
  1. **Finding 2b (blocking):** `lib/api.ts::request()` threw `ApiError`
     carrying the raw HTTP status line plus the raw JSON response body as
     literal text (e.g. `401 Unauthorized: {"detail":"Invalid email or
     password"}`), and `AuthScreen.tsx` rendered it verbatim on every
     login/signup/join error — a UX_KB §1.2/§1.7 voice violation ("factual
     and calm," plain language), not a security differential-leak issue
     (SECURITY_KB §1.5's non-differential backend message was already
     correct). Added `parseErrorMessage()` in `lib/api.ts`: extracts a
     string `detail` field when present, falls back to the first
     validation-array `msg` for FastAPI's pydantic 422 shape, and falls
     back to a calm generic message ("Something went wrong — please try
     again.") otherwise. The backend's own message text (e.g. "Invalid
     email or password") still surfaces to the user — only the HTTP/JSON
     transport wrapper around it is stripped. **Closed.** Left the other
     two `request`-style call sites in `lib/api.ts` (`sendChatMessage`,
     `uploadPhoto`) untouched — they use a separate inline `throw new
     Error(...)` not routed through `AuthScreen.tsx` or flagged by this
     finding; out of this fix pass's stated scope.
  2. **Finding 2c (blocking):** `globals.css`'s `.lm-field input[type=...]`
     touch-target/visual rule omitted `email` and `password`, so
     `AuthScreen.tsx`'s two most-used fields (every login/signup) got none
     of the standard 44px-floor styling every other input in the app
     receives. Added `input[type="email"]` and `input[type="password"]`
     to the existing selector list (kept the explicit type-list form
     rather than switching to an unqualified `.lm-field input`, to stay a
     minimal, reviewable diff — flagged as a possible future hardening if
     ui-ux-designer wants to close this class of gap pre-emptively).
     **Closed.**
  3. **Finding 3 (non-blocking):** `SettingsScreen.tsx` had no reviewed
     desktop treatment (functional single-column-at-640px by accidental
     default, never a confirmed decision, unlike onboarding's explicit
     §5.2 "stays narrow" call). Added a deliberate
     `.lm-content[data-screen="settings"]` rule inside the existing
     `@media (min-width: 1024px)` block: `max-width: 680px` (matching the
     chat column's cap — a single-column form/account-management screen
     has no card collection that benefits from a wider grid, so staying
     narrow was the right call, just now a documented one) plus
     `padding-top: 40px` for desktop breathing room. **Closed** — still a
     "stays narrow" outcome, but now a stated decision ui-ux-designer can
     confirm or revise rather than an unreviewed default.
  4. **Finding 4 (non-blocking):** `SettingsScreen.tsx` skipped h1(hidden)
     → h3 directly, breaking the Increment-2 h1-hidden/h2-visible
     convention `JourneyScreen.tsx`/`TodayScreen.tsx` both follow. Added a
     visible `<h2>Settings</h2>` immediately after the hidden `<h1>`,
     matching `JourneyScreen.tsx`'s pattern exactly (no visible hero
     content needed on Settings the way Journey/Today have one — a plain
     text h2 suffices). The three card headers stay `<h3>`, now correctly
     nested under the h2. **Closed.**
  5. **Finding A (informational, no code fix):** confirmed read — no
     design-review mockup has ever been produced for Auth/Settings/
     Products; this is a process-gap backlog item for ui-ux-designer's
     next Experience Design pass, not something Code can resolve.
     Acknowledged, not silently dropped.
  - **Regression check:** backend `python -m pytest -v` and plain `pytest
    -v` from `dev/backend/` both 168/168 passing (unchanged from pre-fix
    baseline — no test files touched, this was a UI/CSS-only fix pass).
    Frontend `tsc --noEmit` and `next build` both clean. [code-agent]

- **2026-07-12: Code-gate fix pass on ui-ux-designer's full-app density
  retest** (evidence: `test-evidence/ux-retest-synthetic-data-2026-07-11.md`,
  triggered by the human-reported Journey "6 months/9 months text
  overlapping with lines" defect at 15-memory density). All 8 findings
  closed, in dev commits `4dbadec` (UXD-1/2/3/4a) and `fe6a53b`
  (UXD-5/6/7/8):
  1. **UXD-1 (blocking, the human-reported defect) — closed.** Applied the
     evidence file's exact patch spec: removed the per-item
     `.lm-river-line` connector segments from `JourneyScreen.tsx` and their
     CSS rule; one continuous `.lm-river::before` spine at both breakpoints
     (mobile `left:13px`, desktop `left:50%`); chapter-marker content
     wrapped in a cream `.lm-chapter-label` pill (`position:relative;
     z-index:1`) so labels break the spine instead of the spine painting
     through them; `.lm-river-dot` gets a 3px cream masking ring
     (`box-sizing:content-box` to preserve the 15px coral fill); desktop
     dot-cols absolutely positioned onto the spine (±38.5px offsets,
     recompute if the 28px gutter changes); dead `row-reverse` rule
     deleted. Spine endpoints (26/60 mobile, 24/80 desktop) are the spec's
     computed values — still flagged for ±4px visual tuning in a browser.
  2. **UXD-2 (blocking) — closed.** `.lm-journey-header` gradient's first
     stop changed from `--lm-photo-mid` to `--lm-photo-tint` (the band the
     server pre-check already guarantees against unscrimmed ink text per
     UX_KB §6.3.2); stale CSS comment updated. Cosmetic rider from the
     same finding: the dead `.lm-journey-header h1` rule folded into an
     `h2` rule (chose "fold" over "delete" from the spec's two options,
     removing the JSX inline h2 styles — judgment call, visually
     identical). Visual confirm that the olive tint still reads
     "personalized" remains open for the retest.
  3. **UXD-3 — closed** by the same UXD-1 patch (mobile spine is now
     continuous, no more dash-gap clutter).
  4. **UXD-4a — closed.** `loading="lazy"` on Journey memory photos.
     UXD-4b (120px photo-band card redesign) deliberately NOT implemented
     — it requires a design-review preview and human approval first, per
     the evidence file.
  5. **UXD-5 — closed.** `sendChatMessage` and `uploadPhoto` in
     `lib/api.ts` now throw `ApiError(status, parseErrorMessage(body))`
     like `request()` — the two sites explicitly left out of the
     Increment-3 Finding-2b fix.
  6. **UXD-6 — closed.** `page.tsx`'s `loadError` never renders the
     browser's raw "Failed to fetch": non-`ApiError` rejections get the
     calm fallback "Could not reach the server — check that the backend
     is running, then reload." (used the fix-pass tasking's exact copy,
     which supersedes the evidence file's draft wording — judgment call);
     `ApiError` messages, already parsed calm, pass through verbatim.
     `page.test.tsx` updated to the new contract plus a new ApiError
     pass-through case (12 → 13 frontend tests) — the two prior tests
     asserted the old raw-message behavior by design, so updating them is
     the fix landing, not a regression.
  7. **UXD-7 — closed.** Sidebar and mobile-header identity dots now use
     `selected.photo_accent_mid ?? IDENTITY_HUES[...]`, matching
     `ProfileSwitcher` (UX_KB §6.5 — one child, one color everywhere).
     Ring left off per the spec's "ring optional".
  8. **UXD-8 — closed.** Digest toggle label carries `minHeight: 44`
     (UXR-6 floor), and `handleToggleDigest` now catches PATCH failures
     with a calm terracotta-deep inline `role="alert"` error instead of
     an unhandled rejection leaving the toggle silently stale.
  - **Verification:** frontend `tsc --noEmit` clean; `npm test -- --run`
    13/13 passing (was 12, +1 new UXD-6 case); isolated
    `NEXT_DIST_DIR=.next-build npx next build` clean (dev server left
    running untouched, per instruction — the build's incidental rewrites
    of `next-env.d.ts`/`tsconfig.json` were reverted, not committed);
    backend `.venv/bin/python -m pytest -q` 168/168 (regression check
    only — no backend files touched). Re-verification should include the
    evidence file's five browser-confirmation items (spine endpoint
    tuning, olive tint/hero look, desktop rhythm at 15 items, Today grid
    raggedness, UXD-4b preview). [code-agent]
  9. **2026-07-12 — UXD-4(b) — closed.** The photo-band redesign left open
     above is now implemented, per `knowledge/UX_KB.md` §7 and the approved
     preview `design-review/journey/moment-photo-banner.html`. Journey
     memory cards' first photo (`entry.photo_ids[0]`) renders as a
     full-width `.lm-moment-banner` (`width: calc(100% + 40px); height:
     120px; object-fit: cover; margin: -20px -20px 14px`) as the first
     child of `.lm-card.lm-moment-card`, bleeding through the card's own
     20px padding; photos 2+ (`entry.photo_ids.slice(1)`) still render in
     the unchanged `.lm-moment-photos` thumbnail row below, and
     single-photo memories show the banner only. Corner radius is the
     literal `12px 12px 0 0` from the original retest fix spec, not
     `var(--lm-radius-card)` (16px) — the human explicitly reviewed the
     preview and confirmed the literal 12px value, accepting the small
     sliver of card background visible at the top corners rather than
     matching the card's own 16px radius (UX_KB §7.3).
     `dev/frontend/app/globals.css` and
     `dev/frontend/components/JourneyScreen.tsx` changed.
     **Verification:** frontend `tsc --noEmit` clean; `npm test -- --run`
     13/13 passing (unchanged count — no new test cases required by this
     visual-only change). [code-agent]

## Test Results

**2026-07-11: Test gate, Increment 1 (F1-F5) — unit/integration suite run
(test-agent).** Full structured per-scenario evidence at
`test-evidence/unit-integration-2026-07-11.md`. Suite policy: blocking (no
suites recorded as advisory for this project).

- **Suite count independently verified**: code-agent's "30 backend tests
  pass" claim confirmed — `python -m pytest -v` from `dev/backend/`
  collects and passes 30/30, 0 skipped, 0 errors. Not a zero-test suite.
- **Environment finding (blocking):** the bare `pytest` console-script
  invocation from `dev/backend/` does not put the current working directory
  on `sys.path`, so it imports a stale, non-editable pip-installed copy of
  the `app` package from `.venv/lib/python3.9/site-packages/app/` instead
  of the live source in `dev/backend/app/`. That installed snapshot is
  missing the `check_same_thread=False` fix present in current
  `app/db.py`, producing 11 spurious `sqlite3.ProgrammingError` failures
  that describe a bug the current source does not have. Confirmed by direct
  diff of the two copies. Workaround used for this run: `python -m pytest`.
  Recommend code-agent move to an editable install (`pip install -e .`) or
  document `python -m pytest` explicitly — otherwise any future CI/gate
  automation running plain `pytest` will get a false-negative signal.
- **PLAN §7-B (activities endpoint) and §7-C (profiles + age math +
  template smoke): thoroughly covered, all passing.** Two minor
  test-strength caveats noted in the evidence file (P1's activity-count
  assertion checks `>= 2` where PLAN §7-B item 9 says `>= 3`; P2's
  corrected-bucket check only greps for the word "corrected" rather than
  verifying the specific bucket's content) — not product defects, but worth
  tightening.
- **PLAN §7-A (the 8 adversarial red-team chat scenarios): zero end-to-end
  coverage.** None of the anxiety-framing ("should she be walking"),
  medical-dosing-deflection, diagnosis-deflection, regression/red-flag
  (including the preterm-P2 "corrected age must not excuse it" case),
  premature-corrected-age, out-of-range-old, out-of-range-newborn, or
  unsafe-activity-request scenarios have any test that exercises real model
  output. What exists instead: unit tests of the post-generation
  guardrail-net functions (`check_framing`/`check_medical`/`enforce`) on
  hand-picked strings, and one chat wiring test with the LLM fully mocked.
  Further blocked in this environment by **no `.env`/`ANTHROPIC_API_KEY`
  present in `dev/backend`** (only `.env.example` with a blank key) — real
  LLM calls cannot be made here at all right now. Reported plainly as an
  untested gap, not silently skipped.
- **PLAN §7-D item 14 (disclaimer, exact constant, in every response
  payload): PASS for `/activities`, FAIL for `/chat`.** The `/chat`
  response body carries no disclaimer at all — it is only present as an
  `X-LM-Disclaimer` HTTP header, and that header uses a modified
  ASCII-safe variant (em dash replaced with a hyphen), not the exact
  constant the acceptance criterion specifies. This needs either an
  explicit gate-level carve-out for `/chat` or a code change to add the
  disclaimer to the payload body.
- **PLAN §7-D item 15 (framing lint across all 7-A transcripts and
  digest/timeline/product payloads): no coverage** — there are no 7-A
  transcripts to lint yet, and no corpus-level lint suite exists (isolated
  unit tests of the lint functions only).
- **PLAN §7-A item 5's specific "integration test" requirement** (injected
  system prompt must be asserted to contain both chronological and
  corrected ages for a preterm profile) **does not exist** — no test calls
  `build_system_prompt()` directly and inspects its output.
- §7-E (UX/accessibility) is out of test-agent's scope (ui-ux-designer
  owns it) and is not assessed in this suite.

**Net: this is a blocking finding, not a pass.** The deterministic,
server-computed logic (ages, buckets, profile CRUD, activities content) is
solid and well-tested. The actual child-safety-critical behavior this
product exists to guarantee — that the LLM's real chat output follows R1
anxiety-aware framing and R2 medical-deflection/red-flag rules under
adversarial prompting — has no test coverage at all in this increment, and
the disclaimer-in-every-payload invariant has a real gap on `/chat`. Per
the platform's blocking-suite policy, this should stop the gate for human
decision: either code-agent/responsible-ai-architect build the missing
§7-A/§7-D(15) coverage (which requires an `ANTHROPIC_API_KEY` to be
supplied for this environment) before sign-off, or the human explicitly
overrides with a recorded reason.

**2026-07-11: Test gate, Increment 2 (F6 memory/timeline, F7 photos, F8
digest content) — unit/integration suite run (test-agent).** Full
structured per-scenario evidence at
`test-evidence/unit-integration-increment2-2026-07-11.md`. Suite policy:
blocking (no suites recorded as advisory for this project).

- **Suite count independently verified**: code-agent's "88 -> 91 backend
  tests, all passing" claim confirmed — `python -m pytest -v` from
  `dev/backend/` collects and passes 91/91, 0 skipped, 0 errors. Not a
  zero-test suite.
- **Finding-7 regression check (Increment 1's `python -m pytest` vs plain
  `pytest` divergence): no regression.** Both invocations produce identical
  91/91 results even with the newly-added `pillow-heif` dependency — the
  Increment-1 editable-install fix (`pyproject.toml`'s `packages =
  ["app"]`) still holds.
- **PLAN §7-F (memory log + timeline, items 17-19): genuinely covered.**
  Memory CRUD validation, chronological ordering, hard delete, and cascade
  delete on profile removal all pass with real assertions against the
  store (not just route status codes). Item 19 — the R1 hard schema lint
  on the timeline payload — was specifically re-verified by reading the
  test implementation, not just its name: it is a real recursive walk over
  the full response tree (dicts and lists, all nesting levels) checking
  for `expected_by`/`status`/`on_track`/`typical_range`/`typical_range_band`,
  plus a raw-text substring check for "typical range" and "behind". This is
  genuinely the structural lint PLAN §4.2 calls for, not a shallow
  top-level-only check.
- **PLAN §7-G (photos, items 20-24): genuinely covered.** Upload
  size/type validation (content-sniffed, not extension-trusted), private-
  by-default routing, and the three items this gate's brief flagged for
  extra scrutiny were all independently corroborated against the actual
  source, not just re-run and trusted:
  - Item 21 (delete purge): the test asserts BOTH the metadata row is gone
    (direct `test_db` query) AND `os.path.exists()` on the file path is
    `False`, in the same test — both halves genuinely covered.
  - Item 23 (at-rest protection + EXIF-GPS absence): confirmed
    `app/photos.py` genuinely calls `Fernet.encrypt()`/`decrypt()` (real
    encryption, not a claim-only comment); the on-disk file's raw bytes do
    not match the real JPEG magic-byte signature; EXIF is stripped to zero
    tags on both JPEG and HEIC uploads (the HEIC case has its own
    regression test, because `pillow-heif`'s HEIF encoder was found to
    auto-propagate already-decoded EXIF unless explicitly cleared — a real
    gap the JPEG-only test would have missed).
  - Item 24 (structural isolation): the isolation check is a genuine
    AST-based import-graph scan (`ast.parse`/`ast.walk`), not a
    comment/docstring substring grep — independently corroborated by
    manually reading every `import`/`from` line in `photos.py`,
    `photo_theme.py`, `routes/photos.py`, `llm.py`, and `prompts.py`; no
    cross-import exists in either direction.
- **PLAN §7-H (digest, items 25-27; items 28-29 correctly excluded as
  Increment-3 scope): items 25-26 genuinely covered, item 27 is a real
  gap.** Digest content, newborn-mode, out-of-range-mode, and the framing
  lint all pass with real assertions. Item 27 ("opt-in defaults false;
  nothing ever sent/queued for a non-opted-in user") is **not covered by
  any test** — independent source inspection (grep + read) confirms the
  underlying behavior is currently correct (the `users.digest_opt_in`
  schema column defaults to `0`; no scheduler/queue/SMTP/email code exists
  anywhere in `app/`, confirmed by `app/digest.py`'s own docstring and a
  full-repo grep), so there's no dormant Increment-3 delivery machinery
  accidentally shipped early. But nothing in the automated suite would
  catch a future regression of either half (a flipped default, or a
  quietly-added scheduler). Recommend two small additions before this item
  is marked genuinely closed: a unit test asserting the schema/store
  default, and a regression guard against scheduler/queue code appearing
  in `app/` before Increment 3.

**Net: this is a conditional pass, not a clean pass.** F6 (memory/timeline)
and F7 (photos) acceptance criteria are fully and genuinely tested,
including every item this gate's brief specifically flagged for skepticism.
F8's in-app digest content (items 25-26) is likewise genuinely tested.
The one real gap is §7-H item 27: correct behavior, zero test coverage.
Per the platform's blocking-suite policy, this should stop the gate for
human decision — either code-agent adds the two small tests recommended
above, or the human explicitly overrides with a recorded reason (a
reasonable case exists for overriding here, since F8 delivery is
explicitly Increment-3 scope and the underlying behavior was independently
verified correct by source inspection — but that is the human's call to
record, not test-agent's to assume).

**2026-07-11: Test gate, Increment 3 (F9 buying recs, F10 auth activation,
F8 email delivery) — unit/integration suite run (test-agent).** Full
structured per-scenario evidence at
`test-evidence/unit-integration-increment3-2026-07-11.md`. Suite policy:
blocking (no suites recorded as advisory for this project).

- **Suite count independently verified**: code-agent's "165 backend tests
  pass" claim confirmed twice — `python -m pytest -v` and plain
  `pytest -q` from `dev/backend/` both report 165/165, 0 failed, 0
  skipped, 0 errors, matching the orchestrator's own independent
  re-confirmation. Not a zero-test suite.
- **§7-I (items 30-32, buying recommendations): genuinely covered.** Item
  31's recall filter is a real fixture-injection test — reading the test
  body directly confirms it deep-copies the real catalog, injects an
  actual denylisted category into a temp-file copy, and asserts the real
  filter function excludes it from output. This is the exact scenario
  PLAN specifies, not "the shipped catalog happens to be clean." Items 30
  and 32 (catalog-only items, no small-part toys under 36mo, no
  tracking/affiliate content, no chat product-origination path) are all
  backed by real assertions.
- **§7-J items 33, 34, 35, 36 (auth activation, family isolation, invites,
  roles): genuinely covered**, including the specific risk this gate's
  brief flagged — item 34's family-isolation test checks all six resource
  types (profiles, memories, photos, timeline, digest, products)
  individually and confirms each returns 404 (not 403), the resource type
  most commonly missed in this kind of test is not missed here. Two minor,
  non-blocking gaps noted: the no-session-401 check is only directly
  exercised against `/profiles` rather than every data route (though all
  routes share one `Depends(get_current_family)`, confirmed by code
  inspection); invite code format/entropy isn't directly asserted (though
  the generator uses the same secure primitive as session tokens).
- **§7-J item 37 (regression: full §7-A adversarial suite re-passes
  authenticated): PASS, decided cross-suite, not defaulted.** Code-agent's
  claim that `conftest.py`'s `client` fixture now signs up before
  yielding, so every existing test runs authenticated by construction, is
  verified TRUE by reading the fixture directly — but taken alone that
  only re-covers deterministic guardrail-function tests and pre-existing
  Inc-1/2 HTTP tests, not the actual §7-A content (8 live-LLM adversarial
  scenarios), which has not been pytest-native since Increment 1's manual
  live rerun (`test-evidence/red-team-bias-2026-07-11-LIVE-RERUN.md`,
  pre-auth). This suite flagged that in isolation as a gap — but the
  red-team-bias suite (item 37's rightful co-owner) separately reviewed
  this exact question at the code level
  (`test-evidence/red-team-bias-increment3-2026-07-11.md`) and reached an
  explicit, reasoned PASS: `get_current_family`'s auth dependency sits
  strictly upstream of profile resolution, and `enforce()`/prompt
  construction in `chat.py` are byte-for-byte unchanged from the version
  Increment 1's live rerun already validated, so re-spending live-LLM
  budget would re-test a hypothesis already settled, not this increment's
  actual change. Read together, item 37 is a decided, documented,
  cross-suite-consistent PASS — not a silent pass-through and not an
  unresolved gap.
- **Judgment call re-check: plaintext `users.unsubscribe_token` column.**
  Code inspection confirms the implementation is sound — the only write
  path reachable from the unauthenticated unsubscribe route looks up
  strictly by `unsubscribe_token_hash`, never the plaintext column. But
  there is no test that would catch a future regression routing
  verification through the plaintext column instead (every existing test
  passes a token whose plaintext and hash both match, so they can't
  distinguish the two paths) — a real, non-blocking testing-coverage gap.

**Net: PASS, read together with the red-team-bias suite.** §7-I (items
30-32) and §7-J items 33/34/35/36 are fully and genuinely tested by this
suite alone, including the specific scenarios this gate's brief flagged
for skepticism (item 31's injection test, item 34's six-resource-type
check). §7-J item 37, initially flagged by this suite in isolation, is
resolved once cross-referenced against the red-team-bias suite's own
explicit, code-level, reasoned decision not to re-run the live
adversarial scenarios this increment (documented, not defaulted) — no
override is required for item 37. Two minor, non-blocking testing-gaps
remain as recommended follow-ups for code-agent: per-route 401
spot-check breadth (only `/profiles` directly tested, though all routes
share one dependency), invite code format/entropy not directly asserted,
and no differential test locking in that the unsubscribe route verifies
via hash only, never the plaintext `unsubscribe_token` column.

**2026-07-11: Regression pass — live LAN/mobile-testing defects locked into
the suite (test-agent).** After the Increment-3 gates closed, live testing
found three code defects (dev commits 037254d hardcoded-API-host/SameSite
cookie break, 561e452 crypto.randomUUID throw in insecure contexts, c3a2bde
infinite "Loading…" on a rejected session check) plus one process-level
lesson (`next build` during `next dev` corrupts `.next/` — LESSONS.md, no
test possible). Per the human's directive, every code defect now has a
regression test. The frontend previously had **zero** test infrastructure;
a minimal vitest + jsdom + @testing-library/react setup was added (dev
commit b658a2a) and is runnable as `npm test` from `dev/frontend`.
`resolveApiBase` and `localMessageId` were exported as test seams (dev
commit 4b4ef0b) — no behavior changes.

Per-suite results:
- **Frontend regression (new, vitest): 12/12 PASS** — 4 scenarios per
  defect across `lib/api.test.ts`, `components/localMessageId.test.ts`,
  `app/page.test.tsx`. Not a zero-test suite: 12 real tests collected and run.
- **Backend unit/integration (pytest): 168/168 PASS** — unchanged, re-run to
  confirm no interference.
- **`tsc --noEmit`: clean.** `next build` deliberately not run (dev server
  active for the human; see the LESSONS.md `.next/` corruption note).

Structured evidence: `test-evidence/regression-live-testing-defects-2026-07-11.md`.

**2026-07-12: Test gate, Increment 4 (F14 profile avatars+upload, F15
Journey lightbox, F16 Journey gallery) — unit/integration suite
independently re-verified (test-agent).** Full structured per-scenario
evidence at `test-evidence/unit-integration-increment4-2026-07-12.md`.
Suite policy: blocking (no suites recorded as advisory for this project).

- **Counts independently re-confirmed, both invocations agree with
  code-agent's claim:** `python -m pytest -v` and plain `pytest -v` from
  `dev/backend` both collect and pass **173/173**, 0 failed (the
  Increment-1-era bare-`pytest`-vs-stale-installed-package gotcha noted
  above no longer reproduces). `npm test -- --run` from `dev/frontend`
  passes **34/34**. No suite here has zero tests.
- **Both security-architect-mandated regression tests (ARCHITECTURE_KB
  §9.3) exist and are meaningful, not just present:**
  `test_repeated_profile_level_upload_replaces_not_accumulates` asserts
  exactly one `memory_id IS NULL` row/file remains after a second
  profile-level upload, checking both the DB row count and the on-disk
  file count (not just one or the other); `test_avatar_replacement_is_cross_profile_isolated`
  asserts profile B's uploads never touch profile A's rows/files.
- **Both security-architect code-level conditions confirmed by direct code
  read, not by trusting a comment:** the cleanup query's `profile_id`
  filter is explicit in the actual SQL (`app/photos.py`, both the SELECT
  and DELETE), and the deliberate `delete()`-authz-bypass is documented in
  an explicit docstring comment at the same call site.
- **Frontend spot-check, Avatar.tsx and Lightbox.tsx:** fallback-to-dot on
  image load error and per-surface size/ring are both directly exercised
  in `Avatar.test.tsx`; Escape/backdrop dismiss and multi-photo vs.
  single-photo nav are directly exercised in `Lightbox.test.tsx`. **Gap
  found:** Lightbox's Tab-trap (keyboard focus cycling among dialog
  controls) and its focus-return-to-trigger-on-close behavior are both
  implemented (confirmed in `Lightbox.tsx`/`JourneyScreen.tsx`) and named
  in the Increment-4 commit message as delivered, but neither has an
  actual regression test — no `Tab`/`Shift+Tab` keydown assertion, no
  post-close `document.activeElement` assertion. Sent back to code-agent
  to add the two missing test cases.
- **`next build`-against-live-dev-server contamination check: clean.** No
  incidental `tsconfig.json`/`next-env.d.ts` diff in the Increment-4
  frontend commit; `next.config.js`'s `NEXT_DIST_DIR` isolation is in
  place and working tree is clean.
- **Gate verdict: hold.** Everything else re-verified and passing; the one
  Lightbox test-coverage gap is a missing-test gap (the underlying
  implementation reads correctly on inspection), not a failing/broken
  behavior, but it is being treated as blocking per this project's default
  policy (no advisory suites recorded) until code-agent adds the two tests.

**2026-07-12: Test gate, Increment 4 — CLOSED, 4/4 suites pass.**
Architecture: PASS, verified `avatar_photo_id`'s derived-field design,
the new index, and the exact create→cleanup→accent-set ordering
line-by-line against §9.3. Security: PASS, all 3 conditions confirmed in
shipped code; the suite's own live-check caveat (no Bash that session)
was closed directly by the orchestrator — real double-upload against
the running backend confirmed exactly one `memory_id IS NULL` row/file
survives, old file genuinely unlinked from disk. UX/accessibility: PASS,
0 blocking, 2 non-blocking (optimistic-preview `onError` gap; shell
switcher-trigger buttons still show the flat dot even with a photo —
both flagged as future-increment candidates, not this scope). Unit/
integration: held for one missing (not broken) test pair — Lightbox's
Tab-trap and focus-return-to-trigger were implemented but untested;
code-agent added both, 34 → 36 frontend tests, all passing. Red-team/
bias suite deliberately skipped — zero LLM surface in F14/F15/F16, same
reasoning as Increment 3's auth-activation pass. **All findings closed.**

**2026-07-12: Review gate, Increment 4 — Approve.** Diff hygiene clean
across all 3 commits; decision-intent match confirmed against UX_KB §8/
§8.1a and ARCHITECTURE_KB §9.3; no cross-cutting consistency issues.
**Proceeding to Deploy gate, Increment 4.**

**2026-07-12: Test gate, Increment 5 (F13 chat history + dynamic suggested
prompts + "Ask" rename/stage card) — unit/integration suite independently
re-verified (test-agent).** Full structured per-scenario evidence at
`test-evidence/unit-integration-increment5-2026-07-12.md`. Suite policy:
blocking (no suites recorded as advisory for this project).

- **Counts independently re-confirmed, both invocations agree with
  code-agent's claim:** `python -m pytest -v` and plain `pytest -v` from
  `dev/backend` both collect and pass **197/197**, 0 failed. `npm test --
  --run` from `dev/frontend` passes **53/53** (9 test files). No suite here
  has zero tests.
- **All six ARCHITECTURE_KB §10.9 Test-gate ownership items confirmed real,
  by reading the actual test bodies, not just names/counts:**
  1. **Contract test** — `test_chat_response_gains_session_id_additive_only`
     asserts the response's key set is exactly `{text, disclaimer,
     session_id}`; `test_chat_omitting_new_session_still_works_unaffected`
     confirms clients that never send `new_session` keep landing in the same
     session; the pre-existing `test_chat_response_payload_contains_exact_
     disclaimer_constant` still passes unmodified, confirming `text`/
     `disclaimer` content, not just key names, is unchanged.
  2. **4-hour boundary property test** — genuinely manipulates time via an
     injectable `now=` datetime parameter on `ChatSessionStore.resolve_or_
     create_session` (not a sleep or a decorative constant check): >4h apart
     produces two distinct session ids and two rows in `list_for_profile`;
     <4h apart with no forced new session reuses the same session id and
     produces one row.
  3. **Snippet immutability** — `test_snippet_set_once_at_creation_never_
     recomputed` sends a second, different message into the same session
     and asserts the snippet still equals the *first* message, with
     `message_count` correctly incremented to 4 — a real "does it change"
     check, not just "was it set once."
  4. **Cascade-delete** — `test_profile_delete_cascades_chat_sessions_and_
     messages` queries the real sqlite connection directly after a profile
     delete and asserts zero rows remain in both `chat_sessions` and
     `chat_messages`, extending the project's existing FK-cascade pattern.
  5. **Family-scoping** — all three new surfaces (`GET /profiles/{id}/
     chat_sessions`, `GET /chat_sessions/{id}/messages`, `DELETE
     /chat_sessions/{id}`) have dedicated cross-family tests asserting 404
     (not 403); the delete-route test additionally re-authenticates as the
     owning family afterward and confirms the session was NOT actually
     deleted despite the cross-family 404.
  6. **Delete-permission** — `test_caregiver_can_delete_chat_session_not_
     owner_only` genuinely joins a second family member via the real invite
     flow (not the owner) and asserts that non-owner's delete returns 200,
     per security-architect's confirmed any-caregiver decision (§10.8).
- **Frontend spot-check, `ChatScreen.test.tsx`, assertions read directly
  (not just test names):** session-resume-on-open asserts `listChatMessages`
  is called with the *most-recent* session's id and that the resumed message
  renders inside `.lm-chat-main` specifically; the dynamic suggested-prompt
  chips test asserts the server's exact prompt text renders AND explicitly
  asserts the static fallback pool text is absent on the success path
  (`queryByText(...) === null`) — the stronger, correct check — with a
  separate test confirming the static pool appears only when the fetch
  rejects; the stage card test asserts exactly 4 `.lm-domain-chip` elements
  all sharing the identical className (no filled/empty modifier class,
  confirming true equal visual weight) plus a separate assertion that no
  progressbar/ring/fill element exists; the "Ask" rename test positively
  asserts the new heading text is present.
- **`next build`-against-live-dev-server contamination check (3
  crashed/resumed attempts): clean.** `git log -p --follow` on
  `frontend/tsconfig.json` and `frontend/next-env.d.ts` shows exactly one
  commit each across the entire dev-repo history (the original Increment-1
  scaffold) — zero touches from either Increment-5 commit or any
  uncommitted working-tree state; `git status` is clean and `git diff HEAD`
  on both files is empty.
- **Gate verdict: PASS.** No gaps found between code-agent's claimed
  coverage and actual coverage; every mandated Test-gate item is backed by a
  genuine, specific test. This suite does not block the gate.

## Ports (local dev, assigned by deploy-agent 2026-07-11)
- Backend (FastAPI/uvicorn): `8000`
- Frontend (Next.js): `3000`
- Stable across redeploys — reuse these, do not reassign, unless a conflict
  forces a change (record any change here if it happens).

**2026-07-11: Test gate, Increment 2 — CLOSED.** 5 suites run (unit/
integration, UX/accessibility, architecture, security, red-team/bias).
Initial pass: unit/integration conditional-pass (1 coverage gap), UX
BLOCK (4 blocking), architecture BLOCK (4 blocking, incl. a real bug —
memory-only delete orphaned encrypted photo files due to a
`Memory.photo_ids` type mismatch), security pass-conditional (2 checks
needed Bash the agent lacked, closed directly by the orchestrator: 91/91
→ later 101/101 tests, `python -m pytest`/plain `pytest` parity, `.env`/
`data/photos` git-ignore confirmed), red-team/bias pass clean. All 13
findings (7 blocking, 6 non-blocking) fixed by code-agent in one pass;
re-verification passes by architecture and UX suites both confirm
**CLOSED** on every finding, plus one new trivial non-blocking item
(duplicate `<h1>` on Journey) found and fixed immediately. Backend:
91 → 101 tests, all passing, both pytest invocations identical. Also
this session: F12 (hardened auth suite — MFA/OAuth/password-reset)
added to `FEATURES.md`'s later backlog per human request, referencing
SECURITY_KB §1.6's existing revisit triggers rather than inventing new
criteria.

**2026-07-11: Review gate, Increment 2 — Approve.** Diff hygiene clean
across all 14 Increment-2 commits; decision-intent match confirmed
against PLAN §4.2-§4.4 and all 8 documented judgment calls. One trivial
finding: `TimelineEntry.photo_ids` (a TypedDict, not runtime-validated)
was left `list[int]` when the real `Memory.photo_ids` type fix landed —
inert at runtime, fixed same-day for documentation accuracy. 101/101
tests still passing. **Proceeding to Deploy gate, Increment 2.**

## Current Status
Architecture gate held 2026-07-10 (solution-architect + security-architect
joint design, responsible-ai-architect advisory) — **pending human
approval**. All PLAN.md §6 open questions resolved; see Architecture
Summary above and `knowledge/ARCHITECTURE_KB.md` /
`knowledge/SECURITY_KB.md` / `knowledge/RESPONSIBLE_AI_KB.md` for full
detail. **Item 5 (email/notification infra) was subsequently revised
same-day per human override**, and security-architect's independent
re-consultation on that revision is now complete (see Decisions Log above
and `SECURITY_KB.md` §1.7/§5/§6.1) — approved conditional on two
unsubscribe-route implementation requirements and a privacy-policy/vendor-
disclosure item, both tracked as pre-production checklist items rather than
Code-gate blockers.

**2026-07-10: Code gate, Increment 1 (F1-F5) built.** See "Increment 1
implementation summary" above for the full file list, judgment calls, and
what's deliberately not built yet. Backend unit/integration tests (30)
pass; frontend type-checks and builds cleanly. Not yet run: the
UX/accessibility, architecture, security, and red-team/bias suites
(test-agent, ui-ux-designer, solution-architect, security-architect,
responsible-ai-architect) that PLAN §7-A through §7-E specify as
Increment-1's blocking Test-gate criteria — those are the Test gate's
job, not code-agent's, and are the next step before Increment 2 starts.
[code-agent]

**2026-07-11: Test, Review, and Deploy gates for Increment 1 all closed.**
Test gate: 7 findings fixed + 3 additional live-red-team-discovered defects
fixed, 48/48 tests passing. Review gate: approved, one architecture/code
divergence found and closed (stale-age backstop implemented). Deploy gate:
backend (`:8000`) and frontend (`:3000`) confirmed genuinely serving,
health-checked, real end-to-end `/chat` call verified. **Increment 1
(F1-F5) is deployed (dev, local).** Proceeding to Increment 2 (F6-F7 +
digest content) per PLAN §4.7's three-increment structure.

**2026-07-11: Increment 2 (F6/F7/F8-content) built; two open design
questions code-agent flagged were resolved by solution-architect
pre-Test-gate** — HEIC EXIF/theme gap closed (new `pillow-heif` dependency
approved, implementation steps specified for code-agent), multi-photo
theme-source tracking accepted as a documented limitation with a revisit
trigger. See Decisions Log above and `knowledge/ARCHITECTURE_KB.md` §9.
Proceeding to Test gate for Increment 2 next.

- **2026-07-11: code-agent — ARCHITECTURE_KB §9.1 HEIC fix implemented,
  small scoped follow-up ahead of Test gate.** `pillow-heif` added to
  `dev/backend/pyproject.toml`; `pillow_heif.register_heif_opener()`
  called once at import time in `app/main.py` (module-level, so it's
  active for test collection too, not only a running server). Removed
  `_strip_exif`'s HEIC special-case in `app/photos.py`: HEIC now maps to
  Pillow's `"HEIF"` save format (not `"JPEG"`) so the re-saved bytes stay
  HEIC — this preserves the existing invariant every other accepted
  format already had, that `PhotoMeta.content_type` (the sniffed type)
  always matches the on-disk/served format. One judgment call the KB's
  five steps didn't anticipate: `pillow-heif`'s HEIF encoder auto-carries
  forward any EXIF already present in `image.info["exif"]` on re-save
  unless it's explicitly cleared first (unlike the JPEG/PNG/WEBP save
  path, where simply omitting the `exif=` kwarg is enough) — caught by
  the new regression test, fixed with an explicit `image.info.pop("exif",
  None)` before every re-save (JPEG/PNG/WEBP unaffected, since they never
  populated that key in the first place). No changes needed to
  `photo_theme.py`, confirming the KB's "zero pipeline-logic changes"
  expectation for extraction. `pip install pillow-heif` pulled no new
  transitive dependencies beyond Pillow itself (already a floor
  dependency) — no conflict with the plan's approved dependency list.
  Three new regression tests (`tests/test_photos.py`): HEIC upload
  accepted (201), HEIC EXIF-GPS stripped on upload (same assertion
  shape as the JPEG test), HEIC upload reaches `photo_theme.
  extract_accent` and sets the profile's accent columns. Full suite:
  88 -> 91 backend tests, all passing. [code-agent]

**2026-07-11: Increment 2 Test gate run — architecture (blocking FAIL),
UX/accessibility (blocking FAIL), unit/integration (conditional pass,
non-blocking gap) — 13 findings total, see evidence:
`test-evidence/{architecture,ux-accessibility,unit-integration}-increment2-
2026-07-11.md`. Sent to code-agent for a fix pass rather than proceeding
to Review gate.**

**2026-07-11: Increment 2 Code-gate fix pass — all 13 findings closed.**
See the Decisions Log entry above for the full per-finding breakdown. One
real defect found and fixed in the process (a `Memory.photo_ids` type
mismatch that made memories with attached photos fail validation, masking
what the architecture evidence had read as "unlinking never happens" —
the unlink code was already correct). Backend suite 91 -> 101 passing,
verified identical under both `python -m pytest -v` and plain `pytest -v`
from `dev/backend/`. Frontend `tsc --noEmit` and `next build` both clean.
`knowledge/ARCHITECTURE_KB.md` §0/§3/§6.1 updated to match the fix pass
(store-interface wording, `photo_meta.id` shape note, `/digest` framing-
check correction). Ready for solution-architect/ui-ux-designer/test-agent
to re-verify and, pending that, Review gate. [code-agent]

**2026-07-11: Deploy gate, Increment 2 (local) — verified up, ready.**
[deploy-agent] Found both `:8000` (backend) and `:3000` (frontend) already
listening from a prior session — stale Increment-1-era processes, not
verified as running current Increment-2 code. Killed both cleanly and
restarted fresh from `dev/backend` (`.venv/bin/uvicorn app.main:app --port
8000`) and `dev/frontend` (`npm run dev -- --port 3000`), reusing the same
recorded ports (no reassignment). Confirmed genuinely serving (not just
process-exit-0) via health check + full new-surface round-trip, not process
existence alone:
- `GET /health` -> `200 {"status":"ok"}`.
- F6: `POST /profiles` (id=1) -> 201; `POST /profiles/1/memories` -> 201
  real memory row; `GET /profiles/1/timeline` -> 200, real chronological
  merge of the new memory with server-computed `age_at_moment` interleaved
  among CDC-bucket chapter markers -- not a stub/empty array.
- F7: uploaded a real 100x100 JPEG (Pillow-generated, 824 bytes) to
  `POST /profiles/1/photos` -> 201, real `uuid4`-hex photo id (not an
  autoincrement int, per the Increment-2 schema change). `GET
  /profiles/1/photos/{id}` -> 200, `content-type: image/jpeg`, body
  byte-identical to the original upload (`cmp` confirmed) -- decrypt-on-
  serve genuinely works. Independently confirmed the on-disk file at
  `dev/backend/data/photos/1/{id}` is `file`-typed as opaque ASCII text
  (Fernet ciphertext), not JPEG, and differs byte-for-byte from the
  plaintext upload -- encryption at rest is real, not a pass-through.
- F8: `GET /profiles/1/digest` -> 200, real content (age line, 3 curated
  milestones, 2 activities with supervision notes, memory-prompt nudge,
  full disclaimer text) -- not an empty/stub payload.
- Frontend: fresh `next dev` process on `:3000` (new PID, distinct from
  the stale one killed) -> `GET /` returns 200 with `<title>little-
  milestones</title>`, confirming it's serving this project, not a
  leftover process from something else.
- Backend log reviewed end-to-end for this session: every request 200/201
  as expected, zero 4xx/5xx besides one intentional 422 during smoke-test
  schema discovery (missing `display_name` on first `POST /profiles`
  attempt -- corrected, not a product defect).
- `target_env=local` only, per MVP scope -- no cloud deploy attempted, per
  `admin/ROADMAP.md`'s explicit deferral.

**Deploy gate: ready.** Ports unchanged (`8000`/`3000`, recorded above).
Handing off to test-agent for the template's documented smoke test next.
Current Status remains as previously recorded pending human approval of
this gate -- deploy-agent does not set "deployed" status unilaterally.

**Increment 2 (F6-F7-F8 content) is deployed (dev, local).** Test,
Review, and Deploy gates are all closed for this increment. Proceeding
to Increment 3 (F9 buying recommendations, F10 auth activation +
multi-caregiver, F8 email delivery) per PLAN §4.7.

**2026-07-11: Increment 3 Code gate — F9, F10, and F8 delivery built.**
See "Increment 3 implementation summary" above and the matching Decisions
Log entry for the full file list, 9 documented judgment calls, and two
items explicitly flagged rather than silently resolved (F8 real sending
stays disabled pending an unmet Resend-domain-verification precondition;
`MAILING_ADDRESS` is a placeholder pending a real address). Backend:
101 → 165 tests, both `python -m pytest -v` and plain `pytest -v` from
`dev/backend/` reporting identical results. Frontend `tsc --noEmit`/`next
build` both clean. This is the final increment per PLAN §4.7 — not yet
run: the Test gate's five suites (unit/integration, UX/accessibility,
architecture, security, red-team/bias) against PLAN §7-I, §7-J, §7-H(4-5),
and the §7-A regression-under-auth requirement. [code-agent]

**2026-07-11: Test gate, Increment 3 — CLOSED.** All 5 suites run.
Unit/integration: PASS (168/168 after a route-signature contract test
was added and 2 false-negative test-authoring bugs fixed; CPSC
fixture-injection test confirmed real, all §7-I/§7-J items covered).
UX/accessibility: 2 blocking + 2 non-blocking findings (raw HTTP error
text shown on auth screens; email/password inputs missing standard
styling/touch-target; Settings desktop layout undecided; heading-level
skip) — all fixed by code-agent, 168/168 maintained. Architecture: PASS
after 3 crashed attempts (transient API errors, not file-safety
incidents — `ARCHITECTURE_KB.md` confirmed untouched after each crash)
— auth-seam contract, F8 delivery contracts (mocked Resend headers +
content-free body, scheduler due-check truth table), CPSC filter, and
the plaintext-`unsubscribe_token` deviation all verified; addendum
documenting that deviation added to ARCHITECTURE_KB §5.4. Security:
APPROVE, then independently live-verified by the orchestrator (404
cross-family, 401 no-session, 403 role-restricted, all confirmed live
against a real running backend; git history confirmed clean of
secrets). Red-team/bias: PASS, with an explicit reasoned decision NOT
to re-run the 7 live adversarial scenarios (auth sits upstream of
unchanged guardrail code; the broader pytest suite now running under
real authenticated sessions is stronger evidence for PLAN §7-J item 37
than 7 sampled live prompts would be) — boundary condition noted: this
reasoning doesn't carry forward to any future change touching
`chat.py`'s response path, `prompts.py`, or `guardrails.py` itself.
**All findings closed.**

**2026-07-11: Review gate, Increment 3 — Approve.** Diff hygiene clean
across all 9 Increment-3 commits; decision-intent match confirmed
against PLAN §4.5-§4.6 and ARCHITECTURE_KB §5. A cross-increment
look-back (all 3 increments' commit history) found no accumulated
drift beyond two stale-doc lines (`FEATURES.md`'s F8 description still
described delivery as undecided; `memory/INDEX.md`'s stage was stale) —
both corrected same-day. **Proceeding to Deploy gate, Increment 3 —
the final gate of this project's original F1-F10 scope.**

- **2026-07-11 — Deploy gate, Increment 3 (local) — verified up, ready.
  This is the FINAL gate of this project's original F1-F10 scope.**
  [deploy-agent] Found both `:8000` (backend) and `:3000` (frontend)
  already listening from a prior session — stale processes, not verified
  as running current Increment-3 code. Killed both cleanly (PIDs 30904,
  28701) and restarted fresh from `dev/backend` (`.venv/bin/uvicorn
  app.main:app --port 8000`) and `dev/frontend` (`npm run dev -- --port
  3000`), reusing the same recorded ports (no reassignment; see Ports
  section above). Confirmed genuinely serving, not just process-exit-0.

  **New Increment-3 surface (auth now required on every data route —
  the biggest behavioral change of the project):**
  1. `GET /health` -> `200 {"status":"ok"}` — still unauthenticated, as
     required.
  2. `GET /profiles` with no session cookie -> `401 {"detail":"Not
     authenticated"}` — confirms auth is actually enforced, not just
     built-and-unused.
  3. `POST /auth/signup` (real test email/password) -> `201`, real
     `lm_session` cookie set (`HttpOnly`, confirmed via cookie jar).
  4. Using that session: `POST /profiles` -> `201`; `GET /profiles` ->
     `200` with real data (the new profile plus a pre-existing one from
     earlier live-verification sessions this increment — expected,
     harmless local dev data). Full auth-gated flow confirmed end to
     end.
  5. `GET /profiles/1/products` (with session) -> `200`, two real
     curated recommendations (`simple_building_blocks`,
     `picture_naming_books`) — cross-checked against
     `app/data/cpsc_denylist.json`'s 12 denied categories: neither
     returned item is denylisted.
  6. `POST /invites` (with session, as owner) -> `201`, real invite code
     (`lI5tRq7cxP84`, 12-char base64url, 7-day expiry).
  7. Frontend confirmed serving: `GET /` -> `200`, correct
     `<title>little-milestones</title>`. `AuthScreen.tsx`,
     `SettingsScreen.tsx`, `ProductsPanel.tsx` all present under
     `dev/frontend/components/` and wired into `app/page.tsx` (grep-
     confirmed) — **visual/browser verification not possible without a
     browser tool; noted as a gap, not silently skipped.**
  8. Digest scheduler confirmed genuinely NOT auto-starting: backend
     startup log shows no scheduler-start line; `grep -i scheduler` on
     the startup log returns nothing. `RESEND_API_KEY` and
     `ENABLE_DIGEST_SCHEDULER` both confirmed absent from
     `dev/backend/.env` (grep returned no matches for either key).

  **Full-system sanity check — F1-F5 (Increment 1) and F6-F8-content
  (Increment 2) surfaces re-verified live under a real session, now that
  auth wraps everything:**
  - `POST /chat` (profile 1, real message) -> `200`, real non-empty LLM
    text (age-bucket-appropriate activity suggestions), `disclaimer`
    field present in the JSON payload, R1-safe framing observed
    (no "behind"/"ahead" language).
  - `GET /profiles/1/timeline` -> `200`, real chronological merge of a
    pre-existing memory ("First laugh," from an earlier live-
    verification session) interleaved with CDC-bucket chapter markers
    and server-computed `age_at_moment` — not a stub.
  - `GET /profiles/1/photos` (no such collection route by design) ->
    `405`, expected. Found one **orphaned** `photo_meta` DB row from an
    earlier session (id `48d3eac8...`, no matching on-disk file) ->
    `GET /profiles/1/photos/{id}` correctly returned `404` and the
    backend logged `photo_orphaned_metadata profile_id=1` — graceful,
    logged handling of stale prior-session data, not a current-code
    defect. Verified this by performing a **fresh** upload/serve
    round-trip through the current session instead: `POST
    /profiles/1/photos` (real 100x100 JPEG) -> `201`; `GET
    /profiles/1/photos/{new_id}` -> `200`, byte-identical to the
    original upload (`cmp` confirmed) — decrypt-on-serve genuinely
    works. On-disk file independently confirmed as opaque ASCII
    (Fernet ciphertext), byte-different from the plaintext upload —
    encryption at rest is real, not a pass-through.

  Backend log reviewed end-to-end for this session: every request
  200/201 as expected except the three intentional negative-path checks
  (401 no-session, 405 no-collection-route, 404 orphaned-photo) — zero
  unexpected 4xx/5xx. CORS confirmed scoped to `http://localhost:3000`
  only with `allow_credentials=True` (required for the session cookie
  across the :3000 -> :8000 origin boundary, per Increment-3 judgment
  call 5). `target_env=local` only, per MVP scope — no cloud deploy
  attempted, per `admin/ROADMAP.md`'s explicit deferral.

  **Deploy gate: ready.** Ports unchanged (`8000`/`3000`, recorded
  above). Handing off to test-agent for the template's documented smoke
  test next. Current Status remains as previously recorded pending human
  approval of this gate — deploy-agent does not set "deployed" status
  unilaterally.

  **This completes the entire original F1-F10 approved scope** (Plan &
  Backlog gate, 2026-07-10) across all three increments — pending human
  approval of this final Deploy gate and the resulting Current Status
  update.

- **2026-07-11 — Deploy gate, Increment 3 (local) — re-verified against
  the live LAN-serving instances, ready. Supersedes the CORS/process
  details of the entry immediately above (which predates the LAN setup);
  the "ready" verdict and F1-F10-complete conclusion stand.** [deploy-agent]
  This run did **not** restart or kill anything — the orchestrator already
  had backend (`:8000`) and frontend (`:3000`) running, both bound to
  `0.0.0.0` so the human's phone can reach them at `10.0.0.47`, with
  `EXTRA_CORS_ORIGINS` extending the CORS allow-list (confirmed wired in
  `app/main.py`, `allow_credentials=True` preserved) and the frontend's
  `NEXT_PUBLIC_API_BASE_URL` pointed at the LAN IP. Human is actively using
  these for LAN/mobile testing and was explicitly told to keep them up, so
  this gate verified against the already-running processes (PIDs unchanged
  before/after: backend 32410, frontend 32433/32434) instead of the usual
  restart-and-confirm pattern.

  All checks run via `curl` against `http://localhost:8000` (same process
  as the LAN-reachable one):
  1. `GET /health` -> `200`.
  2. `GET /profiles` no session cookie -> `401` (auth genuinely enforced).
  3. `POST /auth/signup` (real test email `deploy-agent-verify+lm3@
     example.com`) -> `201`, real `HttpOnly` `lm_session` cookie set.
  4. With that session: `POST /profiles` -> `201`; `GET /profiles` ->
     `200` with the real created profile.
  5. `GET /profiles/{id}/products` -> `200`, two real curated items
     (`simple_building_blocks`, `picture_naming_books`) — cross-checked
     against all 12 entries in `app/data/cpsc_denylist.json`, neither
     returned category is denylisted.
  6. `POST /invites` (as owner) -> `201`, real invite code + 7-day expiry.
  7. F1-F5/F6-F8-content surfaces re-confirmed live under the same real
     session: `POST /chat` -> `200` non-empty, age-appropriate, R1-safe
     text; `GET /profiles/{id}/timeline` -> `200` real CDC-bucket chapter
     markers; photo upload/serve/delete round-trip (`POST` then `GET` then
     `DELETE` on `/profiles/{id}/photos/{photo_id}`, the collection-level
     `GET /profiles/{id}/photos` correctly `405`s by design, no such
     route) -> `201`/`200`/`200`, byte count matched on serve.
  8. Digest scheduler confirmed genuinely not auto-starting: `grep -i
     scheduler` on the live backend's stdout log (`/private/tmp/
     lm-backend.log`) returns nothing beyond the four expected startup
     lines (`Started server process` / `Waiting for application startup`
     / `Application startup complete` / `Uvicorn running`); `RESEND_API_KEY`
     and `ENABLE_DIGEST_SCHEDULER` both confirmed absent from `dev/backend/
     .env`; the live process's own environment (`ps eww`) also shows
     neither var set, consistent with `.env`.

  Test data cleanup: the test profile (`id=5`) and its one uploaded test
  photo were deleted via the API's own `DELETE /profiles/{id}` and
  `DELETE /profiles/{id}/photos/{id}` endpoints (both `200`) — confirmed
  gone from `GET /profiles` afterward. The one test user/family row
  (`deploy-agent-verify+lm3@example.com`, family_id 3) could not be
  cleaned up the same way — no user-delete endpoint exists in this scope
  (expected; not a gap) — left in place as a harmless, invisible-to-the-
  human-session DB row rather than reaching outside the API to hand-edit
  SQLite.

  **Deploy gate: ready.** Ports unchanged (`8000`/`3000`). ***Servers are
  being left running, per explicit human instruction*** — this is not the
  usual "confirm up" close-out; it's "confirm up AND stays up," since the
  human is actively browsing/mobile-testing against these exact processes.
  Handing off to test-agent for the template's documented smoke test.
  Current Status remains as previously recorded pending human approval of
  this gate — deploy-agent does not set "deployed" status unilaterally.

  **This re-confirms completion of the entire original F1-F10 approved
  scope** (Plan & Backlog gate, 2026-07-10) across all three increments —
  pending human approval of this final Deploy gate and the resulting
  Current Status update.

**2026-07-11: Increment 3 (F9-F10-F8 delivery) is deployed (dev, local).**
Test, Review, and Deploy gates all closed. Also added LAN/mobile
reachability this session (an operational convenience, not a gated
increment): backend/frontend both bound to `0.0.0.0`, backend CORS
extended via a new `EXTRA_CORS_ORIGINS` env var (additive — does not
change the `http://localhost:3000` default), frontend's
`NEXT_PUBLIC_API_BASE_URL` pointed at the LAN IP for phone testing.
Servers deliberately left running per explicit human instruction.

**All three increments (F1-F10) are now deployed (dev, local). This is
the entire originally-approved MVP scope for little-milestones,
complete.** Only F11 (conditional RAG mode) and F12 (hardened auth
suite, added 2026-07-11) remain in the later backlog, both explicitly
deferred and neither blocking this project's MVP completion.

- **2026-07-12: Code gate, Increment 4 (F14 profile avatars + upload
  affordance, F15 Journey lightbox, F16 Journey gallery view) built and
  committed to `dev/` in two logical commits (backend avatar_photo_id +
  photo-replace fix; frontend F14/F15/F16), per the Experience Design +
  Architecture consult (`knowledge/UX_KB.md` §8/§8.1a,
  `knowledge/ARCHITECTURE_KB.md` §9.3).** See "Increment 4 implementation
  summary" above for the full file list and four documented judgment
  calls (none scope-changing). 173 backend tests pass (up from 168, both
  `python -m pytest` and plain `pytest` agree); 34 frontend tests pass (up
  from 13); `tsc --noEmit`/`next build` both clean (build run against an
  isolated `NEXT_DIST_DIR` so the live `:3000` demo server was never
  touched; the build's incidental `tsconfig.json`/`next-env.d.ts`
  regeneration was reverted afterward). Both backend/security-architect
  conditions from ARCHITECTURE_KB §9.3 (explicit `profile_id` filter on
  the cleanup query; the authz-bypass code comment) and its required
  regression test (upload-twice leaves exactly one row/file) are
  implemented and verified, plus a cross-profile-isolation regression test
  beyond what was strictly asked. No backend server restart was performed
  this session (a Deploy-gate action) — the live `:8000` process predates
  this session's backend edits and will not reflect them until restarted,
  flagged explicitly rather than left implicit. [code-agent] Next: Test
  gate.

**2026-07-12: Increment 4 (F14 avatars+upload, F15 lightbox, F16
gallery) is deployed (dev, local).** Test (4/4 suites), Review
(approved), and Deploy gates all closed. Backend restarted on current
code and live-verified (`avatar_photo_id` confirmed present on a real
profile response); frontend confirmed serving current markup. One
caveat carried forward: no browser tool available this session, so
F14/F15/F16's actual visual rendering (avatar circles, lightbox overlay,
gallery grid) has not been screenshot-verified — functionally verified
via 36/36 frontend tests + live backend checks, but a human/browser
look is still the final confirmation. Both `dev/` and outer-repo history
are fully committed. Proceeding to Increment 5 (F13, chat history +
suggested prompts).

**2026-07-12: Increment 5 (F13) Code gate — built and committed.**
Experience Design (UX_KB §9/§9.5, including the human-requested "Ask"
rename + stage-card infographic addendum) and Architecture consult
(ARCHITECTURE_KB §10, security-architect-confirmed) both complete
before code started. Backend: `chat_sessions`/`chat_messages` schema,
4-hour conversation-boundary rule, additive `/chat` contract
(`session_id` in response, optional `new_session` in request), new
`GET /profiles/{id}/chat_sessions`, `GET /chat_sessions/{id}/messages`,
`DELETE /chat_sessions/{id}` (any caregiver), `GET
/profiles/{id}/suggested_prompts`. Frontend build hit 3 consecutive
transient background-agent crashes/stalls (infrastructure issues, not
code problems — each left the working tree in a safe, verified,
tsc-clean partial state); resumed and completed directly by the
orchestrator rather than a 4th subagent attempt. 197/197 backend tests
(both `python -m pytest`/plain `pytest` agree), 53/53 frontend tests
(16 new). Backend restarted on current code; live-verified
`/suggested_prompts` and `/chat_sessions` against the real tester
profile. Proceeding directly to Test gate — human is asleep, asked to
review Increments 5/6/7 together at the end, so gates proceed without
per-step pause per explicit instruction.

**2026-07-12: Test gate, Increment 5 — CLOSED, 4/4 suites pass, zero
blocking findings.** Architecture: PASS (schema, 4-hour boundary,
snippet immutability, additive `/chat` contract, server-side
suggested-prompts, no pagination — all verified line-by-line against
§10). Security: PASS, live-verified by the orchestrator (cross-family
404 on read+delete with survival confirmation, any-caregiver delete
confirmed live via a real invited caregiver — not owner). UX/
accessibility: APPROVE, 4 non-blocking notes (stage card omits age —
shown elsewhere on screen; pre-existing app-wide dialog aria-label gap,
not a new regression; a doc-only column-width typo in UX_KB; one
inferred-not-measured touch-target note). Unit/integration: PASS,
197/197 backend (both invocations) + 53/53 frontend independently
re-verified, all 6 ARCHITECTURE_KB §10.9 mandated test items confirmed
genuine by reading actual assertions, not names. Red-team/bias suite
again deliberately skipped (chat's LLM/guardrail surface unchanged this
increment). **Proceeding to Review gate, Increment 5.**

**2026-07-12: Review gate, Increment 5 — Approve, zero issues.** Diff
hygiene clean across both commits; explicitly confirmed no leftover
artifacts from the 3 interrupted background-agent attempts (clean
working tree, no dead code, no stray files, tsc clean). Decision-intent
match confirmed against UX_KB §9/§9.1/§9.2/§9.5 and ARCHITECTURE_KB §10
line-for-line. **Proceeding to Deploy gate, Increment 5.**
