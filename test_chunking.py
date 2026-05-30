from utils.document_loader import load_pdf
from utils.chunker import split_documents

docs = load_pdf("uploads/Employee_Handbook.pdf")

chunks = split_documents(docs)

print(f"Original Pages: {len(docs)}")
print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)