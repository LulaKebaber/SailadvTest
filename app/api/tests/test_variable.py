import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestVariableEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.new_system = self.client.post("/api/system", json={"name": "new_system"})
        self.new_system_id = self.new_system.json()["id"]
        self.new_variable = self.client.post("/api/variable", json={
            "system_id": self.new_system_id,
            "name": "new_variable",
            "type": "string"
        })
        self.new_variable_id = self.new_variable.json()["id"]

    def test_add_new_variable(self):
        data = {"system_id": self.new_system_id, "name": "new_variable", "type": "string"}
        response = self.client.post("/api/variable", json=data)

        assert response.status_code == 201
        assert "id" and "name" and "type" and "system_id" in response.json()
        assert response.json()["name"] == "new_variable"
        assert response.json()["type"] == "string"
        assert response.json()["system_id"] == self.new_system_id

    def test_get_variables(self):
        response = self.client.get("/api/variable")

        assert response.status_code == 200
        assert "variables" in response.json()

    def test_delete_variable_by_id(self):
        response = self.client.delete(f"/api/variable/{self.new_variable_id}")

        assert response.status_code == 200
        assert response.json()["message"] == f"Variable with id {self.new_variable_id} was deleted"

    def test_delete_non_existing_variable(self):
        response = self.client.delete(f"/api/variable/0")

        assert response.status_code == 404
        assert response.json()["detail"] == "Variable not found"

    def test_update_variable(self):
        data = {"system_id": self.new_system_id, "name": "updated_variable", "type": "int"}
        response = self.client.put(f"/api/variable/{self.new_variable_id}", json=data)

        assert response.status_code == 200
        assert response.json()["name"] == "updated_variable"
        assert response.json()["type"] == "int"
        assert "id" and "name" and "type" and "system_id" in response.json()

    def test_update_non_existing_variable(self):
        data = {"system_id": self.new_system_id, "name": "updated_variable", "type": "int"}
        response = self.client.put(f"/api/variable/0", json=data)

        assert response.status_code == 404
        assert response.json()["detail"] == "Variable not found"
