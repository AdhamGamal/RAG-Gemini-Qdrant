# utils/vectorstore.py
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

def get_qdrant_client(qdrant_url: str, qdrant_api_key: str = None) -> QdrantClient:
    """
    Initialize a Qdrant client, with or without API key.
    """
    if qdrant_api_key:
        return QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    return QdrantClient(url=qdrant_url)

def get_vectorstore(qdrant_url: str, qdrant_api_key: str, qdrant_collection: str, embedding_model) -> QdrantVectorStore:
    """
    Connect to Qdrant and ensure the collection exists.
    Returns a QdrantVectorStore object.
    """
    client = get_qdrant_client(qdrant_url, qdrant_api_key)

    collections = [c.name for c in client.get_collections().collections]
    if qdrant_collection not in collections:
        vector_size = len(embedding_model.embed_query("test sentence"))
        client.create_collection(
            collection_name=qdrant_collection,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )
        print(f"✅ Created Qdrant collection '{qdrant_collection}' with vector size {vector_size}")
    else:
        print(f"ℹ️ Using existing Qdrant collection '{qdrant_collection}'")

    return QdrantVectorStore(
        client=client,
        collection_name=qdrant_collection,
        embedding=embedding_model,
    )
