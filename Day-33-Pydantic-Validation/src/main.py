from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Day 33 Pydantic Validation API",
    description="FastAPI application with Pydantic request and response validation.",
    version="1.0.0",
)


# Request Model
class UserRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=1, le=100)
    email: str
    city: str = Field(..., min_length=2, max_length=50)


# Response Model
class UserResponse(BaseModel):
    message: str
    status: str
    user: UserRequest


@app.get("/")
def home():
    return {
        "message": "Welcome to Day 33 Pydantic Validation API",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI",
    }


@app.post("/users", response_model=UserResponse)
def create_user(user: UserRequest):
    return {
        "message": "User created successfully",
        "status": "success",
        "user": user,
    }