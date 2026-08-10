"""
native.py — rendered-UI verification harness (React Native Testing Library backend).

The sibling of `browser.py`, for native surfaces. Same job, same vocabulary,
same honest-degradation rule; different backend.

Why this exists, specifically
-----------------------------
`test-agent` made rendered-UI verification contractual on 2026-07-26 — and the
F18 mobile build then shipped six rendering defects anyway. The reason was not
neglect: the capability had exactly ONE built backend, Playwright, which cannot
load a React Native tree. The intended native backend (Maestro + simulator) was
deferred when the toolchain spike found no simulator available. So for a React
Native surface the contract was live and the capability was empty, and defects
of this shape were structurally uncatchable:

  * `Avatar` built, imported, never rendered.
  * `RemoteImage`/`Lightbox`/gallery built, state-managed, never mounted.
  * `ChatHistorySheet` imported AND state-managed AND never mounted.

All three are invisible to typecheck, to the bundler, and to every API test, by
construction. The one that *was* caught without a human was caught by RNTL.

RNTL is the right backend for this tier because it needs **no simulator and no
emulator** — it renders the real component tree in-process, in about a second.
That is what makes it runnable inside a suite's turn at all. Maestro + simulator
remains the deeper backend for true end-to-end flows and is still future work;
this does not replace it, it fills the gap beneath it.

The rule that makes it actually work
------------------------------------
A reachability test MUST render from the screen's or app's real entry point and
assert the component appears in the resulting tree. Rendering the component
directly proves only that it compiles:

    render(<Avatar />)            # passes while Avatar is mounted nowhere
    render(<TodayScreen />)       # fails until Avatar is actually wired in

That distinction is the whole point. Every one of the defects above would have
passed the first form.

Design constraints, inherited from `browser.py`
----------------------------------------------
* **Process lifecycle.** Everything runs synchronously inside one command
  invocation. No watcher, no long-lived process — a process started inside a
  subagent's turn dies with the turn.
* **Honest degradation.** Missing toolchain raises `HarnessUnavailable`, which
  the suite translates to exit code 4 (STATIC-ONLY). "Could not verify" must
  never render as "verified".

Usage inside a suite scenario:

    from harness.native import run_native_render_tests, HarnessUnavailable

    def test_mobile_components_are_reachable():
        result = run_native_render_tests()
        assert result.passed, result.summary
"""
from __future__ import annotations

import dataclasses
import json
import pathlib
import shutil
import subprocess


class HarnessUnavailable(RuntimeError):
    """The native toolchain isn't installed — report STATIC-ONLY, don't fail."""


DEV_ROOT = pathlib.Path(__file__).resolve().parents[3]
MOBILE = DEV_ROOT / "mobile"


@dataclasses.dataclass
class NativeResult:
    passed: bool
    total: int
    failed: int
    summary: str

    def __bool__(self) -> bool:  # pragma: no cover - convenience
        return self.passed


def _require_toolchain() -> pathlib.Path:
    if not MOBILE.is_dir():
        raise HarnessUnavailable(
            f"No native surface at {MOBILE} — this project has no mobile app. "
            "Report STATIC-ONLY (exit 4), never passing."
        )
    if not (MOBILE / "node_modules").is_dir():
        raise HarnessUnavailable(
            f"{MOBILE}/node_modules missing. Run `npm install` in mobile/. "
            "Report this suite as STATIC-ONLY (exit 4), never as passing."
        )
    npx = shutil.which("npx")
    if npx is None:
        raise HarnessUnavailable(
            "npx not on PATH — cannot drive jest/RNTL. Report STATIC-ONLY (exit 4)."
        )
    return pathlib.Path(npx)


def run_native_render_tests(pattern: str | None = None, timeout: int = 300) -> NativeResult:
    """Run the RNTL component-render suite and report structured results.

    Synchronous and short-lived by design. `pattern` narrows to a subset
    (jest's `-t`). Raises `HarnessUnavailable` rather than failing when the
    toolchain is absent, so a missing backend can never masquerade as a pass.
    """
    npx = _require_toolchain()
    cmd = [str(npx), "jest", "--json", "--silent"]
    if pattern:
        cmd += ["-t", pattern]

    try:
        proc = subprocess.run(
            cmd, cwd=MOBILE, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired as exc:
        raise HarnessUnavailable(f"jest exceeded {timeout}s — treat as unverified") from exc
    except OSError as exc:  # pragma: no cover - environment-dependent
        raise HarnessUnavailable(f"could not launch jest: {exc}") from exc

    # jest writes its JSON report to stdout; a crash before that leaves it empty.
    payload = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                payload = json.loads(line)
                break
            except json.JSONDecodeError:
                continue

    if payload is None:
        raise HarnessUnavailable(
            "jest produced no parseable report — toolchain misconfigured.\n"
            f"stderr tail: {proc.stderr[-400:]}"
        )

    total = int(payload.get("numTotalTests", 0))
    failed = int(payload.get("numFailedTests", 0))

    if total == 0:
        # An empty run is NOT a pass — same rule the suite runner applies.
        raise HarnessUnavailable(
            "jest ran zero tests. An empty suite is not a passing suite; "
            "report STATIC-ONLY (exit 4)."
        )

    return NativeResult(
        passed=failed == 0 and proc.returncode == 0,
        total=total,
        failed=failed,
        summary=f"{total - failed}/{total} native render tests passed",
    )


def reachable_components(screen_sources: dict[str, str]) -> dict[str, list[str]]:
    """Static companion check: which components each screen actually renders.

    Cheap and deliberately narrow — it reports JSX element names found in each
    source. It exists to pair with the RNTL run, not to replace it: static
    analysis cannot see conditional rendering or dynamic imports, and RNTL
    cannot cheaply enumerate every screen. Together they cover more than either
    does alone.
    """
    import re

    out: dict[str, list[str]] = {}
    for name, src in screen_sources.items():
        out[name] = sorted(set(re.findall(r"<([A-Z][A-Za-z0-9_]*)", src)))
    return out
