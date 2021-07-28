colors = ["red","blue","yellow","black","white","magenta","skyblue","gray","green"]
for color in colors: 
    print(color)

print("--------------------------------------------")
#Every indented line following the line for magician in magicians is considered inside the loop
colors = ["red","blue","yellow","black","white","magenta","skyblue","gray","green"]
for color in colors: 
    print(color)
    print(f"My fav color is {color.title()}\n")

print("--------------------------------------------")
#range function
for v in range(1, 6):
    print(v) #print 1 to 6-1

print("--------------------------------------------")
#range to list
mylist = list(range(1,6))
print(mylist)

evennumbers = list(range(2,11,2))
print(evennumbers)

print("--------------------------------------------")
squares = []
for num in range(1,11):
    square = num ** 2
    squares.append(square)
print(squares)

#list functions
nums = [2, 4 , 8, 15, 19, 32]
print(min(nums))
print(max(nums))
print(sum(nums))

print("--------------------------------------------")
#list comprhensions
squares = [num**2 for num in range(1,10)]
print(squares)


#slice
print("--------------------------------------------")
colors = ["red","blue","yellow","black","white","magenta","skyblue","gray","green"]
print(colors[0:3])
print(colors[1:3])
print(colors[:3])
print(colors[3:])
print(colors[-3:])

for color in colors[5:]:
    print(color)

print("--------------------------------------------")
my_colors = colors[0:5]
print(my_colors)

my_colors2 = colors[:] #This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list
print(my_colors2)

print("--------------------------------------------")
my_colors3 = colors
print(my_colors3)

colors.append("pink")
print(colors)
print(my_colors2) #colors and colors 2 are pointing to the different variables since slice is used in copying colors to colors2
print(my_colors3) #colors and colors 3 are pointing to the same variable since no slice is used in copying in copying colors to colors3

print("--------------------------------------------")
#tuples
#tuples are immutable lists i.e. once defined their membership can't be changed
colors_touple = ("red","blue","yellow","black","white","magenta","skyblue","gray","green") #parenthesis instead of bracket
print(colors_touple)
print(colors_touple[3])
print(colors_touple[0:3])
#colors_touple[3] = "new_color" #not allowed, will throw error becuase it's touple

#Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. 
# If you want to define a tuple with one element, you need to include a trailing comma:
single_touple = ("yellow,")

for color in colors_touple:
    print(color)

print("--------------------------------------------")
#writing over a touple
#you can't change ut you can redefine a touple keeping the same variable name
colors_touple = ("red","blue","magenta","yellow","black","white")
for color in colors_touple:
    print(color)

 #https://python.org/dev/peps/pep-0008/