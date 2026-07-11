# UX/Usability + Accessibility — Increment 3 Test Gate
**Date:** 2026-07-11
**Owner:** ui-ux-designer
**Scope:** F9 (`ProductsPanel.tsx`), F10 (`AuthScreen.tsx`, `SettingsScreen.tsx`), session-gating in `page.tsx`

## 0. Framing — design-review coverage check (done first, changes what this suite can be)

**Confirmed: no design mockup exists for auth/signup/login/join, Settings/invite, or the
product-recommendation panel.** Checked directly:
- `knowledge/UX_KB.md` §1.7 (Flow 3a/3b/3c) specifies exact **flow and copy** for all three
  surfaces, but §2 (DesignSync Status) and §4.3/§5.7/§6.6 (the three full-screen mockup
  passes: revision 2 "full screens," revision 3 "desktop," revision 4 "photo
  personalization") list only onboarding/chat/today/journey/photo-upload — never
  auth/settings/products.
- `design-review/index.html` has exactly four sections (Full Screens, Desktop, Photo
  Personalization, plus the original foundations/components nav) — no Auth, Settings, or
  Products section exists anywhere in the file.
- code-agent's own Increment 3 report flags this explicitly in-source
  (`AuthScreen.tsx` lines 7–15, `SettingsScreen.tsx` lines 7–10): "no design mockup exists
  for this screen... flagged here as a real design gap for ui-ux-designer to review, not a
  silent substitute for one."

**Conclusion: these are the first-ever implementations of these three screens with no
approved visual mockup to check against.** This is therefore **not** a design-match
review — it is a baseline sanity pass against UX_KB's general, screen-agnostic contracts
(§1.9 UXR rules, §1.3 hard color rules, §1.4 typography/44px floor, the Increment-2
h1-hidden/h2-visible convention). **Gap itself flagged as a finding below (non-blocking
for this gate, but real backlog item for ui-ux-designer).**

---

## Finding A — Design-review gap: F9/F10 screens never went through Experience Design visual review
**Severity: Non-blocking (process gap, not a shipped-code defect)**
**Evidence:** `knowledge/UX_KB.md` §1.7, §2, §4–§6; `design-review/index.html` (no
Auth/Settings/Products section); `dev/frontend/components/{AuthScreen,SettingsScreen}.tsx`
source comments confirming the gap.
**Action:** ui-ux-designer owes a follow-up Experience Design pass producing rendered
mockups for these three screens (mobile + desktop, per the project's binding responsive-web
platform decision — see Finding D) before/alongside this feature's next design revision.
Not a gate blocker because F9/F10 were plan-approved for this increment and the code
faithfully implements UX_KB's flow/copy spec even without a rendered mockup; a design
review can happen retroactively without blocking Test/Review/Deploy.

---

## 1. R1/R2 safety-language check — `SettingsScreen.tsx` digest toggle, `ProductsPanel.tsx`
**Severity: PASS, no finding**
**Evidence (source review):**
- `SettingsScreen.tsx` digest section copy: "A short weekly note — your child's age, a few
  ideas, and a memory prompt. Off unless you turn it on. One tap to stop anytime." No
  assessment/comparison/percentile/"on track"/"behind" language. Toggle is a plain
  checkbox, default state driven by `user.digest_opt_in` (defaults false server-side per
  Increment 3 summary), no pre-checked/nagging pattern.
- `ProductsPanel.tsx` renders only `title`, `why_this_age`, `safety_note` per item, framed
  with: "Just ideas keyed to {name}'s age — we don't sell anything or earn from these." No
  LLM-originated text in this component — `getProducts()` hits `/profiles/{id}/products`,
  a structural serve-time catalog filter (`app/products.py`), not a chat/LLM code path, per
  ARCHITECTURE_KB §7 and the Increment 3 summary. Confirmed clean: no assessment/percentile/
  comparison language anywhere in `data/products_catalog.json`'s curated copy either
  (spot-checked buckets 2/4/6/9/12 — all "why_this_age"/"safety_note" phrasing is
  informational, non-comparative).
**Verdict:** matches expectation — F9 is curated categories with safety notes, not
LLM-originated, and carries no R1/R2-relevant language. No finding.

## 2. `AuthScreen.tsx` — password field, error messaging, touch targets
**Severity: mixed — one blocking finding (2b), one non-blocking finding (2c), rest PASS**

### 2a. Password field type — PASS
`<input id="lm-password" type="password" ... minLength={8} required />` — correctly masked,
not a differential UX signal either way. No finding.

### 2b. Backend error differential — PASS (backend); **frontend error text quality — BLOCKING finding**
- **Backend (`routes/auth.py::login`) is correctly non-differential**: a single generic
  `401 "Invalid email or password"` for both unknown-email and wrong-password cases, and
  `verify_password` is always run (even against `DUMMY_PASSWORD_HASH` for an unknown email)
  specifically so response timing doesn't leak which case occurred — this matches
  SECURITY_KB §1.5 exactly. No per-field leak on the backend. **PASS.**
- **Frontend `lib/api.ts::request()` throws `ApiError` with `message = \`${status}
  ${statusText}: ${bodyText}\`` — the raw HTTP status line plus the raw JSON response body
  as literal text.** `AuthScreen.tsx`'s error paragraph renders `err.message` verbatim
  (`{error}` inside `<p role="alert">`). Concretely, a wrong-password login would render:
  `401 Unauthorized: {"detail":"Invalid email or password"}` — not the clean, calm sentence
  the backend intended — and any 422 validation error (e.g. a password under 8 characters
  submitted via a means that bypasses the HTML `minLength` attribute, or any other pydantic
  validation failure) would render FastAPI's raw validation-error JSON array
  (`422 Unprocessable Entity: {"detail":[{"type":"value_error","loc":["body","password"],
  "msg":"Value error, Password must be at least 8 characters",...}]}`) directly to the
  user. This is not a differential-per-field *security* leak (the content itself doesn't
  distinguish which credential was wrong), but it is a real, source-confirmed violation of
  UX_KB §1.2's "Voice in microcopy: second person, warm, plain language, short sentences"
  and §1.7 Flow 3b's explicit "Error copy is factual and calm" requirement — raw JSON/HTTP
  status text is neither calm nor plain-language, and it affects **every** error path on
  every auth screen (login, signup, join), not an edge case. Flagged **blocking** because
  it's the first thing many users will see on any credential mistake, on a brand-new
  first-time-user-facing screen, and it's a straightforward, mechanical parsing gap (`request()`
  should surface `body.detail` — string or first validation message — not the raw envelope).
  **Recommendation:** code-agent fix: parse JSON body for a `detail` field (string) in
  `request()`'s error path and fall back to a generic calm message ("Something went wrong —
  please try again.") when `detail` is absent or is the FastAPI validation-array shape.

