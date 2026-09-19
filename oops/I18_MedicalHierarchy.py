class Person: pass
class Doctor(Person): pass
class Patient(Person): pass
class Surgeon(Doctor): pass
class MedicalResearcher(Doctor): pass
s = Surgeon()
print(isinstance(s, Person))
