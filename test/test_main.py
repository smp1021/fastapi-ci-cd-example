from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_saludo_default():
    # Prueba el endpoint SIN enviar un nombre
    response = client.get("/saludo")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola, Mundo"}


def test_read_saludo_with_name():
    # Prueba el endpoint ENVIANDO un nombre
    response = client.get("/saludo?nombre=Gemini")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola, Gemini"}
