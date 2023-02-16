import tkinter as tk
import hashlib
from urllib.request import urlopen

# create the main window of the app
root = tk.Tk()
# set the title of the main window as 'Brute Force'
root.title("Brute Force")
root.geometry("600x400")
root.config(background="#000000")


# functions
def read_word_list(url):
    """
    A function used to read the list of guess password
    """
    try:
        word_list_file = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return word_list_file


def get_hash(password):
    """
    A function used return the password as a string of double length
    """
    result = hashlib.sha1(password.encode())
    return result.hexdigest()


def bruteforce(guess_password_list, password_hash):
    for guess_password in guess_password_list:
        if hash(guess_password) == password_hash:
            correct_password = guess_password
            answer = tk.Label(root, text="Your password is", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
            answer.place(x=350, y=310)
            answer.config(text="Your password is \n" + correct_password)
            print('your password is:', correct_password)
        # else:
        #    no_answer = tk.Label(root, text="no list", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
        #    no_answer.place(x=350, y=310)
        #    no_answer.config(text="Your password is not in the word list")


def check_password():
    """
    A function used to show the user's input password
    """
    password = enter_text.get()
    password_check = tk.Label(root, text="Hacking...", font=("Verdana", 20), bg="#000000", fg="#1e00ff")
    password_check.place(x=120, y=310)
    password_check.config(text="Hacking... \n" + password)

    url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable' \
          '-v2.txt'
    password_hash = get_hash(password)
    wordlist = read_word_list(url).decode('UTF-8')
    guess_password_list = wordlist.split('\n')
    # Running the Brute Force attack
    bruteforce(guess_password_list, password_hash)


# interface

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
