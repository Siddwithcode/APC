import re

email = input("Enter email: ")

if re.fullmatch(r'[\w.-]+@[\w.-]+\.[A-Za-z]{2,}', email):
    print("Valid email")
else:
    print("Invalid email")