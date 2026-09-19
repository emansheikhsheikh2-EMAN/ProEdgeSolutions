from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def get_valid_customer():
    return {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "One year",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 65.5,
        "TotalCharges": 786.0,
    }


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Customer Churn Prediction API"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True


def test_prediction():
    response = client.post(
        "/predict",
        json=get_valid_customer(),
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "churn" in data
    assert "message" in data


def test_validation_error():
    invalid_customer = get_valid_customer()

    del invalid_customer["gender"]

    response = client.post(
        "/predict",
        json=invalid_customer,
    )

    assert response.status_code == 422