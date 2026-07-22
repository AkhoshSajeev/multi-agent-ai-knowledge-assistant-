from app.agents.base import BaseAgent


class TestAgent(BaseAgent):

    def __init__(self):
        super().__init__("Test")

    def run(self, question: str):
        return f"You asked: {question}"


agent = TestAgent()

print(agent.run("Hello"))