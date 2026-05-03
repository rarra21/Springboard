import pandas as pd

# -----------------------------
# Step 1: Load raw PeMS data
# -----------------------------
# Replace with your actual file path
input_file = "combined.txt"

df_full = pd.read_csv(input_file, header=None)

# -----------------------------
# Step 2: Select relevant columns
# -----------------------------
df = df_full[[0, 1, 9, 10, 11]]
df.columns = ["timestamp", "station_id", "flow", "occupancy", "speed"]

# -----------------------------
# Step 3: Clean data
# -----------------------------
df = df.dropna()
df["timestamp"] = pd.to_datetime(df["timestamp"])

# -----------------------------
# Step 4: Feature engineering
# -----------------------------
df["hour"] = df["timestamp"].dt.hour
df["dayofweek"] = df["timestamp"].dt.dayofweek

# -----------------------------
# Step 5: Sort data (important for time series)
# -----------------------------
df = df.sort_values(["station_id", "timestamp"])

# -----------------------------
# Step 6: Create target variable (30 min ahead)
# 5-min data → 6 steps = 30 min
# -----------------------------
df["speed_30min_ahead"] = df.groupby("station_id")["speed"].shift(-6)

# Drop rows with NaN after shift
df = df.dropna()

# -----------------------------
# Step 7: Create smaller sample dataset (for GitHub)
# -----------------------------
df_sample = df.sample(20000, random_state=42)

df_sample.to_csv("data/sample_pems_data_small.csv", index=False)

# -----------------------------
# Step 8: Create 60-min prediction dataset
# -----------------------------
df_sample["speed_60min_ahead"] = df_sample.groupby("station_id")["speed"].shift(-12)

df_60 = df_sample.dropna()

df_60.to_csv("data/sample_pems_60min_small.csv", index=False)

# -----------------------------
# Step 9: Create metadata dataset
# -----------------------------
meta = df_sample[["station_id"]].drop_duplicates()

meta.to_csv("data/station_metadata.csv", index=False)

# -----------------------------
# Done
# -----------------------------
print("Data processing complete. Files saved in /data folder.")
