# 1.Random password generator

import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
pncn = string.punctuation

password = lower + upper + digits + pncn

password = "".join(random.sample(password, 10))
print("\nYour random password is:",password)