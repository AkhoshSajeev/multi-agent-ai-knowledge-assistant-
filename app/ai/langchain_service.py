from app.ai.prompts import prompt
from app.ai.langchain_llm import llm
from app.ai.retriever import retrieve


def answer_question(question: str):
    context = retrieve(question)

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return response.content