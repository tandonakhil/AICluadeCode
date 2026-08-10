# Changelog — `conformance-kit`

## 1.0.0 — 2026-08-09

Initial harvest. Approved by the human 2026-08-08
(`admin/proposals/2026-08-08-accelerator-layer.md`, item A5), placed by
`mas-registrar`.

Both pieces vendored here were written after a real guard failure, not
speculatively — see `ACCELERATOR.md` H6 for exact provenance:

- `src/boundaries.py` + `src/closure.py` — the data-driven forbidden-import
  manifest and its pure-function-of-a-package-root checker, generalized from
  `rate-case-analyzer`'s `app/boundaries.py` and
  `tools/structural_checks/closure.py`. Fourteen RCA-specific boundaries
  replaced with two worked examples reproducing the two shapes RCA's rules
  actually took (plain forbidden-module; zero-import/zero-symbol).
- `src/live_ledger_guard.py` — the resource-scoped (not caller-scoped)
  construction guard, generalized from `conclave-finance-studio`'s
  `conclave_harness/live_ledger_guard.py`. Written specifically because a
  caller-scoped (per-fixture) fix to the same defect had already failed once;
  see `ACCELERATOR.md` H6 and the module's own docstring for the two-part
  failure history, preserved from the source.
- `src/rendered_numbers.py` — numeric-tokenisation leak assertion, generalized
  from `conclave-finance-studio`'s `conclave_harness/rendered_numbers.py`,
  replacing substring checks that were wrong in both directions (false-failed
  on a timestamp, would have false-passed on a reformatted value like
  `0.020`).

Status: `built`, version `1.0.0`. `tests/run.sh` and `tests/test_conformance_kit.py`
were written but **not executed** by `mas-registrar` at harvest time (no
`Bash` grant).

## [1.0.1] — 2026-08-09

Not a behaviour change to `src/` — PATCH, test-fixture-only. Executed for
real (orchestrator pass, same day): 1 real bug found and fixed, in
`tests/test_conformance_kit.py`, not in `src/`:

- The forbidden-import fixture tests passed `package_root =
  .../fixture_violates` (the fixture tree's *parent*), but `closure.py`'s
  `build_module_map()` — vendored unmodified from RCA — expects
  `package_root` to point *at* the package directory itself (matching RCA's
  own convention: `CONTROLS / name / "app"` in its `test_boundaries.py`, not
  `CONTROLS / name`). Pointing at the parent double-prefixed every module
  name (`app.app.public.api`), so the closure silently found nothing and the
  positive-control test failed with 0 violations instead of a violation.
  Fixed by appending `/ "app"` to all three fixture-path constructions.
  `closure.py`/`boundaries.py` themselves needed no change — confirmed
  domain-free as originally harvested.
- Also corrected the fixed test's expected violation count from 1 to 2: a
  plain `from app.private.store import PrivateStore` reaches two candidate
  module names (the module and the symbol-qualified name), both correctly
  flagged by the unmodified checker — real behaviour, not a fixture defect,
  confirmed by tracing `direct_imports()` by hand.

After both fixes: `9 passed`, exit code 0.
