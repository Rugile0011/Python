--CREATE TABLE carts(
--	id INT PRIMARY KEY,
--  customer_id INT,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL,
--	CONSTRAINT fk_customer
--    	FOREIGN KEY(customer_id)
--			REFERENCES customers(id)
--)

--CREATE TABLE categories(
--	id INT PRIMARY KEY,
--	name VARCHAR(50),
--	description TEXT,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL
--)

--CREATE TABLE categoriesxproducts(
--	category_id INT,
--	product_id INT,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL,
--	CONSTRAINT fk_category
--    	FOREIGN KEY(category_id)
--			REFERENCES categories(id),
--	CONSTRAINT fk_product
--    	FOREIGN KEY(product_id)
--			REFERENCES products(id)
--)

--CREATE TABLE customers(
--	id INT PRIMARY KEY,
--	name VARCHAR(50),
--	email VARCHAR(50),
--	address VARCHAR(50),
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL
--)


--CREATE TABLE orders(
--	id INT PRIMARY KEY,
--  cart_id INT,
--	total_price DECIMAL NOT NULL,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL,
--	CONSTRAINT fk_cart
--    	FOREIGN KEY(cart_id)
--			REFERENCES cart(id)
--)


--CREATE TABLE products(
--	id INT PRIMARY KEY,
--	name VARCHAR(50),
--	price DECIMAL,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL
--)

--CREATE TABLE productxcart(
--	id INT PRIMARY KEY,
--	product_id INT,
--	cart_id INT,
--	created_at TIMESTAMP NOT NULL,
--	updated_at TIMESTAMP NOT NULL,
--	CONSTRAINT fk_product
--    	FOREIGN KEY(product_id)
--			REFERENCES products(id),
--	CONSTRAINT fk_cart
--    	FOREIGN KEY(cart_id)
--			REFERENCES cart(id)
--)


--INSERT INTO carts(id, created_at, updated_at, customer_id)
--VALUES (1, '2022-06-25 10:06:06', '2022-06-26 08:06:06', 2);

--INSERT INTO categories(id, name, description, created_at, updated_at)
--VALUES (2, 'cut flowers', 'freshly picked flowers for any festival', '2022-06-30 04:06:06', '2022-07-01 08:06:06');

--INSERT INTO categoriesxproducts(category_id, product_id, created_at, updated_at)
--VALUES (1, 2, '2022-07-07 10:06:06', '2022-07-07 08:06:06');

--INSERT INTO customers(id, name, email, address, created_at, updated_at)
--VALUES (1, 'Tom', 'tom@gmail.com', '3152 Parker Drive', '2022-06-30 04:06:06', '2022-07-01 08:06:06');

--INSERT INTO orders(id, cart_id, total_price, created_at, updated_at)
--VALUES (1, 1, '37.90', '2022-06-25 10:06:06', '2022-06-26 08:06:06');

--INSERT INTO products(id, name, price, created_at, updated_at)
--VALUES (1, 'bouquet of carnations and daisies', '37.90', '2022-06-25 10:06:06', '2022-06-26 08:06:06');

--INSERT INTO productxcart(product_id, cart_id, created_at, updated_at)
--VALUES (6, 2, '2022-07-08 10:06:06', '2022-07-08 010:06:06');



-- -- SELECT name, email, created_at FROM customers WHERE created_at >  CURRENT_DATE - INTERVAL '1 months' ORDER BY email DESC NULLS LAST
-- -- SELECT id, total_price FROM orders ORDER BY total_price DESC LIMIT 10
-- -- SELECT SUM(total_price) FROM orders WHERE created_at >  CURRENT_DATE - INTERVAL '1 months'
-- SELECT id, customer_id, created_at FROM orders WHERE customer_id IN (2) ORDER BY created_at DESC
--SELECT customers.id, customers.name, products.name FROM customers, products WHERE
--customers.name LIKE 'J%' AND products.name LIKE '%cup%'



