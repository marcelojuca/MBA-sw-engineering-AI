from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


system = (
    "system",
    "You are a helpful assistant that can answer questions about the user's input.",
)
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate.from_messages([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who was Alan Turing?")

for message in messages:
    print(f"{message.type}: {message.content}")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

result = llm.invoke(messages)

print(result.content)
