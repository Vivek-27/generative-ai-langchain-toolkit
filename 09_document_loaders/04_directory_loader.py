from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data"

loader = DirectoryLoader(
    str(data_path),
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()


print("Number of documents:", len(documents))

for doc in documents:
    print("\n--- DOCUMENT ---")
    print("Content:")
    print(doc.page_content)
    print("Metadata:")
    print(doc.metadata)