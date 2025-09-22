from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_crear_usuario():
    response = client.post("/usuarios/", json={"nombre":"Hernan", "email":"hernan@test.com"})
    assert response.status_code == 200
    assert response.json()["nombre"] == "Hernan"

def test_crear_turno():
    # Primero crear usuario
    client.post("/usuarios/", json={"nombre":"Test", "email":"test@test.com"})
    response = client.post("/turnos/", json={"fecha_hora":"2025-09-21T10:00:00","usuario_id":1})
    assert response.status_code == 200
    assert response.json()["usuario_id"] == 1
