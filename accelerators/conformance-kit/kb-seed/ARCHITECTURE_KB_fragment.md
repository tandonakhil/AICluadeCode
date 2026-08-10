# ARCHITECTURE_KB fragment — structural conformance kit

Paste/adapt this section into your project's own `knowledge/ARCHITECTURE_KB.md`
if you adopt `accelerators/conformance-kit`. Written so it reads as a decision
your project made, not an inherited default — edit the boundary names, module
paths and guarded resource before committing it.

## §N.1 — Import-boundary closure checks

This project enforces named structural invariants (e.g. "the public path never
reaches the private store") as a **data-driven manifest** checked by a **pure
function of a package root path**, rather than by code review alone.

- Manifest: `<your app package>/boundaries.py` — one `Boundary` entry per
  invariant, each carrying a `rationale` and the acceptance-criterion IDs it
  backs.
- Checker: `<your tooling path>/closure.py` — `ast`-based, never imports to
  inspect, closes the `importlib`/`__import__`/`eval`/`exec`/`globals()`/
  `sys.modules` dynamic-import escape hatch, and reports the **path** through
  the import graph a violation was reached by, not just the endpoint.
- Every boundary that is a genuine *rule* (not merely descriptive) has a
  negative-control fixture pair under `tests/negative_controls/<name>/`: one
  fixture that makes it fire, one that makes it not. A boundary without both is
  not trusted here — see `admin/LESSONS.md`, 2026-07-28, "always run a
  negative control before trusting a new guard."
- Two rule shapes recur: a plain forbidden-module rule (root closure may not
  reach a named module), and a zero-import/zero-symbol rule (root closure must
  be empty, and specific case-fold/regex/substring symbols may not appear
  anywhere in it) — used where a criterion needs a whole code path kept
  provably small and pure.
- When a criterion is written as **transitive** but is actually unsatisfiable
  that way (the forbidden module is necessarily in every caller's closure by
  construction), narrow the rule to `direct_only=True` and record the judgment
  call in the boundary's `rationale` — do not silently weaken the criterion
  the rule was meant to carry.

## §N.2 — Resource-scoped construction guards

Where a test suite must never touch a **live, out-of-tree resource** (a
developer's live database, a shared credential store, anything not owned by
the test run), guard the **resource's construction**, not the call sites that
might reach it.

- A caller-scoped fix (patching one fixture, one factory) is known to fail
  silently the next time a new call site is written without going through the
  fixed path — this is not hypothetical, see `ACCELERATOR.md` H6 for the exact
  defect this pattern was written to close, twice.
- Install once per test session, idempotently, with a holder-count so that
  multiple independent installers (e.g. two test trees run in one session)
  share one guard rather than laying patches on top of each other — an
  uncounted guard can silently disarm itself when the first of several
  installers tears down.
- The guard both **raises** (stops the write) and **records** (so a session-end
  assertion can report what happened even if something in the stack swallows
  the raised exception into a generic failure).
- Do not patch the live-path *getter* itself unless you have checked nothing
  else in the suite relies on it returning the real path — a redirected getter
  can make an unrelated measurement vacuously pass.

## §N.3 — Numeric-leak assertions on rendered output

Where a criterion says a value (a rate, a threshold, an internal number) must
not be readable from rendered output, assert on **tokenised numeric
literals**, not substrings of the disclosed bound.

- A substring check on a band's bounds is wrong in both directions: it
  false-fails on unrelated numbers that happen to contain the substring (a
  timestamp), and false-passes on the same value spelled differently (`0.02`
  vs `0.020`).
- `decimal_tokens()` extracts standalone numeric literals via a lookaround
  regex that refuses to match a digit run embedded in a longer numeric run
  (`1,234.56`, `40.023468`) — use `decimal.Decimal` comparisons, not floats, so
  differently-formatted equal values compare equal.

## Self-certification (H3)

This accelerator's own `closure.py` can be pointed at its own `src/` as a
check that it contains no import of a host project's domain modules. See
`ACCELERATOR.md` H3 for the worked example.
