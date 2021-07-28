from car2 import Car, ElectricCar

my_electric_car = ElectricCar("Tesla", "CyberTruck", "Black", "2021", 300)
print(my_electric_car.color)
print(my_electric_car.max_dist_single_charge)
my_electric_car.battery.describe_battery()

print("--------------------------")
my_electric_car.max_mileage()