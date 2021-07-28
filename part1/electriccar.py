'''A simple class to reprsent an electric car'''
from car import Car
from battery import Battery
class ElectricCar(Car):
    def __init__(self, make, model, color, year, max_dist_single_charge):
        super().__init__(make, model, color, year)
        self.max_dist_single_charge = max_dist_single_charge
        #self.battery_size = 75
        self.battery = Battery()

    def max_mileage(self): #overridden
        print(f"This car goes max {self.max_dist_single_charge} miles in a single charge ")