### 2c. Touch targets — **BLOCKING finding: email/password inputs miss the 44px CSS rule entirely**
`globals.css`'s only touch-target/visual rule for `.lm-field` inputs is:
```css
.lm-field input[type="text"],
.lm-field input[type="date"],
.lm-field input[type="number"] {
  padding: 14px 16px;
  border-radius: 12px;
  border: 1px solid rgba(61, 56, 51, 0.2);
  font-size: 16px;
  min-height: 44px;
}
```
This selector list **does not include `input[type="email"]` or `input[type="password"]`.**
`AuthScreen.tsx`'s email field is `type="email"` and password field is `type="password"` —
both inside a `.lm-field` wrapper — so **neither gets the 44px `min-height`, the padding, the
border-radius, or the visual field styling every other text input in the app receives.**
They fall back to unstyled native browser input rendering, which is well under the 44px
floor in most browsers' default styling. This is the exact class of defect UXR-6 exists to
catch, is mechanically verifiable from source alone (a CSS selector omission, not a
runtime/rendering judgment call), and affects the two most-used fields on brand-new
first-run screens (signup and login, used by every single user). The join-code field
(`type="text"`) is unaffected — it's the only input in `AuthScreen.tsx` that happens to hit
an existing selector.
**Submit/mode-switch buttons — PASS:** `.lm-btn`/`.lm-btn-primary`/`.lm-btn-quiet` all carry
explicit `min-height: 44px` (and `min-width: 44px` for `.lm-btn-quiet`), confirmed in
`globals.css`. Submit ("Log in"/"Create account"/"Join family") and the three mode-switch
quiet buttons ("Already have an account?", etc.) are all compliant.
**Recommendation:** extend the CSS selector to include `input[type="email"], input[type="password"]`
(or better, drop the type-selector list in favor of `.lm-field input` unqualified, which
would also close this class of gap pre-emptively for any future field type).

