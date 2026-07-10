from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# /ask requires the sample docs to be ingested (python -m app.ingest) and a
# real OpenAI API key for embeddings — exercised at the Test gate's
# behavioral checks, not in this deterministic smoke test.
