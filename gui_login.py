import tkinter as tk
from tkinter import messagebox
from database import Database
from gui_enrolment import open_enrolment_window

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

# Create main window
root = tk.Tk()
root.title("GUIUniApp - Login")
root.geometry("500x350")  # Larger window for macOS

# Use a better font that works well on macOS
mac_font = ("SF Pro", 13)  # SF Pro is a system font on macOS

# Container frame
container = tk.Frame(root)
container.pack(padx=40, pady=40, fill="both", expand=True)

# Email field - with extra visual cues
tk.Label(container, text="Email:", font=mac_font).pack(anchor="w", pady=(0, 5))
email_frame = tk.Frame(container, highlightbackground="gray", highlightthickness=1)
email_frame.pack(fill="x", pady=(0, 15))
entry_email = tk.Entry(email_frame, font=mac_font, bd=0, relief="flat")
entry_email.pack(fill="x", padx=10, pady=8)

# Password field - with extra visual cues
tk.Label(container, text="Password:", font=mac_font).pack(anchor="w", pady=(0, 5))
password_frame = tk.Frame(container, highlightbackground="gray", highlightthickness=1)
password_frame.pack(fill="x", pady=(0, 15))
entry_password = tk.Entry(password_frame, font=mac_font, show="•", bd=0, relief="flat")  # macOS style bullet
entry_password.pack(fill="x", padx=10, pady=8)

# Login button - macOS style
login_button = tk.Button(container, text="Login", font=mac_font, 
                        bg="#0058e2", fg="white", 
                        activebackground="#003c99", activeforeground="white",
                        padx=15, pady=8, bd=0, relief="flat")
login_button.config(command=login)
login_button.pack(pady=20)

# Set focus to email entry
entry_email.focus()

# macOS native look - if available
try:
    from tkmacosx import Button as MacButton
    # Replace the login button with a macOS native button
    login_button.destroy()
    login_button = MacButton(container, text="Login", font=mac_font,
                           bg="#0058e2", fg="white", 
                           activebackground="#003c99", activeforeground="white",
                           borderless=True, padx=15, pady=8)
    login_button.config(command=login)
    login_button.pack(pady=20)
except ImportError:
    pass  # If tkmacosx is not available, we still have a good-looking button

root.mainloop()