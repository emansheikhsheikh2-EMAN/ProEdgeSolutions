import json
import os

FILE_NAME = "students.json"


def load_students():
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return {}
    except (json.JSONDecodeError, OSError):
        print("Error loading student data.")
        return {}


def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student data.")


def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    department = input("Enter Department: ").strip()

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    email = input("Enter Email Address: ").strip()

    students[student_id] = {
        "name": name,
        "department": department,
        "age": age,
        "email": email,
        "marks": []
    }

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- All Students ---")

    for student_id, student in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Department: {student['department']}")
        print(f"Age: {student['age']}")
        print(f"Email: {student['email']}")
        print(f"Marks: {student['marks']}")


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\n--- Student Record ---")
    print(f"Student ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"Age: {student['age']}")
    print(f"Email: {student['email']}")
    print(f"Marks: {student['marks']}")


def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("Press Enter to keep the current value.")

    name = input(f"Name ({student['name']}): ").strip()
    department = input(f"Department ({student['department']}): ").strip()
    age = input(f"Age ({student['age']}): ").strip()
    email = input(f"Email ({student['email']}): ").strip()

    if name:
        student["name"] = name

    if department:
        student["department"] = department

    if age:
        try:
            age_value = int(age)
            if age_value > 0:
                student["age"] = age_value
            else:
                print("Invalid age. Old age kept.")
        except ValueError:
            print("Invalid age. Old age kept.")

    if email:
        student["email"] = email

    save_students(students)
    print("Student information updated successfully!")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    del students[student_id]
    save_students(students)

    print("Student record deleted successfully!")


def enter_marks(students):
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    try:
        number_of_subjects = int(input("Enter number of subjects: "))

        if number_of_subjects <= 0:
            print("Number of subjects must be greater than 0.")
            return

        marks = []

        for i in range(number_of_subjects):
            mark = float(input(f"Enter marks for Subject {i + 1} (out of 100): "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        students[student_id]["marks"] = marks
        save_students(students)

        print("Marks entered successfully!")

    except ValueError:
        print("Please enter valid numbers.")


def calculate_academic_result(students):
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    marks = students[student_id]["marks"]

    if not marks:
        print("No marks available for this student.")
        return

    total = sum(marks)
    maximum = len(marks) * 100
    percentage = (total / maximum) * 100

    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if percentage >= 40 else "Fail"

    print("\n--- Academic Result ---")
    print(f"Student Name: {students[student_id]['name']}")
    print(f"Total Marks: {total:.2f} / {maximum}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Academic Status: {status}")


def main():
    students = load_students()

    while True:
        print("\n========== Student Management System ==========")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Delete Student Record")
        print("6. Enter Student Marks")
        print("7. Calculate Academic Result")
        print("8. Exit")
        print("===============================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            enter_marks(students)

        elif choice == "7":
            calculate_academic_result(students)

        elif choice == "8":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()