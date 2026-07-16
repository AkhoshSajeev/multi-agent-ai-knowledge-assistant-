import google.generativeai as genai

from app.core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_llm(
    question: str,
    context: str,
) -> str:

    prompt = f"""
You are an AI Knowledge Assistant.

Rules:
1. Answer only from the provided context.
2. Do not invent information.
3. If the answer is missing, reply:
   "I couldn't find that information in the uploaded documents."
4. Keep answers clear and concise.

Context:
{context}

Question:
{question}
"""

    try:
      response = model.generate_content(prompt)
      return response.text
    except Exception as e:
      return f"Error communicating with Gemini: {str(e)}"