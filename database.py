# database.py
import os
import json
from student import Student

class Database:
    FILE_PATH = "students.data"

    def initialize_file(self):
        """Ensure the file exists with an empty list."""
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as f:
                json.dump([], f)

    def load_students(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                data = json.load(f)
                return [Student.from_dict(s) for s in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.initialize_file()
            return []

    def save_students(self, students):
        with open(self.FILE_PATH, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=4)

    def clear_students(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump([], f)
