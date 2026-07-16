from app.db.database import SessionLocal
from app.documents.model import Document

from app.ai.loader import load_pdf
from app.ai.splitter import split_documents
from app.ai.vector_store import store_document


def process_document(document_id: int):
    db = SessionLocal()

    try:
        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document is None:
            return

        document.status = "processing"
        db.commit()

        # Load PDF using LangChain
        documents = load_pdf(document.file_path)

        # Split into chunks
        chunks = split_documents(documents)

        # Store embeddings
        store_document(
            document_id=document.id,
            chunks=chunks,
        )

        document.status = "completed"
        db.commit()

    except Exception as e:
        print(f"Processing Error: {e}")

        if document is not None:
            document.status = "failed"
            db.commit()

    finally:
        db.close()