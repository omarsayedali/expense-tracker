-- 1. Create a table for clients
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    budget INT
);

-- 2. Add a fake client
INSERT INTO clients (name, email, budget) 
VALUES ('Mostaql Client', 'client@mostaql.com', 500);

-- 3. Show me the money
SELECT * FROM clients;