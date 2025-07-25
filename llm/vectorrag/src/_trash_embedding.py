import sys

from dotenv import load_dotenv
import os
import json
import pandas as pd
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
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


def process_json_lines(file_path):
    """Process each JSON line and extract relevant information."""
    extracted = []


    with open(file_path, 'r') as file:
        data = json.load(file)
        print(f"Processed Data:\n {json.dumps(data, indent=4)}")
        print(data['aufgaben'][1])
        return data



    # with open(file_path, encoding="utf-8") as f:
    #     for line in f:
    #         line = line.strip()
    #         if not line:
    #             continue
    #         obj = json.loads(line)
    #         extracted.append(obj)
    #
    # return extracted


#file_content = process_json_lines(os.getenv("DATASET_STORAGE_FOLDER")+"data.txt")
file_content = process_json_lines(os.getenv("DATASET_STORAGE_FOLDER")+"data_json.txt")


print(file_content['projektname'])

texts = []
texts = text_splitter.create_documents([file_content['projektname']],
                                       metadatas=[{
                                           "name_unternehmen": file_content['name_unternehmen'],
                                           "anschrift_unternehmen": file_content['anschrift_unternehmen'],
                                           "name_ansprechpartner": file_content['name_ansprechpartner'],
                                           "position_ansprechpartner": file_content['position_ansprechpartner'],
                                           "telefon_ansprechpartner": file_content['telefon_ansprechpartner'],
                                           "email_ansprechpartner": file_content['email_ansprechpartner'],
                                           "homepage": file_content['homepage'],
                                           "kurzbeschreibung": file_content['kurzbeschreibung'],
                                           "branche": file_content['branche'],
                                           "rolle_leistungserbringer": file_content['rolle_leistungserbringer'],
                                           "leistungsgegenstand": file_content['leistungsgegenstand'],
                                           "aufgaben": file_content['aufgaben'],
                                           "werkzeuge": file_content['werkzeuge'],
                                           "projektdauer": file_content['projektdauer'],
                                           "beauftragungszeitraum": file_content['beauftragungszeitraum'],
                                           "projektvolumen_pt": file_content['projektvolumen_pt'],
                                           "projektvolumen_euro": file_content['projektvolumen_euro'],
                                           "projektteam_groesse": file_content['projektteam_groesse'],
                                           "projektteam_rollen": file_content['projektteam_rollen']
                                       }])

uuids = [str(uuid4()) for _ in range(len(texts))]

vector_store.add_documents(documents=texts, ids=uuids)


# def process_json_lines(file_path):
#     """Process each JSON line and extract relevant information."""
#     extracted = []
#
#     with open(file_path, encoding="utf-8") as f:
#         for line in f:
#             line = line.strip()
#
#             # remove unwanted characters
#             preprocessed_line = line.translate(str.maketrans('', '', '-+.|:='))
#             print(preprocessed_line)
#
#             if not preprocessed_line:
#                 continue
#             #obj = json.loads(preprocessed_line)
#             extracted.append(preprocessed_line)
#
#     return extracted




# for line in file_content:
#
#     texts = []
#     if len(line.strip()) > 1:
#         print(line.strip())
#         texts = text_splitter.create_documents(line.strip())
#         uuids = [str(uuid4()) for _ in range(len(texts))]
#         vector_store.add_documents(documents=texts, ids=uuids)
#     else:
#         print("Empty line found!")
#
#     if len(line) < 10:
#         break