from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm_gemini = init_chat_model(
    model="gemini-2.5-flash", 
    temperature=0, 
    model_provider="google_genai"
)
message = llm_gemini.invoke("Hello World!")
print(message.content)
