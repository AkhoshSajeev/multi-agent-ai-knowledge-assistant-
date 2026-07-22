from app.agents.base import BaseAgent
from app.ai.service import answer_question


class SummaryAgent(BaseAgent):
    """
    Agent responsible for summarizing documents.
    """

    def __init__(self):
        super().__init__("Summary Agent")

    def run(self, question: str) -> str:

        prompt = f"""
You are an expert summarizer.

Summarize the uploaded document clearly using:

- Main topic
- Important points
- Key technologies or concepts
- Final conclusion

User request:
{question}
"""

        return self.ask_llm(prompt)