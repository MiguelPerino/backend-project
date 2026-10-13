from flask import Blueprint

from models import user_model
from views import user_view

user_bp = Blueprint("users", __name__)


@user_bp.route("/users")
def list_users():
    """GET /users

    Pede os vendedores ao model e devolve o JSON pela view.
    """
    users = user_model.list_sellers()

    return user_view.render_users(users)
