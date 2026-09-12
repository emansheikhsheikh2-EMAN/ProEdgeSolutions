import pandas as pd

from src.pipeline import build_pipeline


def test_pipeline_prediction():
    data = pd.DataFrame(
        {
            "tenure": [10, 20, 30, 40],
            "MonthlyCharges": [50.0, 60.0, 70.0, 80.0],
            "TotalCharges": [500.0, 1200.0, 2100.0, 3200.0],
            "Contract": [
                "Month-to-month",
                "One year",
                "Two year",
                "Month-to-month",
            ],
        }
    )

    target = [1, 0, 0, 1]

    pipeline = build_pipeline(data)

    pipeline.fit(data, target)

    predictions = pipeline.predict(data)

    assert len(predictions) == len(data)
    assert all(prediction in [0, 1] for prediction in predictions)