# Step 12: Share Your Project with the World

## Machine Learning Engineering Bootcamp Capstone Project

# Traffic Speed Prediction Using California PeMS Data

## Project Overview

This project was completed as part of the Machine Learning Engineering Bootcamp Capstone. The objective is to predict traffic speed **60 minutes ahead** using historical California PeMS traffic sensor data.

The project demonstrates the complete machine learning engineering lifecycle, including:

- Research and literature review
- Data preprocessing and feature engineering
- Model development and evaluation
- Model scaling
- Deployment planning
- Deployment architecture
- Production implementation
- Interactive Streamlit application

---

# Problem Statement

Traffic congestion significantly impacts travel time, fuel consumption, and road safety. This project develops a machine learning model capable of predicting traffic speed one hour into the future to support intelligent transportation systems and traffic management.

---

# Dataset

**Dataset:** California Performance Measurement System (PeMS)

Sample dataset included:

```
sample_pems_data_small.csv
```

**Target Variable**

```
speed_60min_ahead
```

Features include:

- Station ID
- Traffic Flow
- Occupancy
- Current Speed
- Hour of Day
- Day of Week

---

# Machine Learning Workflow

The project follows the complete ML lifecycle:

1. Research existing solutions
2. Data preprocessing
3. Feature engineering
4. Model experimentation
5. Model evaluation
6. Model scaling
7. Deployment planning
8. Deployment implementation
9. Interactive application

---

# Models Evaluated

The following regression models were compared:

- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regressor (SVR)
- Ensemble Model

TimeSeriesSplit cross-validation was used to evaluate model performance while preserving the temporal order of the data.

---

# Final Model

The final model predicts traffic speed 60 minutes ahead using:

- Traffic Flow
- Occupancy
- Current Speed
- Hour
- Day of Week

The trained model is integrated into an interactive Streamlit application.

---

# Interactive Application

The project includes a Streamlit interface that allows users to enter traffic conditions and obtain predicted traffic speed.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python3 -m streamlit run app.py
```

After starting Streamlit, open your browser and navigate to:

```
http://localhost:8501
```

---

# Repository Structure

```
Step12_Project_Showcase/
│
├── app.py
├── README.md
├── requirements.txt
├── models/
├── data/
└── docs/
```

---

# GitHub Repository

Repository:

**https://github.com/rarra21/Springboard**

The capstone project is organized into GitHub branches corresponding to each milestone.

### Branches

- Step 4 – Research and Reproduction
- Step 7 – Model Experiments
- Step 8 – Scaling Prototype
- Step 9 – Deployment Planning
- Step 10 – Deployment Architecture
- Step 11 – Deployment Implementation
- Step 12 – Project Showcase

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git
- GitHub

---

# Future Improvements

Future work may include:

- Training on the complete California PeMS dataset
- Cloud deployment using Streamlit Community Cloud, AWS, or Azure
- Real-time traffic data ingestion through APIs
- Automatic model retraining
- Deep learning models such as LSTM, GRU, DCRNN, STGCN, and Graph WaveNet


### Prediction Result

![Prediction](screenshots/prediction_result.png)

---

# Acknowledgements

This project was completed as part of the **Machine Learning Engineering Bootcamp Capstone Project**, demonstrating the complete machine learning engineering lifecycle from research and experimentation to deployment and user interaction.
