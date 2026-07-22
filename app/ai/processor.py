from app.db.database import SessionLocal
from app.documents.model import Document

from app.ai.loader import load_pdf
from app.ai.splitter import split_documents
from app.ai.vector_store import store_document


def process_document(document_id: int):
    db = SessionLocal()
    document = None

    try:
        # Get document from database
        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document is None:
            return

        # Update status
        document.status = "processing"
        db.commit()

        # Load PDF using LangChain
        documents = load_pdf(document.file_path)

        if not documents:
            raise Exception("No text could be extracted from the PDF.")

        # Split into chunks
        chunks = split_documents(documents)

        if not chunks:
            raise Exception("No chunks were created from the document.")

        # Store chunks in ChromaDB
        store_document(
            document_id=document.id,
            chunks=chunks,
        )

        # Mark as completed
        document.status = "completed"
        db.commit()
        db.refresh(document)

    except Exception as e:
        print(f"[PROCESS DOCUMENT ERROR] {e}")

        if document is not None:
            document.status = "failed"
            db.commit()

    finally:
        db.close()