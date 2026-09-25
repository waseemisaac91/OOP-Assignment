"""
Question 4: Vehicle 
By Dana
"""
class Vehicle:
    """Base class representing a vehicle."""

    def __init__(self, make, model, year):
        self.make = make      # Brand of vehicle
        self.model = model    # Vehicle model
        self.year = year      # Year of manufacture

    def display_info(self):
        """Return a formatted string with vehicle details."""
        return (
            f"Make:  {self.make}\n"
            f"Model: {self.model}\n"
            f"Year:  {self.year}"
        )

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return f"Vehicle(make={self.make!r}, model={self.model!r}, year={self.year})"


class OffRoadVehicle(Vehicle):
    """Off-Road Vehicle (SUV) - inherits from Vehicle and adds four_wheel_drive."""

    def __init__(self, make, model, year, four_wheel_drive=True):
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
        """Override to include four-wheel-drive info."""
        base_info = super().display_info()
        drive = "Yes" if self.four_wheel_drive else "No"
        return f"{base_info}\n4WD:   {drive}"

    def __str__(self):
        return f"{super().__str__()} (4WD: {self.four_wheel_drive})"

    def __repr__(self):
        return (
            f"OffRoadVehicle(make={self.make!r}, model={self.model!r}, "
            f"year={self.year}, four_wheel_drive={self.four_wheel_drive})"
        )


class SportsCar(Vehicle):
    """Sports Car - inherits from Vehicle and adds max_speed."""

    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed  # in km/h

    def display_info(self):
        """Override to include max speed."""
        base_info = super().display_info()
        return f"{base_info}\nMax Speed: {self.max_speed} km/h"

    def __str__(self):
        return f"{super().__str__()} (Max: {self.max_speed} km/h)"

    def __repr__(self):
        return (
            f"SportsCar(make={self.make!r}, model={self.model!r}, "
            f"year={self.year}, max_speed={self.max_speed})"
        )


# ---------- Testing ----------
if __name__ == "__main__":
    # Create instances
    vehicle = Vehicle("Toyota", "Corolla", 2020)
    suv = OffRoadVehicle("Jeep", "Wrangler", 2022, four_wheel_drive=True)
    sports = SportsCar("Ferrari", "488 GTB", 2021, max_speed=330)

    # Display vehicle info
    print("=" * 45)
    print("🚗 VEHICLE")
    print("=" * 45)
    print(vehicle.display_info())

    print("\n" + "=" * 45)
    print("🚙 OFF-ROAD VEHICLE (SUV)")
    print("=" * 45)
    print(suv.display_info())

    print("\n" + "=" * 45)
    print("🏎️  SPORTS CAR")
    print("=" * 45)
    print(sports.display_info())

    # Quick summary using __str__
    print("\n" + "=" * 45)
    print("SUMMARY")
    print("=" * 45)
    print(f"Vehicle:         {vehicle}")
    print(f"OffRoadVehicle:  {suv}")
    print(f"SportsCar:       {sports}")
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
