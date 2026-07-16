from app.ai.embeddings import create_embedding
from app.ai.vector_store import collection


def retrieve(
    question: str,
    top_k: int = 5,
):
    embedding = create_embedding(question)

    result = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )

    print("=" * 60)
    print("Question:", question)

    for i in range(len(result["documents"][0])):
        print(f"\nChunk {i+1}")

        print(
            "Distance:",
            result["distances"][0][i]
        )

        print(
            "Metadata:",
            result["metadatas"][0][i]
        )

        print(
            "Text:",
            result["documents"][0][i][:300]
        )

    print("=" * 60)

    return "\n\n".join(
        result["documents"][0]
    )