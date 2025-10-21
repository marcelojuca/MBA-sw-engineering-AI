import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ---------------- validate environment variables for PGVECTOR ----------------
for k in ("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

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

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-5-nano")


PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

custom_rag_prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)

# Create the RAG chain
# Question vectorization (handled by store_pgvector.as_retriever())
rag_chain = (
    {
        "contexto": store_pgvector.as_retriever(search_kwargs={"k": 10}) | format_docs, # retrieve the documents from the vector store and format the documents to a string
        "pergunta": RunnablePassthrough() # the question will be unchanged and propagated to the next step
    }
    | custom_rag_prompt
    | llm
)


def search_prompt(question=None):
    """
    Search for relevant documents and return the RAG chain.
    If question is provided, execute the search and return results.
    If no question is provided, return the chain for external use.
    """
    
    if question:
        result = rag_chain.invoke(question)
        return result
    else:
        return rag_chain


def main():
    # question = "Qual o faturamento da Empresa SuperTechIABrazil?"
    # question = "Qual o faturamento da Empresa Beta IA LTDA?"
    # question = "Qual o faturamento da Empresa Brava Telecom Holding?"
    # result = search_prompt(question)
    # print(result.content)
    # return result
    pass

if __name__ == "__main__":
    main()
