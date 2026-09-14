from fastapi import FastAPI

app = FastAPI(
    title="Day 32 FastAPI Application",
    description="A minimal FastAPI application for the ProEdge Solutions AI/ML Internship.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Day 32 FastAPI Application",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI",
    }


@app.get("/api/info")
def api_info():
    return {
        "project": "Day 32 - FastAPI Application",
        "technology": "FastAPI",
        "documentation": "/docs",
    }