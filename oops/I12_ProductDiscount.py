class Product:
    def __init__(self, pid, name, price): self.pid, self.name, self.price = pid, name, price
class ElectronicProduct(Product):
    def __init__(self, pid, name, price, brand, warranty):
        super().__init__(pid, name, price)
        self.brand, self.warranty = brand, warranty
    def final_price(self, discount):
        return self.price * (1 - discount/100)
e = ElectronicProduct(1, "TV", 1000, "Sony", "2 yrs")
print(f"Final Price: ${e.final_price(15)}")
