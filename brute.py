import tkinter as tk
import hashlib
import time

# create the main window of the app
root = tk.Tk()
# set the title of the main window as 'Brute Force'
root.title("Brute Force")
root.geometry("1000x500")
root.config(background="#000000")


# functions #
def get_hash_password(password):
    """
    A function used return the password as a string of double length
    """
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def bruteforce(password_list, hashed_password):
    for guessed_password in password_list:
        if get_hash_password(guessed_password) == hashed_password:
            correct_password = guessed_password
            answer = tk.Label(root, text="Your password is", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
            answer.place(x=350, y=310)
            answer.config(text="Your password is \n" + correct_password
                               + "\n please change this, it was really easy to guess it (:")
            print('your password is:', correct_password)
        else:
            no_answer = tk.Label(root, text="no list", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
            no_answer.place(x=350, y=310)
            no_answer.config(text="Your password is not in the word list")


def check_password():
    """
    A function used to show the user's input password
    """
    password = enter_text.get()
    password_check = tk.Label(root, text="Hacking...", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
    password_check.place(x=120, y=310)
    password_check.config(text="Hacking... \n" + password)

    with open('password.txt', 'r', encoding='utf-8') as text_file:
        contents = text_file.read()

    st = time.time()
    hashed_password = hash(password)
    password_list = contents.split('\n')
    # Running the Brute Force attack
    bruteforce(password_list, hashed_password)

    # get the end time
    et = time.time()

    # get the execution time
    res = et - st
    final_res = res * 1000
    print('Execution time:', final_res, 'milliseconds')
    time_used = tk.Label(root, text="Execution time", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
    time_used.place(x=350, y=400)
    time_used.config(text="Execution time: " + str(final_res) + 'milliseconds')


# interface #

heading = tk.Label(root, text="Password Hacker", font=("Verdana", 23, "bold"), bg="#000000", fg="#1e00ff")
heading.pack(pady=(90, 0))

enter_text = tk.Entry(root, justify="center", width=18, font=("Verdana", 20, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

Button = tk.Button(root, text="Check Password", width=15, font=("Verdana", 20, "bold"), fg="#1e00ff", bg="#000000",
                   command=check_password)

Button.pack()

root.mainloop()
