from subject import Subject

class Student:
    def __init__(self, email, password, subjects=None, name=None):
        self.email = email
        self.password = password
        self.name = name
        self.subjects = subjects or []

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "subjects": [subj.to_dict() for subj in self.subjects]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
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

    def __str__(self):
        subject_info = "\n".join(str(subj) for subj in self.subjects)
        return f"Email: {self.email}, Subjects:\n{subject_info if subject_info else 'None'}"
