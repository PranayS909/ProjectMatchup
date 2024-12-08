import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
import os
import hashlib
import uuid

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class EnhancedSignupSystem:
    def __init__(self):
        # Main window configuration
        self.root = ctk.CTk()
        self.root.title("Alliance High - Account Creation")
        self.root.geometry("1000x900")
        self.root.configure(fg_color="#0E1321")

        # Courses and Branches
        self.courses = {
            "Computer Engineering": ["Branch A", "Branch B", "Branch C"],
            "Computer Science Engineering": [],
            "Electric and Computer Science": [],
            "Mechanical": []
        }

        # Semester mapping
        self.semester_map = {
            "1st Year": ["Semester 1", "Semester 2"],
            "2nd Year": ["Semester 3", "Semester 4"],
            "3rd Year": ["Semester 5", "Semester 6"],
            "4th Year": ["Semester 7", "Semester 8"]
        }

        # Create signup layout
        self.create_signup_layout()

    def create_signup_layout(self):
        # Signup Card
        signup_card = ctk.CTkFrame(self.root, 
                                   fg_color="#1A2B3C",
                                   corner_radius=20,
                                   width=800,
                                   height=850)
        signup_card.pack(expand=True, padx=20, pady=20)
        signup_card.pack_propagate(False)

        # Signup Title
        signup_title = ctk.CTkLabel(signup_card, 
                                    text="Create Your Account", 
                                    font=("Inter", 32, "bold"),
                                    text_color="#4ECDC4")
        signup_title.pack(pady=(40, 20))

        # Create scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(signup_card, 
                                              width=700, 
                                              height=650,
                                              fg_color="transparent")
        scroll_frame.pack(pady=20)

        # Input Fields
        # Username
        username_label = ctk.CTkLabel(scroll_frame, text="Username", 
                                      font=("Inter", 16),
                                      text_color="#4ECDC4")
        username_label.pack(anchor="w")
        self.username_entry = ctk.CTkEntry(scroll_frame, 
                                           width=600, 
                                           height=40,
                                           fg_color="#253645",
                                           border_color="#4ECDC4",
                                           border_width=2,
                                           text_color="white")
        self.username_entry.pack(pady=(0,10))

        # Password
        password_label = ctk.CTkLabel(scroll_frame, text="Password", 
                                      font=("Inter", 16),
                                      text_color="#4ECDC4")
        password_label.pack(anchor="w")
        self.password_entry = ctk.CTkEntry(scroll_frame, 
                                           width=600, 
                                           height=40,
                                           show="*",
                                           fg_color="#253645",
                                           border_color="#4ECDC4",
                                           border_width=2,
                                           text_color="white")
        self.password_entry.pack(pady=(0,10))

        # Confirm Password
        confirm_password_label = ctk.CTkLabel(scroll_frame, text="Confirm Password", 
                                              font=("Inter", 16),
                                              text_color="#4ECDC4")
        confirm_password_label.pack(anchor="w")
        self.confirm_password_entry = ctk.CTkEntry(scroll_frame, 
                                                   width=600, 
                                                   height=40,
                                                   show="*",
                                                   fg_color="#253645",
                                                   border_color="#4ECDC4",
                                                   border_width=2,
                                                   text_color="white")
        self.confirm_password_entry.pack(pady=(0,10))

        # Course Dropdown
        course_label = ctk.CTkLabel(scroll_frame, text="Course", 
                                    font=("Inter", 16),
                                    text_color="#4ECDC4")
        course_label.pack(anchor="w")
        self.course_var = ctk.StringVar()
        self.course_dropdown = ctk.CTkComboBox(scroll_frame, 
                                               variable=self.course_var,
                                               values=list(self.courses.keys()),
                                               width=600,
                                               height=40,
                                               fg_color="#253645",
                                               border_color="#4ECDC4",
                                               button_color="#4ECDC4",
                                               text_color="white")
        self.course_dropdown.pack(pady=(0,10))

        # Branch Dropdown
        branch_label = ctk.CTkLabel(scroll_frame, text="Branch", 
                                    font=("Inter", 16),
                                    text_color="#4ECDC4")
        branch_label.pack(anchor="w")
        self.branch_var = ctk.StringVar()
        self.branch_dropdown = ctk.CTkComboBox(scroll_frame, 
                                               variable=self.branch_var,
                                               width=600,
                                               height=40,
                                               fg_color="#253645",
                                               border_color="#4ECDC4",
                                               button_color="#4ECDC4",
                                               text_color="white")
        self.branch_dropdown.pack(pady=(0,10))

        # Year Dropdown
        year_label = ctk.CTkLabel(scroll_frame, text="Year", 
                                  font=("Inter", 16),
                                  text_color="#4ECDC4")
        year_label.pack(anchor="w")
        self.year_var = ctk.StringVar()
        self.year_dropdown = ctk.CTkComboBox(scroll_frame, 
                                             variable=self.year_var,
                                             values=["1st Year", "2nd Year", "3rd Year", "4th Year"],
                                             width=600,
                                             height=40,
                                             fg_color="#253645",
                                             border_color="#4ECDC4",
                                             button_color="#4ECDC4",
                                             text_color="white")
        self.year_dropdown.pack(pady=(0,10))

        # Semester Dropdown
        semester_label = ctk.CTkLabel(scroll_frame, text="Semester", 
                                      font=("Inter", 16),
                                      text_color="#4ECDC4")
        semester_label.pack(anchor="w")
        self.semester_var = ctk.StringVar()
        self.semester_dropdown = ctk.CTkComboBox(scroll_frame, 
                                                 variable=self.semester_var,
                                                 width=600,
                                                 height=40,
                                                 fg_color="#253645",
                                                 border_color="#4ECDC4",
                                                 button_color="#4ECDC4",
                                                 text_color="white",
                                                 state="disabled")
        self.semester_dropdown.pack(pady=(0,10))

        # Dynamic Updates
        def update_branches(*args):
            selected_course = self.course_var.get()
            branches = self.courses.get(selected_course, [])
            self.branch_dropdown.configure(values=branches)
            self.branch_dropdown.set('')
            
            # Enable/disable branch dropdown
            if branches:
                self.branch_dropdown.configure(state="normal")
            else:
                self.branch_dropdown.configure(state="disabled")

        def update_semesters(*args):
            selected_year = self.year_var.get()
            semesters = self.semester_map.get(selected_year, [])
            self.semester_dropdown.configure(values=semesters)
            self.semester_dropdown.set('')
            
            # Enable semester dropdown
            if semesters:
                self.semester_dropdown.configure(state="normal")
            else:
                self.semester_dropdown.configure(state="disabled")

        # Trace variables to update dropdowns
        self.course_var.trace_add('write', update_branches)
        self.year_var.trace_add('write', update_semesters)

        # Create Account Button
        create_account_button = ctk.CTkButton(signup_card, 
                                              text="Create Account", 
                                              command=self.register,
                                              width=600,
                                              height=50,
                                              fg_color="#4ECDC4",
                                              hover_color="#45B7AA",
                                              text_color="#0E1321",
                                              font=("Inter", 18, "bold"))
        create_account_button.pack(pady=20)

    def register(self):
        # Gather all input data
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        course = self.course_var.get()
        branch = self.branch_var.get() or "N/A"
        year = self.year_var.get()
        semester = self.semester_var.get()

        # Validation
        if not all([username, password, confirm_password, course, year, semester]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Check if user already exists
        user_file = f"users/{username}.json"
        if os.path.exists(user_file):
            messagebox.showerror("Error", "Username already exists!")
            return

        # Generate salt and hash password
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

        # Save user data
        user_data = {
            "username": username,
            "salt": salt,
            "password": hashed_password,
            "course": course,
            "branch": branch,
            "year": year,
            "semester": semester
        }

        # Save user to JSON file
        os.makedirs("users", exist_ok=True)
        with open(user_file, 'w') as f:
            json.dump(user_data, f, indent=4)

        messagebox.showinfo("Success", "Account created successfully!")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

def main():
    app = EnhancedSignupSystem()
    app.run()

if __name__ == "__main__":
    main()
