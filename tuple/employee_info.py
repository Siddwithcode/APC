# Create tuples containing: Employee ID, Name, Salary
employee1 = (201, "John Doe", 55000)
employee2 = (202, "Jane Smith", 62000)
employee3 = (203, "Bob Johnson", 48000)

employees = (employee1, employee2, employee3)

print("--- Employee Information ---")
for emp in employees:
    print(f"ID: {emp[0]} | Name: {emp[1]} | Salary: ${emp[2]:,}")
