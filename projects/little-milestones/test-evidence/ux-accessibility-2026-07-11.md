# UX / Accessibility Suite — Test Gate, Increment 1

**Project:** little-milestones
**Scope:** F1–F5 frontend (onboarding, chat, Today, profile switcher, responsive shell) built by code-agent 2026-07-10.
**Owner:** ui-ux-designer
**Method:** Code-level review of the real Next.js frontend against `knowledge/UX_KB.md` §1 (testable rules UXR-1–UXR-12, Increment-1-scoped subset only — UXR-1/7/10/11/12/13 are Increment 2+ scope, journey/photos/products/digest/personalization not built this increment, so not tested here) and against the Flow 1a–1d / §1.10 exact-copy spec.

**Execution note (honesty disclosure):** This session's tool set did not include a shell/Bash tool — only file Read/Write. I could not run `npm install`, `npm run build`, `npm run dev`, or Playwright to produce a live render or automated computed-style/DOM assertions. Everything below is a **thorough manual code-level review** of the actual component and CSS source in `dev/frontend/`, not a live-rendered or executed check. Contrast ratios and touch-target sizes are computed from the literal CSS values (hex math / declared px), not measured from a rendered DOM. Where the review requires live rendering to be conclusive (e.g. "Skip visible without scrolling" on a real 375×667 viewport), I've marked it UNVERIFIED rather than guessing pass/fail. This should be re-run with Playwright once a shell tool is available, per PLAN §7-D/E's own stated method.

Files reviewed: `dev/frontend/app/page.tsx`, `app/globals.css`, `app/layout.tsx`, `components/OnboardingFlow.tsx`, `components/ChatScreen.tsx`, `components/TodayScreen.tsx`, `components/ProfileSwitcher.tsx`, `components/DeleteConfirmDialog.tsx`, `components/DisclaimerFooter.tsx`, `dev/backend/app/routes/profiles.py`, `dev/backend/app/ages.py`, `dev/backend/app/milestones.py`, `dev/backend/app/data/milestones_cdc2022.json` (spot check).

---

## Summary

| Result | Count |
|---|---|
| PASS | 8 |
| FAIL | 6 |
| PARTIAL / gap | 3 |
| UNVERIFIED (needs live render) | 2 |

**Two findings are load-bearing and should block or be fixed before Increment 2 starts:**
1. **UXR-5 FAIL (both chat strip and switcher):** corrected age is not actually displayed anywhere — the backend collapses chronological + corrected age into a single number, so preterm children never see the "6 months (about 4 months corrected)" dual-age display the spec and this KB require.
2. **UXR-9 FAIL:** `--lm-danger` (the "one red surface" reserved for delete-confirmation dialogs) is used for ordinary error text in both the chat composer and the onboarding submit-error state — outside any destructive dialog.

---

## Scenario-by-scenario evidence

### 1. Onboarding — one-question-per-screen structure
**Rule:** UX_KB §1.4/§1.5 Flow 1a, "one question per screen."
**Evidence:** `OnboardingFlow.tsx` step machine: `welcome → name → birthday → born-early → weeks-early → ready`. Each `step === "..."` block renders exactly one focal question/decision (name input; DOB picker; born-early options; weeks stepper). No screen combines two unrelated questions.
**Result: PASS.**

