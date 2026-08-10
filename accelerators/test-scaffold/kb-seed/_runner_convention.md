# The `_runner.sh` exit-code convention

Standalone doc so the convention can be pointed to from anywhere — this
platform's own `admin/proposals/2026-08-08-accelerator-layer.md`, other
accelerators' `ACCELERATOR.md` (H4), and a project's own `tests/suites/README.md`
— without re-deriving it each time.

## The convention

| Code | Meaning | How a consumer must report it |
|---|---|---|
| `0` | Executed, all scenarios passed | **EXECUTED — passed** |
| `1` | Executed, one or more scenarios failed | **EXECUTED — failed** (blocking unless the project's Test Policy marks the suite advisory) |
| `3` | No scenarios defined | **EMPTY — not a pass.** An empty suite must never be reported as passing |
| `4` | Cannot execute (missing interpreter/dependency) | **STATIC-ONLY** — findings are review-only, not verification |

The `3` and `4` codes exist specifically so an unexecuted suite and a passing
suite are never indistinguishable in a report. This is what makes the
platform's `STATIC ONLY — NOT EXECUTED` policy checkable rather than asserted:
a suite that cannot honestly claim `0` must fall through to `3` or `4`, never
be silently reported as passing.

## Reference implementation — `_runner.sh`

Confirmed byte-identical across five of the six on-disk copies at harvest time
(2026-08-08): `templates/genai-chatbot`, `templates/agentic-workflow`,
`templates/rag-knowledge-base`, `projects/conclave-marketing/dev`,
`projects/little-milestones/dev`, all at `tests/suites/_runner.sh`.

```sh
#!/usr/bin/env bash
# Shared suite runner. Each suite's run.sh delegates here.
#
# Exit codes are meaningful — test-agent maps them to its per-suite report:
#   0 = EXECUTED, all scenarios passed
#   1 = EXECUTED, one or more scenarios failed
#   3 = NO SCENARIOS DEFINED (an empty suite is NOT a passing suite)
#   4 = CANNOT EXECUTE (missing interpreter/dependency) — report as STATIC-ONLY
set -uo pipefail

SUITE="${1:?usage: _runner.sh <suite-name>}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUITE_DIR="$HERE/$SUITE"
DEV_ROOT="$(cd "$HERE/../.." && pwd)"

echo "── suite: $SUITE ──"
[ -d "$SUITE_DIR" ] || { echo "NO SCENARIOS DEFINED (no directory $SUITE_DIR)"; exit 3; }

shopt -s nullglob
scenarios=("$SUITE_DIR"/test_*.py)
shopt -u nullglob
if [ ${#scenarios[@]} -eq 0 ]; then
  echo "NO SCENARIOS DEFINED — this suite has no test_*.py files yet."
  echo "An empty suite is not a passing suite. Report it as such."
  exit 3
fi

# Prefer the project's own venv, per the platform's dev/-local-env convention.
PY=""
for cand in "$DEV_ROOT/.venv/bin/python" "$DEV_ROOT/backend/.venv/bin/python" "$(command -v python3 || true)"; do
  [ -n "$cand" ] && [ -x "$cand" ] && PY="$cand" && break
done
[ -n "$PY" ] || { echo "CANNOT EXECUTE — no python interpreter found."; exit 4; }

"$PY" -c "import pytest" 2>/dev/null || { echo "CANNOT EXECUTE — pytest not installed in $PY"; exit 4; }

echo "interpreter: $PY"
echo "scenarios:   ${#scenarios[@]}"
cd "$DEV_ROOT" || exit 4
"$PY" -m pytest "${scenarios[@]}" -q
rc=$?
[ $rc -eq 0 ] && echo "EXECUTED — suite passed" || echo "EXECUTED — suite FAILED (pytest rc=$rc)"
exit $rc
```

## The `conclave-finance-studio` delta — flagged, not silently absorbed

`projects/conclave-finance-studio/dev/tests/suites/_runner.sh` diverges from
the five above. Per the standing discipline (never drop a discrepancy silently
— report it, let a human decide), the delta as found on 2026-08-08:

1. An extra header comment block (lines 10–11) making explicit what the other
   five leave implicit: *"This script starts no server and installs nothing. A
   suite needing a running app assumes deploy-agent or the orchestrator started
   it, and fails loudly."*
2. `pytest` is invoked with an added `-p no:cacheprovider` flag (the five
   others omit it).
3. The `echo "scenarios: ..."` line reads `"${#scenarios[@]} file(s)"` in CFS
   vs. plain `"${#scenarios[@]}"` in the other five — cosmetic only.
4. The final pass/fail branch is written as an `if/else` block in CFS vs. a
   `[ ] && ... || ...` one-liner in the other five — behaviourally identical,
   stylistic only.

None of these change the exit-code contract above; the reference
implementation copied into this accelerator matches the five-way-identical
version, not the CFS variant. **This delta is recorded here, not resolved** —
resolving which copy is canonical (or whether the CFS additions should be
folded back in) is `mas-registrar`'s to do only under explicit human approval,
not this accelerator's to silently pick a winner on.

## Adoption note

`_runner.sh` itself is **not vendored as part of this accelerator's `src/`** —
it is the SME-suite convention documented above, not a harness module. What
`code-agent` vendors from `accelerators/test-scaffold/src/` is `browser.py`
and `native.py`; `_runner.sh` is authored per-project by `code-agent` at the
Code gate following the convention this document defines (per
`admin/LESSONS.md`, 2026-07-26 / "B2"). This document exists so that
convention has one canonical, citable source instead of six copies that could
each quietly drift.
