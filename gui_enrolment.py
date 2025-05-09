# gui_enrolment.py
import tkinter as tk
from tkinter import messagebox
from subject import Subject

def open_enrolment_window(student, all_students, db):
    enrol_win = tk.Tk()
    enrol_win.title("GUIUniApp - Subject Enrolment")

    def enrol_subject():
        if len(student.subjects) >= 4:
            messagebox.showerror("Error", "Cannot enrol in more than 4 subjects.")
            return
        
        subject = Subject()
        student.subjects.append(subject)
        db.save_students(all_students)
        refresh_subjects()
        messagebox.showinfo("Enrolled", f"Subject {subject.id} enrolled with mark {subject.mark}.")

    def refresh_subjects():
        listbox_subjects.delete(0, tk.END)
        for subj in student.subjects:
            listbox_subjects.insert(tk.END, f"ID: {subj.id}, Mark: {subj.mark}, Grade: {subj.grade}")

    label_info = tk.Label(enrol_win, text=f"Welcome {student.name}!", font=("Helvetica", 14))
    label_info.pack(pady=10)

    btn_enrol = tk.Button(enrol_win, text="Enrol in Subject", command=enrol_subject)
    btn_enrol.pack(pady=10)

    listbox_subjects = tk.Listbox(enrol_win, width=50)
    listbox_subjects.pack(pady=10)

    refresh_subjects()

    enrol_win.mainloop()
