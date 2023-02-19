# This piece of code does not mean to be fully workable
# due to SoloLearn Code Playground limitations..
import itertools
import string
import time

# charset will contain letters, numbers
# and punctuation marks..
# charset = string.ascii_letters + string.digits + string.punctuation

# this charset contains only uppercase letters...
charset = string.ascii_lowercase

password = input("Enter password to crack:")
start = time.time()
for pwd in itertools.product(charset, repeat=len(password)):
    test = ''.join(pwd)
    print("Trying %s..." % test)
    if test == password:
        # print("Password Found! [%s]" % test)
        break
end = time.time()
res = (end - start) * 1000
print("It takes {} milliseconds to crack {} ".format(res, password))
