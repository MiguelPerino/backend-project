from flask import Blueprint, request

from models import product_model
from views import product_view

product_bp = Blueprint("products", __name__)


@product_bp.route("/products")
def list_products():
    """GET /products?search=<texto>

    Recebe a pesquisa, pede os dados ao model e devolve o JSON pela view.
    """
    search = request.args.get("search", "").strip()

    offers = product_model.search_offers(search)

    return product_view.render_products(offers)
