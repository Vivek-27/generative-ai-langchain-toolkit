from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior Java backend engineer."),
    ("human", "Explain {tech} to a {level} Java developer.")
])

# final_prompt = prompt.invoke({
#     "tech":"Redis",
#     "level":"beginner"
# })
# print(final_prompt)


chain = prompt | model

response = chain.invoke({
    "tech":"Redis",
    "level":"beginner"
})

print(response.content)
