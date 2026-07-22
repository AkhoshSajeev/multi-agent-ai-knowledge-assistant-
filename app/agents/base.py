from abc import ABC, abstractmethod

from app.ai.service import answer_question


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, question: str) -> str:
        pass

    def ask_llm(self, prompt: str) -> str:
        """
        Send a prompt to the AI service.
        """
        return answer_question(prompt)