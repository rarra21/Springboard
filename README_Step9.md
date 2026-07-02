# Step 9: Deployment Method and Engineering Plan

This folder contains the Step 9 deployment plan for the Machine Learning Engineering Bootcamp capstone project.

## Project
Traffic Speed Prediction Using California PeMS Data

## Repository
https://github.com/rarra21/Springboard

## Selected Deployment Method
FastAPI REST API packaged with Docker, with a future path to AWS SageMaker, Google Vertex AI, Azure ML, or Kubernetes.

## Files

```text
Step9_Deployment_Plan/
├── README.md
├── reports/
│   ├── Step9_Assignment_Submission.docx
│   └── Step9_Assignment_Submission.md
├── deployment/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── sample_request.json
└── diagrams/
    └── deployment_architecture.txt
```

## API Endpoint

`POST /predict`

The API accepts traffic sensor features and returns a predicted traffic speed 60 minutes ahead.

## MLOps Lifecycle

1. Train model
2. Save model artifact
3. Package with FastAPI and Docker
4. Deploy API
5. Log predictions
6. Monitor latency, errors, drift, and model performance
7. Retrain when performance degrades
8. Version and redeploy model

## Dataset
https://raw.githubusercontent.com/rarra21/Springboard/main/sample_pems_data_small.csv
