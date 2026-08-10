"""Abstention as a first-class output object, and the fourth RAG state (L3).

HARVEST NOTE: this file is carried over near-verbatim from
``conclave-finance-studio``'s ``backend/common/abstention.py``. It already
had ZERO imports beyond the stdlib (``decimal``, ``typing``) and no
domain-specific vocabulary baked into its code -- only its docstrings
reference CFS's own module boundary (``ges``/`app`) and its own KB
(``RESPONSIBLE_AI_KB``, register citations). Those references are left as
provenance/rationale (H6), not as an obligation this file imposes on an
adopter: the *module boundary* argument in the first docstring section
generalises directly ("whichever two processes / layers produce and render
an abstention in your system"), but the specific process names (`ges`,
`app`) are CFS's own and do not apply elsewhere.

MATURITY, STATED HONESTLY: CFS shipped through all 11 gates (3,158 scenarios
at Deploy, gate 10 Review closed 2026-08-06), but that scenario count covers
the whole product, not this module in isolation -- there is no module-scoped
test count for ``abstention.py`` the way RCA's 899/gate-10 figure is scoped
to the grounding+coverage kernel. Treat this file's provenance as "shipped
inside a gate-10 product" rather than "899-test proven" in the specific
sense L1/L3's coverage ledger can claim.

WHY THIS LIVES IN A SHARED MODULE (generalised from the source)
-----------------------------------------------------------------
An abstention is typically produced by one layer (a broker, an agent, a
retrieval/verification pipeline) and rendered by another (an API, a UI). If
each side encodes the abstention vocabulary independently, the vocabulary
drifts -- and the specific drift that matters is one side deciding an
abstention is a kind of failure. So the type set, the RAG mapping, and the
routing weights are defined once, here, and imported by both sides.

THE FOURTH STATE, AND WHY THREE IS THE BUG
------------------------------------------
A three-state red/amber/green has no way to say **"I could not establish
this."** Every item must be assigned a colour, so an item the system could
not conclude on gets whichever colour is least inconvenient -- and in a
close process the least inconvenient colour is green. If instead it is
forced to red, the abstention arrives on a reviewer's queue as an exception
they must clear, which is a tax on declining, and pushes abstention out.

`UNKNOWN` is therefore not a shade of amber and not a weak red. It is the
state that says the question was asked, work was done, and the answer could
not be established -- and it carries the named evidence gap that would
resolve it.

**THE INVARIANT THIS MODULE EXISTS TO HOLD: an abstention never renders as a
negative finding.** Not "usually", not "unless the queue is full". `RAG_FOR`
maps all six abstention types to `UNKNOWN`, `NEGATIVE_STATES` does not
contain `UNKNOWN`, and `AssuranceItem.is_negative_finding` is computed from
the state rather than set by a caller.

THE DENOMINATOR RULE, STATED AS CODE
-----------------------------------------------
`quality_denominator` returns the CONCLUDED count and nothing else, and
`rates()` reports abstentions as a named third figure. There is deliberately
no function in this module that divides concluded by
(concluded + abstained). The first time a headline number falls because
someone declined, somebody tunes declining down.

ADAPT PER PROJECT: the six ``AbstentionType`` entries (``AB1``..``AB6``) are
CFS's own taxonomy (evidence-insufficient, coverage-insufficient,
out-of-population, refused-by-design, ambiguous-resolution,
conflicting-evidence) and every ``trigger`` string names CFS-specific
concepts (a "declared resolution type", "G-RESTYPE"). Kept as-is because they
are a genuinely reusable STARTING TAXONOMY for a RAG abstention vocabulary,
not because they are domain-neutral -- rewrite the six triggers for your own
domain before wiring this in, same as L1's ``STATEMENT_TEMPLATES``.
"""

from __future__ import annotations

import decimal
from typing import Any, Dict, List, Optional, Sequence, Tuple

# --------------------------------------------------------------------------
# the six types
# --------------------------------------------------------------------------


class AbstentionType(object):
    __slots__ = ("code", "name", "trigger", "computed_by")

    def __init__(self, code: str, name: str, trigger: str, computed_by: str):
        self.code = code
        self.name = name
        self.trigger = trigger
        self.computed_by = computed_by

    def as_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "name": self.name,
            "trigger": self.trigger,
            "computed_by": self.computed_by,
        }


