from services.pinecone_client import index

def query_vectorstore(query_embedding, top_k: int = 5):
    """Returns the top_k similar documents (IDs and scores)."""
    query_results = index.query(queries=[query_embedding], top_k=top_k)
    return query_results['matches'][0] if query_results['matches'] else []
