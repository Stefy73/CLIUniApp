# main.py
from student_controller import student_menu
from admin_controller import admin_menu

def university_menu():
    while True:
        print("\nUniversity System : (A)dmin, (S)tudent, or X:")

        choice = input("Enter your choice: ")

        if choice == 'A':
            admin_menu()
        elif choice == 'S':
            student_menu()
        elif choice == 'X':
            print("Exiting the University System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    university_menu()
