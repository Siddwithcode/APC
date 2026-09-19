class Vehicle: pass
class Car(Vehicle): pass
class Bike(Vehicle): pass
class SportsCar(Car): pass
class ElectricBike(Bike): pass
sc = SportsCar()
eb = ElectricBike()
print(f"SportsCar is Vehicle? {isinstance(sc, Vehicle)}")
