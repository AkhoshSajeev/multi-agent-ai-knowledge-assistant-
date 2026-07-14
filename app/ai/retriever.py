from .embeddings import create_embedding
from .vector_store import collection


def retrieve(query: str, top_k: int = 5):

    embedding = create_embedding(query)

    result = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )

    return result["documents"][0]