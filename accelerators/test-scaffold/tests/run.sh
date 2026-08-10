#!/usr/bin/env bash
# accelerators/test-scaffold/tests/run.sh — this accelerator's own H4 suite.
#
# STATIC-REVIEW-ONLY BY NECESSITY: this suite verifies the harness modules
# themselves (browser.py, native.py), not an application under test. It
# cannot spin up a real browser or app server without violating H4's own
# "no long-lived process, no network, no credentials" rule and
# admin/LESSONS.md 2026-07-09 (a process started inside a subagent's turn
# dies when that turn ends). So what this suite checks is necessarily bounded
# to what is checkable without a live browser/native toolchain:
#
#   1. Both harness modules import cleanly (no syntax errors, no eager
#      dependency on playwright/RNTL at import time — both defer their
#      external dependency into function bodies, by design).
#   2. Their public surface matches what ACCELERATOR.md documents as the
#      contract (function/class names + signatures).
#   3. Neither module imports anything host-project-specific (H3 decoupling)
#      — no `from app.`, `from backend.`, `from mobile.`, or similar.
#
# What this suite does NOT and CANNOT verify (would require a live harness,
# i.e. an actual adopting project with Playwright/RNTL installed and a
# running app): that `render()` actually launches a browser and produces
# correct assertions, or that `run_native_render_tests()` actually drives
# jest against a real React Native tree. Those are proven by the harness's
# own provenance (five/six years of production use across five projects —
# see ACCELERATOR.md H6) and must be re-verified by any adopting project's
# own suite, per "Reuse never lowers the evidence bar."
#
# Exit codes — the platform convention this accelerator itself defines
# (see kb-seed/_runner_convention.md):
#   0 = all checks passed
#   1 = one or more checks failed
#   3 = no scenarios defined (src/ has no harness modules)
#   4 = cannot execute (no python3 interpreter)
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
SRC="$ROOT/src"

echo "── accelerators/test-scaffold — H4 admission suite ──"

shopt -s nullglob
modules=("$SRC"/*.py)
shopt -u nullglob
if [ ${#modules[@]} -eq 0 ]; then
  echo "NO SCENARIOS DEFINED — $SRC has no harness modules."
  exit 3
fi

PY="$(command -v python3 || true)"
if [ -z "$PY" ]; then
  echo "CANNOT EXECUTE — no python3 interpreter found."
  exit 4
fi
echo "interpreter: $PY"
echo "modules:     ${#modules[@]} ($(basename -a "${modules[@]}" | tr '\n' ' '))"

fail=0

# --- Check 1: static host-decoupling scan (H3) -----------------------------
# grep-equivalent: no `from app.`, `from backend.`, `from mobile.`, or a bare
# `import app` naming a host project's own package.
echo ""
echo "[1/3] host-decoupling scan (H3)"
if grep -nE '^\s*(from|import)\s+(app|backend|mobile)(\.|[[:space:]]|$)' "${modules[@]}" 2>/dev/null; then
  echo "FAIL — a host-project-shaped import was found above."
  fail=1
else
  echo "PASS — no host-project imports in ${#modules[@]} module(s)."
fi

# --- Check 2: modules import cleanly ---------------------------------------
echo ""
echo "[2/3] clean import (no syntax errors, no eager external dependency)"
if "$PY" -c "
import sys
sys.path.insert(0, '$SRC')
import browser
import native
print('PASS — browser and native both imported without error.')
"; then
  :
else
  echo "FAIL — one or both harness modules failed to import."
  fail=1
fi

# --- Check 3: public surface matches the documented contract ---------------
echo ""
echo "[3/3] public-surface signature check (matches ACCELERATOR.md)"
if "$PY" -c "
import sys, inspect
sys.path.insert(0, '$SRC')
import browser, native

errors = []

def expect(obj, name, owner_label):
    if not hasattr(obj, name):
        errors.append(f'{owner_label} is missing {name!r}')

expect(browser, 'render', 'browser')
expect(browser, 'HarnessUnavailable', 'browser')
expect(browser, 'Page', 'browser')
for m in ('effective_opacity', 'computed', 'has_horizontal_overflow', 'visible_text', 'screenshot_evidence'):
    expect(browser.Page, m, 'browser.Page')

expect(native, 'run_native_render_tests', 'native')
expect(native, 'reachable_components', 'native')
expect(native, 'HarnessUnavailable', 'native')
expect(native, 'NativeResult', 'native')

# Signature spot-checks — the documented contract, not every internal detail.
sig = inspect.signature(browser.render)
if list(sig.parameters)[0] != 'url':
    errors.append(f'browser.render first parameter should be url, got {list(sig.parameters)}')

sig = inspect.signature(native.run_native_render_tests)
if 'pattern' not in sig.parameters or 'timeout' not in sig.parameters:
    errors.append(f'native.run_native_render_tests should accept pattern, timeout; got {list(sig.parameters)}')

if errors:
    for e in errors:
        print('FAIL —', e)
    sys.exit(1)
print('PASS — public surface matches the documented contract.')
"; then
  :
else
  echo "public-surface check failed."
  fail=1
fi

echo ""
if [ "$fail" -eq 0 ]; then
  echo "EXECUTED — all static checks passed."
  exit 0
else
  echo "EXECUTED — one or more checks FAILED."
  exit 1
fi
