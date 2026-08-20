import pandas as pd


def load_data(file_path):
    """Load student data from CSV file."""
    return pd.read_csv(file_path)


def show_summary(df, title):
    """Display dataset summary."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print("\nDataset:")
    print(df)

    print("\nShape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:", df.duplicated().sum())


def validate_before_cleaning(df):
    """Check data quality issues before cleaning."""
    issues = {}

    issues["Missing Values"] = int(df.isnull().sum().sum())
    issues["Duplicate Records"] = int(df.duplicated().sum())

    # Check invalid age values
    age_numeric = pd.to_numeric(df["Age"], errors="coerce")
    issues["Invalid Age Values"] = int(age_numeric.isnull().sum())

    return issues


def clean_data(df):
    """Clean and standardize the student dataset."""
    cleaned_df = df.copy()

    # 1. Remove extra spaces from text columns
    text_columns = ["Student_ID", "Name", "Gender", "Department"]

    for column in text_columns:
        cleaned_df[column] = cleaned_df[column].astype(str).str.strip()

    # 2. Standardize gender values
    cleaned_df["Gender"] = cleaned_df["Gender"].str.title()

    # 3. Standardize department names
    cleaned_df["Department"] = cleaned_df["Department"].str.strip().str.title()

    # 4. Convert Age to numeric
    cleaned_df["Age"] = pd.to_numeric(cleaned_df["Age"], errors="coerce")

    # 5. Convert Marks to numeric
    cleaned_df["Marks"] = pd.to_numeric(cleaned_df["Marks"], errors="coerce")

    # 6. Fill missing Age with median
    cleaned_df["Age"] = cleaned_df["Age"].fillna(cleaned_df["Age"].median())

    # 7. Fill missing Marks with mean
    cleaned_df["Marks"] = cleaned_df["Marks"].fillna(
        cleaned_df["Marks"].mean()
    )

    # 8. Remove duplicate records
    cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)

    return cleaned_df


def validate_after_cleaning(df):
    """Check data quality after cleaning."""
    issues = {}

    issues["Missing Values"] = int(df.isnull().sum().sum())
    issues["Duplicate Records"] = int(df.duplicated().sum())

    # Check data types
    issues["Invalid Age Values"] = int(
        pd.to_numeric(df["Age"], errors="coerce").isnull().sum()
    )

    issues["Invalid Marks Values"] = int(
        pd.to_numeric(df["Marks"], errors="coerce").isnull().sum()
    )

    return issues


def generate_cleaning_report(before, after):
    """Display cleaning operations report."""
    print("\n" + "=" * 60)
    print("CLEANING REPORT")
    print("=" * 60)

    print(f"Missing values found: {before['Missing Values']}")
    print(f"Missing values remaining: {after['Missing Values']}")

    print(f"\nDuplicate records found: {before['Duplicate Records']}")
    print(f"Duplicate records remaining: {after['Duplicate Records']}")

    print(f"\nInvalid age values found: {before['Invalid Age Values']}")
    print(f"Invalid age values remaining: {after['Invalid Age Values']}")

    print("\nCleaning Operations Performed:")
    print("1. Removed extra spaces from text values")
    print("2. Standardized gender formatting")
    print("3. Standardized department formatting")
    print("4. Converted Age to numeric")
    print("5. Converted Marks to numeric")
    print("6. Filled missing Age values with median")
    print("7. Filled missing Marks values with mean")
    print("8. Removed duplicate records")

    print("\nData cleaning completed successfully!")


def main():
    file_path = "student_data.csv"

    # Load dataset
    df = load_data(file_path)

    # Before cleaning
    show_summary(df, "DATASET SUMMARY BEFORE CLEANING")
    before_issues = validate_before_cleaning(df)

    # Clean dataset
    cleaned_df = clean_data(df)

    # Save cleaned dataset
    cleaned_df.to_csv("cleaned_student_data.csv", index=False)

    # After cleaning
    show_summary(cleaned_df, "DATASET SUMMARY AFTER CLEANING")
    after_issues = validate_after_cleaning(cleaned_df)

    # Cleaning report
    generate_cleaning_report(before_issues, after_issues)


if __name__ == "__main__":
    main()