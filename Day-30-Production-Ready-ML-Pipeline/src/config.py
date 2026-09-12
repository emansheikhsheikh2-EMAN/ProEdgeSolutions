import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / "configs" / ".env"

load_dotenv(ENV_FILE)

TEST_SIZE = float(os.getenv("TEST_SIZE", "0.2"))
RANDOM_STATE = int(os.getenv("RANDOM_STATE", "42"))
N_ESTIMATORS = int(os.getenv("N_ESTIMATORS", "200"))
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")
TARGET_COLUMN = os.getenv("TARGET_COLUMN", "Churn")
MODEL_NAME = os.getenv("MODEL_NAME", "RandomForest")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DATA_PATH = BASE_DIR / "data" / "train.csv"
MODEL_PATH = BASE_DIR / "models" / f"churn_model_{MODEL_VERSION}.joblib"
LOG_PATH = BASE_DIR / "logs" / "application.log"
EXPERIMENT_PATH = BASE_DIR / "experiments" / "experiment_results.json"
