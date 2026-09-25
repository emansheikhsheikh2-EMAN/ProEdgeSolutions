from fastapi import FastAPI

from src.config import settings


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get("/")
def root():
    return {
        "message": "ML Prediction API is running",
        "environment": settings.environment,
        "debug": settings.debug,
        "log_level": settings.log_level,
        "service_url": settings.service_url,
        "model_path": settings.model_path,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }