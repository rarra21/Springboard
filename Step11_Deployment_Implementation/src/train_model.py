"""Train and save the PeMS traffic speed prediction model artifact.

This script implements the production training step for the Step 11 deployment
implementation. It trains a scikit-learn Pipeline that includes preprocessing
and an SVR model, then saves both the model artifact and model metrics.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVR

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_pems_data_small.csv"
MODEL_PATH = ROOT / "models" / "traffic_speed_svr_pipeline.pkl"
METRICS_PATH = ROOT / "models" / "model_metrics.json"

TARGET = "speed_60min_ahead"
FEATURES = ["station_id", "flow", "occupancy", "speed", "hour", "dayofweek"]
NUMERIC_FEATURES = ["flow", "occupancy", "speed", "hour", "dayofweek"]
CATEGORICAL_FEATURES = ["station_id"]


def load_training_data(path: Path = DATA_PATH) -> tuple[pd.DataFrame, pd.Series]:
    """Load, clean, and split the training dataset into features and target."""
    df = pd.read_csv(path)
    required = FEATURES + [TARGET]
    df = df.dropna(subset=required).copy()
    if "timestamp" in df.columns:
        df = df.sort_values("timestamp")

    X = df[FEATURES].copy()
    X["station_id"] = X["station_id"].astype(str)
    y = df[TARGET].astype(float)
    return X, y


def build_pipeline() -> Pipeline:
    """Create the preprocessing and model pipeline."""
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )
    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", SVR()),
        ]
    )


def train() -> dict:
    """Train the model and persist artifacts to the models directory."""
    X, y = load_training_data()
    pipeline = build_pipeline()

    param_grid = {
        "model__C": [1.0, 10.0],
        "model__epsilon": [0.1, 0.5],
        "model__kernel": ["rbf"],
    }

    search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=TimeSeriesSplit(n_splits=3),
        scoring="neg_mean_absolute_error",
        n_jobs=1,
    )

    start = time.time()
    search.fit(X, y)
    training_time = time.time() - start

    best_model = search.best_estimator_
    predictions = best_model.predict(X)

    metrics = {
        "target": TARGET,
        "features": FEATURES,
        "best_params": search.best_params_,
        "mae_training_set": float(mean_absolute_error(y, predictions)),
        "rmse_training_set": float(np.sqrt(mean_squared_error(y, predictions))),
        "r2_training_set": float(r2_score(y, predictions)),
        "training_time_seconds": float(training_time),
        "row_count": int(len(X)),
        "model_artifact": MODEL_PATH.name,
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


if __name__ == "__main__":
    result = train()
    print(json.dumps(result, indent=2))
