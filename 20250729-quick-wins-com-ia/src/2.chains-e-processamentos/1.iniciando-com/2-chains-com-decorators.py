from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI

load_dotenv()


@chain
def square(inputs: dict) -> dict:
    x = inputs["x"]
    return {"square_result": x * x}


result = square.invoke({"x": 10})
print(result)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

question_template = PromptTemplate(
    input_variables=["name"], template="Hi, I am {name}. Tell me a joke with my name?"
)

question_template2 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}",
)

chain = question_template | model
chain2 = square | question_template2 | model

# result = chain.invoke({"name": "John"})
# print(result.content)

result2 = chain2.invoke({"x": 10})
print(result2.content)
