from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.llm import get_chat_model

load_dotenv()

app = FastAPI(title="{{PROJECT_NAME}}")


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    model = get_chat_model()

    def stream():
        for chunk in model.stream(request.message):
            yield chunk.content

    return StreamingResponse(stream(), media_type="text/plain")
