#A dictionary in Python is a collection of key-value pairs. 
employee = {"name": "Mo Faruqe", "years_of_employment": 15, "position": "Manager"}
print(employee["position"])
employee['department'] = 'ITS' #add a new pair
print(employee)


print("------------------------------------------")
student = {}
student["name"] = "Ayesha"
student["major"] = "IT"
print(student)

student["major"] = "Finance" #upadte the value
print(student)

del student["major"]  #remove a pair
print(student)

#formatting
employee1 = {
    "name": "Mo Faruqe", 
    "years_of_employment": 15, 
    "position": "Manager"
    }
print(employee1)

# handling no key presence
# print("------------------------------------------")
name = student.get("name","Name doesn't exist")
major = student.get("major","Major doesn't exist")
print(name)
print(major)
#If you leave out the second argument in the call to get() and the key doesn’t exist, 
# Python will return the value None. The special value None means “no value exists.” 
# This is not an error: it’s a special value meant to indicate the absence of a value.

print("------------------------------------------")
#looping through dictionary
user = {
    "name": "mo faruqe",
    "id": "mo",
    "password": "my_password",
    "level": 3
    }
for k, v in user.items():
    print(f"Key: {k}")
    print(f"Value: {v}")

print("------------------------------------------")
for k in user.keys():
    print(f"Key: {k}")

print("------------------------------------------")
for v in user.values():
    print(f"Value: {v}")

print("------------------------------------------")
#looping through dictionary in an order
for k in sorted(user.keys()):
    print(f"Key: {k}")

print("------------------------------------------")
#set
favorite_cars = {
    "Mo": "bmw",
    "Jenny": "kia",
    "Ria": "kia",
    "Alex": "honda",
    "Kerry": "mercedes",
    "John": "honda"
}

for car in favorite_cars.values():
    print(car) #repeats car names

print("---")

for car in set(favorite_cars.values()):
    print(car) #no repeat

#a set
cars = {"bmw", "kia", "honda"}
#It’s easy to mistake sets for dictionaries because they’re both wrapped in 
# braces. When you see braces but no key-value pairs, you’re probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.


print("------------------------------------------")
#nesting
#You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary. 

student1 = {"name": "Mo Faruqe", "userid": "mfaruqe", "group": "Admin", "access_level": 10}
student2 = {"name": "Ru Haque", "userid": "rhaque", "group": "Admin", "access_level": 8}
students = [student1, student2]

student3 = {"name": "Amy Arnold", "userid": "aarnold", "group": "Users", "access_level": 3}
students.append(student3)
print(students)
for student in students:
    print(f"\n")
    for k, v in student.items():
        print(f"{k.upper()}: {v}")
print("---")
aliens = []
for n in range(1,50):
    if n <= 10:
        speed = 5
    else:
        speed = 10
    
    if n%2 == 0:
        color = "red"
    else:
        color = "green"
    
    new_alien = {"id": "alien"+str(n), "color": color, "speed": speed}
    aliens.append(new_alien)
print(f"Total aliens: {len(aliens)}")

for alien in aliens[:5]: #print first 5, used slice
    print(f"{alien}")
print("....")

#It’s common to store a number of dictionaries in a list when each dictionary 
# contains many kinds of information about one object. For example, you might create 
# a dictionary for each user on a website, as we did in user.py on page 100, and 
# store the individual dictionaries in a list called users. All of the dictionaries 
# in the list should have an identical structure so you can loop through the list 
# and work with each dictionary object in the same way.

print("------------------------------------------")
# Storing lists in a dictionary
color = ["red", "green", "yellow", "blue", "magenta", "black", "white"]
brand = ["toyota", "bmw", "mercedes", "gmc", "buick", "hummer", "lamborghini", "nissasn", "infiniti", "acura", "lexus", "volvo", "maybach", "tesla", "kia"]
chasis = ["truck", "sedan", "suv", "hatchback"]
type = ["sports", "regular", "mini", "off-road", "rv"]
max_speed_kmh = [100, 200, 300, 400]

my_car = {"color": color[2], "brand": brand[1], "chasis": chasis[2], "type": type[0], "max_speed": max_speed_kmh[2]}
print("My car:")
for prop, value in my_car.items():
    if prop != "max_speed":
        print(f"{prop}: {value}")
    else:
        print(f"{prop}: {value}kmh")

print("---")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pineapple'],
    'dough': 'wheet',
    'base': 'pesto',
    'other': ['gluten-free', 'sliced', 'tabasco on the side']
    }

print(f"You orderd a {pizza['crust']} crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

#You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.

#You should not nest lists and dictionaries too deeply. If you’re nesting items much deeper than what 
# you see in the preceding examples or you’re working with someone else’s code with significant 
# levels of nesting, most likely a simpler way to solve the problem exists.


print("------------------------------------------")
# A Dictionary in a Dictionary
# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.
users = {
    "mofaruqe": {
        "fname": "mo",
        "lname": "faruqe",
        "group": "admin",
        "level": 10
    },
    "ruhaque": {
        "fname": "ru",
        "lname": "haque",
        "group": "powerusers",
        "level": 8
    }
}

for user, attribs in users.items():
    print(f"{user}:")
    for attrib, value in attribs.items():
        print(f"\t{attrib}: {value}")
    print("\n")

#Notice that the structure of each user’s dictionary is identical. 
# Although not required by Python, this structure makes nested dictionaries easier to work with. 
# If each user’s dictionary had different keys, the code inside the for loop would be more complicated.

