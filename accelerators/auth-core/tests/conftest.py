from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

# Ensure `accelerators/auth-core` (this file's parent) is on sys.path so
# `import src...` resolves regardless of pytest's import-mode configuration.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient

from src.auth import reset_rate_limits

from ._reference_app import build_app, init_schema

DEFAULT_EMAIL = "owner@example.com"
DEFAULT_PASSWORD = "correct horse battery staple"

MOBILE_HEADERS = {"X-LM-Client": "mobile"}
TOKEN_HEADER = "X-LM-Session-Token"


def bearer(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


@pytest.fixture
def mobile_root() -> Path:
    return Path(__file__).resolve().parent.parent / "mobile"


@pytest.fixture(autouse=True)
def _app_encryption_key(monkeypatch):
    from cryptography.fernet import Fernet

    monkeypatch.setenv("APP_ENCRYPTION_KEY", Fernet.generate_key().decode())


@pytest.fixture
def test_db() -> sqlite3.Connection:
    # check_same_thread=False: FastAPI's TestClient runs sync route handlers
    # in an anyio worker thread, not the thread that created this fixture --
    # sqlite3's default same-thread check raises ProgrammingError on the
    # very first request otherwise. Safe here because a single in-memory
    # connection is used by one TestClient in one test at a time, never
    # concurrently.
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    init_schema(conn)
    return conn


@pytest.fixture
def unauthenticated_client(test_db: sqlite3.Connection) -> TestClient:
    app = build_app(test_db)
    reset_rate_limits()
    with TestClient(app) as c:
        yield c
    reset_rate_limits()


@pytest.fixture
def client(unauthenticated_client: TestClient) -> TestClient:
    resp = unauthenticated_client.post(
        "/auth/signup", json={"email": DEFAULT_EMAIL, "password": DEFAULT_PASSWORD}
    )
    assert resp.status_code == 201, resp.text
    return unauthenticated_client


def signup_mobile(client: TestClient, email: str, password: str = DEFAULT_PASSWORD) -> str:
    """Sign up as a native client and return the header-issued token."""
    res = client.post(
        "/auth/signup", json={"email": email, "password": password}, headers=MOBILE_HEADERS
    )
    assert res.status_code == 201, res.text
    token = res.headers.get(TOKEN_HEADER)
    assert token, "native signup must return the session token in a header"
    return token
