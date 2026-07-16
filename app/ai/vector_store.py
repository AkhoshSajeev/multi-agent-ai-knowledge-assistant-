import chromadb

from .embeddings import create_embeddings

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def store_document(
    document_id: int,
    chunks,
):
    # Extract text from LangChain Document objects
    texts = [
        doc.page_content
        for doc in chunks
    ]

    embeddings = create_embeddings(texts)

    ids = [
        f"{document_id}_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {
                **doc.metadata,
                "document_id": document_id,
                "chunk": i,
            }
            for i, doc in enumerate(chunks)
        ],
    )