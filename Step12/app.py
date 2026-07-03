"""Streamlit interface for the PeMS traffic-speed prediction capstone.

Run locally:
    streamlit run app.py
"""
from pathlib import Path
import json
import pandas as pd
import streamlit as st
import joblib

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "models" / "traffic_speed_svr_pipeline.pkl"
METRICS_PATH = APP_DIR / "models" / "model_metrics.json"
DATA_PATH = APP_DIR / "data" / "sample_pems_data_small.csv"

FEATURE_COLUMNS = ["station_id", "flow", "occupancy", "speed", "hour", "dayofweek"]
TARGET_COLUMN = "speed_60min_ahead"

st.set_page_config(
    page_title="PeMS Traffic Speed Predictor",
    page_icon="🚦",
    layout="centered",
)

@st.cache_resource
def load_model():
    """Load the trained scikit-learn pipeline."""
    if not MODEL_PATH.exists():
        st.error(f"Model artifact not found: {MODEL_PATH}")
        st.stop()
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_sample_data():
    """Load sample PeMS data for default values and preview."""
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)
    return pd.DataFrame()

@st.cache_data
def load_metrics():
    """Load saved model metrics, if available."""
    if METRICS_PATH.exists():
        with open(METRICS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

model = load_model()
df = load_sample_data()
metrics = load_metrics()

st.title("🚦 Traffic Speed Prediction")
st.write(
    "This Streamlit app predicts traffic speed **60 minutes ahead** using a trained "
    "Support Vector Regression model from the California PeMS traffic-speed capstone project."
)

with st.expander("Project information", expanded=False):
    st.markdown(
        """
        **Capstone project:** Traffic Speed Prediction Using California PeMS Data  
        **Target variable:** `speed_60min_ahead`  
        **Model:** Scikit-learn SVR pipeline  
        **Interface:** Streamlit local web application
        """
    )
    if metrics:
        st.json(metrics)

st.subheader("Enter traffic conditions")

# Use sample data ranges where available.
if not df.empty:
    station_options = sorted(df["station_id"].astype(str).unique().tolist())
    default_station = station_options[0]
    flow_min, flow_max = int(df["flow"].min()), int(df["flow"].max())
    occ_min, occ_max = float(df["occupancy"].min()), float(df["occupancy"].max())
    speed_min, speed_max = float(df["speed"].min()), float(df["speed"].max())
    default_flow = int(df["flow"].median())
    default_occ = float(df["occupancy"].median())
    default_speed = float(df["speed"].median())
else:
    station_options = ["1001", "1002", "1003"]
    default_station = "1001"
    flow_min, flow_max, default_flow = 0, 2500, 900
    occ_min, occ_max, default_occ = 0.0, 1.0, 0.12
    speed_min, speed_max, default_speed = 0.0, 85.0, 60.0

col1, col2 = st.columns(2)

with col1:
    station_id = st.selectbox("Station ID", station_options, index=0)
    flow = st.number_input("Traffic flow", min_value=0, max_value=max(flow_max, 1), value=max(default_flow, 0), step=10)
    occupancy = st.number_input(
        "Occupancy",
        min_value=0.0,
        max_value=max(occ_max, 1.0),
        value=min(max(default_occ, 0.0), max(occ_max, 1.0)),
        step=0.01,
        format="%.3f",
    )

with col2:
    speed = st.number_input(
        "Current speed",
        min_value=0.0,
        max_value=max(speed_max, 100.0),
        value=min(max(default_speed, 0.0), max(speed_max, 100.0)),
        step=1.0,
        format="%.2f",
    )
    hour = st.slider("Hour of day", min_value=0, max_value=23, value=8)
    dayofweek = st.slider("Day of week", min_value=0, max_value=6, value=1, help="0 = Monday, 6 = Sunday")

input_df = pd.DataFrame(
    [{
        "station_id": str(station_id),
        "flow": flow,
        "occupancy": occupancy,
        "speed": speed,
        "hour": hour,
        "dayofweek": dayofweek,
    }]
)

st.caption("Model input preview")
st.dataframe(input_df, use_container_width=True)

if st.button("Predict 60-minute-ahead speed", type="primary"):
    try:
        prediction = float(model.predict(input_df[FEATURE_COLUMNS])[0])
        st.success(f"Predicted speed 60 minutes ahead: **{prediction:.2f}**")
        st.write(
            "Interpretation: this is the model's forecasted traffic speed one hour after "
            "the current conditions entered above."
        )
    except Exception as exc:
        st.error("Prediction failed. Please check the input values and model artifact.")
        st.exception(exc)

st.divider()
st.subheader("Sample data preview")
if not df.empty:
    st.dataframe(df.head(10), use_container_width=True)
else:
    st.info("Sample data file was not found, but the app can still run with manual inputs.")
