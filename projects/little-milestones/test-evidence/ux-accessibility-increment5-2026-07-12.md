# UX/Accessibility Suite — Increment 5 (F13: chat history + dynamic suggested prompts + "Ask" rename/stage-card)

Owner: ui-ux-designer. Gate: Test. Date: 2026-07-12.
Method: **source-level review only** — no browser/Playwright tool available
in this session. Every scenario below is checked against the shipped code
(`dev/frontend/components/ChatScreen.tsx`, `dev/frontend/lib/chatDisplay.ts`,
`dev/frontend/app/globals.css`, `dev/frontend/app/page.tsx`,
`dev/backend/app/suggested_prompts.py`) and cross-checked against my own
spec, `knowledge/UX_KB.md` §9/§9.1/§9.2/§9.5. Anything that genuinely
requires a rendered browser (computed layout height, real contrast
rendering, hover/focus visual behavior) is labeled **UNVERIFIED (source-only)**
rather than asserted as passing from inference alone.

Legend: PASS / PASS (unverified-in-browser) / NON-BLOCKING FINDING / BLOCKING FINDING

---

## Scenario 1 — "Ask" rename

- Mobile tab-bar label: `app/page.tsx` line ~278, `<nav className="lm-tabbar">` button reads `Ask` (was `Chat`). **PASS**
- Desktop sidebar label: `app/page.tsx` line ~193, `<aside className="lm-sidebar"><nav>` button reads `Ask`. **PASS**
- Icon unchanged (no icon element added/removed on either button) — confirmed by diff-free surrounding markup. **PASS**
- Route/component naming explicitly left unchanged, per §9.5's stated scope boundary: `Screen` type still uses the literal `"chat"` value (`type Screen = "today" | "chat" | "journey" | "settings"`), `screen === "chat"` still gates `<ChatScreen profile={selected} />`, and the component file is still `ChatScreen.tsx`. No route path or component identifier was touched. **PASS**

**Verdict: PASS**, no findings.

---

## Scenario 2 — Suggested prompts: server-driven, static-pool-as-fallback-only, R1/R2 language check

- `ChatScreen.tsx`: `chips = suggestedPrompts && suggestedPrompts.prompts.length > 0 ? suggestedPrompts.prompts.map(p => p.text) : FALLBACK_CHIPS`. `FALLBACK_CHIPS` is only reached when the `getSuggestedPrompts` fetch hasn't resolved yet or resolved with an empty list (rejects are swallowed with `.catch(() => undefined)`, leaving `suggestedPrompts` null, same fallback path). No other code path substitutes the static pool over a real server response. **PASS**
- Comment at `FALLBACK_CHIPS`'s definition explicitly states the fixed T1–T4 library is "entirely server-generated" and this pool "covers the transient window before that fetch resolves, or if it fails outright" — matches the fetch-failure-fallback-only design intent. **PASS**
- R1/R2 language check, `dev/backend/app/suggested_prompts.py` (the actual source of every chip/sentence a real profile sees):
  - `DOMAIN_PHRASES` (T1 fill + stage-card domain-chip labels): "strength & movement" / "talking & sounds" / "connection" / "curiosity" — no comparison/status word. **PASS**
  - T1 text: `f"Fun ways to build {domain_phrase} right now"` — no comparison word. **PASS**
  - T2 text: `f"What's coming up around {upcoming} months?"` — invitation framing, matches UXR-8, no "due"/"behind"/"should already". **PASS**
  - T3 text: `f"More ideas building on '{_truncate_tag(tagged.milestone_tag)}'"` — the only user-supplied fragment is the parent's own `milestone_tag`, rendered as-is inside a fixed celebratory wrapper that cannot turn it into an assessment claim (matches §9.2's spec exactly). **PASS**
  - `EVERGREEN_PROMPTS` (T4, server-side and the identical client-side `FALLBACK_CHIPS` pool): "Ideas for rainy-day play" / "What's a good first book?" / "Fun ways to build strength" — no comparison word. **PASS**
  - `_stage_sentence_normal`: `f"{display_name} is exploring {domain_phrase} right now."` or, if no domain, `f"{display_name}'s story is unfolding one day at a time."` — no comparison word. **PASS**
  - `_STAGE_SENTENCE_NEWBORN` / `_STAGE_SENTENCE_OUT_OF_RANGE`: "…every day brings something new" / "…here's to many more moments" — no comparison word. **PASS**
  - Grep of the full file for "behind", "ahead", "on track", "not on track", "percentile", "%": zero matches anywhere in template strings. **PASS**

