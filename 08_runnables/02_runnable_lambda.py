from langchain_core.runnables import RunnableLambda

def uppercase(text):
    return text.upper()

upper_runnable = RunnableLambda(uppercase)

result = upper_runnable.invoke("hello docker")

print(result)