from fastapi import APIRouter
from pydantic import BaseModel

from services.granite_llm import call_granite_llm

class ChatRequest(BaseModel):
    user_input: str

router = APIRouter()

@router.post("/", summary="Chat with Granite LLM")
def chat(request: ChatRequest):
    response = call_granite_llm(request.user_input)
    return {"response": response}
