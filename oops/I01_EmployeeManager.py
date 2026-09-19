class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id, self.name, self.salary = emp_id, name, salary
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department
    def annual_salary(self):
        return self.salary * 12
m = Manager(1, "Alice", 5000, "IT")
print(f"{m.name} in {m.department} makes ${m.annual_salary()}/year")
