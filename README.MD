# Desafio Técnico Sparta - Desenvolvedor Backend Júnior

Esta é uma implementação da API REST para o cálculo de taxas de administração de fundos de investimento, conforme especificado no desafio técnico.

## Como Rodar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Danielmadr/backend-sparta-challenge
    cd sparta-challenge
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    A API estará disponível em `http://127.0.0.1:8000`.

## Como Rodar Localmente (com Docker)

Este projeto está containerizado com Docker, garantindo um ambiente de execução consistente e isolado.

**Pré-requisitos:**
*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem com o Docker Desktop)

### 1. Suba o container
Na raiz do projeto, execute o seguinte comando:
```bash
docker-compose up --build
```
*   O `--build` é necessário na primeira vez para construir a imagem. Nas próximas, você pode usar apenas `docker-compose up`.
*   A API estará disponível em `http://127.0.0.1:8000`.
*   Graças ao `volume` e ao `--reload`, você pode editar o código Python e as mudanças serão aplicadas automaticamente sem precisar reiniciar o container.

Para parar o container, pressione `Ctrl+C` no terminal e depois execute `docker-compose down`.

## Documentação e testes

Documentação interativa da API em `http://127.0.0.1:8000/docs` para testar o endpoint.

## Decisões Técnicas

*   **Linguagem:** Optei por **Python**, conforme a preferência indicada no desafio.
*   **Framework:** Utilizei **FastAPI** por sua alta performance, validação de dados nativa com Pydantic (o que garante a integridade do input) e geração automática de documentação interativa (Swagger UI).
*   **Otimização de Cálculo:** Para atender ao requisito de performance com grandes volumes de dados (N e M grandes), o cálculo principal foi implementado com a biblioteca **NumPy**. A vetorização da fórmula evita o uso de loops Python aninhados, delegando as operações matemáticas a rotinas de baixo nível (em C), o que resulta em uma performance superior.