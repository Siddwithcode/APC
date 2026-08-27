def consultation_charge(amount):
    return amount


def laboratory_charge(amount):
    return amount


def medicine_charge(amount):
    return amount


def room_charge(amount):
    return amount


def final_bill(consultation, laboratory, medicine, room, category):
    total = consultation + laboratory + medicine + room

    if category == "senior":
        discount = total * 20 / 100
    elif category == "child":
        discount = total * 10 / 100
    else:
        discount = 0

    final = total - discount

    return final


consultation = consultation_charge(500)
laboratory = laboratory_charge(1000)
medicine = medicine_charge(1500)
room = room_charge(2000)

category = input("Enter patient category (senior/child/normal): ")

bill = final_bill(
    consultation,
    laboratory,
    medicine,
    room,
    category
)

print("Final Hospital Bill =", bill)