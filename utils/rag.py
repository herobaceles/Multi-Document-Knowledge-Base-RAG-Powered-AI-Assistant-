from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

def generate_answer(question, context):

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt)