# Journey maps — the method, not the artifact

**This is the expensive lesson being packaged, not a template to copy
blindly.** The artefact (`v2-journeys.html`) is one project's specific
rendering of four specific journeys for four specific personas — it is not
reusable as a shape, because your journeys, personas and step counts will
not be CFS's. What *is* reusable is the timing rule, and the rule is worth
what it is worth only because of what it cost to learn.

## The rule

> **Journey maps are produced at Experience Design, before Architecture.**
> **A journey that cannot be walked end-to-end in the mockups is a gate-5
> blocker — not a note, not a deferred item, a blocker.**

## The evidence — quoted, not summarized

Journey maps existed as a designed artefact in exactly one project in this
portfolio: `conclave-finance-studio`, at
`design-review/redesign-2026-08-02/v2-journeys.html`. They were produced on
**2026-08-02**, in a design thread the human opened *after using the running
pilot* — that is, **after MVP1 was complete and after gate 5 had already
passed** on the original (pre-journey-map) Experience Design pass.

`projects/conclave-finance-studio/knowledge/UX_KB.md`, **§A2.1**, titled
*"What I found by using the pilot, and what §4 got wrong,"* opens:

> "§4 of this file claimed an information architecture: nine screens, three
> groups (Work / Govern / Evidence). **The build shipped twelve screens in
> two groups.** Evidence was dissolved into Govern; `/readiness` and
> `/my-probe-history` were added at top level with no design pass. The IA
> degraded after approval with no gate watching it. That is the first
> lesson: **§4 was a paragraph, not a checked artefact, and a paragraph does
> not survive contact with 262 acceptance criteria.**"

**§A2.3**, "The four journeys," records the walked state of each, exactly as
tabulated in the KB (quoted verbatim):

| # | Persona | Journey | State today |
|---|---|---|---|
| J1 | Staff accountant | Omission detected → investigate → resolve → leaves my queue | Walks, but **dead-ends at the last step**: saving produces no confirmation, no queue removal, no badge change, and the record it creates is linked from nowhere. Six times a night. |
| J2 | Controller | Approve a reclass → it becomes an export | **Unwalkable.** No approvals surface exists. |
| J3 | Controller | Was last period's close clean? | **Unstartable.** No period-parameterised surface anywhere. |
| J4 | FP&A analyst | Why did this account move? | **No surface, no persona button.** Confirmed by `PROJECT_CONTEXT.md` L2507. |

That is, of four end-to-end journeys checked against the shipped, gate-5-
approved product: **one unwalkable (J2), one unstartable (J3), one with no
surface at all (J4)** — three of four journeys structurally could not be
completed — **and the fourth (J1) walks but dead-ends at its final step**,
a defect repeated six times per night of actual use. The file's own
change-history entry for this pass (2026-08-02, v1.1.0) summarizes it as
*"four end-to-end journey maps (J1–J4, two of them currently unwalkable and
one unstartable)"* — J2 and J4 counted as the two unwalkable, J3 as the one
unstartable.

**§A2.4** records that none of the product's six binding design constraints
(no-green, narrative-collapsed, coverage-as-population-strip, abstention-
structurally-distinct, desktop-only) *caused* this. The cause named
explicitly: *"'No Approve button on the Review screen' was honoured
negatively. The button was removed; the separate deliberate act it implies
must happen somewhere was never given a screen, an object or a state. J2 is
therefore unwalkable. This is a gap created by honouring a constraint only
in its subtractive form, and it is the highest-value gap in the product."*

These were **severity-A gaps** — `UX_KB` §A2.6 classifies "blocks a whole
journey" as its top severity tier — discovered in a shipped product, after
its Experience Design gate had already been marked passed on the strength
of nine individually-designed screens that had never been walked end-to-end
as a sequence.

## Why the rule follows from the evidence, and not the other way round

The failure was not that any individual screen was badly designed — §A2.1
states plainly that "the item page is good... this is a navigation-and-
composition problem sitting on a sound design system." The failure was that
**nothing checked the sequence.** Screen-by-screen review against 186 (later
262) acceptance criteria is necessary and was done; it does not substitute
for walking a named persona through a named goal end-to-end, because
per-screen criteria compose into dead ends in ways no single screen's
criteria set can surface. Producing the journey map *before* Architecture
— rather than after a human notices the product is hard to use in
production — is what would have caught this at the cost of a design pass
instead of the cost of a rebuild.

## What this means operationally for an adopting project

1. At Experience Design, name the real end-to-end journeys — not screens,
   journeys: a named persona pursuing a named goal from trigger to
   completion.
2. Walk each one in the rendered mockup (per this accelerator's
   `design-review-scaffold/`, or your project's own convention) before the
   gate is marked passed.
3. A journey that cannot be walked, or that dead-ends without a confirmation
   / next-step / undo, is a gate-5 blocker for that journey — record it as
   such, not as a follow-up note.
4. Do this **before** Architecture, not after a human has used a running
   pilot and told you it does not work. The whole value of the rule is that
   it is cheaper before the build than after.

## What this accelerator does not claim

It does not claim CFS's four journeys, its persona set, or its specific
navigation redesign (A2.2's four-item task-ordered IA) are reusable as a
template — they are CFS's product-specific answers. It claims only the
timing discipline, purchased at the price of a real, documented, post-MVP1
rework pass.
