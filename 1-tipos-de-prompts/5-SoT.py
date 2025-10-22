from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
You are a senior backend engineer. A junior developer asked you how to optimize SQL queries for better performance. 
Follow the Skeleton of Thought approach: 

Step 1: Generate only the skeleton of your answer in 3–5 concise bullet points. 
Step 2: Expand each bullet point into a clear and detailed explanation with examples. 
Make sure the final answer is structured and easy to follow.
"""

msg2 = f"""
You are a software architect. I want you to produce an Architecture Decision Record (ADR) about choosing PostgreSQL instead of MongoDB. 

Follow the Skeleton of Thought approach:
Step 1: First, output only the skeleton of the ADR as section headers (no explanations yet). 
Use the standard ADR structure with 5 sections: Context, Decision, Alternatives Considered, Consequences, References. 
Step 2: After showing the skeleton, expand each section with clear and detailed content. 
Keep the final ADR professional, structured, and easy to read.
"""

msg3 = f"""
You are a senior Go developer. I want you to help me plan a REST API for managing products in Go.

Follow the Skeleton of Thought approach:

Step 1: Output only the skeleton of the solution in 6–8 concise bullet points. 
The skeleton must cover: data model definition in Go (structs), choice of HTTP framework or net/http, routing, 
handlers, validations, database layer, error handling, and project structure. Do not expand yet.

Step 2: Expand each bullet point with clear technical details, examples, and Go best practices. 
Include sample code snippets in Go (structs, handlers, routes) and considerations about packages 
(e.g., chi, or net/http), error handling with idiomatic Go, and how to organize the project into packages (handlers, models, db). 
Use concise and professional language.

The API must implement CRUD operations for products with fields: id, name, description, price, stock.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)


# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/5-SoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a senior backend engineer. A junior developer asked you how to optimize SQL queries for better performance. 
# Follow the Skeleton of Thought approach: 

# Step 1: Generate only the skeleton of your answer in 3–5 concise bullet points. 
# Step 2: Expand each bullet point into a clear and detailed explanation with examples. 
# Make sure the final answer is structured and easy to follow.


# LLM RESPONSE:
# Step 1:
# 1. Indexing: Ensure proper indexing on columns used in JOIN and WHERE clauses.
# 2. Avoid using SELECT *: Only fetch the columns you need instead of all columns using SELECT *.
# 3. Use EXPLAIN statement: Analyze query execution plans to identify bottlenecks.
# 4. Consider using database-specific optimizations: Utilize features like stored procedures and query caching.
# 5. Limit the use of subqueries and optimize them when necessary.

# Step 2:

# 1. Indexing: Indexing involves creating data structures to improve the speed of data retrieval operations on database tables. By creating 
# indexes on columns frequently used in JOIN and WHERE clauses, you can significantly speed up query execution. For example, let's say you 
# have a table "users" with columns "id" and "email", and you frequently search users by email. Creating an index on the "email" column would
# speed up such queries.

# 2. Avoid using SELECT *: When fetching data from a database, only retrieve the columns you actually need in the result set instead of using
# SELECT * to fetch all columns. Retrieving unnecessary columns can lead to increased memory usage and slower query execution. For example, 
# instead of SELECT * FROM users, prefer selecting specific columns like SELECT id, name FROM users.

# 3. Use EXPLAIN statement: The EXPLAIN statement in SQL can provide insights into how a query will be executed by the database engine and 
# helps in identifying any performance bottlenecks. It shows the query execution plan, including details such as the order in which tables 
# are accessed and the type of join operations used. By analyzing the EXPLAIN output, you can optimize queries by adding appropriate indexes,
# rewriting query logic, or restructuring the query.

# 4. Consider using database-specific optimizations: Different database systems have their own optimization techniques that can improve query
# performance. For example, stored procedures in MySQL can reduce network overhead by executing multiple SQL statements within a single call 
# to the database. Query caching is another efficient way to improve performance by storing the results of frequent queries in memory for 
# faster retrieval.

# 5. Limit the use of subqueries and optimize them when necessary: Subqueries can impact performance, especially when they are nested or 
# executed repeatedly. Whenever possible, try to rewrite subqueries as JOIN operations for better performance. If using subqueries is 
# necessary, ensure they are optimized by limiting the number of rows returned and properly indexing the tables involved. Additionally, 
# consider breaking down complex subqueries into multiple simpler queries to improve readability and maintainability.

# Input tokens: 89
# Output tokens: 501
# Total tokens: 590
# -------------------------------------------------- 
# USER PROMPT:

# You are a software architect. I want you to produce an Architecture Decision Record (ADR) about choosing PostgreSQL instead of MongoDB. 

# Follow the Skeleton of Thought approach:
# Step 1: First, output only the skeleton of the ADR as section headers (no explanations yet). 
# Use the standard ADR structure with 5 sections: Context, Decision, Alternatives Considered, Consequences, References. 
# Step 2: After showing the skeleton, expand each section with clear and detailed content. 
# Keep the final ADR professional, structured, and easy to read.


# LLM RESPONSE:
# ### Context
# ### Decision
# ### Alternatives Considered
# ### Consequences
# ### References

# ---

# ### Context
# Describe the context or the decision that needs to be made. Include any relevant background information.

# ### Decision
# State the decision to choose PostgreSQL instead of MongoDB. Explain the rationale behind this decision.

# ### Alternatives Considered
# Outline any alternatives that were considered in this decision-making process. Explain why they were not chosen.

# ### Consequences
# Discuss the potential consequences of choosing PostgreSQL over MongoDB. Include any risks or trade-offs that were identified.

# ### References
# List any external sources or internal documentation that was consulted during the decision-making process.

# Input tokens: 123
# Output tokens: 129
# Total tokens: 252
# -------------------------------------------------- 
# USER PROMPT:

# You are a senior Go developer. I want you to help me plan a REST API for managing products in Go.

# Follow the Skeleton of Thought approach:

# Step 1: Output only the skeleton of the solution in 6–8 concise bullet points. 
# The skeleton must cover: data model definition in Go (structs), choice of HTTP framework or net/http, routing, 
# handlers, validations, database layer, error handling, and project structure. Do not expand yet.

# Step 2: Expand each bullet point with clear technical details, examples, and Go best practices. 
# Include sample code snippets in Go (structs, handlers, routes) and considerations about packages 
# (e.g., chi, or net/http), error handling with idiomatic Go, and how to organize the project into packages (handlers, models, db). 
# Use concise and professional language.

# The API must implement CRUD operations for products with fields: id, name, description, price, stock.


