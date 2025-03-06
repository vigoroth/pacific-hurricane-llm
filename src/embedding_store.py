import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

current_dir = os.path.dirname(os.path.abspath('__file__'))
file_path = os.path.join(current_dir, "../html/test_parsed.txt")
persistent_directory = os.path.join(current_dir, "../db/chroma_db")

loader = TextLoader(file_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)