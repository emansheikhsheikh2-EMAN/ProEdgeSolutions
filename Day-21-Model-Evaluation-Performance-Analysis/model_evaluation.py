# Day 21 - Model Evaluation & Performance Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay,
    RocCurveDisplay
)

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

# --------------------------------------------------
# 2. Data Cleaning
# --------------------------------------------------

# Drop unnecessary column
if "PassengerId" in df.columns:
    df = df.drop("PassengerId", axis=1)

# Drop Cabin because it contains many missing values
if "Cabin" in df.columns:
    df = df.drop("Cabin", axis=1)

# Fill missing Age with median
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked with mode
if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Convert categorical columns
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

# Make sure all boolean columns are numeric
df = df.select_dtypes(include=["number"])

# --------------------------------------------------
# 3. Features and Target
# --------------------------------------------------

X = df.drop("Survived", axis=1)
y = df["Survived"]

# --------------------------------------------------
# 4. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# --------------------------------------------------
# 5. Train Random Forest Model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------------------------
# 6. Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# --------------------------------------------------
# 7. Evaluation Metrics
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)
cm = confusion_matrix(y_test, y_pred)

print("\n" + "=" * 50)
print("MODEL EVALUATION REPORT")
print("=" * 50)

print(f"\nAccuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

print("\nConfusion Matrix:")
print(cm)

# --------------------------------------------------
# 8. Save Evaluation Results
# --------------------------------------------------

results = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1,
        roc_auc
    ]
})

results.to_csv("evaluation_results.csv", index=False)

print("\nEvaluation results saved to evaluation_results.csv")

# --------------------------------------------------
# 9. Confusion Matrix Visualization
# --------------------------------------------------

plt.figure(figsize=(7, 5))

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Survived", "Survived"]
).plot()

plt.title("Random Forest - Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300)
plt.show()

# --------------------------------------------------
# 10. ROC Curve
# --------------------------------------------------

plt.figure(figsize=(7, 5))

RocCurveDisplay.from_predictions(
    y_test,
    y_prob
)

plt.title("Random Forest - ROC Curve")
plt.tight_layout()
plt.savefig("roc_curve.png", dpi=300)
plt.show()

# --------------------------------------------------
# 11. Metric Comparison Visualization
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    results["Metric"],
    results["Score"]
)

plt.ylim(0, 1)
plt.xlabel("Evaluation Metrics")
plt.ylabel("Score")
plt.title("Random Forest Model Performance")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("evaluation_metrics.png", dpi=300)
plt.show()

print("\n" + "=" * 50)
print("DAY 21 MODEL EVALUATION COMPLETED!")
print("=" * 50)