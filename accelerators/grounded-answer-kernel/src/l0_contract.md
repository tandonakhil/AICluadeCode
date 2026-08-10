# L0 — the contract (read this before touching any code)

This layer is a **page of prose, not code**. It is the one piece of this
accelerator every adopting project should take, regardless of stack, vector
store, or whether it uses any other layer here. `L0` alone would have saved
most of `rate-case-analyzer`'s re-derivation of `policy-lookup-assistant`'s
grounding contract — the prior review's finding, restated here so it travels
with the code.

## The four laws

**1. Refusal is a structured signal, not prose.**
A refusal is a typed value the application recognises and routes on — never a
string the application greps, regexes, or substring-matches out of a model's
free-text answer. The moment a refusal is detected by `"INSUFFICIENT_EVIDENCE"
in response.text`, the model can defeat the detector by mentioning the refusal
token while actually answering, and no test will catch it because the test
suite has the same blind spot as the detector. `L1`'s sentinel exists because
this law needs to be *provably* upheld — no regex, no substring, no case-fold,
statically — not merely upheld by convention.

**2. `sources[]` is built by the application from what was verified, never
parsed from model output.**
The most dangerous hallucination is not a fabricated fact — it is a *real*
quote from a *real* source that does not actually support the claim next to
it. Showing retrieval hits beside an answer, or trusting a model-emitted
citation list, manufactures the appearance of support where none was checked.
The only sources a response may display are the ones a deterministic verifier
confirmed, and the function that builds them (`L1`'s `build_sources`) takes
**exactly one parameter** — the verified set — precisely so the raw retrieval
result can never be passed in and never masquerade as support.

**3. A refusal names the gap.**
"I don't have enough information" sends the user off to guess, which
reproduces the harm the tool exists to prevent, just outside the tool where
nothing can catch it. A refusal states *what dimension* is missing, and what
the system actually examined before declining — built from the coverage
record, never from the model's discarded prose.

**4. Silence is not clearance.**
An empty exceptions list must be distinguishable from a list that is empty
because nothing was examined. A coverage object that does not account for
every candidate it considered is not a coverage object — it is a claim nobody
checked. `L3`'s ledger exists to make that distinction a structural
impossibility to violate, not a convention to remember.

## What this contract does not say

It does not say which vector store to use, which model provider to call, or
how to shape a domain's assertion vocabulary. Those are `L2` and `L3`
decisions, made per adopter. `L0` is the one page that should not need
adapting.
