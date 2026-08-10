"""TOTP MFA helpers. RFC 6238 defaults via `pyotp` (SHA-1, 6 digits, 30s
step, +/-1 step verification window -- standard authenticator-app
compatibility). Harvested from `little-milestones/dev/backend/app/totp.py`
(F12 Increment 6).

The secret is Fernet-encrypted at rest via `crypto.get_fernet()`'s shared
`APP_ENCRYPTION_KEY`; recovery codes are hashed with the SAME argon2id
`CryptContext` `auth.py` uses for passwords (short, human-typeable secrets
are password-class, unlike the 256-bit session/reset tokens elsewhere in
this accelerator, so a slow KDF is warranted here too).

**Sub-module dependency, not an independent unit (security-architect
co-sign item 8(a)):** this file imports `hash_password`/`verify_password`
from `auth.py` specifically so recovery-code hashing shares the exact same
`pwd_context` tuning as password hashing. If you vendor `auth.py` without
`totp.py` (auth-only, no MFA), fine -- nothing here is required. But if you
vendor `totp.py`, you MUST keep this import of `auth.py`'s primitives
rather than constructing a second `CryptContext` with different tuning --
two independently-tuned argon2id contexts in one project is a real
footgun (inconsistent cost parameters, inconsistent upgrade path when
`deprecated="auto"` migrates an old hash).
"""

from __future__ import annotations

import secrets

import pyotp

from .auth import hash_password, verify_password
from .crypto import get_fernet

TOTP_ISSUER = "your-app-name"  # adopting project: override this constant

# ~16 base32 chars, grouped for readability.
_RECOVERY_CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"  # unambiguous base32-ish set
_RECOVERY_CODE_LENGTH = 16
_RECOVERY_CODE_GROUP_SIZE = 4


def generate_totp_secret() -> str:
    return pyotp.random_base32()


def encrypt_secret(raw_secret: str) -> str:
    return get_fernet().encrypt(raw_secret.encode("utf-8")).decode("utf-8")


def decrypt_secret(enc_secret: str) -> str:
    return get_fernet().decrypt(enc_secret.encode("utf-8")).decode("utf-8")


def provisioning_uri(raw_secret: str, account_email: str) -> str:
    """`otpauth://` URI -- the server never generates a QR image itself; the
    frontend renders the QR client-side from this string."""
    return pyotp.TOTP(raw_secret).provisioning_uri(
        name=account_email, issuer_name=TOTP_ISSUER
    )


def verify_totp_code(raw_secret: str, code: str) -> bool:
    """+/-1 step window (~30s either side), RFC 6238 defaults."""
    code = (code or "").strip()
    if not code:
        return False
    return pyotp.TOTP(raw_secret).verify(code, valid_window=1)


def generate_recovery_codes(count: int) -> list[str]:
    """`secrets`-sourced, grouped for readability (e.g. "ABCD-EFGH-JKLM-
    NPQR"). Returned in plaintext exactly once by the enrollment route --
    only the argon2id hash is ever persisted."""
    codes = []
    for _ in range(count):
        raw = "".join(secrets.choice(_RECOVERY_CODE_ALPHABET) for _ in range(_RECOVERY_CODE_LENGTH))
        grouped = "-".join(
            raw[i : i + _RECOVERY_CODE_GROUP_SIZE]
            for i in range(0, len(raw), _RECOVERY_CODE_GROUP_SIZE)
        )
        codes.append(grouped)
    return codes


def hash_recovery_code(code: str) -> str:
    # Reuses the exact same argon2id context as password hashing
    # (auth.py) -- see the module docstring's sub-module dependency note.
    return hash_password(code.strip().upper())


def verify_recovery_code(code: str, code_hash: str) -> bool:
    try:
        return verify_password(code.strip().upper(), code_hash)
    except Exception:
        return False