# LLM RESPONSE:
# Step 1:
# - Define structs for products
# - Use the Chi HTTP framework
# - Define routing for CRUD operations
# - Create handlers for each CRUD operation
# - Implement validations for input data
# - Add a database layer for data persistence
# - Handle errors gracefully
# - Organize the project into packages

# Step 2:
# - Define a struct for products:
# ```go
# type Product struct {
#     ID          int
#     Name        string
#     Description string
#     Price       float64
#     Stock       int
# }
# ```

# - Use the Chi HTTP framework for routing:
# ```go
# r := chi.NewRouter()
# ```

# - Create handlers for CRUD operations:
# ```go
# func CreateProduct(w http.ResponseWriter, r *http.Request) {
#     // Parse request body and create a new product
# }

# func GetProduct(w http.ResponseWriter, r *http.Request) {
#     // Get a product by ID
# }

# func UpdateProduct(w http.ResponseWriter, r *http.Request) {
#     // Update a product by ID
# }

# func DeleteProduct(w http.ResponseWriter, r *http.Request) {
#     // Delete a product by ID
# }
# ```

# - Implement validations using a package like "github.com/go-playground/validator/v10":
# ```go
# validate := validator.New()
# err := validate.Struct(product)
# ```

# - Add a database layer using a package like "database/sql":
# ```go
# db, err := sql.Open("postgres", "user=postgres dbname=products sslmode=disable")
# defer db.Close()
# ```

# - Handle errors gracefully throughout the application:
# ```go
# if err != nil {
#     http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
#     return
# }
# ```

# - Organize the project into packages like "handlers," "models," and "db":
# ```
# /cmd
#   main.go
# /handlers
#   product_handler.go
# /models
#   product.go
# /db
#   db.go
# ```

# Input tokens: 202
# Output tokens: 391
# Total tokens: 593
# -------------------------------------------------- 



# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/5-SoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a senior backend engineer. A junior developer asked you how to optimize SQL queries for better performance. 
# Follow the Skeleton of Thought approach: 

# Step 1: Generate only the skeleton of your answer in 3–5 concise bullet points. 
# Step 2: Expand each bullet point into a clear and detailed explanation with examples. 
# Make sure the final answer is structured and easy to follow.


# LLM RESPONSE:
# ### Step 1: Skeleton of the Answer

# 1. **Indexing**
# 2. **Query Optimization**
# 3. **Avoiding Select ** 
# 4. **Limiting Result Sets**
# 5. **Use Appropriate Data Types**

# ### Step 2: Expanded Explanation

# 1. **Indexing**
#    - **Explanation:** Indexes improve the speed of data retrieval operations on a database at the cost of additional storage space and 
# slower write operations. An index works like a book's index, allowing quick location of data without scanning the whole table.
#    - **Example:** If you have a table called `employees` with columns `id`, `name`, and `department`, and you frequently search for 
# employees by department, you should create an index on the `department` column. In SQL, you can create an index using:
#      ```sql
#      CREATE INDEX idx_department ON employees(department);
#      ```

# 2. **Query Optimization**
#    - **Explanation:** Optimize SQL queries by rewriting them to ensure they execute as efficiently as possible. This can involve 
# restructuring queries, using joins effectively, and minimizing subqueries.
#    - **Example:** Rather than using subqueries, use joins when possible. Instead of:
#      ```sql
#      SELECT e.name FROM employees e WHERE e.id IN (SELECT id FROM departments WHERE name = 'Sales');
#      ```
#      Use a join:
#      ```sql
#      SELECT e.name 
#      FROM employees e 
#      JOIN departments d ON e.department_id = d.id 
#      WHERE d.name = 'Sales';
#      ```

# 3. **Avoiding `SELECT *** `
#    - **Explanation:** Using `SELECT *` retrieves all columns in the table, which can result in unnecessary data loading and processing. 
# Specify only the columns you need in your query to reduce load and improve performance.
#    - **Example:** Instead of:
#      ```sql
#      SELECT * FROM employees;
#      ```
#      Specify needed columns:
#      ```sql
#      SELECT name, department FROM employees;
#      ```

# 4. **Limiting Result Sets**
#    - **Explanation:** Whenever possible, limit the number of rows returned by a query to only what is necessary, especially when working 
# with large datasets. This can significantly reduce the workload on both the database server and the application consuming the data.
#    - **Example:** Use `LIMIT` or `FETCH` to restrict results:
#      ```sql
#      SELECT name FROM employees ORDER BY hire_date DESC LIMIT 10;
#      ```
#      This retrieves only the ten most recently hired employees.

# 5. **Use Appropriate Data Types**
#    - **Explanation:** Choosing the correct data type for each column can help optimize storage and speed up the processing of queries. 
# Smaller data types are generally faster to process.
#    - **Example:** For a column that will store integer values up to 100, use `TINYINT` instead of `INT`:
#      ```sql
#      CREATE TABLE sales(
#        id TINYINT,
#        product_name VARCHAR(255),
#        amount DECIMAL(10, 2)
#      );
#      ```
#    - Proper use of data types can significantly impact the efficiency of data retrieval and storage operations. Choosing the minimal size 
# type that serves your purpose is usually best practice.

# Input tokens: 89
# Output tokens: 650
# Total tokens: 739
# -------------------------------------------------- 
# USER PROMPT:

# You are a software architect. I want you to produce an Architecture Decision Record (ADR) about choosing PostgreSQL instead of MongoDB. 

# Follow the Skeleton of Thought approach:
# Step 1: First, output only the skeleton of the ADR as section headers (no explanations yet). 
# Use the standard ADR structure with 5 sections: Context, Decision, Alternatives Considered, Consequences, References. 
# Step 2: After showing the skeleton, expand each section with clear and detailed content. 
# Keep the final ADR professional, structured, and easy to read.


# LLM RESPONSE:
# ## Step 1: Skeleton of the ADR

# 1. Context
# 2. Decision
# 3. Alternatives Considered
# 4. Consequences
# 5. References

# ---

# ## Step 2: Expanded ADR

# ### 1. Context

# In our current project, we need to select a database management system that can efficiently handle structured data with complex queries and
# provide robust transactional support. The system requirements include high reliability, consistency, and support for complex queries, as 
# well as scalability for anticipated growth. The team is evaluating options for the primary database to be used in our system architecture, 
# with PostgreSQL and MongoDB being the leading candidates. The choice of database will significantly impact development agility and system 
# performance.

# ### 2. Decision

