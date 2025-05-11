# subject.py 
import random

class Subject:
    def __init__(self):
        self.id = str(random.randint(1, 999)).zfill(3)  # 3-digit ID
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'  # High Distinction
        elif self.mark >= 75:
            return 'D'   # Distinction
        elif self.mark >= 65:
            return 'C'   # Credit
        elif self.mark >= 50:
            return 'P'   # Pass
        else:
            return 'F'   # Fail

    def __str__(self):
        return f"Subject ID: {self.id}, Mark: {self.mark}, Grade: {self.grade}"
