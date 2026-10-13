# Loja MP Fish

Projeto simples de e-commerce de peixes, com frontend em HTML/CSS/JS, backend em Flask (Python) e banco de dados PostgreSQL, tudo orquestrado com Docker Compose.

Cada peixe pode ser vendido por vários vendedores (cada um com seu preço e estoque). Na pesquisa:

- buscar um **peixe** mostra os vendedores que vendem esse peixe;
- buscar um **vendedor** mostra os peixes que ele vende.

## Tecnologias

- **Frontend:** HTML, CSS e JavaScript puro
- **Backend:** Python 3.12, Flask, Flask-CORS e psycopg 3
- **Banco de dados:** PostgreSQL 16
- **Infraestrutura:** Docker e Docker Compose

## Arquitetura MVC

| Camada         | Onde fica                                      | O que faz                                                        |
| -------------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| **Model**      | `backend/models/`                              | Conversa com o banco (consultas SQL)                             |
| **View**       | `frontend/` e `backend/views/`                 | O que o usuário vê (HTML/CSS/JS) e o formato JSON da resposta    |
| **Controller** | `backend/controllers/`                         | Recebe a requisição, pede os dados ao Model e responde pela View |

Fluxo de uma pesquisa:

```
Navegador (View) -> Controller -> Model -> Banco
                         |
                         v
                  View (JSON) -> Navegador mostra os cards
```

## Estrutura do projeto

```
.
├── backend/
│   ├── app.py                       # Cria o Flask e registra os controllers
│   ├── config.py                    # Configurações do banco
│   ├── database.py                  # Função que abre a conexão com o Postgres
│   ├── models/
│   │   ├── product_model.py         # Busca peixe + vendedor
│   │   └── user_model.py            # Lista vendedores
│   ├── controllers/
│   │   ├── product_controller.py    # Rota /products
│   │   └── user_controller.py       # Rota /users
│   ├── views/
│   │   ├── product_view.py          # Monta o JSON dos produtos
│   │   └── user_view.py             # Monta o JSON dos usuários
│   ├── requirements.txt
│   └── Dockerfile
├── database/
│   └── init.sql                     # Tabelas e dados iniciais
├── frontend/
│   ├── index.html
│   ├── script.js                    # Consome a API e monta os cards
│   ├── style.css
│   └── imgs/                        # Imagens dos peixes e logo
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

| Método | Rota                       | Descrição                                                                          |
| ------ | -------------------------- | ---------------------------------------------------------------------------------- |
| GET    | `/`                        | Verifica se a API está funcionando                                                 |
| GET    | `/products`                | Lista todas as ofertas (peixe + vendedor)                                          |
| GET    | `/products?search=<texto>` | Busca pelo nome do peixe **ou** do vendedor (ignora maiúsculas, minúsculas e acentos) |
| GET    | `/users`                   | Lista os vendedores e quantos peixes cada um vende                                 |

Exemplo de resposta de `/products?search=tilapia`:

```json
{
  "products": [
    {
      "id": 7,
      "product_id": 3,
      "name": "Tilápia",
      "description": "Filé de tilápia fresco...",
      "image": "tilapa.png",
      "price": "27.50",
      "stock": 20,
      "seller_id": 3,
      "seller": "Carlos do Rio"
    }
  ]
}
```

## Banco de dados

As tabelas são criadas automaticamente na primeira execução pelo `database/init.sql`, já com 4 vendedores e 6 peixes cadastrados.

```
users ──< user_products >── products
```

**users** (vendedores)

| Campo   | Tipo                |
| ------- | ------------------- |
| `id`    | SERIAL (PK)         |
| `name`  | VARCHAR(100)        |
| `email` | VARCHAR(150) único  |

**products** (catálogo de peixes)

| Campo         | Tipo         |
| ------------- | ------------ |
| `id`          | SERIAL (PK)  |
| `name`        | VARCHAR(100) |
| `description` | TEXT         |
| `image`       | VARCHAR(100) |

**user_products** (quem vende o quê, com preço e estoque de cada vendedor)

| Campo        | Tipo                    |
| ------------ | ----------------------- |
| `id`         | SERIAL (PK)             |
| `user_id`    | INTEGER (FK → users)    |
| `product_id` | INTEGER (FK → products) |
| `price`      | DECIMAL(10, 2)          |
| `stock`      | INTEGER                 |

Um peixe pode ter vários vendedores e um vendedor pode vender vários peixes (relação muitos-para-muitos). Cada par vendedor + peixe só pode aparecer uma vez.

## Observações

- As credenciais do banco (`postgres` / `postgres`) são valores padrão em `backend/config.py` e no `docker-compose.yml`. Use apenas para desenvolvimento.
- O script `init.sql` só roda quando o volume do banco é criado. **Se você já tinha subido o projeto antes, recrie o banco** para as novas tabelas existirem:

  ```bash
  docker compose down -v
  docker compose up -d --build
  ```

## Autor

Miguel Perino | João Pedro Magri
