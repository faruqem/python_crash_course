'''
class Dog:

    kind = 'canine'         # class variable shared by all instances
    
    def __init__(self, name, age):

        self.name = name    # instance variable unique to each instance
        self.age = age

    def rolling(self):
        print(f"{self.name} is rolling!")

d = Dog('Fido', 12)
e = Dog('Buddy', 16)

print(d.name)
print(e.kind)

d.rolling()


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

my_car = Car("Nissan", "Murano", "Grey", 2007)

my_car.mileage = 50000
print(my_car.mileage)

my_car.update_mileage(70000)
print(my_car.mileage)

my_car.update_mileage(40000)
print(my_car.mileage)

my_car.increase_mileage(10000)
print(my_car.mileage)

print("--------------------------")

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"Battery size: {self.battery_size}")

#child class
#When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
class ElectricCar(Car):
    def __init__(self, make, model, color, year, max_dist_single_charge):
        super().__init__(make, model, color, year)
        self.max_dist_single_charge = max_dist_single_charge
        #self.battery_size = 75
        self.battery = Battery()

    def max_mileage(self): #overridden
        print(f"This car goes max {self.max_dist_single_charge} miles in a single charge ")

my_electric_car = ElectricCar("Tesla", "CyberTruck", "Black", "2021", 300)
print(my_electric_car.color)
print(my_electric_car.max_dist_single_charge)
my_electric_car.battery.describe_battery()

print("--------------------------")

my_car.max_mileage()
my_electric_car.max_mileage()

#When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.
'''

#Calling standard module
from random import randint, choice

rand_int = randint(1,100) #get a random int between 1 and 100
print(rand_int)

colors = ["red", "green", "blue", "yellow", "ash", "brown", "grey"]
rand_color = choice(colors)
print(rand_color)


#Styling ClassesA few styling issues related to classes are worth clarifying, 
# especially as your programs become more complicated.Class names should be written in 
# CamelCase. To do this, capitalize the first letter of each word in the name, and 
# don’t use underscores. Instance and module names should be written in 
# lowercase with underscores between words.Every class should have a docstring 
# immediately following the class definition. The docstring should be a brief 
# description of what the class does, and you should follow the same formatting 
# conventions you used for writing docstrings in functions. Each module should 
# also have a docstring describing what the classes in a module can be used for.
# You can use blank lines to organize code, but don’t use them excessively. 
# Within a class you can use one blank line between methods, and within a module 
# you can use two blank lines to separate classes.If you need to import a module 
# from the standard library and a module that you wrote, place the import statement 
# for the standard library module first. Then add a blank line and the import 
# statement for the module you wrote. In programs with multiple import statements, 
# this convention makes it easier to see where the different modules used 
# in the program come from.



