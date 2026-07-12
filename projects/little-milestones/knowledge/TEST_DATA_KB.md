# TEST_DATA_KB — little-milestones

Synthetic test-data record. Created 2026-07-11 by the orchestrator (the
platform's `synthetic-data-agent` is still a roadmap item — see
`admin/ROADMAP.md`; this file follows the KB shape `mas-architect`
specified for that future agent, so its content transfers directly when
the agent ships).

## Tester account

- Email: `tester@example.com` (password known to the human; owner role,
  family_id 4)
- Profile: **Emma**, DOB 2025-08-11 (11 months at creation), full-term
- Digest opt-in: true. One live invite code issued for caregiver-join
  testing.

## Character sheet — Emma (synthetic imagery)

**Reuse this block verbatim in every image-generation prompt so all
images read as the same child** (human requirement, 2026-07-11:
"preserve the kid's profile so that it looks the same kid across the
board"):

> a baby girl with soft curly brown hair, big warm brown eyes, round
> rosy cheeks, and a small pink bow in her hair, soft watercolor
> storybook illustration, gentle pastel palette, warm light, consistent
> character design

Scene text is appended as: `The same baby girl {scene description}.`

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

## Volume presets (for the future synthetic-data-agent)

- **low**: 1 profile, 3-4 memories, 2-3 images
- **medium** (this batch): 1 profile, ~14 memories, 15 images, digest
  opt-in on, one invite issued
- **high**: 2+ profiles (incl. one preterm for corrected-age surfaces),
  20+ memories each, multi-caregiver family exercised via a consumed
  invite

## Reset/reload

No one-command reset exists yet — deleting the tester profile via
`DELETE /profiles/{id}` cascades memories/photos correctly (verified at
the Increment 2/3 Test gates), which is the manual reset path today.
The scripted `seed-data.sh reset|reload` mechanism is part of the
synthetic-data-agent roadmap item (code-agent owns the script per
`mas-architect`'s division of labor).
