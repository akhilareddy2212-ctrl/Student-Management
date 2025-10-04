# student_functions.py
from utils import COURSES, get_int_input, get_course_input

def add_student(students):
    if len(students) >= 8:
        print("Cannot add more than 8 students.\n")
        return

    student_id = get_int_input("Enter Student ID: ")
    if student_id is None:
        return

    name = input("Enter Student Name: ").strip()
    course = get_course_input("Enter Course (CSE, ECE, IT, MECH, CIVIL): ")
    if course is None:
        return

    marks = get_int_input("Enter Marks: ")
    if marks is None:
        return

    students.append({"id": student_id, "name": name, "course": course, "marks": marks})
    print(f"Student {name} added successfully!\n")

def view_students(students):
    if not students:
        print("No students found.\n")
        return

    print("\nID\tName\tCourse\tMarks")
    print("-"*30)
    for s in students:
        print(f"{s['id']}\t{s['name']}\t{s['course']}\t{s['marks']}")
    print()

def search_student(students):
    if not students:
        print("No students found.\n")
        return

    choice = input("Search by ID or Name? (ID/Name): ").strip().lower()
    found = False

    if choice == "id":
        student_id = get_int_input("Enter Student ID: ")
        if student_id is None:
            return
        for s in students:
            if s["id"] == student_id:
                print(f"Found: {s}")
                found = True
                break
    elif choice == "name":
        name = input("Enter Student Name: ").strip()
        for s in students:
            if s["name"].lower() == name.lower():
                print(f"Found: {s}")
                found = True
                break
    else:
        print("Invalid choice. Enter 'ID' or 'Name'.\n")
        return

    if not found:
        print("Student not found.\n")

def update_student(students):
    if not students:
        print("No students found.\n")
        return

    student_id = get_int_input("Enter Student ID to update: ")
    if student_id is None:
        return

    for s in students:
        if s["id"] == student_id:
            print("1. Update Course\n2. Update Marks")
            choice = input("Enter choice (1/2): ").strip()
            if choice == "1":
                new_course = get_course_input("Enter new Course (CSE, ECE, IT, MECH, CIVIL): ")
                if new_course:
                    s["course"] = new_course
                    print("Course updated successfully!\n")
            elif choice == "2":
                new_marks = get_int_input("Enter new Marks: ")
                if new_marks is not None:
                    s["marks"] = new_marks
                    print("Marks updated successfully!\n")
            else:
                print("Invalid choice.\n")
            return
    print("Student ID not found.\n")

def delete_student(students):
    if not students:
        print("No students found.\n")
        return

    student_id = get_int_input("Enter Student ID to delete: ")
    if student_id is None:
        return

    for i, s in enumerate(students):
        if s["id"] == student_id:
            students.pop(i)
            print(f"Student ID {student_id} deleted successfully!\n")
            return
    print("Student ID not found.\n")
