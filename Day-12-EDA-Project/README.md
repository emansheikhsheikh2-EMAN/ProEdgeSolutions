# Day 12 - Exploratory Data Analysis (EDA) Project

## Project Overview

This project performs a complete Exploratory Data Analysis (EDA) on the Kaggle Students Performance in Exams dataset.

The analysis demonstrates data exploration, data quality checking, statistical analysis, category comparison, visualization, and insight generation using Python.

## Dataset

- Dataset: Students Performance in Exams
- Source: Kaggle
- Records: 1,000
- Features: 8

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

## Dataset Features

The dataset contains the following columns:

- gender
- race/ethnicity
- parental level of education
- lunch
- test preparation course
- math score
- reading score
- writing score

## Data Exploration

The dataset was loaded using Pandas and examined for:

- Dataset shape
- Column names
- Data types
- First five records
- Missing values
- Duplicate records

### Data Quality Results

- Missing values: 0
- Duplicate records: 0
- Numerical score columns contain integer values.
- Categorical columns contain text values.

No missing-value treatment was required because the dataset contained no missing values. No duplicate records were removed because duplicates were not present.

## Statistical Analysis

### Average Scores

| Subject | Average Score |
|---|---:|
| Math | 66.09 |
| Reading | 69.17 |
| Writing | 68.05 |

Reading had the highest overall average score.

## Category Analysis

### Gender

Female students had higher average Reading and Writing scores, while male students had a higher average Math score.

### Test Preparation

Students who completed the test preparation course had higher average scores in all three subjects.

| Test Preparation | Math | Reading | Writing |
|---|---:|---:|---:|
| Completed | 69.70 | 73.89 | 74.42 |
| None | 64.08 | 66.53 | 64.50 |

### Lunch

The standard lunch group had higher average scores in Math, Reading, and Writing compared with the free/reduced lunch group.

### Parental Education

Students whose parents had a master's degree had the highest average scores across the three subjects.

### Race/Ethnicity

Group E had the highest average Math score at 73.82, while Group A had the lowest average Math score at 61.63.

## Visualizations

The project includes three required visualizations:

1. Average Student Scores by Subject - Bar Chart
2. Average Scores by Gender - Line Chart
3. Distribution of Math Scores - Histogram

## Key Insights

1. Reading had the highest overall average score at 69.17.
2. Students who completed the test preparation course achieved higher average scores in all three subjects.
3. The standard lunch group had higher average scores across Math, Reading, and Writing.
4. Students with parents holding a master's degree had the highest average scores.
5. Group E had the highest average Math score among the race/ethnicity groups.
6. Female students had higher average Reading and Writing scores, while male students had a higher average Math score.
7. The dataset contained no missing values and no duplicate records.

## Project Files

- `StudentsPerformance.csv` - Dataset
- `eda_analysis.py` - EDA analysis and visualization code
- `day-12_average-scores-bar-chart.png` - Bar chart
- `day-12_gender-score-line-chart.png` - Line chart
- `day-12_math-score-histogram.png` - Histogram
- `README.md` - Project documentation

## Conclusion

The EDA revealed meaningful relationships between student performance and factors such as test preparation, lunch type, parental education, gender, and race/ethnicity.

The project demonstrates practical use of Pandas, NumPy, and Matplotlib for cleaning, analyzing, visualizing, and communicating insights from a real-world dataset.