from utils.document_loader import load_pdf
from utils.chunker import split_documents
from utils.vector_store import create_vector_store

def index_document(pdf_path):
    docs = load_pdf(pdf_path)
    chunks = split_documents(docs)

    db = create_vector_store(chunks)

    return db