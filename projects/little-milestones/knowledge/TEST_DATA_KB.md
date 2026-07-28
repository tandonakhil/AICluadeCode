# TEST_DATA_KB — little-milestones

Synthetic test-data record. Created 2026-07-11 by the orchestrator (the
platform's `synthetic-data-agent` is still a roadmap item — see
`admin/ROADMAP.md`; this file follows the KB shape `mas-architect`
specified for that future agent, so its content transfers directly when
the agent ships).

## Tester account

- Email: `tester@example.com` (password known to the human; owner role,
  family_id 4)
- Profiles (as of run 2, 2026-07-27): **Emma** id 6, DOB 2025-08-11,
  full-term; **Rowan** id 8, DOB 2024-11-19, born 7 weeks early.
- Digest opt-in: true. One live invite code issued for caregiver-join
  testing.

## Character sheet — Emma (synthetic imagery)

**Reuse this block verbatim in every image-generation prompt so all
images read as the same child** (human requirement, 2026-07-11:
"preserve the kid's profile so that it looks the same kid across the
board"). **Revised 2026-07-12 per human request: photorealistic, not
cartoon — purely AI-generated synthetic person, never any real child:**

> photorealistic candid family photograph of a baby girl with soft
> curly light-brown hair, big warm brown eyes, round rosy cheeks, and a
> small pink hair bow, natural window light, shallow depth of field,
> shot on a modern mirrorless camera, soft warm tones, entirely
> AI-generated synthetic person, consistent facial features across a
> photo series

Scene text is appended as: `The same baby girl {scene description}.`

(The original watercolor-storybook character sheet from the 2026-07-11
batch is superseded — that batch was fully replaced in the app on
2026-07-12; the human's own uploaded photo on the "First Hotel Visit"
memory was left untouched in both swaps.)

## Generation parameters (2026-07-11 batch)

- Provider/model: OpenAI `gpt-image-1-mini` (key reused from
  policy-lookup-assistant with explicit human approval, 2026-07-11 —
  the older `dall-e-3` model is not available on this key)
- Size `1024x1024`, quality `medium`, one image per call, ~2s spacing
- 15 scenes: portrait (profile-level photo) + 14 journey moments
  spanning 2-11 months (coos, first smile, rolling, giggle-at-puppy,
  sitting, first solids, crawling, first tooth, babbling, pulling to
  stand, paddling pool, waving bye-bye, beach, first steps)
- Generation script pattern preserved at the orchestrator level; images
  are uploaded through the real API (`POST /profiles/{id}/photos`,
  multipart, with `memory_id` where attached) so they exercise the full
  EXIF-strip → encrypt-at-rest → theme-extraction pipeline, never
  hand-placed on disk.

## Run log

### Run 2 — 2026-07-27, `synthetic-data-agent`, volume **medium**

First run by the registered `synthetic-data-agent`. Goal: make the
`tester@example.com` family (family_id 4) look like a real, well-used
multi-child account for demo/test, and exercise the multi-profile and
corrected-age surfaces that a single full-term profile structurally
cannot show.

**All content is invented.** No real child, no real person's name or
details. Every record was created through the live API on
`http://127.0.0.1:8000` (`POST /profiles`, `POST /profiles/{id}/memories`)
— no direct SQLite writes, `prod/` untouched.

#### Personas

| | Emma (existing) | Rowan (new this run) |
|---|---|---|
| Profile id | 6 | **8** |
| DOB | 2025-08-11 | **2024-11-19** |
| Prematurity | full-term | **`born_early: true`, `weeks_early: 7`** |
| `age_summary` on 2026-07-27 | `11 months` | **`20 months (about 18 months corrected)`** |
| Checklist bucket | 9 | 18 (→ `coming_next` 24) |
| Memories after run | 20 (15 pre-existing + 5 added) | 18 (all new) |
| Date range of memories | 2025-08-25 → 2026-07-11 | 2024-11-21 → 2026-07-18 |
| Photos | 15 pre-existing (run 1) | none — see "Not done" |

Rowan is deliberately a *preterm* profile in a *different age band* from
Emma. That combination is what exercises the dual-age display
(`age_summary` = chronological + corrected), the profile switcher's
list call, per-profile activity bucketing, and multi-child scoping.
7 weeks early with a 2024-11-19 DOB keeps corrected age at 18 months —
under `ages.py`'s `CORRECTION_CUTOFF_MONTHS = 24`, so correction is
actually applied and both numbers render. A preterm profile older than
24 months corrected would silently fall back to chronological-only and
would *not* demo the feature.

#### Content shape

Roughly two-thirds ordinary everyday moments, one-third parent-tagged
milestones — a real parent's log, not a checklist. Ordinary entries:
favourite scratchy yellow blanket, asleep in the pram at the market,
avocado in the eyebrows, wellies-and-puddles, wrapping paper beating
every actual Christmas present, porridge behind the radiator, nobody
wanting to open the car door on a sleeping baby. Recurring motifs
(Rowan's yellow blanket, Emma's crinkly giraffe) run across multiple
entries so the Journey timeline reads as one continuous story.

`milestone_tag` used on 8 of Rowan's 18 (`coming home`, `first smile`,
`rolling over`, `sitting up`, `first solids`, `first tooth`, `crawling`,
`first steps`, `first words`); Emma's 5 additions are all untagged
ordinary moments, since her pre-existing 15 were already
milestone-heavy.