# We have decided to use PostgreSQL as our primary database management system for the project. PostgreSQL offers advanced features such as 
# ACID compliance, complex querying capabilities, and strong support for relational data, which align closely with our project requirements. 
# The choice reflects a need for reliable transactional support and the ability to handle complex data queries effectively.

# ### 3. Alternatives Considered

# - **MongoDB**: Considered for its flexibility and scalability. MongoDB is a NoSQL database that can handle unstructured data and allows for
# dynamic schema design, making it suitable for applications that might evolve in unpredictable ways. However, it is not as strong as 
# PostgreSQL in handling complex joins or maintaining ACID transactions without additional configurations.
  
# - **PostgreSQL**: A relational database that offers robust ACID transactions, complex querying capabilities, and extensive support for 
# constraints and data integrity checks. It is highly suitable for applications requiring structured data and a well-defined schema.

# ### 4. Consequences

# - **Positive Consequences**: 
#   - **Data Integrity and Reliability**: PostgreSQL's comprehensive support for ACID transactions ensures data integrity and fault 
# tolerance.
#   - **Complex Queries and Reporting**: The ability to handle complex queries efficiently reduces the need for application-level data 
# processing and allows for more sophisticated reporting and analytics.
#   - **Community and Ecosystem**: PostgreSQL has a strong community and a rich ecosystem of extensions which can be leveraged to add 
# capabilities such as full-text search, geolocation, and more.

# - **Negative Consequences**:
#   - **Scalability Concerns**: While PostgreSQL can scale vertically and supports partitioning and sharding, it is traditionally perceived 
# to have limitations compared to NoSQL options like MongoDB in horizontal scaling out of the box.
#   - **Learning Curve**: The need to understand and design around relational schemas may require additional learning for team members who 
# are less familiar with SQL or relational database design.

# ### 5. References

# - PostgreSQL Official Documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
# - MongoDB Official Documentation: [https://docs.mongodb.com/](https://docs.mongodb.com/)
# - "PostgreSQL vs. MongoDB: A Comparison of Features", Tech Journal, 2023
# - ACID Compliance and Performance Considerations, Database Insights, 2023

# This Architecture Decision Record outlines the decision-making process and the rationale for choosing PostgreSQL over MongoDB in our 
# current project, considering the key requirements and potential impacts.

# Input tokens: 121
# Output tokens: 657
# Total tokens: 778
# -------------------------------------------------- 
# USER PROMPT:

# You are a senior Go developer. I want you to help me plan a REST API for managing products in Go.

# Follow the Skeleton of Thought approach:

# Step 1: Output only the skeleton of the solution in 6–8 concise bullet points. 
# The skeleton must cover: data model definition in Go (structs), choice of HTTP framework or net/http, routing, 
# handlers, validations, database layer, error handling, and project structure. Do not expand yet.

# Step 2: Expand each bullet point with clear technical details, examples, and Go best practices. 
# Include sample code snippets in Go (structs, handlers, routes) and considerations about packages 
# (e.g., chi, or net/http), error handling with idiomatic Go, and how to organize the project into packages (handlers, models, db). 
# Use concise and professional language.

# The API must implement CRUD operations for products with fields: id, name, description, price, stock.


# LLM RESPONSE:
# Certainly! Let's delve into the planning of a REST API for managing products in Go, following your outlined approach.

# ### Step 1: Skeleton

# 1. **Data Model Definition**
#    - Define Product struct with fields: id, name, description, price, stock.

# 2. **Choice of HTTP Framework**
#    - Decide between using `net/http` or a third-party router like `chi`.

# 3. **Routing Setup**
#    - Set up routes for CRUD operations: Create, Read (single and list), Update, Delete.

# 4. **Handlers Implementation**
#    - Write handlers for each route to manage products.

# 5. **Validations**
#    - Implement validation logic for incoming requests (e.g., non-negative price and stock).

# 6. **Database Layer**
#    - Integrate a database layer for persistent storage and retrieval.

# 7. **Error Handling**
#    - Implement structured error handling and return appropriate HTTP status codes.

# 8. **Project Structure**
#    - Organize the project into packages: handlers, models, db, main.

# ### Step 2: Expanded Details

# 1. **Data Model Definition**
#    ```go
#    package models

#    type Product struct {
#        ID          int     `json:"id"`
#        Name        string  `json:"name"`
#        Description string  `json:"description"`
#        Price       float64 `json:"price"`
#        Stock       int     `json:"stock"`
#    }
#    ```
#    *Define a `Product` struct using Go's struct tags to facilitate JSON serialization.*

# 2. **Choice of HTTP Framework**
#    - Use `chi` for its lightweight and idiomatic design that fits naturally with Go's `net/http`.
#    ```go
#    import (
#        "github.com/go-chi/chi/v5"
#    )
#    ```

# 3. **Routing Setup**
#    ```go
#    package main

#    import (
#        "net/http"
#        "github.com/go-chi/chi/v5"
#    )

#    func main() {
#        r := chi.NewRouter()
#        r.Route("/products", func(r chi.Router) {
#            r.Post("/", CreateProduct) // Create
#            r.Get("/", ListProducts)   // Read all
#            r.Get("/{id}", GetProduct) // Read one
#            r.Put("/{id}", UpdateProduct) // Update
#            r.Delete("/{id}", DeleteProduct) // Delete
#        })
#        http.ListenAndServe(":8080", r)
#    }
#    ```
#    *Set up routes using Chi, associating endpoints with the corresponding handler functions.*

# 4. **Handlers Implementation**
#    ```go
#    package handlers

#    import (
#        "encoding/json"
#        "net/http"
#        "strconv"
#        "github.com/go-chi/chi/v5"
#        "your_project/models"
#    )
   
#    func CreateProduct(w http.ResponseWriter, r *http.Request) {
#        var product models.Product
#        if err := json.NewDecoder(r.Body).Decode(&product); err != nil {
#            http.Error(w, "Invalid input", http.StatusBadRequest)
#            return
#        }
#        // Assume addProduct is a function that saves product to DB and assigns an ID
#        addProduct(&product) 
#        w.WriteHeader(http.StatusCreated)
#        json.NewEncoder(w).Encode(product)
#    }

#    func GetProduct(w http.ResponseWriter, r *http.Request) {
#        id, err := strconv.Atoi(chi.URLParam(r, "id"))
#        if err != nil {
#            http.Error(w, "Invalid ID", http.StatusBadRequest)
#            return
#        }
#        product, err := fetchProductByID(id) // Assume this function fetches product from DB
#        if err != nil {
#            http.Error(w, "Product not found", http.StatusNotFound)
#            return
#        }
#        json.NewEncoder(w).Encode(product)
#    }

