# main.py
from student_controller import student_menu
from admin_controller import admin_menu
from database import Database 
import re

def university_menu():
    db = Database()
    db.initialize_file()
    while True:
            print("\nUniversity System : (A)dmin, (S)tudent, or X:")
            choice = input("Enter your choice: ").strip().upper()
            
            if choice == 'A':
                admin_menu()
            elif choice == 'S':
                student_menu()
            elif choice == 'X':
                print("Thank you")
                break
            else:
                print("Invalid")


if __name__ == "__main__":
    university_menu()