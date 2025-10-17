# LangChain

## Visão Geral

LangChain é um framework para desenvolver aplicações alimentadas por modelos de linguagem de grande escala (LLMs). Simplifica todo o ciclo de vida de aplicações LLM, oferecendo componentes de código aberto e integrações de terceiros.

**Fonte de Documentação**: `/websites/python_langchain`

## Principais Recursos

- **Chat Models**: Interação com modelos de chat como GPT, Claude, etc.
- **Prompts e Templates**: Criação de prompts dinâmicos e estruturados
- **Chains**: Encadeamento de componentes para workflows complexos
- **Agents**: Agentes inteligentes com acesso a ferramentas
- **Memory**: Gerenciamento de histórico de conversação
- **Document Loaders**: Carregamento de documentos de várias fontes
- **Text Splitters**: Divisão de texto em chunks
- **Vector Stores**: Integração com bancos de dados vetoriais
- **Embeddings**: Geração de embeddings de texto

## Uso no Projeto

O projeto utiliza LangChain nos seguintes contextos:

### 1. Fundamentos (src/1.fundamentos/)
- Inicialização de modelos de chat
- Templates de prompts
- Chat prompts

### 2. Chains e Processamento (src/2.chains-e-processamentos/)
- Criação de chains
- Decorators para chains
- Runnable Lambda
- Pipelines de processamento
- Sumarização com Map-Reduce

### 3. Agentes e Tools (src/3.agentes-e-tools/)
- Criação de agentes ReAct
- Uso de tools personalizadas
- Integração com Prompt Hub

### 4. Gerenciamento de Memória (src/4.gerenciamento-de-memoria/)
- Armazenamento de histórico
- Sliding window de histórico

### 5. Loaders e Vector Stores (src/5.loaders-e-banco-de-dados-vetoriais/)
- WebBaseLoader
- PyPDFLoader
- Integração com Pinecone

## Exemplos de Código

### Criar Chain Básico

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
    ("human", "{input}"),
])

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | model

result = chain.invoke({
    "input_language": "English",
    "output_language": "German",
    "input": "I love programming.",
})
```

### Criar Agente com Tools

```python
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

@tool
def calculate(expression: str) -> float:
    """Evaluate a mathematical expression."""
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

tools = [calculate]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when needed."),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input": "What's 15 multiplied by 23?"})
```

### Vector Store com Embeddings

```python
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = InMemoryVectorStore(embeddings)
```

### RAG Chain

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
retriever = vector_store.as_retriever()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

### Memory para Conversações

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | model

session_store = {}

def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
```

## Componentes Principais

### Chat Models
- `ChatOpenAI`: Modelos GPT da OpenAI
- `ChatAnthropic`: Modelos Claude
- Outros integrações disponíveis

### Prompts
- `PromptTemplate`: Templates básicos
- `ChatPromptTemplate`: Templates para chat
- `MessagesPlaceholder`: Placeholder para mensagens dinâmicas

### Tools e Agents
- `@tool`: Decorator para criar tools
- `create_tool_calling_agent`: Criação de agentes
- `create_react_agent`: Agentes ReAct
- `AgentExecutor`: Executor de agentes

### Memory
- `ConversationBufferMemory`: Memória de buffer
- `InMemoryChatMessageHistory`: Histórico em memória
- `RunnableWithMessageHistory`: Chain com histórico

### Document Loaders
- `WebBaseLoader`: Carregamento de páginas web
- `PyPDFLoader`: Carregamento de PDFs
- `TextLoader`: Carregamento de arquivos de texto

### Text Splitters
- `RecursiveCharacterTextSplitter`: Divisão recursiva de texto
- `CharacterTextSplitter`: Divisão por caracteres

### Vector Stores
- `PineconeVectorStore`: Integração com Pinecone
- `FAISS`: Vector store local
- `InMemoryVectorStore`: Vector store em memória

## Links Úteis

- [Documentação Oficial](https://python.langchain.com/)
- [GitHub](https://github.com/langchain-ai/langchain)
- [LangSmith](https://smith.langchain.com/) - Plataforma de observabilidade
- [LangGraph](https://langchain.com/langgraph) - Framework para agentes complexos

## Instalação

```bash
pip install langchain langchain-openai langchain-community langchain-core
```

ou com uv:

```bash
uv pip install langchain langchain-openai langchain-community langchain-core
```
