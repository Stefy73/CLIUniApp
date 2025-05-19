# CLIUniApp – University Application System (CLI + GUI)

This project implements a CLI-based university application that allows students to register, log in, enrol in subjects, and view progress. Admins can manage student records.

## Features
- Student Registration & Login
- Subject Enrolment (Max 4)
- Admin Tools: View, Group, Partition, Remove, Clear

- GUI student and subject enrolment


## Getting Started
```bash
python main.py

## Admin_controller.py
-Implemented a command-line admin menu interface allowing access to five core admin operations as mentioned:
    -Shows students (s)
    -Groups the students by their grade (g)
    -Partitions the students into Pass/Fail categories (p)
    -Removes a student by their ID (r)
    -Clears the entire student database (c)
-Show Students (s):
    -Loads the student data from students.data
    -Displays each student’s name, ID, and email in the required CLI format
    -Displays a placeholder message if no students exist
-Group Students by Grade (g):
    -Iterates through all enrolled students and their subjects
    -Groups students by grade (HD, D, C, P, F)
    -Displays grouped output in the format matching the sample I/O with indentation and color
-Partition Students into Pass/Fail (p):
    -Calculates each student’s average subject mark by using calculate_average()
    -Categorizes students into "PASS" (average ≥ 50) and "FAIL" lists
    -Prints both lists with student details and grades
-Remove Student by ID (r):
    -Prompts admin to enter a student ID
    -Validates that the input is numeric and checks for the student’s existence
    -Removes the student from the list and saves the updated list back to the file
    -Handles invalid input and non-existent IDs with appropriate error messages using try-except
-Clear All Students(c):
    -Prompts admin for confirmation before clearing all student records
    -Upon confirmation (Y), clears all data from students.data
-Demonstrated Exception Handling:
    -Uses specific try-except blocks to catch and report:
    -Non-numeric input (ValueError) when removing a student
    -Thereby ensuring smooth user experience and robustness by preventing program crashes



