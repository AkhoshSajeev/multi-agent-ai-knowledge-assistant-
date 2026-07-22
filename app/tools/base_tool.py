from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for all tools.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, *args, **kwargs):
        pass