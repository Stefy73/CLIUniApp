# database.py
import os #operating system module - used to check if the file exists
import pickle #serialised

class Database:
    FILE_PATH = "students.data"

    def initialize_file(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'wb') as f:
                pickle.dump([], f)

    def load_students(self):
        try:
            with open(self.FILE_PATH, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []  # return empty list if file is missing or empty


    def save_students(self, students):
        with open(self.FILE_PATH, 'wb') as f:
            pickle.dump(students, f)

    def clear_students(self):
        with open(self.FILE_PATH, 'wb') as f:
            pickle.dump([], f)
