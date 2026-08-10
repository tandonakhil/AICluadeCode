"""Watches the RESOURCE, not the callers, for construction over a live path.

GENERALIZED from `projects/conclave-finance-studio/dev/backend/conclave_harness/live_ledger_guard.py`.
The original hardcoded the guarded class (`ges.broker.store.BrokerStore`) and
the live path getter (`default_store_path()`, resolving to
`dev/var/broker_db.sqlite3`, CFS's running pilot's live decision ledger).
Those are now parameters to `install()` — `module_path`, `class_name`,
`live_path` — everything else, including the reasoning below, carries over
unchanged.

WHAT WENT WRONG IN THE SOURCE PROJECT, TWICE — preserved verbatim because it
is the entire argument for building a guard shaped like this one rather than a
per-fixture fix
------------------------------------------------------------------------------
In `conclave-finance-studio`, `ges.main.create_app` resolved its broker
lazily: `broker_factory or default_broker_factory`, called on first use.
`default_broker_factory` built `BrokerStore(default_store_path())`, and
`default_store_path()` pointed at `dev/var/broker_db.sqlite3` — the
developer's live decision ledger, the one the running pilot wrote to.

So a fixture that called `create_app(...)` with no `broker_factory` built an
app that looked perfectly correct and passed every scenario, and the first
request that reached the broker appended rows to a file that was not the
test's, was outside the test harness's reach, and made a fresh clone and the
developer's own machine two different starting states. Nothing failed.

Commit `4e5ee47` fixed that in `tests/suites/` and wrote a scenario to hold
it. The scenario was scoped to the suites' own `ges_http` fixture, so it
passed straight over `backend/tests/conftest.py`, where `ges_app` and
`ges_stack` had the IDENTICAL defect: a unit-test file was still adding rows
to the live ledger on every run, after the "fix".

WHY THIS IS A GUARD AND NOT ANOTHER FIXTURE FIX
------------------------------------------------
Fixing the two remaining fixtures fixes today. It does not stop the next
`create_app(...)` written without a `broker_factory` — and the reason this
defect survived a targeted fix once already is that the check watched ONE
tree and one fixture by name.

This guard watches the resource instead of the callers. It refuses the
CONSTRUCTION of the guarded class over the live path, so every route to that
file is covered — a factory function, a script, a fixture not yet written, a
tree not yet created — and it is installed once per test session from each
tree's own conftest.

It deliberately does NOT patch the live-path getter itself. In the source
project that function had to keep returning the real path, because a
behavioural scenario elsewhere measured the live file's size with it, and a
redirected getter would have made that measurement vacuously pass. An
adopter reusing this pattern should check whether the same tension applies
to their own live-path getter before patching it too.

It both RAISES and RECORDS. Raising stops the write. Recording matters
because a test client built to swallow server exceptions turns the raise into
an anonymous failure with no explanation; the session teardown reads the
record and fails the run with the full message and the name of the test that
did it.
"""

from __future__ import annotations

import importlib
import os
from typing import List, Optional


class LiveResourceWriteAttempt(AssertionError):
    """Raised at the point of construction, and recorded on the guard."""


class Guard:
    """An installed guard. Holds what it refused, so a session can report it."""

    def __init__(self, live_path: str):
        self.live_path = live_path
        self.violations: List[str] = []

    def record(self, message: str) -> None:
        self.violations.append(message)

    def drain(self) -> List[str]:
        """Take the recorded violations and forget them.

        Used by the scenarios that PROVE the guard fires: they cause a
        violation on purpose, and a session-end check that then failed on
        their own deliberate violation would make the guard untestable.
        """
        taken = list(self.violations)
        self.violations = []
        return taken


#: The guard installed for the current session, if any. A module global
#: because the thing being guarded is a process-wide resource, and because the
#: scenarios that prove the guard fires need to reach it without every fixture
#: in every tree having to thread it through.
_ACTIVE: Optional[Guard] = None

