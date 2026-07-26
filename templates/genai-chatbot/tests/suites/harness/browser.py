"""
browser.py — rendered-UI verification harness (Playwright backend).

Why this exists: every automated check in this platform previously inspected
HTTP responses and HTML *source*. That cannot see what a visitor actually
sees. A real compounding-opacity bug (a CSS `opacity` multiplying with a
per-shape alpha, leaving an element effectively invisible) and several layout
defects shipped because no non-rendering reviewer could catch them — a human
had to report them by hand. This harness closes that gap.

Design constraints baked in:

* **Process lifecycle.** A browser or server started inside a subagent's turn
  dies when the turn ends. Everything here runs *synchronously within one
  command invocation*. Never background a browser from a suite; any long-lived
  app server must already be running (started by deploy-agent/orchestrator).
* **Honest degradation.** If Playwright or its browser binary is missing, we
  raise `HarnessUnavailable`, which the suite translates to exit code 4
  (STATIC-ONLY). A "could not verify" is always preferable to a false pass.
* **Second backend later.** Native/mobile verification (Maestro + simulator)
  is intended to plug in beside this one with the same assertion vocabulary.

Usage inside a `ux` suite scenario:

    from harness.browser import render, HarnessUnavailable

    def test_headline_is_actually_visible():
        with render("http://localhost:8100/") as page:
            h1 = page.locator("h1").first
            assert h1.is_visible()
            assert page.effective_opacity(h1) > 0.5   # the bug this catches
"""
from __future__ import annotations

import contextlib
import os
import pathlib


class HarnessUnavailable(RuntimeError):
    """Playwright (or its browser) isn't installed — report STATIC-ONLY, don't fail."""


def _require_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError as exc:  # pragma: no cover - environment-dependent
        raise HarnessUnavailable(
            "Playwright is not installed. Run:\n"
            "  .venv/bin/pip install playwright && .venv/bin/playwright install chromium\n"
            "Report this suite as STATIC-ONLY (exit 4), never as passing."
        ) from exc
    from playwright.sync_api import sync_playwright

    return sync_playwright


class Page:
    """Thin wrapper adding assertions about what actually renders."""

    def __init__(self, page):
        self._p = page

    def __getattr__(self, name):
        return getattr(self._p, name)

    def effective_opacity(self, locator) -> float:
        """Opacity as actually composited, including every ancestor.

        Plain `opacity` on one element is not enough: CSS opacity multiplies
        down the tree, which is exactly how an 'invisible but present' element
        slips past source-level review.
        """
        return float(
            locator.evaluate(
                """el => {
                    let o = 1, n = el;
                    while (n && n.nodeType === 1) {
                        const v = parseFloat(getComputedStyle(n).opacity);
                        if (!Number.isNaN(v)) o *= v;
                        n = n.parentElement;
                    }
                    return o;
                }"""
            )
        )

    def computed(self, locator, prop: str) -> str:
        return locator.evaluate(f"el => getComputedStyle(el).getPropertyValue({prop!r})")

    def has_horizontal_overflow(self) -> bool:
        """True if the page scrolls sideways — a layout defect, never intended."""
        return bool(
            self._p.evaluate(
                "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1"
            )
        )

    def visible_text(self) -> str:
        return self._p.inner_text("body")

    def screenshot_evidence(self, name: str, evidence_dir: str = "test-evidence") -> str:
        """Capture a screenshot into test-evidence/ for the per-scenario record."""
        d = pathlib.Path(evidence_dir) / "screenshots"
        d.mkdir(parents=True, exist_ok=True)
        path = d / f"{name}.png"
        self._p.screenshot(path=str(path), full_page=True)
        return str(path)


@contextlib.contextmanager
def render(url: str, *, width: int = 1280, height: int = 900, theme: str | None = None):
    """Load `url` in a real browser and yield a Page. Synchronous by design.

    `theme` may be "light" or "dark" to exercise both grounds — several real
    defects only appeared in one theme.
    """
    sync_playwright = _require_playwright()
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as exc:  # browser binary missing
            raise HarnessUnavailable(
                f"Chromium not available: {exc}\n"
                "Run: .venv/bin/playwright install chromium"
            ) from exc
        ctx = browser.new_context(
            viewport={"width": width, "height": height},
            color_scheme=theme if theme in {"light", "dark"} else None,
            reduced_motion="reduce" if os.environ.get("SUITE_REDUCED_MOTION") else None,
        )
        page = ctx.new_page()
        page.goto(url, wait_until="networkidle")
        try:
            yield Page(page)
        finally:
            ctx.close()
            browser.close()
