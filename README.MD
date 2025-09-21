# Backend Sparta Challenge

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## Descrição do Projeto

Este projeto é um desafio de backend que implementa um serviço para calcular taxas administrativas por cotista. Ele oferece duas abordagens para o cálculo: uma implementação de força bruta e outra otimizada utilizando a biblioteca NumPy para processamento eficiente de dados.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **FastAPI:** Framework web moderno e rápido para construir APIs.
*   **NumPy:** Biblioteca para computação numérica de alto desempenho, utilizada na versão otimizada do cálculo.
*   **Pydantic:** Para validação de dados e serialização.
*   **Docker & Docker Compose:** Para conteinerização e orquestração da aplicação, facilitando o ambiente de desenvolvimento e deploy.

## Estrutura do Projeto

```
. 
├── app
│   ├── main.py
│   └── services
│       ├── calculator_brute_force.py
│       └── calculator_numpy.py
├── data
│   ├── test_data_stakeholders_100k_days_30.json
│   └── test_data_stakeholders_40_days_30.json
├── tests
|   └── test_endpoints.py
├── docker-compose.yml
├── Dockerfile
├── README.MD
└── requirements.txt
```
## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

### Com Docker Compose

1.  Clone o repositório:
    ```bash
    git clone https://github.com/Danielmadr/backend-sparta-challenge
    cd backend-sparta-challenge
    ```
2.  Suba os serviços com Docker Compose:
    ```bash
    docker-compose up --build
    ```
    A aplicação estará disponível em `http://localhost:8000`.

### Diretamente (sem Docker)

1.  Clone o repositório e navegue até o diretório:
    ```bash
    git clone https://github.com/Danielmadr/backend-sparta-challenge
    cd backend-sparta-challenge
    ```
2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Execute a aplicação com Uvicorn:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    A aplicação estará disponível em `http://localhost:8000`.

## Endpoints da API

### 1. Raiz da API

*   **URL:** `/`
*   **Método:** `GET`
*   **Descrição:** Retorna informações básicas sobre o sistema.
*   **Resposta de Exemplo:**
    ```json
    {
        "System": "Backend Sparta Challenge",
        "Version": "1.0.0"
    }
    ```

### 2. Calcular Taxa Administrativa por Cotista (NumPy)

*   **URL:** `/calcular-taxa-administrativa-por-cotista`
*   **Método:** `POST`
*   **Descrição:** Calcula a taxa administrativa por cotista utilizando a implementação otimizada com NumPy.
*   **Corpo da Requisição (Exemplo):**
    ```json
    {
        "taxa": 0.005,
        "cotas": [
            {
                "valor": 100.0,
                "quantidades": [10.0, 20.0]
            },
            {
                "valor": 101.0,
                "quantidades": [10.5, 20.5]
            }
        ]
    }
    ```
*   **Resposta de Exemplo:**
    ```json
    [0.12345, 0.24690]
    ```
*   **Exemplo `curl`:**
    ```bash
    curl -X POST "http://localhost:8000/calcular-taxa-administrativa-por-cotista" \
         -H "Content-Type: application/json" \
         -d '{"taxa": 0.005, "cotas": [{"valor": 100.0, "quantidades": [10.0, 20.0]}, {"valor": 101.0, "quantidades": [10.5, 20.5]}]}'
    ```

### 3. Calcular Taxa Administrativa por Cotista (Força Bruta)

*   **URL:** `/calcular-taxa-administrativa-por-cotista-brute-force`
*   **Método:** `POST`
*   **Descrição:** Calcula a taxa administrativa por cotista utilizando a implementação de força bruta.
*   **Corpo da Requisição e resposta :** Mesmo formato do endpoint anterior
    
## Testes

Para rodar os testes, utilize `pytest`:

```bash
pytest -v
```

## Próximos Passos e Melhorias

- Adicionar tratamento de exceções nos endpoints
- Implementar testes para entradas inválidas e erros

---

*Este projeto foi desenvolvido como parte do processo seletivo da Sparta.*