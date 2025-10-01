# extras/list_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

def list_gemini_models():
    """
    List all available Gemini models for the configured API key.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found in .env")

    genai.configure(api_key=api_key)

    print("📌 Available Gemini Models:")
    for m in genai.list_models():
        # Show only generative models
        if "generateContent" in m.supported_generation_methods:
            print(f" - {m.name}")

list_gemini_models()