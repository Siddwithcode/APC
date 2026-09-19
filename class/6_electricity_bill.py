class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units_consumed):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed

    def calculate_bill(self):
        bill = 0
        units = self.units_consumed
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = (100 * 5) + ((units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        return bill

bill = ElectricityBill(1001, "Alice", 250)
print(f"Total Bill: ${bill.calculate_bill()}")
