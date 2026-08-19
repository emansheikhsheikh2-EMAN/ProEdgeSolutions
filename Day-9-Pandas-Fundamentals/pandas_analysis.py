import pandas as pd

# Load the student dataset
df = pd.read_csv("students.csv")

print("Student Data Explorer")
print("=" * 40)

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)
# Data Filtering & Sorting

# 1. Students with marks greater than 80
print("\nStudents with Marks Greater Than 80:")
print(df[df["Marks"] > 80])

# 2. Students from Data Science department
print("\nStudents from Data Science Department:")
print(df[df["Department"] == "Data Science"])

# 3. Students sorted by marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# 4. Students sorted by attendance percentage
print("\nStudents Sorted by Attendance Percentage:")
print(df.sort_values(by="Attendance Percentage", ascending=False))
# Data Analysis

# 1. Total number of students
total_students = len(df)
print("\nTotal Number of Students:", total_students)

# 2. Average marks
average_marks = df["Marks"].mean()
print("Average Marks:", round(average_marks, 2))

# 3. Highest marks
highest_marks = df["Marks"].max()
print("Highest Marks:", highest_marks)

# 4. Lowest marks
lowest_marks = df["Marks"].min()
print("Lowest Marks:", lowest_marks)

# 5. Department-wise student count
department_count = df["Department"].value_counts()
print("\nDepartment-wise Student Count:")
print(department_count)

# 6. Department-wise average marks
department_average = df.groupby("Department")["Marks"].mean()
print("\nDepartment-wise Average Marks:")
print(department_average.round(2))