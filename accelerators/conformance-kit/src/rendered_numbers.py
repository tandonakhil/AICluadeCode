"""Reading the NUMBERS out of a rendered page, rather than searching it for a
string that happens to look like one.

GENERALIZED from
`projects/conclave-finance-studio/dev/backend/conclave_harness/rendered_numbers.py`.
The algorithm below is already domain-free — confirmed at harvest (2026-08-08):
no CFS module name, class or import appears in it. The one change made here is
to the default assertion message, which embedded CFS's own acceptance-criterion
ID (`AC-F12-15`); that is now an optional `criteria` label the caller supplies,
defaulting to nothing.

WHY THIS EXISTS — preserved from the source, because it is the whole argument
for the mechanism
------------------------------------------------------------------------------
In the source project, an acceptance criterion said a disclosed numeric band
(bounds `0.02`–`0.08`) must not be readable from the rendered product. Four
scenarios across three test files asserted that by searching the whole page
for the bare substrings `"0.02"` and `"0.08"` — the band's bounds. That
assertion was wrong in both directions at once:

  * it FAILED when nothing had leaked. Under one test ordering, a rendered
    timestamp `...T07:04:40.023468+00:00` contains `0.02` inside `40.023468`,
    and the scenario failed while both of its substantive assertions passed.
    Intermittent, because it depended on the wall-clock second the page was
    rendered in.
  * it PASSED when something had. `0.020` is the same value and is not the
    same substring; so is `.02`; so is any value actually drawn inside the
    band, such as `0.0473`, which is what an internal computation would have
    leaked if it ever leaked anything, since the bounds themselves are the two
    values a drawn value almost never takes.

So the check is done on numbers: tokenise the page's standalone numeric
literals, and assert none of them lands in the band. That is a STRONGER claim
than the substring pair it replaces — it covers the whole closed interval, not
its two endpoints — and it cannot collide with a timestamp, a document id or a
money amount, because a digit run that sits inside a longer numeric run is not
a token at all.
"""

from __future__ import annotations

import decimal
import re
from typing import Iterable, List, Optional, Set, Tuple

#: A standalone decimal literal.
#:
#: The lookaround is the whole point. `(?<![\d.,])` and `(?![\d.,])` mean a run
#: of digits that is part of a LONGER numeric run is not a token:
#:
#:   "40.023468"  -> one token, 40.023468.        Not 0.02, not 0.023468.
#:   "1.0.02"     -> no tokens at all.            A dotted version is not a value.
#:   "1,234.56"   -> no tokens at all.            Grouped money is not a rate.
#:   "rate: 0.02" -> one token, 0.02.             Which is exactly the leak.
#:
#: A leading `-` is deliberately NOT consumed: sign is irrelevant to whether a
#: value is readable, and `ITEM-21400` should tokenise to 21400 rather than to
#: nothing, so that an id which happens to encode a value is still caught.
_NUMERIC_TOKEN = re.compile(r"(?<![\d.,])(\d+(?:\.\d+)?)(?![\d.,])")


def decimal_tokens(text: str) -> Set[decimal.Decimal]:
    """Every standalone numeric literal in `text`, as exact decimals.

    Exact decimals rather than floats, so that `0.020` and `0.02` compare
    equal — they are the same value, and a check that distinguished them would
    be the substring check again under another name.
    """
    tokens: Set[decimal.Decimal] = set()
    for match in _NUMERIC_TOKEN.finditer(text):
        try:
            tokens.add(decimal.Decimal(match.group(1)))
        except decimal.InvalidOperation:  # pragma: no cover - regex forbids it
            continue
    return tokens


def numbers_in_band(text: str, band: Tuple[decimal.Decimal, decimal.Decimal]) -> List[decimal.Decimal]:
    """Every number on the page that lies in the closed interval `band`.

    Sorted, so an assertion message names the offenders in a stable order.
    Empty is the passing state; the caller asserts on that rather than being
    handed a bool, because a failure that cannot say WHICH number leaked sends
    the reader back to the page with a grep.
    """
    low, high = band
    if low > high:
        raise ValueError("band bounds are the wrong way round: {!r}".format(band))
    return sorted(token for token in decimal_tokens(text) if low <= token <= high)


def band_is_not_readable(
    text: str,
    band: Tuple[decimal.Decimal, decimal.Decimal],
    where: str = "",
    criteria: Optional[str] = None,
) -> None:
    """Raise `AssertionError` naming the leak, or return.

    Kept as a function rather than left to each caller so that every scenario
    that makes this claim makes the identical claim. In the source project
    they previously did not: two searched the markup, one searched
    `inner_text`, and one of the four also banned two prose phrases the others
    did not.

    `criteria` is an optional label (e.g. an acceptance-criterion ID) the
    caller supplies to appear in the failure message; it is config, not code —
    the source project's default baked in its own `AC-F12-15`, which this
    accelerator does not vendor as a default.
    """
    leaked = numbers_in_band(text, band)
    if leaked:
        suffix = f" ({criteria})" if criteria else ""
        raise AssertionError(
            "a number inside the undisclosed band {} is rendered at {}: {}{}".format(
                tuple(str(b) for b in band), where or "<unnamed surface>",
                [str(n) for n in leaked], suffix,
            )
        )


def any_band_is_not_readable(
    texts: Iterable[Tuple[str, str]],
    band: Tuple[decimal.Decimal, decimal.Decimal],
    criteria: Optional[str] = None,
) -> None:
    """`band_is_not_readable` over `(where, text)` pairs."""
    for where, text in texts:
        band_is_not_readable(text, band, where, criteria)
