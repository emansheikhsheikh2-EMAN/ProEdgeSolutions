def find_highest(marks):
    if not marks:
        return 0
    return max(marks, key=lambda x: x)


def find_lowest(marks):
    if not marks:
        return 0
    return min(marks, key=lambda x: x)


def sort_marks(marks):
    return sorted(marks, key=lambda x: x)


def search_student(students, student_id):
    return students.get(student_id)


def sort_student_records(students):
    return sorted(
        students.items(),
        key=lambda item: item[1]["name"]
    )


def process_marks(marks):
    return list(map(lambda x: x + 5, marks))