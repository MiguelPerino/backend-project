import psycopg
from psycopg.rows import dict_row

import config


def get_connection():
    """Abre uma conexão com o Postgres.

    Com dict_row, cada linha do banco volta como dicionário
    (row["name"]) em vez de tupla (row[1]).
    """
    return psycopg.connect(
        host=config.DB_HOST,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        row_factory=dict_row,
    )
