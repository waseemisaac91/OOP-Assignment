# Parent Class
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Child Class 1
class OffRoadVehicle(vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

# Child Class 2
class SportsCar(vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

# Create objects
vehicle = vehicle("Toyota", "Corolla", 2022)

offroad = OffRoadVehicle("Jeep", "Wrangler", 2023, True)

sports_car = SportsCar("Ferrari", "488", 2024, 330)

# Display Vehicle properties
print("Vehicle:")
print("Make:", vehicle.make)
print("Model:", vehicle.model)
print("Year:", vehicle.year)

# Display OffRoadVehicle properties
print("\nOff-Road Vehicle:")
print("Make:", offroad.make)
print("Model:", offroad.model)
print("Year:", offroad.year)
print("Four Wheel Drive:", offroad.four_wheel_drive)

# Display SportsCar properties
print("\nSports Car:")
print("Make:", sports_car.make)
print("Model:", sports_car.model)
print("Year:", sports_car.year)
print("Max Speed:", sports_car.max_speed, "km/h")