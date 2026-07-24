from app.agents.classifier import classify
from app.agents.rag_agent import RAGAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.quiz_agent import QuizAgent
from app.agents.translator_agent import TranslatorAgent
class RouterAgent:

    def __init__(self):
        self.rag_agent = RAGAgent()
        self.summary_agent = SummaryAgent()
        self.interview_agent = InterviewAgent()
        self.quiz_agent = QuizAgent()
        self.translator_agent = TranslatorAgent()
    def run(self, question: str):

        agent = classify(question)

        print("Selected:", agent)

        if agent == "summary":
            return self.summary_agent.run(question)

        elif agent == "interview":
            return self.interview_agent.run(question)

        
        elif agent == "quiz":
           return self.quiz_agent.run(question)
        elif agent == "translator":
          return self.translator_agent.run(question)
        else:
            return self.rag_agent.run(question)