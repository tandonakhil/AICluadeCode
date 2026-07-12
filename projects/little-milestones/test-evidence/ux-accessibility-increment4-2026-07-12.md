# UX/usability + accessibility suite — Increment 4 (F14 avatars, F15 lightbox, F16 gallery)

Date: 2026-07-12. Owner: ui-ux-designer (Test-gate suite owner for UX/usability
+ accessibility). Checking shipped code against my own design spec
(`knowledge/UX_KB.md` §8, §8.1a).

**Method: source-level review only** — no browser/Playwright tool available in
this session. Every finding below is a static read of the shipped TSX/CSS
against the spec text; anything that requires a rendered browser (actual
computed contrast ratios, real focus-trap behavior, real backdrop-click
geometry) is labeled "unverifiable — source-level only" rather than asserted
as visually confirmed, per this role's standing discipline in prior passes
(see `ux-retest-synthetic-data-2026-07-11.md`).

Files checked: `dev/frontend/components/Avatar.tsx`, `Lightbox.tsx`,
`SettingsScreen.tsx`, `JourneyScreen.tsx`, `TodayScreen.tsx`,
`ProfileSwitcher.tsx`, `app/page.tsx`, `app/globals.css`, `lib/api.ts`,
`lib/types.ts`.

**Verdict: PASS — 0 blocking findings, 2 non-blocking.**

---

## Scenario 1 — F14 avatar sizes/rings, four surfaces

