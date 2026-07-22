import google.generativeai as genai

from app.core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to Gemini.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error communicating with Gemini: {e}"