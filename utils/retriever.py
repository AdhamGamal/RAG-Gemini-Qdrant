# utils/retriever.py
from .vectorstore import get_vectorstore

def get_retriever(
    qdrant_url: str,
    qdrant_api_key: str,
    qdrant_collection: str,
    embedding_model,
    k: int = 3
):
    """
    Create a retriever from Qdrant vectorstore.
    """
    vs = get_vectorstore(qdrant_url, qdrant_api_key, qdrant_collection, embedding_model)
    return vs.as_retriever(search_kwargs={"k": k})

def format_docs(docs):
    return "\n\n".join(
        f"[{doc.metadata.get('source', 'unknown')}] {doc.page_content}"
        for doc in docs
    )