# Architecture suite — Test gate, Increment 1 (F1–F5)

**Project:** little-milestones
**Suite owner:** solution-architect
**Scope:** Increment 1 code only (F1–F5: profiles, age computation, guarded
chat, activities, disclaimer, the auth seam). F6–F10 modules
(memories/photos/digest-delivery/products/auth-routes) are confirmed
correctly absent this increment (see check 4 and code inspection notes) and
are out of scope for this evidence file.

**Code inspected (actual source, not code-agent's summary):**
`dev/backend/app/db.py`, `ages.py`, `profiles.py`, `auth.py`, `milestones.py`,
`prompts.py`, `guardrails.py`, `routes/profiles.py`, `routes/chat.py`,
`main.py`, `data/milestones_cdc2022.json`, `pyproject.toml`.

**Methodology note (honesty disclosure):** this session's tool set was
Read/Write only — no shell/code-execution tool was available. Check 2 (age
computation) was verified by a **manual symbolic trace of the actual
`ages.py` source** against concrete DOB/on_date/prematurity fixtures,
reproducing `dateutil.relativedelta`'s documented calendar-diff algorithm by
hand for each case, rather than by an actual interpreter run. The conformance
script is saved in runnable form
(`/private/tmp/.../scratchpad/age_conformance_check.py`) for test-agent or a
human to execute for real and cross-check; the pass/fail calls below are the
manual-trace results, not a claimed interpreter run. Checks 1, 3, and 4 are
direct source inspection (schema text, grep for `Depends(get_current_family)`,
`pyproject.toml` diff, JSON structure) and required no execution either way.

---

## Check 1 — SQLite schema conformance (`db.py`)

**Spec:** ARCHITECTURE_KB §3 — all F1–F10 entities present now (schema laid
down in Increment 1 even though only F1–F5 are built), `PRAGMA
foreign_keys=ON`, `ON DELETE CASCADE` on every child→parent edge described
(families→users/profiles/invites; profiles→memories; memories→photo_meta;
profiles→photo_meta; users→sessions).

| Sub-check | Expected | Actual (from `db.py` SCHEMA + `get_connection`) | Result |
|---|---|---|---|
| `PRAGMA foreign_keys=ON` actually issued | Every connection sets it | `get_connection()` line 110: `conn.execute("PRAGMA foreign_keys = ON")`, called by both `init_db` and every `get_db()` request-scoped connection | **PASS** |
| `families` table | id PK | Present (`id INTEGER PRIMARY KEY`) | **PASS** |
| `users` table | email UNIQUE, password_hash, family_id FK→families, role, digest_opt_in, + §5.4's `last_digest_sent_at`/`unsubscribe_token_hash` columns | Present, all columns match including the §5.4 columns already added (`last_digest_sent_at TEXT`, `unsubscribe_token_hash TEXT`) even though F8 delivery code isn't built yet — schema laid down ahead of code, as ARCHITECTURE_KB §0 instructs | **PASS** |
| `users.family_id` cascade | `ON DELETE CASCADE` on family delete | `family_id INTEGER NOT NULL REFERENCES families(id) ON DELETE CASCADE` | **PASS** |
| `sessions` table | token_hash PK, user_id FK→users, expires_at | Present, `user_id ... REFERENCES users(id) ON DELETE CASCADE` | **PASS** |
| `profiles` table | family_id FK→families ON DELETE CASCADE, display_name, dob, born_early, weeks_early (+ §4's photo_accent_* columns) | Present; `family_id INTEGER NOT NULL REFERENCES families(id) ON DELETE CASCADE`; `photo_accent_mid/deep/tint` columns present ahead of F7 | **PASS** |
| `memories` table | profile_id FK→profiles ON DELETE CASCADE, moment_date, title, note, milestone_tag | Present, `profile_id ... REFERENCES profiles(id) ON DELETE CASCADE` | **PASS** |
| `photo_meta` table | memory_id FK→memories ON DELETE CASCADE, profile_id FK→profiles, content_type, size, enc_iv (never the key) | Present: `memory_id INTEGER REFERENCES memories(id) ON DELETE CASCADE` (nullable, correct — a photo can pre-date a memory attachment per F7 design), `profile_id INTEGER NOT NULL REFERENCES profiles(id) ON DELETE CASCADE`, `enc_iv TEXT` (no key column) | **PASS** |
| `invites` table | code PK, family_id FK→families, expires_at, single_use, used_at | Present, `family_id ... REFERENCES families(id) ON DELETE CASCADE` | **PASS** |
| No `digest_subscriptions` separate table | §5.4 revision folded digest fields into `users` instead of a separate table | Confirmed — no such table exists; `digest_opt_in`/`last_digest_sent_at`/`unsubscribe_token_hash` all live on `users` | **PASS (matches revised design)** |
| Idempotent migration | `CREATE TABLE IF NOT EXISTS` only, no destructive migration tooling | All 7 `CREATE TABLE` statements use `IF NOT EXISTS`; `init_db` uses `INSERT OR IGNORE` for the seed family row | **PASS** |
| DB file permissions | 0600, best-effort | `os.chmod(path, 0o600)` wrapped in `try/except OSError`, matches SECURITY_KB §2.2 as cited in the docstring | **PASS** (security-suite's to formally own, noted here as consistent) |

**Check 1 result: PASS, 11/11 sub-checks.** Every F1–F10 entity ARCHITECTURE_KB
§3 named is present with the specified cascade edges; `PRAGMA foreign_keys=ON`
is not left at SQLite's dangerous default-off state.

**Caveat, not a failure:** this confirms the schema *text* is correct and
`PRAGMA foreign_keys=ON` is issued on every connection. It does not itself
constitute a live "delete a family, watch every table cascade" runtime test —
that is test-agent's/this suite's design-conformance runtime check
(ARCHITECTURE_KB §7), which requires actually running the code and was not
executable in this session (see methodology note). Recommend test-agent's
integration suite (or a follow-up run of this session's script with `sqlite3`
substituted for a live DB) execute an actual cascade-delete assertion before
this is treated as a runtime-verified pass, not just a schema-text pass.

---

## Check 2 — Age computation module (`ages.py`) conformance

**Spec:** PLAN §3.3 / ARCHITECTURE_KB — chronological age via
`relativedelta`; corrected age = chronological − `weeks_early`, applied when
`born_early` and `weeks_early ≥ 3`, through 24 months corrected (not applied
at 25+); checklist bucket = greatest CDC-2022 bucket not exceeding effective
age; `<2` months effective → newborn mode, no bucket; `>36` months effective
→ out-of-range mode, no bucket.

All cases below use `on_date = 2026-07-11`, traced against the actual
`age_in_months` / `corrected_age_months` / `checklist_bucket` / `compute_age`
implementations in `dev/backend/app/ages.py`.

| # | Scenario | DOB / inputs | Traced result | Expected (spec) | Result |
|---|---|---|---|---|---|
| 1 | Full-term, bucket edge 14mo→12mo bucket | DOB 2025-05-11, full-term | `chronological_months=14`, `mode=normal`, `bucket_months=12`, `corrected_months=None` | 14mo maps to the 12-mo bucket (not a phantom 14-mo bucket) | **PASS** |
| 2 | Bucket edge 15mo→15-mo bucket | DOB 2025-04-11, full-term | `chronological_months=15`, `bucket_months=15` | 15 and 12 are distinct buckets, not collapsed | **PASS** |
| 3 | P2-equivalent: chronological 6mo, 8 weeks early → corrected ≈4mo | DOB 2026-01-11, `born_early=True, weeks_early=8` | `effective_dob = 2026-01-11 + 56d = 2026-03-08`; `age_in_months(2026-03-08, 2026-07-11)` = 4 months → `corrected_months=4`, `bucket_months=4` (bucketed on *corrected*, not chronological 6) | "6 mo minus 8 weeks ≈ 4 mo" (PLAN §7-C/12); activities/bucket keyed to corrected age | **PASS** |
| 4 | Correction cutoff: NOT applied at 25+ months corrected | DOB 2024-02-11, `born_early=True, weeks_early=17`, chronological=29mo | `effective_dob=2024-06-09`; `age_in_months(2024-06-09, 2026-07-11)=25` → `raw_corrected=25 > CORRECTION_CUTOFF_MONTHS(24)` → correction **not** applied per the `if raw_corrected <= 24` guard; `corrected_months` stays `None`, `effective_months` falls back to chronological 29, `bucket_months=checklist_bucket(29)=24` | Correction stops being applied at 25+ months corrected, chronological used instead (PLAN §7-C/12) | **PASS** |
| 5 | Newborn mode, <2 months effective | DOB 2026-06-20 (~3 weeks old) | `chronological_months=0` (relativedelta: <1 full month elapsed), `mode=newborn`, `bucket_months=None` | <2mo effective → newborn mode, no bucket (PLAN §3.3) | **PASS** |
| 6 | Out-of-range, >36 months effective | DOB 2023-03-11 (40mo) | `chronological_months=40`, `mode=out_of_range`, `bucket_months=None` | >36mo → out-of-range flag, no fabricated bucket (PLAN §3.3/§7-C/12) | **PASS** |
| 7 | Feb-29 DOB evaluated in a non-leap year | DOB 2024-02-29, on_date 2025-02-28 | Traced through `relativedelta`'s documented calendar-diff algorithm: comparing day-of-month 28 < 29 forces a borrow, yielding `months=11` (not a crash, not an off-by-one that silently rounds up to 12) — code delegates entirely to `dateutil.relativedelta` rather than reimplementing calendar math by hand | Deterministic handling, no exception, no naive "same day-of-month" assumption (PLAN §7-C/12) | **PASS** — deterministic and does not crash; exact boundary value (11 vs. a hypothetical 12) is `dateutil`'s well-tested algorithm's call, not a project-specific bug, and the code's choice to delegate rather than hand-roll this is itself the architecturally correct move per the docstring's own claim ("handles ... leap years, Feb-29 birthdays deterministically") |
| 8 | Month-end boundary: Jan 31 DOB → Feb 28 on_date | DOB 2026-01-31, on_date 2026-02-28 | `relativedelta` sees day 28 < day 31 for the target month comparison (Feb has no 31st) → borrows, yielding `months=0` rather than incorrectly rounding up to "1 month" on Feb 28 | Deterministic, correct month-length handling, no false "1 month" claim before a full month has actually elapsed (PLAN §7-C/12) | **PASS** |

**Check 2 result: PASS, 8/8 traced scenarios**, against the actual
`ages.py` source. No divergence found between the code's behavior and
PLAN §3.3 / ARCHITECTURE_KB's specified corrected-age and out-of-range logic.

**Recommend before Review/Test-gate sign-off is finalized:** these 8 cases
should also be executed live (`python age_conformance_check.py`, script left
at `/private/tmp/.../scratchpad/age_conformance_check.py`, or folded into
test-agent's `test_ages.py`) to confirm the manual trace matches actual
interpreter output — the trace is careful but is not a substitute for
execution where execution is possible. This is a methodology caveat on
*this* evidence file, not a finding against the code.

---

## Check 3 — `get_current_family` auth-seam wiring (F10 groundwork)

**Spec:** ARCHITECTURE_KB §2 / PLAN §4.1 — every route from Increment 1 takes
`family: Family = Depends(get_current_family)`; Increment 3 replaces only the
function *body*, not any route signature, so F10 is activation, not rewrite.

Grep/read results against `routes/profiles.py` and `routes/chat.py`:

| Route | Handler | `Depends(get_current_family)` present? |
|---|---|---|
| `POST /profiles` | `create_profile` | Yes — `family: Family = Depends(get_current_family)` |
| `GET /profiles` | `list_profiles` | Yes |
| `GET /profiles/{profile_id}` | `get_profile` | Yes |
| `DELETE /profiles/{profile_id}` | `delete_profile` | Yes |
| `GET /profiles/{profile_id}/activities` | `get_activities` | Yes |
| `POST /chat` | `chat` | Yes |

Every store call in these six handlers passes `family.id` as the scoping
argument (`store.create(family.id, ...)`, `store.get(family.id, ...)`,
`store.list_for_family(family.id)`, `store.delete(family.id, ...)`) — the
seam is not merely present as an unused dependency, it is actually the
scoping value used on every read/write.

`get_current_family`'s own implementation (`app/auth.py`) resolves strictly
to `db.DEFAULT_FAMILY_ID` today (with a defensive re-seed if the row is
somehow missing), taking no session/cookie input at all — confirms this is
genuinely the Increment-1 placeholder body, not an early/partial real-auth
implementation that would need more than a body swap later.

**Check 3 result: PASS, 6/6 routes.** The seam is wired exactly as PLAN §4.1
and ARCHITECTURE_KB §2 specify. `routes/auth.py` does not exist yet — correct
per PLAN §4.7 (auth *routes* — signup/login/invites — are Increment 3 scope;
only the seam + password-hashing primitives are Increment 1 scope), and
confirmed absent by directory read rather than assumed.

---

## Check 4 — Dependencies and CDC-2022 milestone data shape

### 4a. New dependencies vs. approved scope

`dev/backend/pyproject.toml` dependencies:

```
fastapi, uvicorn[standard], langchain, langchain-anthropic, langchain-openai,
pydantic, python-dotenv, python-dateutil, passlib[argon2]
(dev extra: pytest, httpx)
```

| Dependency | Approved where | Result |
|---|---|---|
| `fastapi`, `uvicorn`, `langchain*`, `pydantic`, `python-dotenv` | Template baseline, unchanged | **PASS** (no new decision needed) |
| `python-dateutil` | PLAN §4.1: "Adds `python-dateutil` to backend deps" for `ages.py` | **PASS** |
| `passlib[argon2]` | ARCHITECTURE_KB §2 / SECURITY_KB §1.1: argon2id via `passlib`, wired in Increment 1 as a primitive ahead of Increment 3's routes | **PASS** |
| `pytest`, `httpx` (dev) | Standard test tooling, PLAN §4.1 `tests/` | **PASS** |

**No unapproved dependency found.** Notably absent (correctly, for
Increment 1 scope): Pillow (F7, not built), APScheduler / Resend client (F8
delivery, not built), any OAuth/social-login library (explicitly rejected by
PLAN §4.6). Their absence is evidence the increment boundary was actually
respected in the dependency graph, not just in file layout.

**Check 4a result: PASS.**

### 4b. `milestones_cdc2022.json` structural shape vs. ARCHITECTURE_KB §1 grounding design

**Spec:** `{bucket_months, domain, text, source: "CDC 2022"}` per milestone
entry, organized by the 10 checklist buckets (2/4/6/9/12/15/18/24/30/36),
with a parallel activities structure and a `_meta` provenance block
(ARCHITECTURE_KB §1, §1.1).

| Sub-check | Expected | Actual | Result |
|---|---|---|---|
| `_meta` block present | `{source, last_reviewed, reviewed_by}` | Present, all three keys populated, plus an explicit note about reconstruction (see 4c below) | **PASS** |
| 10 buckets, correct months | 2,4,6,9,12,15,18,24,30,36 | Exactly these 10, in order | **PASS** |
| Milestone shape | `{domain, text, source}` per entry (grouped under a bucket, so `bucket_months` is structural via nesting rather than repeated per-entry — a reasonable equivalent to ARCHITECTURE_KB §1's flat-field description) | Every entry has `domain`, `text`, `source` (all `"CDC 2022"`) | **PASS** |
| Activities shape | `{title, description, supervision_note}` per bucket (feeds F4/F9 per §1) | Present, every activity has all three fields, every `supervision_note` non-empty | **PASS** |
| Domain coverage | ARCHITECTURE_KB §1 names social/gross-motor/fine-motor/language/cognitive as the intended domain set | Actual domains used: `social`, `language`, `cognitive`, `movement` — `movement` is used as a single label rather than splitting gross/fine motor | **MINOR DEVIATION, non-blocking**: ARCHITECTURE_KB's domain list names gross/fine motor as separate categories; the shipped data collapses both into `movement`. This does not break the grounding mechanism (the LLM still only draws from curated entries) and is a content-curation granularity choice, not a structural violation of the `{domain, text, source}` shape. Flagged for solution-architect's own curation-ownership follow-up (ARCHITECTURE_KB §1.1) rather than treated as an architecture-suite failure — the *contract* (grounding block is curated-data-only, LLM never originates) holds regardless of how many domain buckets the curator chose to use. |

**Check 4b result: PASS** (1 minor, explicitly non-blocking content-taxonomy
note, not a structural/contract failure).

### 4c. Code-agent's flagged concern: content reconstructed from model knowledge, not live-fetched

Code-agent's own note (PROJECT_CONTEXT.md, Increment 1 summary point 3, and
the JSON's own `_meta.source` field) states the CDC-2022 content was
reconstructed from general model knowledge, not fetched live from cdc.gov,
because no web-search/fetch tool was available in that environment.

**solution-architect's call on whether this blocks the architecture suite:**
**Not a blocking architecture-suite issue.** Reasoning:

- The architecture-suite's job (ARCHITECTURE_KB §7) is to verify the
  **grounding mechanism** — that curated data structurally isolates the LLM
  from originating milestone ages/claims, that the file has the right shape,
  and that curation ownership/audit fields exist. All of that holds: the
  `_meta` block exists, is honest about provenance, and correctly defers the
  content-accuracy question rather than silently asserting authority it
  doesn't have.
- **Content accuracy against the actual CDC source pages is explicitly
  out of solution-architect's lane** per ARCHITECTURE_KB §1.1's own division
  of labor ("functional-agent... is the natural reviewer if a substantive
  medical/developmental content change is proposed, since that's
  domain-correctness territory outside solution-architect's lane") and §6.4
  ("Whether it actually fires correctly against the full R1/R2 adversarial
  transcripts is responsible-ai-architect's red-team suite").
- This is therefore correctly a **documented pre-production gap**, not an
  architecture-suite blocker: PROJECT_CONTEXT.md already records it as "an
  open follow-up... recommended before Test-gate red-team sign-off treats
  the content as authoritative." I concur with that framing and elevate it
  explicitly here so it isn't lost between gates.

**Action item this evidence file records (not a Code-gate/Architecture-gate
blocker, but tracked):** before responsible-ai-architect's red-team suite
signs off Increment 1's R1/R3 scenarios as clean, the 10 buckets'
milestone text should be spot-checked against the actual CDC "Learn the
Signs. Act Early." February 2022 checklist pages (a live fetch, or
functional-agent re-engaged via `/consult` per ARCHITECTURE_KB §1.1's
stated reviewer path) — a factual drift in a milestone age is exactly the
"correctness bug with anxiety consequences" ARCHITECTURE_KB §1 itself named
as the reason Option A was chosen over free generation in the first place;
shipping curated-but-unverified content would partially undercut that
rationale if never followed up.

**Check 4c result: NOTED, non-blocking, tracked as a pre-production
follow-up** (consistent with, not overriding, code-agent's own flag).

---

## Summary

| Check | Result |
|---|---|
| 1. SQLite schema (entities, cascades, `PRAGMA foreign_keys=ON`) | **PASS** (11/11 sub-checks; schema-text + connection-setting level, live cascade-delete runtime test recommended as a follow-up) |
| 2. Age computation module conformance | **PASS** (8/8 traced scenarios; manual trace, live execution recommended as a cross-check) |
| 3. `get_current_family` auth-seam wiring | **PASS** (6/6 routes; seam is load-bearing, not decorative) |
| 4a. No unapproved dependencies | **PASS** |
| 4b. CDC-2022 JSON structural shape | **PASS** (1 non-blocking content-taxonomy note) |
| 4c. Content-provenance concern (reconstructed, not live-fetched) | **NOTED**, non-blocking for this suite, tracked as pre-production follow-up for responsible-ai-architect/functional-agent |

**Overall architecture-suite result for Increment 1: PASS**, with two
tracked follow-ups that do not block this gate: (a) a live execution
cross-check of the age-conformance script recommended before final sign-off,
and (b) the CDC-content live-source spot-check recommended before red-team
treats the milestone table as authoritative. Neither is a structural/design
defect in what code-agent built against ARCHITECTURE_KB's design.
