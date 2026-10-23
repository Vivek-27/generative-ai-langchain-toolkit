from langchain_community.document_loaders import TextLoader

loader = TextLoader("data.txt")

documents = loader.load()

print(documents)