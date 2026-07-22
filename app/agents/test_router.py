from app.agents.router import RouterAgent

router = RouterAgent()

print(
    router.run(
        "What skills are mentioned?"
    )
)