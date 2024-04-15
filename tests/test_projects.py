import pytest
from fastapi.testclient import TestClient
from src.project_managment.main import app  
from uuid import uuid4

client = TestClient(app)

def test_project_routes():
    project_id = uuid4()  
    worker_id = uuid4()  

    
    response = client.get("/projects")  
    assert response.status_code == 200

    
    project = {"name": "Test Project", "description": "This is a test project"}  
    response = client.post("/projects", json=project)  
    assert response.status_code == 201
    assert response.json()["name"] == project["name"]
    assert response.json()["description"] == project["description"]

    
    response = client.get(f"/projects/{project_id}")  
    assert response.status_code == 200

    
    project = {"name": "Updated Project", "description": "This is an updated test project"}  
    response = client.put(f"/projects/{project_id}", json=project)  
    assert response.status_code == 200
    assert response.json()["name"] == project["name"]
    assert response.json()["description"] == project["description"]

    
    response = client.delete(f"/projects/{project_id}")  
    assert response.status_code == 204

    
    response = client.put(f"/projects/{project_id}/add_to_project/{worker_id}")  
    assert response.status_code == 200

    
    response = client.put(f"/projects/{project_id}/remove_from_project/{worker_id}")  
    assert response.status_code == 200