import json


API_CONTRACT = {
    "api_name": "Customer Churn Prediction API",
    "version": "v1",
    "base_url": "/api/v1",
    "format": "JSON",

    "endpoints": {
        "health": {
            "method": "GET",
            "path": "/api/v1/health",
            "description": "Checks whether the prediction API is running.",
            "request_body": None,
            "success_status": 200,
            "response_schema": {
                "status": "string",
                "service": "string",
                "version": "string"
            },
            "sample_response": {
                "status": "healthy",
                "service": "Customer Churn Prediction API",
                "version": "1.0.0"
            }
        },

        "prediction": {
            "method": "POST",
            "path": "/api/v1/predict",
            "description": "Accepts customer data and returns a churn prediction.",
            "request_schema": {
                "tenure": "number",
                "MonthlyCharges": "number",
                "TotalCharges": "number",
                "Contract": "string",
                "InternetService": "string",
                "OnlineSecurity": "string",
                "TechSupport": "string",
                "PaymentMethod": "string"
            },
            "sample_request": {
                "tenure": 12,
                "MonthlyCharges": 70.35,
                "TotalCharges": 844.20,
                "Contract": "Month-to-month",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "TechSupport": "No",
                "PaymentMethod": "Electronic check"
            },
            "success_status": 200,
            "response_schema": {
                "prediction": "string",
                "churn_probability": "number",
                "model_version": "string"
            },
            "sample_response": {
                "prediction": "Yes",
                "churn_probability": 0.78,
                "model_version": "v1"
            }
        }
    },

    "status_codes": {
        "200": "OK - Request completed successfully",
        "400": "Bad Request - Invalid request data",
        "404": "Not Found - Endpoint does not exist",
        "422": "Unprocessable Entity - Validation error",
        "500": "Internal Server Error",
        "503": "Service Unavailable - API or model unavailable"
    },

    "error_response": {
        "error": {
            "code": "VALIDATION_ERROR",
            "message": "Invalid input data",
            "details": "tenure must be a non-negative number"
        }
    }
}


def display_contract():
    """Display the REST API contract in a readable format."""

    print("=" * 65)
    print("DAY 31 - REST API CONTRACT")
    print("=" * 65)

    print(f"\nAPI Name     : {API_CONTRACT['api_name']}")
    print(f"Version      : {API_CONTRACT['version']}")
    print(f"Base URL     : {API_CONTRACT['base_url']}")
    print(f"Data Format  : {API_CONTRACT['format']}")

    print("\n" + "-" * 65)
    print("ENDPOINTS")
    print("-" * 65)

    for name, endpoint in API_CONTRACT["endpoints"].items():
        print(f"\n{name.upper()}")
        print(f"Method       : {endpoint['method']}")
        print(f"Path         : {endpoint['path']}")
        print(f"Description  : {endpoint['description']}")
        print(f"Success Code : {endpoint['success_status']}")

    print("\n" + "-" * 65)
    print("HTTP STATUS CODES")
    print("-" * 65)

    for code, description in API_CONTRACT["status_codes"].items():
        print(f"{code} : {description}")

    print("\n" + "-" * 65)
    print("SAMPLE PREDICTION REQUEST")
    print("-" * 65)

    print(
        json.dumps(
            API_CONTRACT["endpoints"]["prediction"]["sample_request"],
            indent=2
        )
    )

    print("\n" + "-" * 65)
    print("SAMPLE PREDICTION RESPONSE")
    print("-" * 65)

    print(
        json.dumps(
            API_CONTRACT["endpoints"]["prediction"]["sample_response"],
            indent=2
        )
    )

    print("\n" + "-" * 65)
    print("ERROR RESPONSE")
    print("-" * 65)

    print(json.dumps(API_CONTRACT["error_response"], indent=2))

    print("\n" + "=" * 65)
    print("API CONTRACT DESIGN COMPLETED SUCCESSFULLY")
    print("=" * 65)


if __name__ == "__main__":
    display_contract()