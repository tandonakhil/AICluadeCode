# UX retest under real data density — full app (ui-ux-designer)

Date: 2026-07-11 (evening pass, post-synthetic-data). Trigger: explicit human
request — "retest the entire app after synthetic data has been added. Journey
page is not looking clean, 6 months, 9 months text is overlapping with lines."

Context: first UX pass with dense real data — tester profile (Emma, 11 months),
15 memories spanning 2–11 months, every memory carrying a real 1024x1024
watercolor image, plus a profile-level portrait powering an olive-toned photo
theme (`photo_accent_mid/deep/tint` set on the profile). All prior UX suite
passes were source-level against sparse or no data.

Method: source-level review of `dev/frontend/` (JSX + `globals.css`) and
`dev/backend/app/photo_theme.py`, cross-checked against the approved mockups
(`design-review/journey/timeline.html`, `design-review/screens/desktop/
journey-desktop.html`) and the binding Decisions Log (responsive web app;
UXR-1 no norm axis; UXR-6 44px floor; UXR-9 one red surface; UXR-11 product
cards; UX_KB §6.3 contrast contract). **No browser tool available in this
environment** — every geometric/contrast conclusion below is derived from the
code and flagged where it needs visual confirmation.

Verdict: **BLOCK — 2 blocking findings (UXD-1, UXD-2), 6 non-blocking.**
Everything else passes at density. Exact fix specs included per finding.

---

## UXD-1 (BLOCKING) — Journey desktop: chapter labels ("6 months", "9 months") overlap the spine; stray connector segments; dots float off the spine

**This is the human-reported defect. Root cause diagnosed, three linked
mechanisms, all from the same divergence: `JourneyScreen.tsx` kept the
*mobile* DOM (per-item flex dot-columns with per-item `.lm-river-line`
segments) when the desktop alternating layout was added, while the approved
desktop mockup (`journey-desktop.html`) uses one continuous centered
`::before` spine + absolutely-positioned dots with a cream masking border and
`li.chapter::after { display:none }`.**

Mechanisms, in order of visibility at 15-item density:

1. **Label-on-spine overlap (the reported one).** At >=1024px,
   `globals.css:272` draws `.lm-river::before` — a 4px coral (35% opacity)
   spine at `left: 50%`, spanning `top: 0; bottom: 0` of the whole `<ol>`,
   i.e. straight through every `.lm-chapter-marker`, which is `width: 100%;
   text-align: center` — its text is horizontally centered at exactly 50%,
   directly on top of the spine. Because the `::before` is a *positioned*
   box and the marker text is in normal flow, the spine also *paints above*
   the text per CSS stacking order — the line literally crosses through
   "6 months" / "9 months". The mockup had the same latent geometry but was
   only ever reviewed with 2 chapter markers and 5 cards; at 4 markers + 15
   photo cards the collisions are constant.
2. **Stray line segments beside every card.** Each memory `<li>` still
   renders its mobile `.lm-river-dot-col` with a `.lm-river-line` segment
   (`JourneyScreen.tsx:101-104`, gated only by `i < entries.length - 1`,
   never by breakpoint). On desktop these segments sit ~28-36px off-center
   next to each card — 14 short vertical dashes running parallel to the real
   spine. This is the "lines" clutter compounding the label overlap.
3. **Dots don't sit on the spine.** The dot-col is inside the
   `calc(50% - 28px)`-wide item (row-reversed on the left side), so dot
   centers land ~35px off the spine, versus the mockup where dots straddle
   the spine (`li.side-l::after { right: -40px }` with a 3px cream border).

### Fix spec (exact, for a direct patch)

**JSX — `dev/frontend/components/JourneyScreen.tsx`:**

1. Delete the connector segment: remove line 103
   (`{i < entries.length - 1 && <span className="lm-river-line" .../>}`)
   — the continuous CSS spine below replaces it at both breakpoints. The
   `.lm-river-dot-col` wrapper and `.lm-river-dot` stay.
2. Wrap the chapter-marker content so it can mask the spine:
   ```tsx
   <li className="lm-chapter-marker" key={`chapter-${entry.bucket_months}`}>
     <span className="lm-chapter-label">
       <span className="lm-flourish" aria-hidden="true">❧</span>{" "}
       {entry.label}{" "}
       <span className="lm-flourish" aria-hidden="true">☀</span>
     </span>
   </li>
   ```

**CSS — `dev/frontend/app/globals.css`:**

