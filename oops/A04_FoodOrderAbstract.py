from abc import ABC, abstractmethod
class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self): pass
    @abstractmethod
    def delivery_charge(self): pass
class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self): return 500
    def delivery_charge(self): return 50
print(f"Delivery Charge: {HomeDeliveryOrder().delivery_charge()}")