#    // Implement other handler functions similarly
#    ```
#    *Create handlers with proper parameter reading, logic execution, and response serialization.*

# 5. **Validations**
#    ```go
#    package handlers

#    func validateProduct(product *models.Product) error {
#        if product.Price < 0 {
#            return fmt.Errorf("Price cannot be negative")
#        }
#        if product.Stock < 0 {
#            return fmt.Errorf("Stock cannot be negative")
#        }
#        // other validations as needed
#        return nil
#    }
#    ```
#    *Incorporate simple validation checks using functions returning errors.*

# 6. **Database Layer**
#    - Use an ORM like GORM or directly use database/sql for DB operations.
#    ```go
#    package db

#    import (
#        "gorm.io/driver/postgres"
#        "gorm.io/gorm"
#    )

#    var DB *gorm.DB

#    func Init() {
#        dsn := "host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai"
#        db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
#        if err != nil {
#            panic("failed to connect database")
#        }
#        db.AutoMigrate(&models.Product{})
#        DB = db
#    }
#    ```
#    *Set up a database connection and handle initialization tasks.*

# 7. **Error Handling**
#    - Use Go's error handling paradigm with concise error messages and context where necessary.

# 8. **Project Structure**
#    ```
#    project/
#    ├── main.go
#    ├── handlers/
#    │   └── products.go
#    ├── models/
#    │   └── product.go
#    ├── db/
#        └── setup.go
#    ```
#    *Maintain a clean and logical organization that aligns with Go's package system, aiding readability and maintenance.*

# Input tokens: 202
# Output tokens: 1171
# Total tokens: 1373
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 




# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/bin/python /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/1-tipos-de-prompts/5-SoT.py
# /Users/mhcj/Downloads/github/MBA-sw-engineering-AI/20250902-criacao-e-tipos-de-prompt/.venv/lib/python3.14/site-packages/openai/_compat.py:48: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
#   from pydantic.v1.typing import (
# USER PROMPT:

# You are a senior backend engineer. A junior developer asked you how to optimize SQL queries for better performance. 
# Follow the Skeleton of Thought approach: 

# Step 1: Generate only the skeleton of your answer in 3–5 concise bullet points. 
# Step 2: Expand each bullet point into a clear and detailed explanation with examples. 
# Make sure the final answer is structured and easy to follow.


# LLM RESPONSE:
# Step 1
# - Indexing strategy and up-to-date statistics
# - Write sargable predicates and avoid non-sargable patterns
# - Minimize data scanned and returned (projection, early filtering, pagination)
# - Tune with query plans and related patterns (EXPLAIN, refactor N+1, materialized views, partitioning)

# Step 2
# - Indexing strategy and up-to-date statistics
#   - Why: Proper indexes reduce full-table scans and help the optimizer choose efficient access paths. Keeping statistics fresh helps the 
# planner estimate cardinalities correctly.
#   - How:
#     - Create composite indexes that cover filters and joins used by the query.
#     - Consider covering indexes so the engine can satisfy the query from the index itself (no extra lookups).
#     - Update stats regularly (e.g., ANALYZE in PostgreSQL, ANALYZE TABLE in MySQL).
#   - Example:
#     - Problem query:
#       SELECT o.id, o.total
#       FROM orders o
#       JOIN customers c ON o.customer_id = c.id
#       WHERE c.status = 'ACTIVE' AND o.created_at >= '2024-01-01'
#       ORDER BY o.created_at DESC
#       LIMIT 100;
#     - Recommended indexes:
#       - On orders: CREATE INDEX idx_orders_customer_created ON orders (customer_id, created_at DESC);
#       - On customers: CREATE INDEX idx_customers_status ON customers (status);
#       - Optional covering index (PostgreSQL 11+): CREATE INDEX idx_orders_cover ON orders (customer_id, created_at) INCLUDE (id, total);
#     - Verify with explain:
#       - EXPLAIN ANALYZE SELECT ...;
#         You should see an index scan rather than a sequential scan, and the join path chosen (e.g., hash join, nested loop) will reflect 
# the plan.
#     - Keep stats fresh:
#       - PostgreSQL: ANALYZE orders; ANALYZE customers;
#       - MySQL: ANALYZE TABLE orders; ANALYZE TABLE customers;
#   - Takeaway: Start with a plan, add targeted indexes for the specific predicates and joins, and confirm with a real EXPLAIN plan.

# - Write sargable predicates and avoid non-sargable patterns
#   - Why: Sargable predicates allow the index to be used efficiently; non-sargable patterns force full scans or broad scans.
#   - How:
#     - Prefer direct comparisons or ranges on columns, avoid wrapping a column in a function.
#     - Avoid leading wildcards and apply proper search strategies (full-text search or trigram indexes if needed).
#     - Prefer EXISTS for correlated subqueries over IN with a subquery in many cases; avoid OR across large conditions.
#   - Examples:
#     - Non-sargable vs sargable:
#       - Bad: WHERE YEAR(created_at) = 2024
#       - Good: WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'
#     - Case-insensitive comparisons:
#       - Bad: WHERE LOWER(email) = LOWER('alice@example.com')
#       - Good: Normalize data or use a case-insensitive collation; or create a functional index if you must use a function (e.g., CREATE 
# INDEX ON users (LOWER(email)); and query with LOWER(email)).
#     - Subqueries:
#       - Bad: SELECT * FROM users u WHERE u.id IN (SELECT user_id FROM orders WHERE amount > 100)
#       - Good: SELECT u.* FROM users u JOIN orders o ON o.user_id = u.id WHERE o.amount > 100
#     - Leading wildcard:
#       - Bad: WHERE name LIKE '%john%'
#       - Good: For such searches, consider trigram indexes or full-text search, e.g., PostgreSQL pg_trgm: CREATE INDEX ON users USING gin 
# (name gin_trgm_ops); and query with WHERE name ILIKE '%john%'.
#   - Takeaway: Make predicates operate on indexed columns in a way the DB can use.

