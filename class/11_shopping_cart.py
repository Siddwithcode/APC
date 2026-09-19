class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.items = []

    def add_product(self, product_name, price):
        self.items.append({"name": product_name, "price": price})
        print(f"Added {product_name} to cart.")

    def remove_product(self, product_name):
        self.items = [item for item in self.items if item["name"] != product_name]
        print(f"Removed {product_name} from cart.")

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def __del__(self):
        print(f"Shopping Cart {self.cart_id} for {self.customer_name} has been destroyed.")

cart = ShoppingCart("Alice", "CART_001")
cart.add_product("Laptop", 1200)
cart.add_product("Mouse", 25)
print(f"Total Bill: ${cart.calculate_total()}")
