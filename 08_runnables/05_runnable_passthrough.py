from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model = ChatOllama(
    model = "qwen3:0.6b"
)

parser = StrOutputParser()

explain_prompt = ChatPromptTemplate.from_template(
    "Explain {technology} to a beginner."
)
summary_prompt = ChatPromptTemplate.from_template(
    "Give a one-line summary of {technology}."
)

explain_chain = explain_prompt | model | parser

summary_chain = summary_prompt | model | parser

explain_chain = RunnablePassthrough()

parallel_chain = RunnableParallel(
    explanation=explain_chain,
    summary=summary_chain
)

result = parallel_chain.invoke({
    "technology": "Kafka"
})

print(result)