
# main.py 

from student_controller import student_menu
from admin_controller import admin_menu
from database import Database 

def university_menu():
    try:
        db = Database()
        db.initialize_file()
    except Exception as e:
        print(f"\033[91mError initializing database: {e}\033[0m")
        return
    
    while True:
            try:
                choice = input("\033[96mUniversity System : (A)dmin, (S)tudent, or X:\033[0m").strip().upper()
                
                if choice == 'A':
                    admin_menu()
                elif choice == 'S':
                    student_menu()
                elif choice == 'X':
                    print("\033[93mThank you\033[0m")
                    break
                else:
                    print("\033[91mInvalid choice. Please try again.\033[0m")
            except KeyboardInterrupt:
                print("\n\033[93mExiting the system\033[0m")
                break   
            except EOFError:
                print ("\n\033[93mInput closed\033[0m")
            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")
                break

if __name__ == "__main__":
    university_menu()