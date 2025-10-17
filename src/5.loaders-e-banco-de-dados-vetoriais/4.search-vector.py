import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
for k in ("OPENAI_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
)
store = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
)

results = store.similarity_search_with_score(query, k=3)

for i, (doc, score) in enumerate(results, start=1):
    print(f"-" * 50)
    print(f"Result {i}, Score: {score}")
    print(f"-" * 10)
    print("\nDocument:\n")
    print(doc.page_content.strip())
    print("\nMetadata:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")
