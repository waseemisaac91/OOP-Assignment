# Parent Class
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)

# Child Class 1
class OffRoadVehicle(vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        print("\nOff-Road Vehicle:")
        super().display_info()
        print("Four Wheel Drive:", self.four_wheel_drive)

# Child Class 2
class SportsCar(vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        print("\nSports Car:")
        super().display_info()
        print("Max Speed:", self.max_speed, "km/h")

# Create objects
vehicle = vehicle("Toyota", "Corolla", 2022)

offroad = OffRoadVehicle("Jeep", "Wrangler", 2023, True)

sports_car = SportsCar("Ferrari", "488", 2024, 330)

# Display information
print("Vehicle:")
vehicle.display_info()
offroad.display_info()
sports_car.display_info()
