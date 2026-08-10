# `conformance-kit` — structural conformance kit

**Slug**: `conformance-kit` (A5). **Version**: `1.0.0`. **Status**: `built`.

## Purpose

Domain-free structural guards, harvested because both pieces were written
*after* a real guard failure, not designed speculatively:

1. **Import-boundary closure checking** (`boundaries.py` + `closure.py`) — a
   data-driven manifest of forbidden-import rules, checked by a pure function
   of a package root path, that closes the dynamic-import escape hatch
   (`importlib`/`__import__`/`eval`/`exec`/`globals()`/`sys.modules`) a naive
   static check would miss.
2. **Live-resource construction guard** (`live_ledger_guard.py`) — refuses
   construction of a named resource class over a named live path, watching the
   *resource* rather than enumerating callers, because a caller-scoped fix to
   the same defect had already failed once in the source project. See H6.
3. **Numeric-tokenisation leak assertion** (`rendered_numbers.py`) — asserts no
   numeric literal on a rendered page falls inside a forbidden band, replacing
   a substring check that was wrong in both directions.

This is the direct answer to `admin/LESSONS.md`'s standing rule: *"always run
a negative control before trusting a new guard."* Every guard vendored here
ships with one (H5).

## H1 — Declared contract

Public surface, everything else is private and may change in a MINOR:

- `boundaries.Boundary` (dataclass) and `boundaries.EXAMPLE_BOUNDARIES` (the
  worked example manifest an adopter replaces).
- `closure.check(package_root: Path, boundaries: Iterable[Boundary], package_alias: str = "app") -> tuple[Violation, ...]`
  and `closure.Violation` (dataclass with `boundary`, `kind`, `detail`,
  `path`).
- `live_ledger_guard.install(*, module_path: str, class_name: str, live_path: str) -> Guard`,
  `live_ledger_guard.uninstall()`, `live_ledger_guard.active()`,
  `live_ledger_guard.holders()`, `live_ledger_guard.assert_nothing_was_refused(guard)`,
  `live_ledger_guard.Guard` (`.record`, `.drain`, `.violations`),
  `live_ledger_guard.LiveResourceWriteAttempt`.
- `rendered_numbers.decimal_tokens(text) -> set[Decimal]`,
  `rendered_numbers.numbers_in_band(text, band) -> list[Decimal]`,
  `rendered_numbers.band_is_not_readable(text, band, where="", criteria=None)`,
  `rendered_numbers.any_band_is_not_readable(texts, band, criteria=None)`.

Everything else (module-internal helpers like `_matches`, `_symbol_hits`,
`_message`) is private.

## H2 — Config-vs-code boundary

| What | Config (adopter changes freely) | Code (requires a fork) |
|---|---|---|
| Which import pairs are forbidden | `Boundary` entries in your own replacement for `boundaries.EXAMPLE_BOUNDARIES` — names, `roots`, `forbidden_modules`, `forbidden_symbols`, `except_modules`, `direct_only`, `rationale`, `criteria` | The AST-walking algorithm in `closure.py` (`direct_imports`, `references_dynamic_import`, `closure`, `_symbol_hits`, `check`) |
| Which package alias root modules use | `package_alias` parameter to `build_module_map`/`check` (defaults `"app"`) | The module-name derivation logic in `_module_name` |
| Which class/module/path the live-resource guard watches | `module_path`, `class_name`, `live_path` keyword arguments to `install()` | The patch-and-restore mechanism, the holder-count, the raise+record behaviour |
| Which band a rendered-numbers check forbids, and its label | `band` tuple and optional `criteria` string passed to `band_is_not_readable`/`any_band_is_not_readable` | The tokenisation regex `_NUMERIC_TOKEN` and the `Decimal`-based comparison |

## H3 — Host decoupling, proven

**Verification method**: manual read-through of all four `src/*.py` files
during generalization, checking for any import, string literal or symbol name
naming `rate-case-analyzer`'s (`app.answer.*`, `app.stores.*`,
`app.grounding.*`, `AC-F*` acceptance-criterion IDs) or `conclave-finance-studio`'s
(`ges.*`, `BrokerStore`, `default_store_path`) domain modules. Result: none
remain in `src/`. Specifically —

- `closure.py` was already domain-free in the source (confirmed, not asserted
  — its only project-shaped string is the *default value* `"app"` for the
  `package_alias` parameter, which is a convention every Conclave project's
  layout shares, not an RCA name, and is overridable).
- `boundaries.py` originally held 14 boundaries naming RCA's own module tree
  and acceptance-criterion IDs; none are vendored. `EXAMPLE_BOUNDARIES` uses
  placeholder names (`app.public.api`, `app.private.store`, `app.core.pure`)
  that exist nowhere in RCA or CFS.
- `live_ledger_guard.py` originally hardcoded `ges.broker.store.BrokerStore`
  and `default_store_path()`; both are now caller-supplied arguments to
  `install()`.
