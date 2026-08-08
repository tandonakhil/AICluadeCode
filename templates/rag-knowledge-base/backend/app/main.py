import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

from app.rag import ask

load_dotenv()

app = FastAPI(title="{{PROJECT_NAME}}")

# Scoped to the local frontend dev origin, not a wildcard — even a local,
# internal-tool-first MVP with no auth should not default to an open CORS
# policy. FRONTEND_ORIGIN lets the port be reconfigured without a code
# change. Hardening delta harvested from policy-lookup-assistant (2026-08-08).
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("FRONTEND_ORIGIN", "http://127.0.0.1:3421")],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)

    @field_validator("question")
    @classmethod
    def question_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("question must not be empty or whitespace-only")
        return value


class SourceInfo(BaseModel):
    document: str
    label: str
    authority: str
    as_of: str


class AskResponse(BaseModel):
    answer: str
    sufficient_evidence: bool
    sources: list[SourceInfo]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest):
    return ask(request.question)
