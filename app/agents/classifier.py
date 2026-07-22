from app.ai.llm import model

def classify_question(question: str) -> str:
    prompt = f"""
You are an AI router.

Choose ONLY ONE of these agents.

- rag
- summary
- interview

Rules:

rag:
- answer questions
- retrieve information
- explain concepts

summary:
- summarize
- overview
- brief
- condense

interview:
- interview questions
- mock interview
- recruiter

Return ONLY the agent name.

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()