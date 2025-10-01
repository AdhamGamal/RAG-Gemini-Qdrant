# 📘 RAG with Qdrant, Google Gemini, and LangChain

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain Expression Language (LCEL)**, **Qdrant** as a vector store, and **Google Gemini** as the LLM. It allows you to query knowledge from your own PDF documents, combining **retrieval** and **generation** in a clean, modular pipeline.

---

## 🚀 Project Overview

The pipeline works as follows:

1. **PDF Loader & Splitter**

   * Loads PDF documents and splits them into smaller text chunks for efficient retrieval.

2. **Embeddings Model**

   * Generates dense vector representations of the document chunks.
   * These embeddings are stored in the Qdrant vector database.

3. **Vector Store (Qdrant)**

   * Stores embeddings and enables fast similarity search (retriever).
   * When you ask a question, Qdrant retrieves the most relevant chunks.

4. **Retriever + Formatter**

   * The retriever pulls the top-k most relevant chunks.
   * `format_docs` converts them into a context string suitable for prompting.

5. **Prompt Template**

   * Uses a **ChatPromptTemplate** with `{context}` and `{question}` variables.
   * Ensures the LLM receives both the retrieved knowledge and the user’s query.

6. **LLM (Google Gemini)**

   * Answers the user’s question in natural language.
   * Powered by Google’s **Generative AI API**.

7. **LCEL Pipeline**

   * Built using LangChain Expression Language.
   * Final output is a plain string answer.

---

## 📂 Project Structure

```
project/
│── data/                  # PDF documents
│   ├── eldoria_history.pdf
│   ├── quantum_drive_specs.pdf
│   └── zirconia_recipes.pdf
│
│── utils/                 # Modular pipeline helpers
│   ├── loader.py          # PDF loader & splitter
│   ├── embeddings.py      # Embeddings model
│   ├── ingest.py          # Store docs in Qdrant
│   ├── retriever.py       # Retriever + format_docs
│   ├── llm.py             # LLM setup
│   └── prompt.py          # Prompt templates
│
│── rag_notebook.ipynb     # Main RAG pipeline
│── .env                   # API keys and config
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## 🛠️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Environment Variables

Create a `.env` file:

```env
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_COLLECTION=rag_demo
GOOGLE_API_KEY=your_google_api_key
```

---

### 3. Run Qdrant in Docker

Start a local Qdrant instance:

```bash
docker run -d \
  -p 6333:6333 \
  -v $(pwd)/qdrant_storage:/qdrant/storage \
  qdrant/qdrant
```

---

### 4. Obtain API Keys

* **Google API Key**
  Create a project in [Google AI Studio](https://aistudio.google.com/), enable the Generative AI API, and generate an API key.

* **Qdrant API Key** (optional for local, required for cloud)
  If you use Qdrant Cloud, generate an API key from the dashboard.

---

### 5. Run the RAG pipeline

You can test the pipeline using the `rag_notebook.ipynb`

You should see output like:

```
[QUERY] What led to the fall of the Kingdom of Eldoria?
[ANSWER] The fall of Eldoria was caused by...
```

---

## ❓ Why These Components?

* **LangChain Expression Language (LCEL)**
  A modern, declarative way to compose RAG pipelines. Cleaner than old `RetrievalQA`.

* **Qdrant (Vector Store)**
  Efficient, production-ready similarity search for embeddings.

* **Embeddings Model**
  Converts text chunks into numerical vectors for retrieval.

* **RunnablePassthrough**
  Ensures the **original user query** is preserved while context is retrieved.

* **ChatPromptTemplate**
  Structured prompt designed for chat-based LLMs. Handles both `{context}` and `{question}` cleanly.

* **Google Gemini (LLM)**
  Generates fluent answers with access to retrieved knowledge.

---

✅ With this setup, you now have a modular, extensible **RAG system** that can be adapted to any PDF knowledge base.