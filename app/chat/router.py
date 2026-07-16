from fastapi import APIRouter

from app.chat.schemas import (
    ChatRequest,
    ChatResponse,
)

from app.chat.service import chat

router = APIRouter()


@router.post(
    "",
    response_model=ChatResponse,
)
def ask(
    request: ChatRequest,
):

    answer = chat(
        request.question
    )

    return ChatResponse(
        answer=answer
    )