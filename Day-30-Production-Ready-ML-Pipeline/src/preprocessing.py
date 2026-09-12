import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


def load_data(file_path):
    """Load the Telco Customer Churn dataset."""
    return pd.read_csv(file_path)


def prepare_features(data, target_column="Churn"):
    """Separate features and target and prepare data types."""

    data = data.copy()

    # Remove customer ID because it is not useful for prediction
    if "customerID" in data.columns:
        data = data.drop(columns=["customerID"])

    # Convert TotalCharges to numeric
    if "TotalCharges" in data.columns:
        data["TotalCharges"] = pd.to_numeric(
            data["TotalCharges"], errors="coerce"
        )

    # Convert target from Yes/No to 1/0
    if target_column in data.columns:
        data[target_column] = data[target_column].map(
            {"Yes": 1, "No": 0}
        )

    X = data.drop(columns=[target_column])
    y = data[target_column]

    return X, y


def create_preprocessor(X):
    """Create reusable preprocessing pipeline."""

    numeric_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median"))
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                ),
            ),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_features),
            ("categorical", categorical_pipeline, categorical_features),
        ]
    )

    return preprocessor