# - Minimize data scanned and returned (projection, early filtering, pagination)
#   - Why: Reducing column and row scans reduces I/O and memory usage, speeding up queries and reducing network transfer.
#   - How:
#     - SELECT only the columns you actually need (avoid SELECT *) and, if possible, rely on covering indexes.
#     - Push filters as close to the data as possible (early WHERE clauses before ORDER BY or JOINs).
#     - Use efficient pagination (prefer keyset pagination over OFFSET-based pagination for large datasets).
#   - Examples:
#     - Narrow projection:
#       - Bad: SELECT * FROM orders WHERE customer_id = ? AND status = 'SHIPPED' LIMIT 50;
#       - Good: SELECT id, created_at, total FROM orders WHERE customer_id = ? AND status = 'SHIPPED' ORDER BY created_at DESC LIMIT 50;
#       - Index suggestion: CREATE INDEX idx_orders_customer_status_created ON orders (customer_id, status, created_at DESC);
#     - Keyset pagination:
#       - Instead of OFFSET 1000, use:
#         SELECT id, created_at FROM orders
#         WHERE customer_id = ? AND created_at < '2025-01-01'
#         ORDER BY created_at DESC
#         LIMIT 50;
#       - This keeps the plan stable and avoids skipping lots of rows.
#   - Takeaway: Projection and pagination choices can dramatically cut data movement and improve latency.

# - Tune with query plans and related patterns (EXPLAIN, refactor N+1, materialized views, partitioning)
#   - Why: A plan reveals bottlenecks (seq scans, heavy sorts, large hash joins, etc.) and helps you choose concrete fixes.
#   - How:
#     - Always start with EXPLAIN (and EXPLAIN ANALYZE) to see how the planner executes the query.
#     - Address N+1 patterns by transforming them into a single query with joins or aggregations.
#     - Consider materialized views or caching for expensive, rarely-changing results; consider partitioning for large, date-based datasets.
#   - Examples:
#     - N+1 problem:
#       - N+1 version: for each user, query their orders individually.
#       - Better: SELECT u.id, SUM(o.total) AS total_spent FROM users u LEFT JOIN orders o ON o.user_id = u.id GROUP BY u.id;
#       - If data changes slowly, consider a materialized view: CREATE MATERIALIZED VIEW mv_user_totals AS SELECT user_id, SUM(total) AS 
# total_spent FROM orders GROUP BY user_id; REFRESH MATERIALIZED VIEW mv_user_totals;
#     - Plan-driven refactor:
#       - If EXPLAIN shows a Seq Scan on a large table with a join, add a targeted index or rewrite the query to use a more selective 
# predicate.
#     - Partitioning:
#       - For large, time-based data (e.g., orders by date), use partitioning to prune partitions:
#         - PostgreSQL: PARTITION BY RANGE (created_at); create partitions like orders_2024_01, orders_2024_02, etc.
#       - This reduces the amount of data scanned per query when you filter by created_at.
#   - Takeaway: Use explain plans to drive concrete changes, optimize join paths, remove N+1 patterns, and consider caching or partitioning 
# for heavy workloads.

# If you want, share a specific query or schema, and I can walk through a concrete optimization plan with exact indexes, query rewrites, and 
# a sample EXPLAIN ANALYZE output.

# Input tokens: 88
# Output tokens: 6024
# Total tokens: 6112
# -------------------------------------------------- 
# USER PROMPT:

# You are a software architect. I want you to produce an Architecture Decision Record (ADR) about choosing PostgreSQL instead of MongoDB. 

# Follow the Skeleton of Thought approach:
# Step 1: First, output only the skeleton of the ADR as section headers (no explanations yet). 
# Use the standard ADR structure with 5 sections: Context, Decision, Alternatives Considered, Consequences, References. 
# Step 2: After showing the skeleton, expand each section with clear and detailed content. 
# Keep the final ADR professional, structured, and easy to read.


# LLM RESPONSE:
# Step 1: Skeleton of the ADR
# Context
# Decision
# Alternatives Considered
# Consequences
# References

# Step 2: Expanded ADR
# Context
# - Objective and scope: This Architecture Decision Record evaluates the primary data persistence technology for the system. The goal is to 
# durability, consistency, and maintainability across services by selecting PostgreSQL over MongoDB as the default operational data store.
# - Problem statement: The organization currently uses MongoDB for certain services and workloads. While MongoDB offers flexible schemas and 
# rapid development for unstructured data, it presents challenges around data integrity, complex transactional requirements, and long-term 
# maintainability when used as the sole persistence layer for diverse domains.
# - Requirements driving the decision:
#   - Strong data integrity and ACID transactions for business processes spanning multiple entities.
#   - Support for complex queries, reporting, and analytics with SQL-based tooling.
#   - Efficient handling of relational data with clear schema enforcement and constraints.
#   - Ability to store semi-structured data where needed (JSONB) without sacrificing relational capabilities.
#   - Mature ecosystem of tooling, monitoring, backup, restores, and security features.
#   - Operational considerations: predictable scaling, high availability, point-in-time recovery, and cloud/provider options (including 
# managed services).
# - Constraints and context: The system includes services that require cross-service joins, referential integrity, and robust transaction 
# semantics. The team has strong SQL and relational-database experience. There is a desire to unify persistence across services to simplify 
# data governance and developer onboarding. A migration plan will be staged to minimize risk and downtime.

# Decision
# - The organization will adopt PostgreSQL as the primary data persistence layer for new work and as the canonical database for existing 
# services currently relying on MongoDB, where feasible.
# - PostgreSQL will be used as the system’s OLTP backbone, supplemented by:
#   - JSONB storage for semi-structured data and evolving schemas, with appropriate indexing.
#   - PostgreSQL extensions as needed (for example, PostGIS for geospatial data, full-text search, and indexing enhancements).
#   - Read replicas and partitioning to scale read throughput and manage large datasets.
# - MongoDB usage will be evaluated for each workload currently backed by MongoDB. Where data models are naturally document-oriented with 
# minimal cross-document transactions, a migration to PostgreSQL with JSONB may be pursued. If a workload remains better suited to 
# document-centric access patterns, MongoDB may be retained there, but within a well-defined boundary and with explicit justification.
# - Data governance, security, and observability will be standardized around PostgreSQL capabilities, with migration tooling and a phased 
# plan to minimize risk and downtime.

