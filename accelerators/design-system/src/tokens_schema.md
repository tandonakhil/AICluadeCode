# The token schema — names and roles, no values

This is the part of the Conclave design language that is genuinely shared: a
**structural** schema of token *roles*, independently re-derived four times
(`conclave-finance-studio`, `rate-case-analyzer`, `conclave-marketing`,
`conclave-dashboard` — see `../ACCELERATOR.md` §H6 for exact source paths).
No project used identical token *names*, and none should be forced to. What
is identical across all four is the **shape**: a ground ramp, a line/rule
pair, an ink ramp, one interactive accent with a soft background, and (in
three of the four) an explicit `--shadow` token. That shape is the surface
this accelerator vendors. **Values are never part of it** — see
`../ACCELERATOR.md`'s H2 config table.

## The roles

| Role | Purpose | CFS | RCA | Dashboard | Marketing |
|---|---|---|---|---|---|
| **ground-0** | Page background, the palest/deepest plane | `--bg` | `--paper` | `--void` | `--paper` |
| **ground-1** | Card / panel surface, one step up from ground-0 | `--surface` | `--surface` | `--floor` | `--surface` |
| **ground-2** | A second surface step (hover fill, nested panel) | `--surface-2` | `--surface-2` | `--surface` | *(not separately named — see note)* |
| **ground-3** | A third surface step (deepest nesting, active/pressed) | `--surface-3` | `--surface-3` | `--surface2` | *(not separately named)* |
| **line** | Decorative rule/border — never carries text | `--line` | `--rule` | `--hair` | `--hairline` |
| **line-strong** | A stronger rule for emphasis dividers | `--line-2` | `--rule-strong` | `--hair-hi` | `--line2` |
| **ink** | Primary text | `--ink` | `--ink` | `--ink` | `--ink` |
| **ink-2** | Secondary text | `--ink-2` | `--ink-2` | `--ink-dim` | `--muted` |
| **ink-3** | Tertiary / smallest-permitted text | `--ink-3` | `--ink-3` | `--ink-faint` | *(not separately named — `--muted` covers both dim tiers)* |
| **accent** | The one interactive colour: links, focus, primary action | `--accent` | `--accent` | `--accent` | `--teal` |
| **accent-bg** | A soft tint of accent, for selected/active fills | `--accent-bg` | `--accent-soft` | `--accent-soft` | `--teal-soft` |
| **shadow** | Elevation, as a single composed token, never ad hoc | *(not present in `tokens.py`; present in the RCA and dashboard renderings)* | `--shadow` | `--shadow` | *(not present)* |

**Note on the two projects with a shallower ramp.** `conclave-marketing` is a
five-page brand site, not a dense data product; it did not need a
`ground-2`/`ground-3` step or a separate `ink-3`, and did not invent one it
had no use for — which is the schema working correctly, not incompletely.
`conclave-dashboard` names four ground steps but folds line-vs-content
differently (`--hair`/`--hair-hi` as alpha-composited hairlines rather than
solid tokens). **Do not "complete" a project's ramp to match this table.**
The table exists so a future project can *choose* how many ground steps and
ink steps it needs, not to mandate four of each.

## The two structural laws that travel with the schema

### 1. Light/dark is mandatory, expressed via `[data-theme]`

All four source projects gate their dark palette behind `[data-theme=dark]`
(CFS, marketing) or `html[data-theme="dark"]` (dashboard), or
`@media(prefers-color-scheme:dark)` as a fallback layered under the same
attribute (RCA). **A design that ships light-only is not to this schema's
standard.** The attribute selector, not a class, is the convention — it
composites cleanly with `data-variant` style palette switches (dashboard's
"quiet"/"paper"/"low-light" experiment) without a selector explosion.

### 2. Numerics law — `tabular-nums lining-nums`

Every source project applies `font-variant-numeric: tabular-nums` (RCA,
dashboard use `tabular-nums` alone; CFS and marketing pair it with
`lining-nums` and `font-feature-settings: "tnum" 1, "lnum" 1` for broader
engine support) to every rendered figure: money, counts, coverage ratios,
risk scores. The rule: **any numeral a reader compares against another
numeral in the same column must not shift width per digit.** This is a
`.mono`/`.num`/`.amt` utility class in every source project, never applied
ad hoc per component.

```css
.mono, .num, .amt {
  font-variant-numeric: tabular-nums lining-nums;
  font-feature-settings: "tnum" 1, "lnum" 1;
}
```

## What this schema is not

It is not a component library, not a type scale, and not a spacing system —
those are genuinely per-project (CFS's Apple-pro-app 7-size scale at
12·13·15·17·21·28·40 is right for a dense finance product and wrong for
`little-milestones`' storybook register). It is the **ground/line/ink/accent
role vocabulary only**, because that is the part four independent designers
reached for the same shape without copying from each other.
