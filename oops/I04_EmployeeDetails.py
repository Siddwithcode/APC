class PersonalDetails:
    def __init__(self, name, age): self.name, self.age = name, age
class ProfessionalDetails:
    def __init__(self, emp_id, desig, salary):
        self.emp_id, self.desig, self.salary = emp_id, desig, salary
class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, desig, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, desig, salary)
    def display(self): print(f"{self.name} ({self.age}), {self.desig}, {self.salary}")
e = Employee("Eve", 30, 101, "Dev", 60000)
e.display()
