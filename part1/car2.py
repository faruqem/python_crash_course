#You can store as many classes as you need in a single module, although each class in a module should be related somehow. 
from battery import Battery

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

'''A simple class to reprsent an electric car'''
class ElectricCar(Car):
    def __init__(self, make, model, color, year, max_dist_single_charge):
        super().__init__(make, model, color, year)
        self.max_dist_single_charge = max_dist_single_charge
        #self.battery_size = 75
        self.battery = Battery()

    def max_mileage(self): #overridden
        print(f"This car goes max {self.max_dist_single_charge} miles in a single charge ")