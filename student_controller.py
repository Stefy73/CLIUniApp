# student_controller.py
import re
from database import Database
from student import Student
from subject import Subject
def student_menu():
    while True:
        choice = input("        \033[96mStudent System: (l/r/x): \033[0m").strip().lower()
        if choice == 'l':
            login_student()
        elif choice == 'r':
            register_student()
        elif choice == 'x':
            break
        else:
            print("        Invalid choice. Please try again.")

def register_student():
    info("\033[92mStudent Sign Up\033[0m")
    email = input("        Email: ").strip()
    password = input("        Password: ").strip()

    # Validate email
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[uU]niversity\.com$", email):
        info("\033[91mInvalid email or password format.\033[0m")
        return

    # Validate password
    if not re.match(r"^[A-Z][a-zA-Z]{4,}\d{3,}$", password):
        info("\033[91mIncorrect email or password format.\033[0m")
        return
    
    info("\033[93memail and password formats acceptable\033[0m")


    db = Database()
    students = db.load_students()


    existing_student = next((s for s in students if s.email.lower() == email.lower()), None)
    if existing_student:
        info(f"\033[91mStudent {existing_student.name} already exists.\033[0m")
        return
    name = input("        Name: ").strip()
    if not name:
        info("Name cannot be empty.")
        return
    student = Student(email=email, password=password, name=name)
    students.append(student)
    db.save_students(students)
    

def login_student():
    info("\033[92mStudent Sign in\033[0m")
    email = input("        Email: ").strip()
    password = input("        Password: ").strip()

    db = Database()
    students = db.load_students()

    # Find studentx
    
    student = next((s for s in students if s.email.lower() == email.lower() and s.password == password), None)
    if student:
        info("\033[93memail and password formats acceptable\033[0m")
        subject_enrolment_menu(student, students, db)
    else:
        info("\033[91mIncorrect email or password format.\033[0m")

def subject_enrolment_menu(student, all_students, db):
    while True:
        print("\nSubject Enrolment System: (c)hange password, (e)nrol, (r)emove subject, (s)how enrolment, (x)exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'c':
            new_password = input("Enter your new password: ").strip()
            if re.match(r"^[A-Z][a-zA-Z]{4,}\d{3,}$", new_password):
                student.password = new_password
                db.save_students(all_students)
                print("Password changed successfully.")
            else:
                print("Invalid password format.")
        
        elif choice == 'e':
            if len(student.subjects) >= 4:
                print("You cannot enrol in more than 4 subjects.")
            else:
                subject = Subject()
                student.subjects.append(subject)
                db.save_students(all_students)
                print(f"Subject enrolled successfully! Subject ID: {subject.id}, Mark: {subject.mark}, Grade: {subject.grade}")
        
        elif choice == 'r':
            if not student.subjects:
                print("No subjects to remove.")
            else:
                print("Your Subjects:")
                for subj in student.subjects:
                    print(f"{subj.id}: {subj.grade} ({subj.mark})")
                sub_id = input("Enter Subject ID to remove: ").strip()
                student.subjects = [s for s in student.subjects if str(s.id) != sub_id]
                db.save_students(all_students)
                print("Subject removed successfully.")
        
        elif choice == 's':
            if not student.subjects:
                print("No enrolled subjects.")
            else:
                print("Your Enrolled Subjects:")
                for subj in student.subjects:
                    print(f"ID: {subj.id}, Mark: {subj.mark}, Grade: {subj.grade}")
        
        elif choice == 'x':
            
            break
        else:
            print("Invalid choice. Please try again.")
def info(msg):
    print("        " + msg)