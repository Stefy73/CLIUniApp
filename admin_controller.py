# admin_controller.py
from database import Database
from student import Student

def admin_menu():
    db = Database()
    while True:
        print("\n\033[94mAdmin System (c/g/p/r/s/x):\033[0m", end=" ")
        choice = input().strip().lower()

        if choice == 's':
            print("\033[92mStudent List\033[0m")
            students = db.load_students()
            if not students:
                print("        < Nothing to Display >")
            else:
                for s in students:
                    print(f"        {s.name} :: {s.id} ==> Email: {s.email}")

        elif choice == 'g':
            print("\033[93mGrade Grouping\033[0m")
            students = db.load_students()
            if not students:
                print("        < Nothing to Display >")
            else:
                grouped = {}
                for s in students:
                    for subj in s.subjects:
                        grade = subj.grade
                        grouped.setdefault(grade, []).append((s.name, s.id, subj.mark))
                for grade, entries in grouped.items():
                    print(f"        {grade} --> [", end="")
                    print(", ".join([f"{name} :: {sid} --> GRADE: {grade} - MARK: {mark:.2f}" for name, sid, mark in entries]), end="")
                    print("]")

        elif choice == 'p':
            print("\033[93mPASS/FAIL Partition\033[0m")
            students = db.load_students()
            passed = []
            failed = []
            for s in students:
                if s.subjects:
                    avg = sum(subj.mark for subj in s.subjects) / len(s.subjects)
                    grade = s.subjects[-1].grade if s.subjects else "N/A"
                    entry = f"{s.name} :: {s.id} --> GRADE: {grade} - MARK: {avg:.2f}"
                    if avg >= 50:
                        passed.append(entry)
                    else:
                        failed.append(entry)
            print(f"        FAIL --> {failed}")
            print(f"        PASS --> {passed}")

        elif choice == 'r':
            print("\033[94mRemove by ID:\033[0m", end=" ")
            sid = input().strip()
            students = db.load_students()
            matched = [s for s in students if str(s.id) == sid]
            if matched:
                students = [s for s in students if str(s.id) != sid]
                db.save_students(students)
                print(f"\033[93mRemoving Student {sid} Account\033[0m")
            else:
                print(f"\033[91mStudent {sid} does not exist\033[0m")

        elif choice == 'c':
            print("\033[91mClearing students database\033[0m")
            confirm = input("        \033[91mAre you sure you want to clear the database (Y)ES/(N)O:\033[0m ").strip().upper()
            if confirm == 'Y':
                db.clear_students()
                print("        \033[93mStudents data cleared\033[0m")
            else:
                print("        \033[93mDatabase clear cancelled\033[0m")

        elif choice == 'x':
            break

        else:
            print("        \033[91mInvalid choice. Please try again.\033[0m")
