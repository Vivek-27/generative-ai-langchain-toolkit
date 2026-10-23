from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableSequence
model = ChatOllama(
    model="qwen3:0.6b"
)

prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a backend mentor."),
    ("human", "Explain {technology} in one sentence.")
])

parser = StrOutputParser()

chain = RunnableSequence(
    prompt,
    model,
    parser
)

response = chain.invoke({
    "technology":"OS"
})

print(response)