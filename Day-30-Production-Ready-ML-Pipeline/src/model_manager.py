import logging
import joblib

from src.config import MODEL_PATH


logger = logging.getLogger(__name__)


def save_model(model):
    """Save the trained model to the models directory."""

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    logger.info("Model saved successfully: %s", MODEL_PATH)


def load_model():
    """Load the saved model from disk."""

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Saved model not found: {MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)

    logger.info("Model loaded successfully: %s", MODEL_PATH)

    return model


def predict(model, input_data):
    """Generate predictions using the trained model."""

    predictions = model.predict(input_data)

    logger.info(
        "Prediction generated successfully for %d records.",
        len(input_data),
    )

    return predictions