Guardrail compliance for every generated string:
- No developmental-norm framing anywhere — no "ahead", "behind",
  "on track", "should be doing X by now", no comparison to any other
  child or any expected age.
- Milestones sequenced against **corrected** age for Rowan (smile ~6wk
  corrected, rolling ~4mo, sitting ~6mo, crawling ~9mo, steps ~13mo,
  two-word combos ~17mo) so nothing reads as broken or implausible.
- No memory predates its profile's DOB (server-enforced anyway,
  `routes/memories.py` → 422).
- Notes are pronoun-free / name-based: the product deliberately does not
  collect gender (DOMAIN_KB R6 data minimization), so seeded prose must
  not smuggle it back in.

#### Regeneration

The generation script was a throwaway session script (deliberately not
committed — the durable mechanism is code-agent's `seed-data.sh`, not a
one-off of mine). It is trivially reconstructible: log in via
`POST /auth/login` with header `X-LM-Client: mobile`, read the bearer
token off the `X-LM-Session-Token` response header, then `POST /profiles`
with `{display_name, date_of_birth, born_early, weeks_early}` and
`POST /profiles/{id}/memories` with `{moment_date, title, note,
milestone_tag}` per row. Send the bearer token and `X-LM-Client` on
every call. To regenerate from clean:

1. `DELETE /profiles/8` as owner — hard-deletes Rowan and cascades all
   18 memories (and any photos). Emma's 5 added memories are individually
   removable via `DELETE /profiles/6/memories/{id}` (ids 35–39).
2. Re-run the script. Profile id will differ; `age_summary` will drift as
   real time passes — DOBs are fixed dates, not offsets from today, so
   after ~2026-09 Rowan's corrected age crosses 24 months and the dual
   display stops rendering. **Shift Rowan's DOB forward before any
   later demo** if the corrected-age surface needs to be shown.

#### Not done, deliberately

- **No photo uploads.** `POST /profiles/{id}/photos` needs real image
  bytes through the EXIF-strip → encrypt-at-rest → theme-extraction
  pipeline; out of scope for this run. Consequence: Rowan has
  `avatar_photo_id: null` and all three `photo_accent_*` tokens null, so
  Rowan's screens render the fixed default theme (UX_KB §6.4) while
  Emma's render her extracted accent. That contrast is itself a useful
  thing to look at, but it does mean Rowan's timeline is text-only.
- **No `scripts/seed-data.sh`.** It does not exist in `dev/` — see
  "Reset/reload" below. Per the agent contract that mechanism is
  code-agent's to build; this run did not work around it with an
  alternate seeding mechanism, it used the public API directly.

## Volume presets (for the future synthetic-data-agent)

- **low**: 1 profile, 3-4 memories, 2-3 images
- **medium** (this batch): 1 profile, ~14 memories, 15 images, digest
  opt-in on, one invite issued
- **high**: 2+ profiles (incl. one preterm for corrected-age surfaces),
  20+ memories each, multi-caregiver family exercised via a consumed
  invite

## Reset/reload

Still no one-command reset as of 2026-07-27 (run 2 re-confirmed:
`dev/scripts/` does not exist, so there is no `seed-data.sh` to invoke).
**Open gap for code-agent.** Deleting the tester profile via
`DELETE /profiles/{id}` cascades memories/photos correctly (verified at
the Increment 2/3 Test gates), which is the manual reset path today.
The scripted `seed-data.sh reset|reload` mechanism is part of the
synthetic-data-agent roadmap item (code-agent owns the script per
`mas-architect`'s division of labor).
