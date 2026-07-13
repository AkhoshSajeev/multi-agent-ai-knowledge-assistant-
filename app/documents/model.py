from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    original_filename = Column(String, nullable=False)

    file_type = Column(String, nullable=False)

    file_size = Column(Integer, nullable=False)

    file_path = Column(String, nullable=False)

    status = Column(String, default="uploaded")

    version = Column(Integer, default=1)

    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    user = relationship("User")