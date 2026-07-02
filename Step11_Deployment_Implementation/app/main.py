"""Production-style Flask app for PeMS traffic speed prediction.

Endpoints:
- GET /health: service health check
- GET /model-info: model artifact and training metrics
- POST /predict: JSON prediction API
- GET / and POST /ui-predict: lightweight browser UI
"""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "traffic_speed_svr_pipeline.pkl"
METRICS_PATH = ROOT / "models" / "model_metrics.json"
LOG_PATH = ROOT / "logs" / "app.log"
FEATURES = ["station_id", "flow", "occupancy", "speed", "hour", "dayofweek"]

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

app = Flask(__name__)
model = joblib.load(MODEL_PATH)


def validate_payload(payload: dict[str, Any]) -> pd.DataFrame:
    """Validate request payload and return one-row prediction dataframe."""
    missing = [field for field in FEATURES if field not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")

    row = {
        "station_id": str(payload["station_id"]),
        "flow": float(payload["flow"]),
        "occupancy": float(payload["occupancy"]),
        "speed": float(payload["speed"]),
        "hour": int(payload["hour"]),
        "dayofweek": int(payload["dayofweek"]),
    }

    if not 0 <= row["hour"] <= 23:
        raise ValueError("hour must be between 0 and 23")
    if not 0 <= row["dayofweek"] <= 6:
        raise ValueError("dayofweek must be between 0 and 6")
    if row["flow"] < 0:
        raise ValueError("flow must be non-negative")
    if row["occupancy"] < 0:
        raise ValueError("occupancy must be non-negative")
    if row["speed"] < 0:
        raise ValueError("speed must be non-negative")

    return pd.DataFrame([row], columns=FEATURES)


@app.get("/")
def home():
    """Render the browser UI."""
    return render_template("index.html", prediction=None, error=None)


@app.get("/health")
def health():
    """Return application health and model status."""
    return jsonify({"status": "ok", "model_loaded": MODEL_PATH.exists()})


@app.get("/model-info")
def model_info():
    """Return model training metadata and metrics."""
    if METRICS_PATH.exists():
        return jsonify(json.loads(METRICS_PATH.read_text(encoding="utf-8")))
    return jsonify({"message": "metrics file not available"})


@app.post("/predict")
def predict():
    """Predict traffic speed 60 minutes ahead from JSON input."""
    start = time.time()
    try:
        payload = request.get_json(force=True)
        X = validate_payload(payload)
        prediction = float(model.predict(X)[0])
        latency_ms = round((time.time() - start) * 1000, 3)
        logging.info(
            "prediction_success latency_ms=%s payload=%s prediction=%s",
            latency_ms,
            payload,
            prediction,
        )
        return jsonify(
            {
                "prediction_speed_60min_ahead": prediction,
                "latency_ms": latency_ms,
            }
        )
    except Exception as exc:  # intentional API boundary error handling
        latency_ms = round((time.time() - start) * 1000, 3)
        logging.exception("prediction_error latency_ms=%s error=%s", latency_ms, str(exc))
        return jsonify({"error": str(exc), "latency_ms": latency_ms}), 400


@app.post("/ui-predict")
def ui_predict():
    """Return a prediction through the browser form."""
    try:
        X = validate_payload(request.form.to_dict())
        prediction = round(float(model.predict(X)[0]), 2)
        return render_template("index.html", prediction=prediction, error=None)
    except Exception as exc:
        return render_template("index.html", prediction=None, error=str(exc))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
