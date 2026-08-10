#!/usr/bin/env bash
# accelerators/design-system/tests/run.sh — this accelerator's own H4 suite.
#
# STATIC ONLY — NOT EXECUTED. Written by `mas-registrar`, which holds no
# `Bash` grant. Per the platform's `STATIC ONLY — NOT EXECUTED` discipline,
# this file is reviewed by a human/agent with Bash for correctness, and its
# first real execution happens at the first vendoring project's own Test
# gate — not here, and not claimed here. Do not read "written" as "passing".
#
# What this suite checks, once actually run: `src/enforcer.py`'s two guard
# functions (`assert_no_hue_band`, `assert_contrast_aa`) against known-good
# and known-bad fixtures — i.e. H5's negative control ("a fixture that makes
# the guard fire, and one that makes it not fire") for both guards, plus
# H3's host-decoupling scan reused from `test-scaffold`'s own convention.
#
# Exit codes — the platform convention (accelerators/test-scaffold defines
# it; kb-seed/_runner_convention.md there is the canonical statement):
#   0 = all checks passed
#   1 = one or more checks failed
#   3 = no scenarios defined (src/ has no python modules)
#   4 = cannot execute (no python3 interpreter, or pytest unavailable)
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
SRC="$ROOT/src"

echo "── accelerators/design-system — H4 admission suite ──"

shopt -s nullglob
modules=("$SRC"/*.py)
shopt -u nullglob
if [ ${#modules[@]} -eq 0 ]; then
  echo "NO SCENARIOS DEFINED — $SRC has no python modules."
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

# --- Check 1: host-decoupling scan (H3) ------------------------------------
echo ""
echo "[1/3] host-decoupling scan (H3)"
if grep -nE '^\s*(from|import)\s+(app|backend|mobile)(\.|[[:space:]]|$)' "${modules[@]}" 2>/dev/null; then
  echo "FAIL — a host-project-shaped import was found above."
  fail=1
else
  echo "PASS — no host-project imports in ${#modules[@]} module(s)."
fi

# --- Check 2: enforcer.py imports cleanly -----------------------------------
echo ""
echo "[2/3] clean import"
if "$PY" -c "
import sys
sys.path.insert(0, '$SRC')
import enforcer
print('PASS — enforcer imported without error.')
"; then
  :
else
  echo "FAIL — enforcer.py failed to import."
  fail=1
fi

# --- Check 3: negative controls for both guards (H5) ------------------------
# assert_no_hue_band: fixture that FIRES (a planted green, hue ~142deg) and
# one that does NOT (CFS's own accent blue, hue ~221deg — hand-checkable:
# #1D4ED8 -> R=29,G=78,B=216 -> hue in the 210-230 range, well outside any
# 75-175 band).
#
# assert_contrast_aa: fixture that FIRES (a fixture pair below 4.5:1 — pure
# mid-grey #949494 on white #FFFFFF is ~2.86:1, hand-computable from the
# WCAG relative-luminance formula) and one that does NOT (black #000000 on
# white #FFFFFF is exactly 21:1, the maximum possible ratio).
echo ""
echo "[3/3] negative controls for both guards (H5)"
if "$PY" -c "
import sys
sys.path.insert(0, '$SRC')
import enforcer

errors = []

# --- assert_no_hue_band: positive control (must fire) ---
try:
    enforcer.assert_no_hue_band({'light': {'ok': '#22C55E'}}, 75.0, 175.0, reason='test ban')
    errors.append('assert_no_hue_band did NOT fire on a planted green — guard is inert')
except enforcer.HueBandForbidden:
    pass

# --- assert_no_hue_band: negative control (must NOT fire) ---
try:
    enforcer.assert_no_hue_band({'light': {'accent': '#1D4ED8'}}, 75.0, 175.0)
except enforcer.HueBandForbidden:
    errors.append('assert_no_hue_band fired on #1D4ED8 (blue, hue ~221deg) — false positive')

# --- assert_contrast_aa: positive control (must fire) ---
try:
    enforcer.assert_contrast_aa('#949494', '#FFFFFF', 'normal')
    errors.append('assert_contrast_aa did NOT fire on a ~2.86:1 pair — guard is inert')
except enforcer.ContrastFailure:
    pass

# --- assert_contrast_aa: negative control (must NOT fire) ---
try:
    enforcer.assert_contrast_aa('#000000', '#FFFFFF', 'normal')
except enforcer.ContrastFailure:
    errors.append('assert_contrast_aa fired on black-on-white (21:1) — false positive')

if errors:
    for e in errors:
        print('FAIL —', e)
    sys.exit(1)
print('PASS — both guards fire on their positive control and stay silent on their negative control.')
"; then
  :
else
  echo "negative-control check failed."
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
