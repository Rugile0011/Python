# Task
Let’s create a database for an e-shop! We must have an ER diagram so that we would understand what is the structure of the tables. Later on, let’s create those tables, insert example entries, and prepare queries for the work. The main tasks:

1. Firstly - create an ER diagram for your structure. Main entities must involve user, product, cart, order. After creating this schema - contact your mentor to confirm it.
 - 1.1. To draw the ER diagrams you can use https://app.diagrams.net (choose Software -> Database 1 as a template)
 - 1.2. Make sure, that your entities have `created_at` field.

2. After creating schema - let’s start a practical part. Lets start a database:
 - 2.1. Using terminal go to `be-academy/4_postgresql/` directory and run `docker-compose up` to start a local PostgreSQL database instance and PGAdmin4 - browser based database console.
 - 2.2. Go to http://localhost:8080, log in with `admin@example.com` email and `postgres` password. Connect to database `postgres` database using `postgres` username and `postgres` password. Open query editor: ![SQL query editor window](sql_query_editor_window.png "SQL query editor window")
 - 2.3. Create tables from the confirmed schema, and add example entries to the tables. Be sure to save all those queries in some file, we’ll discuss them later.

3. Create statements to query the following use cases:
 - 3.1. Get all users who were created within the last month and sorted by their emails from Z to A order
 - 3.2. Get top 10 biggest orders within the system
 - 3.3. Get a total sum of last month's orders
 - 3.4. Select specific user with all his orders together ordered by order date descending
