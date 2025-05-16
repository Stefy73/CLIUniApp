# student_controller.py
import re
from database import Database
from student import Student
from subject import Subject
def student_menu():
    while True:
        print("\nStudent System: (l/r/x): ")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'l':
            login_student()
        elif choice == 'r':
            register_student()
        elif choice == 'x':
            print("Returning to the University Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def register_student():
    print("\nStudent Registration Sign Up")
    name = input("Enter your full name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    # Validate email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[uU]niversity\.com$", email):
        print("Invalid email format. Must end with @university.com")
        return

    # Validate password
    if not re.match(r"^[A-Z][a-zA-Z]{4,}\d{3,}$", password):
        print("Invalid password format. Must start with uppercase, 5+ letters, then 3+ digits.")
        return

    db = Database()
    students = db.load_students()

    # Check if email already exists
    if any(s.email.lower() == email.lower() for s in students):
        print("A student with this email already exists.")
        return

    # Create new student
    student = Student(name=name, email=email, password=password)
    students.append(student)
    db.save_students(students)
    print("Registration successful!")

def login_student():
    print("\n[Student Login]")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    db = Database()
    students = db.load_students()

    # Find student
    student = next((s for s in students if s.email.lower() == email.lower() and s.password == password), None)
    if student:
        print(f"Welcome {student.name}!")
        subject_enrolment_menu(student, students, db)
    else:
        print("Invalid credentials. Please try again.")

def subject_enrolment_menu(student, all_students, db):
    while True:
        choice = input("\033[96mStudent Course Menu (c/e/r/s/x): \033[0m").strip().lower()
        

        if choice == 'c':
            print("\033[93mUpdating Password\033[0m")
            new_password = input("New Password: ").strip()
            confirm_password = input("Confirm Password: ").strip()

            while new_password != confirm_password: # Confirms password first
                print("\033[91mPassword does not match - try again\033[0m")
                confirm_password = input("Confirm Password: ").strip()

            if new_password == confirm_password: # Then checks for Regex format
                if re.match(r"^[A-Z][a-zA-Z]{4,}\d{3,}$", new_password):
                    student.password = new_password
                    db.save_students(all_students)
                    print("\033[93mPassword changed successfully.\033[0m")
                else:
                    print("\033[91mIncorrect password format.\033[0m")
           
        
        elif choice == 'e':
            if len(student.subjects) >= 4:
                print("\033[91mStudents are allowed to enrol in 4 subjects only\033[0m")
            else:
                subject = Subject()
                student.subjects.append(subject)
                db.save_students(all_students)
                print(f"\033[93mEnrolling in Subject-{subject.id}\033[0m")
                print(f"\033[93mYou are now enrolled in {len(student.subjects)} out of 4 subjects\033[0m")
        
        elif choice == 'r':
            if not student.subjects:
                print("\033[93mNo subjects to remove.\033[0m")
            else:
                sub_id = input("Remove subject by ID: ").strip()

                for subject in student.subjects:
                    if str(subject.id) == sub_id:
                        student.subjects.remove(subject)
                        print(f"\033[93mDropping subject -{sub_id}\033[0m")
                        break
                db.save_students(all_students)
                print(f"\033[93mYou are now enrolled in {len(student.subjects)} out of 4 subjects\033[0m")
        
        elif choice == 's':
            if not student.subjects:
                print("\033[93mShowing 0 subjects\033[0m")
            else:
                print(f"\033[93mShowing {len(student.subjects)} subjects\033[0m")
                for subj in student.subjects:
                    print(f"[ Subject:: {subj.id} -- mark = {subj.mark} -- grade = {subj.grade} ]")
        
        elif choice == 'x':
            print("\033[93mYou are now logged out.\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")
