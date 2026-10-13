import os

# Configurações do banco de dados.
# Os valores padrão funcionam com o docker-compose.yml.
# "db" é o nome do serviço do Postgres no docker-compose (rede interna do Docker).
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "ecommerce")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
