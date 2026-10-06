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


@app.route("/")
def home():
    return {"message": "funcionando"}

    
#aqui vamos fazer a rota pro flask consultar o bd podemos chamar pelo localhost:5000/products
@app.route("/products")
def products():
    #tem que ter a connection com o banco, o cursor, e ai  a gente pode fazer qualquer acao
    #da pra dar o select all, depoiis lembrar de fechar o cursor e a connection e retornar o prodfucts
    #depois disso salva o arquivo e roda novamnete o docker compose up -d --build

    connection = get_connection()
    cursor = connection.cursor()

    search = request.args.get("search") #QUERY PARAMETER - diferentes infos na hora da req
    #request recebe o fetch(requisicao) do js, o .args é onde pega o query parameters
    
    if search:
        cursor.execute(
            """
            SELECT * FROM products
            WHERE name ILIKE %s
            """,
            (f"%{search}%",)
        )
    else:
        cursor.execute("SELECT * FROM products LIMIT 3")

    products = cursor.fetchall()
    products = [
        {
            "id": product[0],
            "name": product[1],
            "description": product[2],
            "price": product[3],
            "stock": product[4]
        }
        for product in products
    ]
    cursor.close()
    connection.close()

    return {
        "products": products
    }

# @app.route("/product/<int:id>")
# def search(id):
#     connection = get_connection()
#     cursor = connection.cursor()

#     cursor.execute(
#         "SELECT * FROM products WHERE id = %s",
#         (id,)
#     )

#     product = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return {
#         "product": product
#     }
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)