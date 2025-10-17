from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that can answer questions about the user's input.",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | chat_model
session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


converstional_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "demo-session"}}

# interactions
response1 = converstional_chain.invoke({"input": "Hi, my name is John"}, config=config)
print("Assistant: ", response1.content)
print("-" * 30)

response2 = converstional_chain.invoke(
    {"input": "Can you repeat my name?"}, config=config
)
print("Assistant: ", response2.content)
print("-" * 30)

response3 = converstional_chain.invoke(
    {"input": "Can you repeat my name in a motivational way?"}, config=config
)
print("Assistant: ", response3.content)
print("-" * 30)

response4 = converstional_chain.invoke({"input": "What is my name?"}, config=config)
print("Assistant: ", response4.content)
print("-" * 30)
