class Vehicle:
    def start(self): pass
class Car(Vehicle):
    def start(self): print("Car starts with key")
class Bike(Vehicle):
    def start(self): print("Bike starts with kick/button")
class Bus(Vehicle):
    def start(self): print("Bus starts with heavy engine")
for v in [Car(), Bike(), Bus()]: v.start()
