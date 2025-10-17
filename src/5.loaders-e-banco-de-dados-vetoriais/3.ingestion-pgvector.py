import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
for k in ("OPENAI_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

current_dir = Path(__file__).parent
pdf_path = current_dir / "sample.pdf"

doc = PyPDFLoader(pdf_path).load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=150, add_start_index=False
).split_documents(doc)
if not splitter:
    raise RuntimeError("No chunks were created")

enriched_docs = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)},
    )
    for d in splitter
]

ids = [f"doc-{i}" for i in range(len(enriched_docs))]
# embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))
# store = PGVector(
#     embeddings=embeddings,
#     collection_name=os.getenv("PGVECTOR_COLLECTION"),
#     connection=os.getenv("PGVECTOR_URL"),
#     use_jsonb=True,
# )

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
)
store = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
)

# store.add_documents(documents=enriched_docs, ids=ids)
