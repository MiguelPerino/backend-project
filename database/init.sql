CREATE EXTENSION IF NOT EXISTS unaccent;



CREATE TABLE users (
    id    SERIAL PRIMARY KEY,
    name  VARCHAR(100) NOT NULL
);



CREATE TABLE products (
    id  SERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    description TEXT,
    image   VARCHAR(100)
);


-- USER_PRODUCTS (quem vende o quê)

CREATE TABLE user_products (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users(id)    ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    price      DECIMAL(10, 2) NOT NULL,
    stock      INTEGER NOT NULL,
    UNIQUE (user_id, product_id)
);



INSERT INTO users (name)
VALUES
    ('João Pedro'),
    ('Maria'),
    ('Miguel'),
    ('Cleitin');

INSERT INTO products (name, description, image)
VALUES
    ('Salmão',   'Filé de salmão fresco, vindo diretamente dos alpes chilenos.',                                       'salmao.png'),
    ('Pirarara', 'Pirarara fresca, de carne saborosa e ótima para assados.',                                           'pirara.png'),
    ('Tilápia',  'Filé de tilápia fresco, pode comprar o tanto que quiser que tem de sobra, esse ai nasce de monte.', 'tilapa.png'),
    ('Piranha',  'Peixe piranha fresco',                                                                               'piranha.jpeg'),
    ('Pacu',     'Peixe pacu fresco',                                                                                  'pacu.jpeg'),
    ('Traíra',   'Peixe traíra fresco',                                                                                'traira.jpeg');

-- Os ids abaixo seguem a ordem dos INSERTs acima:
--   usuários: 1 João, 2 Maria, 3 Carlos, 4 Ana
--   produtos: 1 Salmão, 2 Pirarara, 3 Tilápia, 4 Piranha, 5 Pacu, 6 Traíra
INSERT INTO user_products (user_id, product_id, price, stock)
VALUES
    -- João vende Salmão, Tilápia e Pacu
    (1, 1, 59.90, 10),
    (1, 3, 29.90, 15),
    (1, 5, 45.00, 10),

    -- Maria vende Salmão, Pirarara e Traíra
    (2, 1, 62.00,  6),
    (2, 2, 34.90,  8),
    (2, 6, 40.00,  8),

    -- Carlos vende Tilápia, Piranha e Pacu
    (3, 3, 27.50, 20),
    (3, 4, 35.00, 12),
    (3, 5, 47.00,  7),

    -- Ana vende Pirarara, Piranha e Traíra
    (4, 2, 36.00,  5),
    (4, 4, 33.00,  9),
    (4, 6, 41.50,  4);
