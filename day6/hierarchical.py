class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def vehicle_type(self):
        return "Car"

class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

# Example usage:
car = Car()
print(car.move())           # Output: Vehicle is moving
print(car.vehicle_type())   # Output: Car

bike = Bike()
print(bike.move())          # Output: Vehicle is moving
print(bike.vehicle_type())  # Output: Bike
