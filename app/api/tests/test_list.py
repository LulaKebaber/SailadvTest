import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestListEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.system_1 = self.client.post("/api/system", json={"name": "system_1"})
        self.system_2 = self.client.post("/api/system", json={"name": "system_2"})
        self.system_1_id = self.system_1.json()["id"]
        self.system_2_id = self.system_2.json()["id"]
        self.variable_1 = self.client.post("/api/variable", json={
            "system_id": self.system_1_id,
            "name": "variable_1",
            "type": "string"
        })
        self.variable_2 = self.client.post("/api/variable", json={
            "system_id": self.system_1_id,
            "name": "variable_2",
            "type": "int"
        })
        self.variable_3 = self.client.post("/api/variable", json={
            "system_id": self.system_2_id,
            "name": "variable_3",
            "type": "string"
        })
        self.variable_1_id = self.variable_1.json()["id"]
        self.variable_2_id = self.variable_2.json()["id"]
        self.variable_3_id = self.variable_3.json()["id"]

    def test_get_systems_with_variables(self):
        response = self.client.get("/api/list")

        assert response.status_code == 200
