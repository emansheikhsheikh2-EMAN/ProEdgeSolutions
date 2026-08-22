import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# Day 12 - Exploratory Data Analysis (EDA)
# ==========================================

# 1. Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS REPORT")
print("=" * 50)

# 2. Dataset Exploration
print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# 3. Data Quality Check
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 4. Data Cleaning
df = df.drop_duplicates()

# No missing values were found, so no missing-value removal was required.

# 5. Statistical Analysis
score_columns = ["math score", "reading score", "writing score"]

print("\nSummary Statistics:")
print(df[score_columns].describe())

print("\nAverage Scores:")
print(df[score_columns].mean().round(2))

# 6. Gender Analysis
print("\nAverage Scores by Gender:")
print(
    df.groupby("gender")[score_columns]
    .mean()
    .round(2)
)

# 7. Test Preparation Analysis
print("\nAverage Scores by Test Preparation:")
print(
    df.groupby("test preparation course")[score_columns]
    .mean()
    .round(2)
)

# 8. Lunch Analysis
print("\nAverage Scores by Lunch Type:")
print(
    df.groupby("lunch")[score_columns]
    .mean()
    .round(2)
)

# 9. Parental Education Analysis
print("\nAverage Scores by Parental Education:")
print(
    df.groupby("parental level of education")[score_columns]
    .mean()
    .round(2)
    .sort_values("math score", ascending=False)
)

# 10. Race/Ethnicity Analysis
print("\nAverage Scores by Race/Ethnicity:")
print(
    df.groupby("race/ethnicity")[score_columns]
    .mean()
    .round(2)
    .sort_values("math score", ascending=False)
)


# ==========================================
# VISUALIZATIONS
# ==========================================

# 11. Bar Chart - Average Scores by Subject
subject_means = df[score_columns].mean()

plt.figure(figsize=(8, 5))
subject_means.plot(kind="bar")
plt.title("Average Student Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("day-12_average-scores-bar-chart.png")
plt.show()


# 12. Line Chart - Average Scores by Gender
gender_means = df.groupby("gender")[score_columns].mean()

plt.figure(figsize=(8, 5))
gender_means.T.plot(kind="line", marker="o")
plt.title("Average Scores by Gender")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("day-12_gender-score-line-chart.png")
plt.show()


# 13. Histogram - Math Score Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["math score"], bins=10)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("day-12_math-score-histogram.png")
plt.show()


print("\n" + "=" * 50)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)