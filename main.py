
# main.py 

from student_controller import student_menu
from admin_controller import admin_menu
from database import Database 

def university_menu():
    db = Database()
    db.initialize_file()
    while True:
            choice = input("\033[36mUniversity System : (A)dmin, (S)tudent, or X:\033[0m").strip().upper()
            
            if choice == 'A':
                admin_menu()
            elif choice == 'S':
                student_menu()
            elif choice == 'X':
                print("\033[93mThank you\033[0m")
                break
            else:
                print("Invalid")


if __name__ == "__main__":
    university_menu()