## 3. Desktop layout — real treatment or missing (per this project's repeated pattern)
**Severity: BLOCKING finding — no desktop-specific layout for any of the three new screens**
Checked `globals.css`'s `@media (min-width: 1024px)` block (the project's established
desktop breakpoint, §5.1) for any rule targeting `AuthScreen`/`SettingsScreen`/
`ProductsPanel`'s markup (`.lm-onboarding`, `data-screen="settings"`,
`data-panel="ideas-for-this-stage"`): **none exist.** The 1024px media query only contains
rules for `.lm-tabbar`/`.lm-sidebar`/`.lm-mobile-header` (nav shell), `.lm-content[data-screen="today"]`,
`.lm-content[data-screen="journey"]`, and the journey river alternation — nothing for
onboarding/auth, settings, or the products panel.
- **`AuthScreen.tsx`** reuses `.lm-onboarding` (`max-width: 440px`, centered, no responsive
  rule) — this is actually **consistent** with §5.2's explicit decision that onboarding
  "stays centered at max-width 440–480px at every breakpoint, no sidebar" — so on inspection
  this is *not* a gap: it correctly inherits the one already-designed desktop treatment for
  this exact wrapper class. **No finding here** — flagged as checked, not skipped.
- **`SettingsScreen.tsx`** (`data-screen="settings"`) and **`ProductsPanel.tsx`**
  (rendered inside `.lm-today-grid`, which *does* get the 1024px 2-column grid rule since
  it's a sibling grid item alongside activity cards) need to be assessed separately:
  - `ProductsPanel`'s cards (`.lm-card`) render as direct children of `.lm-today-grid`,
    which **does** get `grid-template-columns: 1fr 1fr` at ≥1024px per the existing Today
    desktop rule (§5.4) — so product-idea cards **do** correctly pick up the 2-column
    desktop treatment automatically, with no code changes needed. **PASS, not a gap** —
    confirmed by re-reading `TodayScreen.tsx`: `<ProductsPanel profile={profile} />` is a
    grid-item sibling inside `.lm-today-grid`, same as activity/coming-next cards.
  - **`SettingsScreen.tsx` has a real gap**: it renders inside `.lm-content` (capped at the
    global default 640px at all breakpoints — `.lm-content[data-screen="settings"]` has no
    entry, so it doesn't inherit `today`'s 980px or `journey`'s 760px override) with three
    stacked `.lm-card` sections and no grid/column treatment at any width. This isn't
    necessarily *wrong* — a settings page reasonably stays single-column and narrow even on
    desktop — but per this project's own repeated finding pattern (3 prior missing-desktop
    catches this session across other screens) and given no design review ever confirmed
    this is the *intended* desktop treatment (as opposed to an unconsidered default), this
    is flagged as **blocking-adjacent**: not because single-column-at-640px is wrong, but
    because it was never a deliberate decision anyone can point to (unlike onboarding's
    §5.2, which explicitly confirms "stays narrow" as a considered choice). Recommend
    ui-ux-designer's follow-up pass (Finding A) explicitly confirm or revise Settings'
    desktop width as a stated decision, closing this the same way §5.2 closed onboarding's.
**Verdict:** Auth = confirmed correct (inherits existing decision). Products = confirmed
correct (inherits existing grid). **Settings = real gap, un-reviewed desktop treatment**,
downgraded from "missing" to "undecided" since single-column-narrow is plausible but
unconfirmed. Non-blocking for this gate (no user-facing breakage — the layout is
functional, just never deliberately reviewed), but should not recur a fourth time
uncaught.

## 4. Semantic structure — `<main>` landmark, heading hierarchy
**Severity: one non-blocking finding (SettingsScreen heading skip), rest PASS**
- **`<main>` landmark:** Present and correctly wraps all three screens.
  `AuthScreen`/`DisclaimerFooter` sit inside `<main>` in `page.tsx`'s unauthenticated
  branch (line 74); `SettingsScreen`/`ProductsPanel` (via `TodayScreen`) both render inside
  `<main className="lm-content" data-screen={screen}>` in the authenticated shell (line
  203). **PASS.**
- **`AuthScreen.tsx` heading:** Plain visible `<h1>` inside `.lm-onboarding` — this
  correctly matches the *pre-existing* convention already used by `OnboardingFlow.tsx`
  (also a visible `<h1>` in the same `.lm-onboarding` wrapper, styled via
  `.lm-onboarding h1` in `globals.css`), not the hidden-h1 convention used inside the
  authenticated app shell (Today/Chat/Journey/Settings). This is the right call — Auth and
  Onboarding are both standalone, chrome-less, single-purpose screens outside the tabbed
  shell, so a visible h1 (no competing nav landmark to announce first) is consistent, not a
  divergence. **PASS, no finding.**
- **`SettingsScreen.tsx` heading hierarchy — non-blocking finding:** `<h1
  className="lm-visually-hidden">Settings</h1>` followed immediately by three `<h3>`
  elements ("Your family", "Weekly digest", "Privacy") with **no `<h2>` anywhere on the
  screen.** This breaks the h1(hidden)→h2(visible, one)→h3(repeatable items) pattern
  established at the Increment-2 fix pass and followed correctly by both `JourneyScreen.tsx`
  (hidden h1 + one visible h2 "The Story of {Name}") and `TodayScreen.tsx` (hidden h1 + one
  visible h2 hero card + h3 activity cards). Skipping directly from h1 to h3 is a genuine
  heading-hierarchy skip (screen-reader users navigating by heading level lose the
  expected h2 waypoint). **Non-blocking** (doesn't break the landmark/announce contract,
  only the level-skip convention), but should be fixed alongside Finding A's design pass —
  simplest fix is promoting the three card headers to `<h2>` (no visible h2 needed on this
  screen the way Journey/Today have a hero) or adding one visible h2 ("Settings") to match
  the sibling screens' pattern exactly.
- **`ProductsPanel.tsx` heading:** `<h3>Ideas for this stage</h3>` — correctly a sibling
  h3 alongside `TodayScreen`'s other h3 cards (activity cards, "Things to look forward to"),
  under `TodayScreen`'s own single h2 hero. **PASS, no finding** — this is the one new
  Increment-3 heading that *does* follow the established pattern exactly, because it lives
  inside an existing, already-fixed screen rather than being a new top-level screen itself.

## 5. `ProductsPanel.tsx` — no brand names/tracking parameters (belt-and-suspenders)
**Severity: PASS, no finding**
Checked three layers, not just the rendered component:
1. **UI (`ProductsPanel.tsx`):** renders only `item.title`, `item.why_this_age`,
   `item.safety_note` — no field for brand/price/URL/tracking param exists in the JSX at
   all, so there's no code path that *could* render one even if the payload changed.
2. **Type contract (`lib/types.ts::ProductItem`):** `{ category, title, why_this_age,
   safety_note }` — no brand/price/url/tracking fields in the TypeScript interface either
   (matches the backend Pydantic model per the Increment 3 summary).
3. **Source data (`data/products_catalog.json`):** spot-checked five buckets (2/4/6/9/12
   months) — every item is `{category, title, why_this_age, safety_note}`, generic category
   labels ("high_contrast_board_books", "reach_and_grasp_toys," etc.), no brand/SKU names,
   no affiliate/tracking URLs, matching the file's own `_meta` block's stated constraint.
**Verdict:** clean at UI, type, and data layers — genuine belt-and-suspenders confirmation,
not just an absence-in-the-current-payload observation. No finding.

---

## Summary

| # | Finding | Severity | Screen |
|---|---|---|---|
| A | No design-review mockup ever produced for Auth/Settings/Products screens | Non-blocking (process gap) | Auth, Settings, Products |
| 2b | Frontend surfaces raw HTTP status + JSON error body verbatim instead of calm parsed copy | **Blocking** | Auth (all 3 modes) |
| 2c | `.lm-field` CSS touch-target/visual rule omits `input[type="email"]` and `input[type="password"]` | **Blocking** | Auth (email + password fields) |
| 3 | Settings has no reviewed/confirmed desktop treatment (functional but undecided, not literally missing) | Non-blocking | Settings |
| 4 | `SettingsScreen.tsx` skips h2, going h1(hidden)→h3 directly | Non-blocking | Settings |

**Not verifiable from source alone (flagged, not assumed passing):** actual computed
contrast ratios on rendered auth/settings/products surfaces, real tap-hit-testing of the
44px targets once CSS is fixed, and focus-trap/keyboard-order behavior across
`AuthScreen.tsx`'s three modes and `SettingsScreen.tsx`'s conditional invite-reveal flow —
no browser/rendering tool was available in this environment; these should be confirmed by
whichever agent/step next has live rendering (Playwright per PLAN §7-D/E's existing
convention, or a human pass).

## Gate verdict: **Changes requested (not a full block)**

Two blocking findings (2b, 2c) are both small, mechanical, source-level fixes (a CSS
selector addition and an error-body parsing fix in `lib/api.ts::request()`) — not
architectural or design-scope issues — recommended to route back to code-agent for a
quick fix pass before Review/Deploy, the same pattern as Increment 1's fix-pass findings
5–6 (non-blocking UXR-6 CSS fixes) upgraded here to blocking only because they land on
brand-new, first-use auth screens rather than an already-shipped surface. The three
non-blocking findings (A, 3, 4) do not need to gate Increment 3 and should be tracked for
ui-ux-designer's follow-up Experience Design pass on these three screens.
