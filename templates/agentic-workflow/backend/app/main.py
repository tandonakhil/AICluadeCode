from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import run_agent

load_dotenv()

app = FastAPI(title="{{PROJECT_NAME}}")


class InvokeRequest(BaseModel):
    input: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/invoke")
def invoke(request: InvokeRequest):
    return run_agent(request.input)
