import os
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.documents.model import Document


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_document(
    db: Session,
    file: UploadFile,
    user_id: int,
):
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
        file_size=os.path.getsize(file_path),
        file_path=file_path,
        user_id=user_id,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document