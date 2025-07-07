from fastapi import APIRouter
from pydantic import BaseModel
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/feedback.json")
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")  # initialize

class Feedback(BaseModel):
    name: str
    category: str
    message: str

router = APIRouter()

@router.post("/", summary="Submit citizen feedback")
def submit_feedback(feedback: Feedback):
    existing = json.loads(DATA_FILE.read_text())
    feedback_dict = feedback.dict()
    feedback_dict["timestamp"] = datetime.utcnow().isoformat()
    existing.append(feedback_dict)
    DATA_FILE.write_text(json.dumps(existing, indent=2))
    return {"status": "success", "count": len(existing)}
