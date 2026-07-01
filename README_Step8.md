# Step 8: Scale Your Prototype with Large-Scale Data

## Capstone Project
Traffic Speed Prediction Using California PeMS Data

## Repository
https://github.com/rarra21/Springboard

## Dataset
- File: `sample_pems_data_small.csv`
- GitHub link: https://github.com/rarra21/Springboard/blob/main/sample_pems_data_small.csv
- Raw URL used in notebook: https://raw.githubusercontent.com/rarra21/Springboard/main/sample_pems_data_small.csv

## Goal
Step 8 demonstrates how the Step 7 prototype can be scaled from a small PeMS sample to larger real-world traffic datasets.

## Scaling Strategy
This prototype uses:
- Chunked data processing so the entire dataset does not need to fit in memory.
- Incremental training with `SGDRegressor.partial_fit`.
- A documented SparkML architecture for future distributed training.
- Lightweight model storage using `joblib`.

## Files
- `notebooks/Step8_Scaling_Prototype_EXECUTED.ipynb`: executed notebook.
- `reports/Step8_Assignment_Submission.docx`: Word report.
- `reports/Step8_Assignment_Submission.md`: markdown report.
- `results/`: metrics, predictions, timing data.
- `figures/`: architecture and model performance plots.
- `models/`: saved incremental model.

## How to Run
Install requirements:

```bash
pip install -r requirements.txt
```

Open the notebook in Jupyter or Google Colab and run all cells.
