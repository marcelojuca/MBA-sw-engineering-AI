# Python-dotenv

## Visão Geral

Python-dotenv lê pares chave-valor de um arquivo .env e pode defini-los como variáveis de ambiente. Ajuda no desenvolvimento de aplicações seguindo os princípios 12-factor.

**Fonte de Documentação**: `/theskumar/python-dotenv`

## Principais Recursos

- **Carregamento de .env**: Leitura automática de arquivos .env
- **12-Factor App**: Segue princípios de configuração externa
- **Variáveis de Ambiente**: Integração com os.environ
- **CLI**: Interface de linha de comando
- **IPython Integration**: Suporte para IPython/Jupyter
- **Streams**: Carregamento de configuração de streams
- **Múltiplos Arquivos**: Suporte para múltiplos arquivos .env

## Uso no Projeto

O projeto utiliza python-dotenv em praticamente todos os arquivos para carregar configurações sensíveis:

### Padrão de Uso

```python
from dotenv import load_dotenv

load_dotenv()
```

Este padrão aparece em:
- src/1.fundamentos/1-hello-world.py
- src/3.agentes-e-tools/1.agente-react-e-tools.py
- src/4.gerenciamento-de-memoria/1.armazenamento-de-historico.py
- src/5.loaders-e-banco-de-dados-vetoriais/3.ingestion-pgvector.py
- E outros arquivos

## Exemplos de Código

### Carregamento Básico

```python
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis de ambiente do .env

# Usar variáveis
import os
api_key = os.environ.get("OPENAI_API_KEY")
# ou
api_key = os.getenv("OPENAI_API_KEY")
```

### Carregamento com Path Específico

```python
from dotenv import load_dotenv
from pathlib import Path

# Caminho específico
dotenv_path = Path('.') / '.env.production'
load_dotenv(dotenv_path=dotenv_path)

# Ou string path
load_dotenv(dotenv_path='/path/to/.env')
```

### Sobrescrever Variáveis Existentes

```python
from dotenv import load_dotenv

# Por padrão, não sobrescreve variáveis existentes
load_dotenv()

# Para sobrescrever
load_dotenv(override=True)
```

### Carregar de Stream

```python
from io import StringIO
from dotenv import load_dotenv

config = StringIO("USER=foo\nEMAIL=foo@example.org")
load_dotenv(stream=config)
```

### Parse para Dicionário

```python
from dotenv import dotenv_values

# Retorna um dicionário sem modificar o ambiente
config = dotenv_values(".env")
# config = {"USER": "foo", "EMAIL": "foo@example.org"}
```

### Combinar Múltiplos Arquivos

```python
import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.shared"),     # variáveis compartilhadas
    **dotenv_values(".env.secret"),     # variáveis sensíveis
    **os.environ,                        # sobrescrever com env vars
}
```

### Busca Automática

```python
from dotenv import load_dotenv, find_dotenv

# Busca .env automaticamente subindo na árvore de diretórios
load_dotenv(find_dotenv())
```

## Interface de Linha de Comando

### Instalação com CLI

```bash
pip install "python-dotenv[cli]"
```

### Comandos

```bash
# Definir variável
dotenv set USER foo
dotenv set EMAIL foo@example.org

# Listar variáveis
dotenv list

# Listar como JSON
dotenv list --format=json

# Executar comando com variáveis carregadas
dotenv run -- python foo.py

# Obter valor específico
dotenv get OPENAI_API_KEY

# Remover variável
dotenv unset USER
```

## Integração com IPython/Jupyter

```python
# Carregar extensão
%load_ext dotenv

# Carregar .env
%dotenv

# Carregar .env específico
%dotenv relative/or/absolute/path/to/.env

# Com opções
%dotenv -o  # Override variáveis existentes
%dotenv -v  # Modo verbose
```

## Formato do Arquivo .env

### Variáveis Básicas

```bash
# Comentários são permitidos
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=your-api-key

# Com espaços (use aspas)
DATABASE_URL="postgresql://user:pass@localhost/db"
```

### Variáveis sem Valor

