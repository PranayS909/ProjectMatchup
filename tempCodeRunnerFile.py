import customtkinter as ctk
import json
import os

# Path to store the profile data
DATA_FILE = "profile_data.json"

# Function to save and display profile data
def save_and_display_profile():
    # Save data to JSON
    profile_data = {
        "name": name_entry.get(),
        "year": year_entry.get(),
        "branch": branch_entry.get(),
        "skill1": skill1_entry.get(),
        "skill2": skill2_entry.get(),
        "skill3": skill3_entry.get(),
        "description": description_box.get("1.0", "end").strip(),
        "achievements": achievements_box.get("1.0", "end").strip(),
    }
    with open(DATA_FILE, "w") as file:
        json.dump(profile_data, file)
    
    # Update labels dynamically
    name_label.configure(text=f"Name: {profile_data['name']}")
    year_label.configure(text=f"Year: {profile_data['year']}")
    branch_label.configure(text=f"Branch: {profile_data['branch']}")
    description_label.configure(text=f"Description: {profile_data['description']}")
    achievements_label.configure(text=f"Achievements: {profile_data['achievements']}")
    skill_tag1.configure(text=profile_data["skill1"])
    skill_tag2.configure(text=profile_data["skill2"])
    skill_tag3.configure(text=profile_data["skill3"])
    
    status_label.configure(text="Profile saved and displayed!", text_color="green")


# Function to load profile data from JSON
def load_profile_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            profile_data = json.load(file)
        # Pre-fill inputs with loaded data
        name_entry.insert(0, profile_data.get("name", ""))
        year_entry.insert(0, profile_data.get("year", ""))
        branch_entry.insert(0, profile_data.get("branch", ""))
        skill1_entry.insert(0, profile_data.get("skill1", ""))
        skill2_entry.insert(0, profile_data.get("skill2", ""))
        skill3_entry.insert(0, profile_data.get("skill3", ""))
        description_box.insert("1.0", profile_data.get("description", ""))
        achievements_box.insert("1.0", profile_data.get("achievements", ""))
        status_label.configure(text="Profile loaded successfully!", text_color="blue")
    else:
        status_label.configure(text="No previous profile found. Enter new data.", text_color="red")


# Function to clear all fields and delete the stored JSON data
def clear_all_data():
    # Clear all fields
    name_entry.delete(0, "end")
    year_entry.delete(0, "end")
    branch_entry.delete(0, "end")
    skill1_entry.delete(0, "end")
    skill2_entry.delete(0, "end")
    skill3_entry.delete(0, "end")
    description_box.delete("1.0", "end")
    achievements_box.delete("1.0", "end")
    
    # Clear JSON file if exists
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

    # Reset the status and UI
    status_label.configure(text="Data cleared successfully!", text_color="red")


# Initialize the main window
app = ctk.CTk()
app.geometry("600x900")
app.title("Interactive Profile Page")

# Set the new color scheme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Profile picture placeholder
profile_pic = ctk.CTkLabel(app, text="", width=100, height=100, corner_radius=50, fg_color="darkgray")
profile_pic.place(x=30, y=30)

# Input fields for profile data
name_label = ctk.CTkLabel(app, text="Name:", font=("Arial", 14))
name_label.place(x=150, y=30)

name_entry = ctk.CTkEntry(app, placeholder_text="Enter your name")
name_entry.place(x=230, y=30)

year_label = ctk.CTkLabel(app, text="Year:", font=("Arial", 14))
year_label.place(x=150, y=70)

year_entry = ctk.CTkEntry(app, placeholder_text="Enter your year")
year_entry.place(x=230, y=70)

branch_label = ctk.CTkLabel(app, text="Branch:", font=("Arial", 14))
branch_label.place(x=150, y=110)

branch_entry = ctk.CTkEntry(app, placeholder_text="Enter your branch")
branch_entry.place(x=230, y=110)

# Skill tags with input fields
skill1_label = ctk.CTkLabel(app, text="Skill 1:", font=("Arial", 14))
skill1_label.place(x=30, y=180)

skill1_entry = ctk.CTkEntry(app, placeholder_text="Skill 1")
skill1_entry.place(x=120, y=180)

skill2_label = ctk.CTkLabel(app, text="Skill 2:", font=("Arial", 14))
skill2_label.place(x=30, y=220)

skill2_entry = ctk.CTkEntry(app, placeholder_text="Skill 2")
skill2_entry.place(x=120, y=220)

skill3_label = ctk.CTkLabel(app, text="Skill 3:", font=("Arial", 14))
skill3_label.place(x=30, y=260)

skill3_entry = ctk.CTkEntry(app, placeholder_text="Skill 3")
skill3_entry.place(x=120, y=260)

# Description section
description_label = ctk.CTkLabel(app, text="Description:", font=("Arial", 14))
description_label.place(x=30, y=320)

description_box = ctk.CTkTextbox(app, width=500, height=100, fg_color="gray")
description_box.place(x=30, y=350)

# Achievements section
achievements_label = ctk.CTkLabel(app, text="Achievements:", font=("Arial", 14))
achievements_label.place(x=30, y=470)

achievements_box = ctk.CTkTextbox(app, width=500, height=100, fg_color="gray")
achievements_box.place(x=30, y=500)

# Enter button to save data
enter_button = ctk.CTkButton(app, text="Enter", command=save_and_display_profile, width=200, height=50)
enter_button.place(x=300, y=645)

# Clear button to clear all data
clear_button = ctk.CTkButton(app, text="Clear", command=clear_all_data, width=200, height=50, fg_color="red")
clear_button.place(x=92, y=645)

# Status label for feedback
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.place(x=180, y=820)

# Load profile data at startup
load_profile_data()

# Run the app
app.mainloop()
