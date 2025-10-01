from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate

def get_rag_prompt():
    """
    Returns a prompt template for RAG that guides the model to use context.
    """
    template = """
You are an AI assistant. Use the following context from documents to answer the question.
If you don't know, just say you don't know. Be concise but informative.

Context:
{context}

Question:
{question}

Answer:
"""
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

def get_chat_rag_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Use the provided context to answer the user’s question. "
                   "If you don't know, just say you don't know. Be concise."),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:")
    ])