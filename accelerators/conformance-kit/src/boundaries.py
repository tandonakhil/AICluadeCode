"""The machine-readable import-boundary manifest format, with a worked example.

**Data, not code.** Each `Boundary` entry names a set of root modules, a set of
module patterns their TRANSITIVE import closure may not contain, and
optionally a set of symbols that may not appear anywhere in that closure. The
checker that reads this shape lives in `closure.py` (this package) and is a
pure function of a package root path — which is what makes negative controls
cheap and non-destructive: the same function is pointed at a mutated fixture
tree under `tests/negative_controls/`, and no mutation ever touches the real
source tree.

GENERALIZED from `projects/rate-case-analyzer/dev/app/boundaries.py`. The
source file held **fourteen** boundaries naming RCA's own package layout
(`app.answer.public_path`, `app.stores.workproduct_store`, acceptance-criterion
IDs like `AC-F22-03`, and so on) — those are RCA's product law, not a
reusable payload, and are not vendored here. What *is* reusable, and is
vendored below, is the manifest **format** (the `Boundary` dataclass) plus two
worked examples that reproduce the two shapes RCA's fourteen boundaries
actually took:

  1. a plain forbidden-module rule ("this root may not reach that module"),
     modelled on RCA's `public-answer-path`;
  2. a zero-import, zero-symbol rule ("this root's closure must be empty, and
     it may not case-fold or regex anything"), modelled on RCA's
     `sentinel-path-is-bare` — the boundary that made AC-F31-12 ("no regex,
     case-fold or substring operation exists anywhere in the sentinel path,
     statically") checkable rather than merely reviewable.

Replace `EXAMPLE_BOUNDARIES` with your own manifest. Nothing in `closure.py`
depends on the *names* used here.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Boundary:
    name: str
    roots: tuple[str, ...]
    forbidden_modules: tuple[str, ...] = ()
    forbidden_symbols: tuple[str, ...] = ()
    except_modules: tuple[str, ...] = ()
    #: When True the rule applies to the roots' OWN import statements only, not
    #: to their transitive closure. Used where a transitive rule would be
    #: unsatisfiable but a direct rule still carries the invariant. (RCA hit
    #: this exact case: a rule written as transitive was unsatisfiable because
    #: the forbidden module was necessarily in every caller's closure by
    #: construction — see `web-never-composes-directly` in the source file's
    #: history for the worked judgment call.)
    direct_only: bool = False
    rationale: str = ""
    criteria: tuple[str, ...] = field(default_factory=tuple)


#: EXAMPLE MANIFEST — replace with your own. Kept deliberately small: two
#: boundaries demonstrating the two shapes a rule commonly takes. Module names
#: below (`app.public.api`, `app.private.store`, `app.core.pure`) are
#: placeholders; they do not need to exist for the *shape* to be useful as a
#: template, but the accelerator's own tests point `closure.py` at real
#: fixture trees using these same names — see
#: `tests/negative_controls/example_forbidden_import/`.
EXAMPLE_BOUNDARIES: tuple[Boundary, ...] = (
    Boundary(
        name="public-api-no-private-store",
        roots=("app.public.api",),
        forbidden_modules=("app.private.store",),
        rationale=(
            "A public-facing module must have NO CODE PATH to a private/"
            "internal data store — not a path that returns empty, and not a "
            "filtered view. Modelled on rate-case-analyzer's "
            "'public-answer-path' boundary, which made exactly this property "
            "of its public-answer surface a structural fact rather than a "
            "convention."
        ),
        criteria=("EXAMPLE-1",),
    ),
    Boundary(
        name="pure-module-is-bare",
        roots=("app.core.pure",),
        forbidden_modules=("*",),
        forbidden_symbols=("re", "regex", "lower", "upper", "casefold", "find"),
        rationale=(
            "A zero-import, zero-case-fold boundary: the root's import "
            "closure must be EMPTY, and it may not perform a case-fold, "
            "regex or substring operation. Modelled on rate-case-analyzer's "
            "'sentinel-path-is-bare' boundary (AC-F31-12), achievable only "
            "because the guarded path was kept small enough to close: "
            "exactly two modules, both with an empty import closure."
        ),
        criteria=("EXAMPLE-2",),
    ),
)

#: Alias kept for drop-in replacement: an adopter typically renames this
#: module's `EXAMPLE_BOUNDARIES` to `BOUNDARIES` once real boundaries replace
#: the two examples above.
BOUNDARIES: tuple[Boundary, ...] = EXAMPLE_BOUNDARIES
BOUNDARY_NAMES: tuple[str, ...] = tuple(b.name for b in BOUNDARIES)
