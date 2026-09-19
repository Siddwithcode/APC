class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_total_bill(self):
        tax_rate = 0.05
        base_price = self.quantity * self.price
        total = base_price + (base_price * tax_rate)
        return total

    def __del__(self):
        print(f"Order {self.order_id} for {self.customer_name} is completed and processed.")

order = FoodOrder("ORD_99", "Bob", "Burger", 2, 8.50)
print(f"Total Bill (incl. tax): ${order.calculate_total_bill()}")
