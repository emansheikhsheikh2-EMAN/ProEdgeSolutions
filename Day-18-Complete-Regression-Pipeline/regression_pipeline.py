# ==========================================
# DAY 18 - COMPLETE REGRESSION PIPELINE
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(20))


# ==========================================
# 3. TARGET VARIABLE
# ==========================================

target = "SalePrice"

print("\nTarget Variable:", target)


# ==========================================
# 4. SUMMARY STATISTICS
# ==========================================

print("\nSummary Statistics:")
print(df.describe())


# ==========================================
# 5. EDA - TARGET DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))
plt.hist(df[target], bins=30)
plt.title("Sale Price Distribution")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("day-18-eda.png")
plt.show()


# ==========================================
# 6. FEATURE / TARGET SEPARATION
# ==========================================

X = df.drop(columns=[target])
y = df[target]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)


# ==========================================
# 7. IDENTIFY FEATURE TYPES
# ==========================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("\nNumber of Numerical Features:", len(numeric_features))
print("Number of Categorical Features:", len(categorical_features))


# ==========================================
# 8. TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ==========================================
# 9. PREPROCESSING
# ==========================================

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)


# ==========================================
# 10. PREPARE FEATURES
# ==========================================

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print("\nPreprocessing completed successfully!")
print("Processed Training Shape:", X_train_processed.shape)
print("Processed Testing Shape:", X_test_processed.shape)


# ==========================================
# 11. LINEAR REGRESSION MODEL
# ==========================================

model = LinearRegression()

model.fit(X_train_processed, y_train)

print("\nLinear Regression model trained successfully!")


# ==========================================
# 12. GENERATE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test_processed)

print("\nActual vs Predicted:")

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print(comparison.head(10))


# ==========================================
# 13. MODEL EVALUATION
# ==========================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n==========================================")
print("MODEL EVALUATION")
print("==========================================")

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

# ==========================================
# 14. ACTUAL VS PREDICTED GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(y_test, y_pred, alpha=0.6)

plt.xlabel("Actual Sale Price")
plt.ylabel("Predicted Sale Price")
plt.title("Actual vs Predicted Sale Prices")

plt.tight_layout()

plt.savefig("day-18-actual-vs-predicted.png")

plt.show()


# ==========================================
# 15. FINAL MESSAGE
# ==========================================

print("\n==========================================")
print("DAY 18 REGRESSION PIPELINE COMPLETED!")
print("==========================================")