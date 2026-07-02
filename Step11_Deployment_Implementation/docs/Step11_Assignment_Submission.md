# Machine Learning Engineering Bootcamp Capstone Project
## Step 11: Deployment Implementation

## Project
Traffic Speed Prediction Using California PeMS Data

## Overview
This step converts the capstone prototype into a production-style application. The implementation includes a trained scikit-learn SVR model artifact, a Flask REST API, a simple browser UI, structured logging, tests, Docker containerization, and clear README instructions.

## Major Components

### Data pipeline
The PeMS sample dataset is stored in `data/sample_pems_data_small.csv`. The training script `src/train_model.py` loads the data, preprocesses it, tunes an SVR model with GridSearchCV, and saves the trained pipeline.

### Model artifact
The trained model is stored as:

`models/traffic_speed_svr_pipeline.pkl`

Model metrics are stored as:

`models/model_metrics.json`

### API
The Flask application in `app/main.py` exposes:

- `GET /health`
- `GET /model-info`
- `POST /predict`
- `GET /` for the simple UI

### UI
The root route contains a simple web form that lets a user enter station ID, flow, occupancy, current speed, hour, and day of week to generate a 60-minute-ahead traffic-speed prediction.

### Logging
Prediction successes and errors are logged to:

`logs/app.log`

Logs include latency, input payload, predictions, and exception traces.

### Containerization
The application includes a Dockerfile. The container installs dependencies, trains the model, exposes port 8000, and runs the Flask API with Gunicorn.

## How to Run Locally

```bash
pip install -r requirements.txt
python src/train_model.py
python app/main.py
```

Open:

```text
http://localhost:8000
```

## How to Run with Docker

```bash
docker build -t pems-traffic-api .
docker run -p 8000:8000 pems-traffic-api
```

## API Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "station_id": "1001",
    "flow": 120,
    "occupancy": 0.08,
    "speed": 60,
    "hour": 8,
    "dayofweek": 2
  }'
```

## Testing

```bash
pytest tests/
```

## Production Readiness
This implementation satisfies Step 11 by providing production-ready code, API documentation, a UI, logging, tests, Docker containerization, data storage, trained model artifact storage, and clear instructions for running the application.
