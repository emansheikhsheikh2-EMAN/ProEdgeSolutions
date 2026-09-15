from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning prediction API using the Day 30 trained model.",
    version="1.0.0",
)


# Load the trained model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model_v1.joblib"

model = joblib.load(MODEL_PATH)


# Pydantic request model
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int = Field(ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: int = Field(ge=0)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running",
        "endpoint": "/predict",
    }


@app.post("/predict")
def predict(data: CustomerData):
    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Yes"
    else:
        result = "No"

    return {
        "prediction": int(prediction),
        "churn": result,
    }