**Verdict: PASS**, no findings.

---

## Scenario 3 — Stage card anatomy and R1-safe domain-chip weighting

- **Identity strip:** `StageCard` renders `<Avatar profile={profile} size={44} .../>` + `<b>{profile.display_name}</b>` inside `.lm-stage-identity`. **NON-BLOCKING FINDING (spec deviation):** §9.5 specifies the identity strip as "child's avatar + name + **age**" (three elements) — the shipped strip renders avatar + name only; no age value appears anywhere inside `.lm-stage-identity` or `.lm-stage-elapsed`. The child's age *is* visible elsewhere on the same screen (the `.lm-age-strip` above the stage card already shows "{Name} · 14 months"), so this isn't a case of age being hidden from the parent, but the stage card itself doesn't carry the three-element strip as literally specified. Not R1/accessibility-affecting — flagging as a content-completeness gap for a follow-up pass, not a blocker.
- **Elapsed-time line — confirmed genuinely text, not a progress element:** `.lm-stage-elapsed` in `ChatScreen.tsx` renders `{daysOfStory(...)} days of {name}'s story so far ✦` as plain text inside a `<div>`. Grepped `globals.css` in full for any bar/ring/fill/progress-related rule scoped to `.lm-stage-*` — none exists; `.lm-stage-elapsed` (globals.css line ~536) is `font-size / color / font-weight` only, no `width`, no `background` gradient, no `border-radius` ring styling. **PASS**
- **Current-stage sentence:** `<p className="lm-stage-sentence">{prompts.current_stage_sentence}</p>` — server-sourced string, already language-checked in Scenario 2. **PASS**
- **Four domain chips, always equal visual weight:** `DOMAIN_ORDER.map(...)` in `ChatScreen.tsx` unconditionally renders all four (`movement`/`language`/`social`/`cognitive`) regardless of `prompts.current_domain`; the only per-chip attribute that varies is `aria-pressed={prompts.current_domain === domain}` (assistive-tech-only signal, not styling). Checked `.lm-domain-chip`'s full CSS rule in `globals.css` (lines 552–570): a single rule set, **no** `[aria-pressed="true"]` variant, no conditional class, no filled/graying-out treatment — unlike `.lm-option-btn[aria-pressed="true"]` and `.lm-tag-btn[aria-pressed="true"]` elsewhere in the same file, which *do* carry pressed-state styling, confirming this is a deliberate, verifiable exclusion for this component specifically. **PASS** — this is the load-bearing R1 check for this component and it holds.

**Verdict: PASS**, with one non-blocking content-completeness finding (missing age in the identity strip).

---

## Scenario 4 — History UI structural patterns