# Alternatives Considered
# - MongoDB as primary database (document store)
#   - Pros: Flexible schema, fast writes for certain workloads, natural fit for unstructured data, easy horizontal scaling in some scenarios.
#   - Cons: Historically weaker guarantees around multi-document transactions (though modern versions support ACID across documents to an 
# extent), more complex data integrity enforcement for cross-collection relationships, less straightforward for complex analytics and ad hoc 
# reporting, and a different query paradigm that requires learning.MongoDB’s eventual consistency in certain configurations can complicate 
# business-critical workflows.
#   - Rationale for not selecting: Our domain benefits from strong data integrity, relational queries, and robust SQL tooling. A single, 
# relational-first store reduces data modeling complexity, improves consistency guarantees, and simplifies governance.
# - MySQL/MariaDB as alternative relational store
#   - Pros: Mature, widely supported, strong replication options.
#   - Cons: PostgreSQL generally offers more advanced features (e.g., richer JSON support with JSONB, more sophisticated indexing and 
# partitioning, advanced concurrency controls, Postgres extensions) that align better with our requirement set.
#   - Rationale for not selecting as the primary: PostgreSQL provides broader feature parity with a modern extension ecosystem that better 
# fits our needs (JSONB, advanced indexing, extensibility, analytics capabilities).
# - Other NoSQL or NewSQL options (e.g., Cassandra, Redis as primary store)
#   - Pros: Specialized guarantees or extremely scalable architectures for certain workloads.
#   - Cons: Require separate data models and significantly different application logic; lack of strong relational features for multi-entity 
# transactions; higher total cost of ownership for a unified persistence strategy.
#   - Rationale for not selecting: We seek to minimize polyglot persistence complexity unless a compelling, workload-driven justification 
# exists. The PostgreSQL route offers a well-supported, unified model with flexible JSON storage and strong transactional guarantees.

# Consequences
# - Positive consequences:
#   - Data integrity and correctness: ACID transactions and strong constraints improve data quality and correctness across services.
#   - Unified tooling and skills: Teams can leverage a single, mature SQL-based ecosystem for development, testing, analytics, and 
# operations.
#   - Rich querying and analytics: SQL interfaces enable complex joins, aggregations, and ad-hoc reporting; JSONB provides flexibility for 
# semi-structured data without abandoning relational benefits.
#   - Observability and management: Mature backup/restore, point-in-time recovery, auditing, security (roles, permissions, row-level 
# security), and monitoring capabilities.
#   - Scalability path: Read replicas, connection pooling, table partitioning, and streaming replication enable scalable reads and large data
# volumes; PostgreSQL extensions broaden capabilities (e.g., geographic data, full-text search).
#   - Operational cost and vendor risk: PostgreSQL is open source with wide cloud support (managed services and on-prem), reducing vendor 
# lock-in and offering flexibility in hosting.
# - Negative consequences:
#   - Migration effort and risk: Phased migration from MongoDB to PostgreSQL requires careful data modeling, ETL steps, and potential 
# downtime planning.
#   - Learning curve and design changes: Teams may need to adjust to relational modeling best practices, SQL optimization, and migration 
# tooling; JSONB usage requires new indexing and query patterns.
#   - Storage footprint: Relational schemas may incur different storage characteristics; planning is needed to optimize schema design and 
# indexing to avoid bloat.
#   - Operational overhead during transition: Dual-write or data-synchronization strategies may be necessary during migration; monitoring and
# consistency checks become more important.
# - Migration plan highlights:
#   - Inventory workloads and data models currently in MongoDB.
#   - Map to PostgreSQL relational schema with JSONB for semi-structured data.
#   - Pilot migration for non-critical services to validate performance and data integrity.
#   - Introduce staged data synchronization or dual-write approaches where appropriate.
#   - Establish testing harnesses, rollback strategies, and monitoring dashboards.
#   - Provide training and documentation for the engineering teams on PostgreSQL-specific features and best practices.
# - Risks and mitigations:
#   - Risk: Increased migration complexity and potential service disruption.
#     - Mitigation: Start with non-critical components, use feature flags, and employ robust rollback procedures.
#   - Risk: Suboptimal JSONB indexing leading to performance regressions.
#     - Mitigation: Profile queries, implement appropriate GIN/BTREE indexes, and adopt best practices for JSONB data modeling.
#   - Risk: Inadequate operational readiness (backups, point-in-time recovery, security).
#     - Mitigation: Establish and test runbooks, automate backups, and enforce security policies early in the migration.

# References
# - PostgreSQL Documentation: https://www.postgresql.org/docs/current/
# - PostgreSQL JSONB and indexing: https://www.postgresql.org/docs/current/functions-json.html
# - PostgreSQL performance and partitioning: https://www.postgresql.org/docs/current/ddl-partitioning.html
# - MongoDB Documentation (for comparison): https://www.mongodb.com/docs/
# - ACID and transaction concepts: https://en.wikipedia.org/wiki/ACID
# - Cloud-managed PostgreSQL offerings and best practices: vendor-specific documentation (e.g., AWS RDS/Aurora PostgreSQL, Google Cloud SQL 
# for PostgreSQL, Azure Database for PostgreSQL)

# Input tokens: 120
# Output tokens: 4536
# Total tokens: 4656
# -------------------------------------------------- 
# USER PROMPT:

# You are a senior Go developer. I want you to help me plan a REST API for managing products in Go.

# Follow the Skeleton of Thought approach:

# Step 1: Output only the skeleton of the solution in 6–8 concise bullet points. 
# The skeleton must cover: data model definition in Go (structs), choice of HTTP framework or net/http, routing, 
# handlers, validations, database layer, error handling, and project structure. Do not expand yet.

# Step 2: Expand each bullet point with clear technical details, examples, and Go best practices. 
# Include sample code snippets in Go (structs, handlers, routes) and considerations about packages 
# (e.g., chi, or net/http), error handling with idiomatic Go, and how to organize the project into packages (handlers, models, db). 
# Use concise and professional language.

# The API must implement CRUD operations for products with fields: id, name, description, price, stock.


# LLM RESPONSE:
# Step 1 – Skeleton (6–8 concise bullets)

# - Data model: define a Go struct for Product with id, name, description, price, stock (JSON/db tags as needed). 
# - HTTP framework: choose chi (a lightweight, idiomatic net/http router) and illustrate minimal net/http usage. 
# - Routing: expose CRUD endpoints for /products (POST, GET, GET /{id}, PUT /{id}, DELETE /{id}). 
# - Handlers: implement create, read (single and list), update, delete with clear separation (handler layer uses a store). 
# - Validations: validate required fields and constraints (e.g., non-negative price/stock) with clear error responses. 
# - Database layer: repository pattern with a ProductStore interface and a Postgres (sql.DB) implementation; include basic SQL statements. 
# - Error handling & project structure: unified error responses, domain errors mapping to HTTP status codes; modular project layout (cmd, 
# internal/models, internal/handler, internal/store, internal/db).

# Step 2 – Expanded details, with Go code samples

# 1) Data model: Product struct (id, name, description, price, stock)

# - Rationale: type-safe domain model, JSON tags for API, optional DB tags if using ORM or SQL.
# - Example (pkg: internal/models/product.go):

# package models

# type Product struct {
#     ID          int64   `json:"id"`
#     Name        string  `json:"name"`
#     Description string  `json:"description"`
#     Price       float64 `json:"price"`
#     Stock       int     `json:"stock"`
# }

