TOTAL_SUBJECTS = 5


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        return 0
    return calculate_total(marks) / len(marks)


def calculate_percentage(marks, total_possible=None):
    if not marks:
        return 0

    if total_possible is None:
        total_possible = len(marks) * 100

    return (calculate_total(marks) / total_possible) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def demonstrate_scope():
    local_message = "This is a local variable."

    print("\n--- Scope Demonstration ---")
    print(local_message)
    print("Global variable TOTAL_SUBJECTS:", TOTAL_SUBJECTS)