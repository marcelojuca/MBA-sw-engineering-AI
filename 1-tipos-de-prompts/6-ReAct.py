from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
You are a Go backend engineer helping debug a REST API. 
Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) 
and "Action:" (a concrete step or check you would perform). 
After each action, write "Observation:" to capture what you found. 
At the end, conclude with "Final Answer:" as your recommended fix.

Do not fabricate any information that is not provided in the context. 
Example: if the context does not provide errors logs, do not use error logs in your reasoning.

Context: A user reports that the endpoint `POST /products` always returns HTTP 500.  

Here is the handler code for `POST /products`:

```go
func CreateProduct(w http.ResponseWriter, r *http.Request) {
    var product Product
    err := json.NewDecoder(r.Body).Decode(&product)
    if err != nil {
        http.Error(w, "Bad Request", http.StatusBadRequest)
        return
    }

    stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
    if err != nil {
        log.Fatal(err)
    }

    _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
    if err != nil {
        log.Println("Error during Exec:", err)
        http.Error(w, "Internal Server Error", http.StatusInternalServerError)
        return
    }

    w.WriteHeader(http.StatusCreated)
}

type Product struct {
    ID          string  `json:"id"`
    Name        string  `json:"name"`
    Description string  `json:"description"`
    Price       string  `json:"price"` 
    Stock       int     `json:"stock"`
}
```
"""

msg2 = f"""
You are a travel planner helping a family choose the best way to go from Orlando to New York next month. 
Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and 
"Action:" (a step such as checking flight time, costs, or convenience). 
After each action, write "Observation:" with what you found. 
At the end, conclude with "Final Answer:" as your recommendation. 

Context:  
- The family has 2 adults and 2 children (ages 5 and 8).  
- Budget: max $1,000 for transport (not including hotel).  
- Dates: they must arrive on July 10 in the evening.  
- Options:  
  - **Flight**: $220 per person round trip, 3-hour flight, plus $80 total in baggage fees.  
  - **Train**: $150 per person round trip, 20-hour journey, with onboard WiFi and beds available for $50 extra per person.  
  - **Car rental**: $60/day, 2 days of driving each way (gas + tolls estimated $250 total). Kids get restless on long trips.  

Other details:  
- The kids’ school finishes on July 9 at noon.  
- Parents prefer not to arrive too tired, since they have a family wedding on July 11 in the morning.  

Start your reasoning now.
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)



# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/6-ReAct.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a Go backend engineer helping debug a REST API. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a concrete step or check you would perform). 
# After each action, write "Observation:" to capture what you found. 
# At the end, conclude with "Final Answer:" as your recommended fix.

# Do not fabricate any information that is not provided in the context. Example: if the context does not provide errors logs, do not use 
# error logs in your reasoning.

# Context: A user reports that the endpoint `POST /products` always returns HTTP 500.  

# Here is the handler code for `POST /products`:

# ```go
# func CreateProduct(w http.ResponseWriter, r *http.Request) {
#     var product Product
#     err := json.NewDecoder(r.Body).Decode(&product)
#     if err != nil {
#         http.Error(w, "Bad Request", http.StatusBadRequest)
#         return
#     }

#     stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
#     if err != nil {
#         log.Fatal(err)
#     }

#     _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
#     if err != nil {
#         log.Println("Error during Exec:", err)
#         http.Error(w, "Internal Server Error", http.StatusInternalServerError)
#         return
#     }

#     w.WriteHeader(http.StatusCreated)
# }

# type Product struct {
#     ID          string  `json:"id"`
#     Name        string  `json:"name"`
#     Description string  `json:"description"`
#     Price       string  `json:"price"` 
#     Stock       int     `json:"stock"`
# }
# ```


# LLM RESPONSE:
# Thought: The code seems to be handling potential errors during decoding of the JSON request body and SQL execution. Let's check if the 
# database connection is properly established.

# Action: Verify the `db` connection to ensure it is valid before preparing the statement.

# Observation: The database connection appears to be missing in the provided code snippet.

# Thought: The missing database connection could be the reason for the HTTP 500 error. We need to establish a connection to the database 
# before executing SQL statements.

# Action: Add code to establish a connection to the database before preparing the SQL statement.

# ```go
# var db *sql.DB

# func init() {
#     var err error
#     db, err = sql.Open("mysql", "user:password@tcp(127.0.0.1:3306)/dbname")
#     if err != nil {
#         log.Fatal(err)
#     }
#     err = db.Ping()
#     if err != nil {
#         log.Fatal(err)
#     }
# }
# ```

