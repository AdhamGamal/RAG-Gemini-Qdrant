from google import genai
from google.genai.errors import APIError

def embed_texts(texts, GEMINI_API_KEY):
    try:
        response = genai.Embeddings.create(
            model="text-embedding-ada-002",
            input=texts,
            api_key=GEMINI_API_KEY
        )
        return [r.embedding for r in response.data]
    except APIError as e:
        print(f"Error calling Gemini API: {e}")
        return []