from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool("calculator")
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and returns the result."""
    try:
        result = eval(expression)
    except Exception as e:
        return f"Error: {e}"
    return str(result)


@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Mock a web search for the given query."""

    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C.",
    }

    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."


prompt = hub.pull("hwchase17/react")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [calculator, web_search_mock]
agent_chain = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent_chain,
    tools=tools,
    verbose=True,
    handle_parsing_errors="Invalid format. Either provide an Action with Action Input or a Final Answer only.",
)

print("-"*50)
result = agent_executor.invoke(
    {"input": "What is the capital of Brazil?"}
)
print(result)
print("-"*50)

result = agent_executor.invoke(
    {"input": "What is the capital of Iran? And how much is 2 + 2?"}
)
print(result)
print("-"*50)

result = agent_executor.invoke(
    {"input": "What is the capital of Brazil? And how much is 3 + 3?"}
)
print(result)
print("-"*50)

result = agent_executor.invoke(
    {"input": "What is the capital of Italy and Spain? And how much is four plus four?"}
)
print(result)
print("-"*50)