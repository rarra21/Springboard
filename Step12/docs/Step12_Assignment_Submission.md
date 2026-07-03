# Machine Learning Engineering Bootcamp Capstone Project

# Step 12: Share Your Project with the World

## Project title

Traffic Speed Prediction Using California PeMS Data

## GitHub repository

The complete project repository is available at:

https://github.com/rarra21/Springboard

The repository contains capstone deliverables for research, model experimentation, scaling, deployment planning, deployment architecture, deployment implementation, and the final project showcase.

## Visual manifestation / user interface

A lightweight Streamlit application is included as the user interface for the project. The app allows users to enter traffic-related inputs and receive a traffic speed prediction 60 minutes ahead.

The Streamlit app can be run locally with:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app then opens in the browser at:

```text
http://localhost:8501
```

## Problem statement

Traffic congestion affects travel time, safety, and transportation planning. The goal of this capstone project is to predict traffic speed 60 minutes ahead using California PeMS traffic sensor data. A model that can forecast traffic speed can support traffic monitoring, congestion analysis, and future intelligent transportation applications.

## Dataset

The project uses a sample California PeMS traffic dataset.

Features include:

- Station ID
- Traffic flow
- Occupancy
- Current speed
- Hour of day
- Day of week

The prediction target is:

- `speed_60min_ahead`

## Approach

The project followed the machine learning engineering lifecycle:

1. Researched existing traffic forecasting approaches.
2. Prepared and explored PeMS traffic data.
3. Compared multiple regression models.
4. Used time-series-aware validation.
5. Selected a final model based on prediction performance and practicality.
6. Designed a scaling plan for larger datasets.
7. Designed a deployment architecture.
8. Built a local Streamlit interface for user interaction.

## Model experimentation

The project compared several regression models:

- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regressor
- Ensemble model

Because this is a forecasting problem, TimeSeriesSplit was used to avoid future-data leakage.

## Final model

The final model used in the Streamlit app is a scikit-learn Support Vector Regression pipeline. The model is saved as a serialized artifact and loaded by the app at runtime.

## Deployment and interaction

The Step 12 interface is implemented with Streamlit. The user enters traffic conditions, clicks the prediction button, and receives a forecasted traffic speed 60 minutes ahead.

This satisfies the requirement for an interface that allows users to interact with the machine learning model.

## Future work

Future improvements include:

- Deploying the Streamlit app to Streamlit Community Cloud or another cloud provider.
- Training on the complete California PeMS dataset.
- Adding real-time traffic data ingestion.
- Adding monitoring and retraining automation.
- Testing advanced models such as LSTM, GRU, STGCN, DCRNN, and Graph WaveNet.

## Conclusion

This capstone project demonstrates the complete machine learning lifecycle from problem definition and research to model experimentation, scaling, deployment planning, implementation, and user-facing presentation. The final Streamlit interface provides a simple way for users to interact with the traffic speed prediction model.
