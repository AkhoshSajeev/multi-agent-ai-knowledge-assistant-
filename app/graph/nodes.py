from app.agents.rag_agent import RAGAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.quiz_agent import QuizAgent
from app.agents.translator_agent import TranslatorAgent

from app.agents.classifier import classify

rag_agent = RAGAgent()
summary_agent = SummaryAgent()
interview_agent = InterviewAgent()
quiz_agent = QuizAgent()
translator_agent = TranslatorAgent()


def router_node(state):
    return state


def rag_node(state):

    state["answer"] = rag_agent.run(
        state["question"]
    )

    return state


def summary_node(state):

    state["answer"] = summary_agent.run(
        state["question"]
    )

    return state


def interview_node(state):

    state["answer"] = interview_agent.run(
        state["question"]
    )

    return state


def quiz_node(state):

    state["answer"] = quiz_agent.run(
        state["question"]
    )

    return state


def translator_node(state):

    state["answer"] = translator_agent.run(
        state["question"]
    )

    return state


def route(state):

    return classify(
        state["question"]
    )