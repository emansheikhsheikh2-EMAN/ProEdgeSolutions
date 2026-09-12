import json
from datetime import datetime

from src.config import (
    EXPERIMENT_PATH,
    MODEL_NAME,
    MODEL_VERSION,
    N_ESTIMATORS,
    RANDOM_STATE,
)


def record_experiment(metrics):
    """Save model training results and parameters."""

    EXPERIMENT_PATH.parent.mkdir(parents=True, exist_ok=True)

    if EXPERIMENT_PATH.exists():
        try:
            with open(EXPERIMENT_PATH, "r", encoding="utf-8") as file:
                experiments = json.load(file)
        except (json.JSONDecodeError, OSError):
            experiments = []
    else:
        experiments = []

    experiment = {
        "model_name": MODEL_NAME,
        "training_date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "model_version": MODEL_VERSION,
        "parameters": {
            "n_estimators": N_ESTIMATORS,
            "random_state": RANDOM_STATE,
        },
        "metrics": {
            key: round(value, 4)
            for key, value in metrics.items()
        },
    }

    experiments.append(experiment)

    with open(EXPERIMENT_PATH, "w", encoding="utf-8") as file:
        json.dump(experiments, file, indent=4)

    return experiment