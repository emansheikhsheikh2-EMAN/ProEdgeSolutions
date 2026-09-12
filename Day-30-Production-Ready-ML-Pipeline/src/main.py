from src.logging_config import setup_logging
from src.pipeline import train_model
from src.model_manager import load_model, predict
from src.preprocessing import load_data, prepare_features
from src.config import DATA_PATH


def main():
    setup_logging()

    print("=" * 50)
    print("DAY 30 - PRODUCTION-READY ML PIPELINE")
    print("=" * 50)

    # Train model
    _, metrics, _, _ = train_model()

    print("\nMODEL TRAINING COMPLETED")
    print("------------------------")
    print(f"Accuracy : {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall   : {metrics['recall']:.4f}")
    print(f"F1 Score : {metrics['f1_score']:.4f}")

    # Load saved model
    loaded_model = load_model()

    # Load raw data
    raw_data = load_data(DATA_PATH)

    X, _ = prepare_features(raw_data)

    # Generate predictions
    sample_input = X.head(5)

    predictions = predict(
        loaded_model,
        sample_input
    )

    print("\nSAVED MODEL PREDICTION TEST")
    print("---------------------------")
    print(f"Input records : {len(sample_input)}")
    print(f"Predictions   : {predictions.tolist()}")

    print("\nPIPELINE EXECUTION SUCCESSFUL")


if __name__ == "__main__":
    main()