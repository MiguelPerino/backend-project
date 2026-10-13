def render_users(users):
    """Monta o JSON de resposta da lista de usuários."""
    return {
        "users": [
            {
                "id": user["id"],
                "name": user["name"],
                "products_count": user["products_count"],
            }
            for user in users
        ]
    }
