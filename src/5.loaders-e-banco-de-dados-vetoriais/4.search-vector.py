import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_postgres import PGVector

load_dotenv()

# ---------------- validate environment variables for PGVECTOR ----------------
for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

# ---------------- validate environment variables for PINECONE ----------------
# for k in ("OPENAI_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX_NAME"):
#     if not os.getenv(k):
#         raise RuntimeError(f"Environment variable {k} is not set")

# ---------------- create embeddings ----------------
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
)


# ---------------- create PGVector store ----------------
store_pgvector = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

# ---------------- create Pinecone store ----------------
# store_pinecone = PineconeVectorStore(
#     index_name=os.getenv("PINECONE_INDEX_NAME"),
#     embedding=embeddings,
#     pinecone_api_key=os.getenv("PINECONE_API_KEY"),
# )

# ---------------- search vector store ----------------
query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"
results = store_pgvector.similarity_search_with_score(query, k=3)

# Sort results by similarity score (highest first)
# Note: similarity_search_with_score already returns results sorted by score descending
# But this explicit sorting ensures proper order
results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

print(f"Found {len(results_sorted)} results for query: '{query}'\n")

for i, (doc, score) in enumerate(results_sorted, start=1):
    print(f"-" * 50)
    print(f"Result {i}, Score: {score:.4f}")
    print(f"-" * 10)
    print("\nDocument:\n")
    print(doc.page_content.strip())
    print("\nMetadata:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")
    print()  # Add extra line between results
