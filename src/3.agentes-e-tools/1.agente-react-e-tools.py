from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
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


prompt = PromptTemplate.from_template(
    """
Answer the following questions as best you can. You have access to the following tools.
Only use the information you get from the tools, even if you know the answer.
If the information is not provided by the tools, say you don't know.

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Rules:
- If you choose an Action, do NOT include Final Answer in the same step.
- After Action and Action Input, stop and wait for Observation.
- Never search the internet. Only use the tools provided.

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
)

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