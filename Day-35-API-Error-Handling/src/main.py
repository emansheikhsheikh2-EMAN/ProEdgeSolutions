from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Machine Learning prediction API with error handling.",
    version="1.1.0",
)


# Model path
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model_v1.joblib"


# Load the trained model safely
try:
    model = joblib.load(MODEL_PATH)
    model_load_error = None
except Exception as e:
    model = None
    model_load_error = str(e)


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


# Handle invalid or incomplete request data
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "message": "Invalid or incomplete request data.",
            "details": exc.errors(),
        },
    )


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running",
        "endpoint": "/predict",
    }


@app.post("/predict")
def predict(data: CustomerData):

    # Handle model loading failure
    if model is None:
        return JSONResponse(
            status_code=500,
            content={
                "error": "Model Loading Error",
                "message": "The machine learning model could not be loaded.",
                "details": model_load_error,
            },
        )

    try:
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

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": "Prediction Error",
                "message": "An error occurred while generating the prediction.",
                "details": str(e),
            },
        )