from app.ai.llm import ask_llm
from app.ai.retriever import retrieve


def retrieve_context(question: str) -> str:
    """
    Retrieve relevant context from the vector database.
    """
    return retrieve(question)


def answer_question(question: str) -> str:
    context = retrieve_context(question)

    if not context:
        return "I couldn't find any relevant information in the uploaded documents."

    return ask_llm(
        question=question,
        context=context,
    )