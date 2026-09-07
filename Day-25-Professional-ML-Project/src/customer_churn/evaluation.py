from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


def evaluate_model(model, X_test, y_test):
    """Evaluate a trained classification model."""

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(
            y_test, y_pred, zero_division=0
        ),
        "Recall": recall_score(
            y_test, y_pred, zero_division=0
        ),
        "F1 Score": f1_score(
            y_test, y_pred, zero_division=0
        ),
        "ROC-AUC": roc_auc_score(
            y_test, y_prob
        )
    }

    return metrics


def print_metrics(model_name, metrics):
    """Print model evaluation metrics."""

    print("\n" + "=" * 50)
    print(model_name)
    print("=" * 50)

    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")