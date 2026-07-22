from app.agents.rag_agent import RAGAgent

agent = RAGAgent()

answer = agent.run(
    "Summarize my resume."
)

print(answer)