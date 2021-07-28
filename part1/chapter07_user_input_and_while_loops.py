'''
name = input("Your name, please: ")
print(f"Your name is: {name}")

print("-------------------------------")
prompt = "\nWelcome! Hope you are doing well!!"
prompt += "\nWhat is your name, BTW: "
name = input(prompt)
print(f"\nYour name is: {name}\n")

# When you use the input() function, Python interprets everything the user enters as a string.
# So type cast is necessary for calculation.
# When you use numerical input to do calculations and comparisons, be sure to convert the 
# input value to a numerical representation first.
age = input("\nHow old are you? ")
if int(age) > 18:
    print("You are an adult!")
else:
    print("You are too young!")


#Modulo operation
for i in range(1,100):
    if i%2 == 0:
        print(i)

print("-------------------------------")
#while loop
i = 1
while i<= 5:
    print(i)
    i += 1


prompt = "\nTell me something, I will repeat it back to you."
prompt += "\nTo exit write 'quit' and then press Enter: "
msg = ''
while msg != 'quit':
    msg = input(prompt)
    if msg != 'quit':
        print(f"\nYou said: {msg}")



#using flag
active = True
prompt = "\nTell me something, I will repeat it back to you."
prompt += "\nTo exit write 'quit' and then press Enter: "
msg = ''
while active:
    msg = input(prompt)
    if msg != 'quit':
        print(f"\nYou said: {msg}")
    else:
        active = False
        print(f"\nGoodbye!")



#break statement
numbers = [2, 3, 4, 67, 89, 90, 45]
MAX_TRY = 5
current_try = 1
active = True
prompt = "Guess a number or input 'quit' to exit: "
my_number = input(prompt)
while active:
    if int(my_number) in numbers:
        print("Good guess!")
        break
    elif my_number == 'quit':
        break
    elif current_try == MAX_TRY:
        print("No more try left.")
        active = False
    else:
        current_try += 1
        my_number = input("Try again or enter 'quit' to exit: ")


#continue statement
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
        i += 1
        continue
    else:
        i += 1
    



# If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal 
# window displaying your program’s output.

#A for loop is effective for looping through a list, but you shouldn’t modify a list 
# inside a for loop because Python will have trouble keeping track of the items in 
# the list. To modify a list as you work through it, use a while loop. Using while 
# loops with lists and dictionaries allows you to collect, store, and organize lots 
# of input to examine and report on later.

cars = ["bmw", "toyota", "kia", "mercedes"]
chosen_cars = []
print(cars)

while cars:
    chosen_car = cars.pop() #move the last one
    chosen_cars.append(chosen_car)
print(cars)
print(chosen_cars)


pets = ["dog", "monkey", "cat", "parrot", "monkey", "turtle", "fish", "monkey"]
print(pets)
while "monkey" in pets:
    pets.remove("monkey")
print(pets) #all monkeys are removed
''' #So, that above line don't execute, an alternative of multiline comment

polling_active = True
responses = {}
while polling_active:
    name = input("What is your name? ")
    color = input("What is your favorite color? ") 
    responses[name] = color

    repeat = input("Any other person want to response (yes/no)? " )
    if repeat == "no":
        polling_active = False

print(responses)
