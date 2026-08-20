# Store item prices in a tuple and calculate statistics
prices = (19.99, 5.49, 120.00, 45.50, 3.25, 89.99)

total_bill = sum(prices)
average_price = total_bill / len(prices) if prices else 0
highest_price = max(prices) if prices else 0
lowest_price = min(prices) if prices else 0

print("Item Prices:", prices)
print(f"Total Bill           : ${total_bill:.2f}")
print(f"Average Price        : ${average_price:.2f}")
print(f"Highest-Priced Item  : ${highest_price:.2f}")
print(f"Lowest-Priced Item   : ${lowest_price:.2f}")
