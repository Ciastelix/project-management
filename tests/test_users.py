import pytest
from fastapi.testclient import TestClient
from src.project_managment.main import app
from uuid import uuid4

client = TestClient(app)

def test_user_routes():
    user_id = uuid4()  

    
    user = {"username": "testuser", "password": "testpassword"}  
    response = client.post("/users", json=user)  
    assert response.status_code == 201
    assert response.json()["username"] == user["username"]

    
    response = client.get(f"/users/{user_id}")  
    assert response.status_code == 200

    
    user = {"username": "updateduser", "password": "updatedpassword"}  
    response = client.put(f"/users/{user_id}", json=user)  
    assert response.status_code == 200
    assert response.json()["username"] == user["username"]

    
    response = client.delete(f"/users/{user_id}")  
    assert response.status_code == 204

    
    user = {"username": "testuser", "password": "testpassword"}  
    response = client.post("/users/login", data=user)  
    assert response.status_code == 200
    
def main():
    test_user_routes()
    
if __name__ == "__main__":
    main()