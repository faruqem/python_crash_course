#import all functions
'''
import my_library

user1 = my_library.build_user_profile("Mo", "Faruqe", dept = "IT", location = "Toronto")
user2 = my_library.build_user_profile("Mo", "Faruqe")
print(user1)
print(user2)



#import specfic function(s)
from my_library import build_user_profile, baloons_order

baloons_order("red") #library name prefix is not necessary now to call a function
baloons_order("red", "green")
baloons_order("red", "green", "yellow")



#Using as to Give a Function an AliasIf the name of a function you’re 
# importing might conflict with an existing name in your program or if the function name 
# is long, you can use a short, unique alias—an alternate name similar to a nickname 
# for the function. You’ll give the function this special nickname when you import the function.

from my_library import build_user_profile, baloons_order as bo

bo("red") 
bo("red", "green")
bo("red", "green", "yellow")

# Using as to Give a Module an Alias
# You can also provide an alias for a module name.
import my_library as ml
ml.baloons_order("red") #library name prefix is not necessary now to call a function
ml.baloons_order("red", "green")
ml.baloons_order("red", "green", "yellow")

'''
# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the asterisk (*) operator:
#The asterisk in the import statement tells Python to copy every function 
# from the module pizza into this program file. Because every function is imported, 
# you can call each function by name without using the dot notation. However, it’s 
# best not to use this approach when you’re working with larger modules that you 
# didn’t write: if the module has a function name that matches an existing name 
# in your project, you can get some unexpected results. Python may see several functions 
# or variables with the same name, and instead of importing all the functions separately, 
# it will overwrite the functions.
# The best approach is to import the function or functions you want, 
# or import the entire module and use the dot notation. This leads to clear 
# code that’s easy to read and understand. 

from my_library import *
baloons_order("red") #library name prefix is not necessary now to call a function
baloons_order("red", "green")
baloons_order("red", "green", "yellow")

#Styling Functions
# You need to keep a few details in mind when you’re styling functions. 
# Functions should have descriptive names, and these names should use lowercase letters 
# and underscores. Descriptive names help you and others understand what your code is trying to do. 
# Module names should use these conventions as well.Every function should have a comment that 
# explains concisely what the function does. This comment should appear immediately after 
# the function definition and use the docstring format. In a well-documented function, 
# other programmers can use the function by reading only the description in the docstring. 
# They should be able to trust that the code works as described, and as long as they know the name 
# of the function, the arguments it needs, and the kind of value it returns, 
# they should be able to use it in their programs.If you specify a default value 
# for a parameter, no spaces should be used on either side of the equal sign:
# def function_name(parameter_0, parameter_1='default value')
# The same convention should be used for keyword arguments in function calls:
# function_name(value_0, parameter_1='value')PEP 8 (https://www.python.org/dev/peps/pep-0008/) 
# recommends that you limit lines of code to 79 characters so every line is visible in a reasonably 
# sized editor window. If a set of parameters causes a function’s definition to be longer than 
# 79 characters, press ENTER after the opening parenthesis on the definition line. 
# On the next line, press TAB twice to separate the list of arguments from the body of the f
# unction, which will only be indented one level.

#If your program or module has more than one function, you can separate each by two blank 
# lines to make it easier to see where one function ends and the next one begins.
# All import statements should be written at the beginning of a file. The only exception is 
# if you use comments at the beginning of your file to describe the overall program.