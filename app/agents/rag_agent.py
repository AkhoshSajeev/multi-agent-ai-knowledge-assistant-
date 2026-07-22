from app.agents.base import BaseAgent
from app.tools.document_search import DocumentSearchTool
from app.ai.llm import ask_llm
from app.ai.prompts import RAG_PROMPT


class RAGAgent(BaseAgent):

    def __init__(self):
        super().__init__("RAG Agent")
        self.search_tool = DocumentSearchTool()

    def run(self, question: str):

        context = self.search_tool.run(question)

        if not context:
            return (
                "I couldn't find any relevant information "
                "in the uploaded documents."
            )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        return ask_llm(prompt)