class Employee:
    def __init__(self, emp_id, name, basic): self.emp_id, self.name, self.basic = emp_id, name, basic
class Manager(Employee):
    def salary(self): return self.basic + 5000
class Developer(Employee):
    def salary(self): return self.basic + 3000
class Tester(Employee):
    def salary(self): return self.basic + 1500
d = Developer(1, "Dev", 40000)
print(f"Developer Salary: {d.salary()}")
