Multi-Document Knowledge Base (RAG-Powered AI Assistant)
Overview

This project is a Retrieval-Augmented Generation (RAG) system that allows users to upload multiple PDF documents and ask questions in natural language. The system retrieves relevant context from the documents and generates accurate AI-powered answers using a Large Language Model.

It demonstrates how LLMs can be grounded with private data using embeddings and vector search.

Key Features
Upload multiple PDF documents
Extract and process text automatically
Chunk documents for efficient retrieval
Generate embeddings using sentence transformers
Store and search vectors using ChromaDB
Ask questions in natural language
Get AI-generated answers based on document context
View source passages used for responses
Simple web UI using Streamlit
Tech Stack
Frontend
Streamlit
Backend
Python
AI / LLM
Ollama (Llama 3.2)
Embeddings
Sentence Transformers (all-MiniLM-L6-v2)
Vector Database
ChromaDB
Frameworks / Libraries
LangChain
PyPDF
HuggingFace Transformers
System Architecture
User
  ↓
Streamlit UI
  ↓
Upload PDF
  ↓
PyPDF Loader
  ↓
Text Chunking
  ↓
Embedding Model
  ↓
ChromaDB Vector Store
  ↓
Semantic Retrieval
  ↓
Llama 3.2 (Ollama)
  ↓
Generated Answer
How It Works
User uploads PDF documents
Text is extracted using PyPDF
Documents are split into chunks
Each chunk is converted into embeddings
Embeddings are stored in ChromaDB
User asks a question
Relevant chunks are retrieved using similarity search
Context is passed to LLM (Llama 3.2)
Model generates final answer
Installation
1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd multi-document-rag
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
Install Ollama

Download and install:

https://ollama.com

Pull the model:

ollama pull llama3.2

Start server:

ollama serve
Run the App
streamlit run app.py
Example Usage
Upload a PDF (e.g., Employee Handbook)
Click Process Documents
Ask a question:
What are the company core values?
Get AI-generated answer with supporting sources
Skills Demonstrated
Retrieval-Augmented Generation (RAG)
Vector Databases (ChromaDB)
Embedding Models
LLM Integration (Ollama)
NLP Document Processing
Python Backend Development
Streamlit UI Development
Project Structure
multi-doc-rag/
│
├── app.py
├── utils/
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── chat.py
│   └── index_documents.py
│
├── uploads/
├── vectorstore/
├── requirements.txt
└── README.md