# Observation: The database connection is established during application initialization.

# Final Answer: The issue causing the HTTP 500 error when calling `POST /products` appears to be resolved by establishing a valid database 
# connection before executing SQL statements.

# Input tokens: 370
# Output tokens: 243
# Total tokens: 613
# -------------------------------------------------- 
# USER PROMPT:

# You are a travel planner helping a family choose the best way to go from Orlando to New York next month. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a step such as checking flight time, costs, or 
# convenience). 
# After each action, write "Observation:" with what you found. 
# At the end, conclude with "Final Answer:" as your recommendation. 

# Context:  
# - The family has 2 adults and 2 children (ages 5 and 8).  
# - Budget: max $1,000 for transport (not including hotel).  
# - Dates: they must arrive on July 10 in the evening.  
# - Options:  
#   - **Flight**: $220 per person round trip, 3-hour flight, plus $80 total in baggage fees.  
#   - **Train**: $150 per person round trip, 20-hour journey, with onboard WiFi and beds available for $50 extra per person.  
#   - **Car rental**: $60/day, 2 days of driving each way (gas + tolls estimated $250 total). Kids get restless on long trips.  

# Other details:  
# - The kids’ school finishes on July 9 at noon.  
# - Parents prefer not to arrive too tired, since they have a family wedding on July 11 in the morning.  

# Start your reasoning now.


# LLM RESPONSE:
# Thought: Considering the family's budget and the fact that they have young children, I need to find the option that is both cost-effective 
# and convenient.
# Action: Check the flight prices for 2 adults and 2 children from Orlando to New York on July 10.
# Observation: The total cost for flights for the family would be $880 ($220 x 4).
# Thought: The flight is within budget and it's the quickest option, but there are additional costs for baggage fees.
# Action: Check the train prices for 2 adults and 2 children from Orlando to New York on July 10.
# Observation: The total cost for train tickets for the family would be $600 ($150 x 4), without any additional charges.
# Thought: The train is cheaper but it takes much longer. Let's also consider the car rental option.
# Action: Check the car rental prices for 2 days of driving from Orlando to New York and back for the family.
# Observation: The total cost for car rental, gas, and tolls would be around $370 ($60 x 2 days + $250).
# Thought: The car rental option is cheaper than flying and could provide more flexibility, but it's a long drive and the kids might get 
# restless.
# Action: Consider the time constraints and the family's preference for not arriving too tired for the wedding on July 11.
# Observation: Driving for 2 days each way may not be the best option considering the family's schedule and the kids' restlessness.
# Final Answer: I recommend the family to take the train from Orlando to New York on July 10. It is within budget, and although it takes 
# longer than a flight, it offers onboard WiFi and the option to have beds for a more comfortable journey. This way, the family can arrive in
# New York in time for the wedding on July 11, without being too tired from a long drive.

# Input tokens: 293
# Output tokens: 385
# Total tokens: 678
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 

# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/6-ReAct.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a Go backend engineer helping debug a REST API. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a concrete step or check you would perform). 
# After each action, write "Observation:" to capture what you found. 
# At the end, conclude with "Final Answer:" as your recommended fix.

# Do not fabricate any information that is not provided in the context. Example: if the context does not provide errors logs, do not use 
# error logs in your reasoning.

# Context: A user reports that the endpoint `POST /products` always returns HTTP 500.  

# Here is the handler code for `POST /products`:

# ```go
# func CreateProduct(w http.ResponseWriter, r *http.Request) {
#     var product Product
#     err := json.NewDecoder(r.Body).Decode(&product)
#     if err != nil {
#         http.Error(w, "Bad Request", http.StatusBadRequest)
#         return
#     }

#     stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
#     if err != nil {
#         log.Fatal(err)
#     }

#     _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
#     if err != nil {
#         log.Println("Error during Exec:", err)
#         http.Error(w, "Internal Server Error", http.StatusInternalServerError)
#         return
#     }

#     w.WriteHeader(http.StatusCreated)
# }

# type Product struct {
#     ID          string  `json:"id"`
#     Name        string  `json:"name"`
#     Description string  `json:"description"`
#     Price       string  `json:"price"` 
#     Stock       int     `json:"stock"`
# }
# ```


# LLM RESPONSE:
# Thought: The `POST /products` handler is returning an HTTP 500 error which indicates an internal server error. There could be several 
# points of failure in this code. Since we do not have access to logs directly, we'll have to reason through potential issues.

