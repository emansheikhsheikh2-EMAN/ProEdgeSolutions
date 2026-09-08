import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


# Load dataset
def load_data(file_path):
    return pd.read_csv(file_path)


# Create reusable ML pipeline
def create_pipeline(X):
    
    # Identify numerical and categorical features
    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    # Numerical preprocessing
    numerical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    # Categorical preprocessing
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore",
                    drop="first"
                )
            )
        ]
    )

    # ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_features
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features
            )
        ]
    )

    # Complete pipeline
    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                LogisticRegression(
                    max_iter=1000,
                    random_state=42
                )
            )
        ]
    )

    return model_pipeline


def main():

    # 1. Load dataset
    file_path = "data/train.csv"
    df = load_data(file_path)

    print("=" * 60)
    print("DAY 26 - REUSABLE MACHINE LEARNING PIPELINE")
    print("=" * 60)

    print("\nDataset Shape:", df.shape)

    # 2. Remove customerID
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    # 3. Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

    # 4. Separate features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"].map({
        "Yes": 1,
        "No": 0
    })

    # 5. Identify features
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

    # 6. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining Data Shape:", X_train.shape)
    print("Testing Data Shape:", X_test.shape)

    # 7. Create pipeline
    pipeline = create_pipeline(X_train)

    # 8. Train complete pipeline
    pipeline.fit(X_train, y_train)

    # 9. Generate predictions
    y_pred = pipeline.predict(X_test)

    # 10. Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n" + "=" * 60)
    print("PIPELINE EVALUATION")
    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    # 11. Test raw input prediction
    raw_input = X_test.iloc[[0]]

    raw_prediction = pipeline.predict(raw_input)

    print("\n" + "=" * 60)
    print("RAW INPUT PREDICTION")
    print("=" * 60)

    print("Raw Input:")
    print(raw_input)

    print("\nPrediction:", raw_prediction[0])

    if raw_prediction[0] == 1:
        print("Result: Customer is likely to Churn")
    else:
        print("Result: Customer is likely to Stay")

    # 12. Save complete pipeline
    model_path = "models/churn_pipeline.joblib"

    joblib.dump(pipeline, model_path)

    print("\n" + "=" * 60)
    print("PIPELINE SAVED SUCCESSFULLY")
    print("=" * 60)

    print(f"Model saved at: {model_path}")


if __name__ == "__main__":
    main()