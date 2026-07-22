from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.core.config import settings

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=settings.GEMINI_API_KEY,
)

vector_db = Chroma(
    collection_name="documents",
    embedding_function=embedding,
    persist_directory="chroma_db",
)