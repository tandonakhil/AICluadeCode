#!/usr/bin/env bash
# accelerators/conformance-kit — H4 suite entry point.
#
# Exit codes are the platform convention (see
# accelerators/test-scaffold/kb-seed/_runner_convention.md):
#   0 = EXECUTED, all scenarios passed
#   1 = EXECUTED, one or more scenarios failed
#   3 = NO SCENARIOS DEFINED (an empty suite is NOT a passing suite)
#   4 = CANNOT EXECUTE (missing interpreter/dependency) -- report as STATIC-ONLY
#
# Standalone: no app server, no long-lived process, no network, no
# credentials. Pure-Python-importable, so this file is a real runner, not a
# doc-only placeholder -- but see ACCELERATOR.md's H4 section: mas-registrar
# wrote and wired this without a Bash grant and has NOT executed it. The exit
# codes above are what a real invocation reports; nobody has produced one yet.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

shopt -s nullglob
scenarios=("$HERE"/test_*.py)
shopt -u nullglob
if [ ${#scenarios[@]} -eq 0 ]; then
  echo "NO SCENARIOS DEFINED -- this suite has no test_*.py files."
  echo "An empty suite is not a passing suite. Report it as such."
  exit 3
fi

PY=""
for cand in "$(command -v python3 || true)" "$(command -v python || true)"; do
  [ -n "$cand" ] && [ -x "$cand" ] && PY="$cand" && break
done
[ -n "$PY" ] || { echo "CANNOT EXECUTE -- no python interpreter found."; exit 4; }

"$PY" -c "import pytest" 2>/dev/null || { echo "CANNOT EXECUTE -- pytest not installed in $PY"; exit 4; }

echo "interpreter: $PY"
echo "scenarios:   ${#scenarios[@]}"
"$PY" -m pytest "$HERE" -q
rc=$?
[ $rc -eq 0 ] && echo "EXECUTED -- suite passed" || echo "EXECUTED -- suite FAILED (pytest rc=$rc)"
exit $rc
