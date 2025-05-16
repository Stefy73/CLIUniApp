import tkinter as tk
from tkinter import messagebox, ttk
import random
from database import Database
from student import Student
from subject import Subject

class UniversityModel:
    def __init__(self):
        self.db = Database()
        self.students = self.db.load_students()
        self.all_subjects = list(set([
            f"{random.choice(['Cybersecurity', 'Algorithms', 'Data Structures', 'Artificial Intelligence', 'Machine Learning', 'Operating Systems', 'Database Systems', 'Computer Networks', 'Software Engineering', 'Web Development'])} {i}" 
            for i in range(1, 21)
        ]))
       
    def authenticate(self, email, password):
        for student in self.students:
            if student.email.lower() == email.lower() and student.password == password:
                return student
        return None
    
    def get_random_subjects(self, count=8):
        return random.sample(self.all_subjects, count)

    def save_students(self):
        self.db.save_students(self.students)

class UniversityController:
    def __init__(self, model):
        self.model = model
        self.current_student = None
    
    def login(self, email, password):
        student = self.model.authenticate(email, password)
        if student:
            self.current_student = student
            return True
        return False
    
    def get_available_subjects(self):
        return self.model.get_random_subjects()
    
    def get_student_subjects(self):
        if self.current_student:
            return self.current_student.subjects
        return []
    
    def enroll_subject(self, subject_name):
        if self.current_student and len(self.current_student.subjects) < 4:
            subject_id = ''.join(filter(str.isdigit, subject_name))
            subject_name_only = ' '.join(subject_name.split()[:-1])  
            if not subject_id:
                subject_id = str(random.randint(100, 999))
            
            subject = Subject(subject_id, subject_name_only, random.randint(30, 100))
            self.current_student.subjects.append(subject)
            self.model.save_students()
            return True
        return False
    
    def logout(self):
        self.current_student = None