# Action: Check the error handling for the SQL statement preparation. The use of `log.Fatal(err)` on the preparation failure may terminate 
# the application.

# Observation: The use of `log.Fatal(err)` results in the server crashing if the `Prepare` statement fails. This behavior is not causing HTTP
# 500 errors on its own but should be addressed as it can cause the server to stop running unexpectedly.

# Thought: The next potential failure point is the execution of the SQL statement in `stmt.Exec(product.ID, product.Name, 
# product.Description, product.Price, product.Stock)`. Incorrect data types or database constraints could cause this to fail.

# Action: Consider the data types and constraints for the database table 'products'. Investigate whether the `Price` field, which is a string
# in the `Product` struct, matches the database schema. It is common for prices to be stored as numeric types.

# Observation: There might be a type mismatch between the `Price` field which is a string in the code and a numeric field in the database. 
# This mismatch could certainly cause an error during the execution of the SQL insertion, leading to the HTTP 500 response.

# Thought: To fix this, the `Price` field should be converted to a numeric type before inserting it into the database. This can often be done
# using `strconv.ParseFloat` if the price should be a float.

# Final Answer: Change the type of the `Price` field in the `Product` struct from `string` to a numeric type (e.g., `float64`). Ensure any 
# data parsing or conversion needed for `Price` is done before executing the SQL statement, such as using `strconv.ParseFloat` to handle the 
# conversion from string to float. Also, replace `log.Fatal(err)` with proper error handling that sends an appropriate response without 
# crashing the server.

# Input tokens: 374
# Output tokens: 417
# Total tokens: 791
# -------------------------------------------------- 
# USER PROMPT:

# You are a travel planner helping a family choose the best way to go from Orlando to New York next month. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a step such as checking flight time, costs, or 
# convenience). 
# After each action, write "Observation:" with what you found. 
# At the end, conclude with "Final Answer:" as your recommendation. 

# Context:  
# - The family has 2 adults and 2 children (ages 5 and 8).  
# - Budget: max $1,000 for transport (not including hotel).  
# - Dates: they must arrive on July 10 in the evening.  
# - Options:  
#   - **Flight**: $220 per person round trip, 3-hour flight, plus $80 total in baggage fees.  
#   - **Train**: $150 per person round trip, 20-hour journey, with onboard WiFi and beds available for $50 extra per person.  
#   - **Car rental**: $60/day, 2 days of driving each way (gas + tolls estimated $250 total). Kids get restless on long trips.  

# Other details:  
# - The kids’ school finishes on July 9 at noon.  
# - Parents prefer not to arrive too tired, since they have a family wedding on July 11 in the morning.  

# Start your reasoning now.


# LLM RESPONSE:
# Thought: Let's evaluate each travel option based on cost, convenience, and the need to arrive in New York on July 10 in the evening. The 
# parents prefer not to arrive too tired due to a family wedding the next morning.

# Action: Check the total cost and travel duration for the flight option.

# Observation: The flight costs $220 per person, which equals $880 for four people. Adding $80 for baggage, the total cost is $960. The 
# flight duration is about 3 hours, which is the fastest option and allows the family to arrive rested.

# Thought: The flight is within budget and time-efficient, allowing the family to arrive in the evening, rested for the wedding.

# Action: Check the total cost and travel duration for the train option.

# Observation: The train costs $150 per person, totaling $600. Adding $50 per person for beds comes to $800. The journey is 20 hours long, 
# potentially exhausting for both kids and parents.

# Thought: While the train is budget-friendly, the long journey might leave the family exhausted, especially considering the kids' 
# restlessness.

# Action: Check the total cost and travel duration for the car rental option.

# Observation: The car rental costs $60 per day for 4 days, totaling $240. Adding gas and tolls, estimated at $250, brings it to $490. The 
# driving time is approximately 18-20 hours each way, requiring 2 days of travel.

# Thought: The car rental is the cheapest option, but the long drive over multiple days can be tiring, increasing the chance of fatigue 
# before the wedding.

# Final Answer: I recommend the **flight** option. It's within budget at $960 and allows the family to arrive in New York on July 10 in the 
# evening efficiently and rested, ensuring they are well-prepared for the wedding the following morning.

# Input tokens: 296
# Output tokens: 371
# Total tokens: 667
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 

# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/6-ReAct.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a Go backend engineer helping debug a REST API. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a concrete step or check you would perform). 
# After each action, write "Observation:" to capture what you found. 
# At the end, conclude with "Final Answer:" as your recommended fix.

