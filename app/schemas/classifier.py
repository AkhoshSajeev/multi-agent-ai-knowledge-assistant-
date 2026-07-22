import json

from app.ai.llm import model
from app.schemas.classifier import RouteResponse

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

- rag
- summary
- interview
- quiz
- translator

Return ONLY valid JSON.

Example:

{{
    "agent": "summary"
}}

Question:
{question}
"""

    response = model.generate_content(prompt)

    try:
        data = json.loads(response.text)

        route = RouteResponse(**data)

        if route.agent not in VALID_AGENTS:
            return "rag"

        return route.agent

    except Exception:
        return "rag"