import pinecone
from core.config import settings

pinecone.init(api_key=settings.pinecone_api_key, environment=settings.pinecone_env)
index = pinecone.Index(settings.pinecone_index)
