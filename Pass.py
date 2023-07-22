import tkinter as tk
import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation


    password = ''.join(random.choices(characters, k=length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        if length <= 0:
            password_label.config(text="Invalid length.")
            return

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        password_label.config(text="Invalid input. Please enter a valid integer for the password length.")
    except Exception as e:
        password_label.config(text="An error occurred: " + str(e))

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x250")

length_label = tk.Label(app, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_var.set(True)
uppercase_check = tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_var.set(True)
digits_check = tk.Checkbutton(app, text="Include Digits", variable=digits_var)
digits_check.pack()

symbols_var = tk.BooleanVar()
symbols_var.set(True)
symbols_check = tk.Checkbutton(app, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

password_label = tk.Label(app, text="")
password_label.pack()

app.mainloop()
