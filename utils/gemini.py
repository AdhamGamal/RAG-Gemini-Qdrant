import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Placeholder: Replace with actual Gemini LLM API call

def ask_gemini(question, context):
    # TODO: Replace with Gemini LLM API call
    # For now, return a dummy answer
    return f"[Gemini would answer the question: '{question}' using the context provided.]"
