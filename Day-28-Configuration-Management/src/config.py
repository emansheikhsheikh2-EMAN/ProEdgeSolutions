import os
from dotenv import load_dotenv

load_dotenv()

DATASET_PATH = os.getenv("DATASET_PATH")
MODEL_PATH = os.getenv("MODEL_PATH")
PROJECT_NAME = os.getenv("PROJECT_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")
EXPERIMENT_PATH = os.getenv("EXPERIMENT_PATH")