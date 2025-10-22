from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts = db.FindPostsByUserID(u.ID)
}

How many database queries will this code execute if there are N users?

Generate 3 different reasoning paths step by step.
At the end, summarize the answers and choose the most consistent one, ignoring outliers.
If there are 3 different answers, ONLY reply: "I can't find a consistent answer".
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
print_llm_result(msg1, response1)


# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3.1-CoT-Self-consistency.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

# users := db.FindAllUsers()
# for _, u := range users {
#     u.Posts = db.FindPostsByUserID(u.ID)
# }

# How many database queries will this code execute if there are N users?

# Generate 3 different reasoning paths step by step.
# At the end, summarize the answers and choose the most consistent one, ignoring outliers.
# If there are 3 different answers, ONLY reply: "I can't find a consistent answer".


# LLM RESPONSE:
# Reasoning Path 1:
# 1. For each user, the code calls db.FindPostsByUserID(u.ID) to find the posts for that user.
# 2. If there are N users, this means the code will execute N database queries to find posts for each user.
# 3. Therefore, the total number of database queries executed will be N.

# Reasoning Path 2:
# 1. The code starts by fetching all users using db.FindAllUsers().
# 2. For each user, the code then fetches their posts using db.FindPostsByUserID(u.ID).
# 3. If there are N users, then the call to db.FindAllUsers() will be one query, and the subsequent call db.FindPostsByUserID(u.ID) will be N 
# queries.
# 4. Therefore, the total number of database queries executed will be N+1.

# Reasoning Path 3:
# 1. The code iterates through all users retrieved from db.FindAllUsers().
# 2. Within each iteration, it calls db.FindPostsByUserID(u.ID) to find posts for that user.
# 3. For N users, this means N queries will be executed inside the loop.
# 4. Therefore, the total number of database queries executed will be N.

# Summary:
# - The three reasoning paths provided resulted in different answers: N, N+1, and N.
# - However, the most consistent answer based on the majority of the reasoning paths is that the code will execute N database queries.
# - Therefore, the most consistent answer is that the code will execute N database queries.

# Input tokens: 117
# Output tokens: 310
# Total tokens: 427
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/githu
# b/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e
# -tipos-de-prompt/1-tipos-de-prompts/3.1-CoT-Self-consistency.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3.1-CoT-Self-consistency.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

# users := db.FindAllUsers()
# for _, u := range users {
#     u.Posts = db.FindPostsByUserID(u.ID)
# }

# How many database queries will this code execute if there are N users?

# Generate 3 different reasoning paths step by step.
# At the end, summarize the answers and choose the most consistent one, ignoring outliers.
# If there are 3 different answers, ONLY reply: "I can't find a consistent answer".


# LLM RESPONSE:
# Reasoning Path 1:
# 1. The code begins by executing `db.FindAllUsers()`, which retrieves all the users from the database. This is one database query.
# 2. Next, the code iterates over each user retrieved. For each user, it executes `db.FindPostsByUserID(u.ID)` to get that user's posts.
# 3. Since there are N users, `db.FindPostsByUserID(u.ID)` will be called N times, executing one query for each user.
# 4. Therefore, there will be a total of 1 (for fetching users) + N (one for each user's posts) = N + 1 database queries.

# Reasoning Path 2:
# 1. Initially, the call to `db.FindAllUsers()` fetches all users. This is one database operation.
# 2. For every user in the list (total N users), the code executes `db.FindPostsByUserID(u.ID)` to get the posts for the user.
# 3. This results in one query per user as the function `db.FindPostsByUserID(u.ID)` runs once for each user.
# 4. As a result, there will be 1 (for finding all users) + N (one per user for their posts) = N + 1 total queries.

# Reasoning Path 3:
# 1. The code executes `db.FindAllUsers()`, which queries the database once to retrieve all user records.
# 2. After fetching the users, the iteration over the list results in one database query per user to get their respective posts—using 
# `db.FindPostsByUserID(u.ID)`, which runs N times.
# 3. Total queries executed would be 1 (to get users) + N (one per user to fetch their posts), summing to N + 1 queries.

# Summary:
# All three reasoning paths conclude that the code executes a total of N + 1 database queries: one query to retrieve all users and N queries to 
# retrieve the posts for each user. The most consistent and repeated answer is N + 1 queries.

