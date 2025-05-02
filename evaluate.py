import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data/train_ready.csv")

# Prepare features and target
y_true = df["success"].astype(int)
X = df.select_dtypes(include=[np.number]).drop(columns=["success", "cluster"], errors='ignore')

# Drop columns with all NaNs
X = X.dropna(axis=1, how='all')
print("Columns after dropping all-NaN columns:", X.columns.tolist())

# Analyze NaN distribution
print("\nNaN counts in numeric columns:")
nan_counts = X.isna().sum()
print(nan_counts)
print("\nPercentage of NaNs per column:")
print((nan_counts / len(X) * 100).round(2))

# Evaluate with NaN-tolerant model (HistGradientBoostingClassifier)
print("\n=== Evaluating with HistGradientBoostingClassifier (NaN-tolerant) ===")
hgb = HistGradientBoostingClassifier(random_state=0)
hgb.fit(X, y_true)
print("Classification Report (HistGradientBoostingClassifier):")
print(classification_report(y_true, hgb.predict(X)))

# Encode NaNs for RandomForestClassifier
X_encoded = X.copy()
nan_indicators = pd.DataFrame(index=X.index)
for col in X.columns:
    if X[col].isna().any():
        # Create indicator column for NaNs
        nan_indicators[f"{col}_is_nan"] = X[col].isna().astype(int)
        # Fill NaNs with a sentinel value (e.g., -999)
        X_encoded[col] = X[col].fillna(-999)

# Combine features with NaN indicators
X_encoded = pd.concat([X_encoded, nan_indicators], axis=1)
print("\nColumns after adding NaN indicators:", X_encoded.columns.tolist())

# Evaluate RandomForestClassifier with encoded NaNs
print("\n=== Evaluating with RandomForestClassifier (NaN-encoded) ===")
rf = RandomForestClassifier(n_estimators=100, random_state=0)
rf.fit(X_encoded, y_true)
print("Classification Report (RandomForestClassifier with NaN encoding):")
print(classification_report(y_true, rf.predict(X_encoded)))

# Compare with imputed NaNs
imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
print("\n=== Evaluating with RandomForestClassifier (NaN-imputed) ===")
rf_imputed = RandomForestClassifier(n_estimators=100, random_state=0)
rf_imputed.fit(X_imputed, y_true)
print("Classification Report (RandomForestClassifier with mean imputation):")
print(classification_report(y_true, rf_imputed.predict(X_imputed)))

# Optional: Split data to evaluate on a test set
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_true, test_size=0.2, random_state=42)
rf_test = RandomForestClassifier(n_estimators=100, random_state=0)
rf_test.fit(X_train, y_train)
print("\n=== RandomForestClassifier (NaN-encoded) on Test Set ===")
print("Classification Report (Test Set):")
print(classification_report(y_test, rf_test.predict(X_test)))