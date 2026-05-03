# Springboard
# Traffic Speed Prediction using PeMS Data

## Overview
This project focuses on predicting freeway traffic speed 30 minutes ahead using historical traffic data. The dataset is sourced from the California PeMS (Performance Measurement System), which provides real-time and historical traffic information.

The goal is to build a machine learning model that can forecast near-term traffic conditions based on current measurements.

---

## Datasets

This repository includes three datasets:

### 1. sample_pems_data_small.csv
- Cleaned and processed traffic data
- Features:
  - timestamp
  - station_id
  - flow
  - occupancy
  - speed
  - hour
  - dayofweek
  - speed_30min_ahead (target)

### 2. sample_pems_60min_small.csv
- Similar to above but includes:
  - speed_60min_ahead (1-hour prediction target)

### 3. station_metadata.csv
- Contains station-level information (station IDs)

---

## Data Source

Raw data was collected from:
- California Department of Transportation (Caltrans) PeMS
- https://pems.dot.ca.gov

Due to large size (~400MB+), only processed sample datasets are included in this repository.

---

## Data Collection & Processing

The script used to collect and process the data is:
