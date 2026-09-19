class Student:
    def calculate_grade(self): pass
class EngineeringStudent(Student):
    def calculate_grade(self): print("Eng Grade: Relative")
class MedicalStudent(Student):
    def calculate_grade(self): print("Med Grade: Absolute")
class ManagementStudent(Student):
    def calculate_grade(self): print("Mgmt Grade: Percentile")
for s in [EngineeringStudent(), MedicalStudent(), ManagementStudent()]: s.calculate_grade()