TYPES: Tuple[AbstentionType, ...] = (
    AbstentionType(
        "AB1",
        "evidence-insufficient",
        "The declared resolution type's evidence schema cannot be satisfied "
        "from in-scope certified data.",
        "broker",
    ),
    AbstentionType(
        "AB2",
        "coverage-insufficient",
        "The declared population is not fully covered, or snapshot "
        "staleness is beyond tolerance.",
        "broker",
    ),
    AbstentionType(
        "AB3",
        "out-of-population",
        "The request is outside the skill's declared scope. A typed decline "
        "for anything the corpus does not cover: silent absence is not an "
        "answer.",
        "broker",
    ),
    AbstentionType(
        "AB4",
        "refused-by-design",
        "The refusal registry -- a named, closed list of things this "
        "product declines to do, defined as code and not a bundle object.",
        "broker",
    ),
    AbstentionType(
        "AB5",
        "ambiguous-resolution",
        "Two or more resolution types are equally supported by the "
        "evidence held. A STRUCTURAL test over the evidence schema, not a "
        "probability the model volunteers.",
        "broker",
    ),
    AbstentionType(
        "AB6",
        "conflicting-evidence",
        "Sources disagree -- e.g. a warehouse-to-source-of-record tie-out "
        "break.",
        "broker",
    ),
)

CODES: Tuple[str, ...] = tuple(t.code for t in TYPES)
_BY_CODE = {t.code: t for t in TYPES}


def abstention_type(code: str) -> AbstentionType:
    try:
        return _BY_CODE[code]
    except KeyError:
        raise KeyError(
            "{!r} is not an abstention type. The set is closed at {}; an "
            "abstention with an unlisted type is an untyped decline, which "
            "is the silent gap this module refuses.".format(code, ", ".join(CODES))
        )


# --------------------------------------------------------------------------
# the four-state RAG
# --------------------------------------------------------------------------

GREEN = "green"
AMBER = "amber"
RED = "red"
UNKNOWN = "unknown"

RAG_STATES: Tuple[str, ...] = (GREEN, AMBER, RED, UNKNOWN)

#: The states that mean "something is wrong here". UNKNOWN IS NOT ONE OF THEM
#: and never becomes one: an abstention is not a finding against the item,
#: it is the system declining to conclude about the item.
NEGATIVE_STATES: Tuple[str, ...] = (RED,)

#: Every abstention type maps here. All six map to UNKNOWN -- the mapping is
#: total and constant, so there is no type for which "well, that one really
#: is a problem" can creep in.
RAG_FOR: Dict[str, str] = {code: UNKNOWN for code in CODES}


class Abstention(object):
    """A recorded, typed decline to conclude.

    Note what is absent: no `confidence`, no `score`, no `severity`. A model
    reporting its own confidence is a model asked to police itself, and a
    severity on an abstention is the first step to sorting abstentions next
    to exceptions.
    """

    __slots__ = (
        "type",
        "type_code",
        "item_ref",
        "evidence_gap",
        "resolving_action",
        "period",
        "principal_id",
        "detail",
    )

    def __init__(
        self,
        type_code: str,
        item_ref: str,
        evidence_gap: str,
        resolving_action: str,
        period: int,
        principal_id: str = "",
        detail: Optional[Dict[str, Any]] = None,
    ):
        # The type is validated on construction, so an untyped abstention is
        # not constructible rather than being caught at render time.
        self.type = abstention_type(type_code)
        if not evidence_gap.strip():
            raise ValueError(
                "an abstention must NAME its evidence gap. An abstention "
                "that cannot say what is missing is a silent gap wearing a "
                "type code, and it routes to a human who then has nothing "
                "to act on"
            )
        if not resolving_action.strip():
            raise ValueError(
                "an abstention must carry exactly one resolving action "
                "(supply this / escalate). Abstention must be CHEAPER for "
                "the human than a conclusion"
            )
        self.type_code = type_code
        self.item_ref = item_ref
        self.evidence_gap = evidence_gap
        self.resolving_action = resolving_action
        self.period = period
        self.principal_id = principal_id
        self.detail = dict(detail or {})

    @property
    def rag(self) -> str:
        return RAG_FOR[self.type_code]

    @property
    def is_negative_finding(self) -> bool:
        """Computed from the state. Not a field, so no caller can set it."""
        return self.rag in NEGATIVE_STATES

    @property
    def is_error(self) -> bool:
        return False

    @property
    def counts_as_coverage(self) -> bool:
        """An abstained item WAS evaluated.

        If abstaining degraded the run's coverage statement, the design
        would carry a direct incentive to conclude.
        """
        return True

    def as_dict(self) -> Dict[str, Any]:
        return {
            "kind": "Abstention",
            "type": self.type_code,
            "type_name": self.type.name,
            "item_ref": self.item_ref,
            "evidence_gap": self.evidence_gap,
            "resolving_action": self.resolving_action,
            "period": self.period,
            "principal_id": self.principal_id,
            "rag": self.rag,
            "is_negative_finding": self.is_negative_finding,
            "is_error": self.is_error,
            "counts_as_coverage": self.counts_as_coverage,
            "detail": dict(self.detail),
        }


