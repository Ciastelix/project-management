import pytest
from fastapi.testclient import TestClient
from src.project_managment.main import app
from uuid import uuid4

client = TestClient(app)

def test_skill_routes():
    skill_id = uuid4()  
    worker_id = uuid4()  

    
    response = client.get("/skills")  
    assert response.status_code == 200

    
    skill = {"name": "Test Skill", "description": "This is a test skill"}  
    response = client.post("/skills", json=skill)  
    assert response.status_code == 201
    assert response.json()["name"] == skill["name"]
    assert response.json()["description"] == skill["description"]

    
    response = client.get(f"/skills/{skill_id}")  
    assert response.status_code == 200

    
    skill = {"name": "Updated Skill", "description": "This is an updated test skill"}  
    response = client.put(f"/skills/{skill_id}", json=skill)  
    assert response.status_code == 200
    assert response.json()["name"] == skill["name"]
    assert response.json()["description"] == skill["description"]

    
    response = client.delete(f"/skills/{skill_id}")  
    assert response.status_code == 204

    
    response = client.put(f"/skills/{skill_id}/add_to_skill/{worker_id}")  
    assert response.status_code == 200

    
    response = client.put(f"/skills/{skill_id}/remove_from_skill/{worker_id}")  
    assert response.status_code == 200
    
def main():
    test_skill_routes()
    
if __name__ == "__main__":
    main()