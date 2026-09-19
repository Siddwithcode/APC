from abc import ABC, abstractmethod
class Patient(ABC):
    @abstractmethod
    def calculate_bill(self): pass
    @abstractmethod
    def treatment(self): pass
class EmergencyPatient(Patient):
    def calculate_bill(self): return 10000
    def treatment(self): print("Emergency Care")
e = EmergencyPatient()
e.treatment()
