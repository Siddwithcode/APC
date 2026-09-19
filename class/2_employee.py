class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.basic_salary

    def calculate_da(self):
        return 0.50 * self.basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

emp = Employee(101, "John Doe", 50000)
print(f"Gross Salary for {emp.name}: ${emp.calculate_gross_salary()}")
