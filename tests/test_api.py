import os
# Set up environment variable for testing BEFORE importing the app
os.environ["API_TOKEN"] = "test-secret"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

valid_payload = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

def test_predict_success():
    response = client.post(
        "/predict",
        json=valid_payload,
        headers={"X-API-Token": "test-secret"}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid_token():
    response = client.post(
        "/predict",
        json=valid_payload,
        headers={"X-API-Token": "wrong-token"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Unauthorized"

def test_predict_missing_field():
    incomplete_payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4
    }
    response = client.post(
        "/predict",
        json=incomplete_payload,
        headers={"X-API-Token": "test-secret"}
    )
    assert response.status_code == 422

def test_predict_invalid_data_type():
    invalid_payload = {
        "sepal_length": "invalid",
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post(
        "/predict",
        json=invalid_payload,
        headers={"X-API-Token": "test-secret"}
    )
    assert response.status_code == 422