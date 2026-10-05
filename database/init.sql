CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO products (name, description, price, stock)
VALUES
    ('Salmão', 'Filé de salmão fresco, vindo diretamente dos alpes chilenos.', 59.90, 10),
    ('Pirarara', 'Pirarara fresca, de carne saborosa e ótima para assados.', 34.90, 8),
    ('Tilápia', 'Filé de tilápia fresco, pode comprar o tanto que quiser que tem de sobra, esse ai nasce de monte.', 29.90, 15);