from tkinter import *
from tkinter import messagebox 

def login():
    username = entry_login_user.get()
    password = entry_login_pass.get()

    if not username.strip() or not password.strip():
        messagebox.showerror("Error", "Please enter both username and password.")
        return

def register():
    username = entry_login_user.get()
    password = entry_login_pass.get()

    if not username.strip() or not password.strip():
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    with open("Credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")
    
    messagebox.showinfo("Success", "Account saved successfully!")
    entry_login_user.delete(0, END)
    entry_login_pass.delete(0, END)
    
root = Tk()
root.title("=== Login System ===")
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
root.mainloop()
