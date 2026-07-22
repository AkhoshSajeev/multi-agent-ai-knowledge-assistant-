from app.agents.classifier import classify_question
from app.agents.rag_agent import RAGAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.interview_agent import InterviewAgent


class RouterAgent:

    def __init__(self):
        self.rag_agent = RAGAgent()
        self.summary_agent = SummaryAgent()
        self.interview_agent = InterviewAgent()

    def run(self, question: str):

        agent = classify_question(question)

        print("Selected:", agent)

        if agent == "summary":
            return self.summary_agent.run(question)

        elif agent == "interview":
            return self.interview_agent.run(question)

        else:
            return self.rag_agent.run(question)