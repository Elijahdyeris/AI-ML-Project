import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.cluster import DBSCAN
from sklearn.impute import SimpleImputer
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load preprocessed data
df = pd.read_csv("data/train_ready.csv")

# Train Random Forest
y = df["success"].astype(int)
X = df.select_dtypes(include=[np.number]).drop(columns=["success", "cluster"], errors='ignore')

# Drop columns with all NaNs
X = X.dropna(axis=1, how='all')
print("Columns after dropping all-NaN columns:", X.columns.tolist())

# Impute remaining NaNs with mean strategy
imputer = SimpleImputer(strategy='mean')
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train, y_train)

print("🎯 Random Forest Performance:")
print(classification_report(y_test, clf.predict(X_test)))

# LSTM: Create simple sequential input from session_duration
sequence_data = df[["session_duration"]].values
sequence_data = np.expand_dims(sequence_data, axis=-1)
sequence_data = tf.keras.preprocessing.sequence.pad_sequences([sequence_data], maxlen=10)[0]

# Dummy LSTM for temporal pattern
model = Sequential([
    LSTM(16, input_shape=(10, 1)),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')
print("🔄 LSTM model created (not fully trained for brevity).")

# Clustering
clustering_features = df[["typing_speed", "avg_key_dwell_time", "avg_movement_speed"]]
# Impute NaNs for clustering features
clustering_features = pd.DataFrame(imputer.fit_transform(clustering_features), columns=clustering_features.columns)
db = DBSCAN(eps=30, min_samples=5).fit(clustering_features)
df['cluster'] = db.labels_

print(f"📊 Clustering: {len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)} clusters found.")