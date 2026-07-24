from app.agents.base import BaseAgent
from app.tools.document_search import DocumentSearchTool
from app.ai.prompts import INTERVIEW_PROMPT
from app.ai.llm import ask_llm


class InterviewAgent(BaseAgent):

    def __init__(self):
        super().__init__("Interview Agent")
        self.search_tool = DocumentSearchTool()

    def run(
        self,
        question: str,
        count: int = 10,
    ) -> str:

        context = self.search_tool.run(question)

        if not context:
            return (
                "I couldn't find any relevant information "
                "in the uploaded documents."
            )

        prompt = INTERVIEW_PROMPT.format(
            context=context,
            question=question,
            count=count,
        )

        return ask_llm(prompt)