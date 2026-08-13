from student_info import students, add_student, display_student, update_student
from academic import (
    calculate_total,
    calculate_average,
    calculate_percentage,
    calculate_grade,
    demonstrate_scope
)
from utility import (
    find_highest,
    find_lowest,
    sort_marks,
    search_student,
    sort_student_records,
    process_marks
)


def add_marks():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found! Add the student first.")
        return

    marks_input = input("Enter marks separated by spaces: ")

    try:
        marks = [float(mark) for mark in marks_input.split()]
        students[student_id]["marks"] = marks
        print("Marks added successfully!")
    except ValueError:
        print("Please enter valid numbers.")


def show_academic_result():
    student_id = input("Enter Student ID: ")

    student = search_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    marks = student["marks"]

    if not marks:
        print("No marks available for this student.")
        return

    total = calculate_total(marks)
    average = calculate_average(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("\n--- Academic Result ---")
    print("Student:", student["name"])
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


def show_mark_analysis():
    student_id = input("Enter Student ID: ")

    student = search_student(students, student_id)

    if student is None:
        print("Student not found!")
        return

    marks = student["marks"]

    if not marks:
        print("No marks available.")
        return

    print("\n--- Mark Analysis ---")
    print("Highest Marks:", find_highest(marks))
    print("Lowest Marks:", find_lowest(marks))
    print("Sorted Marks:", sort_marks(marks))
    print("Processed Marks (+5):", process_marks(marks))


def show_all_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- All Student Records ---")

    sorted_records = sort_student_records(students)

    for student_id, student in sorted_records:
        print(
            student_id,
            "-",
            student["name"],
            "-",
            student["department"]
        )


def menu():
    while True:
        print("\n===== STUDENT UTILITY TOOLKIT =====")
        print("1. Add Student Information")
        print("2. Display Student Information")
        print("3. Update Student Information")
        print("4. Add Student Marks")
        print("5. Calculate Academic Result")
        print("6. Find Highest/Lowest & Sort Marks")
        print("7. Search Student Record")
        print("8. Display All Students")
        print("9. Demonstrate Scope")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_student()

        elif choice == "3":
            update_student()

        elif choice == "4":
            add_marks()

        elif choice == "5":
            show_academic_result()

        elif choice == "6":
            show_mark_analysis()

        elif choice == "7":
            student_id = input("Enter Student ID: ")
            student = search_student(students, student_id)

            if student:
                print("Student Found:", student["name"])
            else:
                print("Student not found!")

        elif choice == "8":
            show_all_students()

        elif choice == "9":
            demonstrate_scope()

        elif choice == "10":
            print("Thank you for using Student Utility Toolkit!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()