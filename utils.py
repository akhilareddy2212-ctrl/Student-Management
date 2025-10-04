# Allowed courses
COURSES = ["CSE", "ECE", "IT", "MECH", "CIVIL"]

def get_int_input(prompt):
    """
    Helper function to safely get integer input from user.
    Returns None if invalid.
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Must be a number.\n")
        return None

def get_course_input(prompt):
    """
    Helper function to get valid course input from user.
    """
    course = input(prompt).upper().strip()
    if course not in COURSES:
        print(f"Invalid course. Choose from {', '.join(COURSES)}.\n")
        return None
    return course
