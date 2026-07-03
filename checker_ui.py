import customtkinter as Ctk
from PIL import Image
import os

def check_password_strength(password):
    # Load the common passwords from the file
    common_passwords = []
    try:
        with open("common_passwords.txt","r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                common_passwords.append(line.strip().lower())
    except FileNotFoundError:
        pass

    # Check for character variety
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif character in symbols:
            has_special = True

    # Check if it's a common password
    is_common = password.lower() in common_passwords

    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if is_common:
        score = 0

    # Determine the rating
    if score == 0:
        rating = "VERY WEAK- DO NOT USE"
    elif score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MODERATE"
    elif score <= 5:
        rating = "STRONG"
    else:
        rating = "VERY STRONG"
    # Build the result dictionary and return it
    results = {
        "password": password,
        "score": score,
        "rating": rating,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "long_enough": len(password) >= 8,
        "is_common": is_common,
    }
    return results

def handle_check_click():
    #Get whatever the user typed in the input field
    typed_password = password_entry.get()
    
    # If nothing was typed, show a friendly warning message
    if typed_password == "":
        results_label.configure(
            text = "Please enter a password First",
            text_color = "red"
        )
        return
    
    results = check_password_strength(typed_password)

   # Pick a color based on the rating
    if results["score"] == 0:
         color = "#ff4444"
    elif results["score"] <= 2:
        color = "#ff8800"
    elif results["score"] <=4:
        color = "#ffcc00"
    elif results["score"] <=5:
        color = "#88dd44"
    else:
        color = "#44dd88" 
    
    # Build the results text
    report = f"Score: {results['score']}  / 6\n"
    report += f"Rating: {results['rating']}\n\n"

    if results["long_enough"]:
        report += "✓ Password is long enough (8+ characters).\n"
    else:
        report += "✗ Password is too short (less than 8 characters).\n"

    if results["has_upper"]:
        report += "✓ Password contains uppercase letters.\n"
    else:
        report += "✗ Password does not contain uppercase letters.\n"

    if results["has_lower"]:
        report += "✓ Password contains lowercase letters.\n"
    else:
        report += "✗ Password does not contain lowercase letters.\n"

    if results["has_digit"]:
        report += "✓ Password contains digits.\n"
    else:
        report += "✗ Password does not contain digits.\n"

    if results["has_special"]:
        report += "✓ Password contains special characters.\n"
    else:
        report += "✗ Password does not contain special characters.\n"
    
    if results["is_common"]:
        report += "✗ WARNING: This password is too common. Please choose a more unique password.\n"

    # Update the results label with the full report
    results_label.configure(text=report, text_color=color)

if __name__ == "__main__":
    # Configure the app apperance
    Ctk.set_appearance_mode("dark")
    Ctk.set_default_color_theme("blue")

    # Create the main window
    app = Ctk.CTk()
    app.title("Password Strength Checker")
    app.geometry("500x600")
    app.resizable(False, False)

# ==============================================
# UI ELEMENTS
# ==============================================

#Logo image
logo_path = os.path.join(os.path.dirname(__file__), "padlock.png")
logo_image = Ctk.CTkImage(
    light_image=Image.open(logo_path),
    dark_image=Image.open(logo_path),
    size=(90, 90)
)
logo_label = Ctk.CTkLabel(app, image=logo_image, text ="")
logo_label.pack(pady=(30, 10))

# Ttitle Label
title_label = Ctk.CTkLabel(app,
 text="MARCELL'S Password Strength Checker", 
 font=("Arial", 20, "bold"),
 text_color="white"
 )
title_label.pack(pady=(0, 5))

# Subtitle Label
subtitle_label = Ctk.CTkLabel(app,
 text="Enter your password below to check its strength.", 
 font=("Segoe UI", 14),
 text_color="#a0a0a0"
 )
subtitle_label.pack(pady=(0, 20))


#Password Input Field
password_entry =    Ctk.CTkEntry(app,
 placeholder_text="Enter your password...",
 width=300,
 height=45,
 font=("Segoe UI", 14),
 corner_radius=12,
 border_width=1
 )
password_entry.pack(pady=10, padx= 5)

# Check Button
check_button = Ctk.CTkButton(app,
    text= "CHECK PASSWORD",
    width = 380,
    height = 45,
    font = ("Segoe UI", 14),
    corner_radius = 12,
    fg_color = "#2b7cff",
    hover_color = "#1a5cd8",
    command=handle_check_click
)
check_button.pack(pady=5, padx=20)

# Results Display area
results_frame = Ctk.CTkFrame(
    app,
    fg_color = "#1e1e1e",
    corner_radius = 12,
    border_width = 1,
    border_color = "#333333"
)
results_frame.pack(pady=(5,20), padx=30, fill="x")
results_label = Ctk.CTkLabel(
    results_frame,
    text="Results will appear here...",
    font = ("Segoe UI", 13),
    text_color = "white",
    wraplength = 380,
    justify = "left"
)
results_label.pack(pady=(20,), padx=15)
# Start the app (keeps window running)
app.mainloop()
