from dotenv import load_dotenv
import os

load_dotenv(".env")
os.environ["GORQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_INDEX_NAME"] = os.getenv("PINECONE_INDEX_NAME")

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

load_dotenv()

loader = PyMuPDFLoader(
    "Learning_Python.pdf",
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

from pinecone import Pinecone, ServerlessSpec
import os

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
)

index_name = "python-rag-assistant"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

print("Index ready!")

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index(
    "python-rag-assistant"
)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

vector_store.add_documents(chunks)

print("Documents indexed successfully.") 

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 10,          # Number of chunks to return
        "fetch_k": 20,    # Initial pool size to fetch before applying diversity filter
        "lambda_mult": 0.5# 1 = strictly similar, 0 = maximum diversity
    }
)

from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0
)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the question ONLY from the provided context.

If the answer is not in the context, say:
"I don't have enough information to answer that."

Context:
{context}

Question:
{question}

Answer:
""")

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(messages)

    print("\nAnswer:")
    print(response.content)
    