import logging
import os

import joblib
import pandas as pd
import redis
from fastapi import FastAPI, HTTPException

from src.config import MODEL_PATH
from src.logging_config import setup_logging
from src.models import CustomerData, PredictionResponse

logger = setup_logging()

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning Prediction API with Redis",
    version="1.0.0",
)

# Redis configuration
REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL:
    redis_client = redis.from_url(
        REDIS_URL,
        decode_responses=True,
    )
else:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        decode_responses=True,
    )

model = None

try:
    model = joblib.load(MODEL_PATH)
    logger.info("ML model loaded successfully from %s", MODEL_PATH)
except Exception as e:
    logger.error("Failed to load ML model: %s", e)


@app.get("/")
def root():
    logger.info("Root endpoint request received")
    return {
        "message": "Customer Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
    }


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


@app.get("/redis-health")
def redis_health():
    try:
        redis_client.ping()

        logger.info("Redis connection successful")

        return {
            "status": "connected",
            "message": "Redis service is available",
        }

    except Exception as e:
        logger.error("Redis connection failed: %s", e)

        raise HTTPException(
            status_code=503,
            detail="Redis service is not available",
        )


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
        input_data = customer.model_dump()

        input_df = pd.DataFrame([input_data])

        logger.info("Input data prepared successfully")

        prediction = model.predict(input_df)[0]

        prediction = int(prediction)

        churn = "Yes" if prediction == 1 else "No"

        # Store prediction count in Redis
        redis_client.incr("prediction_count")

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