#: How many conftests currently hold it. In the source project there are two
#: trees, and when both run in one pytest session both conftest fixtures that
#: call `install()` fire.
#:
#: This counter is the fix for a real defect, found by running the whole tree
#: shuffled rather than in file order: `install` used to build a NEW `Guard`
#: and lay a SECOND patch over the first, so the outermost patch recorded
#: refusals on one guard while a test asserted on the other. In file order the
#: two trees did not interleave and it passed; shuffled, three scenarios
#: failed. A guard that is wrong about who refused what is a guard that would
#: report a leak against the wrong tree.
_HOLDERS = 0

#: The unpatched `__init__` of the guarded class, held so that `uninstall`
#: restores it. The module owns the patch rather than a caller's test-framework
#: patch helper, because with two independent session-scoped installers the
#: FIRST one's teardown would otherwise silently disarm the guard while the
#: second still believed it held.
_ORIGINAL_INIT = None
_PATCHED_CLASS = None


def active() -> Optional[Guard]:
    return _ACTIVE


def holders() -> int:
    return _HOLDERS


def _message(path: str, resource_label: str) -> str:
    return (
        "a test tried to construct {} over the live resource path {}.\n"
        "The test that did it: {}\n"
        "This is almost always a factory or entry point called with no "
        "override for the resource's path — pass an explicit path over a "
        "tmp-path instance instead.".format(
            resource_label, path, os.environ.get("PYTEST_CURRENT_TEST", "<unknown>")
        )
    )


def install(*, module_path: str, class_name: str, live_path: str) -> Guard:
    """Refuse construction of `module_path.class_name` over `live_path`.

    `module_path`/`class_name`/`live_path` are CONFIG (see `ACCELERATOR.md`
    H2) — the algorithm below is the code half.

    Idempotent, and deliberately so: multiple conftests may call this, and
    when several trees run in one session the second caller must get the
    FIRST caller's guard rather than a second one laid on top. See
    `_HOLDERS`.
    """
    global _ACTIVE, _HOLDERS, _ORIGINAL_INIT, _PATCHED_CLASS

    _HOLDERS += 1
    if _ACTIVE is not None:
        return _ACTIVE

    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)

    live = os.path.abspath(live_path)
    guard = Guard(live)
    original_init = cls.__init__
    resource_label = f"{module_path}.{class_name}"

    def guarded_init(self, path, *args, **kwargs):
        if os.path.abspath(str(path)) == live:
            message = _message(live, resource_label)
            guard.record(message)
            raise LiveResourceWriteAttempt(message)
        return original_init(self, path, *args, **kwargs)

    cls.__init__ = guarded_init
    _ORIGINAL_INIT = original_init
    _PATCHED_CLASS = cls
    _ACTIVE = guard
    return guard


def uninstall() -> None:
    """Release one hold. The patch is lifted when the last holder lets go.

    A holder that releases early must not disarm the guard for the tree still
    running, which is why this counts rather than simply restoring.
    """
    global _ACTIVE, _HOLDERS, _ORIGINAL_INIT, _PATCHED_CLASS

    if _HOLDERS == 0:
        return
    _HOLDERS -= 1
    if _HOLDERS > 0:
        return

    if _PATCHED_CLASS is not None and _ORIGINAL_INIT is not None:
        _PATCHED_CLASS.__init__ = _ORIGINAL_INIT
    _ORIGINAL_INIT = None
    _PATCHED_CLASS = None
    _ACTIVE = None


def assert_nothing_was_refused(guard: Guard) -> None:
    """The session-end check. Fails the run, naming what happened.

    Separate from the raise so that a violation swallowed by a test client's
    exception-suppression mode still ends the run non-zero with its message
    intact rather than as an unexplained failure.
    """
    if guard.violations:
        raise AssertionError(
            "{} attempt(s) to write to the live resource during this "
            "session:\n\n{}".format(
                len(guard.violations), "\n\n".join(guard.violations)
            )
        )
