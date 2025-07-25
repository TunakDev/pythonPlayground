from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import pandas as pd

load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

loader = TextLoader("data/data_txt.txt")
read_data = loader.load()

print(read_data)

# with open("data/data_txt.txt", encoding="utf-8") as file:
#     read_data = file.read()
#     print(read_data)

all_splits = text_splitter.split_documents(read_data)
print(f"Split textfile into {len(all_splits)} sub-documents.")


embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    id_iterator=0

    for doc in all_splits:
        document = Document(
            page_content=doc.page_content, metadata={"filename":"data_txt.txt"},
            id=str(id_iterator)
        )
        ids.append(str(id_iterator))
        documents.append(document)
        id_iterator+=1

vector_store = Chroma(
    collection_name=os.getenv("COLLECTION_NAME"),
    embedding_function=embeddings,
    persist_directory=os.getenv("DATABASE_LOCATION"),
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)