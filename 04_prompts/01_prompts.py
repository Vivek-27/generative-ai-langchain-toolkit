from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt = PromptTemplate(
    template="Explain {tech} to a {level} Java developer.",
    input_variables=["tech", "level"]
)

final_prompt = prompt.invoke({
    "tech":"Redis",
    "level":"beginner"
})

model = ChatOllama(
    model="qwen3:0.6b"
)

response = model.invoke(final_prompt)
print(response.content)