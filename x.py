import hashlib
# import the builtin time module
import time
import tkinter as tk

# create the main window of the app
root = tk.Tk()
# set the title of the main window as 'Brute Force'
root.title("Brute Force")
root.geometry("750x500")
root.config(background="#000000")

with open('password.txt', 'r', encoding='utf-8') as text_file:
    contents = text_file.read()

    # user_input = input("enter password to test: ")

    password_list = contents.split('\n')


def hash_password(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def bruteforce(guess_passwords, users_input):
    for guess_password in guess_passwords:
        if hash_password(guess_password) == users_input:
            password_check = tk.Label(root,
                     text="Hey! your password:" + str(guess_password) + " "
                        "\nis in the list of common passwords(:",
                     font=("Verdana", 15, "bold"),
                     bg="#000000",
                     fg="#1e00ff")
            password_check.place(x=60, y=310)
        else:
            password_check = tk.Label(root,
                     text="Hey! your password:" + str(guess_password) +
                          "\n is somewhat safe from my hack(:",
                     font=("Verdana", 15, "bold"),
                     bg="#000000",
                     fg="#1e00ff")
            password_check.place(x=60, y=310)


def main():
    st = time.time()
    # START YOUR MAIN FUNCTIONS HERE
    password = enter_text.get()
    # Running the Brute Force attack
    bruteforce(password_list, password)
    et = time.time()
    # get the execution time
    res = et - st
    final_res = str(res * 1000)
    exec_time_label = tk.Label(root,
                               text="Execution Time: \n" + final_res + "\nMilliseconds",
                               font=("Verdana", 15, "bold"),
                               bg="#000000",
                               fg="#1e00ff")
    exec_time_label.place(x=480, y=310)


heading = tk.Label(root,
                   text="Password Checker",
                   font=("Verdana", 23, "bold"),
                   bg="#000000",
                   fg="#1e00ff")
heading.pack(pady=(90, 0))
enter_text = tk.Entry(root,
                      justify="center",
                      show="*",
                      width=18,
                      font=("Verdana", 20, "bold"),
                      bg="white",
                      border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = tk.Button(root,
                   text="Check Password",
                   width=15,
                   font=("Verdana", 20, "bold"),
                   fg="#1e00ff",
                   bg="#000000",
                   command=main)
button.pack()

root.mainloop()
if __name__ == '__main__':
    main()