### 2. Onboarding — exact sensitive prematurity-question copy (UXR-3)
**Rule:** UX_KB §1.10 exact string match.
**Evidence — `OnboardingFlow.tsx` lines 148–189:**
- Heading: `"Did {name} arrive earlier than expected?"` — **exact match.**
- Body: `"Babies born three or more weeks early grow on their own beautiful schedule. Telling us helps us use corrected age — the age pediatricians recommend for milestones in the first two years."` — **exact match** (em-styled "corrected age" preserved).
- Options in spec order: `"Arrived right on time (or close)"`, `"Yes, {name} came early"`, quiet link `"Skip this"` — **exact match, exact order.**
- Weeks-early screen: `"About how many weeks early?"` stepper 3–17 — **exact match**; corrected-age explainer `"{name}'s milestones will use corrected age until around age two. Their birthday is still their birthday."` — **exact match**; EI acknowledgment `"If {name} has a developmental diagnosis or is in early intervention, your care team's guidance comes first — general milestone info may not fit, and that's okay."` — **exact match.**
- Skip path: clicking "Skip this" calls `finish(false, null)` → Ready screen shows `"We'll assume {name} arrived full-term — you can change this anytime in {name}'s profile."` — **exact match.**
**Result: PASS** on copy fidelity. (Settings surface for changing this later doesn't exist yet — Increment 3 scope, correctly not built.)

**Skip-visibility sub-check:** spec requires "a Skip control is visible without scrolling." The Skip button (`lm-btn-quiet`) sits directly below the two option buttons with no other content between the question, options, and skip link — structurally this should fit above the fold on a 375×667 viewport, but I have no live render to confirm actual pixel layout after browser chrome/keyboard. **Result: UNVERIFIED (code structure supports it; needs live render).**

**Deviation noted (not a numbered UXR item, but a spec-fidelity gap):** the spec's Ready screen (§1.5 Flow 1a step 6) calls for "a single suggestion chip (‘Ask anything — try: what does a typical {age}-month-old enjoy?') routes into chat." The built Ready screen (`OnboardingFlow.tsx` line 238) instead renders static, non-interactive text — `"Ask anything — try: what does a typical age-appropriate day look like?"` — with no `{age}` interpolation and no tap-to-chat affordance. This is a real gap from the approved design, worth a code-agent follow-up, though not itself one of the pass/fail UXR-1–12 rules.

### 3. Onboarding — form-error styling uses the reserved destructive color (UXR-9)
**Rule:** "Destructive styling appears only inside delete-confirmation dialogs."
**Evidence:** `OnboardingFlow.tsx` line 214–218, the weeks-early step's `submitError` block:
```
{submitError && (
  <p role="alert" style={{ color: "var(--lm-danger)" }}>
    {submitError}
  </p>
)}
```
`--lm-danger` (`#A33B2E`, hue ≈6.7°, high saturation — unambiguously the reserved red) is applied to an ordinary "profile save failed, try again" message, outside any dialog. Compare: the DOB-validation error on the birthday step correctly uses `--lm-terracotta-deep` (the brand/action color family, not the reserved danger token) with "gentle inline copy, never a red toast" per §1.4 — the weeks-early step didn't follow that same pattern.
**Result: FAIL (UXR-9).**

### 4. Onboarding — touch targets on "quiet" buttons (UXR-6)
**Rule:** touch targets ≥44×44px, all flows keyboard/tap completable.
**Evidence:** `.lm-btn` sets `min-height: 44px` globally, but `.lm-btn-quiet` explicitly overrides it: `padding: 8px 4px; min-height: auto;` (`globals.css` lines 94–100). This class is used for: the onboarding **"Skip this"** link (a control on the flagged-sensitive screen), the **"Cancel"** button in onboarding and in the delete dialog, and the **"Remove"** button in the profile-switcher row. At `font-size: 16px`/`line-height: 1.6` (inherited from body), computed height is roughly 8px+8px padding + ~26px line box ≈ 42px — under the 44px floor, and several of these (Cancel, Remove) also have narrow horizontal padding (4px) that will put text-only labels under 44px width too.
**Result: FAIL (UXR-6)** — the touch-target floor is not honored for the entire `lm-btn-quiet` variant, which includes a control on the sensitive onboarding screen.

### 5. Chat — age-context strip shows corrected age for preterm profiles (UXR-5)
**Rule:** "For a preterm fixture, every UI location displaying age also displays corrected age... chat strip, switcher..." Spec exact format (§1.5 Flow 1c): `"{Name} · 6 months (about 4 months corrected)"`.
**Evidence:** `ChatScreen.tsx` line 79–81 builds `ageLabel` from `ageInfo.age_summary`, which comes straight from the backend `/profiles/{id}/activities` response. In `routes/profiles.py` lines 116–118:
```python
"age_summary": f"{ages.effective_months} months"
    + (" (corrected)" if ages.corrected_months is not None else ""),
```
`ages.effective_months` **is already the corrected value** when correction applies (see `ages.py` `compute_age`: `effective_months = raw_corrected` when `correction_eligible`). The API never returns `chronological_months` at all in this payload. So for a preterm child the chat strip renders something like **`"Maya · 4 months (corrected)"`** — showing only the corrected number, with no chronological age anywhere in the string. This is not the spec's dual-age display ("6 months (about 4 months corrected)") — it's a single number with a parenthetical label, and the chronological age a parent would recognize as "how old my baby actually is" is dropped entirely.
**Result: FAIL (UXR-5)**, chat-strip location. Root cause is backend (`routes/profiles.py`), not the frontend component — the frontend is faithfully rendering what the API gives it.

