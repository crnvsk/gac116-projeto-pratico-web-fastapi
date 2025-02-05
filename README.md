# Projeto Prático Web com FastAPI

Este é um projeto prático desenvolvido com FastAPI para criar uma API backend e um frontend utilizando Vue.js.

## Estrutura do Projeto

- **backend**: Contém o código do servidor FastAPI.
- **frontend**: Contém o código do frontend desenvolvido com Vue.js.

## Requisitos

- Python 3.8+
- Node.js 14+

## Configuração do Backend

1. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

3. Execute o servidor:
    ```sh
    uvicorn main:app --reload
    ```

## Configuração do Frontend

1. Navegue até o diretório [frontend](http://_vscodecontentref_/1):
    ```sh
    cd frontend
    ```

2. Instale as dependências:
    ```sh
    npm install
    ```

3. Execute o servidor de desenvolvimento:
    ```sh
    npm run dev
    ```

## Endpoints da API

### Usuários

- **GET /users/**: Lista todos os usuários.
- **POST /users/**: Cria um novo usuário.
- **PUT /users/{user_id}**: Atualiza um usuário existente.
- **DELETE /users/{user_id}**: Deleta um usuário.

### Receitas

- **GET /users/{user_id}/recipes**: Lista todas as receitas de um usuário.
- **POST /users/{user_id}/recipes/**: Cria uma nova receita para um usuário.

## Estrutura dos Arquivos

### Backend

- `main.py`: Configuração principal do FastAPI.
- [routes.py](http://_vscodecontentref_/2): Definição das rotas da API.
- [models.py](http://_vscodecontentref_/3): Definição dos modelos do banco de dados.
- [schemas.py](http://_vscodecontentref_/4): Definição dos esquemas Pydantic.
- [crud.py](http://_vscodecontentref_/5): Funções CRUD para interagir com o banco de dados.
- [database.py](http://_vscodecontentref_/6): Configuração do banco de dados.

### Frontend

- `src/`: Código fonte do frontend.
- `public/`: Arquivos públicos estáticos.