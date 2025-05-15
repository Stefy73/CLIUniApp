from subject import Subject
import random
class Student:
    def __init__(self, email, password, subjects=None, name=None, id=None):
        self.id = self.generate_id()
        self.email = email
        self.password = password
        self.name = name
        self.subjects = subjects or []

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "subjects": [s.to_dict() for s in self.subjects]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],  # restored from saved data
            email=data["email"],
            password=data["password"],
            name=data.get("name"),
            subjects=[Subject.from_dict(s) for s in data.get("subjects", [])]
        )


    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(subject.mark for subject in self.subjects) / len(self.subjects)

    def is_passed(self):
        return self.calculate_average() >= 50

    def _str_(self):
        subject_info = "\n".join(str(subj) for subj in self.subjects)
        return f"Email: {self.email}, Subjects:\n{subject_info if subject_info else 'None'}"
    def generate_id(self):
        return "{:06d}".format(random.randint(1, 999999))