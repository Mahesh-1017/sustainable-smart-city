from fastapi import FastAPI, UploadFile, File, HTTPException
from app.api import chat_router, feedback_router, eco_tips_router, kpi_upload_router, policy_router

app = FastAPI(title="Sustainable Smart City Assistant API", version="1.0.0")

# Routers
app.include_router(chat_router.router, prefix="/chat", tags=["Chat"])
app.include_router(feedback_router.router, prefix="/feedback", tags=["Feedback"])
app.include_router(eco_tips_router.router, prefix="/eco-tips", tags=["Eco Tips"])
app.include_router(kpi_upload_router.router, prefix="/kpi", tags=["KPI"])
app.include_router(policy_router.router, prefix="/policy", tags=["Policy"])

@app.get("/")
def root():
    return {"message": "Smart City Assistant API is running"}
