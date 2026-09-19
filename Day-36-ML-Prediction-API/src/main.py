import logging

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from src.config import MODEL_PATH
from src.logging_config import setup_logging
from src.models import CustomerData, PredictionResponse


# --------------------------------------------------
# Logging
# --------------------------------------------------

logger = setup_logging()


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning Prediction API for Customer Churn Prediction",
    version="1.0.0",
)


# --------------------------------------------------
# Load Machine Learning Model
# --------------------------------------------------

model = None

try:
    model = joblib.load(MODEL_PATH)
    logger.info("ML model loaded successfully from %s", MODEL_PATH)

except Exception as e:
    logger.error("Failed to load ML model: %s", e)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def root():
    logger.info("Root endpoint request received")

    return {
        "message": "Customer Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
    }


# --------------------------------------------------
# Health Check Endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():
    logger.info("Health check request received")

    if model is None:
        logger.error("Health check failed: ML model is not loaded")

        raise HTTPException(
            status_code=503,
            detail="ML model is not available",
        )

    return {
        "status": "healthy",
        "model_loaded": True,
    }


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):
    logger.info("Prediction request received")

    if model is None:
        logger.error("Prediction failed: ML model is not loaded")

        raise HTTPException(
            status_code=503,
            detail="ML model is not available",
        )

    try:
        # Convert validated Pydantic data into dictionary
        input_data = customer.model_dump()

        # Convert input into DataFrame
        # This preserves the feature/column names expected by
        # the Day 30 ML pipeline.
        input_df = pd.DataFrame([input_data])

        logger.info("Input data prepared successfully")

        # Generate prediction
        prediction = model.predict(input_df)[0]
        prediction = int(prediction)

        # Convert prediction into readable churn result
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