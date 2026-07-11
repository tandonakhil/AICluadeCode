# UX/Accessibility Test-Gate Evidence — little-milestones, Increment 2

Owner: ui-ux-designer. Suite: UX/usability + accessibility (blocking, per
this project's Test Policy — no advisory suites recorded).
Scope: F6 (memory log + journey timeline), F7 (photo upload + photo
personalization), F8 content (in-app "This week" digest).

## Method note (read this before the findings)

**No shell/browser/screenshot tool was available to this agent in this
session** — only file-read/file-write. Per the task's own documented
fallback, this suite was run as a **source-level review** of the shipped
JSX/CSS against `knowledge/UX_KB.md`'s contract (§1.6, §5, §6, §1.9's UXR
rules) and against the two approved mockups
(`design-review/journey/timeline.html`, `design-review/screens/photo-upload.html`),
not a rendered/visual confirmation. Every finding below is traceable to an
exact file/line; nothing is inferred from a screenshot. This is the same
discipline this project's Increment-1 UX suite used when it was
static-only — flagged, not silently presented as equivalent to a real
render. Files reviewed:

- `dev/frontend/app/page.tsx`, `components/JourneyScreen.tsx`,
  `components/AddMemoryForm.tsx`, `components/DigestPanel.tsx`,
  `components/TodayScreen.tsx`, `components/ProfileSwitcher.tsx`,
  `app/globals.css`, `lib/types.ts`, `lib/api.ts`
- `dev/backend/app/routes/profiles.py`, `routes/photos.py`, `photos.py`,
  `profiles.py`, `photo_theme.py`, `db.py`

I could not confirm computed pixel contrast, real focus-trap behavior in
dialogs, or actual on-device tap-target hit-testing — those require a
running/rendered browser. Everything else below (DOM shape, class/CSS
wiring, presence/absence of fields in payload+component code) is a direct
source read, not a guess.

---

## Scenario 1 — R1 payload/UI compliance (critical hard rule)

**Assertion (UXR-1):** the rendered Journey DOM contains no
expected-vs-actual element: no norm axis, no second data series, no
"typical range" band, no status/on-track semantics, no color mapping of
memories to norms.

**Evidence:**
- `JourneyScreen.tsx` renders memory entries and chapter markers from
  `TimelineEntry` (`lib/types.ts`), whose two variants
  (`TimelineMemoryEntry`, `TimelineChapterEntry`) carry only
  `title`/`note`/`milestone_tag`/`photo_ids`/`age_at_moment` and
  `bucket_months`/`label`/`anchor_date` respectively — **no
  `expected_by`/`status`/`on_track` field exists anywhere in the type or
  in the JSX that renders it.**
- Chapter markers (`li.lm-chapter-marker`) render only `entry.label` plus
  two `aria-hidden` decorative flourish glyphs (❧ / ☀) — no comparison
  content, matching the approved `journey/timeline.html` mockup exactly.
