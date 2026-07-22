from app.ai.llm import model

VALID_AGENTS = {
    "rag",
    "summary",
    "interview",
    "quiz",
    "translator",
}


def classify(question: str) -> str:

    prompt = f"""
You are an AI router.

Available agents:

rag
summary
interview
quiz
translator

Choose the best agent.

Return ONLY one word.

Question:

{question}
"""

    response = model.generate_content(prompt)

    agent = response.text.strip().lower()

    # Remove punctuation
    agent = (
        agent.replace(".", "")
             .replace(",", "")
             .replace(":", "")
             .replace('"', "")
    )

    if agent not in VALID_AGENTS:
        return "rag"

    return agent