- `rendered_numbers.py` was already algorithm-only; the one CFS-specific
  string (the default assertion message baking in `AC-F12-15`) is now an
  optional `criteria` parameter with no default.

**Self-certification, not yet run**: an adopter (or a future `mas-architect`
audit) can point this accelerator's own `closure.py` at its own `src/`:

```python
from pathlib import Path
from boundaries import Boundary
from closure import check

no_host_import = Boundary(
    name="conformance-kit-is-host-free",
    roots=("boundaries", "closure", "live_ledger_guard", "rendered_numbers"),
    forbidden_modules=("app.answer", "app.stores", "app.grounding", "ges", "ges.broker"),
)
violations = check(Path("accelerators/conformance-kit/src"), (no_host_import,), package_alias="")
assert violations == ()
```

This is not wired into `tests/test_conformance_kit.py` because `closure.py`'s
`package_alias` model assumes a single dotted-name root package (`app.x.y`),
and `src/` here is four flat top-level modules rather than a package — running
it faithfully needs a `package_alias=""` adaptation this harvest did not have
time to also write and verify. Recorded as a known gap rather than silently
skipped: **the catalogue's own H3 self-certification for this entry is
described, not executed.**

## H4 — Own executable suite

`tests/run.sh`, platform exit-code convention (0/1/3/4, per
`accelerators/test-scaffold/kb-seed/_runner_convention.md`), standalone: no
app server, no long-lived process, no network, no credentials.

**Executed for real** (orchestrator pass, 2026-08-09): `9 passed`, exit code
0. `mas-registrar` held no `Bash` grant at harvest time and had marked this
STATIC ONLY; the first real run found and fixed one genuine bug in the test
fixture, not in `src/` — see `CHANGELOG.md` [1.0.1]. `src/boundaries.py`,
`closure.py`, `live_ledger_guard.py`, and `rendered_numbers.py` all required
no changes.

## H5 — Negative controls

Both guards ship a fire case and a non-fire case, per admission criterion H5:

- `tests/negative_controls/example_forbidden_import/` — `fixture_violates/`
  (fires: `app.public.api` imports `app.private.store`) and `fixture_clean/`
  (does not fire: same module names, no forbidden import).
- `tests/negative_controls/example_live_resource_leak/` — one pytest case
  constructing the guarded resource over the live path (fires,
  `LiveResourceWriteAttempt` raised and recorded) and one constructing it over
  a different path (does not fire, `assert_nothing_was_refused` passes clean).

RCA's own suite carries **eight** mutated-fixture-tree negative controls
against its full 14-boundary manifest (`wall_breach`, `dynamic_import`,
`sentinel_impure`, `web_writes`, `job_answers`, `fixture_online`,
`string_keyed`, `env_leak` — sampled by directory name at harvest, not fully
read for every case). Only the `wall_breach` pattern (a module reaching a
forbidden concrete store) is worked here as `example_forbidden_import`; the
other seven exist in RCA as evidence the checker's dynamic-import,
symbol-scan and zero-closure code paths are each independently exercised, not
just the plain-forbidden-module path. An adopter who needs those other shapes
demonstrated should read RCA's originals directly (H6 paths below) rather than
assume this harvest reproduced all eight.

## H6 — Provenance and rationale

