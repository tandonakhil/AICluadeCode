# Negative control — `public-api-no-private-store`

Demonstrates `src/boundaries.py` + `src/closure.py` both catching a real
violation (fire case) and staying silent on a clean tree (non-fire case), per
admission criterion H5 — a guard admitted without a fixture proving it can
also *not* fire is a guard nobody has confirmed can fail.

Modelled on `rate-case-analyzer`'s `tests/negative_controls/wall_breach/`,
which is the same pattern against the real `public-answer-path` boundary.

## Fixtures

- `fixture_violates/app/` — `app.public.api` imports
  `app.private.store.PrivateStore` directly. Pointing `closure.check()` at
  this tree with the `public-api-no-private-store` boundary from
  `src/boundaries.py` must return exactly one `Violation` naming
  `app.public.api -> app.private.store`.
- `fixture_clean/app/` — same module names, same shapes, but `app.public.api`
  never imports the private store. Pointing `closure.check()` at this tree
  with the same boundary must return zero violations.

Neither fixture is a mutation of the accelerator's own `src/` — both are
free-standing sample package trees that exist only to be pointed at by the
checker. No mutation ever touches `src/`.

## How to reproduce (unexecuted by this harvest — see `ACCELERATOR.md`)

```python
from pathlib import Path
from boundaries import EXAMPLE_BOUNDARIES
from closure import check

fire = check(Path("fixture_violates"), EXAMPLE_BOUNDARIES[:1])
assert len(fire) == 1

no_fire = check(Path("fixture_clean"), EXAMPLE_BOUNDARIES[:1])
assert len(no_fire) == 0
```

See `tests/test_conformance_kit.py` for the pytest form of this.
