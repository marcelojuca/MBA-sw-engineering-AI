# PyPDF

## Visão Geral

pypdf é uma biblioteca Python pura, livre e de código aberto para manipular arquivos PDF. Suporta divisão, mesclagem, corte, transformação, adição de dados e extração de texto e metadados.

**Fonte de Documentação**: `/py-pdf/pypdf`

## Principais Recursos

- **Leitura de PDF**: Leitura e navegação em PDFs
- **Extração de Texto**: Extração de texto de páginas
- **Divisão**: Separação de PDFs em páginas individuais
- **Mesclagem**: Combinação de múltiplos PDFs
- **Rotação**: Rotação de páginas
- **Metadados**: Leitura e escrita de metadados
- **Anotações**: Leitura de anotações e anexos
- **Sem Dependências Externas**: Biblioteca pura Python

## Uso no Projeto

O projeto utiliza PyPDF através do LangChain para carregamento de documentos PDF:

### 1. Carregamento de PDF (src/5.loaders-e-banco-de-dados-vetoriais/2.carregamento-de-pdf.py)
- PyPDFLoader do LangChain
- Leitura de documentos PDF

### 2. Processamento (src/5.loaders-e-banco-de-dados-vetoriais/3.ingestion-pgvector.py)
- Carregamento e divisão de PDFs
- Preparação para embedding

## Exemplos de Código

### Leitura Básica de PDF

```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
```

### Extrair Texto de Todas as Páginas

```python
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Uso
pdf_text = extract_text_from_pdf("report.pdf")
print(pdf_text)
```

### Extrair Texto de Página Específica

```python
from pypdf import PdfReader

def extract_text_from_page(pdf_path, page_number):
    reader = PdfReader(pdf_path)
    page = reader.pages[page_number]
    return page.extract_text()

# Uso
text = extract_text_from_page("document.pdf", 0)  # Primeira página
print(text)
```

### Extração com Diferentes Orientações

```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")
page = reader.pages[0]

# Extrair todo o texto
print(page.extract_text())

# Extrair apenas texto orientado para cima
print(page.extract_text(0))

# Extrair texto orientado para cima e virado para esquerda
print(page.extract_text((0, 90)))

# Extrair texto preservando layout
print(page.extract_text(extraction_mode="layout"))

# Preservar posicionamento horizontal sem excesso de espaço vertical
print(page.extract_text(
    extraction_mode="layout",
    layout_mode_space_vertically=False
))

# Ajustar espaçamento horizontal
print(page.extract_text(
    extraction_mode="layout",
    layout_mode_scale_weight=1.0
))

# Incluir texto rotacionado
print(page.extract_text(
    extraction_mode="layout",
    layout_mode_strip_rotated=False
))
```

### Extração Customizada com Visitor Function

```python
from pypdf import PdfReader

reader = PdfReader("GeoBase_NHNC1_Data_Model_UML_EN.pdf")
page = reader.pages[3]

parts = []

def visitor_body(text, cm, tm, font_dict, font_size):
    y = cm[5]
    # Ignorar header e footer
    if 50 < y < 720:
        parts.append(text)

page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)
```

### Dividir PDF em Páginas Separadas

```python
from pypdf import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_dir):
    reader = PdfReader(input_pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = f"{output_dir}/page_{i+1}.pdf"
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

# Uso
import os
output_directory = "./split_pages"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
split_pdf("document.pdf", output_directory)
```

### Dividir PDF por Intervalos de Páginas

```python
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_prefix, pages_per_file):
    reader = PdfReader(input_path)
    num_pages = len(reader.pages)
    for i in range(0, num_pages, pages_per_file):
        writer = PdfWriter()
        for j in range(pages_per_file):
            if i + j < num_pages:
                writer.add_page(reader.pages[i + j])
        output_filename = f"{output_prefix}_{i // pages_per_file + 1}.pdf"
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)

# Uso: dividir em arquivos de 2 páginas cada
split_pdf('original.pdf', 'split', 2)
```

### Dividir por Ranges Específicos

```python
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_prefix, page_ranges):
    reader = PdfReader(input_path)
    for i, (start_page, end_page) in enumerate(page_ranges):
        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])
        output_filename = f"{output_prefix}_part_{i+1}.pdf"
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

# Uso: páginas 0-4 em um arquivo, 5-9 em outro
split_pdf("document.pdf", "split_doc", [(0, 4), (5, 9)])
```

