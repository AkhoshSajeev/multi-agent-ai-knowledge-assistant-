from app.agents.base import BaseAgent
from app.ai.service import answer_question


class InterviewAgent(BaseAgent):
    """
    Generates interview questions
    from uploaded documents.
    """

    def __init__(self):
        super().__init__("Interview Agent")

    def run(self, question: str) -> str:

        prompt = f"""
You are an experienced technical interviewer.

Using the uploaded document, generate interview questions.

Requirements:
- Beginner questions
- Intermediate questions
- Advanced questions
- Include expected topics the interviewer might explore

User request:
{question}
"""

        return self.ask_llm(prompt)