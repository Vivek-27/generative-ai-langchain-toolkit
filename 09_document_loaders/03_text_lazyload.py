from pathlib import Path
from langchain_community.document_loaders import TextLoader

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data" / "data.txt"


loader = TextLoader(str(file_path))

documents = loader.lazy_load()

print(type(documents))

for doc in documents:
    print("\nCONTENT:")
    print(doc.page_content)

    print("\nMETADATA:")
    print(doc.metadata)