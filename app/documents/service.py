import os
import uuid

from fastapi import BackgroundTasks, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.ai.processor import process_document
from app.ai.vector_store import collection
from app.documents.model import Document

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_FILE_TYPES = [
    "application/pdf",
]

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


def save_document(
    db: Session,
    file: UploadFile,
    user_id: int,
    background_tasks: BackgroundTasks,
):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    file.file.seek(0, os.SEEK_END)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size == 0:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty.",
        )

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 20 MB.",
        )

    extension = os.path.splitext(file.filename)[1]

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename,
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    document = Document(
        filename=unique_filename,
        original_filename=file.filename,
        file_type=file.content_type,
        file_size=file_size,
        file_path=file_path,
        user_id=user_id,
        status="uploaded",
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    background_tasks.add_task(
        process_document,
        document.id,
    )

    return document


def get_documents(
    db: Session,
    user_id: int,
):
    return (
        db.query(Document)
        .filter(Document.user_id == user_id)
        .order_by(Document.created_at.desc())
        .all()
    )


def get_document(
    db: Session,
    document_id: int,
    user_id: int,
):
    return (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )


def get_document_status(
    db: Session,
    document_id: int,
    user_id: int,
):
    return (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )


def delete_document(
    db: Session,
    document_id: int,
    user_id: int,
):
    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == user_id,
        )
        .first()
    )

    if document is None:
        return False

    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    collection.delete(
        where={
            "document_id": document.id,
        }
    )

    db.delete(document)
    db.commit()

    return True