married = input("Is the driver married? (yes/no): ")

if married == "yes":
    print("Insured")
else:
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))

    if gender == "male" and age > 30:
        print("Insured")
    elif gender == "female" and age > 25:
        print("Insured")
    else:
        print("Not Insured")