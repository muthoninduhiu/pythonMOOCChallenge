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

# function to add a hint of input for user experience
def temp_text(e):
    enter_text.delete(0, "end")


def get_hash(password):
    """
    A function used return the password as a string of double length
    param: password
    return: password that has been hashed
    """
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def brute_force(password_list, hashed_password, password, try_random_password):
    """
        A function used return the password as a string of double length
        param: password: user input,
               password_hash: hashed password,
               password_list: common passwords list,
               try_random_password: variable used when userinput is not in  password_list
        return: no return value
        """
    found_password = False
    # check if password is in password list
    for guess_password in password_list:
        if get_hash(guess_password) == hashed_password:
            correct_password = guess_password
            result_label.grid_forget()
            result_label.config(text="Your password:\n" + correct_password
                               + "\n is a common password")
            found_password = 1
            break
    # else try cracking the password using brute force(guessing)

    if try_random_password == 0 and not found_password:
        charset = string.ascii_letters + string.digits + string.punctuation

        # cartesian product, equivalent to a nested for-loop
        # a set of all ordered pairs between charset and repeat
        # which is the length of the password input
        for pwd in itertools.product(charset, repeat=len(password)):
            # add the values without space to the test variable
            test = ''.join(pwd)
            print("Trying %s..." % test)
            if test == password:
                result_label.grid_forget()
                result_label.config(text="Your password:\n" + test
                                   + "\n was cracked!")
                found_password = 1
                break
    # error message if password is not found
    if not found_password:
        result_label.config(text="password not found")


def check_password():
    """
    A function used to call the functions get_hash()and brute_force
    so that we can perform the cracking
    params: none
    return value: none
    """
    user_input = enter_text.get()
    with open('password.txt', 'r', encoding='utf-8') as text_file:
        contents = text_file.read()

    st = time.time()
    hashed_password = get_hash(user_input)
    password_list = contents.split('\n')
    try_random_password = 0
    # Running the Brute Force attack
    brute_force(password_list, hashed_password, user_input, try_random_password)

    # get the end time
    et = time.time()

    # get the execution time
    res = et - st
    time_used.config(
        text="Execution time: \n" + str(round(res, 4)) + 'seconds')


# style the heading
heading = tk.Label(
    root,
    text="Password Cracker",
    font=("Verdana", 23, "bold"),
    bg="#000000",
    fg="#1e00ff")
heading.pack(pady=(90, 0))

# style the entry box
enter_text = tk.Entry(
    root,
    justify="center",
    width=15,
    font=("Verdana", 15, "italic"),
    bg="white",
    border=2)
enter_text.insert(0, "Enter Password...")
enter_text.pack(pady=10)
enter_text.bind("<FocusIn>", temp_text)

result_label = tk.Label(
    root,
    width=30,
    font=("Verdana", 20, "bold"),
    bg="#000000",
    fg="#1e00ff")
result_label.place(x=0, y=250)

time_used = tk.Label(
        root,
        font=("Verdana", 20, "bold"),
        bg="#000000",
        fg="#1e00ff")
time_used.place(x=170, y=400)

# style the button
button = tk.Button(
    root,
    text="Check Password",
    width=17,
    font=("Verdana", 20, "bold"),
    fg="#1e00ff",
    bg="#000000",
    command=check_password)
button.pack()

# end the loop
root.mainloop()
