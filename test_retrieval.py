from utils.retriever import search_documents

results = search_documents(
    "What are the company values?"
)

for result in results:
    print(result.page_content)