from app.agents.base import BaseAgent
from app.tools.document_search import DocumentSearchTool
from app.ai.prompts import TRANSLATOR_PROMPT
from app.ai.llm import ask_llm


class TranslatorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Translator Agent")
        self.search_tool = DocumentSearchTool()

    def run(self, question: str) -> str:

        context = self.search_tool.run(question)

        if not context:
            return (
                "I couldn't find any relevant information "
                "in the uploaded documents."
            )

        prompt = TRANSLATOR_PROMPT.format(
            context=context,
            question=question,
            language="Malayalam",   # Temporary default
        )

        return ask_llm(prompt)