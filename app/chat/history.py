from sqlalchemy.orm import Session

from app.chat.model import ChatMessage


def save_message(
    db: Session,
    user_id: int,
    role: str,
    message: str,
):
    chat = ChatMessage(
        user_id=user_id,
        role=role,
        message=message,
    )

    db.add(chat)
    db.commit()


def get_recent_messages(
    db: Session,
    user_id: int,
    limit: int = 10,
):
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == user_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(limit)
        .all()
    )