# Notes:
# - Use int64 for ID to cover large datasets and easy conversion from SQL.
# - Consider adding validation tags if you opt to use a validator library later.

# 2) HTTP framework: chi + net/http

# - Rationale: lightweight, idiomatic, minimal middleware, good for building clean handlers.
# - Example (pkg: cmd/api/main.go):

# package main

# import (
#     "log"
#     "net/http"
#     "github.com/go-chi/chi/v5"
#     "github.com/go-chi/chi/v5/middleware"
#     "your/module/internal/handler"
#     "your/module/internal/store"
# )

# func main() {
#     r := chi.NewRouter()
#     r.Use(middleware.RequestID)
#     r.Use(middleware.Logger)
#     r.Use(middleware.Recoverer)

#     // assume we have a concrete store wired with DB
#     db := store.MustOpenPostgres() // returns *sql.DB or a Store implementation
#     ps := store.NewPostgresStore(db)
#     h := handler.NewProductHandler(ps)

#     r.Route("/products", func(r chi.Router) {
#         r.Post("/", h.CreateProduct)
#         r.Get("/", h.ListProducts)
#         r.Get("/{id}", h.GetProduct)
#         r.Put("/{id}", h.UpdateProduct)
#         r.Delete("/{id}", h.DeleteProduct)
#     })

#     log.Println("API listening on :8080")
#     http.ListenAndServe(":8080", r)
# }

# 3) Routing: CRUD endpoints

# - Endpoints to implement:
#   - POST /products          -> createProduct
#   - GET /products           -> listProducts
#   - GET /products/{id}       -> getProduct
#   - PUT /products/{id}       -> updateProduct
#   - DELETE /products/{id}    -> deleteProduct
# - Example route wiring (as above) demonstrates chi usage and parameter extraction in handlers.

# 4) Handlers: CRUD logic and wiring to store

# - Rationale: keep handlers thin, delegate persistence to a repository/store; use context for cancellation and tracing.
# - Example (pkg: internal/handler/product.go):

# package handler

# import (
#     "context"
#     "encoding/json"
#     "net/http"
#     "strconv"

#     "github.com/go-chi/chi/v5"
#     "your/module/internal/models"
#     "your/module/internal/store"
#     "your/module/internal/errors"
# )

# type ProductHandler struct {
#     store store.ProductStore
# }

# func NewProductHandler(s store.ProductStore) *ProductHandler {
#     return &ProductHandler{store: s}
# }

# // CreateProduct handles POST /products
# func (h *ProductHandler) CreateProduct(w http.ResponseWriter, r *http.Request) {
#     var p models.Product
#     if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
#         respondError(w, http.StatusBadRequest, "invalid request body")
#         return
#     }

#     // basic validation (could switch to a validator library)
#     if p.Name == "" {
#         respondError(w, http.StatusBadRequest, "name is required")
#         return
#     }
#     if p.Price < 0 {
#         respondError(w, http.StatusBadRequest, "price must be non-negative")
#         return
#     }
#     if p.Stock < 0 {
#         respondError(w, http.StatusBadRequest, "stock must be non-negative")
#         return
#     }

#     if err := h.store.Create(r.Context(), &p); err != nil {
#         respondError(w, http.StatusInternalServerError, "failed to create product")
#         return
#     }

#     w.WriteHeader(http.StatusCreated)
#     json.NewEncoder(w).Encode(p)
# }

# // GetProduct handles GET /products/{id}
# func (h *ProductHandler) GetProduct(w http.ResponseWriter, r *http.Request) {
#     idParam := chi.URLParam(r, "id")
#     id, err := strconv.ParseInt(idParam, 10, 64)
#     if err != nil {
#         respondError(w, http.StatusBadRequest, "invalid id")
#         return
#     }

#     p, err := h.store.Get(r.Context(), id)
#     if err != nil {
#         if errors.IsNotFound(err) {
#             respondError(w, http.StatusNotFound, "product not found")
#         } else {
#             respondError(w, http.StatusInternalServerError, "failed to fetch product")
#         }
#         return
#     }

#     json.NewEncoder(w).Encode(p)
# }

# // ListProducts handles GET /products
# func (h *ProductHandler) ListProducts(w http.ResponseWriter, r *http.Request) {
#     list, err := h.store.List(r.Context())
#     if err != nil {
#         respondError(w, http.StatusInternalServerError, "failed to list products")
#         return
#     }
#     json.NewEncoder(w).Encode(list)
# }

# // UpdateProduct handles PUT /products/{id}
# func (h *ProductHandler) UpdateProduct(w http.ResponseWriter, r *http.Request) {
#     idParam := chi.URLParam(r, "id")
#     id, err := strconv.ParseInt(idParam, 10, 64)
#     if err != nil {
#         respondError(w, http.StatusBadRequest, "invalid id")
#         return
#     }

#     var p models.Product
#     if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
#         respondError(w, http.StatusBadRequest, "invalid request body")
#         return
#     }
#     p.ID = id

#     if p.Price < 0 || p.Stock < 0 || p.Name == "" {
#         respondError(w, http.StatusBadRequest, "invalid product fields")
#         return
#     }

#     if err := h.store.Update(r.Context(), &p); err != nil {
#         if errors.IsNotFound(err) {
#             respondError(w, http.StatusNotFound, "product not found")
#         } else {
#             respondError(w, http.StatusInternalServerError, "failed to update product")
#         }
#         return
#     }

#     json.NewEncoder(w).Encode(p)
# }

# // DeleteProduct handles DELETE /products/{id}
# func (h *ProductHandler) DeleteProduct(w http.ResponseWriter, r *http.Request) {
#     idParam := chi.URLParam(r, "id")
#     id, err := strconv.ParseInt(idParam, 10, 64)
#     if err != nil {
#         respondError(w, http.StatusBadRequest, "invalid id")
#         return
#     }

#     if err := h.store.Delete(r.Context(), id); err != nil {
#         if errors.IsNotFound(err) {
#             respondError(w, http.StatusNotFound, "product not found")
#         } else {
#             respondError(w, http.StatusInternalServerError, "failed to delete product")
#         }
#         return
#     }

#     w.WriteHeader(http.StatusNoContent)
# }

# // helper: respond with JSON error
# func respondError(w http.ResponseWriter, code int, message string) {
#     w.WriteHeader(code)
#     json.NewEncoder(w).Encode(map[string]string{"error": message})
# }

# Notes:
# - The handler relies on the ProductStore interface for persistence and can be swapped with a mock in tests.

# 5) Validations: input checks and error responses

