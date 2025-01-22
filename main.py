import random
import string
from tkinter import PhotoImage

import pyperclip
import customtkinter as ctk

def gen_password(length=12, uppercase=True, digits=True, special=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    if uppercase:
        password = [random.choice(string.ascii_uppercase)]
    else:
        password = []
    if digits:
        password.append(random.choice(string.digits))
    if special:
        password.append(random.choice(string.punctuation))

    remaining_length = length - len(password)
    password.extend(random.choices(characters, k=remaining_length))

    random.shuffle(password)
    return ''.join(password)

def display_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.configure(text="Invalid length.")
        return

    uppercase = uppercase_var.get()
    digits = digits_var.get()
    special = special_var.get()

    password = gen_password(length, uppercase, digits, special)

    result_label.configure(text=password)

    pyperclip.copy(password)
    clipboard_label.configure(text="Password copied to clipboard.")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Generator")
app.geometry("500x500")
icon= PhotoImage("img.png")
app.iconphoto(True, icon)

length_label = ctk.CTkLabel(app, text="Password Length:")
length_label.pack(pady=(20, 5))
length_entry = ctk.CTkEntry(app, placeholder_text="Enter length")
length_entry.pack(pady=5)

uppercase_var = ctk.BooleanVar(value=True)
uppercase_check = ctk.CTkCheckBox(app, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack(pady=5)

digits_var = ctk.BooleanVar(value=True)
digits_check = ctk.CTkCheckBox(app, text="Include Digits", variable=digits_var)
digits_check.pack(pady=5)

special_var = ctk.BooleanVar(value=True)
special_check = ctk.CTkCheckBox(app, text="Include Special Characters", variable=special_var)
special_check.pack(pady=5)

generate_button = ctk.CTkButton(app, text="Generate Password", command=display_password)
generate_button.pack(pady=20)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

clipboard_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
clipboard_label.pack(pady=10)

app.mainloop()
