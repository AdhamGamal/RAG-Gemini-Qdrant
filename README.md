# RAG with Gemini and Qdrant

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Google's Gemini LLM and Qdrant vector database.

## Features
- Document ingestion and chunking
- Embedding generation (Gemini or compatible model)
- Vector storage and retrieval with Qdrant
- Query workflow: retrieve relevant chunks and generate answers with Gemini

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set up your environment variables for Gemini API and Qdrant connection (see `.env.example`).
3. Run the example scripts in order:
   - `ingest.py` to add documents
   - `query.py` to ask questions

## Folder Structure
- `ingest.py`: Ingest and embed documents
- `query.py`: Query pipeline
- `utils/`: Helper functions (chunking, embedding, etc.)
- `requirements.txt`: Dependencies
- `.env.example`: Example environment variables

## Notes
- Replace placeholders in `.env.example` with your actual API keys and endpoints.
- For Gemini, you may need to use Google's Vertex AI or Gemini API (see code comments).
