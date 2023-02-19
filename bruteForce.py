import tkinter as tk

root = tk.Tk()
root.title("Brute Force")
root.geometry("600x400")
root.config(background="#000000")

frame = tk.Frame(root)
frame.pack()


# password = ""



with open('password.txt', 'r', encoding='utf-8') as text_file:
    contents = text_file.read()

actual_password = input("enter password to test: ")

guess_password_list = contents.split('\n')


def hash_password(word_list_password):
    result = hashlib.sha1(word_list_password.encode())
    return result.hexdigest()


def bruteforce(guess_password_list, actual_password_hash):
    for guess_password in guess_password_list:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password,
                  "\n please change this, it was really easy to guess it (:")
            # If the password is found then it will terminate the script here
            exit()


def check_password():
    password = enter_text.get()
    password_check = tk.Label(root, text="Hacking...", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
    password_check.place(x=120, y=310)
    password_check.config(text="Hacking... \n" + password)
    # hash password with hash library
    actual_password_hash = hash_password(actual_password)

    # Running the Brute Force attack
    bruteforce(guess_password_list, actual_password_hash)


heading = tk.Label(root, text="Password Checker", font=("Verdana", 23, "bold"), bg="#000000", fg="#1e00ff")
heading.pack(pady=(90, 0))
enter_text = tk.Entry(root, justify="center", width=18, font=("Verdana", 20, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

Button = tk.Button(root, text="Check Password", width=15, font=("Verdana", 20, "bold"), fg="#1e00ff", bg="#000000",
                command=check_password)
Button.pack()

root.mainloop()