# --------------------------------------------------------------------------
# the denominator rule
# --------------------------------------------------------------------------


class DenominatorViolation(Exception):
    """Raised when a caller tries to build the forbidden ratio."""


def quality_denominator(concluded: int, abstained: int) -> int:
    """The denominator of any quality figure is CONCLUDED items.

    `abstained` is accepted and deliberately ignored, so that a caller who
    passes it gets the right answer rather than being tempted to compute
    `concluded / (concluded + abstained)` themselves.
    """
    return concluded


def rates(concluded: int, abstained: int, correct: int) -> Dict[str, Any]:
    """Precision and automation over CONCLUDED items, with abstentions as a
    named third figure -- never folded into either."""
    if correct > concluded:
        raise ValueError("correct cannot exceed concluded")
    denominator = quality_denominator(concluded, abstained)
    precision = (
        format(
            (decimal.Decimal(correct) / decimal.Decimal(denominator)).quantize(
                decimal.Decimal("0.0001")
            ),
            "f",
        )
        if denominator
        else None
    )
    return {
        "concluded": concluded,
        "abstained": abstained,
        "correct": correct,
        "precision_denominator": denominator,
        "precision": precision,
        # Stated so a reader of the payload cannot mistake the base.
        "precision_is_over": "concluded_items_only",
        "abstentions_are_a_named_third_figure": True,
    }


# --------------------------------------------------------------------------
# the abstention band -- BOTH tails
# --------------------------------------------------------------------------


class BandResult(object):
    __slots__ = ("skill_id", "period", "abstained", "evaluated", "rate", "verdict", "finding")

    def __init__(self, skill_id, period, abstained, evaluated, rate, verdict, finding):
        self.skill_id = skill_id
        self.period = period
        self.abstained = abstained
        self.evaluated = evaluated
        self.rate = rate
        self.verdict = verdict
        self.finding = finding

    def as_dict(self) -> Dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "period": self.period,
            "abstained": self.abstained,
            "evaluated": self.evaluated,
            "rate": self.rate,
            "verdict": self.verdict,
            "finding": self.finding,
        }


#: Verdicts. `at_or_near_zero` is a CONTROL finding and `above_band` is a
#: usefulness finding -- different severities, different owners.
IN_BAND = "in_band"
ABOVE_BAND = "above_band"
AT_OR_NEAR_ZERO = "at_or_near_zero"


def evaluate_band(
    skill_id: str,
    period: int,
    abstained: int,
    evaluated: int,
    band: Tuple[str, str],
    near_zero_at: str = "0.01",
) -> BandResult:
    """Zero abstentions is a finding, and a RED one.

    An agent that never declines on real data is either miscalibrated or its
    abstention path is dead code. Both tails are monitored, so this cannot be
    satisfied by an agent that abstains on everything either.
    """
    low, high = decimal.Decimal(band[0]), decimal.Decimal(band[1])
    if low > high:
        raise ValueError("abstention band low > high")
    if evaluated <= 0:
        raise ValueError(
            "an abstention band over zero evaluated items is not a measurement"
        )
    rate = (decimal.Decimal(abstained) / decimal.Decimal(evaluated)).quantize(
        decimal.Decimal("0.0001")
    )
    if rate <= decimal.Decimal(near_zero_at):
        verdict = AT_OR_NEAR_ZERO
        finding = {
            "severity": "control",
            "routed_to": "control_owner",
            "statement": (
                "{} abstained on {} of {} evaluated items in period {}. An "
                "agent that never declines on real data is either "
                "miscalibrated or its abstention path is dead code."
            ).format(skill_id, abstained, evaluated, period),
        }
    elif rate > high:
        verdict = ABOVE_BAND
        finding = {
            "severity": "usefulness",
            "routed_to": "skill_owner",
            "statement": (
                "{} abstained on {} of {} evaluated items in period {}, "
                "above its declared band."
            ).format(skill_id, abstained, evaluated, period),
        }
    else:
        verdict = IN_BAND
        finding = None
    return BandResult(skill_id, period, abstained, evaluated, format(rate, "f"), verdict, finding)


# --------------------------------------------------------------------------
# no user-facing control reduces abstention
# --------------------------------------------------------------------------

#: Settings a user is never offered. Named so the check is a list somebody
#: has to delete from, not an absence somebody has to notice.
FORBIDDEN_USER_CONTROLS = (
    "be_more_decisive",
    "confidence_threshold",
    "confidence_slider",
    "abstention_rate_target",
    "min_confidence",
    "suppress_abstentions",
    "auto_conclude_when_ambiguous",
)


