print("===== Student Performance Calculator =====")
student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
department = input("Enter Department: ")
semester = input("Enter Semester: ")
print("\nStudent Information")
print("Name:", student_name)
print("ID:", student_id)
print("Department:", department)
print("Semester:", semester)
print("\nEnter Marks (out of 100)")
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
average_marks = total_marks / 5
percentage = (total_marks / 500) * 100
if percentage >= 50:
    status = "Pass"
else:
    status = "Fail"
print("\n===== Final Result =====")
print("Student Name:", student_name)
print("Student ID:", student_id)
print("Department:", department)
print("Semester:", semester)
print("Total Marks:", total_marks, "/ 500")
print("Average Marks:", average_marks)
print("Percentage:", percentage, "%")
print("Result:", status)