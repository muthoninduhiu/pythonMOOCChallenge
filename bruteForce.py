import tkinter as tk

root = tk.Tk()
root.title("Brute Force")
root.geometry("600x400")
root.config(background="#000000")

frame = tk.Frame(root)
frame.pack()


# password = ""


def check_password():
    password = enter_text.get()
    password_check = tk.Label(root, text="Hacking...", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
    password_check.place(x=120, y=310)
    password_check.config(text="Hacking... \n" + password)


heading = tk.Label(root, text="Password Hacker", font=("Verdana", 23, "bold"), bg="#000000", fg="#1e00ff")
heading.pack(pady=(90, 0))
# subheading = Label(root, text="Check how long it takes to brute force your password.", font=("Courier New", 20,
# "bold"), bg="#000000", fg="#16FF00") subheading.pack(pady=(10, 0))

enter_text = tk.Entry(root, justify="center", width=18, font=("Verdana", 20, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

Button = tk.Button(root, text="Check Password", width=15, font=("Verdana", 20, "bold"), fg="#1e00ff", bg="#000000",
                command=check_password)
Button.pack()

root.mainloop()
