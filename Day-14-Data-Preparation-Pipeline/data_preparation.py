import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# 1. Load the Titanic dataset
df = pd.read_csv("train.csv")

print("=" * 60)
print("TITANIC DATA PREPARATION PIPELINE")
print("=" * 60)

# 2. Data Inspection
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Separate features and target
# Survived is the target variable
X = df.drop("Survived", axis=1)
y = df["Survived"]

# 4. Drop columns that are not useful for the model
X = X.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)

# 5. Identify numerical and categorical features
numerical_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
categorical_features = ["Sex", "Embarked"]

print("\nNumerical Features:")
print(numerical_features)

print("\nCategorical Features:")
print(categorical_features)

# 6. Train-Test Split BEFORE preprocessing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split:")
print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training target:", y_train.shape)
print("Testing target:", y_test.shape)

# 7. Numerical preprocessing
# Missing numerical values are replaced with the median.
# Scaling is fitted only on training data through the pipeline.
numerical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

# 8. Categorical preprocessing
# Missing categorical values are replaced with the most frequent value.
# Categorical values are converted into numerical values using OneHotEncoder.
categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ]
)

# 9. Combine numerical and categorical preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("numerical", numerical_pipeline, numerical_features),
        ("categorical", categorical_pipeline, categorical_features)
    ]
)

# 10. Create the complete preprocessing pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor)
    ]
)

# 11. Fit ONLY on training data
X_train_prepared = pipeline.fit_transform(X_train)

# 12. Transform testing data using the fitted preprocessing pipeline
X_test_prepared = pipeline.transform(X_test)

# 13. Display final prepared data information
print("\nPrepared Data:")
print("Prepared training data shape:", X_train_prepared.shape)
print("Prepared testing data shape:", X_test_prepared.shape)

print("\nTarget Distribution:")
print(y_train.value_counts())

print("\nData Preparation Completed Successfully!")

print("\nData Leakage Prevention:")
print("- Train-test split was performed before preprocessing.")
print("- Imputers, scaler, and encoder were fitted only on training data.")
print("- The testing data was transformed using the fitted training objects.")
print("- No information from the test set was used during preprocessing.")

print("=" * 60)