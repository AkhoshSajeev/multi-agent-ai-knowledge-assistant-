from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.documents.schemas import DocumentResponse
from app.documents.service import save_document
from app.models.user import User

router = APIRouter()


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    document = save_document(
        db=db,
        file=file,
        user_id=current_user.id,
        background_tasks=background_tasks,
    )

    return document