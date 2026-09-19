from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance): pass
class Bus(Transport):
    def calculate_fare(self, dist): return dist * 2
class Taxi(Transport):
    def calculate_fare(self, dist): return dist * 10
print(f"Taxi Fare (10km): {Taxi().calculate_fare(10)}")
