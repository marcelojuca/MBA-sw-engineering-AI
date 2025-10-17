from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}```",
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```",
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

translate = template_translate | llm | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm | StrOutputParser()

result = pipeline.invoke({"initial_text": "Ola, como voce esta?"})
print("-"*50)
print(result)
print("-"*50)