from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = PromptTemplate(
    template="Explain {tech} to a {level} Java developer.",
    input_variables=["tech", "level"]
)


chain = prompt | model

response = chain.invoke({
    "tech":"Redis",
    "level":"beginner"
})

print(response.content)