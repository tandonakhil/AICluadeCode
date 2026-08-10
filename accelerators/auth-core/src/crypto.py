"""Shared Fernet key setup. Harvested from `little-milestones/dev/backend/
app/crypto.py`, where the key was named `PHOTO_ENCRYPTION_KEY` and shared
between photo-at-rest encryption and TOTP-secret encryption.

RENAMED to `APP_ENCRYPTION_KEY` (security-architect co-sign item 4).
This key is designed for reuse across an adopting project's own
symmetric-encryption-at-rest needs generally -- it is not restricted to
auth/TOTP use.

**Key-reuse-across-purposes is a decision every adopting project's
`security-architect` must re-make, never silently inherit.** The risk being
named explicitly: a future project reusing this key for an unrelated
sensitive field (e.g. photo bytes, a third-party OAuth token) without
evaluating *that* data's own exposure, rotation, and regulatory profile.
Sharing one symmetric key across purposes was right-sized for
little-milestones' actual shape (single local `.env`, no operational
surface for a second key) -- it is not free of cost, and an adopting
project reaching for a second, differently-rotated key for a different
purpose has made a legitimate, distinct decision, not a mistake.
"""

from __future__ import annotations

import os

from cryptography.fernet import Fernet


def get_fernet() -> Fernet:
    key = os.environ.get("APP_ENCRYPTION_KEY")
    if not key:
        raise RuntimeError(
            "APP_ENCRYPTION_KEY is not set -- see ACCELERATOR.md's config table (H2) "
            "and your project's own SECURITY_KB.md for the key-reuse decision."
        )
    return Fernet(key.encode() if isinstance(key, str) else key)
