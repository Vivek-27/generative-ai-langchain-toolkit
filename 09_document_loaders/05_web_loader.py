from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Lenovo-IdeaPad-i7-13620H-Windows-83K1016UIN/dp/B0GSVP6MWV/?_encoding=UTF8"


loader = WebBaseLoader(url)

documents = loader.load()

print("Number of documents:", len(documents))

for doc in documents:
    print("\n--- CONTENT ---")
    print(doc.page_content[:2000])

    print("\n--- METADATA ---")
    print(doc.metadata)