from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import ask

load_dotenv()

app = FastAPI(title="{{PROJECT_NAME}}")


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask_endpoint(request: AskRequest):
    return ask(request.question)
