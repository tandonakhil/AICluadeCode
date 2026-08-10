"""Generalized token guards — import-time enforcement, not a review comment.

Generalized from `conclave-finance-studio`'s `app/ui/tokens.py`, which hardcodes
one product's own invariant: "there is no green in this product." That
invariant is real and correct *for CFS* (`UX_KB` §3.2: green reads as "fine,
move on", which is the one affect a depleted reviewer must not be handed) but
it is CFS's rule, not a platform rule. A future project may need to ban a
different hue band (a medical product banning red-as-alarm outside a genuine
destructive action, say), or may need to ban no hue at all. So this module
exposes the CHECK as a configurable function rather than a hardcoded band —
see H2's config-vs-code table in `../ACCELERATOR.md`.

WHAT IS REUSED VERBATIM FROM `tokens.py`: `rgb()`, `hsl()`, `chroma()`,
`relative_luminance()`, `contrast_ratio()` — pure colour maths, no host
project's domain modules, no import beyond `colorsys` and `re` (H3 host
decoupling).

WHAT IS NEW: `assert_no_hue_band()` (CFS's `assert_no_green()` generalized to
accept `min_deg`/`max_deg`/`chroma_floor` as parameters instead of module
constants) and `assert_contrast_aa()` (CFS's per-test WCAG assertions,
lifted into a reusable function instead of being re-derived at every call
site as bespoke `assert ratio >= 4.5` lines).

WHAT IS DELIBERATELY NOT HERE: any actual palette. No CFS blue/risk-ramp, no
RCA navy/gold, no marketing teal/gold/rust, no LM terracotta/sage. Palette
values are chosen fresh by every adopting project — see `../ACCELERATOR.md`'s
admission statement on why a "default" palette would misrepresent this
accelerator's own basis for existing.
"""

from __future__ import annotations

import colorsys
import re
from typing import Dict, List, Tuple

_HEX = re.compile(r"^#(?:[0-9A-Fa-f]{6})$")


class BadToken(ValueError):
    """A token that is not a six-digit hex colour."""


class HueBandForbidden(ValueError):
    """A token landed inside a caller-configured forbidden hue band."""


class ContrastFailure(ValueError):
    """A foreground/background pair fails the requested WCAG level."""


# --------------------------------------------------------------------------
# colour maths — verbatim from tokens.py, no behavioural change
# --------------------------------------------------------------------------


def rgb(value: str) -> Tuple[float, float, float]:
    if not _HEX.match(value):
        raise BadToken("{!r} is not a #RRGGBB colour".format(value))
    return (
        int(value[1:3], 16) / 255.0,
        int(value[3:5], 16) / 255.0,
        int(value[5:7], 16) / 255.0,
    )


def hsl(value: str) -> Tuple[float, float, float]:
    """(hue in degrees, saturation, lightness)."""
    r, g, b = rgb(value)
    h, ell, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360.0, s, ell)


def chroma(value: str) -> float:
    r, g, b = rgb(value)
    return max(r, g, b) - min(r, g, b)


def relative_luminance(value: str) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb(value)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(foreground: str, background: str) -> float:
    a = relative_luminance(foreground)
    b = relative_luminance(background)
    lighter, darker = (a, b) if a >= b else (b, a)
    return (lighter + 0.05) / (darker + 0.05)


# --------------------------------------------------------------------------
# guard 1 — configurable hue-band refusal (generalized from assert_no_green)
# --------------------------------------------------------------------------


def is_in_hue_band(
    value: str, min_deg: float, max_deg: float, chroma_floor: float = 0.05
) -> bool:
    """True if `value` falls inside [min_deg, max_deg] AND has chroma above
    the floor. The chroma floor exists because a near-neutral grey can land
    at any hue by numerical accident (CFS's paper tones land at hue ~60) and
    is not a colour in any perceptual sense — it must be exempted by chroma,
    never by an allowlist of specific hex values."""
    if chroma(value) < chroma_floor:
        return False
    hue, _sat, _light = hsl(value)
    return min_deg <= hue <= max_deg


def assert_no_hue_band(
    palettes: Dict[str, Dict[str, str]],
    min_deg: float,
    max_deg: float,
    chroma_floor: float = 0.05,
    reason: str = "",
) -> None:
    """Raise `HueBandForbidden` if any token in any theme falls in the band.

    This is CFS's `assert_no_green()` with the band and the reason string
    taken as parameters instead of module constants `GREEN_HUE_MIN` (75) /
    `GREEN_HUE_MAX` (175). An adopting project that wants CFS's own rule
    reconstructs it by calling:

        assert_no_hue_band(THEMES, 75.0, 175.0, reason="there is no green ...")

    A project with no hue prohibition simply never calls this function —
    that is what H2's config-vs-code table means by "the mechanism is
    reused as-is; whether and what to ban is a project decision."
    """
    offenders: List[str] = []
    for theme, palette in palettes.items():
        for name, value in palette.items():
            if is_in_hue_band(value, min_deg, max_deg, chroma_floor):
                hue, sat, light = hsl(value)
                offenders.append(
                    "{}.{} = {} (hue {:.0f}deg, sat {:.2f}, light {:.2f})".format(
                        theme, name, value, hue, sat, light
                    )
                )
    if offenders:
        prefix = reason + ": " if reason else ""
        raise HueBandForbidden(
            prefix
            + "token(s) fell inside the forbidden hue band "
            + "[{:.0f}, {:.0f}] deg: ".format(min_deg, max_deg)
            + "; ".join(offenders)
        )


# --------------------------------------------------------------------------
# guard 2 — WCAG AA contrast assertion (lifted from bespoke per-test asserts)
# --------------------------------------------------------------------------

#: WCAG 2.x thresholds. "large" = >=18pt regular or >=14pt bold.
AA_NORMAL = 4.5
AA_LARGE = 3.0


def assert_contrast_aa(
    foreground: str, background: str, size: str = "normal", label: str = ""
) -> None:
    """Raise `ContrastFailure` unless the pair meets WCAG AA for `size`
    ("normal" or "large"). This is the assertion every source project wrote
    inline and separately (CFS's `test_every_ink_meets_aa_on_EVERY_ground`,
    RCA's per-pair hex comments, marketing's computed-verification comments)
    — lifted into one function so a future project's own token test file can
    call it directly instead of re-deriving `>= 4.5`/`>= 3.0` per assertion.
    """
    if size not in ("normal", "large"):
        raise ValueError("size must be 'normal' or 'large', got {!r}".format(size))
    threshold = AA_LARGE if size == "large" else AA_NORMAL
    ratio = contrast_ratio(foreground, background)
    if ratio < threshold:
        prefix = "{}: ".format(label) if label else ""
        raise ContrastFailure(
            "{}{} on {} is {:.4f}:1, below WCAG AA {} ({:.1f}:1 required)".format(
                prefix, foreground, background, ratio, size, threshold
            )
        )


def css_variables(palette: Dict[str, str]) -> str:
    """Unchanged utility from `tokens.py`: render a palette dict as a CSS
    custom-property declaration block, tokens sorted for a stable diff."""
    return "".join(
        "--{}:{};".format(name, value) for name, value in sorted(palette.items())
    )