### 6. Profile switcher — corrected age display (UXR-5, switcher location)
**Evidence:** `ProfileSwitcher.tsx` `ageLine()` computes a **client-side chronological month count** from DOB only (not corrected), and appends the literal string `" (corrected age used)"` for `born_early` profiles (line 58) — no actual corrected-age number is shown, just a label saying correction is happening. This matches code-agent's own documented Judgment Call #7 ("a quick list label only... not corrected age"), but that judgment call directly conflicts with UXR-5's explicit text: "every UI location displaying age also displays corrected age... **switcher**..."
**Result: FAIL (UXR-5)**, switcher location — a real number is required, a label alone doesn't satisfy the rule as written.

### 7. Chat — pediatrician-note card styling (UXR-2)
**Rule:** slate, not red/amber; non-warning icon.
**Evidence:** `globals.css` `.lm-pediatrician-note`: `background: var(--lm-slate-tint)` (`#EEF3F8`), `border-left: 4px solid var(--lm-slate)` (`#3D6188`, hue ≈211° — unambiguously blue, nowhere near the <40° red/amber band), text color `var(--lm-ink)`. Icon used: `🗓️` (calendar), not a warning triangle/exclamation. `ChatScreen.tsx`'s `splitPediatricianNote()` correctly extracts only the sentence containing "pediatrician" into this card, leaving the rest of the reply in an ordinary assistant bubble — matches "presentation of the model's already-R1-compliant text, not new generated content."
**Result: PASS.**

### 8. Chat — network/API error message uses the reserved destructive color (UXR-2 / UXR-9)
**Evidence:** `ChatScreen.tsx` lines 146–150:
```
{error && (
  <p role="alert" style={{ color: "var(--lm-danger)" }}>
    {error}
  </p>
)}
```
Same issue as finding #3 — this renders on the **chat surface itself** (not a dialog) whenever `sendChatMessage` throws (e.g. a network failure). UXR-2 explicitly bans `--lm-danger` from the chat surface; UXR-9 explicitly restricts it to delete-confirmation dialogs.
**Result: FAIL (UXR-2, UXR-9).**

### 9. Chat — info-button touch target (UXR-6)
**Evidence:** `.lm-age-strip .lm-info-btn` (`globals.css` lines 318–328): `width: 20px; height: 20px;` — the corrected-age explainer "ⓘ" affordance is well under the 44×44px floor.
**Result: FAIL (UXR-6).**

### 10. Chat — suggestion chips (informational, not a numbered UXR)
**Evidence:** `SUGGESTION_CHIPS` in `ChatScreen.tsx` is a fixed 3-item array ("Ideas for rainy-day play", "What's a good first book?", "Fun ways to build strength"), not age-computed as §1.5 Flow 1c specifies ("3 age-computed suggestion chips"). None of the three is anxiety-priming, so the safety-relevant half of the rule holds, but the age-relevance half doesn't. Flagged as a follow-up, not a formal fail (no UXR number covers "must be age-computed" specifically).

### 11. Today — coming-next invitation framing (UXR-8)
**Evidence:** `routes/profiles.py` lines 106–114 generates: `"Around the {upcoming}-month mark, many little ones start exploring new things — here are ways to play along when you get there."` No "due/by now/should already/behind/on track" lexicon. `TodayScreen.tsx` renders it verbatim inside `.lm-coming-next` under the heading "Things to look forward to" — matches spec wording exactly.
**Result: PASS (UXR-8)**, on the surfaces built this increment (the "this-week" panel is F8 content, Increment 2, correctly not built).

