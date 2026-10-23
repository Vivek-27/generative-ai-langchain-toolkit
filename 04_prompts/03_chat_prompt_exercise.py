from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a strict technical interviewer."),
    ("human", """Explain {technology} to a {level} developer.
Give one real-world example.""")
    
])


chain = prompt | model

response = chain.invoke({
    "technology":"Docker",
    "level":"beginner"
})

print(response.content)