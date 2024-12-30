from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={
        "titulo": "Minha primeira tarefa",
        "descricao": "Descrição da tarefa",
        "estado": "pendente"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Minha primeira tarefa"
    assert data["estado"] == "pendente"

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert "titulo" in data
    assert "estado" in data

def test_update_task():
    response = client.put("/tasks/1", json={
        "titulo": "Tarefa atualizada",
        "descricao": "Descrição atualizada",
        "estado": "concluída"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Tarefa atualizada"
    assert data["estado"] == "concluída"

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 204
