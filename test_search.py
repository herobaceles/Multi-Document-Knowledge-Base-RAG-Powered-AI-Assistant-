from utils.document_loader import load_pdf
from utils.chunker import split_documents
from utils.vector_store import create_vector_store

docs = load_pdf("uploads/Employee_Handbook.pdf")

chunks = split_documents(docs)

db = create_vector_store(chunks)

results = db.similarity_search(
    "What are the company values?",
    k=3
)

for i, result in enumerate(results):
    print(f"\nResult {i+1}")
    print("-" * 50)
    print(result.page_content)