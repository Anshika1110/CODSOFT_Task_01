import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Define character sets for password generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        password = generate_password(length)
        password_display.config(state=tk.NORMAL)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter the desired length for the password:").pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)

password_display = tk.Entry(root, state=tk.DISABLED)
password_display.pack(pady=5)

# Start the main loop
root.mainloop()
