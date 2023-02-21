import tkinter as tk
import hashlib
import threading
import time

# read the password list file
with open('password.txt', 'r', encoding='utf-8') as text_file:
    password_list = text_file.read().splitlines()

# create a dictionary of common passwords and their hashes
password_dict = {}
for password in password_list:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_dict[hashed_password] = password

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


def brute_force(hashed_password):
    """
    A function used to crack the password hash using a dictionary-based approach
    param: hashed_password: the hash of the password to be cracked
    return: the cracked password if found, otherwise None
    """
    if hashed_password in password_dict:
        return password_dict[hashed_password]
    else:
        return None


def check_password():
    """
    A function used to call the functions get_hash()and brute_force
    so that we can perform the cracking
    params: none
    return value: none
    """
    user_input = enter_text.get()

    st = time.time()
    hash_password = hashlib.sha256(user_input.encode()).hexdigest()

    # use multi-threading to run the brute-force attack
    def run_brute_force():
        found_password = brute_force(hash_password)
        if found_password is not None:
            result_label.config(text="Your password:\n" + found_password
                                     + "\n is a common password")
        else:
            result_label.config(text="password not found")

    t = threading.Thread(target=run_brute_force)
    t.start()

    # get the end time
    et = time.time()

    # get the execution time
    res = et - st
    time_used.config(
        text="Execution time: \n" + str(round(res, 4)) + ' seconds')

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
