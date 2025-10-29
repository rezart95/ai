# docker run --name pgvector-container -e POSTGRES_USER=langchain -e POSTGRES_PASSWORD=langchain -e POSTGRES_DB=langchain -p 6024:5432 -d pgvector/pgvector:pg16

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

raw_documents = TextLoader("./test.txt").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

documents = text_splitter.split_documents(raw_documents)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", api_key=openai_key)
connection = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"
db = PGVector.from_documents(documents, embeddings_model, connection=connection)

db.similarity_search("query", k=4)
