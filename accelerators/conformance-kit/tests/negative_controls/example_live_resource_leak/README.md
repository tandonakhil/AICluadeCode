# Negative control — `live_ledger_guard`

Demonstrates `src/live_ledger_guard.py` both firing (fire case) and staying
silent (non-fire case), per admission criterion H5.

## Fixture

`fixture_resource.py` defines a minimal stand-in for the "resource" the guard
watches — a class whose `__init__(self, path)` is the thing that must never be
called with the live path:

```python
class Resource:
    def __init__(self, path):
        self.path = path
```

## Fire case

```python
import live_ledger_guard as guard
from fixture_resource import Resource  # noqa: F401  (patched by install())
import fixture_resource

g = guard.install(
    module_path="fixture_resource",
    class_name="Resource",
    live_path="/tmp/example-live-resource.db",
)
try:
    fixture_resource.Resource("/tmp/example-live-resource.db")  # must raise
except guard.LiveResourceWriteAttempt:
    pass
else:
    raise AssertionError("guard did not fire on the live path")
assert len(g.drain()) == 1
guard.uninstall()
```

## Non-fire case

```python
import live_ledger_guard as guard
import fixture_resource

g = guard.install(
    module_path="fixture_resource",
    class_name="Resource",
    live_path="/tmp/example-live-resource.db",
)
fixture_resource.Resource("/tmp/example-scratch-resource.db")  # must NOT raise
guard.assert_nothing_was_refused(g)  # must not raise either
guard.uninstall()
```

Both cases exercise the same installed guard against the same class — only the
constructed path differs — which is what proves the guard discriminates on the
live path rather than firing unconditionally (which would be indistinguishable
from a guard that is simply broken).

See `tests/test_conformance_kit.py` for the pytest form of both cases.
