from langchain_community.document_loaders import TextLoader

loader = TextLoader("data.txt")

documents = loader.load()

print("Number of documents:", len(documents))

doc = documents[0]

print("\nCONTENT:", doc.page_content)
print("\METADATA:", doc.metadata)
