# 2.password checker

password = input("Enter the Password: ")
while len(password) < 8:
    print("password is too short")
    password = input("Enter the Password Again: ")

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special_chars = "!@#$%^&*()_+"
numbers = "1234567890"

if any(pswrd.islower() for pswrd in password):
    pass
else:
    print("password does not have lower case")
if any(pswrd.isupper() for pswrd in password):
        pass
else:
    print("password does not have upper case")
if any(pswrd in special_chars for pswrd in password):
        pass
else:
    print("password does not have special char")
    pass
print("Your given password is valid")