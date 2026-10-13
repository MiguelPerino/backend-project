from database import get_connection


def list_sellers():
    """Lista os usuários e quantos peixes cada um vende."""
    query = """
        SELECT users.id,
               users.name,
               COUNT(user_products.id) AS products_count
        FROM users
        LEFT JOIN user_products ON user_products.user_id = users.id
        GROUP BY users.id, users.name
        ORDER BY users.name
    """

    with get_connection() as connection:
        return connection.execute(query).fetchall()