| Surface | Size spec | Ring spec | Found in code | Result |
|---|---|---|---|---|
| Switcher (`ProfileSwitcher.tsx`) | 32px | `photo_accent_deep` ring | `<Avatar size={32} ... photoStyle={{boxShadow: p.photo_accent_deep ? \`0 0 0 2px ${p.photo_accent_deep}\` : undefined}}}>` | PASS |
| Today header (`TodayScreen.tsx`) | 44px | fixed translucent white `rgba(255,255,255,.85)` | `<Avatar size={44} ... photoStyle={{boxShadow: "0 0 0 3px rgba(255,255,255,.85)"}}}>` | PASS |
| Journey header (`JourneyScreen.tsx`) | 56px | cream ring (`3px solid var(--lm-cream)`) + drop shadow | `<Avatar size={56} ... photoStyle={{border: "3px solid var(--lm-cream)", boxShadow: "0 2px 8px rgba(61,56,51,.25)"}}}>` | PASS |
| Settings (`SettingsScreen.tsx`) | 72px | none specified (§8.1a doesn't require a ring here) | `<Avatar profile={profile} size={72} fallbackColor={identityColor} />` — no ring, matching spec's silence | PASS |

All four sizes present and correctly differentiated, matching §8.1/§8.1a
literally (values copied verbatim from the KB into this table above).

**`onError` fallback:** `Avatar.tsx` wires `onError={() => setFailed(true)}`
on its single shared `<img>`, and every one of the four call sites above goes
through this shared component — so the fallback is wired on all four "real"
avatar instances. **Non-blocking gap (finding UXD-N1):** `SettingsScreen.tsx`'s
optimistic local preview (`<img className="lm-avatar" src={previewUrl} ...>`,
lines 111–117) is a raw `<img>`, not routed through `Avatar.tsx`, and has no
`onError` handler. Low real-world risk (the src is a same-session
`URL.createObjectURL(file)` blob the browser just created, not a network
fetch that can 401/404), and it's only ever on-screen for the duration of the
upload request, but it is technically an avatar-shaped `<img>` without the
onError-to-dot contract the spec says should hold "on every instance."
Non-blocking — recommend a one-line `onError` fallback to `Avatar`'s render
(or just clearing `previewUrl` on error, which the existing `finally` block
already does on the *next* tick when the upload itself fails).

## Scenario 2 — F14 Settings upload flow vs. §8.1a

| Requirement | Found | Result |
|---|---|---|
| Upload-on-select, no Save step | `onChange={(e) => handlePhotoSelected(e.target.files)}` calls `uploadPhoto` immediately, no separate submit control | PASS |
| "Uploading…" disabled state | `disabled={uploading}` + `{uploading ? "Uploading…" : ...}` | PASS |
| Optimistic local preview via `URL.createObjectURL` | `const localPreview = URL.createObjectURL(file); setPreviewUrl(localPreview);` set before the request fires | PASS |
| Revert-on-failure | `finally` block unconditionally does `setPreviewUrl(null); URL.revokeObjectURL(localPreview);` — on failure this drops back to `<Avatar>` rendering the *unchanged* `profile` (no `onProfileUpdated` call happened), i.e. last-known-good state | PASS |
| `role="alert"` errors via `ApiError`/`parseErrorMessage`, no raw HTTP text | `uploadPhoto()` (`lib/api.ts`) throws `ApiError(status, parseErrorMessage(body))` on non-2xx; `SettingsScreen` catches and does `err instanceof Error ? err.message : ...` into `<p role="alert" style={{color:"var(--lm-terracotta-deep)"}}>{photoError}</p>` — no transport string ever surfaces | PASS |
| Privacy line + lock glyph under the control | `.lm-privacy-note` div directly below the error paragraph, verbatim copy "Photos stay private to your family. Never public, never used for AI, never scanned for faces." + 🔒 | PASS |
| Subtitle "For {profile.display_name}" | `<p style={{color:"var(--lm-ink-soft)", marginTop:-4}}>For {profile.display_name}</p>` immediately under the "Profile photo" heading | PASS |

All seven sub-requirements pass. Error color used is `--lm-terracotta-deep`
(the pre-existing calm error color already used by `inviteError`/
`digestError` on the same screen), **not** `--lm-danger` — correctly avoids
introducing a second red surface (UXR-9, see Scenario 5).

## Scenario 3 — F15 lightbox

| Requirement | Found | Result |
|---|---|---|
| 44×44px close button | `.lm-lightbox-close { width:44px; height:44px; ... }` | PASS |
| `role="dialog" aria-modal="true" aria-label="{title} photo"` | On `.lm-lightbox` div: `role="dialog" aria-modal="true" aria-label={\`${current.title || "Photo"} photo\`}` | PASS |
| Focus-to-close-button on open | `useEffect(() => { closeRef.current?.focus(); }, [])` | PASS (unverifiable — source-level only: actual focus-move behavior in a real browser not confirmed) |
| Focus-return-to-trigger on close | `JourneyScreen.tsx`'s `closeLightbox()`: `lastTriggerRef.current?.focus()` after `setLightbox(null)`, with `lastTriggerRef` set in `openLightbox(..., triggerEl)` from every call site (`e.currentTarget`) | PASS (unverifiable — source-level only) |
| Escape dismiss | `handleKeyDown`: `if (e.key === "Escape") { onClose(); return; }` | PASS |
| Backdrop-click dismiss, image/caption click does not | `onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}` on `.lm-lightbox-backdrop` only — clicks on descendants (image, caption, buttons) have `e.target !== e.currentTarget` and don't bubble-trigger dismissal | PASS |
| 44×44px prev/next only when >1 photo | Shared `.lm-lightbox-close, .lm-lightbox-nav { width:44px; height:44px; }` rule; prev/next buttons conditionally rendered only `{hasMultiple && (...)}` | PASS |
| Dot indicator | `.lm-lightbox-dots` rendered only when `hasMultiple`, one `.lm-lightbox-dot` per photo, `-active` modifier on current index | PASS |
| Max-size caps 70vh mobile / 900px×76vh desktop | `.lm-lightbox-img { max-height: 70vh; }` base rule; `@media (min-width:1024px) { max-width:900px; max-height:76vh; }` | PASS |

Tab-trap behavior (`Tab`/`Shift+Tab` cycling among close/prev/next) is
implemented in the same `handleKeyDown` effect and reads correctly against
the spec, but real focus-trap correctness (e.g. whether `document
.activeElement` checks behave as expected across browsers) is flagged
**unverifiable — source-level only**, consistent with this suite's standing
practice of not asserting real DOM/focus behavior without a browser tool.

## Scenario 4 — F16 gallery

| Requirement | Found | Result |
|---|---|---|
| `.lm-view-toggle` placement | Rendered in `JourneyScreen.tsx` immediately after the "+ Add a moment" button (position unchanged) and immediately before the `entries === null` / empty-state / timeline / gallery content block | PASS |
| 3-col mobile / 5-col desktop grid, matching `AddMemoryForm`/`.lm-photogrid` precedent | `.lm-gallery-grid { grid-template-columns: repeat(3, 1fr); }` base, `@media (min-width:1024px) { repeat(5, 1fr) }` — same 3→5 step as `.lm-photogrid`, intentionally re-keyed to Journey's own 1024px breakpoint instead of `.lm-photogrid`'s 768px, exactly as documented in UX_KB §8.3 ("here stepped at Journey's own 1024px breakpoint for consistency") — not a silent deviation | PASS |
| Empty-state copy | `<p className="lm-card">No photos yet — add a moment with a photo to see it here.</p>` — verbatim match to §8.3 | PASS |
| Gallery tiles open the same `<Lightbox>` seeded with the full profile-wide photo list | `allProfilePhotos` is built once via `memoryEntries.flatMap(...)` (every memory's `photo_ids`, chronological order) and passed to every gallery tile's `openLightbox(allProfilePhotos, i, ...)` — not scoped to one memory, matching the "two seed-list scopes" requirement (timeline triggers use `memoryPhotos`, gallery tiles use `allProfilePhotos`) | PASS |
| `aria-label` per tile = parent memory's title | `aria-label={photo.title || "Photo"}` where `photo.title` comes from the owning `entry.title` at flatMap time | PASS |

Accessibility: gallery is a plain `<ul>` of `<button>`-wrapped `<img alt="">`
tiles — `alt=""` on the image is intentional/correct here since the parent
`<button>` already carries the accessible name via `aria-label`; this avoids
a duplicate screen-reader announcement rather than violating UXR-6's
"images require alt" rule (the accessible name still exists, just on the
interactive wrapper rather than the image itself, and the button is what a
screen-reader user actually activates).

## Scenario 5 — UXR-1 / UXR-9 sweep

- **UXR-1 (no expected-vs-actual framing):** none of the three features
  introduce any norm axis, second data series, "typical" language, or
  status/comparison semantics. Avatars are pure identity display; the
  lightbox is a resolution/viewing affordance over the same photos already
  on the card; the gallery is "bare photos only — no date/age labels" per
  spec, and the shipped code matches (gallery `<img>` renders no age/date
  text, confirmed by reading `JourneyScreen.tsx`'s gallery branch). PASS.
- **UXR-9 (one red surface):** searched all Increment-4 code for
  `--lm-danger` — not referenced anywhere in `Avatar.tsx`, `Lightbox.tsx`,
  the new Settings "Profile photo" card, or the gallery/toggle CSS. The new
  photo-upload error path (`SettingsScreen.tsx`'s `photoError`) uses
  `--lm-terracotta-deep`, the same pre-existing calm error color already
  used for `inviteError`/`digestError` on the same screen — no second red
  surface introduced. PASS.

---

## Non-blocking findings summary

1. **UXD-N1** — `SettingsScreen.tsx`'s optimistic preview `<img>`
   (`previewUrl`, a same-session blob URL) has no `onError` handler, unlike
   every other avatar instance which routes through `Avatar.tsx`'s shared
   `onError`-to-dot fallback. Low risk (blob URLs from a file the browser
   just read essentially never fail to load), but worth a one-line fix for
   contract consistency.
2. **UXD-N2 (observation, not a spec violation)** — the persistent
   switcher-trigger buttons in `app/page.tsx` (the sidebar's child-name
   button and the mobile header's child-name button) still render a plain
   `.lm-identity-dot` span, never the new `<Avatar>`/photo treatment, even
   when the selected child has an uploaded profile photo. §8.1 scoped F14
   explicitly to three surfaces (switcher **sheet** rows, Today header,
   Journey header) plus §8.1a's Settings addition — the always-visible
   shell trigger button was never in scope, so this is not a spec
   violation, just flagged as a natural next-increment consistency
   candidate (a parent who's uploaded a photo would reasonably expect to
   see it in the one identity element that's on-screen at all times).

## Coverage note

This pass is source-level only (no browser/Playwright tool in this
session). Computed-contrast checks (UXR-6/UXR-13 AA thresholds against the
lightbox's white-on-dark-backdrop text, the gallery grid, and the new
Settings card), real keyboard-navigation/focus-trap behavior, and real
backdrop-click geometry are all asserted from code reading, not visual
confirmation, and are labeled as such above. Full accessibility flow tests
(actually completing the upload → view-in-lightbox → toggle-to-gallery
journey with a screen reader or keyboard-only) were not performed and
should be captured by whichever pass in this pipeline has a browser tool.
This pass does not re-check F1–F13/prior increments — those are covered by
this suite's earlier evidence files (`ux-retest-synthetic-data-2026-07-11
.md` and predecessors).

## Verdict

**PASS.** All checklist items in the task (F14 sizes/rings, F14 upload flow,
F15 lightbox, F16 gallery, UXR-1/UXR-9 sweep) match the design spec in
`knowledge/UX_KB.md` §8/§8.1a. Two non-blocking findings recorded above,
neither of which contradicts an explicit spec requirement or introduces a
red-surface/comparison-framing violation. No blocking findings — this gate
does not need to hold Increment 4 for UX/accessibility reasons.
