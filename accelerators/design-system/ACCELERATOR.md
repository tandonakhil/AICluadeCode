# `design-system` — the Conclave token schema and journey-map method

**Version:** 1.0.0 · **Status:** built · **Gate relevance:** Experience
Design, Architecture · **Consumers (source projects, see H10):**
`conclave-finance-studio`, `rate-case-analyzer`, `conclave-marketing`,
`conclave-dashboard`

Harvested under `admin/proposals/2026-08-08-accelerator-layer.md` (A3),
approved by the human 2026-08-08. Written by `mas-registrar` 2026-08-09.

---

## What this is, in one paragraph

**There is one coherent structural token schema, independently re-derived
four times, and four legitimately different palettes that must NOT be
unified.** This accelerator vendors the schema (a role vocabulary: ground
ramp, line/rule pair, ink ramp, one accent + soft background, a `shadow`
token), the mandatory light/dark mechanism, the numerics law
(`tabular-nums lining-nums`), a generalized version of `conclave-finance-
studio`'s import-time colour-guard mechanism, a menu of semantic laws each
tagged with the defect it prevents, and — the part that cost the most to
learn — the rule that journey maps belong at Experience Design, before
Architecture, and that an unwalkable journey is a gate-5 blocker. It does
**not** vendor any palette. See H2 below for exactly where the line sits.

---

## H1 · Declared contract (the public surface)

Everything under `src/` and `kb-seed/` is the declared surface. Anything
else in this directory (this file, `VERSION`, `CHANGELOG.md`, `tests/`) is
accelerator infrastructure, not part of what an adopter vendors into their
own project.

| Path | What it is |
|---|---|
| `src/tokens_schema.md` | The role schema — names and roles, no values |
| `src/enforcer.py` | `assert_no_hue_band()`, `assert_contrast_aa()`, plus reused colour-maths (`rgb`, `hsl`, `chroma`, `relative_luminance`, `contrast_ratio`, `css_variables`) |
| `kb-seed/DESIGN_LAWS.md` | Four semantic laws to choose from, each tagged with origin + defect prevented |
| `kb-seed/JOURNEY_MAPS.md` | The journey-map timing rule and its evidence |
| `kb-seed/design-review-scaffold/index.html` | A template index page for the `design-review/` mockup convention |

Anything not listed — internal helper names inside `enforcer.py` not
mentioned in this table, the exact prose wording of the laws, the exact
markup of the scaffold — is private and may change in a MINOR release
without notice, per H1's own rule.

## H2 · Config-vs-code boundary

