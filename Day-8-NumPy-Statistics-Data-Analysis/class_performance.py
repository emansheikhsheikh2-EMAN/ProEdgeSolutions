import numpy as np

# Student marks dataset
marks = np.array([
    [85, 78, 92, 88],
    [72, 80, 75, 70],
    [90, 95, 89, 94],
    [65, 70, 68, 72],
    [88, 84, 91, 86],
    [76, 79, 74, 81],
    [95, 92, 96, 98],
    [60, 65, 62, 68],
    [82, 87, 85, 89],
    [78, 73, 80, 76]
])

subjects = ["Python", "NumPy", "Statistics", "ML"]

print("Class Performance Report")
print("=" * 40)

print("\nStudent Marks:")
print(marks)

print("\nTotal Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("\nPercentile Values:")
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))

# Student-wise total marks
student_totals = np.sum(marks, axis=1)

top_student = np.argmax(student_totals)
lowest_student = np.argmin(student_totals)

print("\nPerformance Insights:")
print("Top Performing Student: Student", top_student + 1)
print("Top Student Total Marks:", student_totals[top_student])

print("Lowest Performing Student: Student", lowest_student + 1)
print("Lowest Student Total Marks:", student_totals[lowest_student])

# Subject-wise averages
subject_averages = np.mean(marks, axis=0)

print("\nSubject-wise Average Marks:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])

print("\nOverall Class Performance Summary")
print("-" * 40)
print("Class Average:", np.mean(marks))
print("Class Highest Marks:", np.max(marks))
print("Class Lowest Marks:", np.min(marks))