from langchain_ollama import ChatOllama

model = ChatOllama(
    model = "qwen3:4b"
)

response = model.invoke(
    "Explain Redis to a beginner Java developer."
)
print(response.content)