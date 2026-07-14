from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embedding(text: str):
    return model.encode(text).tolist()


def create_embeddings(chunks: list[str]):
    return model.encode(chunks).tolist()