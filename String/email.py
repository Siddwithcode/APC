email = input("Enter email: ")

has_at = "@" in email
has_dot = "." in email
starts_ok = email[0] != "@" and email[0] != "."

if has_at and has_dot and starts_ok and " " not in email:
    print("Valid Email")
else:
    print("Invalid Email")