# - Rationale: enforce business rules at boundary; keep handlers resilient and return meaningful HTTP errors.
# - Validation approaches:
#   - Simple inline checks (as shown above): required fields, non-negative numbers.
#   - Optional: integrate go-playground/validator for struct tags like validate:"required" and validate:"gte=0".
# - Example with a validator (optional enhancement):

# type ProductInput struct {
#     Name        string  `json:"name" validate:"required"`
#     Description string  `json:"description"`
#     Price       float64 `json:"price" validate:"gte=0"`
#     Stock       int     `json:"stock" validate:"gte=0"`
# }

# // inside CreateProduct
# if err := validator.New().Struct(p); err != nil {
#     respondError(w, http.StatusBadRequest, "validation failed")
#     return
# }

# 6) Database layer: repository pattern (ProductStore) and Postgres implementation

# - Rationale: decouple usage from persistence; enables tests with in-memory or alternative stores.
# - Interfaces (pkg: internal/store/store.go):

# package store

# import "context"

# type ProductStore interface {
#     Create(ctx context.Context, p *models.Product) error
#     Get(ctx context.Context, id int64) (*models.Product, error)
#     List(ctx context.Context) ([]*models.Product, error)
#     Update(ctx context.Context, p *models.Product) error
#     Delete(ctx context.Context, id int64) error
# }

# var (
#     // sentinel errors for domain
#     ErrNotFound = errors.New("not found")
# )

# - PostgreSQL implementation (pkg: internal/store/postgres.go):

# package postgres

# import (
#     "context"
#     "database/sql"
#     "errors"

#     "your/module/internal/models"
#     "your/module/internal/store"
# )

# type PostgresStore struct {
#     db *sql.DB
# }

# func NewPostgresStore(db *sql.DB) *PostgresStore { return &PostgresStore{db: db} }

# func (s *PostgresStore) Create(ctx context.Context, p *models.Product) error {
#     query := `INSERT INTO products (name, description, price, stock) VALUES ($1, $2, $3, $4) RETURNING id`
#     err := s.db.QueryRowContext(ctx, query, p.Name, p.Description, p.Price, p.Stock).Scan(&p.ID)
#     return err
# }

# func (s *PostgresStore) Get(ctx context.Context, id int64) (*models.Product, error) {
#     row := s.db.QueryRowContext(ctx, `SELECT id, name, description, price, stock FROM products WHERE id=$1`, id)
#     p := &models.Product{}
#     if err := row.Scan(&p.ID, &p.Name, &p.Description, &p.Price, &p.Stock); err != nil {
#         if err == sql.ErrNoRows {
#             return nil, store.ErrNotFound
#         }
#         return nil, err
#     }
#     return p, nil
# }

# func (s *PostgresStore) List(ctx context.Context) ([]*models.Product, error) {
#     rows, err := s.db.QueryContext(ctx, `SELECT id, name, description, price, stock FROM products ORDER BY id`)
#     if err != nil {
#         return nil, err
#     }
#     defer rows.Close()

#     var list []*models.Product
#     for rows.Next() {
#         p := &models.Product{}
#         if err := rows.Scan(&p.ID, &p.Name, &p.Description, &p.Price, &p.Stock); err != nil {
#             return nil, err
#         }
#         list = append(list, p)
#     }
#     return list, rows.Err()
# }

# func (s *PostgresStore) Update(ctx context.Context, p *models.Product) error {
#     res, err := s.db.ExecContext(ctx, `
#         UPDATE products SET name=$1, description=$2, price=$3, stock=$4 WHERE id=$5
#     `, p.Name, p.Description, p.Price, p.Stock, p.ID)
#     if err != nil {
#         return err
#     }
#     n, err := res.RowsAffected()
#     if err != nil {
#         return err
#     }
#     if n == 0 {
#         return store.ErrNotFound
#     }
#     return nil
# }

# func (s *PostgresStore) Delete(ctx context.Context, id int64) error {
#     res, err := s.db.ExecContext(ctx, `DELETE FROM products WHERE id=$1`, id)
#     if err != nil {
#         return err
#     }
#     n, err := res.RowsAffected()
#     if err != nil {
#         return err
#     }
#     if n == 0 {
#         return store.ErrNotFound
#     }
#     return nil
# }

# Notes:
# - Use prepared statements or parameterized queries to prevent SQL injection.
# - In production, consider migrations (e.g., golang-migrate) to create the products table.
# - If you prefer, sqlx can simplify scanning into structs.

# 7) Error handling & project structure

# - Unified error handling:
#   - Define domain errors (ErrNotFound) and map to HTTP status codes in handlers.
#   - Use a small error response type if you want structured payloads (e.g., { "error": "...", "code": 404 }).
# - Example error utilities (pkg: internal/errors/errors.go):

# package errors

# import "errors"

# var (
#     ErrNotFound = errors.New("not found")
# )

# - Project structure (suggested):

# project-root/
#   go.mod
#   cmd/
#     api/
#       main.go            // entry point, router wiring
#   internal/
#     models/
#       product.go
#     store/
#       postgres.go        // implements ProductStore
#       store.go           // interface and common errors
#     handler/
#       product.go         // HTTP handlers for /products
#     router/
#       router.go          // optional centralized router
#     config/
#       config.go
#  /pkg/
#     logger.go

# - Packages and import paths:
#   - internal/ for application code (not exported across module boundaries).
#   - handler, store, models, etc., to keep concerns separated.
#   - cmd/api/main.go to initialize dependencies (DB pool, store implementations) and start server.

# Putting it all together: a clean, testable design

# - Use the repository pattern (ProductStore) to swap implementations (Postgres, mock in tests, or in-memory).
# - Validate inputs early in handlers; return meaningful HTTP status codes (400 for invalid input, 404 for not found, 500 for server errors).
# - Use chi for routing, with a minimal middleware stack (Logging, Recoverer).
# - Organize code into obvious packages: models (domain types), store (persistence), handler (HTTP layer), and a main entry in cmd/api.
# - Consider adding pagination for list, transaction boundaries for complex operations, and a migrations tool for DB setup.

# If you’d like, I can tailor the skeleton to your preferred project layout (e.g., clean architecture, or a simpler single-package approach) 
# and provide a runnable scaffold with a Dockerfile and a sample Postgres setup.

# Input tokens: 201
# Output tokens: 6100
# Total tokens: 6301
# -------------------------------------------------- 
# (20250902-criacao-e-tipos-de-prompt) ➜  20250902-criacao-e-tipos-de-prompt git:(20250902-criacao-e-tipos-de-prompt) ✗ 