import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)

from .embeddings import create_embeddings


def store_document(
    document_id: int,
    chunks: list[str],
):
    embeddings = create_embeddings(chunks)

    ids = [
        f"{document_id}_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {
                "document_id": document_id,
                "chunk": i,
            }
            for i in range(len(chunks))
        ],
    )