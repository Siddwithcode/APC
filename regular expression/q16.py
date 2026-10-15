import re

p = input("Enter password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'

if re.fullmatch(pattern, p):
    print("Strong password")
else:
    print("Weak password")