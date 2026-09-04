# Day 23 - Hyperparameter Tuning with Random Forest

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ---------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())


# ---------------------------------------------------
# 2. Data Preprocessing
# ---------------------------------------------------

# Remove unnecessary columns
columns_to_drop = ["PassengerId", "Name", "Ticket", "Cabin"]

df = df.drop(columns=columns_to_drop, errors="ignore")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Convert categorical columns into numerical values
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

# Separate features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Convert boolean columns to integers
X = X.astype(int)


# ---------------------------------------------------
# 3. Train-Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ---------------------------------------------------
# 4. Baseline Random Forest Model
# ---------------------------------------------------

baseline_model = RandomForestClassifier(random_state=42)

baseline_model.fit(X_train, y_train)

baseline_predictions = baseline_model.predict(X_test)


# ---------------------------------------------------
# 5. Baseline Evaluation
# ---------------------------------------------------

baseline_accuracy = accuracy_score(y_test, baseline_predictions)
baseline_precision = precision_score(y_test, baseline_predictions)
baseline_recall = recall_score(y_test, baseline_predictions)
baseline_f1 = f1_score(y_test, baseline_predictions)

print("\n" + "=" * 50)
print("BASELINE RANDOM FOREST RESULTS")
print("=" * 50)

print(f"Accuracy  : {baseline_accuracy:.4f}")
print(f"Precision : {baseline_precision:.4f}")
print(f"Recall    : {baseline_recall:.4f}")
print(f"F1 Score  : {baseline_f1:.4f}")

print("\nBaseline Confusion Matrix:")
print(confusion_matrix(y_test, baseline_predictions))


# ---------------------------------------------------
# 6. Hyperparameter Tuning using GridSearchCV
# ---------------------------------------------------

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

rf = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

print("\n" + "=" * 50)
print("STARTING HYPERPARAMETER TUNING...")
print("=" * 50)

grid_search.fit(X_train, y_train)


# ---------------------------------------------------
# 7. Best Parameters
# ---------------------------------------------------

print("\nBest Parameters:")
print(grid_search.best_params_)

print(f"\nBest Cross-Validation Score: "
      f"{grid_search.best_score_:.4f}")


# ---------------------------------------------------
# 8. Optimized Random Forest Model
# ---------------------------------------------------

optimized_model = grid_search.best_estimator_

optimized_predictions = optimized_model.predict(X_test)


# ---------------------------------------------------
# 9. Optimized Model Evaluation
# ---------------------------------------------------

optimized_accuracy = accuracy_score(
    y_test,
    optimized_predictions
)

optimized_precision = precision_score(
    y_test,
    optimized_predictions
)

optimized_recall = recall_score(
    y_test,
    optimized_predictions
)

optimized_f1 = f1_score(
    y_test,
    optimized_predictions
)

print("\n" + "=" * 50)
print("OPTIMIZED RANDOM FOREST RESULTS")
print("=" * 50)

print(f"Accuracy  : {optimized_accuracy:.4f}")
print(f"Precision : {optimized_precision:.4f}")
print(f"Recall    : {optimized_recall:.4f}")
print(f"F1 Score  : {optimized_f1:.4f}")

print("\nOptimized Confusion Matrix:")
print(confusion_matrix(y_test, optimized_predictions))


# ---------------------------------------------------
# 10. Performance Improvement
# ---------------------------------------------------

accuracy_improvement = (
    optimized_accuracy - baseline_accuracy
) * 100

print("\n" + "=" * 50)
print("PERFORMANCE COMPARISON")
print("=" * 50)

print(f"Baseline Accuracy   : {baseline_accuracy:.4f}")
print(f"Optimized Accuracy  : {optimized_accuracy:.4f}")
print(f"Accuracy Improvement: {accuracy_improvement:.2f}%")


if optimized_accuracy > baseline_accuracy:
    print("\nResult: Hyperparameter tuning improved the model.")
elif optimized_accuracy < baseline_accuracy:
    print("\nResult: Baseline model performed better.")
else:
    print("\nResult: Both models achieved the same accuracy.")


# ---------------------------------------------------
# 11. Comparison Graph
# ---------------------------------------------------

models = [
    "Default Random Forest",
    "Optimized Random Forest"
]

accuracies = [
    baseline_accuracy,
    optimized_accuracy
]

plt.figure(figsize=(8, 5))

bars = plt.bar(models, accuracies)

plt.title("Default vs Optimized Random Forest")
plt.ylabel("Accuracy")
plt.ylim(0, 1)

for bar, accuracy in zip(bars, accuracies):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.02,
        f"{accuracy:.3f}",
        ha="center"
    )

plt.tight_layout()

plt.savefig("rf_tuning_comparison.png", dpi=300)

plt.show()


# ---------------------------------------------------
# 12. Completion Message
# ---------------------------------------------------

print("\n" + "=" * 50)
print("DAY 23 RANDOM FOREST TUNING COMPLETED!")
print("=" * 50)
print("Comparison graph saved as: rf_tuning_comparison.png")