Base rules (mobile and up) — replaces the per-item segment with the
mockup's continuous-spine + masked-dot pattern:
```css
.lm-river {
  position: relative;   /* add */
  /* existing list-style/margin/padding unchanged */
}
.lm-river::before {                 /* NEW: continuous mobile spine */
  content: "";
  position: absolute;
  left: 13px;      /* 4px list padding + half the 21px dot box - half the 3px line */
  top: 26px;       /* first dot's center (8px pad + 14px dot margin + ~4px) */
  bottom: 60px;
  width: 3px;
  border-radius: 3px;
  background: var(--lm-coral);
  opacity: 0.35;
}
.lm-river-dot {
  /* existing size/color/margin unchanged, add: */
  border: 3px solid var(--lm-cream);  /* masks the spine where it crosses, per mockup */
  box-sizing: content-box;            /* keep the 15px coral fill (global * is border-box) */
}
/* DELETE the whole .lm-river-line rule (lines 608-615). */
.lm-chapter-label {                   /* NEW */
  position: relative;
  z-index: 1;                 /* lifts above the positioned ::before spine */
  display: inline-block;
  background: var(--lm-cream); /* cream pill cleanly breaks the spine at each label */
  border-radius: 999px;
  padding: 2px 14px;
}
```

Desktop block (inside the existing `@media (min-width: 1024px)`):
```css
.lm-river::before {
  left: 50%;
  margin-left: -2px;
  width: 4px;
  top: 24px;
  bottom: 80px;
}
.lm-river-item {
  position: relative;   /* add — anchors the absolute dot-col */
  /* existing width: calc(50% - 28px); margin: 0 0 26px; unchanged */
}
.lm-river-dot-col {
  position: absolute;
  top: 2px;             /* dot's 14px margin-top puts its visual top ~16px, matching mockup */
}
.lm-river-side-l .lm-river-dot-col { right: -38.5px; }
.lm-river-side-r .lm-river-dot-col { left: -38.5px; }
/* Offset math: spine center = card inner edge + 28px gutter; dot box =
   15px + 2*3px border = 21px; offset = -(28 + 21/2) = -38.5px. Recompute
   if the 28px gutter ever changes. */
/* DELETE: .lm-river-item.lm-river-side-l { flex-direction: row-reverse; }
   — the dot-col is out of flex flow now; row-reverse is dead. Keep the
   margin-right/left: auto side rules. */
```

The `top`/`bottom` endpoint values (26/60 mobile, 24/80 desktop) are
computed, not rendered — **needs visual confirmation in a browser** and may
want ±4px tuning so the spine starts at the first dot and ends before the
last card's Delete row.

Result after patch: one continuous spine at each breakpoint, dots sitting on
it with cream masking rings, chapter labels in cream pills that cleanly break
the spine (no text-over-line), zero stray segments. UXR-1 unaffected — purely
spatial, still no norm axis.

---

## UXD-2 (BLOCKING) — Journey header: `--lm-photo-mid` is a text-bearing background the server contrast pre-check never covers; olive theme likely renders sub-AA text

