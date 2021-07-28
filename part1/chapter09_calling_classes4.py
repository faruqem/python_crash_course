#Importing All Classes from a ModuleYou can import every class from a 
# module using the following syntax:
# from module_name import *
# This method is not recommended for two reasons. 
# First, it’s helpful to be able to read the import statements at the top 
# of a file and get a clear sense of which classes a program uses. 
# With this approach it’s unclear which classes you’re using from the module. 
# This approach can also lead to confusion with names in the file. 
# If you accidentally import a class with the same name as something 
# else in your program file, you can create errors that are hard to diagnose. 
# I show this here because even though it’s not a recommended approach, 
# you’re likely to see it in other people’s code at some point.

from car2 import *
my_electric_car = ElectricCar("Tesla", "CyberTruck", "Black", "2021", 300)
print(my_electric_car.color)
print(my_electric_car.max_dist_single_charge)
my_electric_car.battery.describe_battery()

print("--------------------------")
my_electric_car.max_mileage()