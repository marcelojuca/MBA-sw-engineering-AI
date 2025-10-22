from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Classify the log severity.

Input: "Disk usage at 85%."
Answer only with INFO, WARNING, or ERROR.
"""

msg2 = """
Classify the log severity.

Input: "Disk usage at 85%."
Think step by step about why this is INFO, WARNING, or ERROR. 
At the end, give only the final answer after "Answer:".
"""


msg3 = """
Question: How many "r" are in the word "strawberry"?
Answer only with the number of "r".
"""

msg4 = """
Question: How many "r" are in the word "strawberry"?
Explain step by step by breaking down each letter in bullet points, pointing out the "r" before giving the final answer. 
Give the final result after "Answer:".
"""

llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)

###################
# Results llm = ChatOpenAI(model="gpt-3.5-turbo")
###################

# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3-CoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Answer only with INFO, WARNING, or ERROR.


# LLM RESPONSE:
# INFO

# Input tokens: 34
# Output tokens: 1
# Total tokens: 35
# -------------------------------------------------- 
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Think step by step about why this is INFO, WARNING, or ERROR. 
# At the end, give only the final answer after "Answer:".


# LLM RESPONSE:
# - The message states a statistic about the disk usage, specifically that it is at 85%. This is informational and does not indicate any immediate 
# issues or errors.
# - While a high disk usage percentage could potentially lead to performance issues in the future, the current state of 85% does not necessarily 
# warrant immediate action.
# - Therefore, this log severity can be classified as INFO.

# Answer: INFO

# Input tokens: 54
# Output tokens: 78
# Total tokens: 132
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Answer only with the number of "r".


# LLM RESPONSE:
# 2

# Input tokens: 34
# Output tokens: 1
# Total tokens: 35
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Explain step by step by breaking down each letter in bullet points, pointing out the "r" before giving the final answer. 
# Give the final result after "Answer:".


# LLM RESPONSE:
# - s
# - t
# - r (first "r" found)
# - a
# - w
# - b
# - e
# - r (second "r" found)
# - r (third and final "r" found)
# - y

# Answer: There are 3 "r" in the word "strawberry".

# Input tokens: 61
# Output tokens: 67
# Total tokens: 128
# -------------------------------------------------- 


###################
# Results llm = ChatOpenAI(model="gpt-4o")
###################

# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3-CoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Answer only with INFO, WARNING, or ERROR.


# LLM RESPONSE:
# WARNING

# Input tokens: 34
# Output tokens: 1
# Total tokens: 35
# -------------------------------------------------- 
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Think step by step about why this is INFO, WARNING, or ERROR. 
# At the end, give only the final answer after "Answer:".


# LLM RESPONSE:
# To determine the severity of the log "Disk usage at 85%", we need to consider the typical thresholds and implications associated with disk usage 
# levels:

# 1. **INFO**: Logs categorized as INFO typically provide general information about system operations and status messages that do not require any 
# immediate attention. For instance, disk usage below 70% might be considered an informational message as it indicates normal operations.

# 2. **WARNING**: This level is used for messages that indicate a potential issue or threshold that could escalate into a problem if not addressed.
# Disk usage at 85% fits into this category because it is approaching full capacity. While not immediately critical, it suggests that the disk 
# could soon run out of space, and proactive measures should be taken to prevent this, such as cleaning up unnecessary files or adding more 
# storage.

# 3. **ERROR**: This level is used when a significant problem has occurred, which requires immediate attention. If disk usage were at 95% or 
# higher, it might be categorized as ERROR due to the imminent risk of running out of space and potentially affecting system operations.

# Given that 85% disk usage suggests a potentially problematic situation but does not yet indicate an immediate failure, it fits best under the 
# WARNING category, as it necessitates attention to prevent possible future issues.

# Answer: WARNING

# Input tokens: 54
# Output tokens: 260
# Total tokens: 314
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Answer only with the number of "r".


# LLM RESPONSE:
# 2

# Input tokens: 34
# Output tokens: 1
# Total tokens: 35
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Explain step by step by breaking down each letter in bullet points, pointing out the "r" before giving the final answer. 
# Give the final result after "Answer:".


# LLM RESPONSE:
# To determine how many "r" letters are in the word "strawberry," let's break down the word letter by letter:

# - **s**: This is the first letter. It is not an "r."
# - **t**: This is the second letter. It is not an "r."
# - **r**: This is the third letter. It is an "r." (1st "r")
# - **a**: This is the fourth letter. It is not an "r."
# - **w**: This is the fifth letter. It is not an "r."
# - **b**: This is the sixth letter. It is not an "r."
# - **e**: This is the seventh letter. It is not an "r."
# - **r**: This is the eighth letter. It is an "r." (2nd "r")
# - **r**: This is the ninth letter. It is an "r." (3rd "r")
# - **y**: This is the tenth letter. It is not an "r."

# Count of "r": There are three "r" letters in the word "strawberry."

# Answer: 3

# Input tokens: 60
# Output tokens: 245
# Total tokens: 305
# -------------------------------------------------- 

###################
# Results llm = ChatOpenAI(model="gpt-5-nano")
###################

# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3-CoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Answer only with INFO, WARNING, or ERROR.


# LLM RESPONSE:
# WARNING

# Input tokens: 33
# Output tokens: 138
# Total tokens: 171
# -------------------------------------------------- 
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Think step by step about why this is INFO, WARNING, or ERROR. 
# At the end, give only the final answer after "Answer:".


# LLM RESPONSE:
# Answer: WARNING

# Input tokens: 53
# Output tokens: 460
# Total tokens: 513
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Answer only with the number of "r".


# LLM RESPONSE:
# 3

# Input tokens: 33
# Output tokens: 202
# Total tokens: 235
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Explain step by step by breaking down each letter in bullet points, pointing out the "r" before giving the final answer. 
# Give the final result after "Answer:".


# LLM RESPONSE:
# - s
# - t
# - r (this is an r)
# - a
# - w
# - b
# - e
# - r (this is an r)
# - r (this is an r)
# - y
# Answer: 3

# Input tokens: 59
# Output tokens: 1082
# Total tokens: 1141
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗      
# - **t**: This is the second letter. It is not an "r."
# - **r**: This is the third letter. It is an "r." (1st "r")
# - **a**: This is the fourth letter. It is not an "r."
# - **w**: This is the fifth letter. It is not an "r."
# - **b**: This is the sixth letter. It is not an "r."
# - **e**: This is the seventh letter. It is not an "r."
# - **r**: This is the eighth letter. It is an "r." (2nd "r")
# - **r**: This is the ninth letter. It is an "r." (3rd "r")
# - **y**: This is the tenth letter. It is not an "r."

# Count of "r": There are three "r" letters in the word "strawberry."

# Answer: 3

# Input tokens: 60
# Output tokens: 245
# Total tokens: 305
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3-CoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Answer only with INFO, WARNING, or ERROR.


# LLM RESPONSE:
# WARNING

# Input tokens: 33
# Output tokens: 138
# Total tokens: 171
# -------------------------------------------------- 
# USER PROMPT:

# Classify the log severity.

# Input: "Disk usage at 85%."
# Think step by step about why this is INFO, WARNING, or ERROR. 
# At the end, give only the final answer after "Answer:".


# LLM RESPONSE:
# Answer: WARNING

# Input tokens: 53
# Output tokens: 460
# Total tokens: 513
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Answer only with the number of "r".


# LLM RESPONSE:
# 3

# Input tokens: 33
# Output tokens: 202
# Total tokens: 235
# -------------------------------------------------- 
# USER PROMPT:

# Question: How many "r" are in the word "strawberry"?
# Explain step by step by breaking down each letter in bullet points, pointing out the "r" before giving the final answer. 
# Give the final result after "Answer:".


# LLM RESPONSE:
# - s
# - t
# - r (this is an r)
# - a
# - w
# - b
# - e
# - r (this is an r)
# - r (this is an r)
# - y
# Answer: 3

# Input tokens: 59
# Output tokens: 1082
# Total tokens: 1141
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗      