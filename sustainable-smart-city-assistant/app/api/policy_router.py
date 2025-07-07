from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import tempfile
from uuid import uuid4

from vectorstore.document_embedder import embed_and_store
from services.granite_llm import call_granite_llm

class PolicyQuery(BaseModel):
    question: str

router = APIRouter()

@router.post("/upload", summary="Upload a policy document for embedding & summarization")
async def upload_policy(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt', '.csv', '.md')):
        raise HTTPException(status_code=400, detail="Allowed formats: .txt, .csv, .md")
    content = (await file.read()).decode("utf-8", errors="ignore")
    doc_id = str(uuid4())
    embed_and_store(doc_id, content)
    summary = call_granite_llm(f"Summarize the following policy in 150 words:\n\n{content[:4000]}")
    return {"doc_id": doc_id, "summary": summary}

@router.post("/search", summary="Ask a question about embedded policies")
def search_policy(query: PolicyQuery):
    answer = call_granite_llm(query.question)
    return {"answer": answer}
