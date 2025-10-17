from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm_gpt = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0
)

message = llm_gpt.invoke("Hello World!")
print(message.content)
