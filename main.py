from tkinter import messagebox
from password_generator import PasswordGenerator

WIDTH = 500
HEIGHT = 600

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip


def generate_password():
    """Initiates generator class & get random passcode."""
    password = PasswordGenerator().make_new()
    password_field.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas as pd


def save_password():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()

    new_password = {"Website": [website], "Email": [email], "Password": [password]}
    new_data = pd.DataFrame.from_dict(new_password)

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website_field.get,
                                       message=f"These are the details entered: \nEmail: {email}\nPassowrd: {password} \n Is it ok to save? ")

    if is_ok:
        def header_check():
            try:
                check = pd.read_csv("passwords_list.csv")
                return False
            except:
                return True

        # Practice writing a txt file
        with open("data.txt", 'a') as data_file:
            data_file.write(f"{website}| {email}| {password}")

        new_data.to_csv("passwords_list.csv", mode='a', index=False, header=header_check())
        website_field.delete(0, END)
        email_field.delete(0, END)
        email_field.insert(0, "nik.1031@icloud.com")
        password_field.delete(0, END)
        print("Success!")
    else:
        print("User is going to fix")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# Setting up the window
window = Tk()
window.title("Password Manager")
window.wm_minsize(width=WIDTH, height=HEIGHT)
window.wm_maxsize(width=WIDTH, height=HEIGHT)
window.config(padx=50, pady=50)

# setting up the logo
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=2, row=1, columnspan=3)

# Setting up the website label
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

# Setting up the website field
website_field = Entry(width=40)
website_field.grid(column=2, columnspan=3, row=2)

# Setting up the email label
email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

# Setting up the email field
email_field = Entry(width=40)
email_field.grid(column=2, columnspan=3, row=3)
email_field.insert(0, "nik.1031@icloud.com")  # Enter details to start: aka 0 index

# Setting up the password label
password_label = Label(text="Password:")
password_label.grid(column=1, row=5)

# Setting up the password field
password_field = Entry(width=20)
password_field.grid(column=2, row=5)

# Setting up generate password button
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=3, row=5)

# Setting up Add button
add = Button(text="Add", width=34, command=save_password)
add.grid(column=2, columnspan=3, row=6)

window.mainloop()
