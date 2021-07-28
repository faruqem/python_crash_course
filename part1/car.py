'''A simple class to repsent a car'''
class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = 0
        self.tank_size = 50

    def update_mileage(self, new_mileage):
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("You can't reduce the mileage")
    
    def increase_mileage(self, add_mileage):
        if add_mileage >= 0:
            self.mileage += add_mileage 
        else:
            print("You can't reduce the mileage")
    
    def max_mileage(self):
        print(f"This car goes max 500 mile with {self.tank_size} litre of gas.")