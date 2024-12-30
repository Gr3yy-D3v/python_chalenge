# Projeto FastAPI - Tarefas

Este projeto é uma API RESTful construída com **FastAPI** e **SQLAlchemy** para gerenciar tarefas. Ele inclui operações CRUD (Criar, Ler, Atualizar e Deletar) e validações de dados usando **Pydantic**.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.8+**: A API foi desenvolvida e testada com Python 3.8 ou superior.
- **pip**: O gerenciador de pacotes do Python para instalar as dependências.

## Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
### 2. Crie e ative um ambiente virtual
Para criar o ambiente virtual, execute:

```bash
python -m venv venv
```
**ative o ambiente virtual**

- **Windows:**
    ```
    venv\Scripts\activate
    ```
- **Linux/macOS:**
    ```
    source venv/bin/activate
    ```

### 3. Instale as dependências
Use o **pip** para instalar as dependências do projeto
````
pip install -r requirements.txt
````
### Rodando a aplicação
Com as dependências instaladas e o ambiente virtual ativado, você pode iniciar a aplicação localmente com o **Uvicorn**
### 1. Execute o servidor
Para rodar a aplicação, execute:
````
pip install pytest httpx
````
### Estrutura do Projeto

project/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Código da aplicação FastAPI
│   ├── database.py      # Configurações do banco de dados
│   ├── models.py        # Modelos do banco de dados (SQLAlchemy)
│   ├── schemas.py       # Pydantic schemas para validação
│   ├── crud.py          # Lógica de acesso ao banco de dados
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_api.py      # Testes da API FastAPI
│   └── ...
├── requirements.txt     # Dependências do projeto
├── README.md            # Este arquivo
└── ...

### Detalhes da API
A API tem os seguintes endpoints:
### 1. Criar nova tarefa
- Post ````/tasks/````
- Corpo:
    ````
    {
    "titulo": "Título da Tarefa",
    "descricao": "Descrição opcional",
    "estado": "pendente"
    }
    ````
### 2. listar todas as tarefas
- GET ````/tasks/````
### 3. Visualizar uma tarefa específica pelo ID
- GET ````/tasks/{id}/````
### 4. Atualizar uma tarefa existente
- PUT ````/tasks/{id}/````
- Corpo 
    ````
    {
  "titulo": "Novo Título",
  "descricao": "Nova Descrição",
  "estado": "em andamento"
    }
    ````
### 5. Deletar uma tarefa
- DELETE ````/tasks/{id}/````
### Problemas comuns
### 1. Erros de importação
Se você encontrar um erro relacionado ao módulo ````database```` ou outros, verifique se o arquivo ````database.py```` está presente e corretamente configurado.
### 2. Banco de Dados Não Criado
Certifique-se de que o banco de dados está sendo criado corretamente e que o SQLAlchemy está configurado para usar o banco de dados local.