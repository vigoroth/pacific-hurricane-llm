import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.vectorstores import Chroma
from utils import get_file_path

persistent_directory = get_file_path("chroma_db", "db")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

query = "Your detailed query here"
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 100})
relevant_docs = retriever.invoke(query)

combined_input = query + "\n".join([doc.page_content for doc in relevant_docs])

model = ChatOpenAI(model="gpt-4o")
messages = [SystemMessage(content="You are a helpful assistant."), HumanMessage(content=combined_input)]

result = model.invoke(messages)

output_path = get_file_path("hurricanes_1975-gpt-04.txt", "output")
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(result.content)