class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print(f"{self.brand} {self.model}, {self.storage}GB - ${self.price}")

    def calculate_discount_price(self, discount_percentage):
        return self.price - (self.price * (discount_percentage / 100))

phone = MobilePhone("Samsung", "Galaxy S23", 256, 800)
phone.display_specifications()
print(f"Price after 10% discount: ${phone.calculate_discount_price(10)}")
