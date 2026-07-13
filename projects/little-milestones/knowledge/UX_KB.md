<!--
FILE-INTEGRITY NOTE (recovered 2026-07-12 by orchestrator): §1-§6 of this
file were destroyed by an accidental Write call during the "Design preview
for Journey photo banner" pass earlier in this same session (the same
failure mode already logged for knowledge/ARCHITECTURE_KB.md in
admin/LESSONS.md -- an agent with Write, not Edit, access to a large
append-only KB file). Unlike the ui-ux-designer pass that discovered this
(and correctly declined to fabricate replacement content), this session's
own transcript logs contained the exact pre-corruption Write call
(60,317 chars, ending in "...never-wholesale-replace guidance." -- the
same sentence the corrupted file picked up mid-word), so the recovery
here is a byte-exact splice, not a reconstruction: recovered §1-§6 +
the untouched, already-intact §7/§8. See admin/LESSONS.md for the
recurring pitfall this is another instance of.
-->

# UX_KB — little-milestones

Maintained by: ui-ux-designer. Created at Experience Design gate, 2026-07-10.
Covers the approved F1–F10 scope, organized by PLAN.md §4.7's three build
increments. Advisory to core-pipeline owners at shared gates; code-agent
builds what is specified here — this file contains no implementation.

---

## 1. Design Intent

### 1.1 Who we are designing for, and the emotional register

The user is a sleep-deprived parent, usually on a phone, often one-handed
(the other arm is holding a baby), frequently at 2 a.m. and frequently
worried (DOMAIN_KB R7: milestone anxiety is nearly universal even when
development is fine). Every design decision below serves three rules:

1. **Calm over clinical.** This is a warm consumer parenting product, not a
   dashboard and not a healthcare tool. No metrics, gauges, progress bars,
   percentiles, scores, or status colors applied to the child. Explicitly
   NOT the energy-industry aesthetic of prior projects in this portfolio.
2. **One-handed, thumb-first.** Single-column layouts; primary actions in
   the bottom 60% of the viewport; bottom navigation; touch targets ≥44px;
   nothing important hidden behind hover.
3. **Anxiety-awareness is structural, not tonal** (DOMAIN_KB R1). Where the
   backend enforces R1 in the payload schema (PLAN §4.2), the UI enforces it
   in the component vocabulary: there is literally no component in the
   library that can render the child against a norm. See §1.9 for the
   testable rules.

### 1.2 Visual language — "storybook, not chart"

- **Metaphor:** a family storybook being written, not a tracker being
  filled. Content units are "moments" and "chapters," never "data points"
  or "entries."
- **Shape language:** soft — 16px card radius, 999px pill buttons, no sharp
  corners, no hairline data-grid borders. Generous whitespace.
- **Illustration/iconography:** simple rounded line icons (2px stroke).
  Motifs: leaves/sprout, sun/moon, stars, footprints. Banned motifs in any
  milestone-adjacent surface: warning triangles, exclamation badges,
  checkmark-vs-cross pairs, gauges, red dots, progress rings.
- **Photography treatment:** parent photos are the hero wherever they exist;
  UI chrome recedes (cream surfaces, quiet type). Photos always shown with
  a soft radius mask, never cropped into avatar circles by default (parents
  hate losing the edges of baby photos).
- **Motion:** slow and gentle (200–300ms ease-out); a single soft
  "settle" animation when a memory is saved (the moment lands on the
  journey). No bouncing badges, no attention-seeking pulses, and
  `prefers-reduced-motion` fully honored.
- **Voice in microcopy:** second person, warm, plain language, short
  sentences. Celebratory about logged moments; neutral-informative about
  milestone facts ("most children…"); never exclamatory about development
  itself.

### 1.3 Color scheme and rationale (original, 2026-07-10 — see §4 for the
revision-2 palette update; this section is kept intact as the historical
record of what was first proposed and why, per this file's own convention
of not silently overwriting prior rationale)

Warm, low-glare, nap-time-friendly. Rationale: cream instead of white
reduces glare for night use; terracotta reads warm/human rather than
corporate blue or clinical teal; sage carries "growth" without gamified
green-means-good semantics; and — the load-bearing choice — **the
"mention to your pediatrician" surface is a calm slate blue, never
red/amber**, so routine guidance never looks like an alarm (R1: no false
alarm) while still being visually distinct enough not to be missed (R1: no
false reassurance by burying it).

| Token | Hex | Use | Contrast notes |
|---|---|---|---|
| `--lm-cream` | `#FDF8F2` | App background | — |
| `--lm-card` | `#FFFFFF` | Card surfaces | — |
| `--lm-ink` | `#3D3833` | Primary text (warm near-black) | 11.9:1 on cream — AAA |
| `--lm-ink-soft` | `#6E6259` | Secondary text | 5.4:1 on cream — AA |
| `--lm-terracotta` | `#B85C38` | Primary actions, links | white text on it 4.7:1 — AA; as text on cream 4.5:1 — AA |
| `--lm-terracotta-deep` | `#9A4A2C` | Pressed/hover, small-text links | 6.3:1 on cream |
| `--lm-sage` | `#5F7A61` | Confirmations, activity tags, supervision notes | 4.9:1 on cream — AA |
| `--lm-slate` | `#52708F` | "Pediatrician note" info surface + icons | 4.6:1 on cream — AA (used with `#EEF3F8` tint bg, ink text) |
| `--lm-gold` | `#D9A441` | Celebration accents on the journey (decorative only, never text, never meaning-bearing) | n/a (decorative) |
| `--lm-blush` | `#F6E3D7` | Soft section tints, chat bubbles (assistant) | with ink text 10.8:1 |
| `--lm-danger` | `#A33B2E` | **Destructive delete confirmations ONLY** | white on it 6.5:1 |

**Superseded 2026-07-10 (revision 2, §4): the above hex values for
terracotta, terracotta-deep, sage, slate, gold, and blush were replaced
with more saturated versions after human review feedback that the palette
read too muted. `--lm-cream`, `--lm-ink`, `--lm-ink-soft`, and
`--lm-danger` are unchanged. See §4.2 for the new table and full rationale
— this table is retained as-is for the historical record, not deleted.**

Hard rules: `--lm-danger` (and any red/amber) may never appear on chat,
activities, timeline, digest, or product surfaces — it exists solely for
"delete profile/photo/memory" confirmations. Color is never the only
carrier of meaning (WCAG 1.4.1). Per-child identity hues for the switcher
(peach `#E8B39A`, sky `#A9C3D9`, moss `#AFC3A0`) are decorative labels
only — chosen deliberately un-gendered and never mapped to any status.
(Also revised for vibrancy in §4.2.)

Dark-mode note (2 a.m. use): a warm-dark theme (`#211D1A` bg, same hue
family) is specified as a fast-follow, honoring `prefers-color-scheme`;
Increment 1 ships light-only to protect scope, with tokens structured so
dark mode is a token swap, not a redesign.

### 1.4 Typography and layout system

- **Type:** a warm humanist sans (Nunito Sans or system-stack fallback
  `-apple-system, "Segoe UI", sans-serif`) for UI; optional friendly serif
  (Fraunces) reserved for journey chapter headings only. Base 16px/1.6;
  minimum rendered size 13px (disclaimer footer); headings max ~28px —
  book-like, not poster-like.
- **Layout:** single column, max-width 640px centered on desktop (this is a
  phone product that must merely not embarrass itself on desktop). Bottom
  tab bar on mobile: **Today · Chat · ✦ Journey · Add** (Add is the
  memory-logging quick action). Disclaimer is a persistent quiet footer
  above the tab bar (§1.10). **Superseded in part 2026-07-10 (revision 3,
  §5): "must merely not embarrass itself on desktop" undersold desktop as
  an afterthought — per PROJECT_CONTEXT.md's explicit responsive-web-app
  platform decision, desktop is required scope with real layout decisions,
  not a stretch of the phone view. See §5 for the actual desktop system
  (sidebar nav, per-screen breakpoints and max-widths); this bullet is kept
  for the historical record of the original (too-minimal) assumption.**
- **Forms:** one question per screen in onboarding; large inputs; native
  date picker for DOB; every flow keyboard-completable with visible focus
  rings (`--lm-terracotta` 2px offset outline).

### 1.5 Increment 1 — onboarding, chat, activities (F1–F5)

#### Flow 1a: First-run onboarding → profile creation (F1)
```
Welcome → Name → Birthday → Born-early question → (weeks, if yes) → Ready
```
1. **Welcome** — one screen: app promise ("A calm companion for
   {your child}'s first three years — ideas, answers, and a place to keep
   the moments") + the privacy stance up front ("Everything stays private
   to your family. We never use your child's data or photos to train AI.")
   + primary button "Add your child". No account wall in Increment 1
   (auth arrives in Increment 3 behind the seam).
2. **Name** — "What should we call your little one?" helper text: "A first
   name or nickname is perfect — that's all we ask for." (data-minimization
   made visible, R6).
3. **Birthday** — native date picker; client-side validation (not future,
   not >20y) with gentle inline copy, never a red toast.
4. **Born-early question** — the sensitive screen; exact copy specified in
   §1.10. Skippable with a clearly stated consequence, never a guilt trap.
5. **(Conditional) Weeks early** — stepper input 3–17, plus the one-line
   corrected-age explainer and the early-intervention acknowledgment
   sentence (PLAN §3.1).
6. **Ready** — "{Name}'s space is ready" with the child's identity hue; a
   single suggestion chip ("Ask anything — try: what does a typical
   {age}-month-old enjoy?") routes into chat. If the family already has a
   child, steps 2–5 run inside a sheet from the switcher instead.

#### Flow 1b: Multi-child switcher (F1)
Persistent header element: current child's name + identity-hue dot; tap →
bottom sheet listing all children (name, age line incl. corrected age where
applicable), "+ Add a child", and per-child overflow → "Remove {name}'s
profile" → typed-confirmation destructive dialog (the ONLY red surface;
copy states plainly that memories and photos are permanently deleted).
Selected child scopes every tab. **Extended 2026-07-10 (§6): each row also
previews that child's photo-personalized accent (or the default identity
hue if no photo yet) — see §6.4.**

#### Flow 1c: Milestone chat (F3)
```
Chat tab → (age context strip) → ask → streamed reply → follow-up chips
```
- **Age context strip** at top of chat: "{Name} · 14 months" — and for
  preterm children: "{Name} · 6 months (about 4 months corrected)" with an
  ⓘ affordance opening the plain-language corrected-age explainer.
  Corrected age is visible everywhere age is (UXR-5).
- Bubbles: parent right in white, assistant left in `--lm-blush`; assistant
  has no persona avatar pretending to be a person (trust posture).
- **Pediatrician-note card**: when a reply includes "worth mentioning to
  your pediatrician," the frontend renders that sentence inside the slate
  info card (calendar/speech icon) — visually distinct, calm, and never
  alarm-styled (UXR-2). This is presentation of the model's R1-compliant
  text, not new generated content.
