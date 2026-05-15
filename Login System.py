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

def toggle_password():
    if entry_login_pass.cget('show') == '*':
        entry_login_pass.config(show='')
        btn_toggle.config(text='🙈')
    else:
        entry_login_pass.config(show='*')
        btn_toggle.config(text='👁')
    
root = Tk()
root.title("Login System")
root.geometry("500x300")

char_count = Label(root, text="Password length: 0", font=("Segoe UI", 8), fg="gray")
char_count.pack()

label_login_user = Label(root, text="Username:")
label_login_user.pack(pady=5)
entry_login_user = Entry(root)
entry_login_user.pack(pady=5)

label_login_pass = Label(root, text="Password:")
label_login_pass.pack(pady=5)
entry_login_pass = Entry(root, show="*")

def update_count(*args):
    count = len(entry_login_pass.get())
    char_count.config(text=f"Password length: {count}")

entry_login_pass.bind("<KeyRelease>", update_count)
entry_login_pass.pack(pady=5)

btn_toggle = Button(root, text='👁', command=toggle_password)
btn_toggle.pack(pady=5)

button_login = Button(root, text="Login", command=login)
button_login.pack(pady=10)
button_register = Button(root, text="Register", command=register)
button_register.pack(pady=5)

btn_clear = Button(root, text="Clear", command=lambda: [entry_login_user.delete(0, END), entry_login_pass.delete(0, END)])
btn_clear.pack(pady=5)

status_bar = Label(root, text="Ready", font=("Segoe UI", 8), fg="gray", anchor="w", relief="sunken")
status_bar.pack(fill="x", side="bottom", ipady=2)

root.mainloop()
