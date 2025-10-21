# Desafio MBA Engenharia de Software com IA - Full Cycle

## Ingestão e Busca Semântica com LangChain e PostgreSQL

Este projeto implementa um sistema de busca semântica que permite:
- **Ingestão**: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector
- **Busca**: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: LangChain
- **Banco de dados**: PostgreSQL + pgVector
- **Execução do banco de dados**: Docker & Docker Compose
- **Embeddings**: OpenAI (text-embedding-3-small)
- **LLM**: GPT-5-nano

## Pré-requisitos

1. Docker e Docker Compose instalados
2. Python 3.14+ instalado
3. Chave de API da OpenAI

## Configuração

1. **Clone o repositório e navegue até o diretório**:
   ```bash
   cd 20251021-desafio-tecnico-ingestao-busca-semantica-langchain-postgres
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -e .
   ```

4. **Configure as variáveis de ambiente**:
   ```bash
   cp env.example .env
   ```
   
   Edite o arquivo `.env` e configure:
   ```
   OPENAI_API_KEY=sua_chave_da_openai_aqui
   PGVECTOR_URL=postgresql://postgres:postgres@localhost:5432/rag
   PGVECTOR_COLLECTION=documents
   ```

## Execução

### 1. Subir o banco de dados
```bash
docker compose up -d
```

### 2. Executar ingestão do PDF
```bash
python src/ingest.py
```

### 3. Rodar o chat
```bash
python src/chat.py
```

## Como usar o chat

Após executar `python src/chat.py`, você verá uma interface de chat interativa:

```
=== Chat de Busca Semântica ===
Digite 'sair' ou 'quit' para encerrar o chat.
==================================================

Faça sua pergunta: Qual o faturamento da Empresa SuperTechIABrazil?

PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

Faça sua pergunta: 
```

### Comandos de saída
- `sair`
- `quit`
- `exit`
- `q`
- `Ctrl+C`

## Estrutura do Projeto

```
├── src/
│   ├── ingest.py      # Script de ingestão do PDF
│   ├── search.py      # Lógica de busca semântica
│   └── chat.py        # Interface CLI do chat
├── document.pdf       # Arquivo PDF para ingestão
├── docker-compose.yaml # Configuração do PostgreSQL
├── env.example        # Exemplo de variáveis de ambiente
└── pyproject.toml     # Dependências do projeto
```

## Funcionalidades

- **Chunking**: PDF dividido em chunks de 1000 caracteres com overlap de 150
- **Embeddings**: Conversão de chunks em vetores usando OpenAI
- **Armazenamento**: Vetores armazenados no PostgreSQL com pgVector
- **Busca**: Busca por similaridade dos 10 resultados mais relevantes
- **RAG**: Resposta baseada apenas no contexto do PDF
- **Validação**: Respostas para perguntas fora do contexto

## Exemplos de Uso

### Pergunta dentro do contexto:
```
Pergunta: "Qual o faturamento da Empresa SuperTechIABrazil?"
Resposta: "O faturamento foi de 10 milhões de reais."
```

### Pergunta fora do contexto:
```
Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."
```