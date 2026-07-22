from app.agents.router import RouterAgent

# Create one RouterAgent instance when the application starts
router = RouterAgent()


def chat(question: str):
    return router.run(question)