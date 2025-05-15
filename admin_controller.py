from database import Database
from student import Student
from subject import Subject

# ANSI Colors
CYAN = "\033[36m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def admin_menu():
    db = Database()
    while True:
        print("         \033[36mAdmin System (c/g/p/r/s/x):\033[0m ", end="")
        choice = input().strip().lower()

        if choice == 's':
            show_students(db)
        elif choice == 'g':
            group_students(db)
        elif choice == 'p':
            partition_students(db)
        elif choice == 'r':
            remove_student(db)
        elif choice == 'c':
            clear_students(db)
        elif choice == 'x':
            break
        else:
            print("Invalid choice. Please try again.")

def show_students(db):
    print("         \033[93m Student List \033[0m")
    students = db.load_students()
    if not students:
        print("< Nothing to Display >")
        return
    for student in students:
        print(f"{student.name} :: {student.id} --> Email: {student.email}")

def group_students(db):
    print("         \033[93m Grade Grouping \033[0m")
    students = db.load_students()
    if not students:
        print("< Nothing to Display >")
        return

    grade_map = {}
    for s in students:
        for sub in s.subjects:
            if sub.grade not in grade_map:
                grade_map[sub.grade] = []
            grade_map[sub.grade].append((s.name, s.id, sub.grade, sub.mark))

    for grade, entries in grade_map.items():
        print(f"{grade}  --> [", end="")
        print(", ".join(f"{name} :: {sid} --> GRADE: {grade} - MARK: {mark:.2f}" for name, sid, grade, mark in entries), end="")
        print("]")

def partition_students(db):
    print("         \033[93m PASS/FAIL Partition \033[0m")
    students = db.load_students()
    if not students:
        print("FAIL --> []")
        print("PASS --> []")
        return

    pass_list = []
    fail_list = []

    for s in students:
        avg = s.calculate_average()
        grades = ", ".join(sub.grade for sub in s.subjects)
        info = f"{s.name} :: {s.id} --> GRADE: {grades} - MARK: {avg:.2f}"
        if avg >= 50:
            pass_list.append(info)
        else:
            fail_list.append(info)

    print("FAIL --> [", end="")
    print(", ".join(fail_list), end="")
    print("]")

    print("\nPASS --> [", end="")
    print(", ".join(pass_list), end="")
    print("]")

def remove_student(db):
    students = db.load_students()
    if not students:
        print("No students to remove.")
        return

    print("         \033[36m Remove by ID: \033[0m", end="")
    student_id = input().strip()

    updated_students = [s for s in students if s.id != student_id]

    if len(updated_students) == len(students):
        print("         \033[91m Student {student_id} does not exist \033[0m")
    else:
        db.save_students(updated_students)
        print("         \033[92m Removing Student {student_id} Account \033[0m")

def clear_students(db):
    print("         \033[93m Clearing students database \033[0m")
    confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ").strip().lower()
    if confirm == 'y' or confirm == 'yes':
        db.clear_students()
        print("         \033[92m Students data cleared \033[0m")
    else:
        print("Operation cancelled.")
