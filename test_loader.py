from utils.document_loader import load_pdf

docs = load_pdf("uploads/Employee_Handbook.pdf")

print(f"Pages loaded: {len(docs)}")
print()
print(docs[0].page_content[:500])