The question this retest was asked to answer for Today ("did the
contrast-fallback contract hold?") is **yes for the hero card, no for the
Journey header**:

- `photo_theme.py::_passes_contrast` checks exactly two pairs: white over
  scrimmed `deep` (5% scrim worst case) and ink `#3D3833` over `tint`.
  Per UX_KB §6.3.2, `tint` (L 0.90–0.94) is the band "ink text may sit
  directly on."
- `.lm-hero-card` (Today) composites the fixed 5%→45% black scrim over
  `deep`→`mid` with white text — the checked worst case (white on deep @5%)
  is the real worst case, and the mid end carries ≥~25–45% scrim. **Contract
  held.** (Visual confirm of the olive gradient still recommended.)
- `.lm-journey-header` (globals.css:552) instead paints
  `linear-gradient(180deg, var(--lm-photo-mid, var(--lm-peach)), var(--lm-cream))`
  with **no scrim**, and puts ink `<h2>` (26px) and 14px bold
  `--lm-terracotta-deep` `.lm-elapsed` text on the mid-toned top region. The
  mid band is clamped to L 0.45–0.60 / S 0.30–0.55 — much darker than the
  default peach (#F0A574) these text tokens were chosen against. Estimated
  from the band midpoint: ink-on-olive-mid ≈ 3:1 (fails AA 4.5:1 for the
  14px line; borderline for the 26px h2), terracotta-deep-on-mid ≈ 2:1
  (clear fail). No pre-check covers either pair, so the pipeline happily
  returns tokens that break this surface — the fallback contract has a hole
  for any photo theme, not just olive; density/real-photos made it visible.

### Fix spec

One-token CSS change, honoring §6.3.2's own rule (ink sits on **tint**):

```css
.lm-journey-header {
  background: linear-gradient(
    180deg,
    var(--lm-photo-tint, var(--lm-peach)),   /* was --lm-photo-mid */
    var(--lm-cream)
  );
  ...
}
```

`tint` (L 0.90–0.94) is already pre-checked against ink at 4.5:1;
terracotta-deep on tint computes to ~7:1. No backend change needed. The
header becomes a pale wash of the photo hue — same lightness register as the
default peach→cream, so the personalized and default states finally sit in
the same visual family. Also update the stale CSS comment (it cites
`--lm-photo-mid`). **Needs visual confirmation** that the olive tint still
reads as "personalized" rather than washed out; if the human wants more
color, the alternative is keeping mid + adding a fixed light scrim, but that
requires a matching backend pre-check addition — the tint swap is the
minimal, contract-clean fix.

Cosmetic note found while here: `.lm-journey-header h1` rule is dead CSS —
the JSX renders an inline-styled `<h2>`. Fold the inline styles into an
`.lm-journey-header h2` rule or delete the dead rule.

---

## Non-blocking findings

**UXD-3 — Journey mobile: spine reads as dashes at density.** The per-item
`.lm-river-line` segments leave an 18px gap between every pair of items and
~70px gaps around each chapter marker; with 15 items + 4 markers the mobile
"river" reads as 14 disconnected dashes. The approved mobile mockup
(`timeline.html`) uses a continuous spine + cream-bordered dots. **Fixed by
the same UXD-1 patch** (the base-rule half). Mobile marker labels do not
overlap the spine (it sits at left ~13px, labels centered), so this is
polish, not the reported defect.

**UXD-4 — Moment photos: 64px thumbnails undersell real images; 15 full-res
eager loads.** `.lm-moment-photos img` renders every 1024x1024 watercolor as
a 64x64 thumbnail (`object-fit: cover` — no layout blowout, confirmed), but
the approved mockup gives the photo a 120px full-width band at the top of the
card. With real imagery this is the difference between a storybook and a
contact sheet. Also all 15 images (each ~full-res) load eagerly on tab open.
Fix spec: (a) add `loading="lazy"` to the `<img>` in `JourneyScreen.tsx`
(one attribute, do now); (b) proposed for human review, not unilateral: first
photo of each memory renders as a full-width banner (`width:100%; height:120px;
object-fit:cover; border-radius:12px 12px 0 0` with the card's padding pulled
off the image), additional photos stay 64px thumbs below. (b) needs a
design-review preview before implementation. A backend-resized thumbnail
variant is a further perf option — Architecture's call, flagged only.

**UXD-5 — Chat + photo-upload errors still show raw transport text.**
`lib/api.ts::sendChatMessage` (line 146) and `uploadPhoto` (line 200) throw
`` `${response.status} ${response.statusText}: ${body}` `` — the exact
UX_KB §1.2 voice violation closed as Increment-3 Finding 2b for `request()`,
explicitly left out of that fix pass's scope at the time. `ChatScreen.tsx`
renders it verbatim in its error line; `AddMemoryForm`'s upload failure path
likewise. Fix: `throw new ApiError(response.status, parseErrorMessage(body))`
at both sites (parseErrorMessage already exists in the same file).

**UXD-6 — Shell load error shows raw browser message.** `app/page.tsx:83`
renders `loadError` verbatim; a network failure sets it to the browser's
"Failed to fetch". Fix: in both catch blocks, use the existing calm fallback
("We couldn't reach little-milestones — check that the server is running and
try again.") unless the error is an `ApiError` (whose message is already
parsed/calm).

**UXD-7 — Identity-dot inconsistency: sidebar/mobile header ignore the photo
accent.** `page.tsx` colors the selected child's dot from `IDENTITY_HUES`
only (lines 154, 210), while `ProfileSwitcher.tsx` uses
`photo_accent_mid ?? IDENTITY_HUES[i]` per UX_KB §6.5 — Emma's dot is olive
in the switcher and peach in the sidebar simultaneously. Fix: both `page.tsx`
sites become `selected.photo_accent_mid ?? IDENTITY_HUES[selectedIndex %
IDENTITY_HUES.length]` (ring optional; the switcher keeps its
`photo_accent_deep` ring).

**UXD-8 — Settings: digest checkbox under the UXR-6 floor + missing error
handling on toggle.** The native checkbox is ~13px; the clickable label text
enlarges the target somewhat but the row has no 44px minimum
(`SettingsScreen.tsx:109`). Fix: `style={{ minHeight: 44 }}` on the label
(or a `.lm-toggle-row` class). Separately, `handleToggleDigest` has no
`catch` — a failed PATCH is an unhandled rejection and the toggle silently
stays stale; add a catch with the standard terracotta-deep inline error.
Flagged for code-agent.

---

## Full-density screen-by-screen results (PASS items)

| Screen | Result | Notes |
|---|---|---|
| Today — hero card (olive theme) | PASS (source) | §6.3 scrim contract genuinely held: pre-check covers white-on-deep@5% worst case; mid end carries >=~25–45% scrim. Visual confirm of the olive gradient recommended. |
| Today — digest panel | PASS | Fails quietly per design; content density fine inside one grid cell; supervision notes styled correctly. |
| Today — products panel | PASS | UXR-11 held at density: identical card anatomy to activity cards, no price/brand/urgency grammar, "we don't sell anything" line present. |
| Today — desktop 2-col grid | PASS (source) | Hero spans both columns; panels each take a cell. Needs visual confirm that panel heights don't create ragged rows at this content volume. |
| Journey — mobile, 15 items | BLOCK via UXD-1/UXD-3 | Alternation is mobile-no-op as designed; photos don't blow out sizing (fixed 64px + object-fit). |
| Journey — desktop, 15 items | BLOCK via UXD-1/UXD-2 | Alternation logic itself is sound (memories alternate, markers stay centered full-width, zigzag stacking matches mockup). |
| Chat | PASS w/ UXD-5 | Age strip, corrected-age explainer, pediatrician-note split, UXR-9 terracotta errors, 44px targets all intact. |
| Auth (login/signup/join) | PASS | Calm copy per §1.7 Flow 3b; parseErrorMessage in effect; email/password inputs now carry the 44px rule. Known, already-recorded gap stands: no visual mockup ever produced for this screen (Decisions Log, Increment-3 Finding A) — still on my backlog, not re-flagged as new. |
| Settings | PASS w/ UXD-8 | Plain-words role labels, owner-only invite rendering, no-password-reset gap as honest copy, deliberate 680px desktop cap all confirmed. Same mockup-gap note as Auth. |
| Onboarding — new ready-screen CTA | PASS | "Start {name}'s journey" — full-width `.lm-btn-primary` pill matches the established CTA language and the §1.10 copy register; closes the previously-found dead-end. Second-child flow (`onDone` -> shell) reads correct. |
| Profile switcher | PASS | §6.5 held: olive `photo_accent_mid` dot fill + `photo_accent_deep` ring + informational "photo theme"/"default theme" chip, never a nag. Dual-age `age_summary` server string in use. See UXD-7 for the sidebar inconsistency. |
| Recent code changes (loadError order, `devIndicators: false`, parseErrorMessage) | PASS | loadError-before-loading ordering correct (see UXD-6 for copy); devIndicators removal has no design impact; parseErrorMessage correct where wired (see UXD-5 for the two unwired sites). |

## Items requiring visual/browser confirmation (no browser tool here)

1. UXD-1 patch endpoint values (`top`/`bottom` of both spines) — ±4px tuning.
2. Olive hero-card gradient and olive tint Journey header — do they *look*
   right, beyond passing contrast math.
3. Desktop Journey rhythm at 15 items post-patch (card height variance with
   photos may want a max-height on `.lm-moment-photos`).
4. Today desktop row raggedness (grid cell height variance).
5. UXD-4(b) photo-banner proposal — must go through a design-review preview
   and human approval before implementation.

## Verdict

**BLOCK.** UXD-1 (the human-reported Journey overlap — full root cause and
patch spec above) and UXD-2 (Journey-header contrast contract hole, exposed
by the first real photo theme) must be fixed by code-agent before this
retest can pass; UXD-3 rides along in the same patch. UXD-4a/5/6/7/8 are
non-blocking but specced and cheap. Re-verification after the fix pass
should include an actual browser look at the five items above — this suite's
geometric conclusions are source-derived.

[ui-ux-designer]
