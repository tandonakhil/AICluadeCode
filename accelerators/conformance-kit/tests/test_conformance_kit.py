"""Executable form of the two negative controls documented under
`tests/negative_controls/`.

STATUS: written by `mas-registrar` at harvest time (2026-08-08/09) as a
pure-Python-importable pytest file. `mas-registrar` holds no `Bash` grant and
did NOT run this file — it is unverified-by-registrar, execution-pending at
first real vendor or at `code-agent`'s next invocation with a Python
interpreter available. See `ACCELERATOR.md`'s H4 section for the same
disclosure. Do not report this suite as EXECUTED until something with a
`Bash` grant has actually run it and can report a real exit code.

Run with: `pytest accelerators/conformance-kit/tests/` from the repo root, or
via `tests/run.sh` in this directory.
"""

from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "src"
NEG = HERE / "negative_controls"

sys.path.insert(0, str(SRC))
sys.path.insert(0, str(NEG / "example_live_resource_leak"))

import boundaries  # noqa: E402
import closure  # noqa: E402
import live_ledger_guard as guard  # noqa: E402
import rendered_numbers  # noqa: E402


# ---------------------------------------------------------------------------
# example_forbidden_import — fire and non-fire
# ---------------------------------------------------------------------------

def test_forbidden_import_fires_on_violating_tree():
    # package_root points AT the package dir itself (app/), not its parent --
    # matching RCA's own convention (`CONTROLS / name / "app"` in
    # test_boundaries.py). package_alias="app" reconstructs dotted names
    # relative to this root, so a parent-pointing root double-prefixes
    # every module name ("app.app.public.api") and the closure silently
    # finds nothing -- this was a real bug in this file's first draft,
    # caught by actually executing the suite rather than trusting the
    # STATIC ONLY marker.
    root = NEG / "example_forbidden_import" / "fixture_violates" / "app"
    boundary = boundaries.EXAMPLE_BOUNDARIES[0]
    assert boundary.name == "public-api-no-private-store"
    violations = closure.check(root, (boundary,))
    # A plain `from app.private.store import PrivateStore` reaches TWO
    # candidate module names -- "app.private.store" and the symbol-qualified
    # "app.private.store.PrivateStore" (direct_imports() emits both; see its
    # docstring-adjacent comment on `from x import y` resolution). Both match
    # the forbidden-module pattern and are correctly reported as separate
    # violations -- this is real behaviour of the unmodified checker, not a
    # fixture defect, confirmed by tracing direct_imports() by hand.
    assert len(violations) == 2
    assert all(v.boundary == "public-api-no-private-store" for v in violations)
    assert all("app.private.store" in v.detail for v in violations)


def test_forbidden_import_does_not_fire_on_clean_tree():
    root = NEG / "example_forbidden_import" / "fixture_clean" / "app"
    boundary = boundaries.EXAMPLE_BOUNDARIES[0]
    violations = closure.check(root, (boundary,))
    assert violations == ()


def test_pure_module_boundary_does_not_crash_when_its_root_is_absent():
    # The second example boundary (zero-import/zero-symbol) names a root,
    # app.core.pure, that the fixture trees above don't define. Checking it
    # against a tree that lacks that root must degrade to "no violations
    # found", not crash — a manifest entry for a module not yet written must
    # be inert, not an error.
    root = NEG / "example_forbidden_import" / "fixture_clean" / "app"
    boundary = boundaries.EXAMPLE_BOUNDARIES[1]
    violations = closure.check(root, (boundary,))
    assert violations == ()


# ---------------------------------------------------------------------------
# example_live_resource_leak — fire and non-fire
# ---------------------------------------------------------------------------

def test_live_resource_guard_fires_on_the_live_path(tmp_path):
    import fixture_resource

    live_path = str(tmp_path / "live.db")
    g = guard.install(
        module_path="fixture_resource",
        class_name="Resource",
        live_path=live_path,
    )
    try:
        try:
            fixture_resource.Resource(live_path)
        except guard.LiveResourceWriteAttempt:
            pass
        else:
            raise AssertionError("guard did not fire on the live path")
        assert len(g.drain()) == 1
    finally:
        guard.uninstall()


def test_live_resource_guard_does_not_fire_on_a_scratch_path(tmp_path):
    import fixture_resource

    live_path = str(tmp_path / "live.db")
    scratch_path = str(tmp_path / "scratch.db")
    g = guard.install(
        module_path="fixture_resource",
        class_name="Resource",
        live_path=live_path,
    )
    try:
        fixture_resource.Resource(scratch_path)  # must not raise
        guard.assert_nothing_was_refused(g)  # must not raise either
    finally:
        guard.uninstall()


# ---------------------------------------------------------------------------
# rendered_numbers — the false-fail / false-pass example from the source doc
# ---------------------------------------------------------------------------

def test_rendered_numbers_does_not_false_fail_on_a_timestamp():
    band = (Decimal("0.02"), Decimal("0.08"))
    text = "recorded at 2026-08-08T07:04:40.023468+00:00"
    # 0.023468 is inside the band as a VALUE, but the substring "0.02" living
    # inside "40.023468" is the false-fail this accelerator exists to avoid;
    # here the actual tokenised number is 40.023468, which is NOT in band.
    assert rendered_numbers.numbers_in_band(text, band) == []


def test_rendered_numbers_does_not_false_pass_on_a_reformatted_leak():
    band = (Decimal("0.02"), Decimal("0.08"))
    text = "the internal value was 0.020"
    # A bare substring check for "0.02"/"0.08" would miss "0.020" entirely.
    assert rendered_numbers.numbers_in_band(text, band) == [Decimal("0.020")]


def test_rendered_numbers_band_is_not_readable_raises_on_a_leak():
    band = (Decimal("0.02"), Decimal("0.08"))
    try:
        rendered_numbers.band_is_not_readable("0.047 shown", band, where="page")
    except AssertionError:
        pass
    else:
        raise AssertionError("expected a leak to be reported")


def test_rendered_numbers_band_is_not_readable_is_silent_when_clean():
    band = (Decimal("0.02"), Decimal("0.08"))
    rendered_numbers.band_is_not_readable("nothing in band here: 1.5, 200", band, where="page")
