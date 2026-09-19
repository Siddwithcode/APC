class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = True

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print(f"{self.model} rented successfully.")
        else:
            print(f"{self.model} is currently unavailable.")

    def return_vehicle(self, days):
        self.availability = True
        charges = days * self.rental_rate
        print(f"{self.model} returned. Total rental charges: ${charges}")

car = Vehicle("XYZ-123", "Toyota Camry", 45)
car.rent_vehicle()
car.return_vehicle(3)
