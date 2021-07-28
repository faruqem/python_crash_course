cars = ["toyota","bmw","gmc","mecedes","nissan", "honda","huyundai","kia","gmc","buick","hummer","volvo","infiniti","acura","lexus"]

for car in cars:
    if car.lower() == "gmc" or car.lower() == "bmw": #Testing for equality is case sensitive in Python.
        print(car.upper())
    else:
        print(car.title())

# == != < > <= >= and or
print("---------------------------------------------")
approved_cars = ["toyota","bmw","gmc","mecedes","nissan", "honda","huyundai","kia","gmc","buick","hummer","volvo","infiniti","acura","lexus"]
car = "lamborghini"
if car.lower() in approved_cars: 
    print(f"{car.title()} brand is approved")
else:
    print(f"{car.title()} brand is not approved")

if car.lower() not in approved_cars: 
    print(f"{car.title()} brand is not approved")
else:
    print(f"{car.title()} brand is approved")

print("---------------------------------------------")
age = 22
if age < 8:
    print("child")
elif age >= 9 and age <= 18:
    print("teenager")
elif age >= 19 and age <= 60:
    print("adult")
else: #not mandatory The else block is a catchall statement. 
    print("senior")

print("---------------------------------------------")
cars = []
if cars: #check if list is empty
    for car in cars:
        if car.upper() == "BMW":
            print("My fav car!")
else:
    print("There is no car is in your list")