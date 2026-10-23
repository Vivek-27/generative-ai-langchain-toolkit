from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a Java backend mentor."),
    ("human", "Enxplain {tech} to a {level}.")
])

parser = StrOutputParser()

# formatted_prompt = prompt.invoke({
#     "technology": "Redis"
# })

# model_response = model.invoke(formatted_prompt)

# final_response = parser.invoke(model_response)

# print(final_response)

chain = prompt | model | parser

response = chain.invoke({
    "tech":"Redis",
    "level":"beginner"
})

print(response)