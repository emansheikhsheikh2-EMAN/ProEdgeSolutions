import logging

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from src.config import MODEL_PATH
from src.logging_config import setup_logging
from src.models import CustomerData, PredictionResponse

logger = setup_logging()

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning Prediction API",
    version="1.0.0",
)

model = None

try:
    model = joblib.load(MODEL_PATH)
    logger.info("ML model loaded successfully from %s", MODEL_PATH)
except Exception as e:
    logger.error("Failed to load ML model: %s", e)


@app.get("/")
def root():
    return {
        "message": "Customer Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="ML model is not available",
        )

    return {
        "status": "healthy",
        "model_loaded": True,
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="ML model is not available",
        )

    try:
        input_data = customer.model_dump()
        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)[0]
        prediction = int(prediction)

        churn = "Yes" if prediction == 1 else "No"

        logger.info(
            "Prediction generated successfully: %s",
            prediction,
        )

        return PredictionResponse(
            prediction=prediction,
            churn=churn,
            message="Prediction generated successfully",
        )

    except Exception as e:
        logger.exception("Prediction error: %s", e)

        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating prediction",
        )