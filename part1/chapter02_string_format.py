print("Hello World")

name = "mo faruqe"
print(name.title())

#formatting
#f-strings, f is for format
first_name = "Mo"
last_name = "Faruqe"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

old_full_name = "{} {}".format(first_name,last_name) #f replaced old method format()
print(old_full_name)

print("Languages: \n\tPython \n\tJava \n\tC++ \nare my favorites")

#remove white space
name = ' faruqe '
print(name)
name = name.lstrip().rstrip() #Equivalent to name.strip()
print(name)

print('He said, "How are you?"')

print(2**2)
print(14_000_000_000) #python ignores underscore

x,y,z = 10,20,30
print(f"x = {x}, y= {y}, z= {z}")

#constant
PI = 3.141
print(PI)

#The Zen of Python, by Tim Peters
import this
#Since Python will ignore string literals that are not assigned to a variable, 
#you can add a multiline string (triple quotes) in your code, and place your comment inside it:
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
"""