import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import os

# Load datasets
with open("data/uald.json") as f:
    uald = pd.DataFrame(json.load(f))
with open("data/abbd.json") as f:
    abbd = pd.DataFrame(json.load(f))

# Merge only on anonymous_user_id
merged = pd.merge(uald, abbd, how='inner', on="anonymous_user_id")

if merged.empty:
    print("❌ Merge result is empty. No overlapping user_ids between UALD and ABBD.")
    exit(1)

# Flatten nested dicts
keystroke_df = pd.json_normalize(merged["keystroke_features"])
mouse_df = pd.json_normalize(merged["mouse_features"])

# Drop nested columns and reattach flattened ones
merged = merged.drop(columns=["keystroke_features", "mouse_features", "app_transition_sequence"])
merged = pd.concat([merged, keystroke_df, mouse_df], axis=1)

# Encode categorical variables
categorical = ["role_category", "device_type", "location_type", "campus_zone", "network_type",
               "auth_method", "service_accessed", "academic_period", "client_browser", "client_os"]

encoders = {}
for col in categorical:
    if col in merged.columns:
        encoders[col] = LabelEncoder().fit(merged[col])
        merged[col] = encoders[col].transform(merged[col])

# Drop unused or sensitive columns
merged = merged.drop(columns=["event_id", "timestamp", "device_id", "ip_hash",
                              "start_time", "end_time", "session_id", "primary_activity"],
                     errors="ignore")

# Save
os.makedirs("data", exist_ok=True)
merged.to_csv("data/train_ready.csv", index=False)
print(f"✅ Preprocessed data saved to data/train_ready.csv with {len(merged)} rows.")
