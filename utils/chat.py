from utils.retriever import search_documents
from utils.rag import generate_answer

def ask_question(question):

    docs = search_documents(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = generate_answer(
        question,
        context
    )

    return answer, docs