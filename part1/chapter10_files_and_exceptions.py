'''
with open("pi_digits.txt") as x:
    contents = x.read()
print(contents)

#The keyword with closes the file once access to it is no longer needed. 
# Notice how we call open() in this program but not close(). 
# You could open and close the file by calling open() and close(), 
# but if a bug in your program prevents the close() method from being executed, 
# the file may never close. This may seem trivial, but improperly 
# closed files can cause data to be lost or corrupted. And if you 
# call close() too early in your program, you’ll find yourself trying 
# to work with a closed file (a file you can’t access), which leads 
# to more errors. It’s not always easy to know exactly when you should 
# close a file, but with the structure shown here, Python will figure 
# that out for you. All you have to do is open the file and work with it as 
# desired, trusting that Python will close it automatically when the 
# with block finishes execution.

#The only difference between this output and the original file is the extra blank line at the end of the output. 
# The blank line appears because read() returns an empty string when it reaches the end of the file; 
# this empty string shows up as a blank line.

print(contents.rstrip())

print("--------------------------------------------")
print("\n")
with open("data/pi_digits.txt") as x:
    contents = x.read()
print(contents)
print("\n")


#If you try to use backslashes in a file path, you’ll get an error because the backslash 
# is used to escape characters in strings. For example, in the path "C:\path\to\file.txt", 
# the sequence \t is interpreted as a tab. If you need to use backslashes, you can escape 
# each one in the path, like this: "C:\\path\\to\\file.txt".

print("--------Print line by line------------------------------------")
print("\n")
file_path = 'data/pi_digits.txt'
with open(file_path) as file_obj:
    for l in file_obj:
        print(l)
print("\n")

print("--------Accessing from outside the with block------------------------------------")
print("\n")

file_path = 'data/pi_digits.txt'
with open(file_path) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line)

print("\n")

#The readlines() method takes each line from the file and stores it in a list. 
# This list is then assigned to lines, which we can continue to work 
# with after the with block ends.

print("--------Working with file contents------------------------------------")
print("\n")

file_path = 'data/pi_digits.txt'
with open(file_path) as file_obj:
    lines = file_obj.readlines()

pi = ''
for line in lines:
    pi += line.rstrip()

print(pi)

print("\n")

#When Python reads from a text file, it interprets all text in the file as a string. 
# If you read in a number and want to work with that value in a numerical context, 
# you’ll have to convert it to an integer using the int() function or convert it to a 
# float using the float() function.


with open("test.txt", "w") as fo:
    fo.write("I love programming")

with open("test.txt") as fo:
    my_text = fo.read()

print(my_text)


#The open() function automatically creates the file you’re writing to if it doesn’t already 
# exist. However, be careful opening a file in write mode ('w') because if the 
# file does exist, Python will erase the contents of the file before returning the file object.

with open("test2.txt", "w") as ftw: #write
    ftw.write("First line.\n")
    ftw.write("Second line.\n")

with open("test2.txt") as ftr:
    print(ftr.read())


with open("test2.txt", "a") as ftw: #append
    ftw.write("Third line.\n")
    ftw.write("Fourth line.\n")

with open("test2.txt") as ftr:
    print(ftr.read())



#Exception handling
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
        #print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


#The try-except-else block works like this: Python attempts to run the code in the try block. 
# The only code that should go in a try block is code that might cause an exception to be raised. 
# Sometimes you’ll have additional code that should run only if the try block was successful; 
# this code goes in the else block. The except block tells Python what to do in case a certain 
# exception arises when it tries to run the code in the try block.

filename = "alice.txt"

try:
    with open(filename, encoding = "utf-8") as f:
        f.read()
#except:
except FileNotFoundError:
    print(f"{filename.title()} not found!")

   
title = "Alice in Wonderland"
words = title.split()
for word in words:
    print(word)
print (f"Total words: {len(words)}")


filename = "alice.txt"

try:
    with open(filename, encoding = "utf-8") as f:
        content = f.read()
#except:
except FileNotFoundError:
    print(f"{filename.title()} not found!")

words = content.split()
print(f"Total words: {len(words)}") #17843

 

def count_words(file_name):
    try:
        with open(file_name, encoding = "utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{file_name.title()} not found!")
    else:
        words = content.split()
        print(f"Total words: {len(words)}")

#count_words("alice.txt")

books = ["alice.txt", "moby_dick.txt", "siddhartha.txt", "pride_prejudice.txt"]
for book in books:
    print(f"{book}:")
    count_words(book)


#Failing silently - intentional
def count_words(file_name):
    try:
        with open(file_name, encoding = "utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        #print(f"{file_name.title()} not found!")
        pass
    else:
        words = content.split()
        print(f"Total words: {len(words)}")

#count_words("alice.txt")

books = ["alice.txt", "moby_dick.txt", "siddhartha.txt", "pride_prejudice.txt"]
for book in books:
    #print(f"{book}:")
    count_words(book)


import json
numbers = [3, 9, 67, 8, 14, 23]
file_name = "numbers.json"
#write
with open(file_name, "w") as f:
    json.dump(numbers, f)

#read
with open(file_name) as f:
    n = json.load(f)
    print(n)


import json
# Load the username, if it has been stored previously.   
# Otherwise, prompt for the username and store it.   
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f) 
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")


#refactoring
import json
# Load the username, if it has been stored previously.   
# Otherwise, prompt for the username and store it.  
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f) 
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

#Call the function 
greet_user()

'''

#further refactor

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

