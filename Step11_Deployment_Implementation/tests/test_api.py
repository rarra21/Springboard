from app.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert response.json["model_loaded"] is True


def test_prediction_endpoint_success():
    client = app.test_client()
    payload = {
        "station_id": "1001",
        "flow": 120,
        "occupancy": 0.08,
        "speed": 60,
        "hour": 8,
        "dayofweek": 2,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction_speed_60min_ahead" in response.json
    assert "latency_ms" in response.json


def test_prediction_endpoint_validation_error():
    client = app.test_client()
    response = client.post("/predict", json={"speed": 60})
    assert response.status_code == 400
    assert "error" in response.json
