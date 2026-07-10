from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# /invoke requires a real LLM call (agent reasoning + tool use) and is
# exercised at the Test gate's behavioral checks once a real API key is
# available, not in this deterministic smoke test.