# Input tokens: 118
# Output tokens: 418
# Total tokens: 536
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3.1-CoT-Self-consistency.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

# users := db.FindAllUsers()
# for _, u := range users {
#     u.Posts = db.FindPostsByUserID(u.ID)
# }

# How many database queries will this code execute if there are N users?

# Generate 3 different reasoning paths step by step.
# At the end, summarize the answers and choose the most consistent one, ignoring outliers.
# If there are 3 different answers, ONLY reply: "I can't find a consistent answer".


# LLM RESPONSE:
# ### Reasoning Path 1:

# 1. **Initialize Users:** The code begins by calling `db.FindAllUsers()`, which queries the database to retrieve all users. This counts as 1 
# query.
   
# 2. **Iterate Over Users:** A loop iterates over each user in the `users` list.

# 3. **Query for Posts:** For each user `u`, the code executes `db.FindPostsByUserID(u.ID)`. This makes a separate query for each individual user 
# to retrieve their posts.

# 4. **Total Queries:** With `N` users, the loop runs `N` times, executing 1 query per user. Therefore, the number of queries to get posts is `N`.

# 5. **Total Count:** Adding the 1 query to get all users, the total number of queries executed is `1 + N`.

# **Answer:** 1 + N queries

# ### Reasoning Path 2:

# 1. **Initialize Users:** `db.FindAllUsers()` is called, which performs 1 query to retrieve all users from the database.

# 2. **Iterate and Fetch Posts:** As the loop executes for each user, `db.FindPostsByUserID(u.ID)` makes an individual query for each user to fetch
# their posts.

# 3. **Independent Queries for Posts:** With `N` users, there will be `N` separate calls to `FindPostsByUserID`.

# 4. **Total Queries:** The total number of queries is the sum of the initial users query and the individual post queries for each user.

# 5. **Final Count:** This results in `1 (for users) + N (for each user's posts)` queries.

# **Answer:** 1 + N queries

# ### Reasoning Path 3:

# 1. **Query Users:** Initially, `db.FindAllUsers()` executes a single database query.

# 2. **Loop Through Users:** Each iteration over users results in a separate database query via `db.FindPostsByUserID(u.ID)` to get the posts for 
# that user.

# 3. **Counting Total Queries:** Since there are N users, there will be N queries executed for user posts.

# 4. **Summarizing the Total:** The database is queried once for users and N times for posts.

# 5. **Complete Total:** The total executed queries amount to `1 (users) + N (post queries)`.

# **Answer:** 1 + N queries

# ### Summary:

# All three reasoning paths consistently lead to the conclusion that the code executes `1 + N` database queries, where 1 query retrieves all users 
# and N queries fetch posts for each user individually.

# The most consistent answer among the reasoning paths is:

# **Answer:** 1 + N queries

# Input tokens: 118
# Output tokens: 548
# Total tokens: 666
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/3.1-CoT-Self-consistency.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# Question: In an API endpoint that returns a list of users and their posts, the developer wrote:

# users := db.FindAllUsers()
# for _, u := range users {
#     u.Posts = db.FindPostsByUserID(u.ID)
# }

# How many database queries will this code execute if there are N users?

# Generate 3 different reasoning paths step by step.
# At the end, summarize the answers and choose the most consistent one, ignoring outliers.
# If there are 3 different answers, ONLY reply: "I can't find a consistent answer".


# LLM RESPONSE:
# Reasoning Path A
# 1) The code calls FindAllUsers() once. This executes one database query to fetch all users.
# 2) It then iterates over N users. For each user, it calls FindPostsByUserID(u.ID), which executes one separate query.
# 3) Therefore, total queries = 1 (for users) + N (for posts) = N + 1.

# Reasoning Path B
# 1) The operation starts with a single query to retrieve the list of users.
# 2) For each of the N users, there is an additional query to retrieve that user’s posts.
# 3) Sum: 1 + N = N + 1 queries.

# Reasoning Path C
# 1) Consider round-trips: one round-trip for all users, plus one round-trip per user for posts.
# 2) This yields 1 + N round-trips.
# 3) Hence, the total number of queries is N + 1.

# Summary of answers
# - All three reasoning paths conclude that the code performs N + 1 database queries: 1 to get all users, plus N per-user post queries.

# Final answer
# N + 1 queries.

# Input tokens: 117
# Output tokens: 2038
# Total tokens: 2155
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 