### Ler Anotações de Texto

```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")

for page in reader.pages:
    if "/Annots" in page:
        for annotation in page["/Annots"]:
            subtype = annotation.get_object()["/Subtype"]
            if subtype == "/Text":
                print(annotation.get_object()["/Contents"])
```

### Ler Anexos de Arquivo

```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")

attachments = {}
for page in reader.pages:
    if "/Annots" in page:
        for annotation in page["/Annots"]:
            subtype = annotation.get_object()["/Subtype"]
            if subtype == "/FileAttachment":
                fileobj = annotation.get_object()["/FS"]
                attachments[fileobj["/F"]] = fileobj["/EF"]["/F"].get_data()

# Salvar anexos
for filename, data in attachments.items():
    with open(filename, 'wb') as f:
        f.write(data)
```

### Mesclar PDFs

```python
from pypdf import PdfWriter

writer = PdfWriter()

# Adicionar páginas de múltiplos arquivos
writer.append("file1.pdf")
writer.append("file2.pdf")
writer.append("file3.pdf", pages=(0, 3))  # Apenas páginas 0-3

# Salvar PDF mesclado
with open("merged.pdf", "wb") as output_file:
    writer.write(output_file)
```

## Integração com LangChain

### PyPDFLoader

```python
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

pdf_path = Path(__file__).parent / "sample.pdf"

# Carregar PDF
doc = PyPDFLoader(pdf_path).load()

# doc é uma lista de Documents, um por página
for page in doc:
    print(f"Page {page.metadata['page']}:")
    print(page.page_content[:200])
    print("---")
```

### Com Text Splitter

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

pdf_path = Path(__file__).parent / "sample.pdf"

# Carregar e dividir
doc = PyPDFLoader(pdf_path).load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
    add_start_index=False
)
chunks = splitter.split_documents(doc)

print(f"Total de chunks: {len(chunks)}")
```

### Preparar para Vector Store

```python
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

pdf_path = Path(__file__).parent / "sample.pdf"

# Carregar
doc = PyPDFLoader(pdf_path).load()

# Dividir
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
    add_start_index=False
)
chunks = splitter.split_documents(doc)

# Enriquecer metadados
enriched_docs = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)},
    )
    for d in chunks
]

# Criar IDs
ids = [f"doc-{i}" for i in range(len(enriched_docs))]

# Agora pode fazer upsert no vector store
```

## Informações Adicionais

### Metadados Disponíveis

Ao usar `PdfReader`, você pode acessar metadados:

```python
from pypdf import PdfReader

reader = PdfReader("example.pdf")

# Metadados do documento
metadata = reader.metadata
print(f"Author: {metadata.author}")
print(f"Title: {metadata.title}")
print(f"Subject: {metadata.subject}")
print(f"Creator: {metadata.creator}")
print(f"Producer: {metadata.producer}")
```

### Limitações

- **OCR**: pypdf não faz OCR. Para PDFs scaneados, use pytesseract ou similar
- **Tabelas**: Extração de tabelas pode ser imprecisa
- **Imagens**: Não extrai texto de imagens
- **Layout Complexo**: PDFs com layouts complexos podem ter extração imperfeita

## Boas Práticas

1. **Tratamento de Erros**: Sempre use try-except ao processar PDFs
2. **Encoding**: Atenção a problemas de encoding em textos extraídos
3. **Performance**: Para PDFs grandes, processe por páginas
4. **Validação**: Verifique se o PDF foi carregado corretamente antes de processar
5. **Cleanup**: Feche readers após uso para liberar recursos

## Links Úteis

- [Documentação Oficial](https://pypdf.readthedocs.io/)
- [GitHub](https://github.com/py-pdf/pypdf)
- [PyPI](https://pypi.org/project/pypdf/)
- [Exemplos](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)

## Instalação

```bash
pip install pypdf
```

ou com uv:

```bash
uv pip install pypdf
```

## Alternativas

- **PyMuPDF (fitz)**: Mais rápido, mas com dependências C
- **pdfplumber**: Melhor para tabelas
- **PyPDF2**: Versão anterior (descontinuada, use pypdf)