class LoginView(tk.Frame):
    def __init__(self, master, controller, switch_frame_callback):
        super().__init__(master, bg="darkslategrey")
        self.controller = controller
        self.switch_frame = switch_frame_callback
        tk.Label(self, text="Welcome to the University Portal", font=("Arial", 24), bg="darkslategrey", fg="white").pack(pady=20)
        tk.Label(self, text="Please log in to continue", font=("Arial", 16), bg="darkslategrey", fg="white").pack(pady=10)

        form_frame = tk.Frame(self, bg="darkslategrey")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Email:", bg="darkslategrey", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Password:", bg="darkslategrey", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry = tk.Entry(form_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(form_frame, text="Login", bg="#252525", fg="#ffc107", command=self.login).grid(row=2, column=0, columnspan=2, pady=20)
        tk.Label(self, text="Please note this portal is only for registered students", font=("Arial", 12), bg="darkslategrey", fg="white").pack(side=tk.BOTTOM, pady=10)
    
    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        if self.controller.login(email, password):
            self.switch_frame("options")
        else:
            messagebox.showerror("Error", "Invalid email or password!")
    
    def clear(self):
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

class OptionsView(tk.Frame):
    def __init__(self, master, controller, switch_frame_callback):
        super().__init__(master, bg="darkslategrey")
        self.controller = controller
        self.switch_frame = switch_frame_callback

        tk.Label(self, text="Select an Option", font=("Helvetica", 16), bg="darkslategrey", fg="white").pack(pady=20)
        self.welcome_label = tk.Label(self, text="", font=("Helvetica", 16), bg="darkslategrey", fg="white")
        self.welcome_label.pack(pady=10)

        tk.Button(self, text="Previous Enrollments", bg="#252525", fg="#ffc107", command=lambda: self.switch_frame("view_subjects")).pack(pady=10)
        tk.Button(self, text="Enroll to New Subjects", bg="#252525", fg="#ffc107", command=lambda: self.switch_frame("enrolment")).pack(pady=10)
        tk.Button(self, text="Logout", bg="#252525", fg="#ffc107", command=self.logout).pack(pady=10)
    
    def update_view(self):
        if self.controller.current_student:
            self.welcome_label.config(text=f"Welcome {self.controller.current_student.name}")
    
    def logout(self):
        self.controller.logout()
        self.switch_frame("login")

class EnrolmentView(tk.Frame):
    def __init__(self, master, controller, switch_frame_callback):
        super().__init__(master, bg="darkslategrey")
        self.controller = controller
        self.switch_frame = switch_frame_callback
        self.subject_vars = {}

        self.welcome_label = tk.Label(self, text="", font=("Helvetica", 16), bg="darkslategrey", fg="white")
        self.welcome_label.pack(pady=10)

        tk.Label(self, text="Select up to 4 subjects to enroll:", font=("Helvetica", 14), bg="darkslategrey", fg="white").pack(pady=10)
        self.checkbox_frame = tk.Frame(self, bg="darkslategrey")
        self.checkbox_frame.pack(pady=10)

        button_frame = tk.Frame(self, bg="darkslategrey")
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Submit", bg="#252525", fg="#ffc107", command=self.submit_enrolment).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Back", bg="#252525", fg="#ffc107", command=lambda: self.switch_frame("options")).pack(side=tk.LEFT, padx=10)
    
    def update_view(self):
        if self.controller.current_student:
            self.welcome_label.config(text=f"Welcome {self.controller.current_student.name}")
        for widget in self.checkbox_frame.winfo_children():
            widget.destroy()
        self.subject_vars = {}
        available_subjects = self.controller.get_available_subjects()
        for subject in available_subjects:
            var = tk.IntVar()
            self.subject_vars[subject] = var
            tk.Checkbutton(self.checkbox_frame, text=subject, variable=var, bg="darkslategrey", fg="white", selectcolor="darkslategrey").pack(anchor="w")
    
    def submit_enrolment(self):
        selected = [subject for subject, var in self.subject_vars.items() if var.get() == 1]
        
        if len(selected) > 4:
            messagebox.showerror("Error", "You can only select up to 4 subjects!")
            return
        if not selected:
            messagebox.showerror("Error", "Please select at least one subject!")
            return
        if len(self.controller.get_student_subjects()) >= 4:
            messagebox.showerror("Error", "You are already enrolled in the maximum of 4 subjects!")
            return
        if len(self.controller.get_student_subjects()) + len(selected) > 4:
            messagebox.showerror("Error", f"You can only enroll in {4 - len(self.controller.get_student_subjects())} more subjects!")
            return

        success = []
        for subject in selected:
            if self.controller.enroll_subject(subject):
                success.append(subject)
        if success:
            messagebox.showinfo("Success", f"You have successfully enrolled in: {', '.join(success)}")
            self.switch_frame("options")
        else:
            messagebox.showerror("Error", "Failed to enroll in the selected subjects.")

class ViewSubjectsFrame(tk.Frame):
    def __init__(self, master, controller, switch_frame_callback):
        super().__init__(master, bg="darkslategrey")
        self.controller = controller
        self.switch_frame = switch_frame_callback

        self.welcome_label = tk.Label(self, text="", font=("Helvetica", 16), bg="darkslategrey", fg="white")
        self.welcome_label.pack(pady=10)

        tk.Label(self, text="Your Enrolled Subjects", font=("Helvetica", 14), bg="darkslategrey", fg="white").pack(pady=10)

        # Create a frame and canvas with a scrollbar to handle many subjects
        self.canvas = tk.Canvas(self, bg="darkslategrey", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.subjects_frame = tk.Frame(self.canvas, bg="darkslategrey")

        self.subjects_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.subjects_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=20)
        self.scrollbar.pack(side="right", fill="y")

        # Back Button
        button_frame = tk.Frame(self, bg="darkslategrey")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Back", bg="#252525", fg="#ffc107", command=lambda: self.switch_frame("options")).pack(pady=10)

    def update_view(self):
        student = self.controller.current_student
        if student:
            self.welcome_label.config(text=f"Welcome {student.name}")
        else:
            self.welcome_label.config(text="No student selected.")
            return

        # Clear existing widgets in the scrollable subject frame
        for widget in self.subjects_frame.winfo_children():
            widget.destroy()

        subjects = self.controller.get_student_subjects()
        if not subjects:
            tk.Label(self.subjects_frame, text="You are not enrolled in any subjects.",
                     bg="darkslategrey", fg="white", font=("Helvetica", 12)).pack(pady=5)
        else:
            for subject in subjects:
                name = subject.name if hasattr(subject, 'name') and subject.name else random.choice([
                    "Cybersecurity", "Algorithms", "Data Structures", "Artificial Intelligence", 
                    "Machine Learning", "Operating Systems", "Database Systems", 
                    "Computer Networks", "Software Engineering", "Web Development"
                ])
                subject_id = getattr(subject, 'id', 'N/A')
                grade = getattr(subject, 'grade', 'N/A')
                info = f"Subject Name: {name} | Subject ID: {subject_id} | Grade: {grade}"
                tk.Label(self.subjects_frame, text=info, bg="darkslategrey", fg="white", font=("Helvetica", 12)).pack(anchor="w", pady=3)

class UniversityPortal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Portal")
        self.geometry("1250x800")
        self.model = UniversityModel()
        self.controller = UniversityController(self.model)
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.frames = {}
        self.frames["login"] = LoginView(self.container, self.controller, self.show_frame)
        self.frames["options"] = OptionsView(self.container, self.controller, self.show_frame)
        self.frames["enrolment"] = EnrolmentView(self.container, self.controller, self.show_frame)
        self.frames["view_subjects"] = ViewSubjectsFrame(self.container, self.controller, self.show_frame)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")
    
    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[frame_name]
        if hasattr(frame, "update_view"):
            frame.update_view()
        frame.grid()
        frame.tkraise()

if __name__ == "__main__":
    app = UniversityPortal()
    app.mainloop()
