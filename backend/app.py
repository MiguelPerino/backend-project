import psycopg
from flask import Flask
from flask_cors import CORS

from controllers.product_controller import product_bp
from controllers.user_controller import user_bp

app = Flask(__name__)

# Permite que o frontend (outra origem) converse com esta API
CORS(app)

# Registra as rotas de cada controller
app.register_blueprint(product_bp)
app.register_blueprint(user_bp)


@app.route("/")
def home():
    return {"message": "funcionando"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
