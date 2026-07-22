from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState

from app.graph.nodes import (
    router_node,
    rag_node,
    summary_node,
    interview_node,
    quiz_node,
    translator_node,
    route,
)

builder = StateGraph(GraphState)

builder.add_node("router", router_node)
builder.add_node("rag", rag_node)
builder.add_node("summary", summary_node)
builder.add_node("interview", interview_node)
builder.add_node("quiz", quiz_node)
builder.add_node("translator", translator_node)

builder.add_edge(START, "router")

builder.add_conditional_edges(
    "router",
    route,
    {
        "rag": "rag",
        "summary": "summary",
        "interview": "interview",
        "quiz": "quiz",
        "translator": "translator",
    },
)

builder.add_edge("rag", END)
builder.add_edge("summary", END)
builder.add_edge("interview", END)
builder.add_edge("quiz", END)
builder.add_edge("translator", END)

graph = builder.compile()


def run_graph(question: str):

    result = graph.invoke(
        {
            "question": question,
            "answer": "",
        }
    )

    return result["answer"]