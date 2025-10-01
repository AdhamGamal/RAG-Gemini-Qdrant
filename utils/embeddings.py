# utils/embeddings.py
import google.generativeai as genai
from langchain.embeddings.base import Embeddings

class GeminiEmbeddings(Embeddings):
    """
    Custom LangChain-compatible wrapper for Gemini Embeddings.
    """

    def __init__(self, api_key: str, model: str = "text-embedding-004"):
        genai.configure(api_key=api_key)
        self.model = model
        self.client = genai

    def embed_documents(self, texts):
        return [self.embed_query(t) for t in texts]

    def embed_query(self, text: str):
        response = self.client.embed_content(model=self.model, content=text)
        return response["embedding"]

def get_embedding_model(api_key: str, model: str = "text-embedding-004"):
    """
    Return Gemini embeddings wrapped for LangChain.
    """
    return GeminiEmbeddings(api_key=api_key, model=model)