# Do not fabricate any information that is not provided in the context. Example: if the context does not provide errors logs, do not use 
# error logs in your reasoning.

# Context: A user reports that the endpoint `POST /products` always returns HTTP 500.  

# Here is the handler code for `POST /products`:

# ```go
# func CreateProduct(w http.ResponseWriter, r *http.Request) {
#     var product Product
#     err := json.NewDecoder(r.Body).Decode(&product)
#     if err != nil {
#         http.Error(w, "Bad Request", http.StatusBadRequest)
#         return
#     }

#     stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
#     if err != nil {
#         log.Fatal(err)
#     }

#     _, err = stmt.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
#     if err != nil {
#         log.Println("Error during Exec:", err)
#         http.Error(w, "Internal Server Error", http.StatusInternalServerError)
#         return
#     }

#     w.WriteHeader(http.StatusCreated)
# }

# type Product struct {
#     ID          string  `json:"id"`
#     Name        string  `json:"name"`
#     Description string  `json:"description"`
#     Price       string  `json:"price"` 
#     Stock       int     `json:"stock"`
# }
# ```


# LLM RESPONSE:
# Thought: The code path that could produce a 500 is the Exec error path, but there is a more dangerous issue: on Prepare failure it calls 
# log.Fatal, which would terminate the whole server. If Prepare ever fails (db not initialized, wrong driver, or SQL syntax), the process 
# crashes and clients see 500s (or the server restarts and returns 500 during downtime).

# Action: Inspect the Prepare error handling and the SQL placeholders. Check what database driver is in use (MySQL/SQLite use ?, PostgreSQL 
# uses $1, $2, ...). Also verify the server process isn’t dying due to log.Fatal.

# Observation: The handler uses:
# - http.Error for JSON decode errors (400), and for Exec errors it returns 500 (OK).
# - But on Prepare it calls log.Fatal(err). This could crash the server on any Prepare error, explaining widespread 500s.
# - The SQL uses ? placeholders, which is correct for MySQL/SQLite but not for PostgreSQL. If the project uses PostgreSQL, Prepare would fail
# with a syntax error, again triggering log.Fatal and 500s.
# - Price is defined as string in the Product struct. If the database column is numeric (e.g., DECIMAL/NUMERIC) this type mismatch could 
# cause Exec to fail, producing 500.

# Action: Propose concrete fixes to address these likely root causes.

# Observation: To prevent server crashes and harden error handling, do not use log.Fatal in a request handler. Instead, return a 500 with a 
# safe message and log the error. Also ensure the placeholder style matches the database driver you actually use. If you’re on PostgreSQL, 
# switch to $1, $2, $3, $4, $5 (or use db.Exec with the correct placeholders) and properly close any prepared statements.

# Action: Recommend correcting type mismatches by aligning Go types with DB types. If price is numeric in the DB, use a numeric type in Go 
# (float64 or sql.NullFloat64) instead of string; also validate input.

# Observation: After applying these changes, 500s should reduce to either 400 (bad JSON) or 500 for genuine DB errors, and crashes from 
# Prepare should disappear.

# Final Answer: Suggested fix plan

# - Remove fatal on Prepare:
#   - Replace:
#     stmt, err := db.Prepare(...)
#     if err != nil { log.Fatal(err) }
#   - With:
#     stmt, err := db.Prepare(...)
#     if err != nil {
#       log.Println("Prepare error:", err)
#       http.Error(w, "Internal Server Error", http.StatusInternalServerError)
#       return
#     }
#     defer stmt.Close()

# - Ensure placeholder syntax matches your DB driver:
#   - If you use MySQL/SQLite: keep "VALUES (?, ?, ?, ?, ?)".
#   - If you use PostgreSQL: switch to "VALUES ($1, $2, $3, $4, $5)" and pass the same arguments.

# - Align Product struct with DB types:
#   - Change Price from string to a numeric type, e.g.:
#     Price float64 `json:"price"`
#   - Leave Stock as int (ok if DB stock is integral).
#   - Update any JSON input to provide price as a number, not a string.

# - Add basic input validation (optional but recommended):
#   - Ensure non-empty ID, Name; price >= 0; stock >= 0.

# - Close resources and keep error logs informative:
#   - Use defer stmt.Close() after a successful Prepare.
#   - Log errors with context, e.g., log.Printf("Insert product failed: %v", err).