| File here | Exact source | What defect it prevents | What was deliberately left behind |
|---|---|---|---|
| `src/boundaries.py` (format only) | `projects/rate-case-analyzer/dev/app/boundaries.py` | An import-boundary invariant stated in prose ("the public path never reaches the private store") drifting silently as the codebase changes, with no mechanical check | All 14 of RCA's actual boundaries, their acceptance-criterion IDs, and RCA's own module names — those are RCA's product law, not a reusable payload |
| `src/closure.py` | `projects/rate-case-analyzer/dev/tools/structural_checks/closure.py` | (a) A static check evaded by `importlib.import_module(...)`; (b) a boundary check that reports only a verdict, not the path a violation was reached by, forcing a manual re-derivation of the route on every failure | Nothing — confirmed domain-free, vendored unmodified except this header |
| `src/live_ledger_guard.py` | `projects/conclave-finance-studio/dev/backend/conclave_harness/live_ledger_guard.py` | A test run silently corrupting a developer's live, out-of-test-scope resource (in the source project: `dev/var/broker_db.sqlite3`, the running pilot's live decision ledger) because the guard against it was scoped to specific callers/fixtures rather than to the resource's own construction. **This guard exists because a caller-scoped fix to the identical defect (commit `4e5ee47`, fixing one test tree's `ges_http` fixture) had already been applied and still left a second tree (`backend/tests/conftest.py`'s `ges_app`/`ges_stack` fixtures) writing to the same live file.** The full two-part failure narrative is preserved in the module's own docstring, unshortened, because it is the entire argument for this shape of guard over a fixture-by-fixture fix. | The hardcoded `ges.broker.store.BrokerStore` class reference and `default_store_path()` getter — now `module_path`/`class_name`/`live_path` parameters to `install()` |
| `src/rendered_numbers.py` | `projects/conclave-finance-studio/dev/backend/conclave_harness/rendered_numbers.py` | A substring-based leak check on a disclosed numeric band that was wrong in both directions: it false-failed when a rendered timestamp (`...T07:04:40.023468+00:00`) happened to contain the substring `"0.02"`, and would have false-passed a genuine leak reformatted as `"0.020"` (same value, different substring) — both preserved as the worked example in this file's own docstring and in `kb-seed/ARCHITECTURE_KB_fragment.md` | The CFS-specific default assertion message baking in `AC-F12-15`; now an optional `criteria` label with no default |
| `tests/negative_controls/example_forbidden_import/` | Pattern modelled on `projects/rate-case-analyzer/dev/tests/negative_controls/wall_breach/` (one of RCA's eight) | Same as `boundaries.py`/`closure.py` row, demonstrated concretely | The other seven RCA negative-control shapes — see H5 |
| `tests/negative_controls/example_live_resource_leak/` | Pattern modelled on CFS's own suite usage of `live_ledger_guard` (no single fixture file copied verbatim; CFS's usage is embedded in its two conftests, not a standalone example) | Same as `live_ledger_guard.py` row, demonstrated concretely | CFS's real `BrokerStore`/`default_store_path` wiring, replaced with a minimal stand-in `Resource` class |

What I could **not** determine from the source headers/docstrings and did not
invent: the exact date or commit of the *second* failure (the `ges_app`/
`ges_stack` conftest leak) — only that commit `4e5ee47` is named in the source
docstring as the fix for the *first* occurrence, and that the docstring states
the second was found afterward in the same investigation. No further detail
is asserted beyond what the source docstring itself states.

## H7 — Semver + CHANGELOG

`VERSION` = `1.0.0`. See `CHANGELOG.md`. This is a MAJOR-eligible 1.0.0 rather
than a 0.x because both pieces are proven by a **documented prior guard
failure**, not speculative design — per the harvest brief's explicit
instruction.

## H8 — Deprecation

Not yet superseded. If a future accelerator supersedes this one, this entry
stays runnable and records what supersedes it and why, per admission
criterion H8. Not applicable at 1.0.0.

## H9 — Co-signs

None of `boundaries.py`, `closure.py`, `live_ledger_guard.py` or
`rendered_numbers.py` touches credentials, sessions, secrets or PII, and none
sits on a grounding/refusal/guardrail path in the RAG sense — H9's
security/responsible-AI co-sign requirements do not apply to this entry.
(`live_ledger_guard.py` protects a *test-time* resource from corruption; it is
not an authn/authz or data-handling control.)

## H10 — Known consumers

| Project | Version | Notes |
|---|---|---|
| `rate-case-analyzer` | origin (pre-accelerator) | Source of `boundaries.py` format + `closure.py`. Not yet re-vendored from this accelerator — origin project, not a real consumer of `1.0.0`. |
| `conclave-finance-studio` | origin (pre-accelerator) | Source of `live_ledger_guard.py` + `rendered_numbers.py`. Same caveat. |

Neither project has vendored `1.0.0` back in as of this harvest. Both are
listed as **origin**, per the harvest brief's instruction, not as adopters —
"who has the old copy" is not yet a live question for this entry.

## Adoption steps

1. Copy `src/*.py` into your project (e.g. `app/boundaries.py`,
   `tools/structural_checks/closure.py`, or your own layout).
2. Replace `boundaries.EXAMPLE_BOUNDARIES` with your own manifest — real
   module names, real `rationale`, real acceptance-criterion IDs.
3. If adopting `live_ledger_guard`, identify the resource class and live path
   your project must never touch under test, and call `install()` with
   `module_path`/`class_name`/`live_path` from your own session-scoped test
   fixture (see the module's own docstring for the idempotency/holder-count
   reasoning before wiring two independent installers).
4. If adopting `rendered_numbers`, identify the band(s) that must not be
   readable from your rendered output and call `band_is_not_readable` /
   `any_band_is_not_readable` from your own scenarios.
5. Copy the accelerator's tests (`tests/test_conformance_kit.py`,
   `tests/negative_controls/`) as your starting negative-control fixtures, and
   extend them with fixtures against your own real manifest — the vendored
   examples prove the mechanism, not your project's actual boundaries.
6. Record the vendor in `PROJECT_CONTEXT.md`'s `## Accelerators` section:
   name, version, date, sha256, reuse/adapt/build-new reason, per
   `accelerators/README.md`.
7. Per `solution-architect`'s contract, reuse never lowers the evidence bar —
   write real acceptance criteria against your own manifest and get them
   verified in your own project; "covered upstream by the accelerator" is
   never an answer to `NOT VERIFIED`.
