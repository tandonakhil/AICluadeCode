# Semantic-law checklist — choose from these, do not inherit all of them

Each law below was earned by one project, solving one defect, and is tagged
with its origin and the defect it prevents. **This is a menu, not a
mandate.** A future project's Experience Design pass picks the laws that
apply to *its* product and states which it declined and why — exactly the
discipline `solution-architect`'s Reuse Decision Table already requires for
every accelerator (see `../ACCELERATOR.md` H2). Adopting a law without the
defect it addresses being real for your product is cargo-culting a rule out
of its context, which is the opposite of what this file is for.

---

## L1 · "There is no green" — origin: `conclave-finance-studio`

**The defect it prevents:** green reads as "fine, move on, no further
scrutiny required" — the one affect a depleted reviewer (11pm, day 3 of a
month-end close, fortieth item that night) must never be handed, because the
whole product exists to make a reviewer look harder at the thing most likely
to be wrong.

**How CFS enforces it — a check, not a convention.** `assert_no_green()`
(this accelerator's generalized `assert_no_hue_band()`, `src/enforcer.py`)
converts every declared colour token to HSL at import time of the chrome
module, and again as a unit test, and refuses any token whose hue falls in
band 75°–175° with chroma above a floor. **A green token is an `ImportError`,
not a review comment.** The band is deliberately wide — it reaches into teal
(175°) because a desaturated teal-green reads as "passed" exactly as readily
as a pure green does, which is why CFS's own brand action colour (`--teal`,
hue ~173°) was refused for use as this product's `accent` even though it is
the brand's primary interactive hue everywhere else in the portfolio. See
`../ACCELERATOR.md`'s worked example for the AA-contrast correction history
that accompanied this law.

**When this law does NOT apply.** A product where "this step succeeded" is a
true, low-stakes, non-scrutiny-suppressing fact — a form save confirmation,
a background sync completing — has no defect for this law to prevent, and
forcing neutral ink onto a genuine success confirmation would just be
CFS's house style worn as a costume.

---

## L2 · "Refusal is never styled as an error, and there is no affirmative
clearance" — origin: `rate-case-analyzer`

**The defect it prevents:** two distinct failure modes collapse into one.
(a) Rendering a refusal in error styling (red border, alert role, warning
glyph) teaches the user that the system "broke" when it in fact correctly
declined to assert something it could not substantiate — the opposite of
what should be reinforced. (b) A grounded-answer system that goes quiet when
nothing was found is read by a tired user as "checked, nothing wrong" —
**silence is not clearance**, and the UI must say so affirmatively.

**How RCA implements it.** `.refusal-panel` (`rca.css` §12) is explicit in
its own header comment: "Deliberately NOT error styling: neutral surface, no
red, no alert role, no warning glyph... same visual weight as an answer — a
refusal is a first-class outcome." Distinguished from an answer by a dashed
left rule and an explicit label, never by alarm colour. Separately, `.
coverage-none` (§10) is "deliberately NOT a bar" so a zero-population check
can never be mistaken, at a glance, for a full bar of clean results — the UI
never lets an absence of evidence render as if it were evidence of absence.
The one true system error (`.syserror-panel`, §13) is a visually distinct
component from a refusal, specifically so the two are never confusable.

**When this law does NOT apply.** A product with no grounding/refusal
surface at all has nothing for this law to attach to.

---

## L3 · "Gold is decorative-only, never meaning-bearing" — origin:
`little-milestones` — **unconfirmed at full read depth, stated with that
caveat rather than silently promoted to a confirmed law**

**The defect it (would) prevent:** an anxious parent reading meaning into an
accent colour that was never meant to carry any — the same anxiety-aware
discipline that makes the "mention to your pediatrician" surface a calm
slate blue rather than red/amber (§1.3, `--lm-danger` is reserved
exclusively for destructive-delete confirmations and nothing else).

**What was actually read and confirmed:** `little-milestones/knowledge/
UX_KB.md` §1.3's token table states, verbatim, for `--lm-gold`:
*"Celebration accents on the journey (decorative only, never text, never
meaning-bearing)."* That line is confirmed on disk and quoted exactly.
What was **not** independently re-verified at the harvest depth reached
here is whether that rule held under the file's later revisions (the KB
records a `§4` revision-2 palette update and a file-integrity recovery
event, both after §1.3 was written) — so this law is recorded as **the
original stated intent, confirmed once, not re-confirmed against every
later revision of the same file.** A future adopter should re-read §4
onward before relying on this as still-current for `little-milestones`
itself.

**When this law does NOT apply.** A product where a warm accent colour is
allowed to carry meaning (a brand's "human decision" gold, as in the Council
Mark law below) has the opposite rule on purpose, and the two are not in
tension — they are two different products making two different, equally
deliberate, choices about the same hue family.

---

## L4 · "Gold is used only for the pull-line and its terminus dot — never
the core, never the threads" — origin: `conclave-marketing`, carried into
`conclave-finance-studio`

**The defect it prevents:** the Conclave brand mark (six teal "thread" lines
converging on a neutral core, one gold "pull-line" standing for the human's
final say) loses its one piece of encoded meaning — *you, the human, are the
one gold element in a system of otherwise-neutral agents* — if gold is used
decoratively elsewhere in the same mark. CFS's own A2.7 pass violated this
law once (an invented gold filled disc as an app icon) and A2.8 records the
correction explicitly rather than silently fixing it, because the point of
recording a law is so the next violation is caught by the record, not by
luck.

**Separately, in CFS's own product semantics** (not marketing's, but
directly descended from it): gold is bound to *exactly two things* — the one
Approve control, and a forward prediction a person promised (`UX_KB` A2.7,
A2.8). It is not a status colour and there is no rule anywhere in the
product that gives it to a result.

**When this law does NOT apply.** Only relevant to a product that vendors
the Council Mark or the "gold = human decision" brand semantic at all.

---

## How to use this file

At Experience Design, for each law above: **adopt**, **decline with reason**,
or **adapt with a stated change**. Record the decision in the project's own
`UX_KB.md`, the same way `solution-architect`'s Reuse Decision Table records
reuse/adapt/build-new for every catalogue entry. A design pass that is
silent on all four laws has not considered them, which is not the same as
having decided none apply.
