# student_controller.py
import re
from database import Database
from student import Student
from subject import Subject
def student_menu():
    while True:
        try:
            choice = input("        \033[96mStudent System: (l/r/x): \033[0m").strip().lower()
            if choice == 'l':
                login_student()
            elif choice == 'r':
                register_student()
            elif choice == 'x':
                break
            else:
                print("        Invalid choice. Please try again.")
        except Exception as e:
            info(f"\033[91mAn error occurred: {e}\033[0m")

def register_student():
    try:
        info("\033[92mStudent Sign Up\033[0m")
        email = input("        Email: ").strip()
        password = input("        Password: ").strip()

        # Validate email
        if not re.match(r"^[a-zA-Z0-9.]+@[u]niversity\.com$", email):
            info("\033[91mIncorrect email or password format.\033[0m")
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
    except Exception as e:
        info(f"\033[91mAn error occurred: {e}\033[0m")
    

def login_student():
    try:
        info("\033[92mStudent Sign in\033[0m")
        email = input("        Email: ").strip()
        password = input("        Password: ").strip()

        # Validate email
        if not re.match(r"^[a-zA-Z0-9.]+@[u]niversity\.com$", email):
            info("\033[91mIncorrect email or password format.\033[0m")
            return

        # Validate password
        if not re.match(r"^[A-Z][a-zA-Z]{4,}\d{3,}$", password):
            info("\033[91mIncorrect email or password format.\033[0m")
            return
        info("\033[93memail and password formats acceptable\033[0m")
        db = Database()
        students = db.load_students()

        # Find studentx
        
        student = next((s for s in students if s.email.lower() == email.lower() and s.password == password), None)
        if student:
            subject_enrolment_menu(student, students, db)
        else:
            info("\033[91mStudent does not exist\033[0m")
    except Exception as e:
        info(f"\033[91mAn error occurred: {e}\033[0m")


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

            
            break
        else:
            print("Invalid choice. Please try again.")
def info(msg):
    print("        " + msg)