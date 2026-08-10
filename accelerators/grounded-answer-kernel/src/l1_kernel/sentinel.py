"""The refusal sentinel (F31).

ZERO IMPORTS. ONE LITERAL. ONE OPERATION.

AC-F31-12 requires that no regex, case-fold or substring operation exist
anywhere on the sentinel path, statically. That is achievable only if the path
is small enough to close, so the path is exactly two modules -- this one and
``app/model/content.py`` -- both with an empty import closure.

Deliberately absent: `re`, `.lower()`, `.upper()`, `.casefold()`, `.find()`,
`.index()`, `.search()`, `.match()`, and any `in` test against the literal. An
`in` test would make "the model happened to mention INSUFFICIENT_EVIDENCE while
answering" indistinguishable from "the model refused", which is a bypass in the
direction that matters.

The prompt module IMPORTS this constant rather than retyping the literal, so
there is exactly one occurrence of the token in ``app/`` outside the prompt text
it is interpolated into.

--------------------------------------------------------------------------
HARVEST NOTE (accelerators/grounded-answer-kernel, L1)
--------------------------------------------------------------------------
This file is harvested VERBATIM, unmodified, from
``projects/rate-case-analyzer/dev/app/grounding/sentinel.py`` (gate 10,
899 tests, 8 blocking suites). The prior review was explicit that diluting
this closure defeats its entire point, so nothing here was generalised,
renamed, or reformatted beyond this note. Do not add an import to this file.
If your project needs a different refusal literal, define a new module with
the same shape rather than parameterising this one -- a configurable literal
is one `.format()` call away from a substring test.

The docstring's references to ``app/model/content.py`` and AC-F31-* IDs are
RCA-specific and describe the source project's own verification trail, not
an obligation this accelerator imposes on you. They are left in place because
this file's provenance is itself part of what is being harvested (H6).
--------------------------------------------------------------------------
"""

INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


def is_refusal(content: str) -> bool:
    return content.strip().startswith(INSUFFICIENT_EVIDENCE)