# - Optional improvement: avoid Prepare for simple inserts and use db.Exec with the same placeholder syntax to reduce boilerplate, ensuring 
# you use the correct placeholder style for your driver.

# If you confirm and apply these changes, the endpoint should stop returning random 500s caused by crashes from Prepare and by driver 
# placeholder mismatches, and should properly handle invalid input vs. server-side DB errors.

# Input tokens: 373
# Output tokens: 4471
# Total tokens: 4844
# -------------------------------------------------- 
# USER PROMPT:

# You are a travel planner helping a family choose the best way to go from Orlando to New York next month. 
# Use the ReAct style reasoning: alternate between "Thought:" (your reasoning) and "Action:" (a step such as checking flight time, costs, or 
# convenience). 
# After each action, write "Observation:" with what you found. 
# At the end, conclude with "Final Answer:" as your recommendation. 

# Context:  
# - The family has 2 adults and 2 children (ages 5 and 8).  
# - Budget: max $1,000 for transport (not including hotel).  
# - Dates: they must arrive on July 10 in the evening.  
# - Options:  
#   - **Flight**: $220 per person round trip, 3-hour flight, plus $80 total in baggage fees.  
#   - **Train**: $150 per person round trip, 20-hour journey, with onboard WiFi and beds available for $50 extra per person.  
#   - **Car rental**: $60/day, 2 days of driving each way (gas + tolls estimated $250 total). Kids get restless on long trips.  

# Other details:  
# - The kids’ school finishes on July 9 at noon.  
# - Parents prefer not to arrive too tired, since they have a family wedding on July 11 in the morning.  

# Start your reasoning now.


# LLM RESPONSE:
# Note: I can’t share my internal chain-of-thought, but here is a concise, structured analysis with clear actions, observations, and a final 
# recommendation.

# Action: Assess which option can meet the arrival requirement of July 10 in the evening.
# Observation: 
# - Flight: direct 3-hour flight. With same-time-zone travel (Orlando to NYC), you can’t guarantee arrival exactly on July 10 evening via a 
# direct 3-hour flight; you’d typically land July 9 evening or July 10 morning at the latest. So flights cannot reliably guarantee July 10 
# evening arrival.
# - Train: 20-hour journey. If you depart July 9 evening, you can arrive July 10 evening (roughly 9 PM + 20 hours ≈ 5 PM–9 PM July 10 
# depending on schedule), which fits the requirement.
# - Car: 2 days driving each way (4 days total). That would push arrival well after July 10, likely around July 13–14, not July 10 evening.

# Action: Calculate total costs for four travelers (2 adults, 2 kids) and any extras.
# Observation:
# - Flight: $220/person round trip → 4 × $220 = $880. Baggage fees total $80. Total ≈ $960. Duration: ~3 hours flight (plus airport time). 
# Does not meet the evening-arrival constraint.
# - Train: $150/person round trip → 4 × $150 = $600. Beds option $50/person → 4 × $50 = $200. Total ≈ $800. Duration: ~20 hours. Beds/wifi 
# help with kids. Fully within budget.
# - Car: $60/day. 2 days driving each way → 4 days × $60 = $240. Gas + tolls ≈ $250. Total ≈ $490. But arrival would be around July 13–14, 
# far after the wedding and the July 10 evening target.

# Action: Consider practicality for the kids and wedding date.
# Observation:
# - Flight is short but would likely be a long day with airports; kids may still be tired, and arrival by July 10 evening is not guaranteed.
# - Train offers beds and WiFi, reducing fatigue for the kids and adults and aligning with the July 10 evening target when departing July 9 
# evening.
# - Car involves a long multi-day road trip, increasing fatigue risk and failing the arrival target.

# Final Recommendation:
# - Take the train. Book a round-trip Orlando to New York on July 9 evening with the “beds” option ($50 per person) to ensure rest for the 
# kids and parents. Estimated total cost ≈ $800 (train fare $600 + beds $200). Arrival in New York around the evening of July 10, leaving you
# rested for the family wedding on July 11 morning. This option best balances the required arrival timing, comfort for a family with young 
# children, and staying well within the $1,000 transport budget.

# Final Answer:
# Recommend the train with beds for the four travelers, departing Orlando July 9 evening and arriving in New York July 10 evening. Total 
# expected cost ≈ $800. This avoids fatigue before the July 11 wedding, keeps you under budget, and satisfies the July 10 evening arrival 
# constraint.

# Input tokens: 295
# Output tokens: 5673
# Total tokens: 5968
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 