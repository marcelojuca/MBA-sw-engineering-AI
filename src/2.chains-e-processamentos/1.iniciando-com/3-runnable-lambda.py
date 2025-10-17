from langchain_core.runnables import RunnableLambda


def parse_number(text: str) -> int:
    return int(text.strip())

print("-"*50)
parse_runnable = RunnableLambda(parse_number)
result = parse_runnable.invoke("10")
print(result)
print("-"*50)
