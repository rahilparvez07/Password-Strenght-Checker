import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Medium", "orange"
    else:
        return "Strong", "green"

# Optional: check if password is common
def is_common_password(password):
    try:
        with open("common_passwords.txt", "r") as f:
            common_passwords = f.read().splitlines()
        return password in common_passwords
    except FileNotFoundError:
        return False

# GUI function
def evaluate_password():
    password = entry.get()
    strength, color = check_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

    if is_common_password(password):
        messagebox.showwarning("Warning", "This is a commonly used password!")
    elif strength == "Strong":
        messagebox.showinfo("Nice!", "This password looks good!")

# --- GUI SETUP ---
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 11), bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

# Run the app
root.mainloop()
