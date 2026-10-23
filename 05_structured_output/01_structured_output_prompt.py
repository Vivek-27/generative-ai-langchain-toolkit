from pydantic import BaseModel
from langchain_ollama import ChatOllama

class TechInfo(BaseModel):
    technology: str
    defination: str
    user_case: list[str]


model = ChatOllama(
    model="qwen3:0.6b"
)    

structured_model = model.with_structured_output(TechInfo)

response = structured_model.invoke(
    "Explain Docker and give its main use cases."
)

print(response)