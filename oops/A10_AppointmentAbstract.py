from abc import ABC, abstractmethod
class Appointment(ABC):
    @abstractmethod
    def book_appointment(self): pass
    @abstractmethod
    def calculate_fee(self): pass
class SpecialistAppointment(Appointment):
    def book_appointment(self): print("Specialist Booked")
    def calculate_fee(self): return 1000
s = SpecialistAppointment()
s.book_appointment()
