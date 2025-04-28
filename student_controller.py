# student_controller.py

def student_menu():
    while True:
        print("\nStudent System: (l/x/r): ")

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
    print("\n[Student Registration]")
    # We'll add full registration logic later
    pass

def login_student():
    print("\n[Student Login]")
    # We'll add full login logic later
    pass
