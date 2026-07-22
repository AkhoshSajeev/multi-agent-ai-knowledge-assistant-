from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class GraphState(TypedDict):
    question: str
    answer: str


def router_node(state: GraphState):
    print("Router Node")
    return state


def summary_node(state: GraphState):
    print("Summary Node")
    state["answer"] = "This is a summary."
    return state


def interview_node(state: GraphState):
    print("Interview Node")
    state["answer"] = "These are interview questions."
    return state


def route(state: GraphState):

    question = state["question"].lower()

    if "summary" in question:
        return "summary"

    return "interview"


builder = StateGraph(GraphState)

builder.add_node("router", router_node)
builder.add_node("summary", summary_node)
builder.add_node("interview", interview_node)

builder.add_edge(START, "router")

builder.add_conditional_edges(
    "router",
    route,
    {
        "summary": "summary",
        "interview": "interview",
    },
)

builder.add_edge("summary", END)
builder.add_edge("interview", END)

graph = builder.compile()

result = graph.invoke(
    {
        "question": "Give me a summary",
        "answer": "",
    }
)

print(result)