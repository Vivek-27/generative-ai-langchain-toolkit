from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a backend mentor."),
    ("human", "Explain {technology} in one sentence.")
])

parser = StrOutputParser()

print(type(prompt))
print(type(model))
print(type(parser))


chain = prompt | model | parser

print(type(chain))