from database import get_connection


def search_offers(search=""):
    """Busca as ofertas (peixe + vendedor).

    Uma oferta é um peixe sendo vendido por um usuário, com o preço e
    o estoque dele. A busca olha o nome do peixe E o nome do vendedor
    """
    pattern = f"%{search}%"

    query = """
        SELECT user_products.id,
               products.id   AS product_id,
               products.name,
               products.description,
               products.image,
               user_products.price,
               user_products.stock,
               users.id      AS seller_id,
               users.name    AS seller
        FROM user_products
        JOIN products ON products.id = user_products.product_id
        JOIN users    ON users.id    = user_products.user_id
        WHERE unaccent(products.name) ILIKE unaccent(%s)
           OR unaccent(users.name)    ILIKE unaccent(%s)
        ORDER BY products.name, users.name
    """

    with get_connection() as connection:
        return connection.execute(query, (pattern, pattern)).fetchall()
