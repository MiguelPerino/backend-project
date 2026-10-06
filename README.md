# Loja MP Fish

Projeto simples de e-commerce de peixes, com frontend em HTML/CSS/JS, backend em Flask (Python) e banco de dados PostgreSQL, tudo orquestrado com Docker Compose.

## Tecnologias

- **Frontend:** HTML, CSS e JavaScript puro
- **Backend:** Python 3.12, Flask, Flask-CORS e psycopg 3
- **Banco de dados:** PostgreSQL 16
- **Infraestrutura:** Docker e Docker Compose

## Estrutura do projeto

```
.
├── backend/
│   ├── app.py              # API Flask
│   ├── requirements.txt    # Dependências Python
│   └── Dockerfile
├── database/
│   └── init.sql            # Criação da tabela e dados iniciais
├── frontend/
│   ├── index.html
│   ├── script.js           # Consome a API e monta os cards
│   ├── style.css
│   └── imgs/               # Imagens dos peixes e logo
└── docker-compose.yml
```

## Como rodar

Pré-requisito: [Docker](https://www.docker.com/) instalado.

1. Suba o banco e o backend:

   ```bash
   docker compose up -d --build
   ```

2. Abra o arquivo `frontend/index.html` no navegador.

A API fica disponível em `http://localhost:5000` e o PostgreSQL em `localhost:5432`.

Para parar os containers:

```bash
docker compose down
```

## Endpoints da API

| Método | Rota                       | Descrição                                                                  |
| ------ | -------------------------- | -------------------------------------------------------------------------- |
| GET    | `/`                        | Verifica se a API está funcionando                                         |
| GET    | `/products`                | Lista produtos (retorna apenas 3 quando não há busca)                      |
| GET    | `/products?search=<texto>` | Busca produtos pelo nome (sem diferenciar maiúsculas de minúsculas)        |

Exemplo de resposta de `/products`:

```json
{
  "products": [
    {
      "id": 1,
      "name": "Salmão",
      "description": "Filé de salmão fresco, vindo diretamente dos alpes chilenos.",
      "price": "59.90",
      "stock": 10
    }
  ]
}
```

## Banco de dados

A tabela `products` é criada automaticamente na primeira execução pelo `database/init.sql`, já com 6 peixes cadastrados (Salmão, Pirarara, Tilápia, Piranha, Pacu e Traíra).

| Campo         | Tipo           |
| ------------- | -------------- |
| `id`          | SERIAL (PK)    |
| `name`        | VARCHAR(100)   |
| `description` | TEXT           |
| `price`       | DECIMAL(10, 2) |
| `stock`       | INTEGER        |

## Observações

- As credenciais do banco (`postgres` / `postgres`) estão fixas no código e no `docker-compose.yml`. Use apenas para desenvolvimento.
- O script `init.sql` só roda quando o volume do banco é criado. Para recriar os dados, use `docker compose down -v`.

## Autor

Miguel Perino | João Pedro Magri
