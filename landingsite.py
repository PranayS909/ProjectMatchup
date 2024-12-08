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

    # Feedback message
    status_label.configure(text="Profile saved successfully!", text_color="green")


# Function to load profile data from JSON
def load_profile_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            profile_data = json.load(file)

        # Pre-fill the entry fields with loaded data
        name_entry.insert(0, profile_data.get("name", ""))
        year_entry.insert(0, profile_data.get("year", ""))
        branch_entry.insert(0, profile_data.get("branch", ""))
        skill1_entry.insert(0, profile_data.get("skill1", ""))
        skill2_entry.insert(0, profile_data.get("skill2", ""))
        skill3_entry.insert(0, profile_data.get("skill3", ""))
        description_box.insert("1.0", profile_data.get("description", ""))
        achievements_box.insert("1.0", profile_data.get("achievements", ""))
        status_label.configure(text="Previous profile data loaded.", text_color="blue")
    else:
        status_label.configure(text="No previous profile found. Enter your data.", text_color="red")


# Initialize the main window
app = ctk.CTk()
app.geometry("700x1000")
app.title("Interactive Profile Page")

# Set the new color scheme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Create main container frame
container = ctk.CTkFrame(app, width=650, height=950, corner_radius=10, fg_color="#2a2a2a")
container.pack(pady=10, padx=20)

# Profile Picture Section
profile_pic_frame = ctk.CTkLabel(
    container, text="", width=150, height=150, corner_radius=75, fg_color="gray"
)
profile_pic_frame.place(x=275, y=20)

# Input Fields Section
inputs_frame = ctk.CTkFrame(container, width=600, height=700, corner_radius=10, fg_color="#3d3d3d")
inputs_frame.place(x=50, y=200)

# Add Name Section
ctk.CTkLabel(inputs_frame, text="Name:", font=("Arial", 12)).place(x=20, y=20)
name_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Enter your name", width=400)
name_entry.place(x=120, y=20)

# Add Year Section
ctk.CTkLabel(inputs_frame, text="Year:", font=("Arial", 12)).place(x=20, y=60)
year_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Enter your year", width=400)
year_entry.place(x=120, y=60)

# Add Branch Section
ctk.CTkLabel(inputs_frame, text="Branch:", font=("Arial", 12)).place(x=20, y=100)
branch_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Enter your branch", width=400)
branch_entry.place(x=120, y=100)

# New Skills Header Section
ctk.CTkLabel(inputs_frame, text="Skills", font=("Arial", 14, "bold")).place(x=20, y=150)

# Skill Input Fields
skill1_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Skill 1", width=180)
skill1_entry.place(x=120, y=180)

skill2_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Skill 2", width=180)
skill2_entry.place(x=320, y=180)

skill3_entry = ctk.CTkEntry(inputs_frame, placeholder_text="Skill 3", width=180)
skill3_entry.place(x=120, y=220)

# Description Section
ctk.CTkLabel(inputs_frame, text="Description:", font=("Arial", 12)).place(x=20, y=270)
description_box = ctk.CTkTextbox(inputs_frame, width=500, height=100, fg_color="gray")
description_box.place(x=120, y=270)

# Achievements Section
ctk.CTkLabel(inputs_frame, text="Achievements:", font=("Arial", 12)).place(x=20, y=380)
achievements_box = ctk.CTkTextbox(inputs_frame, width=500, height=100, fg_color="gray")
achievements_box.place(x=120, y=380)

# Save Profile Button (Enter)
enter_button = ctk.CTkButton(
    container, text="Save Profile", command=save_and_display_profile, width=200, height=50
)
enter_button.place(x=250, y=250)  # Placed at the bottom

# Status Label for feedback messages
status_label = ctk.CTkLabel(container, text="", font=("Arial", 12))
status_label.place(x=250, y=910)

# Load data from the previous session, if any
load_profile_data()

# Run the main loop
app.mainloop()
