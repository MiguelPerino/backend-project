from flask import Flask
import psycopg

app = Flask(__name__)


def get_connection():
    #importante aqui o host=db, por que la no docker compose o servico do postgre chama db
    #entao basicamente cria uma rede interna que faz com que eles se comuniquem atraves do nome do serviço
    return psycopg.connect(	
        host="db",
        dbname="ecommerce",
        user="postgres",
        password="postgres"
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
	pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)