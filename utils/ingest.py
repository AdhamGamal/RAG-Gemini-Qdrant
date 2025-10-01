# utils/ingest.py
from .vectorstore import get_vectorstore

def ingest_documents(
    qdrant_url: str,
    qdrant_api_key: str,
    qdrant_collection: str,
    embedding_model,
    documents,
    force_update: bool = False
):
    """
    Embed and store documents into Qdrant vectorstore.
    Skips ingestion if data already exists unless force_update=True.

    Args:
        qdrant_url (str): Qdrant endpoint.
        qdrant_api_key (str): Qdrant API key (optional if local).
        qdrant_collection (str): Collection name.
        embedding_model: Embedding model instance.
        documents: LangChain Document objects.
        force_update (bool): If True, re-embed and overwrite docs even if they exist.

    Returns:
        vectorstore: QdrantVectorStore instance.
    """
    vs = get_vectorstore(qdrant_url, qdrant_api_key, qdrant_collection, embedding_model)
    client = vs.client

    # Check if collection already has points
    collection_info = client.get_collection(qdrant_collection)
    points_count = collection_info.points_count if collection_info else 0

    if points_count > 0 and not force_update:
        print(f"✅ Collection '{qdrant_collection}' already has {points_count} vectors. Skipping ingestion.")
        return vs

    if force_update and points_count > 0:
        print(f"⚠️ Force update enabled. Deleting existing points from '{qdrant_collection}'...")
        client.delete_collection(qdrant_collection)
        # Recreate collection to ensure clean state
        get_vectorstore(qdrant_url, qdrant_api_key, qdrant_collection, embedding_model)

    vs.add_documents(documents)
    print(f"✅ Ingested {len(documents)} documents into collection '{qdrant_collection}'")
    return vs
