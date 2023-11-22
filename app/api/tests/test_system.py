import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestSystemEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.new_system = self.client.post("/api/system", json={"name": "new_system"})
        self.new_system_id = self.new_system.json()["id"]

    def test_add_new_system(self):
        data = {"name": "new_system"}
        response = self.client.post("/api/system", json=data)
        assert response.status_code == 201
        assert "id" and "name" in response.json()
        assert response.json()["name"] == "new_system"

    def test_get_systems(self):
        response = self.client.get("/api/system")
        assert response.status_code == 200
        assert "systems" in response.json()

    def test_update_system(self):
        data = {"name": "updated_system"}
        response = self.client.put(f"/api/system/{self.new_system_id}", json=data)

        assert response.status_code == 200
        assert response.json()["name"] == "updated_system"
        assert "id" and "name" in response.json()

    def test_delete_system_by_id(self):
        response = self.client.delete(f"/api/system/{self.new_system_id}")
        assert response.status_code == 200
        assert response.json()["message"] == f"System with id {self.new_system_id} was deleted"

    def test_delete_non_existing_system(self):
        response = self.client.delete(f"/api/system/0")
        assert response.status_code == 404
        assert response.json()["detail"] == "System not found"

    def test_update_non_existing_system(self):
        data = {"name": "updated_system"}
        response = self.client.put(f"/api/system/0", json=data)
        assert response.status_code == 404
        assert response.json()["detail"] == "System not found"

    def test_add_new_system_with_empty_name(self):
        data = {"name": ""}
        response = self.client.post("/api/system", json=data)
        assert response.status_code == 400
        assert response.json()["detail"] == "Bad request"
