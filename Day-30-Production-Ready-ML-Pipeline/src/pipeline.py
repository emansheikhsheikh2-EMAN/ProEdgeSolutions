import logging

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from src.config import (
    TEST_SIZE,
    RANDOM_STATE,
    N_ESTIMATORS,
    DATA_PATH,
)
from src.preprocessing import (
    load_data,
    prepare_features,
    create_preprocessor,
)
from src.model_manager import save_model
from src.experiment_tracking import record_experiment


logger = logging.getLogger(__name__)


def build_pipeline(X):
    """Build the complete preprocessing and ML pipeline."""

    preprocessor = create_preprocessor(X)

    model = RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    return pipeline


def train_model():
    """Train, evaluate, save, and track the ML model."""

    logger.info("Loading training data.")

    data = load_data(DATA_PATH)

    X, y = prepare_features(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    logger.info("Building machine learning pipeline.")

    pipeline = build_pipeline(X_train)

    logger.info("Starting model training.")

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "recall": recall_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "f1_score": f1_score(
            y_test,
            predictions,
            zero_division=0,
        ),
    }

    logger.info("Model training completed.")
    logger.info("Evaluation metrics: %s", metrics)

    save_model(pipeline)
    record_experiment(metrics)

    logger.info("Model saved and experiment recorded.")

    return pipeline, metrics, X_test, y_test


if __name__ == "__main__":
    from src.logging_config import setup_logging

    setup_logging()

    pipeline, metrics, _, _ = train_model()

    print("\nMODEL TRAINING COMPLETED")
    print("------------------------")
    print(f"Accuracy : {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall   : {metrics['recall']:.4f}")
    print(f"F1 Score : {metrics['f1_score']:.4f}")