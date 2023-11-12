class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)  # Call the constructor of the parent class
        self.fuel_type = fuel_type

    def display_info(self):
        # Call the parent class's display_info method and add fuel type information
        return super().display_info() + f", Fuel Type: {self.fuel_type}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year, fuel_type="Electric")  # Call the constructor of the parent class (Car)
        self.battery_capacity = battery_capacity

    def display_info(self):
        # Call the parent class's display_info method (Car) and add battery capacity information
        return super().display_info() + f", Battery Capacity: {self.battery_capacity} kWh"

# Create instances of the derived classes
car = Car("Toyota", "Camry", 2022, "Gasoline")
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

# Display information about the  vehicles
print(car.display_info())  # Output: "2022 Toyota Camry, Fuel Type: Gasoline"
print(electric_car.display_info())  # Output: "2022 Tesla Model S, Fuel Type: Electric, Battery Capacity: 100 kWh"

