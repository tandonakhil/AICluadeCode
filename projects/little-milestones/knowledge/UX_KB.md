never-wholesale-replace guidance.

---

## 7. Revision — 2026-07-12 (fourth review pass): UXD-4(b) photo-banner fix (density retest)

Source: `test-evidence/ux-retest-synthetic-data-2026-07-11.md`, "Non-blocking
findings" UXD-4, lines ~224–236. Human approved the "(b)" half of that
finding for implementation (the "(a)" half — `loading="lazy"` — was a
do-now one-attribute fix already applied separately and isn't re-specified
here).

### 7.1 The finding and the approved fix

At real-data density (15 memories, full-res watercolor-style photos), the
existing `.lm-moment-photos img` rule renders every photo — including the
first/hero photo of a memory — as a uniform 64×64 thumbnail. With real
parent-uploaded imagery (not the placeholder blocks in earlier mockups)
this reads as a contact sheet, not a storybook — directly working against
this KB's own "storybook, not chart," "photography is the hero wherever it
exists" language (§1.2, §4). The approved mockup already showed a 120px
full-width photo band at the top of the card (`journey/timeline.html`,
`.photo{height:120px}`); the retest simply flagged that the shipped
component never carried that treatment through to `JourneyScreen.tsx`,
and asked for it as an explicit, reviewable fix rather than folding it in
silently.

**Approved fix:** on the Journey timeline, a memory's **first** photo
renders as a full-width banner (`width:100%; height:120px; object-fit:
cover`, top corners rounded to match the card, bleeding to the card's own
edges by pulling the card's padding off just that element) at the top of
the card. If the memory has additional photos, they render **unchanged**
as the existing 64px thumbnail row (`.lm-moment-photos`) below the banner.
A single-photo memory shows the banner only, no thumbnail row.

### 7.2 What stays exactly as designed (re-verified, not re-litigated)

- UXR-1 (no norm axis) — the card's content model is unchanged; this is
  purely which of two existing image treatments a given photo index gets.
- The coral river spine, dots, chapter markers, age badge, delete
  affordance, and card shadow/radius are untouched.
- `loading="lazy"` (UXD-4a) is preserved on both the banner and the
  thumbnail images.
- Photo privacy posture (§1.6/Flow 2c) is unaffected — same images, same
  access path (`photoUrl`, `crossOrigin="use-credentials"`), just a
  different `<img>` layout treatment for index 0.

### 7.3 Corner radius — resolved, literal 12px confirmed (2026-07-12)

The preview originally proposed `var(--lm-radius-card)` (16px, the card's
own radius token) over the retest note's literal `border-radius:12px 12px
0 0`, reasoning that a smaller radius than the card's own would leave a
~4px sliver of card background visible at each top corner. **Human
reviewed the preview and explicitly confirmed the literal 12px value** —
implemented as specified in the original retest note, sliver accepted
as-is rather than revised further.

### 7.4 Preview mockup produced (design-review artifact required before implementation)

Written to `projects/little-milestones/design-review/journey/`:

| File | Shows |
|---|---|
| `journey/moment-photo-banner.html` | Single-photo memory card (banner only) and two-photo memory card (banner + one-row of thumbnails for photos 2+), each rendered at mobile width and at desktop width (alternating-river layout, matching `screens/desktop/journey-desktop.html`'s treatment) — four card renders total. Uses the real fixed tokens from `dev/frontend/app/globals.css` copied verbatim (not a generic mockup palette). Includes an inline implementation note (exact CSS class, exact JSX structural change) and the §7.3 flagged-deviation box. |

`projects/little-milestones/design-review/index.html` gets a new "Journey
Photo Banner (rev. 5)" nav link and section (green `RETEST` badge to
visually distinguish a retest-driven fix from the earlier proactive
revisions), linking the new preview, with a strategy summary box at the
top. The existing `#journey` section's description was updated with one
sentence pointing to the new section — no existing card, screenshot, or
rationale in that section was removed or rewritten.

### 7.5 DesignSync push (incremental, additive only)

Same project, `172e0c51-e31a-46e7-aedb-bead17b38868`. New plan finalized
covering exactly one new path, `journey/moment-photo-banner.html`. No
existing path (including `journey/timeline.html`, which stays as the
original approved river mockup) was touched, overwritten, or deleted.

### 7.6 Implementation note for code-agent (design spec, not code — code-agent owns the actual edit)

**CSS** (`dev/frontend/app/globals.css`): add one new rule immediately
after `.lm-moment-photos img` —
```
.lm-moment-banner {
  display: block;
  width: calc(100% + 40px);
  height: 120px;
  object-fit: cover;
  border-radius: var(--lm-radius-card) var(--lm-radius-card) 0 0;
  margin: -20px -20px 14px;
}
```
(the `-20px`/`40px` figures are `.lm-card`'s own `padding: 20px` pulled
off; if that padding value ever changes, this rule's margin/width must
change with it). `.lm-moment-photos` / `.lm-moment-photos img` are
**unchanged** — reused as-is for photos 2+.

**JSX** (`dev/frontend/components/JourneyScreen.tsx`): inside the existing
`entry.photo_ids.length > 0 && (...)` block (currently a single
`.lm-moment-photos` div mapping the full `photo_ids` array), split into
two pieces:
1. An `<img className="lm-moment-banner">` for `entry.photo_ids[0]` only,
   placed as the **first child** of the `.lm-card.lm-moment-card` div —
   i.e. before the `<b>{entry.title}</b>` line, not inside any wrapper —
   so the negative-margin bleed measures against the card's own padding
   edge. Keep `loading="lazy"` and `crossOrigin="use-credentials"`
   exactly as today.
2. Only when `entry.photo_ids.length > 1`, render the existing
   `.lm-moment-photos` row unchanged except mapping over
   `entry.photo_ids.slice(1)` instead of the full array.

No other file changes required for this fix.

### 7.7 Coverage note (what this pass does and doesn't cover)

This pass covers only UXD-4(b). It does not implement UXD-5 (raw
transport error text in chat/upload) or UXD-6 (raw browser error on shell
load) from the same retest — those remain open findings, unaffected by
and independent of this change. The backend-resized-thumbnail perf option
mentioned alongside UXD-4 in the retest is explicitly Architecture's call
and is not addressed by this design pass.