- **Clock icon in `.lm-age-strip`:** `ChatScreen.tsx` renders a `<button className="lm-info-btn lm-history-toggle">` containing a 🕐 glyph, placed inside the same `.lm-age-strip` div as the age text and the corrected-age "i" button. **PASS** (implementation note, non-blocking: the icon is a plain emoji character, not an SVG 2px-stroke line icon as §1.2's motif language would suggest — but this matches the app's own established icon convention everywhere else, per `chatDisplay.ts`'s own comment: "no SVG icon set exists in this codebase... all use plain characters for their icons." Consistent with existing precedent, not a new gap.)
- **Mobile sheet reuses existing `.lm-sheet-backdrop`/`.lm-sheet` pattern:** confirmed — `className="lm-sheet-backdrop lm-history-sheet-backdrop"` wraps a `.lm-sheet` div with the same grabber (`.lm-sheet-grabber`) used by `AddMemoryForm`. No new sheet CSS pattern introduced; `.lm-history-sheet-backdrop`'s only rule is `z-index: 60` (raising it above the base sheet z-index, a legitimate stacking-order addition, not a new pattern). **PASS**
- **Desktop rail is 230px, sits between sidebar and chat column:** `globals.css`: `.lm-history-rail { width: 230px; flex-shrink: 0; }` inside the `@media (min-width: 1024px)` block, and it's the first child of `.lm-chat-with-rail` (a flex row) ahead of `.lm-chat-main`. **PASS.** One doc-only inconsistency flagged, not a code bug: UX_KB §9.1's own prose says "the 640px-capped chat column," but the actual chat-column rule is `.lm-chat-column { max-width: 680px; }` (matching §5.3's original 680px spec, which §9.1 apparently mis-cited). The shipped code is internally consistent with §5.3; the discrepancy is in my own KB's §9.1 wording, corrected here as a note rather than a code finding.
- **Delete uses the 2-button confirm pattern, not typed-confirmation:** `ChatScreen.tsx`'s delete dialog is `.lm-dialog-backdrop`/`.lm-dialog` with exactly two buttons (`Cancel` / `Delete`), no text-input confirmation field — matches the memory/photo-delete pattern (verified identical structure in `JourneyScreen.tsx`'s own delete dialog), correctly *not* the profile-delete typed-name pattern. **PASS**
- **Delete copy matches exactly:** shipped text is `"Delete this conversation?"` (h2) + `"This permanently deletes every message in this conversation — immediately, with no copies kept. This can't be undone."` (body) — byte-for-byte match against §9.1's specified copy (apostrophe rendered via `&apos;`, em dash present). **PASS**

**Verdict: PASS**, no blocking findings (one documentation-only inconsistency noted, not a code issue).

---

## Scenario 5 — Row anatomy

- Relative date: `<span className="lm-history-row-date">{formatRelativeDate(session.last_message_at)}</span>`. `formatRelativeDate` in `chatDisplay.ts` returns "Today" / "Yesterday" / a `"Tue, Jul 8"`-shaped string, computed against the *caller's local* calendar day (not UTC) — matches spec. **PASS**
- Snippet: `<span className="lm-history-row-snippet">{session.snippet}</span>` — server-sourced literal snippet field, not client-computed. **PASS**
- Message count: `{session.message_count} message{session.message_count === 1 ? "" : "s"}` — correct singular/plural handling. **PASS**
- Hover-reveal delete on desktop with `:focus-within` parity: `globals.css` lines 662–669:
  ```
  @media (min-width: 1024px) {
    .lm-history-row-delete { opacity: 0; }
    .lm-history-row:hover .lm-history-row-delete,
    .lm-history-row:focus-within .lm-history-row-delete { opacity: 1; }
  }
  ```
  Both `:hover` and `:focus-within` selectors are present, not hover-only — a keyboard user tabbing to the delete button inside a row will reveal it via `:focus-within` even without a mouse. On mobile (below 1024px) the delete button has no `opacity:0` rule at all, so it's always visible there (correct — no hover concept on touch). **PASS**

**Verdict: PASS**, no findings.

---

## Scenario 6 — Touch targets (44px floor, UXR-6)

- **History row delete button:** `.lm-history-row-delete { width: 44px; min-width: 44px; ... }` — width is explicitly compliant. Height is **not** explicitly set; `.lm-history-row` has `align-items: stretch` (Note: this is the flexbox *default* value, but it's also written explicitly in the rule, confirming intent), so the delete button stretches to match the row's cross-axis height, which is set by its sibling `.lm-history-row-open` (padding `10px 12px` + three stacked text lines at 12px/13.5px/11.5px font sizes with inherited `line-height: 1.6`, plus `gap: 2px` — computes to roughly 80px+ by hand, well above 44px). **PASS (unverified-in-browser)** — the CSS reasoning supports compliance but actual rendered height depends on real font metrics I can't measure without a browser; flagging the reasoning rather than asserting a measured pass.
- **New-conversation button:** `.lm-history-new` composes with `.lm-btn` (`min-height: 44px`) in both the rail and the sheet. **PASS**
- **History toggle icon:** `.lm-history-toggle` composes with `.lm-info-btn` (`width: 44px; height: 44px`, explicit, not inferred). **PASS**

**Verdict: PASS**, with one item flagged unverified-in-browser (delete button height is CSS-inferred, not measured).

---

## Scenario 7 — Semantic structure

- **History sheet:** `<div className="lm-sheet-backdrop lm-history-sheet-backdrop" role="dialog" aria-modal="true" aria-label={`${profile.display_name}'s conversations`}>` — `role`, `aria-modal`, and a descriptive `aria-label` are all present. **PASS**
- **Delete confirm dialog:** `<div className="lm-dialog-backdrop" role="dialog" aria-modal="true">` — `role="dialog"` and `aria-modal="true"` are present, but **no `aria-label` or `aria-labelledby`** is set. **NON-BLOCKING FINDING:** this doesn't meet the letter of "appropriate `aria-label`" the task calls for. It is, however, **not a regression introduced by this pass** — the pre-existing memory-delete dialog in `JourneyScreen.tsx` (same `.lm-dialog-backdrop` pattern, used before F13 existed) has the identical gap (`role="dialog" aria-modal="true"`, no label), so this is an app-wide, pre-existing convention this feature correctly reused rather than a new defect. Recommended fix (either dialog): add `aria-labelledby` pointing at the `<h2>` already present as the dialog's first content (e.g. `id="delete-session-title"` on the `<h2>`, `aria-labelledby="delete-session-title"` on the backdrop) — cheap, no visual change, and would close the gap for both dialogs at once. Flagging for a future accessibility-hardening pass rather than blocking this gate on a pattern this feature didn't introduce.

**Verdict: PASS**, with one non-blocking, pre-existing-pattern finding (missing aria-label on the destructive-confirm dialog family, not unique to F13).

---

## Summary

| # | Scenario | Verdict |
|---|---|---|
| 1 | "Ask" rename + route/component naming untouched | PASS |
| 2 | Suggested prompts server-driven, R1/R2 language clean | PASS |
| 3 | Stage card anatomy + domain-chip equal weighting | PASS (1 non-blocking: age missing from identity strip) |
| 4 | History UI structural patterns (sheet/rail/delete pattern/copy) | PASS (1 doc-only inconsistency, not a code finding) |
| 5 | Row anatomy incl. `:hover`/`:focus-within` parity | PASS |
| 6 | Touch targets ≥44px | PASS (1 item unverified-in-browser) |
| 7 | Semantic structure (dialog roles/labels) | PASS (1 non-blocking, pre-existing pattern) |

**No blocking findings.**

Non-blocking findings to carry forward (none gate this pass):
1. `.lm-stage-identity` omits the child's age (spec'd in §9.5 as part of the three-element identity strip); age remains visible elsewhere on the same screen. Low priority — content-completeness only.
2. `.lm-dialog-backdrop` dialogs (both the new session-delete dialog and the pre-existing memory-delete dialog) lack `aria-label`/`aria-labelledby`. Pre-existing app-wide gap, not introduced by this pass — recommend a small follow-up wiring `aria-labelledby` to each dialog's existing `<h2>`.
3. UX_KB §9.1's own prose cites "640px-capped chat column" where the shipped/§5.3-specified value is 680px — a documentation correction, not a code defect.
4. History-row delete button's 44px height floor is inferred from CSS cascade (`align-items: stretch`) rather than measured in a browser — recommend a Playwright pass confirm the computed height once tooling is available.

## Gate verdict

**APPROVE.** The shipped F13 implementation matches my own §9/§9.1/§9.2/§9.5
spec on every load-bearing R1/R2, accessibility-baseline, and structural-
pattern check I could verify at the source level: the "Ask" rename is
correctly scoped, suggested prompts and the stage card are entirely
server/template-sourced with no comparison/status language anywhere in the
template library, the four domain chips are provably weight-equal in CSS
(no pressed-state styling exists to differentiate them), the history
sheet/rail/delete-dialog patterns correctly reuse existing shipped
components rather than inventing new ones, delete copy matches verbatim,
and touch targets meet the 44px floor everywhere I could confirm it from
CSS alone. The four items above are non-blocking and don't require
re-work before this gate closes; items 2 and 4 are worth a follow-up pass
once a browser/Playwright tool is available to this role, since several
assertions here (dialog announcement behavior, actual rendered heights,
live contrast) are reasoned from source rather than observed.