- Empty state offers 3 age-computed suggestion chips (never
  anxiety-priming; e.g. "Ideas for rainy-day play", not "Is {name} on
  track?").
- Out-of-range/newborn modes (F2): the context strip states the mode
  plainly ("{Name} is past 36 months — milestone content covers birth to 3,
  but ask me about activities anytime").

#### Flow 1d: Activities + "what's coming next" (F4)
Today tab, two sections:
- **"Good for right now"** — activity cards: title, 1–2 line description,
  and a sage supervision line with a small hand icon ("Stay within arm's
  reach — water play is always together-time"). Supervision context is part
  of the card anatomy, not a footnote.
- **"Things to look forward to"** — the coming-next preview as an
  *invitation*, never a deadline: "Around the {next bucket} mark, many
  little ones start exploring X — here are ways to play along." No dates
  the child is measured against, no countdown (UXR-8).

#### Disclaimer placement (F5)
Persistent quiet footer (see §1.10 for copy): `--lm-ink-soft` small text on
cream, always in the DOM and visible above the tab bar, styled as a calm
signature line — not a banner, not dismissible, never modal, never the word
"warning." It links "CDC Milestone Tracker" as plain text-link. Playwright
asserts presence + ≥4.5:1 contrast on every route (§7-D/E).

### 1.6 Increment 2 — memories, the journey, photos (F6, F7, F8 content)

#### Flow 2a: Logging a memory (F6) — the retention engine, so friction ≈ 0
```
"Add" tab (or + on Journey) → sheet: [photo?] [title] [date=today] → Save
```
- One sheet, three fields, sensible defaults: date pre-filled to today,
  title with rotating gentle placeholder prompts ("First belly laugh?
  A food that got everywhere?"), optional note, optional milestone tag
  picker (a *memory label*, framed "What kind of moment?" — never an
  assessment checkbox list), optional photo (Increment 2 second half).
- **Target: loggable in ≤3 taps plus typing, from anywhere** (UXR-7).
- Save → the gentle "settle onto the journey" animation + "Added to
  {Name}'s journey" toast with a "See it" link. This tiny payoff loop is
  the Qeepsake mechanic (INDUSTRY_KB §1.3–1.4).

#### Flow 2b: The life journey (F6) — the "really cool" moment
The human's words were "a really cool life journey," and INDUSTRY_KB says
this view is the emotional core of the category. Design concept:

**"The Story of {Name}" — a vertical storybook river.**
- Entered from the ✦ Journey tab or the "See {Name}'s journey" button.
- **Header:** the child's name in the serif display face, their identity
  hue as a soft wash, and one warm elapsed-time line: "412 days of Maya —
  23 moments so far." A quiet lock glyph + "Private to your family."
- **The river:** a gently curving vertical path (an organic vine/path
  stroke in the identity hue at 30% opacity) flowing top-to-bottom from a
  "Hello, world" birth marker. Memory cards alternate sides of the path on
  wider screens, stack on phones. Each card: photo (if any) as hero, title,
  note excerpt, and an **age-at-moment badge** ("8 months, 2 weeks" —
  corrected age shown for preterm children within the window, per payload).
- **Chapter markers, not gates:** passed checklist buckets appear only as
  soft typographic dividers along the path — "· Six months ·" in the serif
  face with a small gold sun/leaf flourish. They are chapter headings for
  the child's own book. They carry **no** expected-milestone content, no
  checkmarks, no "typical by now" annotations — there is nothing at a
  marker to have "met" or "missed" (this mirrors the payload guarantee in
  PLAN §4.2: no `expected_by`/`status`/`on_track` fields exist to render).
- **Structurally incapable of comparison (R1 in visual form):** the journey
  is a *list keyed only to the child's own dates*. There is no time axis
  with fixed norm positions, no second series, no "typical range" band, no
  color-coding of moments against anything, no other-children content. A
  child with 3 moments and a child with 300 both get a complete, beautiful
  book. Empty state: "Every story starts somewhere — add {Name}'s first
  moment" (never "you haven't logged anything yet").
- **Celebration, sparingly:** the newest moment gets a one-time soft gold
  shimmer on first view; milestone-tagged memories get a small gold star on
  the card corner. Gold decorates *what the parent chose to celebrate*,
  never what a table says should have happened.
- Accessibility: the river renders as a semantic ordered list
  (`<ol>` of moments with chapter markers as list headings); fully
  keyboard/screen-reader traversable; the decorative path is `aria-hidden`.

#### Flow 2c: Photos (F7) — private by default, said out loud
- Photo attach lives inside the memory sheet (camera/library); upload shows
  a soft progress wash on the card, ≤10MB with a friendly size message.
- **Privacy cue at the exact moment of upload** (UXR-10), one line under
  the picker: "Photos stay private to your family. Never public, never
  used for AI, never scanned for faces." Lock glyph. Same line appears on
  the all-photos view ("{Name}'s photos").
- Deleting a photo or memory: destructive dialog stating "deleted
  immediately and permanently — we keep no copies" (retention policy as UI
  copy, PLAN §4.3).
- No share/export affordances this run — absence of share buttons is itself
  the privacy posture; nothing implies these images go anywhere.

#### Flow 2d: "This week" panel (F8 content)
A card at the top of Today: "{Name} is 14 months this week" + 2–3 typical
things ("most children" framing, current bucket only), one activity, one
memory prompt ("It's been a little while — anything worth remembering from
this week?"). Same component family as activities; disclaimer constant in
payload and footer as everywhere.

### 1.7 Increment 3 — buying ideas, caregivers, digest delivery (F9, F10, F8)

#### Flow 3a: Buying suggestions (F9) — contextual, never ad-like
- A section on Today (below activities): **"Ideas for this stage"** —
  category cards ({title, why_this_age, safety_note}) in the *identical*
  card anatomy as activity cards (UXR-11): same surface, same sage safety
  line. No prices, no brands, no store logos, no urgency ("only 3 left"),
  no "sponsored" visual grammar, no external links this run.
- Framing line above the section: "Just ideas keyed to {Name}'s age — we
  don't sell anything or earn from these."
- Newborn/out-of-range: the defined-mode statement, never fabricated cards.

#### Flow 3b: Auth + caregiver invites (F10)
```
Signup (first run) → creates family/owner | Login
Owner: Settings → "Your family" → Invite → code/share sheet
Caregiver: "Join a family" → enter code → account → sees the journey
```
- Auth screens keep the storybook warmth (cream, one column, pill buttons)
  — a login page is still this product. Error copy is factual and calm.
- Family panel lists caregivers with role labels in plain words: "Owner"
  → shown as "{Name}'s space was created by you"; caregivers as "Can view
  and add moments." Owner-only controls (delete profile/photos, invites)
  simply don't render for caregivers; server enforces (PLAN §4.6), UI
  never dangles a control that will 403.
- Invite: single-use expiring code presented big and copyable, with "This
  code invites someone into {Name}'s private space — share it like a key."
- The migration moment (pre-auth data → first family) must be invisible:
  first signup lands with the journey intact.

#### Flow 3c: Digest opt-in (F8 delivery)
- Per-caregiver toggle in Settings: **default OFF, rendered off,** with
  equal visual weight for both states — no pre-checked box, no nagging
  modal, no "are you sure?" on decline (UXR-12).
- Copy: "A short weekly note — {Name}'s age, a few ideas, and a memory
  prompt. Off unless you turn it on. One tap to stop anytime."
- If Architecture rules email out (PLAN §6.4), the same toggle governs the
  in-app "This week" prominence and the copy adapts; the control's
  location and default don't change.

### 1.8 Screen & component inventory

**Screens/routes:** Welcome/onboarding (4–5 steps) · Today (activities +
coming-next + this-week + ideas-for-this-stage) · Chat · Journey ·
Add-memory sheet · All-photos view · Child switcher sheet · Settings
(family, digest, privacy/retention copy) · Auth (signup, login, join-by-
code, invite) · Destructive-confirm dialogs.

**Component library (DesignSync push set):**
| Component | Variants |
|---|---|
| Foundations: color tokens | full palette + usage rules |
| Foundations: type scale | serif display / sans UI |
| Button | primary pill / secondary outline / quiet text / destructive |
| Input group | text, date, stepper, one-question onboarding frame |
| Chat bubbles | parent / assistant / streaming |
| Pediatrician-note card | slate info card (the R1 surface) |
| Activity card | with supervision line; product-idea variant |
| Coming-next card | invitation framing |
| Memory card | photo / text-only / milestone-tagged (gold star) |
| Journey chapter marker | serif divider + flourish |
| Journey header | elapsed-time line + privacy badge |
| Age context strip | standard / corrected-age / newborn / out-of-range |
| Child switcher row | identity hue dot + age line |
| Disclaimer footer | fixed copy |
| Toggle (digest) | on/off, default-off |
| Destructive dialog | the only red surface |
| Privacy cue line | lock glyph + copy |

### 1.9 Anxiety-aware design rules — testable UX requirements

These are the UX/accessibility suite's assertions at the Test gate
(extends PLAN §7-E/§7-F19; evidence to `test-evidence/` per convention,
screenshots for visual checks). Each is pass/fail.

- **UXR-1 (R1 structural):** The rendered Journey DOM contains no element
  representing expected-vs-actual: no norm axis, no second data series, no
  "typical range" band, no status/on-track semantics, no color mapping of
  memories to norms. Chapter markers contain only the bucket label text +
  decorative flourish. (Playwright DOM assertions + screenshot evidence;
  pairs with the §7-F19 schema lint.) **Re-verified 2026-07-10 for the
  desktop alternating-sides layout (§5.4) — spatial alternation carries no
  norm/axis semantics.**
- **UXR-2 (no alarm styling):** No red/amber (`--lm-danger` or any hue
  <40° at >50% sat) appears on chat, Today, Journey, digest, or product
  surfaces; the pediatrician-note card uses `--lm-slate` styling and a
  non-warning icon. Computed-style scan per route. **Re-verified 2026-07-10
  for photo-personalization (§6) — the personalization system is
  hard-excluded from ever touching the pediatrician-note card's slate
  token; see §6.2.**
- **UXR-3 (sensitive question):** The prematurity screen renders the exact
  §1.10 copy; a Skip control is visible without scrolling; skipping shows
  the full-term-assumption note on the Ready screen and in Settings.
- **UXR-4 (disclaimer):** Fixed disclaimer text present and visible on
  every route, ≥4.5:1 contrast, not inside a dismissible/modal container,
  contains no "warning"/alarm iconography.
- **UXR-5 (corrected age):** For a preterm fixture (P2), every UI location
  displaying age also displays corrected age with the explainer affordance
  — chat strip, switcher, journey badges, this-week card.
- **UXR-6 (accessibility baseline):** WCAG 2.1 AA text contrast on all
  tokens as used; touch targets ≥44×44px; all flows (onboarding, memory
  log, delete, auth, invite/join) keyboard-only completable with visible
  focus; journey traversable as a list by screen reader; images require
  alt (parent-entered or title fallback); `prefers-reduced-motion`
  disables all nonessential animation. **Extended 2026-07-10: desktop
  interactive elements (sidebar nav items, tag chips) also require visible
  hover states, not just focus rings — hover is available to mouse users
  and should not be the odd surface left out.** **Extended again
  2026-07-10 (§6): AA contrast must hold for text sitting on any
  photo-personalized surface regardless of the uploaded photo's colors —
  see §6.3's automated-check + fallback requirement, which becomes a new
  test assertion (UXR-13).**
- **UXR-7 (logging friction):** From Today, a text-only memory is savable
  in ≤3 taps + typing; the Add action is reachable in the bottom
  thumb-zone on a 375×667 viewport.
- **UXR-8 (invitation framing):** Coming-next and this-week surfaces
  contain no deadline/countdown lexicon rendered by the UI ("due," "by
  now," "should already," "behind," "on track") — UI-copy lint,
  complementing the §7-D15 payload lint.
- **UXR-9 (one red surface):** Destructive styling appears only inside
  delete-confirmation dialogs, which require an explicit second action and
  state permanence in plain language.
- **UXR-10 (photo privacy cue):** The upload control and all-photos view
  render the privacy line verbatim; no share/export affordance exists on
  photo surfaces this run.
- **UXR-11 (non-ad commerce):** Product-idea cards computed-style-match
  the activity card family; payload+DOM contain no price, brand, affiliate
  URL, tracking parameter, urgency copy, or sponsored badge.
- **UXR-12 (digest consent):** Fresh caregiver account → toggle renders
  off; enabling requires exactly one deliberate action; disabling requires
  exactly one and shows no retention dialog. Opt-in state per-caregiver
  (with F10 fixtures).
- **UXR-13 (photo-personalization AA + fixed-token isolation, new
  2026-07-10, §6):** (a) For any fixture photo (including adversarial
  dark/low-contrast/monochrome fixtures), computed text contrast on every
  photo-personalized surface is ≥4.5:1 (≥3:1 for large text); if the
  automated pre-render check fails, the surface renders the fixed default
  theme instead, never an unchecked accent. (b) Computed-style scan
  confirms `--lm-slate`, `--lm-danger`, `--lm-ink`, and `--lm-ink-soft`
  are byte-identical to their fixed hex values on every route regardless
  of which child/photo is active — the personalization token set
  (`--lm-photo-*`) never aliases or overrides them. (c) Two child fixtures
  with different photos produce different computed `--lm-photo-mid`
  values in the switcher DOM (no shared/cached accent across profiles).

### 1.10 Sensitive copy specification (exact strings)

**Prematurity question (flagged sensitive — this wording is the design):**
> **"Did {name} arrive earlier than expected?"**
> "Babies born three or more weeks early grow on their own beautiful
> schedule. Telling us helps us use *corrected age* — the age pediatricians
> recommend for milestones in the first two years."
> Options: **"Arrived right on time (or close)"** · **"Yes, {name} came
> early"** · quiet link: **"Skip this"**
> If skipped, Ready screen + Settings show: "We'll assume {name} arrived
> full-term — you can change this anytime in {name}'s profile."
> If yes → "About how many weeks early?" stepper (3–17) + "{name}'s
> milestones will use corrected age until around age two. Their birthday
> is still their birthday." Followed by the acknowledgment line: "If
> {name} has a developmental diagnosis or is in early intervention, your
> care team's guidance comes first — general milestone info may not fit,
> and that's okay."

Rationale: leads with the child's name and "earlier than expected" (the
parent's lived experience), never "Is your child premature?" (a label
applied to the child); frames corrected age as care, not correction;
"their birthday is still their birthday" pre-empts the most common
parental confusion; skip carries zero shame.

**Disclaimer (fixed constant, PLAN §3.4(6) — placement per §1.5):**
> "little-milestones offers general parenting information and ideas — it
> is not medical advice or a developmental screening tool. For concerns
> about your child's health or development, talk to your pediatrician. The
> free CDC Milestone Tracker is the official screening checklist."

**Profile delete confirmation:**
> "Remove {name}'s profile? This permanently deletes {name}'s profile,
> every memory, and every photo — immediately, with no copies kept. This
> can't be undone." Confirm requires typing the child's name.

---

## 2. DesignSync Status

**Pushed 2026-07-10 (initial gate)** to Claude Design project
**"little-milestones design system"** (projectId
`172e0c51-e31a-46e7-aedb-bead17b38868`, created this gate — no prior
project existed). 8 preview files written under plan
`plan_172e0c51e31a46e7_7f5b2c9fcfa9`:

| Group | Path | Card |
|---|---|---|
| Foundations | `foundations/colors.html` | Color palette + usage rules |
| Foundations | `foundations/type.html` | Type scale |
| Components | `components/buttons.html` | Button variants |
| Components | `components/chat.html` | Chat bubbles, age strip, pediatrician-note card |
| Components | `components/cards.html` | Activity / coming-next / product-idea cards |
| Journey | `journey/timeline.html` | Life-journey river (header, moments, chapter markers) |
| Forms | `forms/onboarding.html` | Born-early question screen (sensitive copy) |
| Trust | `trust/trust.html` | Disclaimer footer, privacy cue, digest toggle, destructive dialog |

**Pushed 2026-07-10 (revision 2, same day — post-review palette + screens
pass):** see §4.3 for the full incremental push record (6 files updated
in place with the revised palette, 5 new full-screen files added under a
new `screens/` path). No file was wholesale-replaced; every update kept
the same path/card identity it had before, and the historical rationale
above (§1.3) was preserved rather than overwritten.

**Pushed 2026-07-10 (revision 3, same day — desktop layouts, §5):** 5 new
files under a new `screens/desktop/` path. No existing path touched,
overwritten, or deleted — purely additive, per this tool's own
never-wholesale-replace guidance. See §5.5 for the full push record.

**Pushed 2026-07-10 (revision 4, same day — photo personalization, §6):**
3 new files under a new `screens/personalization/` path. No existing path
touched, overwritten, or deleted — purely additive. See §6.5 for the full
push record.

Next pushes (incremental, per build increment — never wholesale replace):
input group/date/stepper set and child-switcher row as Increment 1 firms
up; memory-entry sheet and all-photos view for Increment 2; auth screens
and invite-code presentation for Increment 3.

---

## 3. Observed Post-Deploy Behavior

_No production usage yet. To be populated after release: which surfaces
parents actually open (Today vs Chat vs Journey), memory-logging frequency
and drop-off, whether the pediatrician-note card correlates with session
abandonment (anxiety signal), digest opt-in rate, and any observed
confusion around corrected age._

---

## 4. Revision — 2026-07-10 (post-review): palette vibrancy pass + full-screen mockups

Human feedback on the initial review: **"UI colors need to pop out more,
research some children-centric apps and draw up some wireframes of the
application perhaps use Figma designs etc."** This section documents what
changed and why, without deleting or silently editing §1's original
rationale. No Figma seat is available to this agent in this environment;
the deliverable equivalent — composed, reviewable full-screen HTML
mockups plus a synced Claude Design component library — is produced
instead (per this role's own approval-artifact requirement).

### 4.1 Research: children/family-app visual language, and the audience
correction that shapes how it applies here

I don't have a live web-search tool available in this session, so what
follows is a synthesis from established design knowledge of these
products' publicly known visual identities, not a freshly fetched source
list — flagged honestly rather than presented as citations I don't have.

- **Child-facing play/education apps** (Sago Mini World, Khan Academy
  Kids, PBS Kids): fully saturated primary-hue palettes (reds, yellows,
  blues at or near full saturation), thick friendly mascot characters, big
  tap targets with high color salience — because the *child* is the one
  choosing where to tap, at an age where color is the primary navigation
  cue. High chroma is functional there, not just decorative.
- **Duolingo**, though it has a mascot, is instructive as a family/adult
  crossover case: a single highly saturated signature hue (its green) used
  confidently and consistently reads as energetic and optimistic to an
  *adult* audience without reading as a kids' toy — because it's deployed
  as one disciplined brand color against a clean neutral UI, not a
  rainbow of competing saturated hues.
- **Parent-facing apps** (Peanut — a community app for mothers; BabyCenter;
  Huckleberry — infant sleep tracking): these skew warm-saturated but
  adult — coral/terracotta/plum accent colors against light neutral
  backgrounds, confident typography, generous whitespace. Huckleberry in
  particular is a useful cautionary data point: it leans on charts/graphs
  for sleep data, which is exactly the "tracker" register this product's
  R1 constraints were written to avoid — vibrancy from that category
  should not be read as license to import chart/gauge visual grammar.
- **The audience correction that governs this revision:** the CHILD never
  opens little-milestones — the PARENT does, often at 2 a.m., often
  anxious, and the pediatrician-note surface has to keep reading as calm
  and trustworthy (R1/R2). So "more pop" is implemented as *Peanut/
  Duolingo-register* vibrancy — richer, more confident saturation on a
  small set of disciplined accent hues — not *Sago Mini/PBS Kids-register*
  vibrancy, which would read as a children's toy and undercut exactly the
  trust posture the pediatrician-note card and disclaimer depend on. This
  is the same reasoning already in §1.1 rule 1 ("Calm over clinical," not
  "muted" — those aren't the same instruction, and the original palette
  conflated them; revision 2 corrects that specific overreach without
  touching the calm-over-clinical *or* anxiety-aware rules themselves).

### 4.2 What changed in the palette, and why (every R1/R2 constraint
re-verified, none relaxed)

| Token | Was (rev. 1) | Now (rev. 2) | Why | Contrast re-check |
|---|---|---|---|---|
| `--lm-cream` | `#FDF8F2` | **unchanged** | Background muted-ness is a hard constraint (2am low-glare), not the complaint — the complaint was about accents, not the backdrop. | n/a |
| `--lm-ink` / `--lm-ink-soft` | `#3D3833` / `#6E6259` | **unchanged** | Text legibility already AAA/AA; no reason to touch. | 11.9:1 / 5.4:1 (unchanged) |
| `--lm-terracotta` | `#B85C38` | `#C1502A` | More saturated/warmer "sunset" terracotta — same role (primary actions/links), deliberately re-tuned to keep luminance in the same band so AA holds both directions. | ~4.5:1 as text on cream; ~4.7:1 white-on-it (still AA both ways, matching the original's claim) |
| `--lm-terracotta-deep` | `#9A4A2C` | `#8F3A1D` | Deepened proportionally with the primary for a consistent pressed/hover state. | ≥6:1 on cream |
| `--lm-sage` | `#5F7A61` (a muted blue-green) | `#2F7A4E` (a true, punchier "leaf" green) | The old sage read closer to gray-green than green; the new one is recognizably vivid growth-green while keeping the same non-gamified role (supervision lines, confirmations only — never a pass/fail signal). | ~5.0:1 on cream — AA |
| `--lm-slate` | `#52708F` | `#3D6188` | Deepened, not saturated toward warm — this is the one token where "pop" had to mean *more presence/legibility*, not more chroma, because it's the load-bearing non-alarm surface (R1). A deeper slate reads more confident/less washed-out while staying unambiguously calm-blue, nowhere near red/amber hue space. | ~6.1:1 on cream (up from 4.6:1) — stronger AA margin |
| `--lm-gold` | `#D9A441` | `#E8A317` | More vivid marigold for journey celebration. Usage rule unchanged: decorative only, never text-bearing, never meaning-bearing beyond "the parent chose to celebrate this." | n/a — decorative, not used for text |
| `--lm-blush` | `#F6E3D7` | `#FADCC5` | Richer peach tint for assistant chat bubbles and soft section fills. | Ink text on it remains >9:1 |
| **`--lm-coral`** | *(new token)* | `#FF7A50` | New decorative-only accent carrying most of the "pop": hero gradients on Welcome/This-week cards, the journey river line, active tab-bar fill accents, large illustration fills. Explicitly restricted to decorative/large-scale use — never small text on light, never a status signal — so it adds energy without creating a new contrast liability or a new "meaning" color that could be confused with alarm/status. | Decorative-only by rule; not used for body text |
| `--lm-danger` | `#A33B2E` | **unchanged** | This was never the "muted" complaint, and it's the one hue that must stay exactly where it is — R1/UXR-9 depend on red meaning exactly one thing (destructive) and appearing nowhere else. Touching it was out of scope by design. | 6.5:1 white-on-it (unchanged) |
| Identity hues (peach/sky/moss) | `#E8B39A` / `#A9C3D9` / `#AFC3A0` | `#F0A574` / `#6FA8D8` / `#7CB56C` | Bumped for the same reason as sage — richer without becoming gamified or status-coded; still decorative labels only, still never mapped to any status (UXR-2's rule extends to these). | Decorative dot/wash use; not relied on for text contrast |

**What did NOT change:** the "storybook not chart" register (§1.2), the
banned-motif list, the R1 structural rule that the Journey view is
incapable of rendering comparison (UXR-1, unchanged and re-verified against
the new coral river-line treatment in the rev-2 mockup — it's still a
decorative `aria-hidden` path with no norm axis), the slate-not-red rule
for pediatrician notes (UXR-2), the single-red-surface rule (UXR-9), all
AA contrast minimums (UXR-6), and the "no norm/comparison framing"
constraint anywhere on the journey. Every hard rule in §1.3's "Hard rules"
paragraph still holds against the new tokens.

### 4.3 Full-screen wireframes produced

Composed, not isolated-component, screens — a human can scroll each one
top to bottom as a real app screen. Written to
`projects/little-milestones/design-review/screens/`:

| File | Screen(s) |
|---|---|
| `screens/onboarding-welcome.html` | Welcome screen + the sensitive born-early question screen, side by side |
| `screens/chat-screen.html` | Full milestone chat screen: status bar, age-context strip, bubbles, pediatrician-note card, composer, disclaimer, tab bar |
| `screens/today-screen.html` | Full Today screen: this-week hero card, good-for-right-now activities, coming-next invitation card, ideas-for-this-stage, disclaimer, tab bar |
| `screens/journey-screen.html` | Full Life Journey screen: "The Story of Maya" composed in-frame with header, river, chapter markers, quick-add action, tab bar |
| `screens/photo-upload.html` | Add-memory sheet over a dimmed Today background: photo grid, privacy cue at the point of upload, memory-label tag chips, save action |

`projects/little-milestones/design-review/index.html` now has a "Full
Screens (revision 2)" section linking all five, plus revision-2 badges on
every existing foundations/components/journey/forms/trust card whose
underlying preview file's tokens were updated in place (colors, chat,
cards, journey/timeline, onboarding, trust — all 6 rewritten with the new
hex values; buttons and type were left as-is since they don't carry the
affected tokens directly beyond the shared palette, and are still valid).

### 4.4 DesignSync push (incremental, not wholesale-replace)

Same project, `172e0c51-e31a-46e7-aedb-bead17b38868`. New plan finalized
covering: overwrites of the 6 existing paths whose token values changed
(`foundations/colors.html`, `components/chat.html`, `components/cards.html`,
`journey/timeline.html`, `forms/onboarding.html`, `trust/trust.html`) plus
5 new paths under `screens/**`. No deletes; no path outside this set was
touched; `components/buttons.html` and `foundations/type.html` were left
untouched since revision 2. See the platform push confirmation in this
gate's chat response for the plan/write result.

---

## 5. Revision — 2026-07-10 (second review pass): desktop/responsive layouts

Human feedback on the revision-2 review: the phone-frame mockups looked
good, but **"is there a desktop view?"** — there wasn't one. Per
PROJECT_CONTEXT.md's explicit platform decision ("responsive web app —
any browser, phone or desktop, no install"), a real desktop layout is
required scope, not a nice-to-have; §1.4's original "must merely not
embarrass itself on desktop" line undersold this (superseded in §1.4
above, not deleted). This section specifies the actual desktop treatment
for the same five key screens already mocked up for phone, as genuine
responsive layouts — not a stretched phone view — plus the reasoning for
each decision.

### 5.1 The one shared structural decision: sidebar nav, 1024px breakpoint

The bottom tab bar (**Today · Chat · ✦ Journey · Add**) is a mobile-only
pattern — thumb-reachable navigation makes no sense once there's no thumb
and no bottom-of-viewport reachability constraint. At **≥1024px** it is
replaced by a **persistent left sidebar** (248px wide, white surface,
right hairline border) containing, top to bottom: the brand mark, the
child switcher (identity-hue dot + name + age line, same content as the
mobile switcher, now always-visible instead of a tap target), the three
primary nav items (Today/Chat/Journey) as a vertical list with the same
icon+label pairing as the tab bar, and the Add action as its own
outlined pill button beneath the nav list rather than folded into it —
preserving Add's status as a distinct quick action (as it already was on
mobile, visually set apart with the gold icon tint) rather than promoting
it to equal rank with the three destinations. 1024px was chosen because
it's the same breakpoint at which Today's grid needs to switch (§5.3) —
one shared number for "desktop mode" rather than two independently-tuned
breakpoints a developer has to reconcile.

**What deliberately does NOT fill the reclaimed horizontal space:** no
dashboard widgets, no secondary metrics panel, no "recent activity" feed
bolted onto the sidebar. That would directly violate the "storybook not
chart" register (§1.2) and the calm-over-clinical rule (§1.1) — a sidebar
crowded with panels is exactly the dashboard aesthetic this product is
explicitly not. The sidebar's job is nav + identity, nothing else.

### 5.2 Onboarding — confirmed narrow, no sidebar, at any width

Decision: **stays centered at max-width 440–480px at every breakpoint**,
with no sidebar and no nav chrome at all (onboarding is a short, linear,
first-run flow — a login-adjacent surface, not a destination you navigate
back into). This was a deliberate confirmation, not a default: a form
with one question per screen (§1.4) does not read better wider — widening
it would only lengthen eye-travel per line and dilute the single-question
focus the mobile design already got right. The desktop mockup makes the
non-decision visible by placing the same-width card inside a full
~1320px frame with generous surrounding whitespace, rather than silently
reusing the phone frame — so a reviewer can see the choice, not just
infer it. One addition made for desktop specifically: visible `:hover`
states on the option buttons and CTA (mouse users get hover in addition
to the focus rings already specified; §1.9 UXR-6 extended accordingly).

File: `design-review/screens/desktop/onboarding-desktop.html`.

### 5.3 Milestone chat — sidebar + reading-width column, not a wide chat

Decision: sidebar nav per §5.1, and the **chat column itself stays capped
at 680px max-width, centered in the remaining space** — it does not
stretch to fill the ~1000px available next to the sidebar. Chat bubbles
that spanned 1000px would be harder to read (line length) and would
visually resemble a support-ticket console rather than a conversation.
The reclaimed margin on either side of the 680px column is filled with
a single quiet, `aria-hidden`, low-opacity decorative radial wash (coral/
gold, 10% opacity) — texture, not content — so the desktop chat screen
doesn't read as an unfinished narrow column floating in empty space, but
still adds zero informational clutter. The age-context strip, bubbles,
pediatrician-note card, chip suggestions, and composer are all otherwise
unchanged in content and behavior from the mobile version.

File: `design-review/screens/desktop/chat-desktop.html`.

### 5.4 Today / Activities — the screen that earns a real grid

Decision: **single column below 1024px, 2-column card grid at/above
1024px**, content capped at max-width 980px within the sidebar layout.
This is the screen flagged as most likely to benefit from desktop space,
and it does: activity cards, coming-next, and ideas-for-this-stage are
all the same card family (§1.8), and a 2-column grid lets a parent scan
more of "what's available right now" without excess scrolling, while
each card keeps its original size and card-anatomy (icon chip, title,
description, sage supervision line) rather than being stretched thin.
The this-week hero card spans both columns (`grid-column: 1 / -1`) since
it is a single per-child summary, not a repeatable item — a 2-up hero
would look like two separate weeks. A 3-column grid at even wider
viewports was considered and rejected for this pass: at 980px content
width, 3 columns would compress each card below a comfortable reading
width for the description + supervision line; 2 columns was chosen
deliberately over "more columns because there's room."

File: `design-review/screens/desktop/today-desktop.html`.

### 5.5 Life Journey timeline — centered river, wider margins, alternating sides (not a fundamentally different treatment)

Decision: the vertical river **stays centered** — this is a deliberate
choice, not the default, made because the journey is explicitly a
narrative/storybook read (§1.6's "The Story of {Name}"), and a
fundamentally different desktop treatment (e.g., a wide multi-column
gallery, a horizontal timeline, or a map-like layout) would trade the
book-like top-to-bottom reading order for something closer to a
dashboard or gallery browse — exactly the register this feature was
built to avoid (UXR-1's "structurally incapable of comparison" logic
extends to layout, not just color/data: a grid of moments invites
scanning-for-completeness in a way a linear river does not). What *does*
change at desktop: the spec already called for "cards alternate sides of
the path on wider screens, stack on phones" (§1.6) — this revision is
where that alternation is actually built. At ≥1024px, moment cards
alternate left/right of a centered vertical path (max content width
760px, generous margins on both sides within the sidebar layout), using
the extra width for breathing room and a more book-spread feel rather
than for more information density. Chapter dividers remain full-width
centered text, unaffected by the alternation. UXR-1 was re-verified
against this layout: alternating sides is a purely spatial/decorative
choice with no norm axis, no second data series, and no meaning attached
to which side a card lands on.

File: `design-review/screens/desktop/journey-desktop.html`.

### 5.6 Photo upload / add-memory — sheet becomes a modal, not just a wider sheet

Decision: this was flagged in the task as "likely a straightforward
width increase" — on inspection, a straightforward width increase would
actually be wrong: a bottom sheet that merely got wider at desktop would
look like a UI bug (sheets are a mobile-gesture pattern; there's no
swipe-to-dismiss affordance or motivation for anchoring content to the
bottom edge on desktop). The correct responsive counterpart is a
**centered modal dialog** at **≥768px** (a lower, independent breakpoint
from the 1024px nav/grid breakpoint, since the add-memory flow is
reachable from Today at any width above phone-only, including narrower
tablet-width windows before the sidebar appears): fixed width 640px,
rounded on all four corners (vs. only the top two on the mobile sheet),
centered both axes over a dimmed backdrop, with an explicit close
control and a two-button footer (Cancel / Add to {Name}'s journey)
replacing the single full-width save button — the standard desktop
dialog affordance. Content is otherwise the same three-field flow
(photo, title, tag, date) with a slightly wider photo grid (5 columns vs
3, since the dialog itself is wider) preserving the "loggable in ≤3 taps
plus typing" target (UXR-7 — desktop point-and-click reduces this
further, not increases it).

File: `design-review/screens/desktop/photo-upload-desktop.html`.

### 5.7 Files produced and where they live

Written to `projects/little-milestones/design-review/screens/desktop/`,
additive only — none of the five revision-2 mobile screen files (§4.3)
were modified:

| File | Screen |
|---|---|
| `screens/desktop/onboarding-desktop.html` | Onboarding — Welcome + born-early question, desktop |
| `screens/desktop/chat-desktop.html` | Milestone chat, desktop (sidebar nav) |
| `screens/desktop/today-desktop.html` | Today/Activities, desktop (2-column grid) |
| `screens/desktop/journey-desktop.html` | Life Journey timeline, desktop (alternating river) |
| `screens/desktop/photo-upload-desktop.html` | Add-memory / photo upload, desktop (centered modal) |

`projects/little-milestones/design-review/index.html` now has a "Desktop
(rev. 3)" nav link and section presenting all five alongside the
existing mobile sections, plus a compact strategy summary box (nav
pattern, breakpoints, max-widths) at the top of that section so a human
reviewer sees the decisions stated plainly, not just the artifacts.

### 5.8 DesignSync push (incremental, additive only)

Same project, `172e0c51-e31a-46e7-aedb-bead17b38868`. New plan finalized
covering exactly the 5 new paths under `screens/desktop/**`. No existing
path (foundations, components, journey, forms, trust, or the revision-2
`screens/*.html`) was touched, overwritten, or deleted. See the platform
push confirmation in this gate's chat response for the plan/write result.

---

## 6. Revision — 2026-07-10 (third review pass): photo-personalized theming

Human feedback: **"once a parent uploads their kid's pics we should show
pictures in general theme so it looks personal. if no picture then
default theme."** This section specifies a decorative accent-layer system
that personalizes select surfaces from an uploaded profile photo, without
touching any structural/R1-load-bearing color, and defines the default
(no-photo) state as a complete theme in its own right rather than a
degraded placeholder. Read together with §1.3/§4.2 (the fixed palette)
and §1.9 (test rules — this revision adds UXR-13).

### 6.1 What gets personalized, and what stays fixed — and why

**Personalized (decorative accent layer only):**
- **Header/hero gradients** — the Today "this-week" card and (if a
  profile photo exists) the Journey header wash switch from the fixed
  coral/gold gradient to a gradient built from the child's extracted
  accent. This is the single highest-visibility surface a parent sees
  first, so it carries the most personalization weight.
- **Card accent borders** — a 4px left border on activity/memory cards
  picks up the accent as a quiet color-coding-free flourish (border color
  carries no meaning beyond "this is {name}'s space," same non-semantic
  role identity hues already play per §1.3's hard rules).
- **Background wash** on Today and Journey — a very light, fast-fading
  tint (see §6.3's tint token) behind the top of the scroll area only,
  fading back to the fixed cream within ~260px. It never becomes the
  page's actual background color; cream remains the base everywhere.
- **Child-switcher avatar ring** — a colored ring around each child's
  photo avatar, so the switcher itself previews each profile's theme
  (§6.4).

**Deliberately stays fixed, never personalized (rationale):**
- Tab bar active-state fill, primary button color, and links stay
  `--lm-terracotta` everywhere. Personalizing the *interactive/action*
  color would make "what's tappable" inconsistent across profiles and
  screens — a usability regression disguised as a personalization
  feature. Action color is product identity, not per-child decoration.
- Sage (supervision lines), gold (celebration), and identity hues
  (peach/sky/moss default dots) are untouched — they already carry
  established, tested non-semantic roles; overloading them with photo
  color would blur two different systems.
- The slate pediatrician-note surface, the single red destructive color,
  and all body/ink text — see §6.2, the hard constraint.

Rationale for this split: personalization should make the app *feel*
like it belongs to this specific child at the moments a parent is
scanning or celebrating (hero cards, cards, the switcher) — exactly
where INDUSTRY_KB's "emotional core" observation about the journey
applies — without becoming a second, uncontrolled color system that
competes with the tested action/status vocabulary the rest of this KB
depends on.

### 6.2 Hard constraint — what this feature is never allowed to touch

Non-negotiable, re-stated explicitly because a decorative feature that
consumes user-uploaded, unpredictable input is exactly the kind of change
that erodes a hard rule by accretion if not pinned down:

1. **`--lm-slate` (pediatrician-note surface, R1/R2) is never derived
   from a photo, never blended with a photo accent, and never
   theme-swapped per child.** It is one fixed hex value, everywhere,
   always. The pediatrician-note card's background, icon, and border are
   excluded from the personalization token set entirely — not "clamped
   to be similar to slate," structurally incapable of being anything
   other than the fixed token, the same way the Journey view is
   structurally incapable of rendering a norm axis (§1.6).
2. **`--lm-danger` (destructive-action red, UXR-9) is never derived from
   a photo.** One hex value, one meaning, everywhere. A dark, saturated
   red-toned extracted accent must never be allowed to visually rhyme
   with the destructive color — see §6.3's hue-exclusion band.
3. **Body/UI text and its contrast ratios are never affected.**
   `--lm-ink`, `--lm-ink-soft`, and any AA/AAA relationship documented in
   §1.3/§4.2 stays exactly as specified regardless of which child or
   photo is active. No extracted color is ever used as a text color, and
   no extracted color ever sits *directly* behind body copy (§6.3's rule
   4).

### 6.3 How AA contrast is guaranteed for an arbitrary uploaded photo

The extraction algorithm itself is Architecture's to design (not
specified here); what follows is the **visual outcome and safety
contract** the algorithm must satisfy, stated in design terms:

1. **Extraction target:** one dominant, personality-carrying accent hue
   from the photo (e.g., the most prominent non-skin-tone, non-neutral
   color — a blanket, an outfit, a toy, ambient light) — not an average
   of the whole image (averaging tends toward a muddy gray/brown that
   reads as "no color" and defeats the point). The visual goal is "this
   looks like it belongs to this specific photo," the same instinct
   behind Spotify/Apple Music's per-album extracted-color players — a
   familiar, trusted pattern for exactly this decorative purpose.
2. **Clamped safe band (three derived tokens, one hue, three lightness/
   saturation bands):**
   - `--lm-photo-mid` — decorative fills/borders/rings only, never
     behind text. Saturation clamped 30–55%, lightness clamped 45–60%.
   - `--lm-photo-deep` — the base for any gradient that will carry
     white headline text. Saturation clamped 35–60%, lightness clamped
     **22–32%** (dark enough that white text is comfortably AA against
     it for the great majority of hues).
   - `--lm-photo-tint` — background wash only, ink text may sit on it.
     Saturation clamped 18–28%, lightness clamped **90–94%** (close
     enough to cream that `--lm-ink`'s existing 11.9:1 relationship is
     essentially undisturbed at any hue).
   - **Hue exclusion band:** if the extracted hue falls within ±20° of
     `--lm-danger`'s hue or renders visually as red/amber at typical
     saturation (mirroring UXR-2's existing red/amber detection logic),
     the system shifts the hue by a fixed rotation (e.g. +40°) before
     clamping, so a red baby blanket can never produce an accent that
     rhymes with the destructive color.
3. **Why clamping lightness/saturation alone is necessary but not
   sufficient — the fixed-scrim requirement:** contrast at a given
   lightness varies by hue (a clamped yellow reads visually lighter than
   a clamped blue at the identical L value in HSL space), so a lightness
   band is a strong constraint but not a mathematical guarantee across
   every possible hue. Therefore, **any surface where fixed-color text
   (white) sits on top of a `--lm-photo-deep` gradient must also
   composite a fixed-opacity dark scrim** (a `black, 5%→45% opacity`
   gradient, independent of the extracted hue) **behind the text zone**
   — the today-photo-personalized mockup (§6.6) implements this exactly.
   The scrim is the actual guarantee; the clamped band just keeps the
   scrim from having to work as hard (and keeps the un-scrimmed parts of
   the gradient from looking muddy).
4. **Automated pre-render check + graceful fallback (the real
   guarantee, not a hope):** before any photo-personalized surface
   renders for a given child, the computed final contrast (extracted +
   clamped + scrim, as applicable) is checked against the ≥4.5:1 (body)
   / ≥3:1 (large text) WCAG thresholds. If a fixture photo somehow still
   fails after clamping and scrimming (the honest edge case — e.g. an
   unusual monochrome image), **that surface renders the fixed default
   theme for that child instead of an unchecked accent.** Personalization
   degrades to default, never to a contrast violation. This is UXR-13(a)
   at the Test gate (§1.9).
5. **Extracted color is never used as a text color and never sits
   directly behind body copy** — only behind large, deliberately-scrimmed
   headline text (rule 3) or not behind text at all (borders, rings,
   thin decorative washes). This is a standing rule for every future
   surface this system touches, not just the ones mocked up now.

### 6.4 Default/fallback state — a complete theme, not a placeholder

Every child profile starts here, and it is possible permanently if a
parent never uploads a photo (privacy-conscious parents are an expected,
respected use case per the existing "private by default" posture in
§1.6/1.7 — declining to upload a photo must never feel like using a
degraded version of the product). Concretely: **no new tokens are
introduced for this state** — it is the existing, fully-designed rev-2
cream/terracotta/coral/sage/gold theme (§4.2), unchanged, rendering
exactly as every other mockup in this review already shows. The only
difference from a photo-personalized profile is which token set is
active — `--lm-photo-*` is simply absent, not replaced by gray/neutral
placeholder values. The child's avatar in this state shows the existing
fixed identity-hue letter mark (peach/sky/moss, §1.3), never a gray
silhouette or generic camera icon — consistent with how the switcher
already worked before this feature existed.

### 6.5 Multi-child handling — independent accents, previewed in the switcher

Each child's `--lm-photo-*` token set is derived from *that child's own*
photo and stored/scoped per-child — there is no shared or "family"
accent. A family with Maya (has a photo, dusty-rose accent), Theo (has a
photo, teal accent), and Sam (no photo yet, default identity hue) sees
three visually distinct rows in the switcher sheet, each previewing its
own state truthfully: a small "photo theme" chip on personalized rows, a
"default theme" chip on Sam's row (informational, not a nag to upload —
no upload prompt is injected into the switcher; that would work against
the privacy-respecting default in §6.4). Switching children swaps the
entire personalization token set atomically with the profile switch — a
parent should never see Maya's screen flash Theo's accent mid-transition.
UXR-13(c) tests that two fixtures produce independently different
computed accent values.

### 6.6 Preview mockups produced

Written to `projects/little-milestones/design-review/screens/personalization/`:

| File | Shows |
|---|---|
| `screens/personalization/today-photo-personalized.html` | Today screen for Maya (has an uploaded photo): dusty-rose accent on the hero gradient (with the fixed dark scrim behind the white headline), card accent borders, top background wash, avatar ring. Annotated with what's personalized vs. structurally fixed. |
| `screens/personalization/today-default-theme.html` | The identical Today screen composition for Sam (no photo yet): the unmodified rev-2 default theme, explicitly annotated as a complete theme, not a degraded placeholder, for direct visual contrast with the personalized version above. |
| `screens/personalization/child-switcher-personalized.html` | The switcher sheet with three children: Maya (dusty-rose photo theme), Theo (teal photo theme — a second, independently different accent), and Sam (default theme) — demonstrating per-child independence and the "photo theme"/"default theme" chip convention. |

`projects/little-milestones/design-review/index.html` gets a new
"Photo Personalization (rev. 4)" section linking all three, with a
strategy summary box (what's personalized / what's fixed / the AA
guarantee) at the top, matching the pattern already established for the
desktop section (§5.7).

### 6.7 DesignSync push (incremental, additive only)

Same project, `172e0c51-e31a-46e7-aedb-bead17b38868`. New plan finalized
covering exactly the 3 new paths under `screens/personalization/**`. No
existing path (foundations, components, journey, forms, trust, the
revision-2 `screens/*.html`, or the revision-3 `screens/desktop/*.html`)
was touched, overwritten, or deleted, per this tool's own
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

---

## 8. Revision — 2026-07-12: Increment 4 — profile avatars, Journey lightbox, Journey gallery (F14 + F15 + F16)

Source: `FEATURES.md`'s "Post-MVP roadmap, approved 2026-07-12" section —
F14, F15, and F16 bundled into one Experience Design pass because all
three touch the same screens/files (`ProfileSwitcher.tsx`,
`TodayScreen.tsx`, `JourneyScreen.tsx`, `globals.css`). Human-approved
scope, per FEATURES.md: "F14 + F15 + F16, bundled into one Experience
Design pass and one Code gate... Frontend-only, no new backend surface" —
§8.4 below flags one small qualification to that "no new backend surface"
framing, found during this pass, not assumed away.

### 8.1 F14 — Profile avatar display

**Problem:** the profile switcher shows a colored identity dot
(`.lm-identity-dot`, hue from a fixed 3-color rotation, or the photo's
extracted accent color as a *tint*, per the pre-existing §6.5 system);
Today's hero card and the Journey header show no identity mark at all.
None of the three surfaces show the child's actual uploaded photo, even
though a profile-level photo (`PhotoMeta` row with `memory_id=null`)
already exists once a parent uploads one.

**Design:** a shared `.lm-avatar` treatment — a circular, `object-fit:
cover` image — replaces the identity mark on all three surfaces when a
profile photo exists; the **exact existing** `.lm-identity-dot` render
(same color logic, same fallback hue rotation, same zero-photo default
theme story from §6.4) is the fallback, completely unchanged, when no
photo exists. This keeps the fallback contract identical to what's
already shipped and approved — F14 only adds a state on top of it, never
replaces or weakens it.

- **Switcher** (`ProfileSwitcher.tsx`): avatar renders inside the exact
  same 32px box `.lm-identity-dot` uses today, so row layout,
  spacing, and the existing `.lm-theme-chip` ("photo theme" / "default
  theme") label are all byte-for-byte unaffected. When a photo exists,
  the ring uses `photo_accent_deep` (the same ring convention already
  shipped on the identity dot's `boxShadow` — §6.5 unchanged, just now
  ringing a photo instead of a flat color).
- **Today header** (`TodayScreen.tsx`): new surface — the hero card
  currently shows no identity mark at all. A 44px avatar sits to the left
  of the "{name} is {age}" heading, inside `.lm-hero-card`. Because the
  hero card's own background is the personalized (or default)
  coral/gold-family gradient — a variable hue — the avatar's ring is a
  fixed translucent white (`rgba(255,255,255,.85)`), not an accent color,
  so it reads consistently regardless of which gradient sits behind it.
  Fallback state renders the identity dot at the same 44px size, same
  position.
- **Journey header** (`JourneyScreen.tsx`): new surface — centered above
  "The Story of {Name}", 56px, ring is the same cream mask-ring already
  used for river dots (UXD-1's `border: 3px solid var(--lm-cream)`
  convention), plus a soft drop shadow for definition against the light
  peach/tint gradient background. Fallback state: identity dot at the
  same 56px size, same centered position.
- **Load-failure fallback:** every avatar `<img>` gets an `onError`
  handler that swaps to the identity-dot render — a decrypt/serve failure
  degrades to the existing dot, never a broken-image icon.
- **Accessibility:** every avatar uses `alt=""` (decorative) — the
  child's name is already visible as adjacent text on all three surfaces,
  so a real `alt` would be a redundant screen-reader announcement.

**Addendum (2026-07-12, human-reported):** §8.1 named `ProfileSwitcher.tsx`,
`TodayScreen.tsx`, and `JourneyScreen.tsx` (plus §8.1a's Settings control)
as the surfaces migrated to `Avatar`. Judgment call 3 in
`PROJECT_CONTEXT.md`'s Increment-4 summary left `app/page.tsx`'s own
sidebar and mobile-header switcher-*trigger* buttons unmigrated,
reasoning they were "a different affordance" — flagged there as a guard
against unstated scope, not a deliberate design decision that they should
look different. The human confirmed by screenshot this reads as a visible
break of "one child, one avatar everywhere": both trigger buttons sit
directly beside the Today hero card's real avatar and still show the flat
dot. Corrected: these two buttons ARE switcher rows (the always-visible
trigger variant, not a new context), so they get the exact same `Avatar`
treatment and `photo_accent_deep` ring convention as `ProfileSwitcher.tsx`'s
internal rows — sidebar at 32px (matching the base `.lm-identity-dot`
size), mobile header at 24px (matching its existing inline-sized
footprint). No new ring convention, no new fallback behavior — this
closes the gap rather than reopening §8.1's scope.

#### 8.1a — Closing the gap: an actual upload affordance (added 2026-07-12)

**Problem, confirmed by inspection:** §8.1 above specifies how a profile
photo *displays* once one exists, but no screen anywhere lets a parent
create one at the profile level. `uploadPhoto(profileId, file, memoryId?)`
(`lib/api.ts`) already supports a `memory_id`-less call — the backend needs
nothing new — but the only caller in the app, `AddMemoryForm.tsx`, always
passes a `memory_id`. Human-confirmed: this affordance folds into F14's
scope, not a separate feature.

**Where it lives — Settings only, this pass.** A new "Profile photo"
`.lm-card` section at the **top** of `SettingsScreen.tsx`, above the
existing "Your family" card, scoped to the **currently-selected child**
(`app/page.tsx` already holds `selected: Profile` in scope where
`<SettingsScreen>` renders — add a `profile: Profile` prop there, same as
`TodayScreen`/`ChatScreen`/`JourneyScreen` already receive). A one-line
subtitle, "For {profile.display_name}," makes the per-child scope explicit
since the rest of Settings today is family-scoped, not child-scoped —
without that line a parent could reasonably assume a family-wide setting.
**Onboarding's "ready" screen is not extended this pass** — Settings-only
is sufficient scope for a single small affordance; the ready screen is a
short, linear, one-CTA-forward flow (§5.2's onboarding-stays-narrow
reasoning applies here too), and adding an optional second CTA there would
mean building and testing two entry points into the same upload logic for
one small feature. If usage data later shows parents want it at first-run,
that's a follow-up, named here rather than silently decided.

**The control — reuses `AddMemoryForm.tsx`'s exact file-input pattern, not
a new picker.** Same hidden `<input type="file"
accept="image/jpeg,image/png,image/webp,image/heic" />` behind a clickable
element (there, an `.lm-ptile-add` tile; here, a visible `.lm-btn
lm-btn-secondary` button labeled **"Change photo"** when a photo already
exists or **"Add photo"** when it doesn't — copied language pattern from
the tag-chip / add-photo affordances already in that form). Layout: the
existing `.lm-avatar` (photo) / `.lm-identity-dot` (fallback) element at
72px, left of the button, in a flex row — the exact same fallback contract
§8.1 already specifies (same color logic, same "complete theme, not a
placeholder" story from §6.4), just a new size for this one screen (join
the switcher's 32px, Today's 44px, and Journey's 56px as a fourth,
documented size). No crop/reposition UI this pass — the existing
`object-fit: cover` circle mask is the only treatment, matching how every
other avatar surface in the app already handles arbitrary source photos.

**Behavior — upload on selection, no separate "Save" step**, matching this
KB's standing "friction ≈ 0" ethos for photo actions (§1.6 Flow 2a/2c):
choosing a file immediately calls `uploadPhoto(profile.id, file)` (no
`memory_id`). While the request is in flight, the button reads "Uploading…"
and is disabled (same `submitting`-state pattern already used for
`AddMemoryForm`'s save button and `SettingsScreen`'s own digest toggle);
the avatar preview optimistically shows the local
`URL.createObjectURL(file)` image immediately on selection, then swaps to
the real served photo once the response resolves. On success, the parent
shell's profile state updates in place (no full page reload) — see the
data-plumbing note below. No toast/confirmation banner beyond the avatar
itself visibly updating; that visual change *is* the confirmation, the
same "the moment lands" principle §1.6 already uses for memory saves, just
without the settle-animation (this is a settings action, not a journey
moment).

**Errors:** identical treatment to every other error surface in this file
— a `role="alert"` paragraph in `--lm-terracotta-deep`, rendering
`err.message` from the `ApiError` thrown by `uploadPhoto` (already routed
through `parseErrorMessage`, so this needs no new copy, no raw HTTP text
ever surfaces) — same pattern as `SettingsScreen`'s existing
`inviteError`/`digestError` state and `AddMemoryForm`'s own upload-failure
message. A failed upload leaves the previous avatar state exactly as it
was (no silent partial state); the optimistic local preview reverts to the
last-known-good state (existing photo, or the fallback dot) on failure.

**Privacy cue:** the same verbatim line UXR-10 already requires "at the
upload control" wherever one exists — "Photos stay private to your family.
Never public, never used for AI, never scanned for faces." with the lock
glyph — sits directly under the control. This is not a new copy decision;
it's the existing requirement extending to a new upload control, so no new
UXR is needed, though the UXR-10 test assertion's location list should be
understood as now including this Settings section.

**Out of scope, named rather than silently dropped:** no "remove photo"
control this pass (a natural follow-on once there's a delete affordance
question to design — deleting a profile's *only* avatar photo has a
slightly different feel than deleting one of many memory photos, worth its
own small pass rather than bolting on now); no crop/zoom/reposition; no
onboarding-flow entry point (see above). None of these block F14's own
display logic, which already has its own documented fallback for the
zero-photo state.

**Data-plumbing dependency — reinforces, doesn't duplicate, §8.4's flagged
gap:** displaying "a photo already exists" on page load (to decide
Change-photo vs. Add-photo copy, and to render the existing `.lm-avatar`)
needs the same `avatar_photo_id` field on `Profile` that §8.4 already
flagged as missing from the backend response. The upload action itself
needs nothing new (`uploadPhoto` works today), but this section's *read*
side depends on that same fix landing — one more reason to resolve §8.4
before code-agent builds F14, not a second, independent gap.

### 8.2 F15 — Journey image lightbox

**Problem:** clicking a photo in the Journey timeline today does nothing
(the `<img>` isn't interactive at all). The task calls for expanding it
full-resolution in an on-screen overlay, not navigating away.

**Design:** every photo `<img>` (both `.lm-moment-banner` and
`.lm-moment-photos img`) gets wrapped in a new `.lm-photo-trigger`
`<button>` (visually inert — `all: unset` — so nothing about the existing
photo-banner treatment from §7 changes visually) that opens a full-screen
`.lm-lightbox-backdrop` overlay:

- **Layout:** a `position: fixed; inset: 0;` dark backdrop
  (`rgba(20,16,12,.88)`, deliberately much darker than the app's existing
  dialog/sheet backdrops since a photo needs real visual isolation to
  read as "full-resolution," not a form dialog) centers the image,
  capped at `max-height: 70vh` on mobile / `900px × 76vh` on desktop so a
  caption and safe dismiss margin stay visible without scrolling.
  Resolution is free: the lightbox reuses the exact same `photoUrl(profileId,
  photoId)` src already rendered as the thumbnail/banner — no new
  resize/thumbnail pipeline, and typically no extra network request at
  all, since the browser already has the thumbnail's identical URL
  cached. `crossOrigin="use-credentials"` carries over unchanged
  (SECURITY_KB §2.3 — no static mount, decrypt-on-serve, family-scoped
  route — is fully respected; the lightbox is a display-layer addition
  on top of the exact same authenticated fetch path).
- **Dismiss:** a visible 44×44px close button (always present, fixed to
  the viewport corner rather than the image, so it's reachable regardless
  of the photo's aspect ratio), the `Escape` key, and a click on the
  backdrop itself (`event.target === event.currentTarget`). Clicking the
  image or its caption never dismisses it.
- **Keyboard/focus-trap accessibility** (per FEATURES.md F14's explicit
  citation of "existing dialog patterns," i.e. the `.lm-dialog-backdrop`
  `role="dialog" aria-modal="true"` convention already shipped for
  `DeleteConfirmDialog`/the delete-moment dialog): the lightbox carries
  the same `role="dialog" aria-modal="true" aria-label="{title} photo"`.
  On open, focus moves to the close button; Tab/Shift+Tab stay trapped
  among the lightbox's own controls (close, and prev/next when a photo
  list has more than one entry). On close, focus returns to the
  `.lm-photo-trigger` button that opened it — a new requirement this
  pass introduces (photos weren't focusable/interactive before), not
  present in any existing dialog to copy verbatim, so it's specified
  explicitly here.
- **Multi-photo navigation:** when the seed photo list has more than one
  entry, `ArrowLeft`/`ArrowRight` (keyboard) and visible prev/next
  buttons (44×44px, sitting in the dark margin on desktop rather than
  overlapping the photo) move within it, with a small dot-indicator row
  in the caption. A single-photo list renders no nav controls at all.
- **Mobile vs. desktop:** the same component and behavior at both
  widths — only the image's max-size caps and nav-button placement
  change (see Layout above). Swipe-gesture navigation is noted as a
  nice-to-have, not required for this pass; arrow buttons/keyboard arrows
  are the required affordance everywhere.

### 8.3 F16 — Journey gallery view

**Problem:** the chronological river is the only way to browse Journey
photos; the task asks for a toggleable dense grid alternative, paired
with F15's lightbox.

**Design:**
- **Toggle:** a new `.lm-view-toggle` segmented pill control ("Timeline" /
  "Gallery") sits between the existing "+ Add a moment" button (position
  unchanged, always visible in both views) and the content it switches.
  Default view is Timeline (the existing first-open experience is
  unaffected); only one view renders at a time. The choice is client-only
  state for this pass, not persisted server-side per caregiver — a scoped
  simplification, named here rather than silently decided (same
  discipline this KB and PROJECT_CONTEXT.md's Decisions Log already apply
  to other judgment calls).
- **Content model:** the gallery flattens every `photo_ids` entry across
  every timeline memory (already fetched by the existing `getTimeline`
  call — no new API request) into one chronological list, same order the
  river presents them in. Tiles show bare photos only — no date/age
  labels, no hover-revealed metadata — which is a direct extension of
  UXR-1 (no norm axis, no comparison framing): a dense grid of photos
  alone carries no expected-vs-actual signal, the same discipline already
  applied to the river's chapter markers.
- **Grid:** `display: grid`, 3 columns on mobile, 5 columns at the app's
  existing ≥1024px breakpoint — reusing the exact column-count precedent
  already shipped for `.lm-photogrid` in the add-memory sheet (3 → 5,
  there stepped at 768px; here stepped at Journey's own 1024px
  breakpoint for consistency with the rest of Journey's desktop
  treatment) rather than inventing a new grid density convention.
- **Empty state:** a profile with memories but no photos yet shows its
  own calm message in the Gallery view ("No photos yet — add a moment
  with a photo to see it here."), independent of Timeline's existing
  empty-state message.
- **F15 pairing (the coherence requirement):** a gallery tile opens the
  exact same `<Lightbox>` component F15 designed — one component, two
  seed-list scopes. The timeline's own photo triggers scope prev/next to
  that one memory's photos; the gallery's tiles scope prev/next to every
  photo on the profile, in the same chronological order the grid itself
  uses. No second lightbox implementation, no divergent dismiss/focus
  behavior between the two entry points.
- **Accessibility:** the grid is a plain `<ul>` of `<button>`-wrapped
  images (native tab order; no custom grid-arrow-key navigation needed
  for this pass, since Tab already moves linearly through 9-30 tiles
  reasonably). Each tile's `aria-label` carries its parent memory's
  title, so a screen-reader user gets the same context a sighted user
  gets from the river's visible card text.

### 8.4 Flagged: a small backend data-exposure gap, found during this pass

FEATURES.md's F14 description and this task's brief both frame the
avatar work as "a display-layer change, not new backend work," reasoning
that `Profile.photo_accent_mid/deep/tint` and the profile-level
`PhotoMeta` row (`memory_id=null`) "already exist." Checked directly
against `dev/backend/app/routes/profiles.py`, `app/profiles.py`, and
`app/photos.py` for this pass: the accent *tokens* are indeed already on
the `Profile` response, but there is **no field or route that exposes
which `PhotoMeta.id` is the profile's own avatar photo** — no
`avatar_photo_id` on `Profile`, and no `GET /profiles/{id}/photos` list
route reachable from the switcher/header context. `PhotoStore
.list_for_profile()` exists server-side but nothing surfaces its result
(or just the `memory_id IS NULL` row within it) to the frontend today.

**This is a small, additive gap, not a scope-changing one** — no new
table, no new storage path, no new encryption surface, and it can be
closed with the same pattern already established for accent extraction:
add `avatar_photo_id: string | null` to the `Profile` response, sourced
as "most recent `photo_meta` row for this profile where `memory_id IS
NULL`" — the identical "last-successful-upload-wins" rule
`PhotoStore._set_profile_accent` already applies to the accent columns
(PROJECT_CONTEXT.md Decisions Log, 2026-07-11, judgment call 2, accepted
as a documented Increment-2 limitation). Because it's sourced from the
same row, `avatar_photo_id != null` and `photo_accent_mid != null` stay
in lockstep by construction — one photo, one accent, one avatar, no new
edge case to reason about. Full detail and the exact implementation note
is inline in `design-review/increment-4/avatar-treatment.html`.

**Flagged for solution-architect/human confirmation before code-agent
builds F14** — this pass does not silently fold it into "no new backend
work" as stated in FEATURES.md/the task brief, since checking the actual
routes showed that framing needs one small qualification.

### 8.5 Preview mockups produced (design-review artifact required before implementation)

Written to `projects/little-milestones/design-review/increment-4/`:

| File | Shows |
|---|---|
| `increment-4/avatar-treatment.html` | Switcher rows (photo avatar + accent ring vs. fallback dot), Today header (photo avatar vs. fallback dot, side by side), Journey header (photo avatar vs. fallback dot, side by side), and a desktop sidebar switcher variant — all using the real `--lm-*` tokens. Inline implementation note including the §8.4 backend-gap flag. |
| `increment-4/journey-lightbox.html` | The lightbox open over a single-photo memory on mobile (dimmed timeline visible behind) and over one photo of a multi-photo memory on desktop, with prev/next controls and a dot indicator. Inline implementation note covering the shared `<Lightbox>` component, dismiss/focus-trap behavior, and mobile-vs-desktop sizing. |
| `increment-4/journey-gallery.html` | The Timeline/Gallery toggle switched to Gallery: a 3-column grid on mobile, a 5-column grid on desktop with sidebar nav visible, plus a callout explaining the tile→lightbox handoff to F15's component. Inline implementation note covering toggle placement, content model, grid breakpoints, empty state, and accessibility. |

`design-review/index.html` gets a new "Increment 4 — Avatars, Lightbox,
Gallery" nav link and section (indigo `F14 / F15 / F16` badge, a new
color distinct from every prior revision's badge), with a strategy
summary box and an explicit flag box surfacing §8.4's backend gap and
§8.6's DesignSync gap. No existing section, nav link, card, or preview
file was removed, overwritten, or rewritten — purely additive, matching
this KB's established "never wholesale replace" convention (see §7.5 and
the file-integrity note at the top of this document).

### 8.6 DesignSync push — not performed this pass, flagged

Prior revisions in this KB (e.g. §7.5) record incremental DesignSync
pushes to this project's Claude Design component-library project
(`172e0c51-e31a-46e7-aedb-bead17b38868`). **This pass could not push to
DesignSync** — no DesignSync tool was available in this session's tool
set (this pass had Read/Write only). This is the same class of gap
PROJECT_CONTEXT.md's Decisions Log already records for other SME agents
in this project (e.g. "responsible-ai-architect has no shell/execution
tool"), not a silently skipped step. Flagged explicitly for whichever
future pass does have DesignSync access to push the three new
`increment-4/*.html` files, additively, alongside the existing pushed
paths — no existing path needs to change.

### 8.7 Coverage note (what this pass does and doesn't cover)

This pass covers F14 (avatar display), F15 (lightbox), and F16 (gallery
view) exactly as scoped in FEATURES.md's Increment 4 bundle — design
only (flows, layout, component states, the two flagged gaps above), no
backend or frontend code written. It does **not** cover F13 (chat
history + suggested prompts, scheduled as Increment 5, "needs a real
schema decision... plus its own Experience Design pass" per FEATURES.md)
or F12/F17 (later increments). It does not resolve §8.4's backend gap or
§8.6's DesignSync gap — both are handed off, not silently absorbed.
**Decisions Log cross-check (per this role's completeness guardrail):**
the full `PROJECT_CONTEXT.md` Decisions Log was read before finalizing
this pass, specifically re-confirming the 2026-07-10 "responsive web
app... real desktop layout" platform decision — every preview in this
section is shown at both mobile and a genuine ≥1024px desktop width
(sidebar nav, browser-chrome frame), not a stretched phone view, matching
that decision and this KB's own §5/§3 (rev-3) desktop-layout precedent.
No decision recorded since then bears on avatars/lightbox/gallery
specifically beyond what FEATURES.md's Increment 4 entry itself already
scopes.

## 9. Revision — 2026-07-12: Increment 5 — chat history + dynamic suggested prompts (F13)

Source: FEATURES.md's F13, human-approved 2026-07-12, sequenced as Increment 5
specifically because it needs a real schema decision (chat is currently
stateless server-side) plus its own Experience Design pass, separate from
Increment 4's F14/F15/F16 bundle. Two related but distinct pieces.

### 9.1 Historical chats — the UX, not the schema

**Model: discrete conversations, not one continuous log.** Matches the
app's existing "chaptered" idiom (Journey's chapter markers) better than
an infinite scroll — a caregiver scanning for "that time we talked about
walking" benefits from date-grouped chunks. A new History icon (clock
glyph, 2px-stroke line icon per §1.2's iconography rules) sits in the
existing `.lm-age-strip`, in the same position as the corrected-age "i"
affordance (both can coexist).

**Mobile:** tapping the icon opens the existing `.lm-sheet-backdrop`/
`.lm-sheet` bottom-sheet component (already shipped for `AddMemoryForm`
and the profile switcher — no new sheet pattern invented), titled
"{Name}'s conversations," with a pinned "+ New conversation" pill at top
and a list below.

**Desktop (≥1024px):** a new, screen-scoped 230px history rail sits
between the existing 248px nav sidebar and the 640px-capped chat column
(§5.3) — visible only on the Chat route. This is deliberately **not**
folded into the main nav sidebar, which §5.1 explicitly scopes to "nav +
identity, nothing else"; the rail is a separate, additive surface. It
uses the reclaimed horizontal margin space §5.3 previously filled with a
purely decorative wash — content there is not a regression of that
decision, since chat is the one screen that now has real content to put
there. Rows show hover-reveal delete (matching the existing desktop-hover
convention, UXR-6 extension) with `:focus-within` parity for keyboard
users, not hover-only.

**Row anatomy (both breakpoints):** relative date ("Today," "Yesterday,"
"Tue, Jul 8"), a **literal snippet of the parent's own first message** in
that conversation — never an AI-generated summary, no new
LLM-origination surface — and a message-count badge. Active/open
conversation gets a `--lm-blush` background tint (existing, non-meaning-
bearing surface, not a new color).

**Continuity default:** opening Chat resumes the most recent conversation
automatically, like returning to an open notebook. The dynamic
suggestion chips (§9.2) render only when the *currently open* conversation
has zero messages — the identical trigger condition `ChatScreen.tsx`
already uses (`messages.length === 0`), now scoped per-conversation
instead of per-app-load.

**Delete:** the existing two-button confirm-dialog pattern already used
for photo/memory delete — **not** profile-delete's heavier typed-
confirmation — since deleting one conversation is lower-stakes than
deleting a child's entire profile/photos/memories at once. Still the
single red surface (UXR-9). Copy: "Delete this conversation? This
permanently deletes every message in this conversation — immediately,
with no copies kept. This can't be undone."

**Retention:** no artificial cap on how far back a caregiver can browse
from the UX side — same "kept until the caregiver deletes it" discipline
already applied to memories/photos.

**Flagged for Architecture (not decided here):**
- Exact `chat_sessions`/`chat_messages` schema shape.
- The precise conversation-boundary staleness rule (explicit "+ New
  conversation" is settled; the implicit auto-new-conversation threshold
  — e.g. calendar-day boundary vs. an N-hour inactivity gap — is not).
- Whether the row snippet is a stored column or computed on read.
- Pagination/performance once a family has many stored conversations.
- **Flagged for Architecture + human explicitly, not UX's call alone:**
  does chat history scope per-profile (shared across all caregivers on
  that child, consistent with how memories/photos already work under
  F10) or per-(profile, caregiver)? This design's default recommendation
  is per-profile for scoping consistency, but chat content is more
  personal than a logged memory — a caregiver's own worried 2am
  questions being visible to a co-caregiver by default is a real privacy
  call this file does not make unilaterally.

### 9.2 Suggested prompts — dynamic, age/history-aware, never LLM-originated

Replaces `ChatScreen.tsx`'s static `SUGGESTION_CHIPS` (3 fixed generic
strings) with chips assembled from a **fixed, non-LLM template library**,
filled only with curated data already available server-side
(`milestones_cdc2022.json` bucket content, already served via
`/profiles/{id}/activities`) and the profile's own logged
`Memory.milestone_tag` values — the identical never-raw-LLM-origination
discipline already applied to F9's product-category cards. Renders in the
same empty-state slot as today (`messages.length === 0`), now scoped per
open conversation (§9.1).

**Template library (fixed, design-owned copy):**
- **T1 — current-stage:** `"Fun ways to build {domain_phrase} right now"`
  — `{domain_phrase}` from a fixed map of the current bucket's milestone
  `domain` field (movement→"strength & movement", language→"talking &
  sounds", social→"connection", cognitive→"curiosity"). Same activity-
  framing register as the existing "Ideas for rainy-day play" chip —
  never references a specific pass/fail milestone.
- **T2 — coming-next:** `"What's coming up around {next_bucket} months?"`
  — reuses the exact "invitation, never deadline" register already
  shipped for Today's "Things to look forward to" (§1.5d, UXR-8). Not
  shown once past the 36-month bucket (no next bucket to reference).
- **T3 — memory-tag extension:** `"More ideas building on '{tag}'"` —
  `{tag}` is the most recently logged memory's own `milestone_tag`, the
  parent's own words, truncated to ~30 chars with ellipsis (already
  capped at 60 chars server-side). Only shown if the profile has ≥1
  tagged memory. Celebratory extension of what the parent chose to log —
  never "is this on track," never a status/comparison word.
- **T4 — evergreen fallback:** the existing fixed pool ("Ideas for
  rainy-day play" / "What's a good first book?" / "Fun ways to build
  strength") — literal carry-over of today's static chips.

**Selection:** 3 chips shown — T1 + T2 + (T3 if available, else another
T4 pick). **Newborn/out-of-range mode:** T1/T2 have no meaningful bucket
to reference, so chips fall back to 2–3 T4 picks only, matching the
existing out-of-range context-strip tone already in `ChatScreen.tsx`.

**RESPONSIBLE_AI_KB R1/R2 compliance (this content is app-originated, so
the same boundaries as chat replies apply to prompt copy itself, per
RESPONSIBLE_AI_KB §3.1/§3.4):** no template contains or can be filled
with "behind," "ahead," "on track," "not on track," a percentile, or any
comparison word; T3's user-supplied `milestone_tag` text is rendered
as-is (the parent's own words) inside a fixed celebratory wrapper that
cannot turn it into an assessment claim, sanitized for display exactly
like every other rendered memory field in the app.

**Flagged for Architecture (not decided here):** whether this templating
runs as a small new backend endpoint (e.g. `GET
/profiles/{id}/suggested_prompts`, mirroring the existing
`/activities`/`/products` curated-table-plus-template pattern — the
recommended option, for the same centralization reason F9's catalog
filtering is server-side) or is computed client-side from data the
frontend already fetches. Implementation-symmetry decision, not visual.

### 9.3 Preview mockups produced (design-review artifact required before implementation)

Written to `projects/little-milestones/design-review/increment-5/`:

| File | Shows |
|---|---|
| `increment-5/suggested-prompts.html` | The fixed T1–T4 template table; mobile empty-state chat with dynamic chips (Maya, 12mo, has a "first steps" tagged memory); mobile newborn/out-of-range fallback (Theo, 3wk, evergreen-only chips); desktop rendering with sidebar nav, same dynamic chips. |
| `increment-5/chat-history-mobile.html` | History icon in the age strip; the "Past conversations" bottom sheet (active/inactive rows, snippet, count, delete affordance); the delete-confirmation dialog; the empty-history state. |
| `increment-5/chat-history-desktop.html` | The new 230px history rail between sidebar and chat column, hover-reveal delete, active-row highlight, callout explaining the one new structural desktop surface this pass adds. |
| `increment-5/index.html` | Assembles all three into one scrollable review page via embedded iframes, plus a "settled vs. flagged-for-Architecture" summary box. |

**Not linked from the root `design-review/index.html`** this pass — this
session had Write-only (no Edit) access to that existing file, and given
this project's two prior file-destruction incidents from careless `Write`
calls on large append-only files (this same KB, and `ARCHITECTURE_KB.md`
— see `admin/LESSONS.md`), the safer call was to leave the root index
untouched and flag the missing link as a follow-up for a pass with Edit
access, rather than risk a third incident. **DesignSync push also not
performed** — no DesignSync tool was available in this session's tool
set, same class of gap already on record at §8.6.

### 9.4 Coverage note (what this pass does and doesn't cover)

This pass covers F13 exactly as scoped in FEATURES.md's Increment 5 entry
— design only (flows, layout, the two flagged real Architecture/privacy-
scoping questions above), no backend or frontend code written. It does
not resolve the schema decision (explicitly Architecture's, per FEATURES.md
itself) or the DesignSync/root-index-link gaps flagged above — both are
handed off, not silently absorbed. **Decisions Log cross-check (per this
role's completeness guardrail):** the full `PROJECT_CONTEXT.md` Decisions
Log was read before finalizing this pass, re-confirming the responsive-
web-app platform decision — both mobile and a genuine ≥1024px desktop
layout are shown for every screen in this pass, not a stretched phone
view.

### 9.5 Addendum (2026-07-12) — page rename ("Chat" → "Ask") + infographic elements

Human approved §9's shared-per-profile chat-history design and added two
requests in the same breath: rename the Chat page to communicate its
actual value, and add infographic-style visual elements. Full proposal,
reasoning, and R1-compliance check in
`design-review/increment-5/chat-rename-infographics.html`.

**Rename: "Chat" → "Ask".** Evaluated against the human's two
suggestions: "Consult" is flagged as risky — it reads as "seek a
professional/medical consultation," directly in tension with
RESPONSIBLE_AI_KB §3.2's refusal boundary and the disclaimer's own "not
medical advice" sentence (§1.10), so a tab labeled "Consult" would set an
expectation the product has to walk back in nearly every reply.
"Discuss" is safe but weak — neutral, but names the mechanism (a
back-and-forth) rather than the value. "Ask" is recommended instead:
it's already the verb baked into this product's existing copy (the
onboarding CTA chip, the empty-state hint, the composer placeholder all
already say "Ask," never "Chat"), so the rename closes a gap between
what the app already calls this action and what the nav label calls the
destination, at zero new copy vocabulary and one syllable (matching the
existing one-word tab convention: Today · Journey · Add).

**Scope, explicitly bounded:** mobile tab-bar label and desktop sidebar
nav-item label change to "Ask" (icon unchanged); the route `<title>`
updates for consistency. Composer placeholder, empty-state hint,
onboarding CTA chip, and the history sheet/rail title ("{Name}'s
conversations") need **no change** — they already say "Ask"/
"conversations," not "Chat." Internal route path / component file name
(e.g. `ChatScreen.tsx`, `/chat`) is explicitly **out of scope** for this
design pass — a code-identifier decision left to code-agent/
Architecture, not silently assumed either way.

**Infographic elements — a new `.lm-stage-card`,** rendered in the same
empty-state slot as the suggested prompts (`messages.length === 0`),
bundling: an illustrated identity strip (child's avatar + name + age, in
the Journey header's serif register); an elapsed-time micro-line reusing
the Journey header's exact phrasing pattern ("342 days of Maya's story
so far ✦") — deliberately **text, not a ring/dial/fill-bar**, since even
an "elapsed time" bar risks being misread as a progress-toward-a-norm
indicator; a current-stage sentence built from the same domain-tag data
and template discipline as §9.2's T1 chip, rendered as prose instead of
a chip; and a row of four tappable domain icon chips (movement/language/
social/cognitive) that fire the same T1 template scoped to that domain.
All four domain chips always render at identical visual weight — no
filled/empty state, no checkmark, no graying-out of "domains not yet
reached" — since a completion-style visual was considered and explicitly
rejected as reproducing the comparison framing R1 bans. Suggested-prompt
chips (T1–T4) also gain matching domain icons. Two new 2px-stroke line
icons (speech-bubble for language, heart outline for social) are
proposed as additions to §1.2's approved motif list (leaves/sprout, sun/
moon, stars, footprints already cover movement/cognitive/coming-next) —
flagged explicitly as new, not silently added.

**R1 re-verification:** no element introduces an expected-vs-actual
visual, a progress-bar-against-norms, or a checklist with pass/fail
visual weight; every string is sourced from the same fixed, non-LLM
template library already cleared in §9.2 — this is a new visual
arrangement of already-approved data, not a new content-origination
surface.

**Preview:** `design-review/increment-5/chat-rename-infographics.html` —
renamed tab bar/sidebar, stage card, domain chips, and iconed suggestion
chips composed with the existing history rail/sheet and suggested-prompt
chips from this increment's earlier files, at both mobile (375px) and
desktop (≥1024px) widths.

## 10. Revision — 2026-07-12 (human feedback pass): nav icons restored + desktop density

Source: human live-testing feedback, two of four reported issues assigned to
this role. Preview: `design-review/increment-5/desktop-density-and-icons.html`.

### 10.1 Nav icons (Issue 2) — an approved-design regression, not a new design

The rev-2 mobile mockups (tab bar: 🏠 Today · 💬 Chat · ✦ Journey · ＋ Add)
and the human-approved rev-3 desktop sidebar (§5.1: "the same icon+label
pairing as the tab bar"; `screens/desktop/*.html`, 18px glyph in a 20px box,
12px gap) both specify icon+label navigation. The shipped `page.tsx` nav is
text-only at both breakpoints — a build-time omission of approved design,
now restored using the app's existing plain-character icon convention
(`lib/chatDisplay.ts` DOMAIN_ICONS precedent; no SVG icon set exists).

Spec — applies to BOTH the ≥1024px sidebar and the <1024px tab bar:
- Today: 🏠 (U+1F3E0) — approved rev 2/3.
- Ask: 💬 (U+1F4AC) — approved as Chat's icon; §9.5's rename kept it.
  Shared glyph with the language domain chip is accepted (both mean
  "speech"; always adjacent to a text label; different surfaces).
- Journey: ✦ (U+2726) — Journey's mark since §1.4; text glyph inherits the
  active terracotta.
- Settings: ⚙︎ (U+2699 U+FE0E, text presentation so it color-inherits like
  ✦) — NEW, flagged: Settings shipped in Increment 3 with no visual pass
  and never had an approved icon. Not on §1.2's banned-motif list.

Placement: `<span className="lm-nav-ic" aria-hidden="true">` before each
label. Sidebar: row-flex, `font-size:18px; width:20px; text-align:center`,
12px gap. Tab bar: column-flex, 18px icon stacked 2px above the existing
13px label. `aria-hidden` is required — the label remains the accessible
name (UXR-6); the glyph is never announced. Active-state styling unchanged.
Out of scope, noted: shipped sidebar pill says "+ Add a child" where the
rev-3 mockup showed "+ Add a moment" — pre-existing divergence, future pass.

### 10.2 Desktop density (Issue 4) — validated per screen, not blanket-widened

- **Ask — agreed, and a shipped bug.** No `.lm-content[data-screen="chat"]`
  override exists, so the generic 640px cap squeezes §9.1's 230px history
  rail + 20px gap + conversation into 640px, leaving ~390px of chat —
  narrower than mobile and contrary to §9.1's own "rail beside the 680px
  chat column" design. Fix: `.lm-content[data-screen="chat"]{max-width:930px}`
  at ≥1024px (230+20+680). `.lm-chat-column` stays 680px — §5.3's
  line-length/register reasoning re-affirmed, not relaxed.
- **Today — agreed at large screens.** 980px/2-col kept at 1024–1439px
  (§5.4's 3-col rejection was scoped to 980px content width and stands).
  New ≥1440px tier: `max-width:1200px`, `.lm-today-grid` 3 columns
  (~380px each — wider than the ~343px mobile card, so no compression);
  hero's `grid-column:1/-1` already spans.
- **Journey — mostly keep.** §5.5 re-affirmed: extra width must not become
  density on the narrative river (UXR-1's layout extension). Single change:
  760px → 860px at ≥1440px only (alternating cards ~352→~402px; the
  Gallery's 5-col tiles inherit ~145→~166px). Spine/dot offsets are
  relative — no recompute.
- **Settings — keep 680px**, re-confirming the Increment-3 recorded
  decision: a single-column form screen gains emptiness, not utility, from
  width (§5.2's reasoning applies verbatim).
- Fixed regardless of width: sidebar remains nav+identity only (§5.1);
  single-column mobile; every R1/UXR rule untouched.

### 10.3 Related same-pass fixes owned elsewhere (for the record)

The human's other two reported issues were fixed directly by the
orchestrator/code path in the same pass: (1) the Journey banner-photo
shrink — a regression from F15's `.lm-photo-trigger` wrapper breaking the
banner's negative-margin bleed, fixed by moving the bleed onto a new
`.lm-banner-trigger` wrapper class (§7's banner design itself unchanged);
(3) Ask now opens in new-conversation mode by explicit human direction,
superseding §9.1's original resume-most-recent default — continuing a
past conversation is now always an explicit choice from the history
sheet/rail (and names the session via an additive `ChatRequest.session_id`
so an older conversation can genuinely be continued, which the implicit
4-hour rule alone could not do).

### 10.4 Artifact, push, and coverage notes

Preview at `design-review/increment-5/desktop-density-and-icons.html`
(before/after renders + the exact CSS table for code-agent). DesignSync
push not performed (no tool available this session; same gap class as
§8.6/§9.3). Decisions Log cross-check performed in full before this pass:
the responsive-web-app platform decision and the §9.5 "Ask" rename are
both honored; this pass covers only the two assigned issues, with the
"+ Add a child/moment" label divergence flagged, not fixed.

## 10.5 Revision — 2026-07-12 (human feedback follow-up): fluid adaptive desktop, superseding §10.2's fixed tiers

Source: human live-testing feedback on the §10.2 pass — desktop must be
"adaptive to screen for all four tabs, based on content it should expand,
not grow too wide but look built for desktop." §10.2's discrete-breakpoint
caps (Today 980→1200px, Ask 930px, Journey 760→860px, Settings 680px) are
superseded by continuous, content-bounded rules. §10.2 is retained as the
historical record per this file's convention. Preview (real iframes at
1024/1440/1920 running the exact proposed CSS, plus the full change
table), human-approved: `design-review/increment-5/adaptive-desktop.html`.
**Implemented and shipped 2026-07-12.**

Per-tab strategy:
- **Today** — fluid grid: `repeat(auto-fit, minmax(300px, 1fr))`,
  container 1400px cap. 2 cols @1024 → 3 @~1440 (~347px, near-exactly the
  343px mobile card) → 4 @1920. §5.4's no-compression rule is now enforced
  structurally by the minmax floor instead of hand-picked column counts.
- **Ask** — the 680px `.lm-chat-column` reading measure stands (§5.3
  re-affirmed a third time, not relaxed). Adaptive = the frame: history
  rail `clamp(230px, 19vw, 280px)`; container `min(1080px, 100%)`
  (280 rail + 20 gap + 680 chat + 2×48 max side padding).
- **Journey** — split by view. Timeline: `clamp(760px, 62vw, 920px)` —
  continuous, hard-capped; UXR-1's layout-width discipline holds at any
  monitor. Gallery: breaks out to `min(1400px, 100%)` via
  `:has(.lm-gallery-grid)` with `repeat(auto-fit, minmax(160px, 1fr))`
  tiles (4/6/7 cols at 1024/1440/1920) — R1-safe to adapt aggressively
  precisely because it is a grid of bare photos with no norm semantics,
  not the narrative river.
- **Settings** — `clamp(680px, 58vw, 960px)` plus a new
  `.lm-settings-grid` wrapper (`repeat(auto-fit, minmax(330px, 1fr))`,
  `align-items:start`) around all four cards: one column @1024 (unchanged
  from the Increment-3 recorded decision at that width), 2-up from
  ~1440 — the "built for desktop" composition without a new visual
  language.
- **Global polish, calm register only**: side padding
  `clamp(16px, 3vw, 48px)`, card padding `clamp(20px, 1.4vw, 28px)`,
  body type `clamp(16px, 1vw + 3px, 17.5px)`. All three resolve to
  today's exact values below ~1300px viewports — zero mobile change. No
  parallax, no decoration, no new tokens.

Implementation: all 13 rows of the change table applied to
`dev/frontend/app/globals.css`, including deletion of the entire §10.2
`@media (min-width:1440px)` block (superseded, not layered) and one
markup change in `SettingsScreen.tsx` (all four cards wrapped in
`.lm-settings-grid`). tsc clean, 54/54 frontend tests unchanged. Fixed
regardless: sidebar 248px nav+identity (§5.1), every R1/UXR rule, all
fixed tokens, all <1024px behavior. `:has()` degrades gracefully
(Gallery stays at Timeline width in an unsupporting browser).

DesignSync: pushed this pass (plan `plan_172e0c51e31a46e7_ebc61a260070`,
additive, 9 files/cards) — including the previously-flagged §8.6/§9.3/
§10.4 backlog (all increment-4/5 previews), closing that standing gap.
Still open, re-flagged: root `design-review/index.html` links for
increment-4/5 sections (needs an Edit-access pass); the sidebar
"+ Add a child/moment" label divergence (§10.1).

## 11. Revision — 2026-07-12: Increment 6 — hardened auth suite (F12)

Source: `SECURITY_KB.md` §7 (2026-07-12), the human-approved F12 build.
Four UI surfaces flagged at §7's "what ui-ux-designer needs to design"
list. Preview: `design-review/increment-6/index.html` (assembles
`login-totp.html`, `forgot-password.html`, `settings-security.html`).

### 11.1 Login additions

A "Forgot password?" quiet link sits directly under the password field
(attached to that field, not floating below the primary button) on
`AuthScreen.tsx`'s login mode only. For TOTP-enrolled accounts
(`totp_verified_at` set, SECURITY_KB §7.3), a correct password reveals a
second step reusing `.lm-onboarding`/`.lm-field`: a 6-digit code entry
(large, monospace, centered) with "Verify," and a quiet "Use a recovery
code instead" link swapping the input for a text field. Error copy
matches the existing calm-terracotta convention exactly (never
`--lm-danger`, per UXR-9) and states remaining attempts factually ("That
code didn't work — 4 attempts left") rather than alarming. A wrong
password never distinguishes TOTP-enrolled from not (the TOTP step is
only reachable after password verification, preserving the existing
generic "invalid email or password" error for that failure mode). A
successful recovery-code login shows a one-time toast on entering the app
("Signed in with a recovery code — 7 codes left..."), reusing the
existing toast pattern.

### 11.2 Forgot-password flow

Four states, all reusing `.lm-onboarding`/`.lm-field`/`.lm-btn-primary`/
`.lm-btn-quiet` verbatim: (A) request — email entry; (B) "Check your
email" — copy is byte-identical whether the account exists, doesn't
exist, or the send failed server-side (SECURITY_KB §7.2's no-enumeration
rule); the email address echoed back is simply what the user typed, not
an account-existence signal; (C) reset — new password + confirm, reached
via the emailed token, with a generic "no longer valid" error for
expired/used/invalid tokens (no distinguishing detail); (D) success —
"Password updated... you've been signed out of every device," routing to
login.

**Functional (non-aesthetic) requirement on state C, carried from
SECURITY_KB §7.2:** the reset page must load no third-party resources
(no font CDN, no analytics, no external embed) and must strip the raw
token from the visible address bar via `history.replaceState` immediately
after reading it into component state, before the form renders — the same
Referer-leak discipline already required of the F8 unsubscribe
confirmation page (SECURITY_KB §1.7 point 5), applied here because a
password-reset token is materially more sensitive than an opt-out token.

### 11.3 Settings → Security section

A new "Security" `.lm-card`, placed inside the existing `.lm-settings-grid`
2-up desktop layout (§10.5) between "Weekly digest" and "Privacy."
Contains: change-password (inline expand: current/new/confirm fields);
two-step verification status (a sage "On"/neutral "Off" status chip —
sage reused from its existing non-gamified confirmation role, §1.3 — with
a secondary-button CTA when off, a quiet "Turn off" CTA plus a passive
"{n} recovery codes remaining" line when on); active-sessions list
(device/browser + last-seen, a sage "Current" tag on the active session,
per-row "Log out," and "Log out everywhere else").

**TOTP enrollment** is a 4-step flow reusing existing overlay patterns
exactly (sheet on mobile, centered dialog on desktop per §5.6's
established split, not a new pattern): (1) password-confirm dialog before
setup starts (SECURITY_KB §7.3); (2) QR code + "Can't scan? Enter this
code manually" monospace secret fallback, in an `.lm-sheet`; (3) 6-digit
verify-code step; (4) one-time recovery-codes display — 8 codes in a
2-column grid, a "Copy all codes" secondary button, and a **forced**
acknowledgment checkbox ("I've saved these recovery codes somewhere
safe") that gates "Done" — disabled until checked, not merely suggested,
since these codes are the only recovery path if both password and
authenticator are lost.

**TOTP disable** requires password + a current code in one dialog,
explicitly **not** styled as destructive (UXR-9 reserves `--lm-danger` for
permanent-data-loss confirmations; disabling MFA is a reversible setting
change, not data loss).

**Copy retirement (SECURITY_KB §7.2's "§1.3 status change"):** the
Privacy card's "No password reset yet — losing your password means losing
access..." sentence is removed outright, not replaced with compensating
copy — the capability it disclaimed now lives as real, discoverable
controls (the login "Forgot password?" link, the Settings "Change
password" control). Before/after shown in the preview.

### 11.4 Reused, unchanged (named explicitly, not silently assumed)

`.lm-sheet`/`.lm-sheet-backdrop`, `.lm-dialog`/`.lm-dialog-backdrop`,
`.lm-card`, all `.lm-btn` variants, `.lm-field`/input styles, the
calm-terracotta (never `--lm-danger`) error convention, the 44px
touch-target floor, and the sheet-on-mobile/centered-dialog-on-desktop
split already established for `AddMemoryForm`/photo-upload (§5.6). No new
component vocabulary is introduced anywhere in this increment.

### 11.5 Preview mockups produced

Written to `projects/little-milestones/design-review/increment-6/`:

| File | Shows |
|---|---|
| `login-totp.html` | Login form + "Forgot password?"; TOTP code step + error state; recovery-code fallback. Mobile + desktop. |
| `forgot-password.html` | Request, uniform check-your-email confirmation, reset (+ invalid-token error state), success. Mobile + desktop, with the token-leak/address-bar constraint annotated inline. |
| `settings-security.html` | Security card, not-enrolled and enrolled states (mobile + desktop with sidebar); full 4-step TOTP enrollment sheet/dialog flow incl. recovery codes with forced checkbox; disable dialog; active sessions; change-password form; Privacy-copy before/after. |
| `index.html` | Assembles all three via iframes, strategy summary, Decisions-Log cross-check note. |

### 11.6 DesignSync push — not performed this pass, flagged

Same gap class as §8.6/§9.3/§10.4: no DesignSync tool was available in
this session's tool set. Flagged for whichever future pass has DesignSync
access to push these three new paths additively to project
`172e0c51-e31a-46e7-aedb-bead17b38868` — no existing path needs to change.

### 11.7 Coverage note

This pass covers exactly the four UI surfaces SECURITY_KB §7 flagged
(login additions, forgot-password flow, Settings Security section, copy
retirement) plus the reset-page functional constraints. It does not
design any backend/token/schema behavior (security-architect's, per §7)
and does not touch F17 (deferred, later increment). Decisions Log
cross-check performed in full before finalizing — no recorded decision
since the last UX_KB pass changes anything about auth screens beyond
SECURITY_KB §7 itself; the responsive-web-app platform decision is
honored (every screen shown mobile + desktop, auth staying narrow/
centered per the established §5.2 split, Settings staying in the
sidebar+2-up-grid shell per §10.5).

## 12. Revision — 2026-07-12: Increment 7 — Google Photos import (F17)

Source: `FEATURES.md`'s F17, human-approved 2026-07-11, largest scope in
this roadmap — real OAuth/third-party integration, requiring solution-
architect + security-architect + responsible-ai-architect + industry-expert
sign-off before code starts (this pass is Experience Design only, ahead of
that sign-off). Preview: `design-review/increment-7/index.html` (assembles
`settings-entry.html`, `oauth-connect.html`, `picker-review.html`,
`import-results.html`).

### 12.1 Scope framing — one-shot connect/pick/import, not a persistent sync

FEATURES.md's F17 text does not imply ongoing library sync, so this pass
treats the feature as a deliberate, repeatable one-shot action: a
caregiver's OAuth *connection* may persist (so they aren't re-consenting
on Google's screen every time), but **no background sync, polling, or
automatic import ever runs**. Every import is an explicit "open picker →
pick → review → confirm" sequence the caregiver initiates. This is the
load-bearing scope decision the rest of §12 is built on — a persistent
connection with zero automatic behavior satisfies both "connect once,
use repeatedly" convenience and FEATURES.md's scope-minimization
constraint (INDUSTRY_KB §2.2), since nothing this app does with that
connection happens without a caregiver-initiated picker session.

### 12.2 Settings entry point

New "Google Photos" `.lm-card`, placed in the existing `.lm-settings-grid`
2-up desktop layout (§10.5) directly after the "Privacy" card — third-
party account linking sits in the privacy-adjacent group, not the
family/digest group. Scoped to the signed-in **caregiver's own** Google
account (not the family or a specific child) — any caregiver can connect
their own account and import into any child profile they already have
access to, under F10's existing caregiver permission model.

- **Not-connected state (default):** explains plainly and up front —
  read-only access, picker-based selection only, no library-wide access,
  off by default, no ongoing sync after import — before the caregiver
  ever clicks Connect. This is the first of two third-party-disclosure
  touchpoints (INDUSTRY_KB §2.2); the review step (§12.4) repeats the
  private-storage reassurance at the point of import itself.
- **Connected state:** shows the connected Google account email, an
  "Import photos" primary action, and a quiet "Disconnect" control. A
  neutral "Connected" chip (informational, not the sage security-posture
  chip §11.3 uses for TOTP — reused role but distinct meaning) plus a
  privacy-cue line restating that nothing syncs automatically.
- Both states carry the exact `.lm-privacy-note` lock-glyph pattern
  already established (§1.6 Flow 2c / UXR-10 / §8.1a).
- **Lapsed/externally-revoked connection** (ARCHITECTURE_KB §12.8's
  flagged gap — a caregiver revoked this app's access directly from their
  Google Account settings, outside this app, so a subsequent refresh
  attempt fails): renders as the plain **not-connected state**, copy
  unchanged — no separate "connection expired" messaging. A lapsed and a
  never-connected state are functionally identical from the caregiver's
  side (both require clicking Connect again), so a distinct copy
  treatment would add a state without adding useful information.

### 12.3 OAuth connect flow

**Full-page redirect, not a popup** — simpler and more transparent than a
popup this app would have to babysit for blocked-popup failures, and
matches how OAuth flows are legible to users generally. Clicking "Connect
Google Photos" shows a brief loading state on the button/screen ("Taking
you to Google…"), then navigates to Google's own hosted consent screen
(not styled by this app — shown in the mockup as a clearly labeled
approximation of Google's own UI, since this app has no control over it),
which redirects back to a fixed callback route on this app.

**Error states, all calm-terracotta, never `--lm-danger` (UXR-9), never
raw HTTP/OAuth error text:**
- **User cancels/denies consent** — "Connection wasn't completed —
  nothing was shared. You can try connecting again anytime." Framed as a
  normal, expected outcome for an optional off-by-default feature, not a
  fault.
- **Network failure during redirect** and **token exchange failure
  server-side** — both render the same generic "Something went wrong
  connecting — please try again," matching the existing
  `parseErrorMessage`/`AuthScreen.tsx` calm-error convention exactly (no
  differentiated copy that would leak which failure mode occurred, same
  discipline already applied to login errors).

**Disconnect** reuses the lighter two-button confirm-dialog pattern
already established for conversation delete (§9.1) — **not** the
destructive-red dialog (UXR-9 reserves `--lm-danger` for permanent
data-loss confirmations; disconnecting revokes access, it does not delete
already-imported photos). Copy explicitly reassures: "Photos you've
already imported into a child's journey stay exactly as they are —
nothing already imported is deleted."

### 12.4 Google Photos Picker flow — the one genuinely new component vocabulary in this pass

**Flagged explicitly, not fit into an existing pattern.** Google's own
Picker widget (launched via Google's Picker API) is a UI surface this app
does not, and by design should not, build a substitute for — this app
deliberately does not construct its own Google-library browsing view,
since that would require the library-wide access FEATURES.md's scope
minimization rules out. Everything on either side of the Picker is fully
native to this app's existing visual language:

- **Intro sheet/dialog** (before the Picker opens) — reuses `.lm-sheet`
  on mobile / centered `.lm-dialog` on desktop (§5.6 split) exactly.
  Copy primes the hand-off: "You'll pick photos in Google's own picker
  window next — we only ever receive the exact photos you select there."
- **The Picker itself** — out of this app's visual control; the mockup
  shows a labeled, illustrative approximation only (native-looking
  selection tiles, Google's own "Select" action), not a component spec.
  code-agent/Architecture should treat it as a black box this app
  launches and receives a selected-photo-id result from.
- **Import review step** (after the Picker closes) — reuses the exact
  photo-upload dialog/sheet treatment and `AddMemoryForm`'s 3→5 column
  photogrid precedent (§5.6) — no new grid convention. Contents:
  - A compact **child selector** row reusing the existing identity-dot +
    name pattern; tapping it opens the standard child-switcher sheet
    already shipped app-wide (no new picker component).
  - **Duplicate detection**: a photo whose content appears to match one
    already stored for the target child shows a slate "Looks like a
    duplicate" badge (the established non-alarm slate information-surface
    role, §1.3/UXR-2 — informational, never terracotta/danger) with a
    per-photo skip toggle, defaulting to skipped but fully overridable.
  - **Privacy reassurance**, extending the verbatim UXR-10 line with one
    added sentence naming the third-party source explicitly: "These will
    be stripped of location data and stored privately, same as every
    other photo here. This is a one-time copy from Google Photos into
    little-milestones' own encrypted storage — nothing keeps syncing, and
    your Google Photos library is never touched or deleted from." This is
    the second of the two third-party-disclosure touchpoints (§12.2 is
    the first).
  - Confirm button copy updates live with the selected count and disables
    at zero — never a silent no-op.

### 12.5 Import progress + results — partial failure shown honestly

The review dialog/sheet transitions in place (no close-and-reopen)
through: **in progress** (a progress bar + disabled "Importing…" button,
reusing the existing `submitting`-state disabled-button convention,
§8.1a) → a **results** state.

- **Full success** reuses the existing "the moment lands on the journey"
  settle payoff (§1.6 Flow 2a) — "Added to {Name}'s journey" phrasing and
  a small gold ✦ accent, extended from a single-memory save to a batch
  outcome rather than inventing new success language.
- **Partial failure** is shown per-photo, never swallowed: a summary line
  states the real count ("3 of 5 photos imported… 2 couldn't be
  imported"), each row shows a sage "Added" tag or a calm-terracotta
  "Couldn't import" tag with a scoped retry, and a "Retry both failed
  photos" secondary action re-attempts only the failed subset.
- **Full failure** (e.g., connection lost mid-batch) states the outcome
  factually and preserves the caregiver's selection for a retry, rather
  than discarding it.
- All error/status copy reuses the same sage-confirmation /
  calm-terracotta-error color roles already established everywhere else
  in this app (§1.3), applied per-row instead of per-form — no new color
  role introduced.

### 12.6 Reused, unchanged (named explicitly, per this KB's own convention)

`.lm-sheet`/`.lm-sheet-backdrop`, `.lm-dialog`/`.lm-dialog-backdrop` and
the sheet-on-mobile/dialog-on-desktop split (§5.6), all `.lm-btn`
variants, `.lm-settings-grid`/`.lm-card` (§10.5), the calm-terracotta
(never `--lm-danger`) error convention, the lighter two-button confirm
dialog (§9.1), the `.lm-privacy-note` lock-glyph pattern (§1.6/UXR-10/
§8.1a), `AddMemoryForm`'s 3→5 column photogrid precedent (§5.6), and the
existing child-switcher sheet. The one deliberate exception is named in
§12.4.

### 12.7 Preview mockups produced

Written to `projects/little-milestones/design-review/increment-7/`:

| File | Shows |
|---|---|
| `settings-entry.html` | Not-connected and connected states of the new "Google Photos" Settings card, mobile + inside the existing 2-up desktop grid. |
| `oauth-connect.html` | Connecting loading state; a labeled approximation of Google's own consent screen; all three error states (cancelled/network/token-exchange); the disconnect confirm dialog. Mobile + desktop. |
| `picker-review.html` | The intro hand-off sheet/dialog; a labeled, explicitly-flagged approximation of Google's Picker widget; the import-review sheet/dialog (child selector, duplicate badge + skip toggle, privacy reassurance, live confirm count). Mobile + desktop. |
| `import-results.html` | In-progress state; full success; partial failure (per-photo status + scoped retry); full failure. Mobile + desktop. |
| `index.html` | Assembles all four via iframes, strategy summary, and an explicit new-component-vocabulary flag box. |

### 12.8 DesignSync push — not performed this pass, flagged

Same gap class as §8.6/§9.3/§10.4/§11.6: no DesignSync tool was available
in this session's tool set (Read/Write only). Flagged for whichever
future pass has DesignSync access to push the four new
`increment-7/*.html` files additively to project
`172e0c51-e31a-46e7-aedb-bead17b38868` — no existing path needs to change.

### 12.9 Coverage note (what this pass does and doesn't cover)

This pass covers F17's UI/flow design only — screens, states, copy,
component reuse, and the one explicitly-flagged new-component-vocabulary
gap. It does **not** decide: the OAuth token storage/refresh mechanism,
the duplicate-detection hashing algorithm, backend routes/schema, rate
limiting, or any Google Photos/Picker API technical integration detail —
all explicitly solution-architect's/security-architect's, per FEATURES.md's
own note that F17 needs full Architecture + security-architect +
responsible-ai-architect + industry-expert sign-off before code starts.
**Decisions Log cross-check (per this role's completeness guardrail):**
the full `PROJECT_CONTEXT.md` Decisions Log was read before finalizing
this pass; the responsive-web-app platform decision is honored (every
screen shown mobile + desktop); nothing recorded since Increment 6 bears
on F17 specifically beyond FEATURES.md's own scope.

### 12.10 Test-gate verification (2026-07-13)

Verified against commit `0056069`'s implementation
(`GooglePhotosCard.tsx`, `GooglePhotosImportDialog.tsx`,
`SettingsScreen.tsx`, `page.tsx`, `globals.css`). Full per-item evidence
in this gate's chat transcript; summary below.

**Pass:** §12.2 settings entry point (both states, correct placement in
`.lm-settings-grid`) — minor deviation: "Import photos" ships as
`lm-btn-secondary`, not the primary action §12.2 calls for. §12.3 OAuth
error copy (calm-terracotta, never raw HTTP/OAuth text, matches spec
verbatim). §12.4 import-review mechanics (skip toggle, live confirm
count, privacy copy verbatim). §12.5 partial-failure honesty and scoped
retry. §12.6 no new component vocabulary beyond the one flagged Picker
exception. Accessibility basics. §12.2's lapsed-connection reuse of
plain not-connected copy (no distinct branch exists in the code).

**Real defects found, not fixed here:**
1. **Disconnect dialog renders destructive-red, contradicting §12.3.**
   `GooglePhotosCard.tsx`'s disconnect dialog uses `className="lm-dialog"`
   without the `lm-dialog-neutral` override `SecurityCard.tsx`'s
   TOTP-disable dialog correctly applies for the identical
   non-destructive case. `globals.css`'s unconditional
   `.lm-dialog h2 { color: var(--lm-danger) }` therefore colors
   "Disconnect Google Photos?" in the one red UXR-9 reserves for
   permanent data loss. Fix: add `lm-dialog-neutral` to that div's
   className.
2. **Duplicate badge and "Added" result tag don't carry the color roles
   §12.4/§12.5 specify.** Both reuse `.lm-theme-chip`
   (`color: var(--lm-ink-soft)`, no background) — a plain gray label
   originally designed for the switcher's "photo theme"/"default theme"
   preview — instead of, respectively, the slate informational surface
   (§12.4, matching `.lm-pediatrician-note`'s role) and a sage
   confirmatory tag (§12.5, matching the sage already used correctly
   elsewhere, e.g. `SecurityCard.tsx`'s password-success text). Not an
   alarm-color violation, but it flattens three visually-distinct
   states (duplicate-flag / added / skipped) into one identical gray
   chip, working against the deliberate color-semantics this KB
   otherwise treats as load-bearing.

Minor, non-blocking: the full-success "✦ Added to {Name}'s journey"
line renders unstyled instead of with the "small gold ✦ accent" §12.5
describes.

Not re-verified here (unchanged from §12.9's scope, still Architecture's):
OAuth token storage/refresh, duplicate-detection hashing, backend
routes/schema.
