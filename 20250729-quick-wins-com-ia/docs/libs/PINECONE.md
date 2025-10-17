# Pinecone

## Visão Geral

Pinecone é um banco de dados vetorial líder projetado para construir aplicações de IA precisas e performáticas em escala na produção, oferecendo recursos como busca semântica, gerenciamento de dados e embeddings integrados.

**Fonte de Documentação**: `/websites/pinecone_io`

## Principais Recursos

- **Vector Search**: Busca por similaridade de vetores
- **Hybrid Search**: Busca combinando vetores densos e esparsos
- **Semantic Search**: Busca semântica usando embeddings
- **Lexical Search**: Busca lexical com vetores esparsos
- **Integrated Embeddings**: Embeddings integrados no índice
- **Metadata Filtering**: Filtragem por metadados
- **Namespaces**: Organização lógica de dados
- **Serverless**: Infraestrutura gerenciada

## Uso no Projeto

O projeto utiliza Pinecone para armazenamento e busca de embeddings de documentos:

### 1. Ingestion de Dados (src/5.loaders-e-banco-de-dados-vetoriais/3.ingestion-pgvector.py)
- Carregamento de PDFs
- Geração de embeddings
- Upload para Pinecone

### 2. Busca Vetorial (src/5.loaders-e-banco-de-dados-vetoriais/4.search-vector.py)
- Busca por similaridade
- Retrieval de documentos

## Exemplos de Código

### Inicialização do Cliente

```python
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")
```

### Criar Índice

```python
from pinecone import ServerlessSpec

pc.create_index(
    name="news",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)
```

### Criar Índice com Embedding Integrado

```python
# Índice que auto-embeds texto usando modelo hospedado
pc.create_index_for_model(
    name="auto-embed-index",
    cloud="aws",
    region="us-east-1",
    embed={
        "model": "llama-text-embed-v2",  # 1024 dimensões
        "field_map": {"text": "chunk_text"}  # Mapeia 'chunk_text' para embeddings
    },
    deletion_protection="disabled"
)

# Conectar ao índice
index = pc.Index(host="auto-embed-index-abc123.svc.aped-4627-b74a.pinecone.io")
```

### Conectar a um Índice

```python
index = pc.Index(host="INDEX_HOST")
```

### Upsert de Vetores Densos

```python
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")
index = pc.Index(host="INDEX_HOST")

index.upsert(
    vectors=[
        {
            "id": "A",
            "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            "metadata": {"genre": "comedy", "year": 2020}
        },
        {
            "id": "B",
            "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
            "metadata": {"genre": "documentary", "year": 2019}
        },
    ],
    namespace="example-namespace"
)
```

### Busca por Similaridade

```python
results = index.query(
    namespace="example-namespace",
    vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    top_k=3,
    include_values=True,
    include_metadata=True
)
```

### Busca com Texto (Auto-Embedding)

```python
# Busca com query de texto - converte automaticamente para vetor
results = index.search(
    namespace="knowledge-base",
    query={
        "inputs": {"text": "How do vector databases work?"},
        "top_k": 5
    },
    fields=["chunk_text", "source", "category"],  # Retornar campos específicos
    filter={
        "category": {"$eq": "technology"}
    }
)

# Exibir resultados
for record in results.records:
    print(f"ID: {record._id}")
    print(f"Score: {record._score:.4f}")
    print(f"Text: {record.chunk_text[:100]}...")
    print(f"Source: {record.source}")
    print("---")
```

### Busca com Filtros de Metadados

```python
# Query com filtros de metadados
results = index.query(
    namespace="documentation",
    vector=query_vector,
    top_k=10,
    filter={
        "$and": [
            {"category": {"$eq": "education"}},
            {"year": {"$gte": 2024}},
            {"tags": {"$in": ["ml", "ai"]}}
        ]
    },
    include_values=False,
    include_metadata=True
)

# Processar resultados
for match in results.matches:
    print(f"ID: {match.id}")
    print(f"Score: {match.score:.4f}")
    print(f"Title: {match.metadata.get('title')}")
    print(f"Author: {match.metadata.get('author')}")
    print("---")
```

### Hybrid Search (Denso + Esparso)

