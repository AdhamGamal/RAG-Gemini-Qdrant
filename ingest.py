import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from utils.chunk import chunk_text
from utils.embedding import embed_texts

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "rag_docs")

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# Example: Ingest a text file, chunk, embed, and store in Qdrant

def ingest_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    chunks = chunk_text(text)
    embeddings = embed_texts(chunks)
    points = [PointStruct(id=i, vector=emb, payload={"text": chunk}) for i, (emb, chunk) in enumerate(zip(embeddings, chunks))]
    client.upsert(collection_name=QDRANT_COLLECTION, points=points)
    print(f"Ingested {len(points)} chunks into Qdrant.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <file.txt>")
    else:
        ingest_document(sys.argv[1])
