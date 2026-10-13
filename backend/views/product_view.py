def render_products(offers):
    """Monta o JSON de resposta da lista de produtos."""
    return {
        "products": [
            {
                "id": offer["id"],
                "product_id": offer["product_id"],
                "name": offer["name"],
                "description": offer["description"],
                "image": offer["image"],
                "price": str(offer["price"]),
                "stock": offer["stock"],
                "seller_id": offer["seller_id"],
                "seller": offer["seller"],
            }
            for offer in offers
        ]
    }
