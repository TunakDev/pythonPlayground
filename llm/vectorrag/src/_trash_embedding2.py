import sys

from dotenv import load_dotenv
import os
import json
import pandas as pd
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from ollama import chat
from ollama import ChatResponse
from uuid import uuid4
import shutil
import time


load_dotenv()

embeddings = OllamaEmbeddings(
    model=os.getenv("EMBEDDING_MODEL"),
)


if os.path.exists(os.getenv("DATABASE_LOCATION")):
    shutil.rmtree(os.getenv("DATABASE_LOCATION"))


vector_store = Chroma(
    collection_name=os.getenv("COLLECTION_NAME"),
    embedding_function=embeddings,
    persist_directory=os.getenv("DATABASE_LOCATION"),
)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

llm = init_chat_model(
    os.getenv("CHAT_MODEL"),
    model_provider=os.getenv("MODEL_PROVIDER"),
    temperature=0
)

# read content from txt file

loader = TextLoader("data/data_txt.txt")
read_data = loader.load()

print(read_data)

# with open("data/data_txt.txt", encoding="utf-8") as file:
#     read_data = file.read()
#     print(read_data)

all_splits = text_splitter.split_documents(read_data)
print(f"Split textfile into {len(all_splits)} sub-documents.")

_ = vector_store.add_documents(documents=all_splits)

prompt = PromptTemplate.from_template("""
Du bist ein Assistent für die Beantwortung von Fragen. Nutze die folgenden Teile des Kontexts um die Frage zu beantworten.
Wenn du die Frage nicht beantworten kannst, sag einfach, dass du es nicht weißt. 
Antworte in kurzen, prägnanten Sätzen.
Frage: {frage}
Kontext: {kontext}
Antwort:
""")

class State(TypedDict):
    frage: str
    kontext: List[Document]
    antwort: str


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["frage"])
    return {"kontext": retrieved_docs}


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["kontext"])
    messages = prompt.invoke({"frage": state["frage"], "kontext": docs_content})
    response = llm.invoke(messages)
    return {"antwort": response.content}




print("Let's ask the model for an answer... ")
response: ChatResponse = chat(model='llama3.2', messages=[
  prompt,
])
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)



example_message = prompt.invoke(
    {"kontext":"(Hier kommt der Kontext hinein)", "frage":"(Hier kommt die Frage hinein)"}
).to_messages()

assert len(example_message) == 1
print(example_message[0].content)
