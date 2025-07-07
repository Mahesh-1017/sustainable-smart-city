import requests
from core.config import settings

def call_granite_llm(prompt: str) -> str:
    """Makes a simple text generation request to IBM Watsonx Granite LLM"""
    headers = {"Authorization": f"Bearer {settings.watsonx_api_key}"}
    payload = {
        "model_id": settings.model_id,
        "project_id": settings.project_id,
        "input": prompt,
    }
    try:
        response = requests.post(
            "https://us-south.ml.cloud.ibm.com/v1/genai/generate",
            json=payload,
            headers=headers,
            timeout=60,
        )
        response.raise_for_status()
        return response.json().get("result", "No response from Granite LLM")
    except Exception as e:
        return f"Granite LLM error: {e}"
