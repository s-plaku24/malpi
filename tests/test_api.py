# tests/test_api.py
import os
os.environ["API_TOKEN"] = "test-token"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction_works():
    """Test that the prediction endpoint works correctly"""
    flower_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    
    response = client.post(
        "/predict",
        json=flower_data,
        headers={"X-API-Token": "test-token"}
    )
    
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_auth_required():
    """Test that authentication is required"""
    response = client.post("/predict", json={})
    assert response.status_code == 401