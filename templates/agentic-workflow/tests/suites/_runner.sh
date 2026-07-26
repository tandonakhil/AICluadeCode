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
