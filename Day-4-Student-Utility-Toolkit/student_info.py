students = {}


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    students[student_id] = {
        "name": name,
        "department": department,
        "semester": semester,
        "marks": []
    }

    print("Student added successfully!")


def display_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        student = students[student_id]

        print("\n--- Student Information ---")
        print("ID:", student_id)
        print("Name:", student["name"])
        print("Department:", student["department"])
        print("Semester:", student["semester"])
        print("Marks:", student["marks"])
    else:
        print("Student not found!")


def update_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        student = students[student_id]

        name = input("Enter new name: ")
        department = input("Enter new department: ")
        semester = input("Enter new semester: ")

        student["name"] = name
        student["department"] = department
        student["semester"] = semester

        print("Student information updated successfully!")
    else:
        print("Student not found!")