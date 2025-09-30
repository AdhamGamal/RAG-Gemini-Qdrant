import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from utils.embedding import embed_texts
from utils.gemini import ask_gemini

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "rag_docs")

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# Example: Query pipeline

def query_rag(question, top_k=5):
    q_emb = embed_texts([question])[0]
    hits = client.search(collection_name=QDRANT_COLLECTION, query_vector=q_emb, limit=top_k)
    context = "\n".join([hit.payload["text"] for hit in hits])
    answer = ask_gemini(question, context)
    print("Context:\n", context)
    print("Answer:\n", answer)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python query.py <question>")
    else:
        query_rag(sys.argv[1])
