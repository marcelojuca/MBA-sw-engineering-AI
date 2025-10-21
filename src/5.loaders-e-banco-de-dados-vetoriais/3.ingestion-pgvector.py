import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
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

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "sample.pdf")

# ---------------- load PDF file ----------------
doc = PyPDFLoader(pdf_path).load()

# ---------------- split PDF file into chunks ----------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=150, 
    add_start_index=False
).split_documents(doc)

if not splitter:
    raise RuntimeError("No chunks were created")

# ---------------- enrich documents with metadata ----------------
enriched_docs = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)},
    )
    for d in splitter
]

# ---------------- create IDs for documents ----------------
ids = [f"doc-{i}" for i in range(len(enriched_docs))]

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
store_pinecone = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
)

# ---------------- add documents to stores ----------------
store_pgvector.add_documents(documents=enriched_docs, ids=ids)
# store_pinecone.add_documents(documents=enriched_docs, ids=ids)
