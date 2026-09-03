import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 2. Select Features
# ==========================================

features = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked"
]

X = df[features].copy()
y = df["Survived"]


# ==========================================
# 3. Handle Missing Values
# ==========================================

X["Age"] = X["Age"].fillna(X["Age"].median())
X["Fare"] = X["Fare"].fillna(X["Fare"].median())
X["Embarked"] = X["Embarked"].fillna(X["Embarked"].mode()[0])


# ==========================================
# 4. Encode Categorical Features
# ==========================================

X = pd.get_dummies(
    X,
    columns=["Sex", "Embarked"],
    drop_first=True
)

print("\nProcessed Features:")
print(X.head())

print("\nProcessed Data Shape:", X.shape)


# ==========================================
# 5. Define Models
# ==========================================

decision_tree = DecisionTreeClassifier(
    random_state=42
)

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 6. K-Fold Cross-Validation
# ==========================================

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# ==========================================
# 7. Decision Tree Cross-Validation
# ==========================================

dt_scores = cross_val_score(
    decision_tree,
    X,
    y,
    cv=kf,
    scoring="accuracy"
)

print("\n======================================")
print("Decision Tree - 5 Fold Cross-Validation")
print("======================================")

for i, score in enumerate(dt_scores, start=1):
    print(f"Fold {i} Accuracy: {score:.4f}")

dt_mean = dt_scores.mean()
dt_std = dt_scores.std()

print(f"\nDecision Tree Average Accuracy: {dt_mean:.4f}")
print(f"Decision Tree Standard Deviation: {dt_std:.4f}")


# ==========================================
# 8. Random Forest Cross-Validation
# ==========================================

rf_scores = cross_val_score(
    random_forest,
    X,
    y,
    cv=kf,
    scoring="accuracy"
)

print("\n======================================")
print("Random Forest - 5 Fold Cross-Validation")
print("======================================")

for i, score in enumerate(rf_scores, start=1):
    print(f"Fold {i} Accuracy: {score:.4f}")

rf_mean = rf_scores.mean()
rf_std = rf_scores.std()

print(f"\nRandom Forest Average Accuracy: {rf_mean:.4f}")
print(f"Random Forest Standard Deviation: {rf_std:.4f}")


# ==========================================
# 9. Model Comparison
# ==========================================

print("\n======================================")
print("MODEL COMPARISON")
print("======================================")

print(f"Decision Tree Mean Accuracy : {dt_mean:.4f}")
print(f"Random Forest Mean Accuracy : {rf_mean:.4f}")

print(f"\nDecision Tree Std Dev       : {dt_std:.4f}")
print(f"Random Forest Std Dev       : {rf_std:.4f}")


# ==========================================
# 10. Determine Best Model
# ==========================================

if rf_mean > dt_mean:
    print("\nHigher Average Accuracy: Random Forest")
else:
    print("\nHigher Average Accuracy: Decision Tree")


if rf_std < dt_std:
    print("More Stable Model: Random Forest")
else:
    print("More Stable Model: Decision Tree")


# ==========================================
# 11. Visualization
# ==========================================

folds = np.arange(1, 6)

plt.figure(figsize=(10, 6))

plt.plot(
    folds,
    dt_scores,
    marker="o",
    label="Decision Tree"
)

plt.plot(
    folds,
    rf_scores,
    marker="o",
    label="Random Forest"
)

plt.axhline(
    dt_mean,
    linestyle="--",
    label="Decision Tree Average"
)

plt.axhline(
    rf_mean,
    linestyle="--",
    label="Random Forest Average"
)

plt.xlabel("Fold Number")
plt.ylabel("Accuracy")
plt.title("5-Fold Cross-Validation Model Comparison")
plt.xticks(folds)
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "cv_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 12. Final Summary
# ==========================================

print("\n======================================")
print("DAY 22 CROSS-VALIDATION COMPLETED!")
print("======================================")

print("\nDecision Tree Fold Scores:")
print(np.round(dt_scores, 4))

print("\nRandom Forest Fold Scores:")
print(np.round(rf_scores, 4))

print(f"\nDecision Tree Mean: {dt_mean:.4f}")
print(f"Random Forest Mean: {rf_mean:.4f}")

print(f"\nDecision Tree Std: {dt_std:.4f}")
print(f"Random Forest Std: {rf_std:.4f}")

print("\nGraph saved as: cv_comparison.png")