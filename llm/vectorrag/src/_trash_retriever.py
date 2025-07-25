# import basics
import os
from dotenv import load_dotenv

# import langchain
from langchain.agents import AgentExecutor
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_tool_calling_agent
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool

# load environment variables
load_dotenv()

embeddings = OllamaEmbeddings(
    model=os.getenv("EMBEDDING_MODEL"),
)

###############################   INITIALIZE CHROMA VECTOR STORE   #############################################################################################

vector_store = Chroma(
    collection_name=os.getenv("COLLECTION_NAME"),
    embedding_function=embeddings,
    persist_directory=os.getenv("DATABASE_LOCATION"),
)

###############################   INITIALIZE CHAT MODEL   #######################################################################################################

llm = init_chat_model(
    os.getenv("CHAT_MODEL"),
    model_provider=os.getenv("MODEL_PROVIDER"),
    temperature=0
)

# pulling prompt from hub
prompt = PromptTemplate.from_template("""
Du bist ein hilfreicher Assistent, dem Informationen zu Referenzen von Softwareprojekten gegeben werden. 
Du erhältst eine Anfrage.
Deine Aufgabe ist es, relevante Informationen aus einer Vektor-Datenbank zu beschaffen und eine Antwort auf die Anfrage zu geben.
Hierfür nutzt du das Tool 'retrieve', um die relevante Information zu beschaffen.

Die Anfrage sieht folgendermaßen aus:
{input}

Bitte gib eine kurze und prägnante Antwort basierend auf den beschafften Informationen.
Wenn du die Antwort nicht kennst, antworte mit "Ich weiß es leider nicht" (und gib keine Quelle zurück).

Du kannst das Notizbuch verwenden, um Zwischenergebnisse oder Notizen zu speichern.
Das Notizbuch sieht wie folgt aus:
{agent_scratchpad}

Bitte nenne zu jedem Stück Information auch deine Quelle.

Antworte folgendermaßen:

<Antwort auf die Frage>
Quelle: quell_url
""")

# creating the retriever tool
@tool
def retrieve(query: str):
    """Retrieve information related to a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)

    serialized = ""

    for doc in retrieved_docs:
        serialized += f"Gefundene Antwort: {doc.page_content}\n\n"

    return serialized

# combining all tools
tools = [retrieve]

# initiating the agent
agent = create_tool_calling_agent(llm, tools, prompt)

# create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

user_question = str(input("Geben Sie eine Frage ein.\n"))

result = agent_executor.invoke({"input": user_question})

print(result["output"])