```bash
# Variável sem valor
FOO

# Com dotenv_values(), FOO será None
# Com load_dotenv(), FOO é ignorado
```

### Valores Multilinhas

```bash
# Usando \n explícito
FOO="first line\nsecond line"

# Usando quebra de linha real
FOO="first line
second line"
```

### Interpolação

```bash
# Referenciar outras variáveis
BASE_URL=https://api.example.com
API_ENDPOINT=${BASE_URL}/v1/users
```

### Aspas

```bash
# Sem aspas
SIMPLE=value

# Aspas simples (literal)
SINGLE='value with spaces'

# Aspas duplas (permite interpolação)
DOUBLE="value with ${VARIABLE}"
```

## Exemplo de .env do Projeto

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Pinecone Configuration
PINECONE_API_KEY=your-api-key
PINECONE_INDEX_NAME=your-index-name

# PostgreSQL Configuration (se usado)
PGVECTOR_URL=postgresql://user:password@localhost:5432/dbname
PGVECTOR_COLLECTION=my_collection
```

## Padrão de Uso no Projeto

### Carregamento e Validação

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Validar variáveis necessárias
required_vars = ("OPENAI_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX_NAME")
for var in required_vars:
    if not os.getenv(var):
        raise RuntimeError(f"Environment variable {var} is not set")
```

### Com Valores Padrão

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Com valor padrão
model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
temperature = float(os.getenv("TEMPERATURE", "0"))
```

### Type Conversion

```python
import os
from dotenv import load_dotenv

load_dotenv()

# String
api_key = os.getenv("OPENAI_API_KEY")

# Integer
port = int(os.getenv("PORT", "8000"))

# Boolean
debug = os.getenv("DEBUG", "false").lower() in ("true", "1", "yes")

# Float
temperature = float(os.getenv("TEMPERATURE", "0.0"))
```

## Boas Práticas

### 1. Nunca Commitar .env

```bash
# .gitignore
.env
.env.local
.env.*.local
```

### 2. Fornecer .env.example

```bash
# .env.example (commitar este)
OPENAI_API_KEY=your-openai-api-key-here
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_INDEX_NAME=your-index-name
```

### 3. Validar Variáveis Necessárias

```python
import os
from dotenv import load_dotenv

load_dotenv()

def validate_env():
    required = ["OPENAI_API_KEY", "PINECONE_API_KEY"]
    missing = [var for var in required if not os.getenv(var)]
    if missing:
        raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

validate_env()
```

### 4. Usar Tipos Apropriados

```python
from typing import Optional
import os

def get_env_int(key: str, default: Optional[int] = None) -> int:
    value = os.getenv(key)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"Environment variable {key} not set")
    return int(value)
```

### 5. Diferentes Ambientes

```bash
# Desenvolvimento
.env.development

# Teste
.env.test

# Produção
.env.production
```

```python
import os
from dotenv import load_dotenv

env = os.getenv("ENV", "development")
load_dotenv(f".env.{env}")
```

## Segurança

### ⚠️ Nunca:

1. Commitar arquivos .env no git
2. Compartilhar .env publicamente
3. Usar valores hardcoded em produção
4. Logar valores de variáveis sensíveis

### ✅ Sempre:

1. Usar .env para desenvolvimento local
2. Usar secrets managers em produção (AWS Secrets Manager, Azure Key Vault, etc.)
3. Adicionar .env ao .gitignore
4. Fornecer .env.example como template
5. Validar variáveis necessárias no startup

## Links Úteis

- [Documentação Oficial](https://github.com/theskumar/python-dotenv)
- [PyPI](https://pypi.org/project/python-dotenv/)
- [12-Factor App](https://12factor.net/config)

## Instalação

```bash
pip install python-dotenv
```

Com CLI:
```bash
pip install "python-dotenv[cli]"
```

Com uv:
```bash
uv pip install python-dotenv
```

## Alternativas

- **python-decouple**: Outra biblioteca similar
- **environs**: Com validação de tipos
- **pydantic-settings**: Integração com Pydantic
