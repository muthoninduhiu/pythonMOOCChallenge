import itertools
import string
import time
import tkinter as tk

# create the main window of the app
root = tk.Tk()
# set the title of the main window as 'Brute Force'
root.title("Brute Force")
root.geometry("700x500")
root.config(background="#000000")


def main():
    # START YOUR MAIN FUNCTIONS HERE
    password = enter_text.get()
    # Running the Brute Force attack
    charset = string.ascii_lowercase
    start = time.time()
    # cartesian product, equivalent to a nested for-loop
    # a set of all ordered pairs between charset and repeat
    # which is the length of the password input
    for pwd in itertools.product(charset, repeat=len(password)):
        # add the values without space to the test variable
        test = ''.join(pwd)
        # print the different combinations of characters
        print("Trying %s..." % test)
        # check if pass word user input is same as the combination above
        if test == password:
            # print("Password Found! [%s]" % test)
            break
    end = time.time()
    res = (end - start) * 1000
    # print("It takes {} milliseconds to crack {} ".format(res, password))

    # get the execution time
    final_res = str(res * 1000)
    exec_time_label = tk.Label(root,
                               text="It takes: \n" + final_res + " milliseconds\nTo crack:"+password,
                               font=("Verdana", 15, "bold"),
                               bg="#000000",
                               fg="#1e00ff")
    exec_time_label.place(x=150, y=310)


heading = tk.Label(root,
                   text="Password Cracker",
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
                   text="Crack Password",
                   width=15,
                   font=("Verdana", 20, "bold"),
                   fg="#1e00ff",
                   bg="#000000",
                   command=main)
button.pack()

root.mainloop()
if __name__ == '__main__':
    main()
