from app.tools.base_tool import BaseTool
from app.ai.service import retrieve_context


class DocumentSearchTool(BaseTool):

    def __init__(self):
        super().__init__("Document Search")

    def run(self, question: str) -> str:
        return retrieve_context(question)