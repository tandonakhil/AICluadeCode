"""A minimal stand-in for "the resource" that `live_ledger_guard` watches.

Not part of the vendorable payload — this exists only so the negative control
has a real `__init__(self, path)` to patch, in place of the source project's
`BrokerStore`.
"""

from __future__ import annotations


class Resource:
    def __init__(self, path):
        self.path = path
