from sentence_transformers import SentenceTransformer
from services.pinecone_client import index

_model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")  # Change device if GPU

def embed_and_store(doc_id: str, text: str):
    """Embeds text and stores it in Pinecone under the given doc_id."""
    embedding = _model.encode([text])[0].tolist()
    index.upsert([(doc_id, embedding)])
