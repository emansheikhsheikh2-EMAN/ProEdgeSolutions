import pandas as pd

from src.preprocessing import prepare_features, create_preprocessor


def test_prepare_features():
    data = pd.DataFrame(
        {
            "customerID": ["001", "002"],
            "tenure": [10, 20],
            "MonthlyCharges": [50.0, 70.0],
            "TotalCharges": ["500", "1400"],
            "Contract": ["Month-to-month", "One year"],
            "Churn": ["Yes", "No"],
        }
    )

    X, y = prepare_features(data)

    assert "customerID" not in X.columns
    assert X["TotalCharges"].dtype != "object"
    assert list(y) == [1, 0]


def test_create_preprocessor():
    data = pd.DataFrame(
        {
            "tenure": [10, 20],
            "MonthlyCharges": [50.0, 70.0],
            "Contract": ["Month-to-month", "One year"],
        }
    )

    preprocessor = create_preprocessor(data)

    assert preprocessor is not None
    assert len(preprocessor.transformers) == 2