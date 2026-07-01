# Step 7: Experiment With Various Models

## Capstone Project
**Traffic Speed Prediction Using California PeMS Data**

## GitHub Repository
All code, dataset, notebook outputs, figures, and results are uploaded here:

https://github.com/rarra21/Springboard

## Dataset
The dataset used for this experiment is:

`sample_pems_data_small.csv`

GitHub file link:

https://github.com/rarra21/Springboard/blob/main/sample_pems_data_small.csv

Raw dataset path used in the notebook:

https://raw.githubusercontent.com/rarra21/Springboard/main/sample_pems_data_small.csv

## Target Variable
The prediction target is:

`speed_60min_ahead`

The model predicts traffic speed 60 minutes into the future.

## Objective
The goal of Step 7 was to experiment with multiple models for traffic-speed prediction, compare their performance, use proper time-series cross-validation, identify overfitting or underfitting, and select the best final model.

## Metrics Used
Because this is a regression problem, I used:

- MAE
- RMSE
- R²
- Correlation
- Training time
- Prediction time
- Model size

MAE was selected as the primary metric because it directly measures average prediction error in traffic-speed units.

## Cross Validation
I used `TimeSeriesSplit` instead of random train-test split because traffic data is sequential. This ensures the model trains on earlier observations and tests on later observations, preventing future-data leakage.

## Models Tested
The automated experiment tested and compared:

1. Linear Regression
2. Ridge Regression
3. Decision Tree Regressor
4. Random Forest Regressor
5. Gradient Boosting Regressor
6. Support Vector Regressor
7. Average Ensemble of the top-performing models

## Final Model
The best model was selected based on the lowest test MAE while also considering RMSE, R², correlation, training time, prediction time, and model size.

## Ensemble Model
An average ensemble of the top models was also created for the excellence requirement. The ensemble was compared against the individual models, but the final selected model remained the model with the strongest overall metric performance.

## Overfitting and Underfitting Analysis
Linear Regression showed underfitting because it could not capture nonlinear traffic patterns. Tree-based models performed better but were limited by the small dataset size. The best model showed the strongest balance between prediction performance and generalization.

## Presentation Materials
The GitHub repository includes:

- Executed Jupyter notebook
- Dataset
- Model comparison results
- Cross-validation results
- Actual vs predicted graph
- Actual vs predicted scatter plot
- Residual plot
- MAE comparison graph
- RMSE comparison graph
- Correlation comparison graph
- Training-time comparison graph
- Final predictions CSV

## Conclusion
This experiment showed that model comparison is necessary before selecting a final model. Since traffic data is time-based, `TimeSeriesSplit` was the correct validation strategy. For this PeMS sample dataset, the strongest model was selected using MAE as the main metric. Future improvements include using a larger PeMS dataset and experimenting with LSTM, GRU, STGCN, DCRNN, or Graph WaveNet models to capture deeper temporal and spatial traffic patterns.
