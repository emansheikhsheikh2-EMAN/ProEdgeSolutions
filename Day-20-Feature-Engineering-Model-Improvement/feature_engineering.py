import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nOriginal Columns:")
print(df.columns.tolist())


# ============================================================
# 2. BASELINE MODEL - DAY 19
# ============================================================

X_baseline = df[
    ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
]

y = df["Survived"]


X_train_base, X_test_base, y_train, y_test = train_test_split(
    X_baseline,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


numeric_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
categorical_features = ["Sex", "Embarked"]


numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


baseline_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)


baseline_model.fit(X_train_base, y_train)

baseline_pred = baseline_model.predict(X_test_base)


baseline_accuracy = accuracy_score(y_test, baseline_pred)
baseline_precision = precision_score(y_test, baseline_pred)
baseline_recall = recall_score(y_test, baseline_pred)
baseline_f1 = f1_score(y_test, baseline_pred)


print("\n" + "=" * 55)
print("BASELINE MODEL - DAY 19")
print("=" * 55)

print(f"Accuracy  : {baseline_accuracy:.4f}")
print(f"Precision : {baseline_precision:.4f}")
print(f"Recall    : {baseline_recall:.4f}")
print(f"F1 Score  : {baseline_f1:.4f}")


# ============================================================
# 3. FEATURE ENGINEERING
# ============================================================

df_engineered = df.copy()


# Family Size
df_engineered["FamilySize"] = (
    df_engineered["SibSp"]
    + df_engineered["Parch"]
    + 1
)


# Is Alone
df_engineered["IsAlone"] = np.where(
    df_engineered["FamilySize"] == 1,
    1,
    0
)


# Title extraction from Name
df_engineered["Title"] = (
    df_engineered["Name"]
    .str.extract(r",\s*([^.]*)\.", expand=False)
    .str.strip()
)


# Group rare titles
common_titles = [
    "Mr", "Miss", "Mrs", "Master"
]

df_engineered["Title"] = np.where(
    df_engineered["Title"].isin(common_titles),
    df_engineered["Title"],
    "Rare"
)


# Fare per person
df_engineered["FarePerPerson"] = (
    df_engineered["Fare"]
    / df_engineered["FamilySize"]
)


# Age Group
df_engineered["AgeGroup"] = pd.cut(
    df_engineered["Age"],
    bins=[0, 12, 18, 35, 60, np.inf],
    labels=[
        "Child",
        "Teenager",
        "YoungAdult",
        "Adult",
        "Senior"
    ]
)


print("\n" + "=" * 55)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 55)

print("\nNew Features:")
print("- FamilySize")
print("- IsAlone")
print("- Title")
print("- FarePerPerson")
print("- AgeGroup")


# ============================================================
# 4. REMOVE IRRELEVANT FEATURES
# ============================================================

X_engineered = df_engineered[
    [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "FamilySize",
        "IsAlone",
        "Title",
        "FarePerPerson",
        "AgeGroup"
    ]
]


X_train_eng, X_test_eng, y_train_eng, y_test_eng = train_test_split(
    X_engineered,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# 5. PREPROCESS ENGINEERED FEATURES
# ============================================================

numeric_features_eng = [
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "FamilySize",
    "IsAlone",
    "FarePerPerson"
]

categorical_features_eng = [
    "Sex",
    "Embarked",
    "Title",
    "AgeGroup"
]


numeric_transformer_eng = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)

categorical_transformer_eng = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)


preprocessor_eng = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer_eng, numeric_features_eng),
        ("cat", categorical_transformer_eng, categorical_features_eng)
    ]
)


# ============================================================
# 6. IMPROVED RANDOM FOREST
# ============================================================

improved_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor_eng),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)


improved_model.fit(X_train_eng, y_train_eng)


# ============================================================
# 7. NEW PREDICTIONS
# ============================================================

improved_pred = improved_model.predict(X_test_eng)


# ============================================================
# 8. IMPROVED MODEL EVALUATION
# ============================================================

improved_accuracy = accuracy_score(
    y_test_eng,
    improved_pred
)

improved_precision = precision_score(
    y_test_eng,
    improved_pred
)

improved_recall = recall_score(
    y_test_eng,
    improved_pred
)

improved_f1 = f1_score(
    y_test_eng,
    improved_pred
)


print("\n" + "=" * 55)
print("IMPROVED MODEL - AFTER FEATURE ENGINEERING")
print("=" * 55)

print(f"Accuracy  : {improved_accuracy:.4f}")
print(f"Precision : {improved_precision:.4f}")
print(f"Recall    : {improved_recall:.4f}")
print(f"F1 Score  : {improved_f1:.4f}")


# ============================================================
# 9. PERFORMANCE COMPARISON
# ============================================================

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]

baseline_scores = [
    baseline_accuracy,
    baseline_precision,
    baseline_recall,
    baseline_f1
]

improved_scores = [
    improved_accuracy,
    improved_precision,
    improved_recall,
    improved_f1
]


comparison = pd.DataFrame(
    {
        "Metric": metrics,
        "Baseline": baseline_scores,
        "After Feature Engineering": improved_scores
    }
)


print("\n" + "=" * 55)
print("PERFORMANCE COMPARISON")
print("=" * 55)

print(comparison.to_string(index=False))


# ============================================================
# 10. IMPROVEMENT
# ============================================================

print("\n" + "=" * 55)
print("IMPROVEMENT")
print("=" * 55)

for metric, baseline, improved in zip(
    metrics,
    baseline_scores,
    improved_scores
):
    difference = improved - baseline

    print(
        f"{metric}: "
        f"{difference:+.4f}"
    )


# ============================================================
# 11. MODEL COMPARISON GRAPH
# ============================================================

x = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    x - width / 2,
    baseline_scores,
    width,
    label="Baseline"
)

plt.bar(
    x + width / 2,
    improved_scores,
    width,
    label="After Feature Engineering"
)

plt.xticks(x, metrics)
plt.ylabel("Score")
plt.xlabel("Evaluation Metrics")
plt.title("Baseline vs Feature Engineered Random Forest")
plt.ylim(0, 1)
plt.legend()

plt.tight_layout()

plt.savefig(
    "day-20-model-comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 12. FEATURE IMPORTANCE GRAPH
# ============================================================

rf_model = improved_model.named_steps["classifier"]
preprocessor_fitted = improved_model.named_steps["preprocessor"]

feature_names = preprocessor_fitted.get_feature_names_out()

importances = rf_model.feature_importances_

importance_df = pd.DataFrame(
    {
        "Feature": feature_names,
        "Importance": importances
    }
).sort_values(
    by="Importance",
    ascending=False
).head(10)


plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"][::-1],
    importance_df["Importance"][::-1]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Top 10 Feature Importances")

plt.tight_layout()

plt.savefig(
    "day-20-feature-importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 13. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 55)
print("DAY 20 FEATURE ENGINEERING PROJECT COMPLETED!")
print("=" * 55)

print("\nFiles saved:")
print("- day-20-model-comparison.png")
print("- day-20-feature-importance.png")