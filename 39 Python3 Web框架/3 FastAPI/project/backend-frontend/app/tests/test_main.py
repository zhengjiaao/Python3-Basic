# app/tests/test_main.py
from fastapi.testclient import TestClient
from ..main import app
from .. import crud, schemas, database

client = TestClient(app)

def test_create_user():
    user_data = {"username": "testuser", "email": "testuser@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]

def test_read_user():
    user_data = {"username": "testuser", "email": "testuser@example.com", "password": "testpassword"}
    response = client.post("/users/", json=user_data)
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]

def test_create_file():
    with open("testfile.txt", "rb") as file:
        response = client.post("/files/", files={"file": file})
    assert response.status_code == 200
    assert response.json()["filename"] == "testfile.txt"

def test_read_file():
    with open("testfile.txt", "rb") as file:
        response = client.post("/files/", files={"file": file})
    file_id = response.json()["id"]
    response = client.get(f"/files/{file_id}")
    assert response.status_code == 200
    assert response.json()["filename"] == "testfile.txt"
