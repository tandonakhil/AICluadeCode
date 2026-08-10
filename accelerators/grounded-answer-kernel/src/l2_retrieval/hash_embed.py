"""Deterministic, offline, stdlib+numpy embedding and ranking (L2).

UNMODIFIED LOGIC, harvested from ``rate-case-analyzer``'s
``app/retrieval/rank.py``. This is what makes an adopting project's test
suites runnable with **zero API credentials**: ``hash_embed`` needs no
network call and no API key, so ingest, retrieve, and refuse paths can all
run in CI with no live model or embedding provider present.

``rank_within`` is a **pure function of the set it is handed**. It never
touches a store, so it cannot return a chunk that was not passed to it --
"the ranked set is a subset of the filtered set" is therefore an assertion
about a function signature, not about behaviour.

The similarity value never leaves this module. It is an ordering key, not a
datum: it must never be carried on an evidence object or a comparability
object, because embedding quality is an ORDERING concern here, never a
correctness one -- embeddings only rank within an already-correct candidate
set.

Embedding quality is a ranking convenience, not a correctness guarantee.
``hash_embed`` is deliberately crude (a signed hash-bucket bag-of-tokens
vector); production-quality ranking is what the credentialed L2 adapter
(Chroma, OpenAI embeddings, or similar) is for. See ACCELERATOR.md's H2
config table: this file IS the "offline/deterministic" side of L2's central
config decision.
"""

from __future__ import annotations

import hashlib
from typing import Mapping, Sequence

import numpy as np

EMBEDDING_DIM = 256


def hash_embed(text: str, dim: int = EMBEDDING_DIM) -> tuple[float, ...]:
    """A deterministic, offline, stdlib-only embedder.

    Embedding quality is an ORDERING concern here, never a correctness one --
    embeddings only rank within an already-correct candidate set -- which is
    why swapping to this offline embedder changes no correctness assertion.
    Use it as the default so ingest, retrieve, refuse and render all run with
    no API key present.
    """
    vector = np.zeros(dim, dtype=np.float32)
    tokens = [t for t in text.lower().replace("\n", " ").split(" ") if t]
    for token in tokens:
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        index = int.from_bytes(digest[:4], "big") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[index] += sign
    norm = float(np.linalg.norm(vector))
    if norm > 0.0:
        vector /= norm
    return tuple(float(x) for x in vector)


def rank_within(
    candidate_ids: Sequence[str],
    query_vector: Sequence[float],
    embeddings: Mapping[str, Sequence[float]],
    k: int,
) -> tuple[str, ...]:
    """Order ``candidate_ids`` by cosine similarity and take the top ``k``.

    Candidates with no embedding keep their filtered order after the ranked
    ones -- they are never dropped, because dropping them would silently
    narrow the candidate set a coverage ledger has already been given.
    """
    if not candidate_ids:
        return ()
    query = np.asarray(query_vector, dtype=np.float32)
    query_norm = float(np.linalg.norm(query))

    scored: list[tuple[float, int, str]] = []
    unscored: list[str] = []
    for position, chunk_id in enumerate(candidate_ids):
        vector = embeddings.get(chunk_id)
        if not vector or query_norm == 0.0:
            unscored.append(chunk_id)
            continue
        # A stored vector of a different dimension is a real corpus condition
        # -- it is what a partially re-embedded corpus looks like. It must
        # degrade to "unranked", never raise: an exception here would take
        # down the whole answer path, and the candidate must stay in the set
        # either way because a coverage ledger has already counted it.
        if len(vector) != len(query):
            unscored.append(chunk_id)
            continue
        candidate = np.asarray(vector, dtype=np.float32)
        candidate_norm = float(np.linalg.norm(candidate))
        if candidate_norm == 0.0:
            unscored.append(chunk_id)
            continue
        similarity = float(np.dot(query, candidate) / (query_norm * candidate_norm))
        scored.append((-similarity, position, chunk_id))

    scored.sort()
    ordered = [chunk_id for _, _, chunk_id in scored] + unscored
    return tuple(ordered[:k])
