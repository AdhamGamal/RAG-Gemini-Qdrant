# utils/loader.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def load_and_split_pdfs(file_paths: List[str], chunk_size: int = 1000, chunk_overlap: int = 200):
    """
    Load multiple PDFs and split into text chunks for embeddings.
    
    Args:
        file_paths (List[str]): Paths to PDF files.
        chunk_size (int): Max characters per chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        List[Document]: LangChain Document objects ready for embedding.
    """
    all_docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        chunks = splitter.split_documents(docs)
        all_docs.extend(chunks)

    print(f"📚 Loaded and split {len(file_paths)} PDF(s) into {len(all_docs)} chunks")
    return all_docs
