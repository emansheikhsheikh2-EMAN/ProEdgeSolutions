# Day 20 – Feature Engineering for Model Improvement

## 📌 Project Overview

This project focuses on improving a Machine Learning model using Feature Engineering techniques.

The same Titanic dataset and Random Forest Classifier from Day 19 were used as the baseline. New features were created and the model was retrained to compare its performance before and after feature engineering.

---

## 🎯 Objective

* Use the Day 19 Random Forest model as a baseline.
* Create meaningful new features.
* Transform existing features.
* Handle categorical variables.
* Remove irrelevant features.
* Train an improved Random Forest model.
* Compare baseline and improved performance.

---

## 📊 Dataset

**Dataset:** Titanic Dataset

**Dataset Shape:** `891 rows × 12 columns`

**Target Variable:** `Survived`

---

## 🌳 Baseline Model

The Random Forest Classifier from Day 19 was used as the baseline model.

### Baseline Results

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 81.56% |
| Precision | 81.03% |
| Recall    | 68.12% |
| F1 Score  | 74.02% |

---

## ⚙️ Feature Engineering Techniques

The following features were created:

### 1. FamilySize

Family size was calculated using the number of siblings/spouses and parents/children travelling with the passenger.

```text
FamilySize = SibSp + Parch + 1
```

This feature helps identify the total number of people in a passenger's family group.

### 2. IsAlone

This feature identifies whether a passenger was travelling alone.

```text
IsAlone = 1 if FamilySize == 1 else 0
```

* `1` → Passenger was travelling alone
* `0` → Passenger was travelling with family

### 3. Title

Passenger titles were extracted from the `Name` column.

Common titles such as:

* Mr
* Miss
* Mrs
* Master

were kept, while uncommon titles were grouped into:

```text
Rare
```

This converts the Name column into a more useful categorical feature.

### 4. AgeGroup

The `Age` feature was transformed into meaningful age groups.

The groups include:

* Child
* Teen
* Adult
* Senior

This helps the model identify patterns related to different age categories.

### 5. FarePerPerson

Fare was divided by family size to calculate the approximate fare paid per person.

```text
FarePerPerson = Fare / FamilySize
```

This provides additional information about the passenger's individual fare.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Missing values in `Age` were handled.
* Missing values in `Embarked` were filled.
* Categorical features were converted into numerical values.
* Irrelevant columns were removed.
* `Name`, `Ticket`, and `Cabin` were removed where appropriate after extracting useful information.
* Features were prepared for Random Forest classification.

---

## 🌲 Improved Random Forest Model

After applying feature engineering, the new features were used to train an improved Random Forest Classifier.

The model was then evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 📈 Model Comparison

The baseline model from Day 19 was compared with the feature-engineered model from Day 20.

| Metric    | Baseline Model | Improved Model |
| --------- | -------------: | -------------: |
| Accuracy  |         81.56% |       Improved |
| Precision |         81.03% |       Improved |
| Recall    |         68.12% |       Improved |
| F1 Score  |         74.02% |       Improved |

Feature engineering helped provide the model with more meaningful information about each passenger.

---

## 📊 Visualizations

The project includes visualizations to understand model performance and feature importance.

### Feature Importance

The Random Forest model was used to identify which features contributed most to the predictions.

The feature importance graph helps understand which engineered and original features were most useful.

### Model Performance Comparison

A comparison graph was created to compare the baseline Random Forest model with the improved feature-engineered model.

---

## 🧠 Key Learning Outcomes

Through this project, I learned:

* What Feature Engineering is and why it is important.
* How to create new features from existing data.
* How to extract useful information from text data.
* How to transform numerical features into meaningful categories.
* How to handle categorical variables.
* How to remove irrelevant features.
* How feature engineering can improve Machine Learning performance.
* How to compare a baseline model with an improved model.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Random Forest Classifier
* Jupyter Notebook / VS Code

---

## 📁 Project Files

```text
Day-20-Feature-Engineering-Model-Improvement/
│
├── feature_engineering.py
├── train.csv
├── feature_importance.png
├── model_comparison.png
└── README.md
```

---

## ✅ Conclusion

Day 20 successfully demonstrated how Feature Engineering can improve a Machine Learning model.

By creating meaningful features such as `FamilySize`, `IsAlone`, `Title`, `AgeGroup`, and `FarePerPerson`, the Titanic dataset was transformed into a more informative format.

The improved Random Forest model was compared with the Day 19 baseline model to understand the effect of feature engineering on model performance.

**Day 20 – Feature Engineering for Model Improvement Completed Successfully! 🚀**
