# 1.Random password generator

import random
import string

pw = ("Password is stong and secure")
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = "".join(random.sample(password, 8))
print("\nYour random password is:",password)
print("\n",pw)
