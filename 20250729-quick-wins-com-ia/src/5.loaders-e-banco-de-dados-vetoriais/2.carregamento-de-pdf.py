from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader(file_path="/Users/mhcj/Downloads/github/fc/5.loaders-e-banco-de-dados-vetoriais/sample.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

print(len(chunks))