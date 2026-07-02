# Step 9: Pick Your Deployment Method and Engineering Plan

## Capstone Project
Traffic Speed Prediction Using California PeMS Data

## Student
Meenu Arora

## GitHub Repository
https://github.com/rarra21/Springboard

## Recommended Deployment Method
For this capstone, I recommend deploying the trained traffic-speed prediction model as a **FastAPI REST service packaged in Docker**, with the option to deploy on **AWS SageMaker real-time endpoint** or a lightweight cloud container service.

This approach is appropriate because the model predicts traffic speed 60 minutes ahead from tabular traffic sensor features. The application needs a reliable prediction API, but the current prototype does not require very large GPU infrastructure.

## Deployment Options Considered

| Option | Strengths | Weaknesses | Fit for This Project |
|---|---|---|---|
| Local batch notebook | Simple, low cost | Not production-ready | Good only for experimentation |
| FastAPI + Docker | Portable, low-cost, easy to test | Requires manual monitoring setup | Best fit for capstone prototype |
| AWS SageMaker endpoint | Managed deployment, autoscaling, monitoring | Higher cost, cloud setup complexity | Strong production option |
| Google Vertex AI endpoint | Managed model registry, deployment, monitoring | Requires GCP setup | Good alternative |
| Azure ML online endpoint | Managed real-time endpoint and MLOps integration | Requires Azure setup | Good enterprise option |
| Kubernetes | Most flexible and production-grade | Highest complexity | Excellence-level option |

## Selected Architecture

```text
PeMS traffic input data
        ↓
Feature validation and preprocessing
        ↓
Saved preprocessing pipeline
        ↓
Trained SVR model / best model artifact
        ↓
FastAPI prediction endpoint
        ↓
Prediction response: speed_60min_ahead
        ↓
Logging, monitoring, drift checks, retraining trigger
```

## API Design

### Endpoint
`POST /predict`

### Example Request
```json
{
  "station_id": 400001,
  "flow": 125.0,
  "occupancy": 0.08,
  "speed": 62.5,
  "hour": 8,
  "dayofweek": 2
}
```

### Example Response
```json
{
  "predicted_speed_60min_ahead": 61.8,
  "model_version": "v1.0",
  "status": "success"
}
```

## Pseudocode

```python
load trained_model.pkl
load preprocessing_pipeline.pkl

@app.post('/predict')
def predict(request):
    validate input schema
    convert request to dataframe
    apply preprocessing
    prediction = model.predict(processed_features)
    log request, prediction, timestamp, model version
    return prediction
```

## Monitoring Plan

The deployed model should be monitored after deployment. Important metrics include:

- API latency
- API error rate
- Number of requests
- Input feature drift
- Prediction drift
- MAE/RMSE when actual future speeds become available
- Missing or invalid input values

## Retraining Plan

1. Store new prediction requests and actual future speed values.
2. Run scheduled evaluation weekly or monthly.
3. Compare current production MAE/RMSE against the training baseline.
4. If performance degrades, retrain the model.
5. Validate the new model using TimeSeriesSplit.
6. Register a new model version.
7. Deploy the new version using a staged rollout.
8. Monitor the new version and roll back if needed.

## Engineering and MLOps Plan

The GitHub repository should include:

```text
Step9_Deployment_Plan/
├── README.md
├── reports/
│   └── Step9_Assignment_Submission.docx
├── deployment/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── sample_request.json
└── diagrams/
    └── deployment_architecture.txt
```

## Tool Choices

- **FastAPI** for the prediction API because it is lightweight and easy to test.
- **Docker** for reproducible packaging.
- **scikit-learn/joblib** for loading the trained model.
- **GitHub** for version control.
- **CloudWatch, Vertex AI Monitoring, or Azure Monitor** if deployed to a managed cloud service.

## Trade-Offs

FastAPI and Docker are simple and cost-effective, but they require more custom monitoring than a managed cloud ML platform. AWS SageMaker, Google Vertex AI, and Azure ML provide stronger managed deployment and monitoring features, but they add cost and cloud complexity.

For this capstone, FastAPI + Docker is the best balance between engineering realism, cost, and deployment speed.

## Conclusion

The deployment plan separates training from serving. The trained model is packaged as a reusable model artifact and exposed through a prediction API. The plan also includes logging, monitoring, drift detection, retraining, model versioning, and redeployment. This demonstrates that deployment is not the end of the ML lifecycle, but the beginning of production model maintenance.