| What you get | Configuration (change freely) | Requires a fork (edit `src/`) |
|---|---|---|
| **Token schema** (`tokens_schema.md`) | Every colour **value**. Token **names** (the schema's role names are suggestions, not required identifiers — CFS, RCA and the dashboard all used different names for the same role and none is "more correct"). Which ground/ink steps you actually need (marketing needed only two ink steps; CFS needed three). | The *shape* of the ramp is documentation, not code — there is nothing to fork. Adapt by choosing what you write in your own CSS. |
| **`assert_no_hue_band()`** | Whether you call it at all. The band (`min_deg`, `max_deg`), the `chroma_floor`, and the `reason` string are all parameters — CFS's own 75°–175° "no green" rule is reconstructed by calling this function with those specific arguments, not by editing the function. | The hue-band **math itself** (HSL conversion, chroma computation) — reused as-is; forking it means you have decided the maths is wrong, which should be rare and reported upstream. |
| **`assert_contrast_aa()`** | The `size` argument (`"normal"`/`"large"`) per call site, and the `label` for error messages. | The WCAG threshold constants (`AA_NORMAL = 4.5`, `AA_LARGE = 3.0`) and the relative-luminance formula — these are the spec, not a project decision. |
| **`DESIGN_LAWS.md`** | Which laws you adopt, decline, or adapt. This is the point of the file — see its own "How to use this file" section. | The prose stating what each law prevented in its origin project — that is provenance, not something to edit in place. If a law's stated origin turns out to be wrong, report it, don't silently rewrite it. |
| **`JOURNEY_MAPS.md`** | Your own journeys, personas, and step counts — entirely project-specific. | The timing rule itself and the CFS evidence quoted in support of it — this is a historical record, not a template. |
| **`design-review-scaffold/index.html`** | Every placeholder value (title, tokens, screens, journey groupings). This file is meant to be edited wholesale on copy-in. | Nothing — there is no "fork" concept for a template you are expected to fully rewrite. |

**"It's configurable" without this table fails admission (H2).** The table
above is the whole answer to "what do I change vs. what do I need to
change the source for."

## H3 · Host decoupling, proven

`src/enforcer.py` imports only `colorsys` and `re` (Python standard
library). No import of any host project's domain modules, no import of
`app.*`, `backend.*`, or `mobile.*`. `tests/run.sh` runs the same
host-decoupling grep scan `accelerators/test-scaffold` defined for itself
(§H4 below) against `src/*.py` — the catalogue eating its own dog food, per
H3's own text. `src/tokens_schema.md`, `kb-seed/*.md` and the scaffold
`index.html` are documentation/markup with no import surface to check.

## H4 · Own executable suite

`tests/run.sh` exists, follows the platform's `0`/`1`/`3`/`4` exit-code
convention (defined by `accelerators/test-scaffold`), and is standalone: no
app server, no long-lived process, no network, no credentials.

`mas-registrar` held no `Bash` tool grant and did not run this suite at
harvest time. **Executed for real** (orchestrator pass, 2026-08-09):
host-decoupling scan PASS, clean import PASS, both negative-control guards
fire on their positive control and stay silent on their negative control —
**EXECUTED, all checks passed**, exit code 0, no changes needed to `src/`.
This confirms the hand-computed hue/contrast fixture values (sourced from
`tokens.py`/`test_ui_tokens.py`, see H5 below) were correct on the first
real run.

## H5 · Negative controls

Both guard functions in `enforcer.py` are guards, so both get a positive
control (a fixture that makes the guard fire) and a negative control (one
that does not), inside `tests/run.sh`:

| Guard | Fires on (positive control) | Silent on (negative control) |
|---|---|---|
| `assert_no_hue_band` | `#22C55E` — a planted success green at hue ≈142° (confirmed against CFS's own `test_known_hues`, which asserts `110 < hue < 160` for this exact value) | `#1D4ED8` — CFS's own accent blue, hue ≈221° (confirmed against CFS's own `test_known_hues`, which asserts `200 < hue < 250`) |
| `assert_contrast_aa` | `#949494` on `#FFFFFF`, hand-computable via the WCAG relative-luminance formula to ≈3.04:1 — below the 4.5:1 AA-normal threshold | `#000000` on `#FFFFFF`, the maximum possible ratio, exactly 21:1 |

A guard admitted without both is a guard nobody has confirmed can fail —
both fixtures above are asserted in `tests/run.sh`'s check 3.

## H6 · Provenance and rationale

**Exact source paths, read in full during harvest (2026-08-09):**

| Source | Path | What was taken |
|---|---|---|
| `conclave-finance-studio` | `dev/backend/app/ui/tokens.py` | The reference implementation: `assert_no_green()`, `rgb`/`hsl`/`chroma`/`relative_luminance`/`contrast_ratio` — generalized into `enforcer.py` |
| `conclave-finance-studio` | `dev/backend/tests/test_ui_tokens.py` | **Confirmed to exist** (the prior review could not confirm this; it does, and was read in full) — used to harden the negative-control fixture values (hue ranges for `#22C55E` and `#1D4ED8` are lifted from this file's own `test_known_hues`) |
| `conclave-finance-studio` | `design-review/redesign-2026-08-02/{brand,apple,ds}.css` | Confirmed the CFS-side token names (`bg`/`surface`/`surface-2`/`surface-3`, `line`/`line-2`, `ink`/`ink-2`/`ink-3`, `accent`/`accent-bg`) that seed `tokens_schema.md`'s CFS column |
| `conclave-finance-studio` | `knowledge/UX_KB.md` §A2.1, §A2.3, §A2.4 (and the 2026-08-02 change-history entry) | The journey-map finding, quoted verbatim in `kb-seed/JOURNEY_MAPS.md` |
| `rate-case-analyzer` | `dev/app/web/static/rca.css` | Token names (`paper`/`surface`/`surface-2`/`surface-3`, `rule`/`rule-strong`, `ink`/`ink-2`/`ink-3`, `accent`/`accent-soft`, `shadow`); `.refusal-panel`/`.coverage-none` for L2 in `DESIGN_LAWS.md` |
| `rate-case-analyzer` | `design-review/index.html` | The `design-review/` index-page convention `kb-seed/design-review-scaffold/index.html` is adapted from |
| `conclave-marketing` | `dev/app/static/css/site.css` | Token names (`paper`, `ink`, `muted`, `hairline`, `line2`, `teal` as accent, `teal-soft`); the "gold only on the pull-line" Council Mark law (L4) |
| `conclave-dashboard` | `design-review/index.html` (inline `<style>`) | Token names (`void`/`floor`/`surface`/`surface2`, `hair`/`hair-hi`, `ink`/`ink-dim`/`ink-faint`, `accent`/`accent-soft`, `shadow`) — the fourth independent re-derivation of the schema |
| `little-milestones` | `knowledge/UX_KB.md` §1.3 | The `--lm-gold` "decorative only, never meaning-bearing" line (L3) — quoted verbatim, flagged unconfirmed against the file's own later revisions (§4 onward), which were not read at harvest depth |

**What defect each piece prevents:** stated per-law in `kb-seed/
DESIGN_LAWS.md` and per-guard in this file's H5 table. **What was
deliberately left behind:** every palette value from every source project
(see the top-level task constraint and this file's closing section); CFS's
`components.py` (1,823 lines of product-specific component law — correct
there, not a shared surface); any project's type scale or spacing system;
the specific navigation/IA redesign CFS produced alongside its journey
maps (A2.2's four-item IA is CFS's answer to CFS's problem, not a
transferable pattern).

## H7 · Semver + CHANGELOG

`VERSION` = `1.0.0`. `CHANGELOG.md` at this directory's root. A future
MAJOR (e.g., a breaking rename inside `enforcer.py`'s public functions)
requires a migration note naming every known consumer at that time.

## H8 · Deprecation is marking, never deletion

Not applicable yet — this is the initial admission. When and if this
accelerator is superseded, the superseding entry's `ACCELERATOR.md` will
name this one and why, and this directory stays runnable rather than being
removed.

## H9 · Co-signs — explicitly none required

**No security co-sign and no responsible-AI co-sign are required for this
accelerator.** Stated explicitly so it is not read as an oversight: this is
a visual/UX accelerator — colour tokens, a light/dark mechanism, a WCAG
contrast checker, and a design-process rule. It touches no credentials, no
sessions, no secrets, no PII, and sits on no grounding/refusal/guardrail
path (admission's H9 triggers are `security-architect` for
credentials/sessions/secrets/PII, and `responsible-ai-architect` for
grounding/refusal/guardrail surfaces — neither applies here). `L2` in
`DESIGN_LAWS.md` *describes* RCA's refusal styling as a design pattern but
does not itself implement or gate any refusal logic.

## H10 · Known consumers

At promotion (2026-08-09), the four **source** projects this accelerator
was harvested *from* — they independently re-derived the schema before this
accelerator existed to vendor it from, so none of them has yet "adopted" it
in the vendoring sense (`# VENDORED from accelerators/design-system@1.0.0`).
Recorded here as the harvest basis, per the catalogue instruction to name
them as consumers:

- `conclave-finance-studio` — origin of the enforcer mechanism and the
  journey-map finding
- `rate-case-analyzer` — origin of the `paper`/`rule`/`shadow` naming branch
  and the refusal-styling law
- `conclave-marketing` — origin of the brand-semantics laws (gold, hairline
  naming branch)
- `conclave-dashboard` — origin of the fourth independent schema
  re-derivation (`void`/`floor`/`hair` naming branch)

No project has yet vendored this accelerator **into** itself via the copy-
with-provenance-stamp mechanism (`accelerators/README.md`). The first real
adopter's provenance stamp and `PROJECT_CONTEXT.md` entry will be the first
row added under a genuine "vendored at version X" reading of this section.

---

## Adoption note for `ui-ux-designer`

`ui-ux-designer`'s own contract is **not changed** by this accelerator's
admission — per `admin/proposals/2026-08-08-accelerator-layer.md`'s
contract-changes table, `ui-ux-designer` is confirmed unchanged, and the
mandatory catalogue-consultation duty in MVP-1 sits only with
`solution-architect` (that proposal's §"solution-architect's new duty").
**This is stated plainly so it is not misread as an oversight rather than a
deferral:** `ui-ux-designer` contract wiring to the accelerator catalogue is
explicitly deferred, not forgotten. In the meantime, `kb-seed/DESIGN_LAWS.md`
and `kb-seed/JOURNEY_MAPS.md` are consultable documentation/pattern
resources — `ui-ux-designer` may read and apply them at any Experience
Design gate exactly as it would any other portfolio precedent, without a
contract change being required to do so. A future contract change adding a
mandatory consultation duty for `ui-ux-designer` would need its own
`mas-architect` recommendation and human approval, per this platform's
standing rule against silently widening any agent's obligations.

---

## Worked example — the AA-contrast correction history (CFS)

Preserved here rather than deleted, because H6 asks for what a future
architect needs to *decide against* as much as what to adopt. From
`tokens.py`'s own inline comments and `test_ui_tokens.py`'s
`test_every_ink_meets_aa_on_EVERY_ground_in_both_themes`:

> "`ink-3`... #6A707A (and the mockup's #7A808A before it) fails AA on
> `surface-2` and `surface-3`, which is where most small text actually
> sits. Darkened until it passes on the darkest ground." — final value
> `#5E646E`.

> "`risk-1-bg`... Lightened from the gate-5 mockup value `#FBF1E4`, which
> put `risk-1` on it at **4.4966:1** — under WCAG AA by 0.004." — final
> value `#FDF6EC`.

And from the test file's own docstring: "The first version of this test
checked white alone and passed while `ink-3` sat at 4.36:1 on `surface-2`,
which is where most of the small text on these screens actually is. The
browser found it; the unit test now covers the same grounds" — i.e. the
lesson that motivated `assert_contrast_aa()` being callable against
*every* ground a token actually renders on, not only the primary surface.
This is the exact kind of near-miss (0.004 under threshold, caught only
because the *dark* ground was checked and not only the lightest one) that
makes a computed guard worth having over a design-time eyeball check.

## What was deliberately NOT extracted

Per the task constraint and this accelerator's own admission basis: **no
palette values.** Not CFS's blue/risk-ramp, not RCA's navy/gold, not
marketing's teal/gold/rust, not little-milestones' terracotta/sage — none of
these appear as defaults anywhere under `src/`. Choosing any one of them as
a "recommended default" would misrepresent the accelerator's own finding
that four different, correct palettes exist for four different products.
Where a palette is shown in this document (the worked example above), it is
labeled as "here is what CFS chose," never as a recommendation.
