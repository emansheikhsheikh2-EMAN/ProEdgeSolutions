import os
import json
from datetime import datetime

from logging_config import setup_logging

import joblib
import pandas as pd

from config import (
    DATASET_PATH,
    MODEL_PATH,
    PROJECT_NAME,
    ENVIRONMENT,
    EXPERIMENT_PATH
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from sklearn.model_selection import train_test_split


# =========================
# 1. Configuration
# =========================

DATA_PATH = DATASET_PATH
DATASET_NAME = "Telco Customer Churn Dataset"
MODEL_NAME = "Random Forest Classifier"
MODEL_VERSION = "v1.0"

TEST_SIZE = 0.20
RANDOM_STATE = 42


# =========================
# 2. Logging Setup
# =========================

logger = setup_logging()

logger.info("ML application started")


# =========================
# 3. Project Information
# =========================

print("Project:", PROJECT_NAME)
print("Environment:", ENVIRONMENT)

logger.info("Project: %s", PROJECT_NAME)
logger.info("Environment: %s", ENVIRONMENT)


# =========================
# 4. Load Dataset
# =========================

try:
    logger.info("Starting data loading")

    df = pd.read_csv(DATA_PATH)

    logger.info("Data loaded successfully")
    logger.info("Dataset shape: %s", df.shape)

except Exception as e:
    logger.error("Failed to load dataset: %s", e)
    raise

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# =========================
# 5. Prepare Data
# =========================

try:
    logger.info("Starting data preprocessing")

    df = df.drop(
        columns=["customerID"],
        errors="ignore"
    )

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df = df.dropna()

    y = df["Churn"].map({
        "Yes": 1,
        "No": 0
    })

    X = df.drop(
        "Churn",
        axis=1
    )

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    logger.info("Data preprocessing completed successfully")

except Exception as e:
    logger.error("Data preprocessing failed: %s", e)
    raise


# =========================
# 6. Train/Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)

logger.info("Train/test split completed")
logger.info("Training data shape: %s", X_train.shape)
logger.info("Testing data shape: %s", X_test.shape)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# =========================
# 7. Train Model
# =========================

model_parameters = {
    "n_estimators": 200,
    "max_depth": 5,
    "min_samples_split": 5,
    "min_samples_leaf": 2,
    "random_state": RANDOM_STATE
}

try:
    logger.info("Model training started")

    model = RandomForestClassifier(
        **model_parameters
    )

    model.fit(
        X_train,
        y_train
    )

    logger.info("Model training completed successfully")

except Exception as e:
    logger.error("Model training failed: %s", e)
    raise


# =========================
# 8. Model Prediction
# =========================

try:
    original_predictions = model.predict(
        X_test
    )

    logger.info("Prediction generation completed successfully")

except Exception as e:
    logger.error("Prediction generation failed: %s", e)
    raise


# =========================
# 9. Model Evaluation
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

logger.info(
    "Model evaluation completed | Accuracy=%.4f | Precision=%.4f | Recall=%.4f | F1=%.4f",
    accuracy,
    precision,
    recall,
    f1
)


# =========================
# 10. Save Model
# =========================

try:
    os.makedirs(
        os.path.dirname(MODEL_PATH),
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    logger.info(
        "Model saved successfully: %s",
        MODEL_PATH
    )

except Exception as e:
    logger.error("Model saving failed: %s", e)
    raise

print("\nModel saved successfully!")
print("Model Path:", MODEL_PATH)


# =========================
# 11. Load Saved Model
# =========================

try:
    loaded_model = joblib.load(
        MODEL_PATH
    )

    logger.info(
        "Saved model loaded successfully"
    )

except Exception as e:
    logger.error(
        "Model loading failed: %s",
        e
    )
    raise

print("\nSaved model loaded successfully!")


# =========================
# 12. Predictions Using Loaded Model
# =========================

try:
    loaded_predictions = loaded_model.predict(
        X_test
    )

    logger.info(
        "Predictions generated using loaded model"
    )

except Exception as e:
    logger.error(
        "Loaded model prediction failed: %s",
        e
    )
    raise

print(
    "Loaded model predictions generated successfully!"
)


# =========================
# 13. Verify Predictions
# =========================

predictions_match = (
    original_predictions == loaded_predictions
).all()

logger.info(
    "Prediction verification completed | Match=%s",
    predictions_match
)

print(
    "Original and loaded model predictions match:",
    predictions_match
)


# =========================
# 14. Experiment Tracking
# =========================

os.makedirs(
    "experiments",
    exist_ok=True
)

experiment = {
    "project_name": PROJECT_NAME,
    "environment": ENVIRONMENT,
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
    "predictions_match": bool(
        predictions_match
    )
}


# =========================
# 15. Maintain Experiment History
# =========================

if os.path.exists(EXPERIMENT_PATH):

    try:
        with open(
            EXPERIMENT_PATH,
            "r"
        ) as file:

            experiment_history = json.load(file)

        if isinstance(
            experiment_history,
            dict
        ):
            experiment_history = [
                experiment_history
            ]

    except Exception as e:
        logger.warning(
            "Could not read experiment history: %s",
            e
        )

        experiment_history = []

else:
    experiment_history = []


experiment_history.append(
    experiment
)


# =========================
# 16. Save Experiment History
# =========================

try:
    with open(
        EXPERIMENT_PATH,
        "w"
    ) as file:

        json.dump(
            experiment_history,
            file,
            indent=4
        )

    logger.info(
        "Experiment results saved successfully"
    )

except Exception as e:
    logger.error(
        "Failed to save experiment results: %s",
        e
    )
    raise


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

logger.info(
    "Total experiments: %s",
    len(experiment_history)
)

logger.info(
    "ML application completed successfully"
)