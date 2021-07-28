'''
def say_hello():
    print("Hello")

say_hello()


def say_hello(user_name):
    print(f"Hello {user_name.title()}")

say_hello("mo faruqe")

#The variable username in the definition of greet_user() is an example 
# of a parameter, a piece of information the function needs to do its job. 
# The value 'jesse' in greet_user('jesse') is an example of an argument. 

#People sometimes speak of arguments and parameters interchangeably. Don’t 
# be surprised if you see the variables in a function definition referred 
# to as arguments or the variables in a function call referred to as parameters.


#Positional Arguments
#When you call a function, Python must match each argument in the function 
# call with a parameter in the function definition. The simplest way to 
# do this is based on the order of the arguments provided. Values matched 
# up this way are called positional arguments.
def describe_pet(animal_type, pet_name):
    print(f"She has a {animal_type} named {pet_name.title()}")

describe_pet("dog", "shadow")


#Keyword ArgumentsA keyword argument is a name-value pair that you pass to a function. 
# You directly associate the name and the value within the argument, so when you pass the 
# argument to the function, there’s no confusion (you won’t end up with a harry named 
# Hamster). Keyword arguments free you from having to worry about correctly ordering your 
# arguments in the function call, and they clarify the role of each value in the function call.

describe_pet(pet_name="shadow", animal_type="dog")


#When writing a function, you can define a default value for each parameter. If an argument for 
# a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s 
# default value. So when you define a default value for a parameter, you can exclude the corresponding 
# argument you’d usually write in the function call. Using default values can simplify 
# your function calls and clarify the ways in which your functions are typically used.

def describe_pet(pet_name, animal_type="dog"):
    print(f"She has a {animal_type} named {pet_name.title()}")

describe_pet("larry")
describe_pet(pet_name="larry")
describe_pet("ginger", "cat")

#Note that the order of the parameters in the function definition had to be changed. 
# Because the default value makes it unnecessary to specify a type of animal as an argument, 
# the only argument left in the function call is the pet’s name. Python still interprets 
# this as a positional argument, so if the function is called with just a pet’s name, 
# that argument will match up with the first parameter listed in the function’s definition. 
# This is the reason the first parameter needs to be pet_name.

#When you use default values, any parameter with a default value needs to be listed 
# after all the parameters that don’t have default values. This allows Python 
# to continue interpreting positional arguments correctly.

print("-------------------------------------------")
def full_name(first_name, last_name):
    fullname = (f"{first_name} {last_name}")
    fullname = fullname.title()
    return fullname

print(full_name("mo", "faruqe"))

#creating an optional argument
def full_name2(first_name, last_name, middle_name=""):
    if middle_name:
        fullname = (f"{first_name} {middle_name} {last_name}")
    else:
        fullname = (f"{first_name} {last_name}")
    fullname = fullname.title()
    return fullname

print(full_name2("mo", "faruqe"))
print(full_name2("mohi", "faruqe", "uddin"))


#return dictionary
def build_person(first_name, last_name, middle_name = "", age = None):
    person = {}
    if middle_name:
        person = {"first_name": first_name, "middle_name": middle_name, "last_name": last_name }
    else:
        person = {"first_name": first_name, "last_name": last_name }

    if age:
        person["age"] = age
    
    return person

print(build_person("mo", "faruqe"))
print(build_person("mohi", "faruqe", "uddin"))
print(build_person("mohi", "faruqe", "uddin", 27))


#passing a list
def greeting(names):
    for name in names:
        print(f"Hello {name.title()}!")

friends = ["jack", "karim", "amy", "leo"]
greeting(friends)

#When you pass a list to a function, the function can modify the list. Any changes made to the 
# list inside the function’s body are permanent, allowing you to work efficiently even 
# when you’re dealing with large amounts of data.

tasks = ["finish laundry", "buy groceries", "finish homework"]
finished_tasks = []
print(tasks)

def complete_tasks(all_tasks, all_finished_tasks):
    while all_tasks:
        finished_task = all_tasks.pop()
        all_finished_tasks.append(finished_task)

complete_tasks(tasks, finished_tasks)

print(tasks)
print(finished_tasks)

#Every function should have one specific job. 
# If you’re writing a function and notice the function is doing too many different tasks, 
# try to split the code into two functions. Remember that you can always call a function 
# from another function, which can be helpful when splitting a complex 
# task into a series of steps.


#Passing a list by value - pass a copy not the original
tasks = ["finish laundry", "buy groceries", "finish homework"]
finished_tasks = []
print(tasks)

def complete_tasks(all_tasks, all_finished_tasks):
    while all_tasks:
        finished_task = all_tasks.pop()
        all_finished_tasks.append(finished_task)

complete_tasks(tasks[:], finished_tasks)  #Pass a slice so that the original doesnt become empty

print(tasks)
print(finished_tasks)



#Passing an Arbitrary Number of Arguments
def baloons_order(*colors):
    print("You want baloon of each of these colors: ")
    for color in colors:
        print(color)

baloons_order("red")
baloons_order("red", "green")
baloons_order("red", "green", "yellow")


#Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, 
# the parameter that accepts an arbitrary number of arguments must be placed 
# last in the function definition. Python matches positional and keyword 
# arguments first and then collects any remaining arguments in the 
# final parameter.
def baloons_order2(type, *colors, size = 'big'):
    print(f"You want {type} type {size} baloon of each of these colors: ")
    for color in colors:
        print(color)

baloons_order2("blown", "red", "green", "yellow")
baloons_order2("blown", "red", "green", "yellow", size = "small")

'''
# Using Arbitrary Keyword ArgumentsSometimes you’ll want to accept an arbitrary 
# number of arguments, but you won’t know ahead of time what kind of information 
# will be passed to the function. In this case, you can write functions that 
# accept as many key-value pairs as the calling statement provides. One example 
# involves building user profiles: you know you’ll get information about a user, 
# but you’re not sure what kind of information you’ll receive. 

def build_user_profile(first_name, last_name, **user_info):
    user_info["f_name"] = first_name
    user_info["l_name"] = last_name
    return user_info

user1 = build_user_profile("Mo", "Faruqe", dept = "IT", location = "Toronto")
user2 = build_user_profile("Mo", "Faruqe")
print(user1)
print(user2)
#The definition of build_profile() expects a first and last name, 
# and then it allows the user to pass in as many name-value pairs 
# as they want. The double asterisks before the parameter **user_info 
# cause Python to create an empty dictionary called user_info 
# and pack whatever name-value pairs it receives into this dictionary. 
# Within the function, you can access the key-value pairs in user_info 
# just as you would for any dictionary.

#Saving functions in module
#Storing Your Functions in ModulesOne advantage of functions is 
# the way they separate blocks of code from your main program. By using 
# descriptive names for your functions, your main program will be much 
# easier to follow. You can go a step further by storing your functions 
# in a separate file called a module and then importing that module into your 
# main program. An import statement tells Python to make the code in a module 
# available in the currently running program file.Storing your functions in 
# a separate file allows you to hide the details of your program’s code 
# and focus on its higher-level logic. It also allows you to reuse functions 
# in many different programs. When you store your functions in separate 
# files, you can share those files with other programmers without having 
# to share your entire program. Knowing how to import functions also allows 
# you to use libraries of functions that other programmers have written.

