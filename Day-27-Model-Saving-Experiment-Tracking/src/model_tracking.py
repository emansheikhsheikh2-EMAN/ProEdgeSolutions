import os
import json
from datetime import datetime

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from sklearn.model_selection import train_test_split


# =========================
# 1. Paths
# =========================

DATA_PATH = "data/train.csv"
MODEL_PATH = "models/random_forest_model.pkl"
EXPERIMENT_PATH = "experiments/experiment_results.json"

DATASET_NAME = "Telco Customer Churn Dataset"
MODEL_NAME = "Random Forest Classifier"
MODEL_VERSION = "v1.0"


# =========================
# 2. Load Dataset
# =========================

df = pd.read_csv(DATA_PATH)

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# =========================
# 3. Prepare Data
# =========================

# Remove customer ID
df = df.drop(columns=["customerID"], errors="ignore")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove missing values
df = df.dropna()

# Separate target
y = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

X = df.drop("Churn", axis=1)

# Convert categorical columns
X = pd.get_dummies(
    X,
    drop_first=True
)


# =========================
# 4. Train/Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# =========================
# 5. Train Model
# =========================

model_parameters = {
    "n_estimators": 200,
    "max_depth": 5,
    "min_samples_split": 5,
    "min_samples_leaf": 2,
    "random_state": 42
}

model = RandomForestClassifier(
    **model_parameters
)

model.fit(X_train, y_train)


# =========================
# 6. Original Model Prediction
# =========================

original_predictions = model.predict(X_test)


# =========================
# 7. Model Evaluation
# =========================

accuracy = accuracy_score(
    y_test,
    original_predictions
)

precision = precision_score(
    y_test,
    original_predictions
)

recall = recall_score(
    y_test,
    original_predictions
)

f1 = f1_score(
    y_test,
    original_predictions
)

print("\n===== MODEL EVALUATION =====")

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")


# =========================
# 8. Save Model
# =========================

os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    MODEL_PATH
)

print("\nModel saved successfully!")
print("Model Path:", MODEL_PATH)


# =========================
# 9. Load Saved Model
# =========================

loaded_model = joblib.load(
    MODEL_PATH
)

print("\nSaved model loaded successfully!")


# =========================
# 10. Predictions Using Loaded Model
# =========================

loaded_predictions = loaded_model.predict(
    X_test
)

print(
    "Loaded model predictions generated successfully!"
)


# =========================
# 11. Verify Predictions
# =========================

predictions_match = (
    original_predictions == loaded_predictions
).all()

print(
    "Original and loaded model predictions match:",
    predictions_match
)


# =========================
# 12. Experiment Tracking
# =========================

os.makedirs(
    "experiments",
    exist_ok=True
)

experiment = {
    "model_name": MODEL_NAME,
    "training_date": datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    ),
    "dataset_name": DATASET_NAME,
    "model_version": MODEL_VERSION,
    "model_parameters": model_parameters,
    "evaluation_metrics": {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4)
    },
    "model_path": MODEL_PATH,
    "predictions_match": bool(predictions_match)
}


# =========================
# 13. Maintain Experiment History
# =========================

if os.path.exists(EXPERIMENT_PATH):

    with open(
        EXPERIMENT_PATH,
        "r"
    ) as file:

        experiment_history = json.load(file)

    # Convert old single experiment
    # into a history list
    if isinstance(
        experiment_history,
        dict
    ):
        experiment_history = [
            experiment_history
        ]

else:
    experiment_history = []


# Add current experiment
experiment_history.append(
    experiment
)


# Save complete history
with open(
    EXPERIMENT_PATH,
    "w"
) as file:

    json.dump(
        experiment_history,
        file,
        indent=4
    )


print(
    "\nExperiment results saved successfully!"
)

print(
    "Experiment Path:",
    EXPERIMENT_PATH
)

print(
    "Total Experiments:",
    len(experiment_history)
)