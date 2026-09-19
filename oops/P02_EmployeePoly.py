class Employee:
    def calculate_salary(self): pass
class Manager(Employee):
    def calculate_salary(self): return 80000
class Developer(Employee):
    def calculate_salary(self): return 60000
class Tester(Employee):
    def calculate_salary(self): return 50000
for e in [Manager(), Developer(), Tester()]: print(e.calculate_salary())
