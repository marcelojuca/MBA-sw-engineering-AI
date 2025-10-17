# OpenAI Python

## Visão Geral

A biblioteca OpenAI Python fornece acesso conveniente à API REST da OpenAI de qualquer aplicação Python 3.8+, oferecendo clientes síncronos e assíncronos.

**Fonte de Documentação**: `/openai/openai-python`

## Principais Recursos

- **Chat Completions**: Geração de respostas conversacionais
- **Embeddings**: Criação de representações vetoriais de texto
- **Completions**: Geração de texto (modelo legado)
- **Moderations**: Verificação de conteúdo
- **Threads e Assistants**: API de assistentes persistentes
- **Realtime API**: Interações em tempo real
- **Streaming**: Respostas em streaming

## Uso no Projeto

O projeto utiliza OpenAI principalmente através do LangChain (`langchain-openai`), mas a biblioteca base é fundamental para:

### 1. Modelos de Chat
- GPT-4o-mini (usado no projeto)
- GPT-4o
- GPT-4 Turbo

### 2. Embeddings
- text-embedding-3-small (usado no projeto)
- text-embedding-3-large

## Exemplos de Código

### Chat Completions Básico

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "How do I check if a Python object is an instance of a class?"},
    ],
)
print(completion.choices[0].message.content)
```

### Chat Completions com JSON Mode

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Generate a JSON with name and age fields"}
    ],
    response_format={"type": "json_object"},
)
print(response.choices[0].message.content)
```

### Criar Embeddings

```python
from openai import OpenAI

client = OpenAI()

query = "What caused the 1929 Great Depression?"

embedding = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
).data[0].embedding
```

### Moderação de Conteúdo

```python
client.moderations.create(**params)
```

### Gerenciar Conversations

```python
# Criar conversa
conversation = client.conversations.create(**params)

# Recuperar conversa
conversation = client.conversations.retrieve(conversation_id)

# Atualizar conversa
conversation = client.conversations.update(conversation_id, **params)

# Deletar conversa
client.conversations.delete(conversation_id)
```

### Completions (Legado)

```python
completion = client.completions.create(**params)
```

### Listar Chat Completions

```python
completions = client.chat.completions.list(**params)
```

### Recuperar Completion Específico

```python
completion = client.chat.completions.retrieve(completion_id)
```

### Mensagens de um Completion

```python
messages = client.chat.completions.messages.list(completion_id, **params)
```

## Endpoints da API

### POST /chat/completions

Cria um chat completion para as mensagens e parâmetros fornecidos.

```python
client.chat.completions.create(**params)
```

**Request Body:**
```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
}
```

**Response:**
```json
{
  "id": "chatcmpl-xxxxxxxxxxxxxxxxx",
  "object": "chat.completion",
  "created": 1678901234,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 10,
    "total_tokens": 30
  }
}
```

### GET /chat/completions

Lista todos os chat completions com filtros opcionais.

### GET /chat/completions/{completion_id}

Recupera um chat completion específico por ID.

### POST /chat/completions/{completion_id}

Atualiza um chat completion específico.

### DELETE /chat/completions/{completion_id}

Deleta um chat completion específico.

### GET /chat/completions/{completion_id}/messages

Lista mensagens para um chat completion específico.

## Tipos de Dados

### Chat Completions

```python
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionRole,
    ChatCompletionStreamOptions,
    ChatCompletionContentPart,
    ChatCompletionToolChoiceOption,
)
```

### Completions

```python
from openai.types import Completion, CompletionChoice, CompletionUsage
```

### Embeddings

```python
from openai.types import CreateEmbeddingResponse, Embedding, EmbeddingModel
```

## Configuração no Projeto

### Variáveis de Ambiente

```bash
OPENAI_API_KEY=sk-...
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
```

### Inicialização

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

# Model de Chat
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
)
```

## Modelos Disponíveis

### Chat Models
- `gpt-4o`: Modelo mais avançado
- `gpt-4o-mini`: Versão otimizada (usado no projeto)
- `gpt-4-turbo`: GPT-4 Turbo
- `gpt-3.5-turbo`: Modelo anterior

### Embedding Models
- `text-embedding-3-small`: 1536 dimensões (usado no projeto)
- `text-embedding-3-large`: 3072 dimensões
- `text-embedding-ada-002`: Modelo anterior

## Boas Práticas

1. **Gerenciamento de API Keys**: Sempre use variáveis de ambiente
2. **Rate Limiting**: Implemente retry logic para limites de taxa
3. **Streaming**: Use streaming para respostas longas
4. **Temperature**: Ajuste para controlar criatividade (0 = determinístico, 2 = criativo)
5. **Token Management**: Monitore uso de tokens para controle de custos

## Links Úteis

- [Documentação Oficial](https://platform.openai.com/docs)
- [GitHub](https://github.com/openai/openai-python)
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Pricing](https://openai.com/pricing)
- [Playground](https://platform.openai.com/playground)

## Instalação

```bash
pip install openai
```

ou com uv:

```bash
uv pip install openai
```
