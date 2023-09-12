import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        result_label.config(text="Please enter a valid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_display.config(text=password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and configure GUI elements
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(app)
length_entry.pack()
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
password_display = tk.Label(app, text="", font=("Helvetica", 14))
password_display.pack()
result_label = tk.Label(app, text="", fg="red")
result_label.pack()

# Start the tkinter main loop
app.mainloop()
