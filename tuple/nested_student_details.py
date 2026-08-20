# Create a nested tuple containing student details
students = (
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 22)
)

print("Displaying Student Records:")
for student in students:
    print(f"Roll No: {student[0]}, Name: {student[1]}, Age: {student[2]}")
