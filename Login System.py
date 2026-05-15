from tkinter import *
from tkinter import messagebox
import re

def login():
    username = entry_login_user.get()
    password = entry_login_pass.get()

    if not username.strip() or not password.strip():
        messagebox.showerror("Error", "Please enter both username and password!")
        return

    try:
        with open("Credentials.txt", "r") as f:
            accounts = f.readlines()
        for account in accounts:
            saved_user, saved_pass = account.strip().split(",")
            if username == saved_user and password == saved_pass:
                messagebox.showinfo("Login Sucess", "Welcome")
                return
        messagebox.showerror("Login Failed", "Incorrect Username or Password!")

    except FileNotFoundError:
        messagebox.showerror("Error", "No Accounts found.")


def register():
    username = entry_login_user.get()
    password = entry_login_pass.get()
    specialChar = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if not username.strip() or not password.strip():
        messagebox.showerror("Error", "Please enter both username and password!")
        return
    elif len(username.strip()) < 6 or len(password.strip()) < 6:
        messagebox.showerror("Error", "Username/Password must be at least 6 characters long!")
        return
    elif not specialChar.search(password):
        messagebox.showerror("Error", "Password has no special character!")
        return
    elif not any(char.isdigit() for char in password):
        messagebox.showerror("Error", "Password must contain at least 1 digit")
        return
    
    with open("Credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")
    messagebox.showinfo("Success", "Account saved successfully!")
    entry_login_user.delete(0, END)
    entry_login_pass.delete(0, END)


root = Tk()
root.title("Login System")
root.geometry("500x300")

label_login_user = Label(root, text="Username:")
label_login_user.pack(pady=5)
entry_login_user = Entry(root)
entry_login_user.pack(pady=5)

label_login_pass = Label(root, text="Password:")
label_login_pass.pack(pady=5)
entry_login_pass = Entry(root, show="*")
entry_login_pass.pack(pady=5)

button_login = Button(root, text="Login", command=login)
button_login.pack(pady=10)
button_register = Button(root, text="Register", command=register)
button_register.pack(pady=5)

root.mainloop()
