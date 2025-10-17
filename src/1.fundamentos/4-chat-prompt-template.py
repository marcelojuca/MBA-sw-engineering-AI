from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


system_message = (
    "system",
    "You are a helpful assistant that can answer questions about the user's input.",
)
user_message = (
    "user", 
    "{question}"
)

chat_prompt = ChatPromptTemplate.from_messages([system_message, user_message])

messages = chat_prompt.format_messages(style="funny", question="Who was Alan Turing?")

for message in messages:
    print("-"*50)
    print(f"{message.type}: {message.content}")
    print("-"*30)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

result = llm.invoke(messages)

print(result.content)
