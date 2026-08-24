import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Titanic Dataset
df = pd.read_csv("train.csv")

# 2. Explore Dataset
print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 3. Basic Statistics
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# 4. Target Variable
target = "Survived"

print("\n===== TARGET VARIABLE =====")
print(target)

# 5. Select Features
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]

print("\n===== FEATURES =====")
print(features)

# Prepare data
X = df[features].copy()
y = df[target]

# Convert Sex into numerical values
X["Sex"] = X["Sex"].map({"male": 0, "female": 1})

# Fill missing Age values
X["Age"] = X["Age"].fillna(X["Age"].median())

# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n===== TRAIN-TEST SPLIT =====")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# 7. Train Baseline Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Generate Predictions
y_pred = model.predict(X_test)

# 9. Evaluate Model
accuracy = accuracy_score(y_test, y_pred)

print("\n===== MODEL RESULTS =====")
print("Accuracy:", round(accuracy * 100, 2), "%")

print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(y_test, y_pred))

# 10. Basic Visualization
df["Survived"].value_counts().plot(kind="bar")

plt.title("Titanic Survival Distribution")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()