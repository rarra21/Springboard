# Step 11: Deployment Implementation

## Project
Traffic Speed Prediction Using California PeMS Data

This folder contains a production-style deployment implementation for the PeMS traffic-speed prediction capstone. The application trains a scikit-learn SVR pipeline, saves the model artifact, exposes a REST API, provides a simple web UI, logs prediction activity, includes tests, and can run inside Docker.

## Folder structure

```text
Step11_Deployment_Implementation/
├── app/
│   ├── main.py
│   └── templates/
│       └── index.html
├── architecture/
│   └── step11_deployment_implementation_architecture.png
├── data/
│   └── sample_pems_data_small.csv
├── docs/
│   ├── Step11_Assignment_Submission.docx
│   └── Step11_Assignment_Submission.md
├── logs/
├── models/
│   ├── traffic_speed_svr_pipeline.pkl
│   └── model_metrics.json
├── src/
│   └── train_model.py
├── tests/
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Features

- Flask REST API
- Simple browser UI
- Trained scikit-learn Pipeline artifact
- Input validation and clear error responses
- Application logging for predictions and failures
- Docker containerization
- Pytest API tests
- README instructions for local and Docker execution

## Run locally

```bash
pip install -r requirements.txt
python src/train_model.py
python app/main.py
```

Open the UI:

```text
http://localhost:8000
```

## API endpoints

### Health check

```bash
curl http://localhost:8000/health
```

### Model information

```bash
curl http://localhost:8000/model-info
```

### Prediction endpoint

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

Example response:

```json
{
  "prediction_speed_60min_ahead": 61.3,
  "latency_ms": 3.2
}
```

## Run with Docker

```bash
docker build -t pems-traffic-api .
docker run -p 8000:8000 pems-traffic-api
```

Or with Docker Compose:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8000
```

## Run tests

```bash
pytest tests/
```

## Logging

The application writes prediction successes and errors to:

```text
logs/app.log
```

Logs include request latency, input payload, prediction value, and exception traces for debugging.

## Deployment notes

This container can be deployed to AWS ECS/Fargate, Google Cloud Run, Azure Container Apps, or Kubernetes. The model artifact is stored in the `models/` folder and can be replaced by a retrained model after validation.
