from app.tools.base_tool import BaseTool


class DatabaseTool(BaseTool):
    """
    Tool for querying the application database.
    """

    def __init__(self):
        super().__init__("Database Tool")

    def run(self):
        raise NotImplementedError("Database queries not implemented yet.")