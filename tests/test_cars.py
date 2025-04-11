import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
id = 0

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_car(client):
    response = client.post("/cars", json={"make": "Toyota", "model": "Corolla", "year": 2020})
    global id
    id = response.json["id"]
    assert response.status_code in [200, 201]

def test_get_all_cars(client):
    response = client.get("/cars")
    assert response.status_code == 200

def test_get_car_with_id(client):
    response = client.get(f"/cars/{id}")
    data = response.json
    print(data)
    assert data["model"] == "Corolla"

def test_update_car(client):
    response = client.put(f"/cars/{id}", json={"make": "Honda", "model": "Civic", "year": 2021})
    assert response.status_code in [200, 404]

def test_delete_car(client):
    response = client.delete(f"/cars/{id}")
    assert response.status_code in [200, 404]
