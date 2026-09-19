class Product:
    def __init__(self, name, price): self.name, self.price = name, price
    def __eq__(self, other): return self.price == other.price
    def __gt__(self, other): return self.price > other.price
p1 = Product("P1", 100)
p2 = Product("P2", 150)
print("P2 > P1:", p2 > p1)
