# Step 12 Project Showcase: PeMS Traffic Speed Prediction

This folder contains the interactive Streamlit interface for the Machine Learning Engineering Bootcamp capstone project.

## Project overview

The project predicts traffic speed 60 minutes ahead using California PeMS traffic sensor data. The user interface allows a reviewer to enter traffic conditions and receive a model prediction.

## Repository

Main repository:

https://github.com/rarra21/Springboard

The repository is organized by branches and capstone steps.

## Interface

The interface is a local Streamlit application.

Inputs:

- Station ID
- Traffic flow
- Occupancy
- Current speed
- Hour of day
- Day of week

Output:

- Predicted traffic speed 60 minutes ahead

## How to run locally

From this folder, run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Files

```text
Step12_Project_Showcase/
├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── sample_pems_data_small.csv
├── models/
│   ├── traffic_speed_svr_pipeline.pkl
│   └── model_metrics.json
├── docs/
│   └── Step12_Assignment_Submission.md
└── screenshots/
```

## Technologies

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib

## Notes

This app is designed as a local project showcase interface. Future work could deploy it to Streamlit Community Cloud, AWS, Azure, or Google Cloud.
