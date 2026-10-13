from flask import Flask, request
from flask_cors import CORS
import psycopg#lib pra conectar com postgre

app = Flask(__name__)

CORS(app)   #permite requisicao de outras origens, isso vai servir pra comunicar com o frontend

def get_connection():
    #importante aqui o host=db, por que la no docker compose o servico do postgre chama db
    #entao basicamente cria uma rede interna que faz com que eles se comuniquem atraves do nome do serviço
    return psycopg.connect(	
        host="db",
        dbname="ecommerce",
        user="postgres",
        password="postgres",
    )

#aqui vamos fazer a rota pro flask consultar o bd podemos chamar pelo localhost:5000/products
@app.route("/")
def home():
    return {"message": "funcionando"}


@app.route("/products")
def products():
    connection = get_connection()
    cursor = connection.cursor()

    search = request.args.get("search", "")

    if search:
        cursor.execute(
            """
            SELECT products.id,
                   products.name,
                   products.description,
                   products.price,
                   products.stock,
                   users.name AS seller
            FROM products
            JOIN users ON products.user_id = users.id
            WHERE products.name ILIKE %s
               OR users.name ILIKE %s
            ORDER BY products.id
            """,
            (f"%{search}%", f"%{search}%")
        )
    else:
        cursor.execute(
            """
            SELECT products.id,
                   products.name,
                   products.description,
                   products.price,
                   products.stock,
                   users.name AS seller
            FROM products
            JOIN users ON products.user_id = users.id
            ORDER BY products.id
            """
        )

    rows = cursor.fetchall()

    products = [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "price": str(row[3]),
            "stock": row[4],
            "seller": row[5]
        }
        for row in rows
    ]

    cursor.close()
    connection.close()

    return {"products": products}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