- The list is a real `<ol className="lm-river">` (semantic ordered list,
  per UXR-1's accessibility requirement), decorative dot/line elements
  (`lm-river-dot`, `lm-river-line`) are `aria-hidden="true"`.
- Color: `.lm-river-dot`/`.lm-river-line` use `--lm-coral` uniformly for
  every entry — no per-entry color variation exists that could encode a
  status.

**Result: PASS.** Source-confirmed no comparison/norm element exists in
the shipped Journey UI. (Cannot independently re-verify the backend
`timeline.py` payload itself — that's test-agent's parallel schema-lint
job per the task brief — but the frontend has no code path that could
render one even if it existed.)

---

## Scenario 2 — Desktop layout (per this project's prior missing-desktop-views precedent)

**Assertion:** JourneyScreen, AddMemoryForm, DigestPanel have real
desktop treatments (UX_KB §5), not mobile-first CSS that merely doesn't
break at wide viewports.

**Evidence — TodayScreen/DigestPanel:** `app/globals.css` `.lm-today-grid`
gets `grid-template-columns: 1fr 1fr` at `min-width:1024px`, with the hero
card spanning both columns — matches UX_KB §5.4 exactly.
`.lm-content[data-screen="today"]` gets `max-width:980px` at the same
breakpoint. `DigestPanel` renders as a plain `.lm-card` inside this grid,
so it inherits the 2-column treatment automatically — **PASS**, rides
along Today's real desktop system.

**Evidence — JourneyScreen: FAIL (blocking).** `app/globals.css` has
**zero** `@media (min-width: 1024px)` rules for `.lm-river`,
`.lm-river-item`, `.lm-journey-header`, or any journey-scoped selector.
There is also no `.lm-content[data-screen="journey"]` rule, unlike the
`data-screen="today"` case — so at desktop widths the journey column has
no max-width cap at all and just stretches with `.lm-content`'s generic
`max-width:640px` (which is `<1024px`, so it never even reaches the point
where a desktop treatment would visibly differ from mobile). UX_KB §5.5
(the design's own second review-round revision, approved by the human)
specifies alternating left/right cards around a centered 760px-max river
at ≥1024px, mocked up in `screens/desktop/journey-desktop.html` — none of
that is implemented. The shipped Journey screen is mobile-only CSS,
exactly the gap this project already had one incident about.

**Evidence — AddMemoryForm: non-blocking deviation.** The form is a
`.lm-dialog-backdrop`/`.lm-dialog` centered modal (`max-width:440` via
inline override) **at every viewport width** — there is no
`@media (min-width: 768px)` rule for it anywhere in `globals.css`. This
matches neither approved mockup precisely: not the mobile bottom-sheet
(`screens/photo-upload.html` — grabber, rounded-top-only corners, sheet
anchored to the bottom edge) nor the desktop modal spec (§5.6 —
640px width, 5-column photo grid at ≥768px). It is, in effect, "desktop
modal at all sizes" rather than "sheet on phone, modal on desktop."
Functionally it stays keyboard/focus-accessible and touch targets inside
it are mostly fine (see Scenario 3), so this is not a hard accessibility
failure, but it is a real, verifiable divergence from both approved
design artifacts and is flagged as such rather than silently accepted.

---

## Scenario 3 — Touch targets / semantic structure on the new screens

**Assertion:** apply the same 44×44px / `<main>`+heading-landmark
standard that caught Increment-1 findings 5–6, directly to the new
components (not assumed to generalize).

**Evidence — landmarks:** `page.tsx` wraps the whole shell in the
existing `<main className="lm-content">`; `JourneyScreen.tsx` adds its own
`<h1 className="lm-visually-hidden">{profile.display_name}'s
journey</h1>`, matching the pattern already fixed for Today/Chat in
Increment 1. **PASS.**

**Evidence — touch targets, JourneyScreen:** "+ Add a moment"
(`.lm-btn.lm-btn-primary`) and each memory's "Delete"
(`.lm-btn.lm-btn-quiet`) both resolve through `.lm-btn`'s `min-height:44px`
/ `.lm-btn-quiet`'s explicit `min-height:44px; min-width:44px` rules.
**PASS.**

**Evidence — touch targets, AddMemoryForm: two findings.**
1. **Blocking:** the title (`#lm-memory-title`), note (`#lm-memory-note`),
   and date (`#lm-memory-date`) `<input>` elements are rendered with **no
   `className` at all** (`AddMemoryForm.tsx` lines 133–178). `globals.css`
   only styles inputs via the scoped selectors `.lm-field input[type=...]`
   (onboarding) and `.lm-composer input` (chat) — there is no bare
   `input[type=text]`/`input[type=date]` rule and no `.lm-dialog input`
   rule that would catch these. That means these three fields — the core
   fields of the "loggable in ≤3 taps" retention-engine flow (UXR-7) —
   render with raw browser-default sizing, which does not meet the 44px
   floor on most browsers' default text-input chrome, and visibly
   diverges from the approved `photo-upload.html` mockup's specified input
   styling (14px radius, 12–14px padding, 15–16px font, 1.5px border).
   This is a straightforward, source-confirmed gap, not a maybe.
2. **Non-blocking:** the staged-photo "remove" control
   (`.lm-ptile-remove`) is 22×22px (`width:22px; height:22px` in
   `globals.css`) with no minimum-hit-area wrapper — unlike `.lm-btn-quiet`,
   which got exactly this fix in Increment 1's finding 5. The fix did not
   generalize to this new Increment-2 control, confirming the task's own
   caution not to assume it would.

**Evidence — DigestPanel:** no interactive controls in this component (it
is read-only content), so no touch-target surface to check. Heading
nesting is `<h1 hidden>` (Today) → `<h3>This week</h3>` (Digest) with no
intervening `<h2>` — consistent with how the other Today cards already do
it (`<h3>` per activity card), so not a new regression, just noted.

**Result: 1 blocking + 1 non-blocking finding**, distinct from and not
covered by Increment 1's fixes.

---

## Scenario 4 — Image alt text (UXR-6, "images require alt")

**Evidence:** `JourneyScreen.tsx` line ~97–101 renders each memory's real
uploaded photo(s) with `alt=""` — i.e. marked purely decorative — even
though these are the actual content photos attached to a named memory
("First real smile", "Avocado everywhere," etc. in the mockup's fixture
language). UXR-6 explicitly requires "images require alt (parent-entered
or title fallback)"; the entry's own `title` field is available in scope
at that point and is not used. `AddMemoryForm.tsx`'s staged-preview
thumbnails (`alt=""`) are less clear-cut (arguably decorative composing
previews with an adjacent labeled remove button), so only the
JourneyScreen instance is scored as a violation.

**Result: FAIL (blocking)** — real photos in the shipped journey render
with no accessible name.

---

## Scenario 5 — Photo-personalization contract (UX_KB §6, UXR-13)

**Assertion:** shipped photo upload + theme application visually matches
the §6.3 clamped-band/contrast-fallback contract.

**Evidence, backend (matches spec well):** `photo_theme.py`'s
`extract_accent()` implements the §6.3 contract closely and correctly —
median-cut quantize, skin-tone/near-gray filtering, the three clamped HSL
bands (`mid`/`deep`/`tint` with the exact saturation/lightness ranges
UX_KB §6.3.2 specifies), the ±20°/+40° hue-exclusion rotation around
`--lm-danger`'s hue, and a real automated WCAG contrast pre-check
(`_passes_contrast`, checking white-on-scrimmed-deep and ink-on-tint,
both against 4.5:1) with `None`-on-failure fallback. `photos.py`'s
`PhotoStore.create()` calls this on every upload and persists
`photo_accent_mid/deep/tint` to the `profiles` table (`db.py` schema);
delete resets all three columns to `NULL`. This part of the contract is
well-built and structurally isolated from the LLM as required.

**Evidence, the break — blocking:** `routes/profiles.py`'s `Profile`
response model (`app/profiles.py`) and its `_row_to_profile()` mapper
**never read or expose `photo_accent_mid/deep/tint`** — those three
columns are written by `PhotoStore.create()`/`delete()` but no route
anywhere in the backend returns them. `lib/types.ts`'s `Profile` interface
correspondingly has no accent fields, and grepping the entire
`dev/frontend` component set for `--lm-photo` or a `photo_accent` field
turns up nothing: `.lm-journey-header`'s gradient
(`var(--lm-journey-accent, var(--lm-peach))`) is never set from any
JS/inline style anywhere, so it always falls through to the default
`--lm-peach`. There is no accent border on cards, no background wash, and
`ProfileSwitcher.tsx` still renders only the three fixed identity hues
(`IDENTITY_HUES`, `peach/sky/moss`) with no photo-theme chip, no avatar
photo thumbnail, and no per-child accent preview — none of §6.1's
"personalized" surfaces or §6.5's multi-child switcher preview exist in
the shipped UI.

**Result: FAIL (blocking).** This is not a contrast bug to spot-check —
the entire approved rev-4 photo-personalization feature is invisible in
the product. The backend computes and stores exactly what the contract
specifies, but nothing carries it to the browser, so UXR-13 cannot even
be exercised end-to-end: there is no rendering path to test contrast
against for an uploaded photo, adversarial or otherwise.

---

## Summary of findings

| # | Severity | Area | Finding |
|---|---|---|---|
| B1 | **Blocking** | Photo personalization (§6, UXR-13) | Backend computes/stores `photo_accent_*` correctly; no route exposes it; frontend has zero code consuming it. Feature is entirely unshipped visually. |
| B2 | **Blocking** | Desktop layout (§5.5) | JourneyScreen has no desktop CSS at all — no alternating river, no max-width cap, repeats this project's prior missing-desktop-views incident. |
| B3 | **Blocking** | Touch targets / UXR-6, UXR-7 | AddMemoryForm's title/note/date inputs have no `className` and get zero design-system styling, including the 44px floor, in the core "≤3 taps" logging flow. |
| B4 | **Blocking** | UXR-6 (alt text) | JourneyScreen renders real memory photos with `alt=""` instead of the available `title` fallback. |
| N1 | Non-blocking | Touch targets | `.lm-ptile-remove` (staged-photo remove) is 22×22px, no hit-area fix — the Increment-1 finding-5 fix didn't generalize to this new control. |
| N2 | Non-blocking | Desktop layout (§5.6) | AddMemoryForm is a centered modal at every width — matches neither the mobile bottom-sheet nor the desktop-modal mockup exactly. |
| N3 | Non-blocking | Heading hierarchy | DigestPanel's `<h3>` follows Today's hidden `<h1>` with no `<h2>`, consistent with sibling cards, just noted. |

**Scenario 1 (R1 UI compliance): PASS.**
**Scenario 2 (desktop): PARTIAL — Today/Digest pass, Journey fails, AddMemoryForm deviates (non-blocking).**
**Scenario 3 (touch targets/semantics): PARTIAL — landmarks/most buttons pass, memory-form text inputs fail.**
**Scenario 4 (alt text): FAIL.**
**Scenario 5 (photo-personalization contract): FAIL.**

## Gate verdict

**BLOCK.** Four blocking findings (B1–B4) under this project's blocking-only
Test Policy (no advisory suites recorded). B1 in particular means an
entire approved, human-reviewed design revision (§6, the photo
personalization pass) shipped with no visible effect — this needs a
code-agent fix (expose the three accent columns on `Profile`/`GET
/profiles*`, then wire `--lm-photo-mid/-deep/-tint` into
`JourneyScreen`/`TodayScreen`/`ProfileSwitcher` per UX_KB §6.1) before this
can pass, not a documentation note. B2–B4 are each independently
straightforward, source-confirmed fixes (add the journey desktop media
query; add a `className` to the three memory-form inputs; use
`entry.title` as alt text). Recommend returning to code-agent with this
evidence before proceeding to Review/Deploy for Increment 2.

**Not visually/runtime verified this pass** (no browser/screenshot tool
available): actual computed contrast ratios, real focus-trap behavior in
the `role="dialog"` overlays, and on-device tap-target hit-testing.
Recommend a follow-up rendered pass (`npm run dev` + a browser or
Playwright) once B1–B4 are fixed, both to confirm the fixes visually and
to catch anything a source-only read cannot (matches the same caveat this
project's Increment-1 UX suite carried).
