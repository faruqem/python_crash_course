'''A simple class to represent a battery'''
class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"Battery size: {self.battery_size}")