### 12. Today — hero-card gradient color check (UXR-2)
**Evidence:** `.lm-hero-card` uses `linear-gradient(135deg, var(--lm-coral), var(--lm-gold))`. Computed hue for `--lm-gold` (`#E8A317`) ≈ 40.2°, saturation ≈82% — this sits *just* above the UXR-2 "<40°" threshold (i.e., technically passes the letter of the rule), but it is visually an amber/marigold tone on the Today surface. This matches the design intent in UX_KB §6.1 (coral/gold gradient is the specified default "this-week"-style hero treatment), so I'm not calling it a fail, but flagging that this is the one surface where the design's own color choice sits closest to the UXR-2 boundary — worth a second look with an actual rendered screenshot/color picker rather than hex math alone.
**Result: PASS (borderline; recommend live-render re-check).**

### 13. Today — supervision line uses sage, not a status color
**Evidence:** `.lm-supervision-note { color: var(--lm-sage); }` (`#2F7A4E`, green, hue far outside the red/amber band), rendered with a hand emoji (✋), not a checkmark/warning icon. Matches §1.5 Flow 1d card anatomy.
**Result: PASS.**

### 14. Profile delete — the one red surface, exact copy (UXR-9)
**Evidence:** `DeleteConfirmDialog.tsx` renders the exact §1.10 copy verbatim: `"Remove {name}'s profile?"` / `"This permanently deletes {name}'s profile, every memory, and every photo — immediately, with no copies kept. This can't be undone."` Confirm button (`lm-btn-destructive`, `--lm-danger` background) is `disabled={typed !== childName}` — a genuine typed-confirmation requirement, not a decorative disable. This is the only intentional, in-dialog use of `--lm-danger` in the codebase (excluding the two out-of-dialog leaks found in #3/#8 above).
**Result: PASS** on this specific dialog's own compliance — the dialog itself does exactly what UXR-9 requires. (The rule fails overall only because of the *other* two out-of-dialog usages documented above.)

### 15. Disclaimer footer (UXR-4)
**Evidence:** `DisclaimerFooter.tsx` renders the exact fixed disclaimer text (verbatim match to §1.10), with a plain-text-styled link to the CDC Milestone Tracker. `.lm-disclaimer` (`globals.css` lines 116–122): `font-size: 13px; color: var(--lm-ink-soft); background: var(--lm-cream);` — `--lm-ink-soft` (`#6E6259`) on `--lm-cream` (`#FDF8F2`) is the documented 5.4:1 ratio, ≥4.5:1 AA. It is rendered unconditionally inside `<main>` on the onboarding path and inside the main shell on every other screen (`page.tsx` lines 80, 170) — always in the DOM, never inside a modal/dialog, no "warning" text or iconography.
**Result: PASS.**

### 16. Responsive shell — 1024px sidebar/tab-bar swap actually exists in code (not just described)
**Evidence:** `globals.css` lines 175–222, a real `@media (min-width: 1024px)` block: hides `.lm-tabbar` and `.lm-mobile-header`, shows `.lm-sidebar` (`display: flex`, 248px fixed width, right hairline border), adds `:hover`/`[aria-current="page"]` styling to sidebar nav buttons, and widens `.lm-content[data-screen="today"]` to 980px. `page.tsx` renders both the `<aside className="lm-sidebar">` (lines 103–135, always in the DOM, CSS-hidden below 1024px) and the mobile header/tab-bar (always in the DOM, CSS-hidden at/above 1024px) — this is a real CSS breakpoint driving a real structural swap, not a stub or a comment.
**Result: PASS.** Today's grid also has a matching real breakpoint (`globals.css` lines 396–403: `grid-template-columns: 1fr` → `1fr 1fr` at 1024px, hero card spans both columns via `grid-column: 1 / -1`) — matches §5.4 exactly.

**Minor deviation noted:** §5.3 specifies the desktop chat column should be centered at up to 680px within the sidebar layout with decorative margin fill. The CSS does define `.lm-chat-column { max-width: 680px }`, but this is nested inside `.lm-content`, which caps at 640px for every screen except `data-screen="today"` — so in practice the chat column never actually reaches 680px; it's capped at 640px by its parent. Not a broken layout, just a smaller-than-specified effective width, and the decorative radial-wash margin treatment from the desktop mockup isn't implemented (arguably acceptable to defer — it was a "texture, not content" decorative detail, not a numbered UXR rule).

### 17. Desktop hover states (UXR-6, extended)
**Evidence:** Sidebar nav buttons have `:hover { background: var(--lm-blush); }` (line 208), `.lm-switcher-row:hover` also styled (line 294). However `.lm-chip` (the suggestion-chip component used in chat, and the closest thing to "tag chips" that exists this increment) has **no `:hover` rule** in `globals.css`.
**Result: PARTIAL** — the two structural nav elements the spec called out (sidebar items) are covered; the chip component is not.

### 18. Semantic structure (accessibility baseline)
**Evidence:** The onboarding path is wrapped in a real `<main>` landmark (`page.tsx` line 65), but the main app shell (Today/Chat, `page.tsx` lines 101–186) has **no `<main>` landmark** around `.lm-content` — it's a bare `<div className="lm-main-column">` → `<div className="lm-content">`. Additionally, neither `TodayScreen.tsx` nor `ChatScreen.tsx` renders a page-level `<h1>` (Today has an `<h2>` inside the hero card only; Chat has no heading at all) — a screen-reader user landing on either screen has no top-level landmark/heading announcing what screen they're on beyond the sidebar's `aria-current`.
**Result: FAIL (semantic structure)** — recommend code-agent add a `<main>` wrapper around `.lm-content` and a visually-de-emphasized (or visually-hidden, if the storybook heading register is meant to stay minimal) `<h1>` per screen.

### 19. Focus rings (UXR-6, keyboard completion)
**Evidence:** Explicit `--lm-terracotta` focus-visible rings exist only on `.lm-btn-primary` and `.lm-field input` (`globals.css` lines 83–86, 253–256). `.lm-btn-secondary`, `.lm-btn-quiet`, `.lm-option-btn`, `.lm-chip`, `.lm-switcher-row`, tab-bar buttons, and sidebar nav buttons have no custom `:focus-visible` rule and no `outline: none` reset either — so they should still receive the browser's default focus outline (nothing in this stylesheet strips it), meaning keyboard completion is very likely still functionally possible end-to-end.
**Result: PARTIAL** — functionally probably passes (no focus trap, no stripped outlines found), but does not fully match §1.4's "every flow keyboard-completable with visible focus rings (`--lm-terracotta` 2px offset outline)" — the branded ring treatment is incomplete, applied to 2 of ~8 interactive component classes. **UNVERIFIED** whether default browser outlines are visually sufficient without a live render (contrast of default `Highlight`/`-webkit-focus-ring-color` against `--lm-cream` background wasn't checked because it's not a value this codebase controls).

---

## Not tested (out of Increment-1 scope, confirmed against code-agent's own "not built this increment" list)
UXR-1 (journey DOM), UXR-7 (memory-logging friction), UXR-10 (photo privacy cue), UXR-11 (product cards), UXR-12 (digest toggle), UXR-13 (photo personalization) — F6/F7/F8/F9/F10 are not built in `dev/frontend/` or `dev/backend/app/routes/` (confirmed: only `profiles.py` and `chat.py` exist under `routes/`), consistent with PROJECT_CONTEXT.md's Increment 1 summary. No frontend code exists for these paths to review.

## Recommended follow-ups for code-agent (priority order)
1. **Backend `routes/profiles.py`**: return both `chronological_months`/`chronological_weeks` *and* `corrected_months` in the `/profiles/{id}/activities` payload, and update `age_summary` (or add a dedicated field) to the spec's dual format `"{chrono} months (about {corrected} months corrected)"`. This also unblocks a correct switcher display.
2. **`ProfileSwitcher.tsx`**: consume the corrected number from the (fixed) API instead of a client-side chronological-only estimate.
3. Replace `var(--lm-danger)` with `var(--lm-terracotta-deep)` (or another non-reserved token) in `ChatScreen.tsx`'s network-error paragraph and `OnboardingFlow.tsx`'s `submitError` paragraph.
4. Remove or raise `.lm-btn-quiet`'s `min-height: auto` override, and enlarge `.lm-info-btn` to 44×44px (padding/hit-area, not necessarily the visible 20px dot).
5. Wrap `.lm-content` in a `<main>` landmark in `page.tsx`, and add a per-screen heading (Today/Chat).
6. Add a `:hover` rule to `.lm-chip` for desktop parity with the sidebar/switcher hover treatment.
