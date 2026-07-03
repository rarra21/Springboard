# Traffic Speed Prediction Using California PeMS Data

## Machine Learning Engineering Bootcamp Capstone Project

## Project Overview

This repository contains my end-to-end Machine Learning Engineering Capstone Project completed as part of the Machine Learning Engineering Bootcamp.

The objective of this project is to develop, evaluate, scale, and deploy a machine learning solution capable of predicting **traffic speed 60 minutes ahead** using California Performance Measurement System (PeMS) traffic sensor data.

The project follows the complete machine learning engineering lifecycle—from research and data preparation to model development, scaling, deployment planning, production implementation, and an interactive application.

---

# Problem Statement

Traffic congestion significantly impacts travel time, fuel consumption, public safety, and transportation planning.

The objective of this project is to build a machine learning model that accurately predicts future traffic speed using historical traffic sensor measurements.

Potential applications include:

- Intelligent Transportation Systems (ITS)
- Congestion prediction
- Dynamic traffic routing
- Smart city infrastructure
- Transportation planning

---

# Dataset

**Source**

California Performance Measurement System (PeMS)

Sample dataset included in the repository:

```
sample_pems_data_small.csv
```

Target variable:

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

The project follows the complete ML Engineering lifecycle:

1. Project Planning
2. Data Collection
3. Data Wrangling
4. Research Review
5. Feature Engineering
6. Model Benchmarking
7. Model Experimentation
8. Prototype Scaling
9. Deployment Planning
10. Deployment Architecture
11. Production Implementation
12. Project Presentation

---

# Repository Organization

This repository is organized into branches corresponding to each capstone milestone.

| Step | Description |
|------|-------------|
| Step 1 | Initial Project Ideas |
| Step 2 | Data Collection |
| Step 3 | Project Proposal |
| Step 4 | Research and Existing Solutions |
| Step 5 | Data Wrangling |
| Step 6 | Model Benchmarking |
| Step 7 | Model Experiments |
| Step 8 | Scaling Prototype |
| Step 9 | Deployment Planning |
| Step 10 | Deployment Architecture |
| Step 11 | Deployment Implementation |
| Step 12 | Final Project Showcase |

---

# Models Evaluated

The following machine learning algorithms were evaluated:

- Linear Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regressor (SVR)
- Ensemble Model

TimeSeriesSplit cross-validation was used to evaluate model performance while preserving the chronological order of the traffic data.

---

# Final Solution

The final application predicts traffic speed 60 minutes into the future using traffic sensor measurements.

The production prototype includes:

- Data preprocessing pipeline
- Feature engineering
- Trained machine learning model
- Interactive Streamlit application
- Deployment architecture
- Production deployment plan

---

# Interactive Application

The project includes a Streamlit web application that allows users to interact with the trained machine learning model.

## Run the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
python3 -m streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# Technologies Used

Programming

- Python

Data Processing

- Pandas
- NumPy

Machine Learning

- Scikit-learn

Visualization

- Matplotlib

Application

- Streamlit

Deployment

- Flask (deployment planning)
- Docker (deployment implementation)
- Git
- GitHub

---

# Repository Contents

- Source Code
- Jupyter Notebooks
- Assignment Reports
- Deployment Documentation
- Architecture Diagrams
- Streamlit Application
- Model Artifacts
- README Documentation

---

# Future Improvements

Future work may include:

- Training on the complete California PeMS dataset
- Real-time traffic prediction
- Automated model retraining
- Cloud deployment using AWS, Azure, or Google Cloud
- Apache Spark distributed processing
- Deep learning models including LSTM, GRU, DCRNN, STGCN, and Graph WaveNet

---

# Capstone Deliverables

This repository contains all deliverables required for the Machine Learning Engineering Bootcamp Capstone Project, including:

- Research
- Data Wrangling
- Model Development
- Model Evaluation
- Scaling
- Deployment Planning
- Deployment Architecture
- Production Implementation
- Interactive Application
- Final Presentation

---

# Acknowledgements

This project was completed as part of the Machine Learning Engineering Bootcamp and demonstrates the complete machine learning engineering workflow from research to production-ready deployment.
