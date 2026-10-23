from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="""
You are a senior backend engineer.

Explain {technology} to a {level} Java developer.

Include:
1. What it is
2. Why it is used
3. One real-world example
""",
    input_variables=["technology", "level"]
)

model = ChatOllama(
    model="qwen3:4b"
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({
    "technology": "Redis",
    "level": "beginner"
})

print(response)