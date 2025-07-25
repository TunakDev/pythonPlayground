from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.1")

template = """
Du bist ein Experte für das Beantworten von Fragen zu Informationen aus einem Referenzdokument fuer ein Softwareprojekt.
Hier sind einige Kontextinformationen: {context}
Hier ist die Frage, die du beantworten sollst: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n---------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n---------------------------------")
    if question == "q":
        break

    context = retriever.invoke(question)
    result = chain.invoke({"context": context, "question": question})
    print(result)