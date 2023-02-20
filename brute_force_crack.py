import tkinter as tk
import hashlib
import itertools
import string
import time

# create the main window of the app
root = tk.Tk()
# set the title of the main window as 'Brute Force'
root.title("Brute Force")
root.geometry("600x600")
root.config(background="#000000")


# functions
def temp_text(e):
    enter_text.delete(0, "end")


def get_hash(password):
    """
    A function used return the password as a string of double length
    """
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def bruteforce(guess_password_list, password_hash, password, try_random):
    for guess_password in guess_password_list:
        if get_hash(guess_password) == password_hash:
            correct_password = guess_password
            answer = tk.Label(root,
                              text="Your password is",
                              font=("Verdana", 20),
                              bg="#000000",
                              fg="#1e00ff")
            answer.place(x=0, y=310)
            answer.config(text="Your password:" + correct_password
                               + "\n is in the common passwords list")
            # print('your password is:', correct_password)
            try_random = 1

    if try_random == 0:
        charset = string.ascii_letters + string.digits + string.punctuation
        for pwd in itertools.product(charset,
                                     repeat=len(password)):
            # add the values without space to the test variable
            test = ''.join(pwd)
            print("Trying %s..." % test)
            if test == password:
                answer = tk.Label(root,
                                  text="Your password is",
                                  font=("Verdana", 20),
                                  bg="#000000",
                                  fg="#1e00ff")
                answer.place(x=0, y=310)
                answer.config(text="Your password: \n" + test
                                   + "\n is somewhat safe")
                # print('your password is:', test)
                break


def check_password():
    """
    A function used to show the user's input password
    """
    password = enter_text.get()
    """password_check = tk.Label(root,
                              text="Hacking...",
                              font=("Verdana", 20),
                              bg="#000000",
                              fg="#1e00ff")
    password_check.place(x=120, y=310)
    password_check.config(text="Hacking... \n" + password)
    """
    with open('password.txt', 'r', encoding='utf-8') as text_file:
        contents = text_file.read()

    st = time.time()
    password_hash = get_hash(password)
    guess_password_list = contents.split('\n')
    try_random = 0
    # Running the Brute Force attack
    bruteforce(guess_password_list, password_hash, password, try_random)

    # get the end time
    et = time.time()

    # get the execution time
    res = et - st
    # print('Execution time:', final_res, 'milliseconds')
    time_used = tk.Label(root,
                         text="Execution time",
                         font=("Verdana", 20),
                         bg="#000000",
                         fg="#1e00ff")
    time_used.place(x=350, y=310)
    time_used.config(text="Execution time: \n" + str(round(res, 2)) + 'seconds')


heading = tk.Label(root,
                   text="Password Cracker",
                   font=("Verdana", 23, "bold"),
                   bg="#000000",
                   fg="#1e00ff")
heading.pack(pady=(90, 0))

enter_text = tk.Entry(root,
                      justify="center",
                      width=15,
                      font=("Verdana", 20, "bold"),
                      bg="white",
                      border=2)
enter_text.insert(0, "Enter Password...")
enter_text.pack(pady=10)
enter_text.bind("<FocusIn>", temp_text)

button = tk.Button(root,
                   text="Check Password",
                   width=17,
                   font=("Verdana", 20, "bold"),
                   fg="#1e00ff",
                   bg="#000000",
                   command=check_password)

button.pack()

root.mainloop()
