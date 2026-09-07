import os
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def train_models(X_train, y_train):
    """Train multiple classification models."""

    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "decision_tree": DecisionTreeClassifier(random_state=42),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    }

    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models


def save_model(model, model_name, model_path="models"):
    """Save trained model to disk."""

    os.makedirs(model_path, exist_ok=True)

    file_path = os.path.join(
        model_path,
        f"{model_name}.joblib"
    )

    joblib.dump(model, file_path)

    print(f"Saved model: {file_path}")