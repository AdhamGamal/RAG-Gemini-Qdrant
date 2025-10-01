# utils/llm.py
import google.generativeai as genai
from langchain.llms.base import LLM
from typing import Any, List, Optional

class GeminiLLM(LLM):
    """Custom wrapper for Google Gemini models to use inside LangChain."""

    api_key: str
    model: str
    temperature: float = 0.2

    def __init__(self, api_key: str, model: str, temperature: float = 0.2, **kwargs):
        super().__init__(api_key=api_key, model=model, temperature=temperature, **kwargs)
        genai.configure(api_key=api_key)

    @property
    def _llm_type(self) -> str:
        return "gemini-custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None, **kwargs: Any) -> str:
        response = genai.GenerativeModel(self.model).generate_content(
            prompt,
            generation_config={"temperature": self.temperature}
        )
        return response.text

def get_llm_model(api_key: str, model: str):
    """
    Return Gemini LLM wrapped for LangChain.
    """
    return GeminiLLM(api_key=api_key, model=model)
