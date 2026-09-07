
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    roc_auc_score
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 2. DATA CLEANING
# ============================================================

# Remove customer ID because it is not useful for prediction
df = df.drop("customerID", axis=1)

# Convert TotalCharges to numeric
# Invalid/blank values become NaN
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing TotalCharges with median
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Convert target column
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})


# ============================================================
# 3. SPLIT FEATURES AND TARGET
# ============================================================

X = df.drop("Churn", axis=1)
y = df["Churn"]


# ============================================================
# 4. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("\nNumerical Features:")
print(numerical_features)

print("\nCategorical Features:")
print(categorical_features)


# ============================================================
# 5. PREPROCESSING
# ============================================================

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "onehot",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)


# ============================================================
# 6. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ============================================================
# 7. DEFINE MODELS
# ============================================================

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
}


# ============================================================
# 8. TRAIN AND EVALUATE MODELS
# ============================================================

results = []

trained_models = {}

for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )
    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )
    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )
    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc
    })

    trained_models[name] = pipeline

    print("\n" + "=" * 55)
    print(name)
    print("=" * 55)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")


# ============================================================
# 9. SAVE EXPERIMENT RESULTS
# ============================================================

results_df = pd.DataFrame(results)

results_df.to_csv(
    "experiment_results.csv",
    index=False
)

print("\nExperiment Results:")
print(results_df)

print("\nSaved: experiment_results.csv")


# ============================================================
# 10. MODEL COMPARISON GRAPH
# ============================================================

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score",
    "ROC-AUC"
]

ax = results_df.set_index("Model")[metrics].plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Customer Churn Model Comparison")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.legend(loc="lower right")
plt.tight_layout()

plt.savefig(
    "model_comparison.png",
    dpi=300
)

plt.show()

print("Saved: model_comparison.png")


# ============================================================
# 11. SELECT BEST MODEL
# ============================================================

best_model_name = results_df.loc[
    results_df["F1 Score"].idxmax(),
    "Model"
]

best_model = trained_models[best_model_name]

print("\nBest Model:", best_model_name)


# ============================================================
# 12. CONFUSION MATRIX
# ============================================================

y_pred_best = best_model.predict(X_test)

cm = confusion_matrix(
    y_test,
    y_pred_best
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Churn", "Churn"]
)

disp.plot()

plt.title(
    f"Confusion Matrix - {best_model_name}"
)

plt.tight_layout()

plt.savefig(
    "confusion_matrix.png",
    dpi=300
)

plt.show()

print("Saved: confusion_matrix.png")


# ============================================================
# 13. ROC CURVE
# ============================================================

y_prob_best = best_model.predict_proba(
    X_test
)[:, 1]

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_prob_best
)

auc_score = roc_auc_score(
    y_test,
    y_prob_best
)

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc_score:.4f}"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title(
    f"ROC Curve - {best_model_name}"
)

plt.legend(loc="lower right")
plt.tight_layout()

plt.savefig(
    "roc_curve.png",
    dpi=300
)

plt.show()

print("Saved: roc_curve.png")


# ============================================================
# 14. FEATURE IMPORTANCE
# ============================================================

model_object = best_model.named_steps["model"]

feature_names = (
    best_model
    .named_steps["preprocessor"]
    .get_feature_names_out()
)

# Get feature importance based on model type
if best_model_name in ["Decision Tree", "Random Forest"]:

    importances = model_object.feature_importances_

else:
    # Logistic Regression uses coefficients
    importances = np.abs(model_object.coef_[0])


feature_importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

feature_importance_df = (
    feature_importance_df
    .sort_values(
        by="Importance",
        ascending=False
    )
    .head(15)
)


plt.figure(figsize=(10, 7))

plt.barh(
    feature_importance_df["Feature"][::-1],
    feature_importance_df["Importance"][::-1]
)

plt.xlabel("Importance")
plt.ylabel("Feature")

plt.title(
    f"Top Feature Importance - {best_model_name}"
)

plt.tight_layout()

plt.savefig(
    "feature_importance.png",
    dpi=300
)

plt.show()

print("Saved: feature_importance.png")

# ============================================================
# 15. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 55)
print("DAY 24 CUSTOMER CHURN PREDICTION COMPLETED")
print("=" * 55)

print("\nGenerated Files:")

print("1. experiment_results.csv")
print("2. model_comparison.png")
print("3. confusion_matrix.png")
print("4. roc_curve.png")
print("5. feature_importance.png")

