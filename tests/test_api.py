from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "W12 MLOps ML API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={
            "features": [5.1, 3.5, 1.4, 0.2],
        },
    )

    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in {
        "setosa",
        "versicolor",
        "virginica",
    }


def test_prediction_rejects_wrong_number_of_features():
    response = client.post(
        "/predict",
        json={
            "features": [5.1, 3.5, 1.4],
        },
    )

    assert response.status_code == 422


def test_prediction_rejects_too_many_features():
    response = client.post(
        "/predict",
        json={
            "features": [5.1, 3.5, 1.4, 0.2, 9.9],
        },
    )

    assert response.status_code == 422
