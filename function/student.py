def total_marks(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def percentage(marks):
    return total_marks(marks) / 5


def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


def student_details(student):
    total = total_marks(student["marks"])
    percent = percentage(student["marks"])
    g = grade(percent)

    print("Name:", student["name"])
    print("Roll No:", student["roll"])
    print("Total:", total)
    print("Percentage:", percent)
    print("Grade:", g)
    print()


students = [
    {"name": "Siddhant", "roll": 1, "marks": [80, 75, 90, 85, 70]},
    {"name": "Rahul", "roll": 2, "marks": [70, 65, 75, 80, 60]},
    {"name": "Amit", "roll": 3, "marks": [90, 95, 85, 92, 88]}
]


for student in students:
    student_details(student)


total_percentage = 0

for student in students:
    total_percentage = total_percentage + percentage(student["marks"])

class_average = total_percentage / len(students)

highest = students[0]
lowest = students[0]

for student in students:
    if percentage(student["marks"]) > percentage(highest["marks"]):
        highest = student

    if percentage(student["marks"]) < percentage(lowest["marks"]):
        lowest = student


print("Class Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])