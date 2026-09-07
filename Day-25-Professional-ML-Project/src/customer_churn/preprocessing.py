import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """Load customer churn dataset."""
    df = pd.read_csv(file_path)
    return df


def preprocess_data(df):
    """Clean and prepare customer churn data."""

    # Remove unnecessary columns
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"], errors="coerce"
        )

    # Fill missing numerical values
    df = df.fillna(df.median(numeric_only=True))

    # Convert target column
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Convert categorical columns using one-hot encoding
    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    df = pd.get_dummies(
        df,
        columns=categorical_columns,
        drop_first=True
    )

    return df


def split_data(df, target_column="Churn"):
    """Split data into training and testing sets."""

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    """Scale numerical features."""

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler