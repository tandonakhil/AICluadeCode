"""Password-reset tokens + TOTP recovery codes. Two dedicated store classes
following the narrow, single-purpose-methods, no-ad-hoc-SQL-in-routes shape.
Harvested from `little-milestones/dev/backend/app/security_tokens.py` (F12
Increment 6). Tenant-agnostic as-is -- no genericization needed.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta, timezone
from typing import Optional

from pydantic import BaseModel

# 30-minute expiry, single-use, one active token per user.
PASSWORD_RESET_TOKEN_EXPIRY_MINUTES = 30

# 8 recovery codes generated at TOTP enrollment.
RECOVERY_CODE_COUNT = 8


def _parse_db_datetime(value: str) -> datetime:
    dt = datetime.fromisoformat(value)
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


class PasswordResetToken(BaseModel):
    id: int
    user_id: int
    created_at: str
    expires_at: str
    used_at: Optional[str] = None


def _row_to_reset_token(row: sqlite3.Row) -> PasswordResetToken:
    return PasswordResetToken(
        id=row["id"],
        user_id=row["user_id"],
        created_at=row["created_at"],
        expires_at=row["expires_at"],
        used_at=row["used_at"],
    )


class PasswordResetTokenStore:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def create(self, user_id: int, token_hash: str) -> PasswordResetToken:
        """"One active token per user (a new request invalidates any
        outstanding token for that user first)" -- done by marking every
        not-yet-used token for this user as used before inserting the new
        one, in the same call, so there is never a window with two live
        tokens for one user."""
        now = datetime.now(timezone.utc)
        self._conn.execute(
            "UPDATE password_reset_tokens SET used_at = ? "
            "WHERE user_id = ? AND used_at IS NULL",
            (now.isoformat(), user_id),
        )
        expires_at = now + timedelta(minutes=PASSWORD_RESET_TOKEN_EXPIRY_MINUTES)
        cur = self._conn.execute(
            "INSERT INTO password_reset_tokens (user_id, token_hash, created_at, expires_at) "
            "VALUES (?, ?, ?, ?)",
            (user_id, token_hash, now.isoformat(), expires_at.isoformat()),
        )
        self._conn.commit()
        row = self._conn.execute(
            "SELECT * FROM password_reset_tokens WHERE id = ?", (cur.lastrowid,)
        ).fetchone()
        return _row_to_reset_token(row)

    def get_valid_by_token_hash(self, token_hash: str) -> Optional[PasswordResetToken]:
        """Returns the token only if it is unexpired and unused -- callers
        must still call `mark_used` themselves once the reset is actually
        applied (kept as two steps so a validation-only check, if ever
        needed, doesn't have the side effect of consuming the token)."""
        row = self._conn.execute(
            "SELECT * FROM password_reset_tokens WHERE token_hash = ?", (token_hash,)
        ).fetchone()
        if row is None:
            return None
        token = _row_to_reset_token(row)
        if token.used_at is not None:
            return None
        if _parse_db_datetime(token.expires_at) < datetime.now(timezone.utc):
            return None
        return token

    def mark_used(self, token_id: int) -> None:
        self._conn.execute(
            "UPDATE password_reset_tokens SET used_at = ? WHERE id = ?",
            (datetime.now(timezone.utc).isoformat(), token_id),
        )
        self._conn.commit()


class RecoveryCode(BaseModel):
    id: int
    user_id: int
    used_at: Optional[str] = None


class RecoveryCodeStore:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def create_batch(self, user_id: int, code_hashes: list[str]) -> None:
        """Replaces any existing codes for this user -- re-running TOTP
        setup/enrollment mints a fresh batch."""
        self._conn.execute("DELETE FROM recovery_codes WHERE user_id = ?", (user_id,))
        self._conn.executemany(
            "INSERT INTO recovery_codes (user_id, code_hash) VALUES (?, ?)",
            [(user_id, h) for h in code_hashes],
        )
        self._conn.commit()

    def unused_count(self, user_id: int) -> int:
        row = self._conn.execute(
            "SELECT COUNT(*) AS n FROM recovery_codes WHERE user_id = ? AND used_at IS NULL",
            (user_id,),
        ).fetchone()
        return row["n"]

    def unused_for_user(self, user_id: int) -> list[sqlite3.Row]:
        return self._conn.execute(
            "SELECT * FROM recovery_codes WHERE user_id = ? AND used_at IS NULL",
            (user_id,),
        ).fetchall()

    def mark_used(self, code_id: int) -> None:
        self._conn.execute(
            "UPDATE recovery_codes SET used_at = ? WHERE id = ?",
            (datetime.now(timezone.utc).isoformat(), code_id),
        )
        self._conn.commit()

    def delete_all_for_user(self, user_id: int) -> None:
        self._conn.execute("DELETE FROM recovery_codes WHERE user_id = ?", (user_id,))
        self._conn.commit()
