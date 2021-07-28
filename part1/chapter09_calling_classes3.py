#You can also import an entire module and then access the classes 
# you need using dot notation. This approach is simple and results in code 
# that is easy to read. Because every call that creates an instance of a class 
# includes the module name, you won’t have naming conflicts with 
# any names used in the current file.

import car2

my_electric_car = car2.ElectricCar("Tesla", "CyberTruck", "Black", "2021", 300)
print(my_electric_car.color)
print(my_electric_car.max_dist_single_charge)
my_electric_car.battery.describe_battery()

print("--------------------------")
my_electric_car.max_mileage()