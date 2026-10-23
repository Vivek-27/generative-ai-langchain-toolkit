from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


model = ChatOllama(model="qwen3:0.6b")

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=["question", "text"]
)

paresr = StrOutputParser()

url = "https://www.amazon.in/Lenovo-IdeaPad-i7-13620H-Windows-83K1016UIN/dp/B0GSVP6MWV/?_encoding=UTF8"

loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | paresr

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))