from pydantic import BaseSettings

class Settings(BaseSettings):
    watsonx_api_key: str
    project_id: str
    model_id: str
    pinecone_api_key: str
    pinecone_env: str
    pinecone_index: str

    class Config:
        env_file = ".env"

settings = Settings()
