"""Self-scoped session management -- list/revoke-one/revoke-others/
revoke-all-for-user. Harvested from `little-milestones/dev/backend/app/
sessions.py` (F12 Increment 6). Tenant-agnostic as-is: this module never
reads or joins on a tenant column, only `sessions.user_id`, so no
genericization was needed here (contrast `auth.py`'s `PrincipalResolver`
seam, which exists because *that* module resolves the tenant-scoped
principal).

`SessionStore` follows a narrow, single-purpose-methods, no-ad-hoc-SQL-in-
routes shape -- keep that shape in your own routes file.
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from pydantic import BaseModel


class SessionInfo(BaseModel):
    """Never carries the token or its hash -- only what a caller needs to
    recognize and manage their own sessions."""

    id: str
    created_at: str
    last_seen_at: str
    is_current: bool = False
    # 'web' | 'mobile' -- lets a caller tell a lost phone from a laptop.
    client: str = "web"


def _row_to_info(row: sqlite3.Row, current_session_id: Optional[str]) -> SessionInfo:
    return SessionInfo(
        id=row["id"],
        client=(row["client"] if "client" in row.keys() else "web"),
        created_at=row["created_at"],
        last_seen_at=row["last_seen_at"],
        is_current=(row["id"] == current_session_id),
    )


class SessionStore:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def list_for_user(
        self, user_id: int, current_session_id: Optional[str] = None
    ) -> list[SessionInfo]:
        rows = self._conn.execute(
            "SELECT id, created_at, last_seen_at, client FROM sessions "
            "WHERE user_id = ? AND id IS NOT NULL AND mfa_pending = 0 "
            "ORDER BY last_seen_at DESC",
            (user_id,),
        ).fetchall()
        return [_row_to_info(r, current_session_id) for r in rows]

    def delete(self, session_id: str, user_id: int) -> bool:
        """Self-scoped: a user manages only their own sessions, never
        another user's. This WHERE clause is what makes cross-user 404
        correct at the route layer: a cross-user id simply matches zero
        rows."""
        cur = self._conn.execute(
            "DELETE FROM sessions WHERE id = ? AND user_id = ?",
            (session_id, user_id),
        )
        self._conn.commit()
        return cur.rowcount > 0

    def delete_all_for_user(self, user_id: int, except_id: Optional[str] = None) -> None:
        """One method, parameterized: a password reset deletes every
        session (`except_id=None`, a possible-compromise event); an
        authenticated password change deletes every OTHER session
        (`except_id=<current session id>`, since a logged-in,
        password-knowing change is not itself a compromise signal)."""
        if except_id is None:
            self._conn.execute("DELETE FROM sessions WHERE user_id = ?", (user_id,))
        else:
            self._conn.execute(
                "DELETE FROM sessions WHERE user_id = ? AND id != ?",
                (user_id, except_id),
            )
        self._conn.commit()
