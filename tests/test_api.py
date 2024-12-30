from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

# Criar o banco de dados para os testes
Base.metadata.create_all(bind=engine)

# Configurar o cliente de teste
client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={
        "titulo": "Teste Tarefa",
        "descricao": "Descrição da tarefa de teste",
        "estado": "pendente"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Teste Tarefa"
    assert data["estado"] == "pendente"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)

def test_update_task():
    # Primeiro, crie uma tarefa
    response = client.post("/tasks/", json={
        "titulo": "Atualizar Tarefa",
        "descricao": "Descrição antes da atualização",
        "estado": "pendente"
    })
    task_id = response.json()["id"]

    # Atualize a tarefa
    response = client.put(f"/tasks/{task_id}/", json={
        "titulo": "Tarefa Atualizada",
        "descricao": "Descrição depois da atualização",
        "estado": "em andamento"
    })
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["titulo"] == "Tarefa Atualizada"
    assert updated_task["estado"] == "em andamento"

def test_delete_task():
    # Primeiro, crie uma tarefa
    response = client.post("/tasks/", json={
        "titulo": "Excluir Tarefa",
        "descricao": "Tarefa a ser excluída",
        "estado": "pendente"
    })
    task_id = response.json()["id"]

    # Exclua a tarefa
    response = client.delete(f"/tasks/{task_id}/")
    assert response.status_code == 204

    # Verifique se a tarefa foi removida
    response = client.get(f"/tasks/{task_id}/")
    assert response.status_code == 404
