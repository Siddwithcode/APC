def calculate_bill(units):
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7

    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10

    fixed_charge = 100

    bill = bill + fixed_charge

    tax = bill * 5 / 100
    bill = bill + tax

    if bill > 5000:
        discount = bill * 10 / 100
        bill = bill - discount

    return bill


units = int(input("Enter units consumed: "))

print("Final Electricity Bill =", calculate_bill(units))