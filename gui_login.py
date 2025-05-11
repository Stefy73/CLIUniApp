import tkinter as tk
from tkinter import messagebox
# from database import Database
# from gui_enrolment import open_enrolment_window

# --- Dummy implementations for demonstration only ---
# Remove these and uncomment your imports above in your real app.
class Student:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Database:
    def load_students(self):
        return [Student("test@example.com", "password123")]
def open_enrolment_window(student, students, db):
    print("Enrolment window opened for:", student.email)
# ----------------------------------------------------

def login():
    email = entry_email.get()
    password = entry_password.get()
    if not email or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    db = Database()
    students = db.load_students()
    student = next((s for s in students if s.email.lower() == email.lower() and s.password == password), None)
    if student:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()
        open_enrolment_window(student, students, db)
    else:
        messagebox.showerror("Error", "Invalid credentials.")

# --- Dark mode theme colors ---
DARK_BG = "#222222"
DARK_FRAME = "#333333"
DARK_ENTRY = "#222222"
DARK_ENTRY_BORDER = "#555555"
DARK_TEXT = "white"
DARK_BUTTON_BG = "#0058e2"
DARK_BUTTON_ACTIVE_BG = "#003c99"

# Create main window
root = tk.Tk()
root.title("GUIUniApp - Login")
root.geometry("500x350")
root.configure(bg=DARK_BG)

# Use a font that works well on macOS and others
mac_font = ("SF Pro", 13)

# Container frame
container = tk.Frame(root, bg=DARK_BG)
container.pack(padx=40, pady=40, fill="both", expand=True)

# Email field
tk.Label(container, text="Email:", font=mac_font, bg=DARK_BG, fg=DARK_TEXT).pack(anchor="w", pady=(0, 5))
email_frame = tk.Frame(container, bg=DARK_ENTRY_BORDER, highlightbackground=DARK_ENTRY_BORDER, highlightthickness=1)
email_frame.pack(fill="x", pady=(0, 15))
entry_email = tk.Entry(
    email_frame, font=mac_font, bd=0, relief="flat",
    fg=DARK_TEXT, bg=DARK_ENTRY, insertbackground=DARK_TEXT
)
entry_email.pack(fill="x", padx=10, pady=8)

# Password field
tk.Label(container, text="Password:", font=mac_font, bg=DARK_BG, fg=DARK_TEXT).pack(anchor="w", pady=(0, 5))
password_frame = tk.Frame(container, bg=DARK_ENTRY_BORDER, highlightbackground=DARK_ENTRY_BORDER, highlightthickness=1)
password_frame.pack(fill="x", pady=(0, 15))
entry_password = tk.Entry(
    password_frame, font=mac_font, show="•", bd=0, relief="flat",
    fg=DARK_TEXT, bg=DARK_ENTRY, insertbackground=DARK_TEXT
)
entry_password.pack(fill="x", padx=10, pady=8)

# Login button
login_button = tk.Button(
    container, text="Login", font=mac_font,
    bg=DARK_BUTTON_BG, fg="white",
    activebackground=DARK_BUTTON_ACTIVE_BG, activeforeground="white",
    padx=15, pady=8, bd=0, relief="flat",
    command=login
)
login_button.pack(pady=20)

# Set focus to email entry
entry_email.focus()

# macOS native look - if available
try:
    from tkmacosx import Button as MacButton
    login_button.destroy()
    login_button = MacButton(
        container, text="Login", font=mac_font,
        bg=DARK_BUTTON_BG, fg="white",
        activebackground=DARK_BUTTON_ACTIVE_BG, activeforeground="white",
        borderless=True, padx=15, pady=8,
        command=login
    )
    login_button.pack(pady=20)
except ImportError:
    pass  # If tkmacosx is not available, the standard button is used

root.mainloop()
