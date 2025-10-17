from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

question_template = PromptTemplate(
    input_variables=["name"], template="Hi, I am {name}. Tell me a joke with my name?"
)

chain = question_template | model

result = chain.invoke({"name": "John"})

print(result.content)