def assert_no_abstention_control(settings: Dict[str, Any]) -> None:
    """Changing abstention behaviour is a versioned skill-definition change
    under change control, never a toggle."""
    offending = sorted(set(settings) & set(FORBIDDEN_USER_CONTROLS))
    if offending:
        raise ValueError(
            "user-facing setting(s) {} would change abstention behaviour. "
            "Abstention behaviour changes by a versioned skill-definition "
            "change under change control".format(offending)
        )


# --------------------------------------------------------------------------
# routing
# --------------------------------------------------------------------------


def routing_cost(items: Sequence[Any], concluded_weight: int, abstention_weight: int) -> int:
    """An abstention must not consume the routing budget at the weight of a
    full review, or abstention becomes a tax on the reviewer."""
    if abstention_weight >= concluded_weight:
        raise ValueError(
            "abstention_routing_weight ({}) must be strictly less than "
            "concluded_routing_weight ({}); otherwise declining costs the "
            "reviewer at least as much as concluding and the organisation "
            "pushes abstention out".format(abstention_weight, concluded_weight)
        )
    total = 0
    for item in items:
        total += abstention_weight if isinstance(item, Abstention) else concluded_weight
    return total


# --------------------------------------------------------------------------
# the shared render: conclusions and abstentions through ONE mapping
# --------------------------------------------------------------------------


class AssuranceItem(object):
    """One row on a status surface, whatever produced it.

    Conclusions and abstentions render through this single object on
    purpose. If abstentions had their own renderer, "an abstention never
    renders as a negative finding" would be a property of one code path and
    a hope about the other -- and the surface that sorts, filters or counts
    by colour is exactly where the two paths meet.
    """

    __slots__ = ("item_ref", "rag", "statement", "source_kind", "abstention_type", "detail")

    def __init__(
        self,
        item_ref: str,
        rag: str,
        rendered_text: str,
        source_kind: str,
        abstention_type_code: str = "",
        detail: Optional[Dict[str, Any]] = None,
    ):
        if rag not in RAG_STATES:
            raise ValueError(
                "{!r} is not one of the four states {}. A fifth state is how "
                "'could not establish' gets quietly re-encoded as a shade of "
                "something else".format(rag, RAG_STATES)
            )
        if source_kind not in ("conclusion", "abstention"):
            raise ValueError("source_kind must be 'conclusion' or 'abstention'")
        if source_kind == "abstention" and rag != UNKNOWN:
            raise ValueError(
                "an abstention rendered as {!r}. Every abstention is "
                "UNKNOWN; this constructor refuses the other three rather "
                "than trusting each caller to map correctly".format(rag)
            )
        self.item_ref = item_ref
        self.rag = rag
        self.statement = rendered_text
        self.source_kind = source_kind
        self.abstention_type = abstention_type_code
        self.detail = dict(detail or {})

    @property
    def is_negative_finding(self) -> bool:
        """Computed from the state. There is no setter and no field."""
        return self.rag in NEGATIVE_STATES

    @property
    def counts_as_coverage(self) -> bool:
        return True

    def as_dict(self) -> Dict[str, Any]:
        return {
            "item_ref": self.item_ref,
            "rag": self.rag,
            "statement": self.statement,
            "source_kind": self.source_kind,
            "abstention_type": self.abstention_type,
            "is_negative_finding": self.is_negative_finding,
            "counts_as_coverage": self.counts_as_coverage,
            "detail": dict(self.detail),
        }


def item_for_abstention(abstention: "Abstention") -> AssuranceItem:
    return AssuranceItem(
        item_ref=abstention.item_ref,
        rag=abstention.rag,
        rendered_text=(
            "This could not be established. {} Resolve by: {}"
        ).format(abstention.evidence_gap, abstention.resolving_action),
        source_kind="abstention",
        abstention_type_code=abstention.type_code,
        detail=dict(abstention.detail),
    )


def item_for_conclusion(
    item_ref: str, rendered_text: str, has_exception: bool, fully_covered: bool
) -> AssuranceItem:
    """The other three states, for completeness of the mapping.

    RED requires an exception actually found. There is no path from "we
    could not tell" to RED here, because there is no argument to this
    function that could express it -- that case is an Abstention and goes
    through `item_for_abstention`.
    """
    if has_exception:
        rag = RED
    elif fully_covered:
        rag = GREEN
    else:
        rag = AMBER
    return AssuranceItem(item_ref, rag, rendered_text, "conclusion")


def negative_findings(items: Sequence[AssuranceItem]) -> List[AssuranceItem]:
    """The exception list a reviewer works. Abstentions are not in it."""
    return [i for i in items if i.is_negative_finding]


def unknowns(items: Sequence[AssuranceItem]) -> List[AssuranceItem]:
    """The separate, named third list. Not a subset of the exception list."""
    return [i for i in items if i.rag == UNKNOWN]
