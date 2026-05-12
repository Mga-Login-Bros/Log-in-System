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


button_register = Button(root, text="Register", command=register)
button_register.pack(pady=5)
