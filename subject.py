
import random

class Subject:
    def __init__(self):
        self.id = str(random.randint(1, 999)).zfill(3)  # 3-digit ID
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if 85 <= self.mark <= 100:
            return 'HD'  # High Distinction
        elif 75 <= self.mark < 85:
            return 'D'  # Distinction
        elif 65 <= self.mark < 75:
            return 'C'  # Credit
        elif 50 <= self.mark < 65:
            return 'P'  # Pass
        else:
            return 'F'  # Fail

    def to_dict(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        subject = cls.__new__(cls)
        subject.id = data["id"]
        subject.mark = data["mark"]
        subject.grade = data["grade"]
        return subject

    def __str__(self):
        return f"Subject ID: {self.id}, Mark: {self.mark}, Grade: {self.grade}"
