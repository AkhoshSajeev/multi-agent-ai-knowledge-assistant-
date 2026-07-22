from app.agents.base import BaseAgent
from app.tools.document_search import DocumentSearchTool
from app.ai.llm import ask_llm
from app.ai.prompts import SUMMARY_PROMPT


class SummaryAgent(BaseAgent):
    """
    Agent responsible for summarizing documents.
    """

    def __init__(self):
        super().__init__("Summary Agent")
        self.search_tool = DocumentSearchTool()

    def run(self, question: str) -> str:

        context = self.search_tool.run(question)

        if not context:
            return "No document was found to summarize."

        prompt = SUMMARY_PROMPT.format(
            context=context,
            question=question,
        )

        return ask_llm(prompt)