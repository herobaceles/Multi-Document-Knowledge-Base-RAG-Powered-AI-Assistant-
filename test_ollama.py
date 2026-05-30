from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

response = llm.invoke(
    "What is a company handbook?"
)

print(response)