```python
import pinecone as pc

index = pc.Index(host="INDEX_HOST")
query = "Q3 2024 us economic data"

# Converter query em vetor denso
dense_query_embedding = pc.inference.embed(
    model="llama-text-embed-v2",
    inputs=query,
    parameters={"input_type": "query", "truncate": "END"}
)

# Converter query em vetor esparso
sparse_query_embedding = pc.inference.embed(
    model="pinecone-sparse-english-v0",
    inputs=query,
    parameters={"input_type": "query", "truncate": "END"}
)

for d, s in zip(dense_query_embedding, sparse_query_embedding):
    query_response = index.query(
        namespace="example-namespace",
        top_k=40,
        vector=d['values'],
        sparse_vector={'indices': s['sparse_indices'], 'values': s['sparse_values']},
        include_values=False,
        include_metadata=True
    )
    print(query_response)
```

### Busca com Reranking

```python
# Busca com query vector e reranking
search_with_vector = index.search(
    namespace="example-namespace",
    query={
        "vector": {
            "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        },
        "top_k": 4
    },
    fields=["category", "chunk_text"],
    rerank={
        "query": "Disease prevention",
        "model": "bge-reranker-v2-m3",
        "top_n": 2,
        "rank_fields": ["chunk_text"]  # Campo deve estar em 'fields'
    }
)
```

### Busca Lexical com Vetores Esparsos

```python
results = index.query(
    namespace="example-namespace",
    sparse_vector={
        "values": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        "indices": [767227209, 1640781426, 1690623792, 2021799277, 2152645940, 2295025838, 2443437770, 2779594451, 2956155693, 3476647774, 3818127854, 4283091697]
    },
    top_k=3,
    include_metadata=True,
    include_values=False
)
```

### Estatísticas do Índice

```python
stats = index.describe_index_stats()
print(stats)
```

### Listar Vetores com Paginação

```python
results = index.list_paginated(
    prefix='10103',
    limit=3,
    pagination_token='xndlsInByZWZpeCI6IjEwMTAzIn0=='
)

print(results.namespace)
print([v.id for v in results.vectors])
print(results.pagination.next)
print(results.usage)
```

## Integração com LangChain

### Inicializar PineconeVectorStore

```python
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
)

store = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
)
```

### Adicionar Documentos

```python
from langchain_core.documents import Document

documents = [
    Document(
        page_content="Conteúdo do documento",
        metadata={"source": "documento.pdf", "page": 1}
    )
]

store.add_documents(documents=documents, ids=["doc-1"])
```

### Busca por Similaridade

```python
results = store.similarity_search_with_score("query text", k=3)

for doc, score in results:
    print(f"Score: {score}")
    print(f"Content: {doc.page_content[:100]}...")
    print(f"Metadata: {doc.metadata}")
    print("---")
```

## Configuração no Projeto

### Variáveis de Ambiente

```bash
PINECONE_API_KEY=your-api-key
PINECONE_INDEX_NAME=your-index-name
```

### Exemplo de Uso no Projeto

```python
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# Verificar variáveis
for k in ("OPENAI_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

# Inicializar embeddings e store
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
)

store = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings,
    pinecone_api_key=os.getenv("PINECONE_API_KEY"),
)
```

## Operadores de Filtro

- `$eq`: Igual
- `$ne`: Diferente
- `$gt`: Maior que
- `$gte`: Maior ou igual
- `$lt`: Menor que
- `$lte`: Menor ou igual
- `$in`: Em lista
- `$nin`: Não em lista
- `$and`: E lógico
- `$or`: Ou lógico

## Boas Práticas

1. **Namespaces**: Use para organizar dados logicamente
2. **Metadata**: Adicione metadados ricos para filtragem eficiente
3. **Batch Operations**: Use upsert em lote para melhor performance
4. **Dimensões**: Garanta que as dimensões dos vetores correspondam ao índice
5. **Métricas**: Escolha a métrica correta (cosine, euclidean, dotproduct)
6. **Monitoring**: Monitore uso e performance do índice

## Links Úteis

- [Documentação Oficial](https://docs.pinecone.io/)
- [GitHub - Python Client](https://github.com/pinecone-io/pinecone-python-client)
- [Exemplos](https://github.com/pinecone-io/examples)
- [Console](https://app.pinecone.io/)
- [Pricing](https://www.pinecone.io/pricing/)

## Instalação

```bash
pip install pinecone-client langchain-pinecone
```

ou com uv:

```bash
uv pip install pinecone-client langchain-pinecone
```
