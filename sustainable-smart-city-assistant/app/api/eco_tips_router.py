from fastapi import APIRouter
from pydantic import BaseModel

from services.granite_llm import call_granite_llm

class EcoTipRequest(BaseModel):
    topic: str

router = APIRouter()

@router.post("/", summary="Get eco-friendly tips")
def get_eco_tips(req: EcoTipRequest):
    prompt = f"Provide five actionable eco-friendly tips related to {req.topic}."
    tips = call_granite_llm(prompt)
    return {"tips": tips}
