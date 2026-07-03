# End-to-End Customer Churn Prediction Using AWS SageMaker

## Overview

This project demonstrates the implementation of an end-to-end customer churn prediction pipeline using Amazon SageMaker. The objective is to predict whether a customer is likely to churn based on historical customer behavior. The project follows the AWS SageMaker workflow for data preprocessing, model training, and deployment.

This project was completed as part of the Machine Learning Engineering Bootcamp.

---

## Business Problem

Customer churn is one of the biggest challenges for subscription-based and customer-centric businesses. Predicting churn enables organizations to:

- Improve customer retention
- Reduce revenue loss
- Target high-risk customers
- Improve marketing strategies
- Enhance customer satisfaction

Machine learning allows businesses to identify customers who are likely to discontinue using their services and take proactive retention measures.

---

## Technologies Used

- Amazon SageMaker Studio
- Amazon S3
- Python
- Pandas
- NumPy
- Scikit-learn
- Amazon SageMaker XGBoost

---

## Project Workflow

### 1. Environment Setup

- Created an AWS account
- Configured Amazon SageMaker Studio
- Launched JupyterLab
- Created an Amazon S3 bucket

---

### 2. Data Preparation

The customer churn dataset was uploaded to Amazon S3.

Preprocessing steps included:

- Loading data from Amazon S3
- Converting date columns
- Handling missing values
- Feature engineering
- One-hot encoding categorical variables
- Removing unnecessary columns

---

### 3. Dataset Splitting

The processed dataset was divided into:

- Training Set
- Validation Set
- Test Set

The datasets were uploaded back to Amazon S3 for model training.

---

### 4. Model Configuration

The project configured the SageMaker built-in XGBoost algorithm using:

- Binary Logistic Objective
- AUC Evaluation Metric
- SageMaker Estimator
- Amazon S3 Training Data

---

## AWS Services Used

- Amazon S3
- Amazon SageMaker Studio
- Amazon SageMaker Training Jobs
- Amazon SageMaker XGBoost

---

## Repository Structure

```
customer-churn-aws/

│
├── README.md
├── Customer_Churn_AWS_SageMaker.ipynb
├── screenshots/
│
└── data/
```

---

## Results

The following tasks were successfully completed:

- AWS environment setup
- SageMaker Studio configuration
- Amazon S3 bucket creation
- Dataset upload
- Data preprocessing
- Feature engineering
- Dataset splitting
- Uploading processed datasets to Amazon S3
- SageMaker XGBoost training job configuration

---

## Limitation Encountered

The SageMaker training job could not be executed because the AWS account used for this project has an account-level service quota of **0 instances** for SageMaker managed training jobs.

AWS returned the following error:

```
ResourceLimitExceeded:
The account-level service limit
'ml.m5.large for training job usage'
is 0 instances.
```

The notebook, preprocessing pipeline, training configuration, and AWS resources were successfully configured. The limitation was due to AWS account service quotas rather than implementation errors.

---

## Future Improvements

If SageMaker training quotas become available, the remaining workflow will include:

- Hyperparameter tuning
- Model evaluation
- Model Registry
- Batch Transform
- SageMaker Pipelines
- SageMaker Clarify for explainability
- Model deployment

---

## References

AWS Blog:

https://aws.amazon.com/blogs/machine-learning/build-tune-and-deploy-an-end-to-end-churn-prediction-model-using-amazon-sagemaker-pipelines/

---

Machine Learning Engineering Bootcamp
