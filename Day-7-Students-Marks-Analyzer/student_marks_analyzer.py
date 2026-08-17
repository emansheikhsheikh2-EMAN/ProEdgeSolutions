import numpy as np


# Student names
students = np.array([
    "Ali", "Sara", "Ahmed", "Ayesha", "Bilal",
    "Hina", "Usman", "Maham", "Hamza", "Zoya"
])

# Subjects
subjects = np.array([
    "Python", "Statistics", "Database", "Machine Learning"
])

# Marks: 10 students × 4 subjects
marks = np.array([
    [85, 78, 92, 88],
    [76, 89, 84, 91],
    [90, 75, 88, 82],
    [95, 92, 90, 94],
    [68, 74, 70, 72],
    [82, 86, 80, 85],
    [88, 79, 91, 87],
    [73, 81, 77, 80],
    [91, 88, 94, 90],
    [79, 85, 83, 86]
])


def display_dataset():
    """Display complete student marks dataset."""
    print("\n" + "=" * 65)
    print("              STUDENT MARKS DATASET")
    print("=" * 65)

    print(f"{'Student':<12}", end="")
    for subject in subjects:
        print(f"{subject:<16}", end="")
    print()

    print("-" * 65)

    for i in range(len(students)):
        print(f"{students[i]:<12}", end="")
        for mark in marks[i]:
            print(f"{mark:<16}", end="")
        print()


def demonstrate_indexing():
    """Demonstrate NumPy indexing."""
    print("\n" + "=" * 65)
    print("                    INDEXING")
    print("=" * 65)

    # First student's complete record
    print(f"First student: {students[0]}")
    print(f"{students[0]}'s marks: {marks[0]}")

    # Specific student's specific subject
    print(f"\n{students[3]}'s Database marks: {marks[3, 2]}")

    # Last student's Machine Learning marks
    print(f"{students[-1]}'s Machine Learning marks: {marks[-1, -1]}")


def demonstrate_slicing():
    """Demonstrate NumPy slicing."""
    print("\n" + "=" * 65)
    print("                     SLICING")
    print("=" * 65)

    # First 5 students
    print("Marks of first 5 students:")
    print(marks[:5])

    # First 3 subjects of all students
    print("\nMarks of all students in first 3 subjects:")
    print(marks[:, :3])

    # Students 3 to 6, selected subjects
    print("\nStudents 3-6, Statistics & Database:")
    print(marks[2:6, 1:3])


def demonstrate_reshaping():
    """Demonstrate NumPy reshaping."""
    print("\n" + "=" * 65)
    print("                    RESHAPING")
    print("=" * 65)

    reshaped_marks = marks.reshape(5, 8)

    print("Original shape:", marks.shape)
    print("Reshaped shape:", reshaped_marks.shape)

    print("\nReshaped array (5 × 8):")
    print(reshaped_marks)


def demonstrate_broadcasting():
    """Demonstrate NumPy broadcasting."""
    print("\n" + "=" * 65)
    print("                  BROADCASTING")
    print("=" * 65)

    # Add 5 bonus marks to every subject
    bonus_marks = np.array([5, 5, 5, 5])

    updated_marks = marks + bonus_marks

    print("Bonus marks added:", bonus_marks)
    print("\nMarks after broadcasting:")
    print(updated_marks)


def marks_analysis():
    """Perform marks analysis."""
    print("\n" + "=" * 65)
    print("                  MARKS ANALYSIS")
    print("=" * 65)

    total_marks = np.sum(marks, axis=1)
    average_marks = np.mean(marks, axis=1)

    highest_mark = np.max(marks)
    lowest_mark = np.min(marks)

    highest_student_index = np.argmax(total_marks)
    lowest_student_index = np.argmin(total_marks)

    print(f"Highest individual mark: {highest_mark}")
    print(f"Lowest individual mark: {lowest_mark}")

    print(
        f"\nHighest total marks: {students[highest_student_index]} "
        f"({total_marks[highest_student_index]})"
    )

    print(
        f"Lowest total marks: {students[lowest_student_index]} "
        f"({total_marks[lowest_student_index]})"
    )

    print("\nStudent-wise Results:")
    print("-" * 45)

    for i in range(len(students)):
        print(
            f"{students[i]:<12} "
            f"Total: {total_marks[i]:<4} "
            f"Average: {average_marks[i]:.2f}"
        )

    # Subject-wise analysis
    subject_totals = np.sum(marks, axis=0)
    subject_averages = np.mean(marks, axis=0)

    print("\nSubject-wise Performance:")
    print("-" * 45)

    for i in range(len(subjects)):
        print(
            f"{subjects[i]:<20} "
            f"Total: {subject_totals[i]:<4} "
            f"Average: {subject_averages[i]:.2f}"
        )


def main():
    """Main program."""
    print("\n" + "=" * 65)
    print("             STUDENT MARKS ANALYZER")
    print("                  Day 7 - NumPy")
    print("=" * 65)

    display_dataset()
    demonstrate_indexing()
    demonstrate_slicing()
    demonstrate_reshaping()
    demonstrate_broadcasting()
    marks_analysis()

    print("\n" + "=" * 65)
    print("              ANALYSIS COMPLETED")
    print("=" * 65)


if __name__ == "__main__":
    main()