from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

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

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | llm
session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

config = {"configurable": {"session_id": "demo-session"}}

# interactions
response1 = conversational_chain.invoke(
    {"input": "Hi, my name is John"}, 
    config=config
)
print("Assistant: ", response1.content)
print("-" * 30)

response2 = conversational_chain.invoke(
    {"input": "Can you repeat my name?"}, 
    config=config
)
print("Assistant: ", response2.content)
print("-" * 30)

response3 = conversational_chain.invoke(
    # {"input": "Can you repeat my name in a motivational way?"}, 
    {"input": "What is 2 + 2?"}, 
    config=config
)
print("Assistant: ", response3.content)
print("-" * 30)

response4 = conversational_chain.invoke(
    {"input": "What is my name?"}, 
    config=config
)
print("Assistant: ", response4.content)
print("-" * 30)


# Automatic History Management
#   - RunnableWithMessageHistory handles injection and storage transparently
#   - No manual history passing required

# Message Format Preservation
# - InMemoryChatMessageHistory stores messages with proper metadata (role, content, timestamp)
# - Maintains conversation structure for the LLM

# Limitations
# - In-Memory Only: Data lost when program restarts
# - History Trimming: Grows indefinitely (can hit token limits)
# - Single Session Store: All sessions stored in one dictionary


# Production Considerations
# - For real applications, you'd replace InMemoryChatMessageHistory with:
#   - Database-backed: Redis, PostgreSQL, MongoDB
#   - History summarization: To manage token limits
#   - Session expiration: Automatic cleanup of old sessions
#   - Distributed storage: For multi-instance deployments