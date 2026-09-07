import pandas as pd

from configs.config import (
    DATA_PATH,
    MODEL_PATH,
    TEST_SIZE,
    RANDOM_STATE,
    TARGET_COLUMN
)

from src.customer_churn.preprocessing import (
    load_data,
    preprocess_data,
    split_data,
    scale_data
)

from src.customer_churn.evaluation import (
    evaluate_model,
    print_metrics
)

from models.train_model import (
    train_models,
    save_model
)


def main():
    """Run the complete customer churn ML pipeline."""

    print("=" * 60)
    print("CUSTOMER CHURN PREDICTION - DAY 25")
    print("=" * 60)

    # 1. Load data
    print("\n1. Loading dataset...")
    df = load_data(DATA_PATH)

    print("Dataset Shape:", df.shape)

    # 2. Preprocess data
    print("\n2. Preprocessing data...")
    df = preprocess_data(df)

    print("Processed Shape:", df.shape)

    # 3. Split data
    print("\n3. Splitting data...")
    X_train, X_test, y_train, y_test = split_data(
        df,
        TARGET_COLUMN
    )

    print("Training Shape:", X_train.shape)
    print("Testing Shape:", X_test.shape)

    # 4. Scale data
    print("\n4. Scaling data...")
    X_train, X_test, scaler = scale_data(
        X_train,
        X_test
    )

    # 5. Train models
    print("\n5. Training models...")
    trained_models = train_models(
        X_train,
        y_train
    )

    # 6. Evaluate models
    print("\n6. Evaluating models...")

    results = []

    for name, model in trained_models.items():

        metrics = evaluate_model(
            model,
            X_test,
            y_test
        )

        print_metrics(name, metrics)

        results.append({
            "Model": name,
            **metrics
        })

        # Save trained model
        save_model(
            model,
            name,
            MODEL_PATH
        )

    # 7. Display results
    results_df = pd.DataFrame(results)

    print("\n" + "=" * 60)
    print("FINAL MODEL COMPARISON")
    print("=" * 60)

    print(results_df.to_string(index=False))

    print("\nDay-25 Professional ML Project Completed!")


if __name__ == "__main__":
    main()

   