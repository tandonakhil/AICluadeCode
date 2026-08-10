# Changelog — `accelerators/design-system`

## 1.0.0 — 2026-08-09

Initial admission. Harvested by `mas-registrar` from four source projects
under `admin/proposals/2026-08-08-accelerator-layer.md` (A3), approved by
the human 2026-08-08.

**Why 1.0.0 and not 0.x:** the token-role schema is proven by four
independent re-derivations (`conclave-finance-studio`, `rate-case-analyzer`,
`conclave-marketing`, `conclave-dashboard`); the enforcer mechanism is
proven in production by `conclave-finance-studio`'s `app/ui/tokens.py` and
its accompanying `tests/test_ui_tokens.py`; and the journey-map timing rule
is proven by a real, expensive, documented failure (see
`kb-seed/JOURNEY_MAPS.md`), not merely reasoned out in advance. This is not
a first draft being versioned optimistically.

### Added

- `src/tokens_schema.md` — the shared token schema as role names, mapped
  against all four source projects' actual token names. No palette values.
- `src/enforcer.py` — `assert_no_hue_band()` (generalized from CFS's
  `assert_no_green()`) and `assert_contrast_aa()` (generalized from CFS's
  inline WCAG assertions), plus the reused-verbatim colour-maths functions
  (`rgb`, `hsl`, `chroma`, `relative_luminance`, `contrast_ratio`).
- `kb-seed/DESIGN_LAWS.md` — four semantic laws, each tagged with origin
  project and the defect it prevents: no-green (CFS, enforced), refusal-
  never-styled-as-error (RCA), gold-decorative-only (little-milestones,
  flagged unconfirmed-at-depth), gold-only-on-the-pull-line (marketing →
  CFS).
- `kb-seed/JOURNEY_MAPS.md` — the timing rule (journey maps at Experience
  Design, before Architecture; an unwalkable journey is a gate-5 blocker),
  with the CFS finding quoted verbatim from `UX_KB.md` §A2.1/§A2.3/§A2.4.
- `kb-seed/design-review-scaffold/index.html` — a template index page for
  the `design-review/` static-HTML mockup convention, adapted from
  `rate-case-analyzer/design-review/index.html`.
- `tests/run.sh` — H4 admission suite: host-decoupling scan, clean-import
  check, and H5 negative controls for both `enforcer.py` guards. **Written,
  not executed** — `mas-registrar` holds no `Bash` grant; first real
  execution is pending at the first vendoring project's Test gate.

### Explicitly not included

No palette values (CFS blue/risk-ramp, RCA navy/gold, marketing
teal/gold/rust, LM terracotta/sage) — see `ACCELERATOR.md`'s admission
statement for why a "default" palette would misrepresent this accelerator's
own basis for existing. No component library, no type scale, no spacing
system — those are per-product decisions the schema deliberately leaves
open.
