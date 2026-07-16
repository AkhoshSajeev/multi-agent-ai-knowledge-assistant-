from app.ai.llm import ask_llm
from app.ai.retriever import retrieve


def answer_question(question: str) -> str:
    context = retrieve(question)

    if not context:
        return "I couldn't find any relevant information in the uploaded documents."

    return ask_llm(
        question=question,
        context=context,
    )