from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="qwen3:0.6b"
)    

parser = StrOutputParser()

chain = model | parser


response = chain.invoke(
    "Explain Docker in one sentence."
)

print(type(response))
print(response)
