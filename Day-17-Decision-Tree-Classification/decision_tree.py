import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)
# Load dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())
# Explore dataset structure
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
# Handle missing values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin because it has too many missing values
df = df.drop("Cabin", axis=1)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# Prepare features and target variable

X = df.drop(["Survived", "PassengerId", "Name", "Ticket"], axis=1)
y = df["Survived"]

# Convert categorical columns into numerical values
X = pd.get_dummies(X, columns=["Sex", "Embarked"], drop_first=True)

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
from sklearn.tree import DecisionTreeClassifier

# Train Decision Tree model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print("\nDecision Tree model trained successfully!")
# Generate predictions on test data

y_pred = model.predict(X_test)

print("\nPredictions generated successfully!")

print("\nActual vs Predicted:")
print(pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
}).head(10))
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Evaluate model performance

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel Evaluation:")
print("Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1 Score:", round(f1, 4))

print("\nConfusion Matrix:")
print(cm)
# Experiment with different tree depths

depths = [2, 3, 5, 10, None]

print("\n========== TREE DEPTH EXPERIMENT ==========")

for depth in depths:
    tree = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    tree.fit(X_train, y_train)

    train_accuracy = tree.score(X_train, y_train)
    test_accuracy = tree.score(X_test, y_test)

    print(f"\nMax Depth: {depth}")
    print(f"Training Accuracy: {train_accuracy:.4f}")
    print(f"Testing Accuracy:  {test_accuracy:.4f}")