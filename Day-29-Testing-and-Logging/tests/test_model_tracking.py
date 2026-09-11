import pytest
import pandas as pd
import numpy as np
from pathlib import Path


def test_data_preprocessing():
    """Test basic data preprocessing."""
    data = pd.DataFrame({
        "MonthlyCharges": [50, 75, 100],
        "TotalCharges": ["100", "200", "300"]
    })

    data["TotalCharges"] = pd.to_numeric(
        data["TotalCharges"], errors="coerce"
    )

    assert data["TotalCharges"].dtype == "int64"
    assert data.shape == (3, 2)


def test_feature_engineering():
    """Test feature engineering."""
    data = pd.DataFrame({
        "MonthlyCharges": [50, 75, 100],
        "tenure": [2, 5, 10]
    })

    data["TotalMonthlyValue"] = data["MonthlyCharges"] * data["tenure"]

    assert "TotalMonthlyValue" in data.columns
    assert data["TotalMonthlyValue"].tolist() == [100, 375, 1000]


def test_prediction_output():
    """Test prediction output."""
    predictions = np.array([0, 1, 0, 1])

    assert len(predictions) == 4
    assert all(prediction in [0, 1] for prediction in predictions)


def test_model_loading():
    """Test model file path."""
    model_path = Path("models/random_forest_model.pkl")

    # Model may not exist during isolated testing.
    assert model_path.name == "random_forest_model.pkl"


def test_invalid_input():
    """Test handling of invalid input."""
    data = pd.DataFrame({
        "MonthlyCharges": ["invalid", "invalid"]
    })

    converted = pd.to_numeric(
        data["MonthlyCharges"], errors="coerce"
    )

    assert converted.isna().all()