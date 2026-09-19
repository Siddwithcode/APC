class Vehicle:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type, self.price = fuel_type, price
    def discounted_price(self, discount_percent):
        return self.price - (self.price * (discount_percent/100))
c = Car("Toyota", "Camry", "Gas", 30000)
print(f"{c.brand} {c.model} Discounted: {c.discounted_price(10)}")
