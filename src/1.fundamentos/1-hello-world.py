from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
message = llm.invoke("Hello, how are you?")
print(message.content)


def main():
    print("Hello from fc!")


if __name__ == "__main__":
    main()
