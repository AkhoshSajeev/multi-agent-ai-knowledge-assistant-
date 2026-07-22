from app.agents.base import BaseAgent
from app.ai.service import answer_question


class RAGAgent(BaseAgent):
    """
    Agent responsible for answering
    questions using RAG.
    """

    def __init__(self):
        super().__init__("RAG Agent")

    def run(self, question: str) -> str:
        return self.ask_llm(question)