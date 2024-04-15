import pytest
from fastapi.testclient import TestClient
from src.project_managment.main import app
from uuid import uuid4

client = TestClient(app)

def test_worker_routes():
    worker_id = uuid4()  
    project_id = uuid4()  
    skill_id = uuid4()  

    
    worker = {"name": "Updated Worker", "role": "ADMIN"}  
    response = client.put(f"/workers/{worker_id}", json=worker)  
    assert response.status_code == 200
    assert response.json()["name"] == worker["name"]
    assert response.json()["role"] == worker["role"]

    
    response = client.delete(f"/workers/{worker_id}")  
    assert response.status_code == 204

    
    response = client.put(f"/workers/{worker_id}/add_to_project/{project_id}")  
    assert response.status_code == 200

    
    response = client.put(f"/workers/{worker_id}/add_skill/{skill_id}")  
    assert response.status_code == 200

    
    response = client.put(f"/workers/{worker_id}/remove_from_project/{project_id}")  
    assert response.status_code == 200

    
    response = client.put(f"/workers/{worker_id}/remove_skill/{skill_id}")  
    assert response.status_code == 200
    
def main():
    test_worker_routes()

if __name__ == "__main__":
    main()